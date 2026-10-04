#!/usr/bin/env python3
"""
Enterprise Value Chain Scenario Simulation Engine
--------------------------------------------------
1. Ingests a scenario simulation payload (simulations/<scenario_id>.json).
2. Ingests knowledge graph or process elements.
3. Computes baseline vs shocked metrics (Cycle Time, Cost, Automation, Error Rate).
4. Highlights bottleneck shifts and risk exposure deltas.
5. Generates a markdown simulation report (index/simulation_report_<scenario_id>.md).
"""

import os
import sys
import json
import pathlib
from typing import Dict, Any, List

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 tools/simulate_scenario.py <path_to_scenario.json>")
        sys.exit(1)

    scenario_path = pathlib.Path(sys.argv[1]).resolve()
    root = scenario_path.parent.parent
    index_dir = root / "index"
    kg_file = index_dir / "knowledge_graph.json"

    if not kg_file.exists():
        print("[-] Knowledge graph index not found. Running validator first...")
        val_script = root / "tools" / "validate_and_build.py"
        os.system(f"python3 {val_script}")

    scenario = json.loads(scenario_path.read_text(encoding="utf-8"))
    kg = json.loads(kg_file.read_text(encoding="utf-8"))
    elements = kg.get("elements", {})

    print("==================================================")
    print(f" Value Chain Scenario Simulation: {scenario.get('name')}")
    print("==================================================")
    print(f"Target Lifecycle: {scenario.get('target_lifecycle')}")
    print(f"Description     : {scenario.get('description')}\n")

    shocks = scenario.get("shocks", [])
    shock_map = {}
    for s in shocks:
        tid = s.get("target_element_id")
        if tid not in shock_map:
            shock_map[tid] = []
        shock_map[tid].append(s)

    baseline_total_time = 0.0
    shocked_total_time = 0.0

    baseline_total_cost = 0.0
    shocked_total_cost = 0.0

    report_rows = []

    # Sort elements by ID
    sorted_elem_ids = sorted(elements.keys())

    for eid in sorted_elem_ids:
        elem = elements[eid]
        if scenario.get("target_lifecycle") not in elem.get("lifecycles", []):
            continue
        if elem.get("type") != "process_step":
            continue

        # Extract attributes from nested dict or root level
        attrs = elem.get("attributes", {})
        if not isinstance(attrs, dict):
            attrs = {}

        base_time = attrs.get("baseline_cycle_time_hours", elem.get("baseline_cycle_time_hours", 0.0))
        base_cost = attrs.get("baseline_cost_per_unit", elem.get("baseline_cost_per_unit", 0.0))
        base_auto = attrs.get("automation_rate", elem.get("automation_rate", 1.0))
        base_err = attrs.get("error_rate", elem.get("error_rate", 0.0))

        s_time = base_time
        s_cost = base_cost
        s_auto = base_auto
        s_err = base_err

        if eid in shock_map:
            for s_spec in shock_map[eid]:
                mod = s_spec.get("attribute_modifier")
                mult = s_spec.get("multiplier", 1.0)
                delta = s_spec.get("additive_delta", 0.0)

                if mod == "baseline_cycle_time_hours":
                    s_time = (s_time * mult) + delta
                elif mod == "baseline_cost_per_unit":
                    s_cost = (s_cost * mult) + delta
                elif mod == "automation_rate":
                    s_auto = max(0.0, min(1.0, (s_auto * mult) + delta))
                elif mod == "error_rate":
                    s_err = max(0.0, min(1.0, (s_err * mult) + delta))

        eff_base_time = base_time * (1 + base_err)
        eff_base_cost = base_cost * (1 + base_err)

        eff_s_time = s_time * (1 + s_err)
        eff_s_cost = s_cost * (1 + s_err)

        baseline_total_time += eff_base_time
        shocked_total_time += eff_s_time

        baseline_total_cost += eff_base_cost
        shocked_total_cost += eff_s_cost

        time_delta_pct = ((eff_s_time - eff_base_time) / eff_base_time * 100) if eff_base_time > 0 else 0.0
        cost_delta_pct = ((eff_s_cost - eff_base_cost) / eff_base_cost * 100) if eff_base_cost > 0 else 0.0

        report_rows.append({
            "id": eid,
            "name": elem.get("name"),
            "base_time": eff_base_time,
            "shock_time": eff_s_time,
            "time_delta_pct": time_delta_pct,
            "base_cost": eff_base_cost,
            "shock_cost": eff_s_cost,
            "cost_delta_pct": cost_delta_pct
        })

    # Generate Markdown Simulation Report
    report_md = f"# Scenario Simulation Executive Report\n\n"
    report_md += f"**Scenario**: {scenario.get('name')} (`{scenario.get('scenario_id')}`)\n"
    report_md += f"**Target Lifecycle**: `{scenario.get('target_lifecycle')}`\n\n"
    report_md += f"## Executive Summary & Macro Outcomes\n\n"
    
    total_time_delta_pct = ((shocked_total_time - baseline_total_time) / baseline_total_time * 100) if baseline_total_time > 0 else 0.0
    total_cost_delta_pct = ((shocked_total_cost - baseline_total_cost) / baseline_total_cost * 100) if baseline_total_cost > 0 else 0.0

    report_md += f"| Metric | Baseline | Shocked Scenario | Variance Delta |\n"
    report_md += f"| :--- | :--- | :--- | :--- |\n"
    report_md += f"| **Total Lifecycle Lead Time** | `{baseline_total_time:.1f} hrs` ({baseline_total_time/24.0:.1f} days) | `{shocked_total_time:.1f} hrs` ({shocked_total_time/24.0:.1f} days) | `+{total_time_delta_pct:.1f}%` |\n"
    report_md += f"| **Total Process Cost / Unit** | `${baseline_total_cost:.2f}` | `${shocked_total_cost:.2f}` | `+{total_cost_delta_pct:.1f}%` |\n\n"

    report_md += f"## Element Breakdown & Bottleneck Sensitivity Analysis\n\n"
    report_md += f"| Process Element | Baseline Time | Shocked Time | Time Delta | Baseline Cost | Shocked Cost | Cost Delta |\n"
    report_md += f"| :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n"

    for r in report_rows:
        t_flag = f"🔥 +{r['time_delta_pct']:.0f}%" if r['time_delta_pct'] > 50 else f"+{r['time_delta_pct']:.0f}%"
        c_flag = f"💸 +{r['cost_delta_pct']:.0f}%" if r['cost_delta_pct'] > 50 else f"+{r['cost_delta_pct']:.0f}%"
        report_md += f"| **{r['name']}** (`{r['id']}`) | {r['base_time']:.1f}h | {r['shock_time']:.1f}h | {t_flag} | ${r['base_cost']:.2f} | ${r['shock_cost']:.2f} | {c_flag} |\n"

    report_out_file = index_dir / f"simulation_report_{scenario.get('scenario_id')}.md"
    report_out_file.write_text(report_md, encoding="utf-8")

    print("📊 Simulation Output Summary:")
    print(f"  - Total Lead Time: {baseline_total_time:.1f}h -> {shocked_total_time:.1f}h (+{total_time_delta_pct:.1f}%)")
    print(f"  - Total Unit Cost: ${baseline_total_cost:.2f} -> ${shocked_total_cost:.2f} (+{total_cost_delta_pct:.1f}%)")
    print(f"\n✅ Simulation Report written to: {report_out_file.relative_to(root)}")

if __name__ == "__main__":
    main()
