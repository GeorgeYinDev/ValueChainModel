---
id: r2r_002_intercompany_reconciliation
type: process_step
name: Intercompany Transaction Matching & Elimination
version: 1.0.0
lifecycles: [R2R]
lod_support: [tier_1, tier_2, tier_3]
tags: [intercompany, elimination, matching, netting, consolidation]

raci:
  responsible: [role_consolidation_specialist]
  accountable: [role_finance_controller]
  consulted: [role_general_ledger_accountant]
  informed: [role_internal_auditor]

daci:
  driver: [role_consolidation_specialist]
  approver: [role_finance_controller]
  contributor: [role_general_ledger_accountant]
  informed: [role_internal_auditor]

attributes:
  baseline_cycle_time_hours: 12.0
  baseline_cost_per_unit: 35.00
  automation_rate: 0.75
  error_rate: 0.025
  sla_hours: 24.0

asset_dependencies:
  - asset_erp_system
  - asset_financial_consolidation_system

graph_relations:
  - relation: feeds_into
    target: r2r_003_balance_sheet_substantiation
    weight: 1.0
  - relation: governed_by
    target: sox_financial_reporting_controls_policy
    weight: 0.90
---

# Process Step: Intercompany Transaction Matching & Elimination

## Executive Summary
Identifies, matches, and eliminates reciprocal intercompany receivables, payables, revenues, and expenses across corporate legal entities, resolving cross-border FX discrepancies and out-of-balance transaction disputes.

## 1. Strategic Intent & Outcome (Tier 1 - Executive Level)
- **Business Value**: Eliminates artificial internal revenue inflation, guarantees consolidated balance sheet accuracy, and ensures compliance with transfer pricing tax regulations.
- **Strategic Alignment**: Directly drives the acceleration of financial close by eliminating intercompany reconciliation bottlenecks.
- **Risk Exposure**: Unbalanced intercompany balances, cross-border currency conversion friction, tax authority scrutiny, and delayed group reporting.

## 2. Operational Workflow & RACI (Tier 2 - Process Architect Level)
- **Workflow Sequence**:
  1. Automated matching engine in `asset_financial_consolidation_system` extracts intercompany AR/AP and buy/sell transaction pairs from `asset_erp_system`.
  2. Transactional matching rules identify exact invoice references and resolve allowable threshold variances (<$100 USD).
  3. Out-of-balance breaks exceeding materiality thresholds route to local entity accountants for dispute resolution.
  4. Reciprocal intercompany balances are netted and automated bilateral elimination entries are generated for corporate group roll-up.
- **RACI Assignment Matrix**:
  - **Responsible**: `role_consolidation_specialist`
  - **Accountable**: `role_finance_controller`
  - **Consulted**: `role_general_ledger_accountant`
  - **Informed**: `role_internal_auditor`
- **Service Level Agreement (SLA)**: 24.0 Hours.

## 3. Systems Math & Simulation Parameters (Tier 3 - Simulation Engineer Level)
```math
\text{Reconciliation Variance} = \sum |\text{Entity A AR} - \text{Entity B AP} \times \text{FX Spot Rate}|
```
- **Primary Data Entity**: Intercompany Matching Reconciliation Voucher (`IC_RECON_VOUCHER_v1`).
- **Asset Load**: Ingestion from `asset_erp_system` into `asset_financial_consolidation_system`.
