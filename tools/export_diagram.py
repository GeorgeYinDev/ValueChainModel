#!/usr/bin/env python3
"""
Enterprise Value Chain Diagram & Visualization Exporter
--------------------------------------------------------
Generates:
1. Mermaid Flowcharts (Process Flow, RACI Swimlanes, System Assets) in .mmd and .md
2. Interactive 2D RACI Matrix with Workload & SoD Analysis in index/diagram_raci_matrix.md
3. Consolidated Architecture & Flow Diagrams in index/diagrams_summary.md
4. Executive Standalone Interactive Visualizer Dashboard in index/value_chain_visualizer.html
"""

import os
import sys
import json
import pathlib
import argparse
from typing import Dict, Any, List, Optional, Tuple

def load_data(root: pathlib.Path, profile: str) -> Tuple[Dict[str, Any], Dict[str, Any], List[Dict[str, Any]], Dict[str, str]]:
    """Loads knowledge graph, lifecycles, scenarios, and role display names."""
    index_dir = root / "index" / profile
    kg_file = index_dir / "knowledge_graph.json"

    # If knowledge graph doesn't exist, run validator first
    if not kg_file.exists():
        print("[-] Knowledge graph index not found. Running validator first...")
        val_script = root / "tools" / "validate_and_build.py"
        os.system(f"python3 {val_script}")

    kg_data = json.loads(kg_file.read_text(encoding="utf-8"))

    # Load lifecycles
    lifecycles = {}
    lifecycles_dir = root / "lifecycles"
    if lifecycles_dir.exists():
        for lf in lifecycles_dir.glob("*.json"):
            try:
                data = json.loads(lf.read_text(encoding="utf-8"))
                lifecycles[data.get("lifecycle_id", lf.stem.upper())] = data
            except Exception:
                pass

    # Load scenarios
    scenarios = []
    sim_dir = root / "simulations"
    if sim_dir.exists():
        for sf in sorted(sim_dir.glob("*.json")):
            try:
                data = json.loads(sf.read_text(encoding="utf-8"))
                scenarios.append(data)
            except Exception:
                pass

    # Load role titles from markdown files
    role_titles = {}
    roles_dir = root / "roles"
    if roles_dir.exists():
        for rf in roles_dir.glob("*.md"):
            content = rf.read_text(encoding="utf-8")
            role_id = rf.stem
            title = role_id.replace("role_", "").replace("_", " ").title()
            for line in content.splitlines():
                if line.startswith("# Role Definition:"):
                    title = line.replace("# Role Definition:", "").strip()
                    break
                elif line.startswith("# "):
                    title = line.replace("# ", "").strip()
                    break
            role_titles[role_id] = title

    return kg_data, lifecycles, scenarios, role_titles


def get_element_raci(elem: Dict[str, Any]) -> Dict[str, List[str]]:
    """Helper to reliably extract RACI roles."""
    raci = elem.get("raci", {})
    if not isinstance(raci, dict):
        raci = {}
    
    return {
        "responsible": elem.get("responsible") or raci.get("responsible", []),
        "accountable": elem.get("accountable") or raci.get("accountable", []),
        "consulted": elem.get("consulted") or raci.get("consulted", []),
        "informed": elem.get("informed") or raci.get("informed", [])
    }


def get_element_daci(elem: Dict[str, Any]) -> Dict[str, List[str]]:
    """Helper to extract DACI roles (Driver, Approver, Contributor, Informed)."""
    daci = elem.get("daci", {})
    if not isinstance(daci, dict):
        daci = {}
    raci = elem.get("raci", {})
    if not isinstance(raci, dict):
        raci = {}

    driver = elem.get("driver") or daci.get("driver") or elem.get("responsible") or raci.get("responsible", [])
    approver = elem.get("approver") or daci.get("approver") or elem.get("accountable") or raci.get("accountable", [])
    contributor = elem.get("contributor") or daci.get("contributor") or elem.get("consulted") or raci.get("consulted", [])
    informed = elem.get("informed") or daci.get("informed") or raci.get("informed", [])

    return {
        "driver": driver if isinstance(driver, list) else [driver],
        "approver": approver if isinstance(approver, list) else [approver],
        "contributor": contributor if isinstance(contributor, list) else [contributor],
        "informed": informed if isinstance(informed, list) else [informed]
    }


def get_element_attrs(elem: Dict[str, Any]) -> Dict[str, float]:
    """Helper to extract operational parameters."""
    attrs = elem.get("attributes", {})
    if not isinstance(attrs, dict):
        attrs = {}

    return {
        "cycle_time": float(elem.get("baseline_cycle_time_hours", attrs.get("baseline_cycle_time_hours", 0.0))),
        "cost": float(elem.get("baseline_cost_per_unit", attrs.get("baseline_cost_per_unit", 0.0))),
        "automation": float(elem.get("automation_rate", attrs.get("automation_rate", 1.0))),
        "error_rate": float(elem.get("error_rate", attrs.get("error_rate", 0.0))),
        "sla": float(elem.get("sla_hours", attrs.get("sla_hours", 0.0)))
    }


def sanitize_label(text: str) -> str:
    """Escapes problematic characters for Mermaid node labels."""
    if not text:
        return ""
    return text.replace("&", "&amp;").replace('"', '&quot;')


def get_order_map(kg_data: Dict[str, Any]) -> Dict[str, int]:
    order_map = {}
    for lf_id, lf_manifest in kg_data.get("lifecycles", {}).items():
        for m in lf_manifest.get("milestones", []):
            order_map[m.get("step_id")] = m.get("order", 999)
    return order_map

def generate_mermaid_process_flow(lifecycle_id: str, kg_data: Dict[str, Any], lifecycles: Dict[str, Any]) -> str:
    """Generates Mermaid flowchart diagram for the lifecycle."""
    elements = kg_data.get("elements", {})
    lines = [
        "flowchart TD",
        "  %% Style Classes",
        "  classDef processStep fill:#0f172a,stroke:#38bdf8,stroke-width:2px,color:#f8fafc,rx:8,ry:8;",
        "  classDef controlPolicy fill:#1e1b4b,stroke:#a855f7,stroke-width:2px,stroke-dasharray: 4 4,color:#f3e8ff,rx:4,ry:4;",
        "  classDef valueStream fill:#064e3b,stroke:#34d399,stroke-width:2px,color:#ecfdf5,rx:12,ry:12;",
        ""
    ]

    matched_elems = {
        eid: data for eid, data in elements.items()
        if lifecycle_id == "ALL" or lifecycle_id in data.get("lifecycles", [])
    }

    # Build data-driven phase mapping from lifecycles manifests
    phase_map = {}
    phase_order = []
    phase_meta = {}

    target_lcs = [lifecycle_id] if lifecycle_id != "ALL" and lifecycle_id in lifecycles else list(lifecycles.keys())
    for lc in target_lcs:
        lc_manifest = lifecycles.get(lc, {})
        phases = lc_manifest.get("phases", [])
        if phases:
            for p in phases:
                pid = f"{lc}_{p.get('phase_id')}"
                pname = p.get("name", pid)
                if pid not in phase_meta:
                    phase_meta[pid] = pname
                    phase_order.append(pid)
                for step_id in p.get("milestones", []):
                    phase_map[step_id] = pid
        else:
            pid = f"{lc}_phase"
            pname = f"{lc_manifest.get('name', lc)} Phase"
            if pid not in phase_meta:
                phase_meta[pid] = pname
                phase_order.append(pid)
            for m in lc_manifest.get("milestones", []):
                step_id = m.get("step_id")
                if step_id:
                    phase_map[step_id] = pid

    grouped_steps = {pid: [] for pid in phase_order}
    other_steps = []
    policies = []
    value_streams = []

    order_map = get_order_map(kg_data)
    for eid, data in sorted(matched_elems.items(), key=lambda x: (order_map.get(x[0], 999), x[0])):
        etype = data.get("type", "process_step")
        if etype == "control_policy":
            policies.append((eid, data))
        elif etype == "value_stream":
            value_streams.append((eid, data))
        elif etype == "process_step":
            pid = phase_map.get(eid)
            if pid and pid in grouped_steps:
                grouped_steps[pid].append((eid, data))
            else:
                other_steps.append((eid, data))

    if value_streams:
        lines.append("  subgraph Subgraph_ValueStreams [\"<b>Enterprise Value Streams</b>\"]")
        for eid, data in value_streams:
            name = sanitize_label(data.get("name", eid))
            lines.append(f"    {eid}[[\"<b>Stream: {name}</b><br/><small>{eid}</small>\"]]:::valueStream")
        lines.append("  end\n")

    for pid in phase_order:
        steps = grouped_steps[pid]
        if not steps:
            continue
        display_name = phase_meta[pid]
        clean_pid = "".join(c for c in pid if c.isalnum() or c == "_")
        lines.append(f"  subgraph Subgraph_{clean_pid} [\"<b>{display_name}</b>\"]")
        for eid, data in steps:
            attrs = get_element_attrs(data)
            name = sanitize_label(data.get("name", eid))
            auto_pct = int(attrs['automation']*100)
            label = f"\"<b>{name}</b><br/><small>ID: {eid}</small><br/>⏱ {attrs['cycle_time']}h | 💰 ${attrs['cost']} | ⚡ {auto_pct}% auto\""
            lines.append(f"    {eid}[{label}]:::processStep")
        lines.append("  end\n")

    if other_steps:
        lines.append("  subgraph Subgraph_Other [\"<b>Other Process Steps</b>\"]")
        for eid, data in other_steps:
            attrs = get_element_attrs(data)
            name = sanitize_label(data.get("name", eid))
            label = f"\"<b>{name}</b><br/><small>ID: {eid}</small><br/>⏱ {attrs['cycle_time']}h | 💰 ${attrs['cost']}\""
            lines.append(f"    {eid}[{label}]:::processStep")
        lines.append("  end\n")

    if policies:
        lines.append("  subgraph Subgraph_Governance [\"<b>Governance & Control Policies</b>\"]")
        for eid, data in policies:
            name = sanitize_label(data.get("name", eid))
            lines.append(f"    {eid}([\"<b>Policy: {name}</b><br/><small>{eid}</small>\"]):::controlPolicy")
        lines.append("  end\n")

    lines.append("  %% Process Flows & Policy Linkages")
    for eid, data in matched_elems.items():
        relations = data.get("graph_relations", [])
        if isinstance(relations, list):
            for rel in relations:
                if isinstance(rel, dict):
                    target = rel.get("target")
                    rtype = rel.get("relation")
                    if not target or target == eid:
                        continue
                    if target in matched_elems:
                        if rtype == "feeds_into":
                            lines.append(f"  {eid} --> {target}")
                        elif rtype == "governed_by":
                            lines.append(f"  {eid} -. governed by .-> {target}")
                        else:
                            lines.append(f"  {eid} -. {rtype} .-> {target}")

    return "\n".join(lines)


def generate_mermaid_raci_swimlanes(lifecycle_id: str, kg_data: Dict[str, Any], role_titles: Dict[str, str]) -> str:
    """Generates Mermaid flowchart organized by RACI role swimlanes."""
    elements = kg_data.get("elements", {})
    all_roles = kg_data.get("roles", [])

    lines = [
        "flowchart LR",
        "  %% RACI Swimlanes Styling",
        "  classDef roleLane fill:#0f172a,stroke:#64748b,stroke-width:1px,color:#cbd5e1;",
        "  classDef rNode fill:#1e3a8a,stroke:#60a5fa,stroke-width:2px,color:#eff6ff,rx:6,ry:6;",
        "  classDef aNode fill:#701a75,stroke:#f472b6,stroke-width:2px,color:#fdf2f8,rx:6,ry:6;",
        ""
    ]

    matched_elems = {
        eid: data for eid, data in elements.items()
        if (lifecycle_id == "ALL" or lifecycle_id in data.get("lifecycles", [])) and data.get("type") == "process_step"
    }

    role_to_r = {r: [] for r in all_roles}
    role_to_a = {r: [] for r in all_roles}

    order_map = get_order_map(kg_data)
    for eid, data in sorted(matched_elems.items(), key=lambda x: (order_map.get(x[0], 999), x[0])):
        raci = get_element_raci(data)
        for r in raci["responsible"]:
            if r in role_to_r:
                role_to_r[r].append((eid, data.get("name", eid)))
        for a in raci["accountable"]:
            if a in role_to_a:
                role_to_a[a].append((eid, data.get("name", eid)))

    for r in all_roles:
        r_steps = role_to_r[r]
        a_steps = role_to_a[r]
        if not r_steps and not a_steps:
            continue

        r_title = sanitize_label(role_titles.get(r, r.replace("role_", "").replace("_", " ").title()))
        lines.append(f"  subgraph Sub_{r} [\"<b>{r_title}</b>\"]")
        for eid, name in r_steps:
            node_id = f"{eid}__R"
            s_name = sanitize_label(name)
            lines.append(f"    {node_id}[\"<b>{s_name}</b><br/>Role: <b>Responsible (R)</b>\"]:::rNode")
        for eid, name in a_steps:
            node_id = f"{eid}__A"
            s_name = sanitize_label(name)
            lines.append(f"    {node_id}[\"<b>{s_name}</b><br/>Role: <b>Accountable (A)</b>\"]:::aNode")
        lines.append("  end\n")

    for eid, data in matched_elems.items():
        relations = data.get("graph_relations", [])
        if isinstance(relations, list):
            for rel in relations:
                if isinstance(rel, dict) and rel.get("relation") == "feeds_into":
                    target = rel.get("target")
                    if target and target != eid and target in matched_elems:
                        lines.append(f"  {eid}__R --> {target}__R")

    return "\n".join(lines)


def generate_mermaid_asset_architecture(kg_data: Dict[str, Any]) -> str:
    """Generates Mermaid system architecture diagram."""
    assets = kg_data.get("assets", {})
    elements = kg_data.get("elements", {})

    lines = [
        "flowchart TD",
        "  %% Systems & Assets Styling",
        "  classDef coreAsset fill:#14532d,stroke:#4ade80,stroke-width:2px,color:#f0fdf4,rx:8,ry:8;",
        "  classDef subAsset fill:#064e3b,stroke:#2dd4bf,stroke-width:2px,color:#f0fdfa,rx:6,ry:6;",
        "  classDef stepDep fill:#1e293b,stroke:#94a3b8,stroke-width:1px,color:#e2e8f0,rx:4,ry:4;",
        ""
    ]

    root_assets = [aid for aid, a in assets.items() if not a.get("parent_asset_id")]
    child_assets = [aid for aid, a in assets.items() if a.get("parent_asset_id")]

    lines.append("  subgraph Subgraph_EnterpriseSystems [\"<b>Enterprise Core IT Systems & Assets</b>\"]")
    for aid in root_assets:
        a = assets[aid]
        name = sanitize_label(a.get("name", aid))
        sla = a.get("sla_uptime_percent", 99.9)
        tps = a.get("capacity_max_tps", 0)
        lines.append(f"    {aid}[\"<b>{name}</b><br/><small>Type: {a.get('asset_type')} | SLA: {sla}% | Max TPS: {tps}</small>\"]:::coreAsset")

    for aid in child_assets:
        a = assets[aid]
        name = sanitize_label(a.get("name", aid))
        sla = a.get("sla_uptime_percent", 99.9)
        tps = a.get("capacity_max_tps", 0)
        parent = a.get("parent_asset_id")
        lines.append(f"    {aid}[\"<b>{name}</b><br/><small>Type: {a.get('asset_type')} | SLA: {sla}% | Max TPS: {tps}</small>\"]:::subAsset")
        if parent:
            lines.append(f"    {parent} ==>|integrates with| {aid}")
    lines.append("  end\n")

    asset_to_steps = {aid: [] for aid in assets}
    for eid, data in elements.items():
        if data.get("type") != "process_step":
            continue
        deps = data.get("asset_dependencies", [])
        for d in deps:
            if d in asset_to_steps:
                asset_to_steps[d].append((eid, data.get("name", eid)))

    lines.append("  subgraph Subgraph_ProcessBindings [\"<b>Value Chain Process Workloads</b>\"]")
    for aid, steps in asset_to_steps.items():
        if steps:
            for eid, sname in steps:
                node_id = f"proc_{eid}_{aid}"
                clean_sname = sanitize_label(sname)
                lines.append(f"    {node_id}[\"{clean_sname}\"]:::stepDep")
                lines.append(f"    {node_id} -. runs on .-> {aid}")
    lines.append("  end\n")

    return "\n".join(lines)


def generate_raci_matrix_markdown(lifecycle_id: str, kg_data: Dict[str, Any], role_titles: Dict[str, str]) -> str:
    """Generates detailed 2D RACI Matrix with Workload Analysis in Markdown."""
    elements = kg_data.get("elements", {})
    all_roles = kg_data.get("roles", [])

    matched_elems = {
        eid: data for eid, data in sorted(elements.items())
        if (lifecycle_id == "ALL" or lifecycle_id in data.get("lifecycles", [])) and data.get("type") == "process_step"
    }

    md = [
        f"# Enterprise RACI Governance Matrix [{lifecycle_id}]\n",
        "> **RACI Legend**: **R** = Responsible (Executes) | **A** = Accountable (Approves) | **C** = Consulted (Inputs) | **I** = Informed (Notified)\n",
        "## 1. Value Chain Process RACI Grid\n"
    ]

    role_headers = [role_titles.get(r, r.replace("role_", "").replace("_", " ").title()) for r in all_roles]
    header_line = "| Step ID | Process Step Name | " + " | ".join(role_headers) + " |"
    sep_line = "| :--- | :--- | " + " | ".join([":---:" for _ in all_roles]) + " |"
    md.append(header_line)
    md.append(sep_line)

    workload = {r: {"R": 0, "A": 0, "C": 0, "I": 0} for r in all_roles}

    for eid, data in matched_elems.items():
        raci = get_element_raci(data)
        name = data.get("name", eid)
        row = [f"`{eid}`", f"**{name}**"]

        for r in all_roles:
            badges = []
            if r in raci["responsible"]:
                badges.append("**R**")
                workload[r]["R"] += 1
            if r in raci["accountable"]:
                badges.append("**A**")
                workload[r]["A"] += 1
            if r in raci["consulted"]:
                badges.append("C")
                workload[r]["C"] += 1
            if r in raci["informed"]:
                badges.append("I")
                workload[r]["I"] += 1

            cell = ", ".join(badges) if badges else "-"
            row.append(cell)

        md.append("| " + " | ".join(row) + " |")

    md.append("\n---\n")
    md.append("## 2. Role Workload & Touchpoint Distribution\n")
    md.append("| Enterprise Role | Responsible (R) | Accountable (A) | Consulted (C) | Informed (I) | Total Touchpoints | Operational Load |")
    md.append("| :--- | :---: | :---: | :---: | :---: | :---: | :--- |")

    for r in all_roles:
        stats = workload[r]
        total = stats["R"] + stats["A"] + stats["C"] + stats["I"]
        r_name = role_titles.get(r, r.replace("role_", "").replace("_", " ").title())
        load_badge = "🟢 Low"
        if stats["R"] >= 3 or total >= 6:
            load_badge = "🔴 High (Key Dependency)"
        elif stats["R"] >= 2 or total >= 4:
            load_badge = "🟡 Moderate"

        md.append(f"| **{r_name}** (`{r}`) | {stats['R']} | {stats['A']} | {stats['C']} | {stats['I']} | **{total}** | {load_badge} |")

    md.append("\n---\n")
    md.append("## 3. Segregation of Duties (SoD) & Conflict Analysis\n")
    sod_conflicts = []
    for eid, data in matched_elems.items():
        raci = get_element_raci(data)
        overlap = set(raci["responsible"]).intersection(set(raci["accountable"]))
        if overlap:
            for r in overlap:
                sod_conflicts.append((eid, data.get("name", eid), r))

    if not sod_conflicts:
        md.append("✅ **No Segregation of Duties (SoD) Violations Detected!**")
        md.append("No single enterprise role holds simultaneous *Responsible* (execution) and *Accountable* (approval) authority on any individual process step.\n")
    else:
        md.append("⚠️ **Potential Segregation of Duties (SoD) Overlaps Detected:**\n")
        for eid, name, r in sod_conflicts:
            md.append(f"- **Step `{eid}` ({name})**: Role `{r}` is listed as both Responsible and Accountable.")

    return "\n".join(md)


def generate_daci_matrix_markdown(lifecycle_id: str, kg_data: Dict[str, Any], role_titles: Dict[str, str]) -> str:
    """Generates detailed 2D DACI Decision Matrix with Governance Analysis in Markdown."""
    elements = kg_data.get("elements", {})
    all_roles = kg_data.get("roles", [])

    matched_elems = {
        eid: data for eid, data in sorted(elements.items())
        if (lifecycle_id == "ALL" or lifecycle_id in data.get("lifecycles", [])) and data.get("type") == "process_step"
    }

    md = [
        f"# Enterprise DACI Decision Governance Matrix [{lifecycle_id}]\n",
        "> **DACI Legend**: **D** = Driver (Orchestrates/Leads) | **A** = Approver (Sole Sign-off/Veto) | **C** = Contributor (Advises/Consulted) | **I** = Informed (Notified)\n",
        "## 1. Value Chain Process DACI Grid\n"
    ]

    role_headers = [role_titles.get(r, r.replace("role_", "").replace("_", " ").title()) for r in all_roles]
    header_line = "| Step ID | Process Step Name | " + " | ".join(role_headers) + " |"
    sep_line = "| :--- | :--- | " + " | ".join([":---:" for _ in all_roles]) + " |"
    md.append(header_line)
    md.append(sep_line)

    workload = {r: {"D": 0, "A": 0, "C": 0, "I": 0} for r in all_roles}

    for eid, data in matched_elems.items():
        daci = get_element_daci(data)
        name = data.get("name", eid)
        row = [f"`{eid}`", f"**{name}**"]

        for r in all_roles:
            badges = []
            if r in daci["driver"]:
                badges.append("**D**")
                workload[r]["D"] += 1
            if r in daci["approver"]:
                badges.append("**A**")
                workload[r]["A"] += 1
            if r in daci["contributor"]:
                badges.append("C")
                workload[r]["C"] += 1
            if r in daci["informed"]:
                badges.append("I")
                workload[r]["I"] += 1

            cell = ", ".join(badges) if badges else "-"
            row.append(cell)

        md.append("| " + " | ".join(row) + " |")

    md.append("\n---\n")
    md.append("## 2. Decision Authority & Driver Distribution\n")
    md.append("| Enterprise Role | Driver (D) | Approver (A) | Contributor (C) | Informed (I) | Total Decision Touchpoints | Governance Weight |")
    md.append("| :--- | :---: | :---: | :---: | :---: | :---: | :--- |")

    for r in all_roles:
        stats = workload[r]
        total = stats["D"] + stats["A"] + stats["C"] + stats["I"]
        r_name = role_titles.get(r, r.replace("role_", "").replace("_", " ").title())
        weight_badge = "🟢 Advisory"
        if stats["A"] >= 5:
            weight_badge = "🚨 Key-Person Risk (Concentrated Approver)"
        elif stats["A"] >= 3:
            weight_badge = "🔴 Strategic Approver"
        elif stats["D"] >= 3:
            weight_badge = "🔵 Primary Driver"
        elif stats["A"] >= 1 or stats["D"] >= 1:
            weight_badge = "🟡 Operational Authority"

        md.append(f"| **{r_name}** (`{r}`) | {stats['D']} | {stats['A']} | {stats['C']} | {stats['I']} | **{total}** | {weight_badge} |")

    md.append("\n---\n")
    md.append("## 3. Decision Governance & Single-Approver Rule Analysis\n")
    multi_approvers = []
    for eid, data in matched_elems.items():
        daci = get_element_daci(data)
        if len(daci["approver"]) > 1:
            multi_approvers.append((eid, data.get("name", eid), daci["approver"]))

    if not multi_approvers:
        md.append("✅ **Single Approver Rule Upheld!**")
        md.append("Every decision milestone has exactly one designated Approver (A), preventing consensus deadlock.\n")
    else:
        md.append("⚠️ **Split Approver Authority Detected:**\n")
        for eid, name, apps in multi_approvers:
            md.append(f"- **Step `{eid}` ({name})**: Multiple approvers listed: {', '.join(apps)}.")

    return "\n".join(md)



def generate_interactive_html(
    root: pathlib.Path,
    kg_data: Dict[str, Any],
    lifecycles: Dict[str, Any],
    scenarios: List[Dict[str, Any]],
    role_titles: Dict[str, str],
    mermaid_flow: str,
    mermaid_raci: str,
    mermaid_assets: str
) -> str:
    """Loads HTML template and injects dynamic JSON datasets and Mermaid graphs."""
    tmpl_file = root / "templates" / "visualizer_template.html"
    if not tmpl_file.exists():
        raise FileNotFoundError(f"Template not found at {tmpl_file}")

    template = tmpl_file.read_text(encoding="utf-8")

    lifecycle_ids = sorted(lifecycles.keys())
    if "ALL" not in lifecycle_ids:
        lifecycle_ids.append("ALL")

    mermaid_flows_dict = {}
    mermaid_raci_dict = {}
    for lid in lifecycle_ids:
        mermaid_flows_dict[lid] = generate_mermaid_process_flow(lid, kg_data, lifecycles)
        mermaid_raci_dict[lid] = generate_mermaid_raci_swimlanes(lid, kg_data, role_titles)

    payload_js = (
        f"const elements = {json.dumps(kg_data.get('elements', {}))};\n"
        f"  const assets = {json.dumps(kg_data.get('assets', {}))};\n"
        f"  const roles = {json.dumps(kg_data.get('roles', []))};\n"
        f"  const roleTitles = {json.dumps(role_titles)};\n"
        f"  const scenarios = {json.dumps(scenarios)};\n"
        f"  const lifecycles = {json.dumps(lifecycles)};\n"
        f"  const mermaidFlows = {json.dumps(mermaid_flows_dict)};\n"
        f"  const mermaidRaci = {json.dumps(mermaid_raci_dict)};\n"
        f"  const mermaidAssets = {json.dumps(mermaid_assets)};\n"
    )

    prof_id = kg_data.get("profile", {}).get("profile_id", "manufacturing")
    prof_name = kg_data.get("profile", {}).get("name", prof_id.title())
    html = template.replace("/*__DATA_PAYLOAD__*/", payload_js)
    html = html.replace("__MERMAID_FLOW__", mermaid_flow)
    html = html.replace("__MERMAID_ASSETS__", mermaid_assets)
    html = html.replace("/*__PROFILE_ID__*/", prof_id)
    html = html.replace("/*__PROFILE_NAME__*/", prof_name)

    return html


def main():
    parser = argparse.ArgumentParser(description="Export Mermaid & Interactive HTML Value Chain Diagrams")
    parser.add_argument("--profile", default="manufacturing", help="Industry profile")
    parser.add_argument("--lifecycle", default="S2P", help="Lifecycle ID to filter (e.g. S2P, O2C, ALL)")
    parser.add_argument("--format", default="all", choices=["mermaid", "markdown", "html", "all"], help="Export format")
    parser.add_argument("--output-dir", default="index", help="Output directory path")
    args = parser.parse_args()

    root = pathlib.Path(__file__).resolve().parent.parent
    
    if args.profile == "ALL":
        import subprocess, sys
        sys.path.insert(0, str(root))
        import json
        profiles = []
        p_root = root / "profiles"
        if p_root.exists():
            for p_dir in p_root.iterdir():
                if p_dir.is_dir() and (p_dir / "profile.json").exists():
                    manifest = json.loads((p_dir / "profile.json").read_text(encoding="utf-8"))
                    if manifest.get("profile_id") != "core":
                        profiles.append(manifest.get("profile_id"))
        for p in profiles:
            res = subprocess.run(["uv", "run", __file__, "--profile", p, "--lifecycle", args.lifecycle, "--format", args.format], check=False)
        sys.exit(0)
    
    out_dir = root / "index" / args.profile
    out_dir.mkdir(parents=True, exist_ok=True)

    print("==================================================")
    print(" Enterprise Value Chain Diagram & Visualizer Builder")
    print("==================================================")
    print(f"Target Lifecycle : {args.lifecycle}")
    print(f"Output Directory : {out_dir.relative_to(root)}")
    print(f"Export Format    : {args.format}\n")

    kg_data, lifecycles, scenarios, role_titles = load_data(root, args.profile)

    # 1. Generate Mermaid Diagrams
    mermaid_flow = generate_mermaid_process_flow(args.lifecycle, kg_data, lifecycles)
    mermaid_raci = generate_mermaid_raci_swimlanes(args.lifecycle, kg_data, role_titles)
    mermaid_assets = generate_mermaid_asset_architecture(kg_data)

    if args.format in ["mermaid", "all"]:
        lifecycle_ids = sorted(lifecycles.keys())
        if "ALL" not in lifecycle_ids:
            lifecycle_ids.append("ALL")
        for lid in lifecycle_ids:
            flow_code = generate_mermaid_process_flow(lid, kg_data, lifecycles)
            flow_file = out_dir / f"diagram_process_flow_{lid.lower()}.mmd"
            flow_file.write_text(flow_code, encoding="utf-8")
            print(f"[+] Exported Mermaid Process Flow ({lid}): {flow_file.relative_to(root)}")

            raci_code = generate_mermaid_raci_swimlanes(lid, kg_data, role_titles)
            raci_mmd_file = out_dir / f"diagram_raci_swimlanes_{lid.lower()}.mmd"
            raci_mmd_file.write_text(raci_code, encoding="utf-8")
            print(f"[+] Exported Mermaid RACI Swimlanes ({lid}): {raci_mmd_file.relative_to(root)}")

        asset_mmd_file = out_dir / "diagram_system_architecture.mmd"
        asset_mmd_file.write_text(mermaid_assets, encoding="utf-8")
        print(f"[+] Exported Mermaid Asset Topology: {asset_mmd_file.relative_to(root)}")

    # 2. Generate Markdown RACI/DACI Matrices & Consolidated Diagrams Summary
    if args.format in ["markdown", "all"]:
        raci_md = generate_raci_matrix_markdown(args.lifecycle, kg_data, role_titles)
        raci_md_file = out_dir / "diagram_raci_matrix.md"
        raci_md_file.write_text(raci_md, encoding="utf-8")
        print(f"[+] Exported RACI Governance Matrix: {raci_md_file.relative_to(root)}")

        daci_md = generate_daci_matrix_markdown(args.lifecycle, kg_data, role_titles)
        daci_md_file = out_dir / "diagram_daci_matrix.md"
        daci_md_file.write_text(daci_md, encoding="utf-8")
        print(f"[+] Exported DACI Decision Matrix  : {daci_md_file.relative_to(root)}")

        summary_md = f"""# Enterprise Value Chain Diagrams Summary [{args.lifecycle}]

Auto-generated visualization pack compiled from validated knowledge graph index.

---

## 1. End-to-End Value Chain Process Flowchart
```mermaid
{mermaid_flow}
```

---

## 2. RACI Role Handoff & Swimlane Sequence
```mermaid
{mermaid_raci}
```

---

## 3. Enterprise IT Asset & Infrastructure Topology
```mermaid
{mermaid_assets}
```

---

## 4. RACI Governance & Operational Execution Grid
{raci_md}

---

## 5. DACI Decision Authority Grid
{daci_md}
"""
        summary_md_file = out_dir / "diagrams_summary.md"
        summary_md_file.write_text(summary_md, encoding="utf-8")
        print(f"[+] Exported Consolidated Diagrams: {summary_md_file.relative_to(root)}")

    # 3. Generate Interactive Standalone Executive Visualizer HTML
    if args.format in ["html", "all"]:
        html_content = generate_interactive_html(
            root, kg_data, lifecycles, scenarios, role_titles,
            mermaid_flow, mermaid_raci, mermaid_assets
        )
        html_file = out_dir / "value_chain_visualizer.html"
        html_file.write_text(html_content, encoding="utf-8")
        print(f"[+] Exported Interactive Executive Dashboard: {html_file.relative_to(root)}")

    print("\n==================================================")
    print("✅ All value chain diagrams exported successfully!")
    print("==================================================")

if __name__ == "__main__":
    main()
