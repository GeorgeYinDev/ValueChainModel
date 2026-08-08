---
id: s2p_008_payment_settlement_disbursement
type: process_step
name: Payment Settlement & Disbursement
version: 1.0.0
lifecycles: [S2P]
lod_support: [tier_1, tier_2, tier_3]
tags: [payment, treasury, disbursement, banking]

raci:
  responsible: [role_accounts_payable_clerk]
  accountable: [role_finance_controller]
  consulted: [role_category_manager]
  informed: [role_supplier]

attributes:
  baseline_cycle_time_hours: 4.0
  baseline_cost_per_unit: 8.50
  automation_rate: 0.95
  error_rate: 0.005
  sla_hours: 8.0

asset_dependencies:
  - asset_erp_system
  - asset_payment_gateway

graph_relations:
  - relation: governed_by
    target: sod_spending_limits_policy
    weight: 1.0
---

# Process Step: Payment Settlement & Disbursement

## Executive Summary
Executes final treasury disbursement runs, transmits ISO 20022 XML files via banking gateway, and sends remittance advice notifications to suppliers.

## 1. Strategic Intent & Outcome (Tier 1 - Executive Level)
- **Business Value**: Optimizes working capital, preserves corporate credit rating, and maintains strong vendor relationships.
- **Strategic Alignment**: Realizes Treasury cash flow forecasting and payment run efficiency targets.
- **Risk Exposure**: Payment fraud, erroneous ACH routing, unauthorized disbursement, or banking gateway transmission failure.

## 2. Operational Workflow & RACI (Tier 2 - Process Architect Level)
- **Workflow Sequence**:
  1. AP Clerk compiles payment proposal batch due according to payment terms (Net 30/60).
  2. Finance Controller reviews batch and performs dual digital signoff.
  3. Encrypted ISO 20022 payment payload transmitted via `asset_payment_gateway` to bank network.
- **RACI Matrix**:
  - **Responsible**: `role_accounts_payable_clerk`
  - **Accountable**: `role_finance_controller`
  - **Consulted**: `role_category_manager`
  - **Informed**: `role_supplier`
- **SLA**: 8.0 Hours.

## 3. Systems Math & Simulation Parameters (Tier 3 - Simulation Engineer Level)
```math
\text{Disbursement Throughput} = \text{Batch Volume} \times \text{Automation Rate} \times \text{Gateway TPS Limit}
```
- **Primary Data Entity**: Payment Disbursement Record (`DISBURSEMENT_REC_v1`).
- **Asset Load**: `asset_erp_system`, `asset_payment_gateway`.
