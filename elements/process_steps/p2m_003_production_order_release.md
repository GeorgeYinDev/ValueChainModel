---
id: p2m_003_production_order_release
type: process_step
name: "Production Order Sequencing & Release"
version: "1.0.0"
lifecycles: ["P2M"]
lod_support: ["tier_1", "tier_2", "tier_3"]
tags: ["manufacturing", "scheduling"]

raci:
  responsible: [role_production_scheduler]
  accountable: [role_manufacturing_supervisor]
  consulted: [role_inventory_manager]
  informed: []

attributes:
  baseline_cycle_time_hours: 8.0
  baseline_cost_per_unit: 10.0
  automation_rate: 0.60
  error_rate: 0.05
  sla_hours: 24.0
  volume_per_period: 500
  capacity_fte: 2.0

asset_dependencies:
  - asset_erp_system
  - asset_mes_system

graph_relations:
  - relation: feeds_into
    target: p2m_004_manufacturing_execution
    weight: 1.0
---

# Process Step: Production Order Sequencing & Release

## Executive Summary
Commits planned orders into active production orders, sequencing them on the shop floor to minimize changeover and setup times.

## 1. Strategic Intent & Outcome (Tier 1 - Executive Level)
- **Business Value**: Maximizes Overall Equipment Effectiveness (OEE) and throughput.
- **Risk Exposure**: Inefficient sequencing causing excessive machine downtime or failure to meet critical customer orders.

## 2. Operational Workflow (Tier 2)
- Scheduler converts planned orders to production orders.
- Orders are sequenced based on physical constraints (e.g., color wheels, allergen washdowns).
- Bill of Materials and routing instructions are dispatched to the MES.
- Components are staged from the warehouse to the line.
