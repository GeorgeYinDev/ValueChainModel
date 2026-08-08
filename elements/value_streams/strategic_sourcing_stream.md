---
id: strategic_sourcing_stream
type: value_stream
name: Strategic Sourcing & Contracting Value Stream
version: 1.0.0
lifecycles: [S2P]
lod_support: [tier_1, tier_2, tier_3]
tags: [value_stream, strategic_sourcing]

raci:
  responsible: [role_category_manager]
  accountable: [role_category_manager]
  consulted: [role_finance_controller]
  informed: [role_supplier]

attributes:
  baseline_cycle_time_hours: 228.0
  baseline_cost_per_unit: 715.00
  automation_rate: 0.55
  error_rate: 0.035
  sla_hours: 312.0

asset_dependencies:
  - asset_eprocurement_portal
  - asset_erp_system

graph_relations:
  - relation: feeds_into
    target: procure_to_pay_stream
    weight: 1.0
---

# Value Stream: Strategic Sourcing & Contracting

## Executive Summary
Encompasses the upstream strategic procurement lifecycle from initial demand identification and vendor qualification through RFx event negotiation and master contract execution (Steps 001 - 004).

## 1. Strategic Outcomes (Tier 1)
- Market competitive pricing discovery.
- Vendor risk mitigation and compliance enforcement.
- Long-term contractual relationship management.

## 2. Included Steps & RACI Summary (Tier 2)
1. `s2p_001_spend_analysis_need_id`
2. `s2p_002_supplier_discovery_qualification`
3. `s2p_003_sourcing_rfx_auction`
4. `s2p_004_contracting_sla_negotiation`
