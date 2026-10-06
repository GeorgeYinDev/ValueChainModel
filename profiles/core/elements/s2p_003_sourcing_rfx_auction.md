---
id: s2p_003_sourcing_rfx_auction
type: process_step
name: Strategic Sourcing & RFx Execution
version: 1.0.0
lifecycles: [S2P]
lod_support: [tier_1, tier_2, tier_3]
tags: [sourcing, rfp, rfq, negotiation]

raci:
  responsible: [role_procurement_specialist]
  accountable: [role_category_manager]
  consulted: [role_finance_controller]
  informed: [role_supplier]

attributes:
  baseline_cycle_time_hours: 96.0
  baseline_cost_per_unit: 250.00
  automation_rate: 0.65
  error_rate: 0.02
  sla_hours: 120.0

asset_dependencies:
  - asset_eprocurement_portal

graph_relations:
  - relation: feeds_into
    target: s2p_004_contracting_sla_negotiation
    weight: 1.0
---

# Process Step: Strategic Sourcing & RFx Execution

## Executive Summary
Executes competitive bidding events (RFP, RFQ, e-Auctions) to negotiate optimal commercial terms, pricing structures, and SLA commitments.

## 1. Strategic Intent & Outcome (Tier 1 - Executive Level)
- **Business Value**: Drives competitive cost reduction and secures favorable pricing and delivery terms.
- **Strategic Alignment**: Directly achieves annual procurement savings milestones.
- **Risk Exposure**: Uncompetitive bidding, vendor collusion, or flawed bid evaluation criteria.

## 2. Operational Workflow & RACI (Tier 2 - Process Architect Level)
- **Workflow Sequence**:
  1. RFx payload configured with technical specifications and pricing breakdown requirements.
  2. Bids invited from qualified vendors on `asset_eprocurement_portal`.
  3. Weighted scoring algorithm evaluates commercial proposals and selects awarded vendor.
- **RACI Matrix**:
  - **Responsible**: `role_procurement_specialist`
  - **Accountable**: `role_category_manager`
  - **Consulted**: `role_finance_controller`
  - **Informed**: `role_supplier`
- **SLA**: 120.0 Hours.

## 3. Systems Math & Simulation Parameters (Tier 3 - Simulation Engineer Level)
```math
\text{Sourcing Savings} = \text{Baseline Spend} \times \left(\text{Competition Index} \times 0.08\right)
```
- **Primary Data Entity**: Sourcing Event Award (`RFX_AWARD_v1`).
- **Asset Load**: `asset_eprocurement_portal`.
