import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.resolve()))
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
6. Builds unified knowledge graph (index/<profile>/knowledge_graph.json).
7. Compiles LLM Context Prompts per Business Lifecycle (index/<profile>/llm_context_<lifecycle_id>.md).
"""

import os
import sys
import json
import pathlib
import yaml
import jsonschema
import argparse
import subprocess
from tools.vcm_profiles import resolve_profile, parse_frontmatter, default_profile, list_profiles
from typing import Dict, Any, List, Tuple

def main():
    parser = argparse.ArgumentParser(description="Enterprise Value Chain Validator")
    parser.add_argument("--profile", default=default_profile(), help="Industry profile")
    parser.add_argument("--profiles-root", default="profiles", help="Path to profiles directory")
    parser.add_argument("--list-profiles", action="store_true", help="List available profiles and exit")
    args = parser.parse_args()

    root = pathlib.Path(__file__).parent.parent.resolve()
    schema_dir = root / "schema"
    profiles_root = root / args.profiles_root
    
    if args.list_profiles:
        profs = list_profiles(profiles_root)
        print("Available Enterprise Profiles:")
        for p in profs:
            print(f" - {p.get('profile_id')}: {p.get('name')} (extends: {p.get('extends', [])}, lifecycles: {p.get('lifecycles', [])})")
        return

    if args.profile == "ALL":
        all_profs = [p for p in list_profiles(profiles_root) if p.get("profile_id") != "core"]
        success = True
        for p_info in all_profs:
            p_id = p_info["profile_id"]
            print(f"\n{'='*50}\n Building Profile: {p_id}\n{'='*50}")
            res = subprocess.run(["uv", "run", __file__, "--profile", p_id, "--profiles-root", args.profiles_root], check=False)
            if res.returncode != 0:
                success = False
        
        # generate index/index.html switcher dashboard
        html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Enterprise Value Chain Architecture - Profiles Switcher</title>
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #0f172a; color: #f8fafc; margin: 0; padding: 40px; }
    h1 { font-size: 2rem; color: #38bdf8; margin-bottom: 8px; }
    p.lead { color: #94a3b8; font-size: 1.1rem; margin-bottom: 32px; }
    .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 24px; }
    .card { background: #1e293b; border: 1px solid #334155; border-radius: 12px; padding: 24px; transition: transform 0.2s, border-color 0.2s; }
    .card:hover { transform: translateY(-4px); border-color: #38bdf8; }
    .card h2 { margin-top: 0; font-size: 1.3rem; color: #e2e8f0; }
    .card p { color: #94a3b8; font-size: 0.95rem; line-height: 1.5; }
    .meta { display: flex; flex-wrap: wrap; gap: 8px; margin: 16px 0; }
    .badge { background: #0f172a; border: 1px solid #475569; color: #cbd5e1; padding: 4px 10px; border-radius: 9999px; font-size: 0.8rem; }
    .badge.lc { border-color: #0284c7; color: #38bdf8; }
    .btn { display: inline-block; background: #0284c7; color: #fff; text-decoration: none; padding: 10px 18px; border-radius: 8px; font-weight: 600; font-size: 0.9rem; }
    .btn:hover { background: #0369a1; }
  </style>
</head>
<body>
  <h1>🏛️ Enterprise Value Chain Modeling Profiles</h1>
  <p class="lead">Select an industry profile to inspect its interactive process graph, RACI/DACI governance, system topology, and scenario simulations.</p>
  <div class="grid">
"""
        for p_info in all_profs:
            p_id = p_info["profile_id"]
            p_name = p_info.get("name", p_id)
            p_desc = p_info.get("description", f"Operating model and value streams for {p_name}.")
            p_ext = ", ".join(p_info.get("extends", [])) or "none"
            lcs = p_info.get("lifecycles", [])
            badges_html = "".join([f'<span class="badge lc">{lc}</span>' for lc in lcs])
            html += f"""    <div class="card">
      <h2>{p_name}</h2>
      <p>{p_desc}</p>
      <div class="meta">
        <span class="badge">Extends: {p_ext}</span>
        {badges_html}
      </div>
      <a class="btn" href="{p_id}/value_chain_visualizer.html">Open Visualizer &rarr;</a>
    </div>
"""
        html += """  </div>
</body>
</html>
"""
        (root / "index" / "index.html").write_text(html, encoding="utf-8")
        if not success:
            sys.exit(1)
        return

    try:
        ep = resolve_profile(profiles_root, args.profile, root)
    except Exception as e:
        print(f"❌ Failed to resolve profile '{args.profile}': {e}")
        sys.exit(1)

    index_dir = ep.output_dir
    index_dir.mkdir(parents=True, exist_ok=True)

    print("==================================================")
    print(f" Enterprise Value Chain Validator & Builder [{args.profile}]")
    print(f" Profile Layers: {' -> '.join(ep.layers)}")
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
    for role_id, (role_file, layer) in ep.role_files.items():
        fm, _ = parse_frontmatter(role_file)
        fm["source_layer"] = layer
        role_id = fm.get("id", role_file.stem)
        roles[role_id] = fm
        print(f"  - Ingested Enterprise Role: {role_id} [{layer}]")

    # 2. Ingest Assets
    assets = {}
    for asset_id, (asset_file, layer) in ep.asset_files.items():
        fm, _ = parse_frontmatter(asset_file)
        fm["source_layer"] = layer
        asset_id = fm.get("id", asset_file.stem)
        validate_schema(fm, asset_schema, f"Asset '{asset_id}'")
        assets[asset_id] = fm
        print(f"  - Ingested Enterprise Asset: {asset_id} [{layer}]")

    # 3. Ingest Elements
    elements = {}
    for elem_id, (md_file, layer) in ep.element_files.items():
        fm, body = parse_frontmatter(md_file)
        fm["source_layer"] = layer
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
        print(f"  - Ingested Value Chain Element: {elem_id} ({fm.get('name', 'Unnamed')}) [{layer}]")

    # Apply patches
    for patch in ep.patches:
        target = patch.get("target")
        if target in elements:
            fm = elements[target]["frontmatter"]
            append_data = patch.get("append", {})
            if "lifecycles" in append_data:
                for lc in append_data["lifecycles"]:
                    if lc not in fm.setdefault("lifecycles", []):
                        fm["lifecycles"].append(lc)
            if "graph_relations" in append_data:
                fm.setdefault("graph_relations", []).extend(append_data["graph_relations"])
            if "tags" in append_data:
                for t in append_data["tags"]:
                    if t not in fm.setdefault("tags", []):
                        fm["tags"].append(t)
            if "asset_dependencies" in append_data:
                for a in append_data["asset_dependencies"]:
                    if a not in fm.setdefault("asset_dependencies", []):
                        fm["asset_dependencies"].append(a)
        elif target in roles:
            pass
        elif target in assets:
            pass
        else:
            errors.append(f"Patch target '{target}' not found in profile elements, roles, or assets")

    # 4. Taxonomy & Governance Validation
    valid_lifecycle_ids = {lc["id"] for lc in ep.taxonomy.get("lifecycles", [])}
    valid_elem_types = set(ep.taxonomy.get("element_types", []))
    valid_rel_types = set(ep.taxonomy.get("relation_types", []))

    print("\n[+] Validating graph relationships & RACI assignments...")
    valid_links = 0
    for elem_id, data in elements.items():
        fm = data["frontmatter"]
        
        # Taxonomy checks
        if valid_lifecycle_ids:
            for lc in fm.get("lifecycles", []):
                if lc not in valid_lifecycle_ids:
                    errors.append(f"Element '{elem_id}' references unknown lifecycle '{lc}' not found in profile taxonomy.")

        if valid_elem_types:
            etype = fm.get("type")
            if etype and etype not in valid_elem_types:
                errors.append(f"Element '{elem_id}' has unknown type '{etype}' not defined in taxonomy.")

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
                    rtype = rel.get("relation")
                    if valid_rel_types and rtype and rtype not in valid_rel_types:
                        errors.append(f"Element '{elem_id}' has unknown relation '{rtype}' not defined in taxonomy.")

                    target = rel.get("target")
                    if target == elem_id:
                        errors.append(f"Element '{elem_id}' has a self-referencing relation '{rtype}' to itself.")
                    elif target and target not in elements and target not in assets:
                        errors.append(f"Element '{elem_id}' references non-existent target '{target}'")
                    else:
                        valid_links += 1

    # 5. Build Lifecycle Prompt Context Packs & Validate
    print("\n[+] Generating LLM Context Packs & Validating Lifecycles...")
    parsed_lifecycles = {}
    for lf_id, (lf_file, layer) in ep.lifecycle_files.items():
        lf_manifest = json.loads(lf_file.read_text(encoding="utf-8"))
        lf_manifest["source_layer"] = layer
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
        prompt_content += f"> Profile: `{ep.profile_id}` | Lifecycle ID: `{lf_id}` | Version: `{lf_manifest.get('version')}` | Source Layer: `{layer}`\n"
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
            prompt_content += f"### [{fm.get('name')}] (`{eid}`) [Layer: `{fm.get('source_layer', layer)}`]\n"
            prompt_content += f"- **Type**: `{fm.get('type')}` | **Tags**: `{', '.join(fm.get('tags', []))}`\n"
            prompt_content += f"- **RACI**: `{json.dumps(fm.get('raci', {}))}`\n"
            prompt_content += f"- **Assets**: `{', '.join(fm.get('asset_dependencies', []))}`\n\n"
            prompt_content += edata["body"] + "\n---\n\n"
            
        out_prompt = index_dir / f"llm_context_{lf_id.lower()}.md"
        out_prompt.write_text(prompt_content, encoding="utf-8")
        print(f"  - Generated context pack: {out_prompt.relative_to(root)} ({len(matched_elements)} elements)")

    # Profile manifest requirement check
    for req_lc in ep.manifest.get("lifecycles", []):
        if req_lc not in parsed_lifecycles:
            errors.append(f"Profile '{ep.profile_id}' requires lifecycle manifest for '{req_lc}', but it was not found.")

    # 6. Validate Scenarios
    print("\n[+] Validating Scenario files...")
    for sim_id, (sim_file, layer) in ep.scenario_files.items():
        sim_data = json.loads(sim_file.read_text(encoding="utf-8"))
        sim_data["source_layer"] = layer
        validate_schema(sim_data, scenario_schema, f"Scenario '{sim_file.name}'")
        
        # Check applicable_profiles
        applicable = sim_data.get("applicable_profiles", [])
        if applicable and ep.profile_id not in applicable:
            continue
            
        # Cross-file reference checks for shocks
        for shock in sim_data.get("shocks", []):
            target_id = shock.get("target_element_id")
            if target_id and target_id not in elements and target_id not in assets:
                errors.append(f"Scenario '{sim_file.name}' references non-existent target_element_id '{target_id}'")

    # 7. Build Knowledge Graph Index
    graph_index = {
        "profile": {
            "profile_id": ep.profile_id,
            "name": ep.manifest.get("name", ep.profile_id),
            "layers": ep.layers
        },
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

    # 8. Auto-compile Diagrams and Visualizer
    diagram_script = root / "tools" / "export_diagram.py"
    if diagram_script.exists():
        print("\n[+] Compiling Mermaid Diagrams & Interactive Visualizer...")
        res = subprocess.run(["uv", "run", str(diagram_script), "--profile", args.profile, "--lifecycle", "ALL", "--format", "all"], check=False)
        if res.returncode != 0:
            errors.append(f"Diagram exporter failed with return code {res.returncode}")

    print("\n==================================================")
    if errors:
        print(f"❌ Completed with {len(errors)} errors:")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)
    else:
        print(f"✅ Validation & Build Successful for profile [{args.profile}]! All enterprise models and visualizers in sync.")
        print("==================================================")

if __name__ == "__main__":
    main()
