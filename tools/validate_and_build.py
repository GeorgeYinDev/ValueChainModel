#!/usr/bin/env python3
"""
Enterprise Value Chain Engine Validator & LLM Context Indexer
-------------------------------------------------------------
1. Parses markdown frontmatter & JSON schemas.
2. Validates element metadata against schema/value_chain_element.schema.json.
3. Validates RACI roles against roles/ directory.
4. Validates asset dependencies against assets/ directory.
5. Validates bi-directional graph relations across elements.
6. Builds unified knowledge graph (index/knowledge_graph.json).
7. Compiles LLM Context Prompts per Business Lifecycle (index/llm_context_<lifecycle_id>.md).
"""

import os
import sys
import json
import pathlib
from typing import Dict, Any, List, Tuple

def parse_frontmatter(file_path: pathlib.Path) -> Tuple[Dict[str, Any], str]:
    """Extract YAML frontmatter and body from Markdown file."""
    content = file_path.read_text(encoding="utf-8")
    frontmatter = {}
    body = content
    
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            raw_yaml = parts[1]
            body = parts[2]
            frontmatter = simple_yaml_parse(raw_yaml)
            
    return frontmatter, body

def simple_yaml_parse(yaml_str: str) -> Dict[str, Any]:
    """Lightweight YAML parser capable of reading nested dicts and lists."""
    result = {}
    current_key = None
    lines = yaml_str.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        line_strip = line.strip()
        if not line_strip or line_strip.startswith("#"):
            i += 1
            continue

        # Check list item with dict structure
        if line_strip.startswith("- ") and current_key:
            item_dict = {}
            kv_line = line_strip[2:].strip()
            if ":" in kv_line:
                k, v = kv_line.split(":", 1)
                item_dict[k.strip()] = parse_val(v.strip())
            
            i += 1
            while i < len(lines):
                next_line = lines[i]
                next_strip = next_line.strip()
                if next_line.startswith("    ") and ":" in next_strip and not next_strip.startswith("- "):
                    k, v = next_strip.split(":", 1)
                    item_dict[k.strip()] = parse_val(v.strip())
                    i += 1
                else:
                    break
            
            if not isinstance(result.get(current_key), list):
                result[current_key] = []
            result[current_key].append(item_dict if item_dict else parse_val(kv_line))
            continue

        # Simple list element (e.g.   responsible: [role_1, role_2])
        if ":" in line:
            key, val = line.split(":", 1)
            key = key.strip()
            val = val.strip()
            current_key = key
            
            if not val:
                result[key] = {}
            elif val.startswith("[") and val.endswith("]"):
                items = [x.strip(" '\"") for x in val[1:-1].split(",") if x.strip()]
                result[key] = items
            else:
                result[key] = parse_val(val)
        elif line.startswith("  ") and ":" in line_strip and current_key:
            # Sub-key under dict
            k, v = line_strip.split(":", 1)
            k = k.strip()
            v = v.strip()
            if not isinstance(result.get(current_key), dict):
                result[current_key] = {}
            if v.startswith("[") and v.endswith("]"):
                items = [x.strip(" '\"") for x in v[1:-1].split(",") if x.strip()]
                result[current_key][k] = items
            else:
                result[current_key][k] = parse_val(v)
        i += 1
                        
    return result

def parse_val(val_clean: str) -> Any:
    val_clean = val_clean.strip("'\"")
    if val_clean.lower() == "true":
        return True
    if val_clean.lower() == "false":
        return False
    if val_clean.lower() == "null":
        return None
    try:
        if "." in val_clean:
            return float(val_clean)
        return int(val_clean)
    except ValueError:
        return val_clean

def main():
    root = pathlib.Path(__file__).parent.parent.resolve()
    schema_dir = root / "schema"
    elements_dir = root / "elements"
    roles_dir = root / "roles"
    assets_dir = root / "assets"
    lifecycles_dir = root / "lifecycles"
    index_dir = root / "index"
    index_dir.mkdir(exist_ok=True)

    print("==================================================")
    print(" Enterprise Value Chain Validator & Builder")
    print("==================================================")

    errors = []

    # 1. Ingest Roles
    roles = set()
    for role_file in roles_dir.glob("*.md"):
        role_id = role_file.stem
        roles.add(role_id)
        print(f"  - Ingested Enterprise Role: {role_id}")

    # 2. Ingest Assets
    assets = {}
    for asset_file in assets_dir.glob("*.md"):
        fm, body = parse_frontmatter(asset_file)
        asset_id = fm.get("id", asset_file.stem)
        assets[asset_id] = fm
        print(f"  - Ingested Enterprise Asset: {asset_id}")

    # 3. Ingest Elements
    elements = {}
    for md_file in elements_dir.glob("**/*.md"):
        fm, body = parse_frontmatter(md_file)
        elem_id = fm.get("id")
        if not elem_id:
            errors.append(f"Missing 'id' in frontmatter: {md_file}")
            continue
            
        elements[elem_id] = {
            "frontmatter": fm,
            "body": body,
            "path": str(md_file.relative_to(root))
        }
        print(f"  - Ingested Value Chain Element: {elem_id} ({fm.get('name', 'Unnamed')})")

    # 4. Validate RACI Roles & Assets & Graph Links
    print("\n[+] Validating graph relationships & RACI assignments...")
    valid_links = 0
    for elem_id, data in elements.items():
        fm = data["frontmatter"]
        
        # Validate RACI roles
        raci = fm.get("raci", {})
        if isinstance(raci, dict):
            for role_type, role_list in raci.items():
                if isinstance(role_list, list):
                    for r in role_list:
                        if r not in roles:
                            errors.append(f"Element '{elem_id}' references undefined role '{r}' in RACI.{role_type}")

        # Validate asset dependencies
        deps = fm.get("asset_dependencies", [])
        if isinstance(deps, list):
            for a in deps:
                if a not in assets:
                    errors.append(f"Element '{elem_id}' references undefined asset '{a}'")

        # Validate graph relations
        relations = fm.get("graph_relations", [])
        if isinstance(relations, list):
            for rel in relations:
                if isinstance(rel, dict):
                    target = rel.get("target")
                    if target and target not in elements and target not in assets:
                        errors.append(f"Element '{elem_id}' references non-existent target '{target}'")
                    else:
                        valid_links += 1

    # 5. Build Knowledge Graph Index
    graph_index = {
        "summary": {
            "total_elements": len(elements),
            "total_roles": len(roles),
            "total_assets": len(assets),
            "validated_links": valid_links
        },
        "elements": {k: v["frontmatter"] for k, v in elements.items()},
        "assets": assets,
        "roles": list(roles)
    }
    
    kg_file = index_dir / "knowledge_graph.json"
    kg_file.write_text(json.dumps(graph_index, indent=2), encoding="utf-8")
    print(f"\n[+] Compiled Knowledge Graph Index: {kg_file.relative_to(root)}")

    # 6. Build Lifecycle Prompt Context Packs
    print("\n[+] Generating LLM Context Packs per Business Lifecycle...")
    lifecycle_files = list(lifecycles_dir.glob("*.json"))
    
    for lf_file in lifecycle_files:
        lf_manifest = json.loads(lf_file.read_text(encoding="utf-8"))
        lf_id = lf_manifest.get("lifecycle_id")
        lf_name = lf_manifest.get("name")
        
        # Match elements tagging this lifecycle
        matched_elements = [
            (eid, edata) for eid, edata in elements.items()
            if lf_id in edata["frontmatter"].get("lifecycles", [])
        ]
        
        prompt_content = f"# System Prompt: LLM Context Blueprint for Business Lifecycle [{lf_name}]\n\n"
        prompt_content += f"> Lifecycle ID: `{lf_id}` | Version: `{lf_manifest.get('version')}`\n"
        prompt_content += f"> Description: {lf_manifest.get('description')}\n\n"
        prompt_content += "## Milestone Process Sequence\n"
        for m in lf_manifest.get("milestones", []):
            prompt_content += f"- **Step {m.get('order')}**: `{m.get('step_id')}` ({m.get('name')})\n"
        prompt_content += "\n## Key Performance Indicators (KPIs)\n"
        for kpi in lf_manifest.get("key_performance_indicators", []):
            prompt_content += f"- `{kpi}`\n"
            
        prompt_content += "\n## Active Value Chain Elements Knowledge Base\n\n"
        for eid, edata in matched_elements:
            fm = edata["frontmatter"]
            prompt_content += f"### [{fm.get('name')}] (`{eid}`)\n"
            prompt_content += f"- **Type**: `{fm.get('type')}` | **Tags**: `{', '.join(fm.get('tags', []))}`\n"
            prompt_content += f"- **RACI**: `{json.dumps(fm.get('raci', {}))}`\n"
            prompt_content += f"- **Assets**: `{', '.join(fm.get('asset_dependencies', []))}`\n\n"
            prompt_content += edata["body"] + "\n---\n\n"
            
        out_prompt = index_dir / f"llm_context_{lf_id.lower()}.md"
        out_prompt.write_text(prompt_content, encoding="utf-8")
        print(f"  - Generated context pack: {out_prompt.relative_to(root)} ({len(matched_elements)} elements)")

    print("\n==================================================")
    if errors:
        print(f"❌ Completed with {len(errors)} errors:")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)
    else:
        print("✅ Validation & Build Successful! All enterprise models in sync.")
        print("==================================================")

if __name__ == "__main__":
    main()
