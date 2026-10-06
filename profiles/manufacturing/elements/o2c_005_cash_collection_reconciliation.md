---
id: o2c_005_cash_collection_reconciliation
type: process_step
name: Cash Collection & Accounts Receivable Reconciliation
version: 1.0.0
lifecycles: [O2C]
lod_support: [tier_1, tier_2, tier_3]
tags: [treasury, cash_application, ar, reconciliation, banking]

raci:
  responsible: [role_billing_specialist]
  accountable: [role_finance_controller]
  consulted: [role_customer]
  informed: [role_sales_ops_specialist]

daci:
  driver: [role_billing_specialist]
  approver: [role_finance_controller]
  contributor: [role_customer]
  informed: [role_sales_ops_specialist]

attributes:
  baseline_cycle_time_hours: 8.0
  baseline_cost_per_unit: 12.00
  automation_rate: 0.85
  error_rate: 0.01
  sla_hours: 24.0

asset_dependencies:
  - asset_erp_system
  - asset_payment_gateway

graph_relations:
  - relation: feeds_into
    target: r2r_001_journal_entry_recording
    weight: 0.90
  - relation: governed_by
    target: sod_spending_limits_policy
    weight: 0.95
---

# Process Step: Cash Collection & Accounts Receivable Match

## Executive Summary
Matches inbound electronic bank remittances (ACH, wire, credit card) against open customer invoices, applies payment settlements, and resolves deductions or short-payment exceptions.

## 1. Strategic Intent & Outcome (Tier 1 - Executive Level)
- **Business Value**: Optimizes cash liquidity, minimizes unapplied cash balances, and ensures rapid restoration of customer credit availability.
- **Strategic Alignment**: Directly drives operating cash flow (OCF), working capital velocity, and bad debt reserve reduction.
- **Risk Exposure**: Unapplied cash backlogs, unearned discount taking by clients, or undetected customer solvency crises.

## 2. Operational Workflow & RACI (Tier 2 - Process Architect Level)
- **Workflow Sequence**:
  1. Electronic bank statements (BAI2 / ISO 20022 CAMT.053) received daily via `asset_payment_gateway`.
  2. Cash application engine automatically reconciles remittance advice against open invoice numbers.
  3. Fully matched line items post clearing entries, clearing Accounts Receivable and debiting Operating Cash.
  4. Discrepancies (unidentified deposits, short-payments) route to AR specialist for deduction management.
- **RACI Assignment Matrix**:
  - **Responsible**: `role_billing_specialist`
  - **Accountable**: `role_finance_controller`
  - **Consulted**: `role_customer`
  - **Informed**: `role_sales_ops_specialist`
- **Service Level Agreement (SLA)**: 24.0 Hours.

## 3. Systems Math & Simulation Parameters (Tier 3 - Simulation Engineer Level)
```math
\text{DSO Reduction Delta} = \frac{\text{Total Open AR}}{\text{Daily Gross Sales}} \times \left(1 - \text{Auto-Match Rate}\right)
```
- **Primary Data Entity**: Remittance Clearing Voucher (`CASH_SETTLEMENT_v1`).
- **Asset Load**: Inbound bank feed processed via `asset_payment_gateway` and matched into `asset_erp_system`.
