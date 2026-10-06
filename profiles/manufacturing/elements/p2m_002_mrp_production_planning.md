---
id: p2m_002_mrp_production_planning
type: process_step
name: "Material Requirements Planning (MRP)"
version: "1.0.0"
lifecycles: ["P2M"]
lod_support: ["tier_1", "tier_2", "tier_3"]
tags: ["supply_chain", "planning", "mrp"]

raci:
  responsible: [role_production_scheduler]
  accountable: [role_production_scheduler]
  consulted: [role_inventory_manager]
  informed: [role_procurement_specialist]

attributes:
  baseline_cycle_time_hours: 24.0
  baseline_cost_per_unit: 15.0
  automation_rate: 0.95
  error_rate: 0.02
  sla_hours: 48.0
  volume_per_period: 100
  capacity_fte: 1.0

asset_dependencies:
  - asset_erp_system
  - asset_aps_planner

graph_relations:
  - relation: feeds_into
    target: p2m_003_production_order_release
    weight: 1.0
  - relation: triggers
    target: s2p_001_spend_analysis_need_id
    weight: 0.30

compensating_control: "Plant Manager reviews finite capacity constraints before confirming the Master Production Schedule (MPS)."
---

# Process Step: Material Requirements Planning (MRP)

## Executive Summary
Explodes the consensus demand forecast through the Bill of Materials (BOM) to determine exact raw material requirements and sub-assembly schedules.

## 1. Strategic Intent & Outcome (Tier 1 - Executive Level)
- **Business Value**: Ensures the right materials are available at the right time for factory consumption.
- **Risk Exposure**: Misconfigured BOMs or lead-time data causing line stoppages due to missing components.

## 2. Operational Workflow (Tier 2)
- ERP engine runs overnight MRP batch job against the forecast and current inventory.
- Scheduler reviews planned orders and exception messages (expedite/defer).
- MRP triggers purchase requisitions (`s2p_001`) for missing raw materials.
- Master Production Schedule (MPS) is finalized.
