---
id: p2m_004_manufacturing_execution
type: process_step
name: "Manufacturing Execution & Yield Tracking"
version: "1.0.0"
lifecycles: ["P2M"]
lod_support: ["tier_1", "tier_2", "tier_3"]
tags: ["manufacturing", "shop_floor"]

raci:
  responsible: [role_manufacturing_supervisor]
  accountable: [role_manufacturing_supervisor]
  consulted: [role_quality_assurance_engineer]
  informed: [role_production_scheduler]

attributes:
  baseline_cycle_time_hours: 48.0
  baseline_cost_per_unit: 1500.0
  automation_rate: 0.40
  error_rate: 0.08
  sla_hours: 96.0
  volume_per_period: 500
  capacity_fte: 50.0

asset_dependencies:
  - asset_mes_system

graph_relations:
  - relation: feeds_into
    target: p2m_005_quality_inspection_release
    weight: 1.0
  - relation: impacted_by
    target: s2p_006_goods_services_receipt
    weight: 1.0

compensating_control: "Automated IIoT sensors halt the line if critical parameters deviate, overriding supervisor input."
---

# Process Step: Manufacturing Execution & Yield Tracking

## Executive Summary
The physical transformation of raw materials into finished goods, consuming labor and machine hours while recording actual yields and scrap rates.

## 1. Strategic Intent & Outcome (Tier 1 - Executive Level)
- **Business Value**: Core value creation step. Converts inputs into sellable revenue-generating products.
- **Risk Exposure**: Machine breakdowns, labor shortages, or poor yields destroying gross margin.

## 2. Operational Workflow (Tier 2)
- Operators clock into the production order in the MES.
- Machines execute routing steps (mixing, assembly, packaging).
- Actual material consumption and scrap are recorded.
- Finished pallets are declared off the end of the line.
