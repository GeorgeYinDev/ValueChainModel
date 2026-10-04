---
id: p2m_006_finished_goods_putaway
type: process_step
name: "Finished Goods Put-Away & ATP Update"
version: "1.0.0"
lifecycles: ["P2M"]
lod_support: ["tier_1", "tier_2", "tier_3"]
tags: ["warehouse", "inventory", "atp"]

raci:
  responsible: [role_inventory_manager]
  accountable: [role_inventory_manager]
  consulted: []
  informed: [role_sales_ops_specialist]

attributes:
  baseline_cycle_time_hours: 4.0
  baseline_cost_per_unit: 10.0
  automation_rate: 0.70
  error_rate: 0.02
  sla_hours: 12.0
  volume_per_period: 475
  capacity_fte: 3.0

asset_dependencies:
  - asset_wms_system
  - asset_erp_system

graph_relations:
  - relation: feeds_into
    target: o2c_003_inventory_allocation_fulfillment
    weight: 1.0

compensating_control: "Automated WMS directed put-away enforces barcode scanning, overriding manual bin placement."
---

# Process Step: Finished Goods Put-Away & ATP Update

## Executive Summary
Physically moves cleared goods into warehouse storage and updates the Available-to-Promise (ATP) inventory ledger so sales can fulfill orders.

## 1. Strategic Intent & Outcome (Tier 1 - Executive Level)
- **Business Value**: Makes the manufactured product instantly available for revenue realization.
- **Risk Exposure**: Misplaced inventory ("phantom inventory") leading to order fulfillment failures.

## 2. Operational Workflow (Tier 2)
- Forklift driver receives put-away task via RF scanner.
- Pallet is scanned and placed in the designated storage bin.
- WMS updates ERP inventory levels.
- ATP quantity is incremented, feeding into the O2C cycle.
