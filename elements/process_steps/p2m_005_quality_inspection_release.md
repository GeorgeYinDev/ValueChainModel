---
id: p2m_005_quality_inspection_release
type: process_step
name: "Quality Inspection & Batch Release"
version: "1.0.0"
lifecycles: ["P2M"]
lod_support: ["tier_1", "tier_2", "tier_3"]
tags: ["manufacturing", "quality"]

raci:
  responsible: [role_quality_assurance_engineer]
  accountable: [role_quality_assurance_engineer]
  consulted: [role_manufacturing_supervisor]
  informed: [role_inventory_manager]

attributes:
  baseline_cycle_time_hours: 24.0
  baseline_cost_per_unit: 50.0
  automation_rate: 0.30
  error_rate: 0.01
  sla_hours: 48.0
  volume_per_period: 500
  capacity_fte: 5.0

asset_dependencies:
  - asset_erp_system
  - asset_mes_system

graph_relations:
  - relation: feeds_into
    target: p2m_006_finished_goods_putaway
    weight: 0.95
  - relation: exception_to
    target: p2m_004_manufacturing_execution
    weight: 1.0
    probability: 0.05

compensating_control: "QA Director signs off on any out-of-spec batches released under a deviation allowance."
---

# Process Step: Quality Inspection & Batch Release

## Executive Summary
Verifies that manufactured goods meet all engineering and regulatory specifications before they are allowed into sellable inventory.

## 1. Strategic Intent & Outcome (Tier 1 - Executive Level)
- **Business Value**: Protects brand reputation and prevents costly customer returns or regulatory recalls.
- **Risk Exposure**: Releasing defective products to the market, or delaying good product in quarantine.

## 2. Operational Workflow (Tier 2)
- Samples are drawn from the finished batch.
- Physical, chemical, or functional testing is performed.
- Batch is designated as 'Unrestricted Use', 'Blocked', or 'Scrap'.
- Blocked items route back to manufacturing for rework if possible.
