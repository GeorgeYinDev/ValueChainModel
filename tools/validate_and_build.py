#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "jsonschema",
#     "pyyaml",
# ]
# ///
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
import yaml
import jsonschema
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
            try:
                frontmatter = yaml.safe_load(raw_yaml) or {}
            except yaml.YAMLError as e:
                print(f"YAML Parse Error in {file_path}: {e}")
                sys.exit(1)
            
    return frontmatter, body

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

    # 0. Load Schemas
    try:
        element_schema = json.loads((schema_dir / "value_chain_element.schema.json").read_text(encoding="utf-8"))
        asset_schema = json.loads((schema_dir / "asset_hierarchy.schema.json").read_text(encoding="utf-8"))
        lifecycle_schema = json.loads((schema_dir / "lifecycle_manifest.schema.json").read_text(encoding="utf-8"))
        scenario_schema = json.loads((schema_dir / "scenario_simulation.schema.json").read_text(encoding="utf-8"))
        print("[+] Loaded JSON Schemas")
    except Exception as e:
        print(f"❌ Failed to load JSON schemas: {e}")
        sys.exit(1)

    def validate_schema(instance, schema, label):
        try:
            jsonschema.validate(instance=instance, schema=schema)
        except jsonschema.exceptions.ValidationError as e:
            errors.append(f"Schema Validation Error in {label}: {e.message}")

    # 1. Ingest Roles
    roles = {}
    for role_file in roles_dir.glob("*.md"):
        fm, body = parse_frontmatter(role_file)
        role_id = fm.get("id", role_file.stem)
        roles[role_id] = fm
        print(f"  - Ingested Enterprise Role: {role_id}")

    # 2. Ingest Assets
    assets = {}
    for asset_file in assets_dir.glob("*.md"):
        fm, body = parse_frontmatter(asset_file)
        asset_id = fm.get("id", asset_file.stem)
        validate_schema(fm, asset_schema, f"Asset '{asset_id}'")
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
            
        validate_schema(fm, element_schema, f"Element '{elem_id}'")
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
            
            # Validate Segregation of Duties (SoD)
            resp = set(raci.get("responsible", []))
            acc = set(raci.get("accountable", []))
            overlap = resp.intersection(acc)
            if overlap:
                if not fm.get("compensating_control"):
                    errors.append(f"SoD Conflict in '{elem_id}': Role(s) {list(overlap)} cannot be both Responsible and Accountable without a 'compensating_control' declared.")

            # Validate Thresholds against Role Limits
            threshold = fm.get("attributes", {}).get("approval_threshold_usd", 0.0)
            if threshold > 0.0:
                for acc_role_id in acc:
                    role_limit = roles.get(acc_role_id, {}).get("approval_limit_usd", 0.0)
                    if role_limit < threshold:
                        errors.append(f"Threshold Violation in '{elem_id}': Accountable role '{acc_role_id}' has limit ${role_limit} which is below the step threshold of ${threshold}")

        # Validate or auto-derive DACI roles
        daci = fm.get("daci", {})
        if isinstance(daci, dict) and daci:
            for role_type, role_list in daci.items():
                if isinstance(role_list, list):
                    for r in role_list:
                        if r not in roles:
                            errors.append(f"Element '{elem_id}' references undefined role '{r}' in DACI.{role_type}")
        else:
            # Auto-derive DACI from RACI if not explicitly specified
            fm["daci"] = {
                "driver": fm.get("responsible") or (raci.get("responsible", []) if isinstance(raci, dict) else []),
                "approver": fm.get("accountable") or (raci.get("accountable", []) if isinstance(raci, dict) else []),
                "contributor": fm.get("consulted") or (raci.get("consulted", []) if isinstance(raci, dict) else []),
                "informed": fm.get("informed") or (raci.get("informed", []) if isinstance(raci, dict) else [])
            }

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
                    if target == elem_id:
                        errors.append(f"Element '{elem_id}' has a self-referencing relation '{rel.get('relation')}' to itself.")
                    elif target and target not in elements and target not in assets:
                        errors.append(f"Element '{elem_id}' references non-existent target '{target}'")
                    else:
                        valid_links += 1


    # 6. Build Lifecycle Prompt Context Packs & Validate
    print("\n[+] Generating LLM Context Packs & Validating Lifecycles...")
    lifecycle_files = list(lifecycles_dir.glob("*.json"))
    
    parsed_lifecycles = {}
    for lf_file in lifecycle_files:
        lf_manifest = json.loads(lf_file.read_text(encoding="utf-8"))
        validate_schema(lf_manifest, lifecycle_schema, f"Lifecycle '{lf_file.name}'")
        
        lf_id = lf_manifest.get("lifecycle_id")
        parsed_lifecycles[lf_id] = lf_manifest
        lf_name = lf_manifest.get("name")
        
        # Cross-file reference checks for milestones
        for m in lf_manifest.get("milestones", []):
            step_id = m.get("step_id")
            if step_id and step_id not in elements:
                errors.append(f"Lifecycle '{lf_id}' references non-existent step_id '{step_id}'")
        
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

    # 6.5 Validate Scenarios
    print("\n[+] Validating Scenario files...")
    simulations_dir = root / "simulations"
    for sim_file in simulations_dir.glob("*.json"):
        sim_data = json.loads(sim_file.read_text(encoding="utf-8"))
        validate_schema(sim_data, scenario_schema, f"Scenario '{sim_file.name}'")
        
        # Cross-file reference checks for shocks
        for shock in sim_data.get("shocks", []):
            target_id = shock.get("target_element_id")
            if target_id and target_id not in elements and target_id not in assets:
                errors.append(f"Scenario '{sim_file.name}' references non-existent target_element_id '{target_id}'")

    # 6.8 Build Knowledge Graph Index
    graph_index = {
        "summary": {
            "total_elements": len(elements),
            "total_roles": len(roles),
            "total_assets": len(assets),
            "validated_links": valid_links
        },
        "elements": {k: v["frontmatter"] for k, v in elements.items()},
        "assets": assets,
        "roles": roles,
        "lifecycles": parsed_lifecycles
    }
    
    kg_file = index_dir / "knowledge_graph.json"
    kg_file.write_text(json.dumps(graph_index, indent=2), encoding="utf-8")
    print(f"\n[+] Compiled Knowledge Graph Index: {kg_file.relative_to(root)}")

    # 7. Auto-compile Diagrams and Visualizer
    diagram_script = root / "tools" / "export_diagram.py"
    if diagram_script.exists():
        print("\n[+] Compiling Mermaid Diagrams & Interactive Visualizer...")
        os.system(f"python3 {diagram_script} --lifecycle ALL --format all")

    print("\n==================================================")
    if errors:
        print(f"❌ Completed with {len(errors)} errors:")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)
    else:
        print("✅ Validation & Build Successful! All enterprise models and visualizers in sync.")
        print("==================================================")

if __name__ == "__main__":
    main()
