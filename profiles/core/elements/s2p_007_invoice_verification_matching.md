---
id: s2p_007_invoice_verification_matching
type: process_step
name: Invoice 3-Way Matching & Exception Handling
version: 1.0.0
lifecycles: [S2P]
lod_support: [tier_1, tier_2, tier_3]
tags: [invoicing, ap, matching, finance]

raci:
  responsible: [role_accounts_payable_clerk]
  accountable: [role_finance_controller]
  consulted: [role_procurement_specialist]
  informed: [role_supplier]

attributes:
  baseline_cycle_time_hours: 16.0
  baseline_cost_per_unit: 22.00
  automation_rate: 0.75
  error_rate: 0.04
  sla_hours: 24.0

asset_dependencies:
  - asset_erp_system
  - asset_eprocurement_portal

graph_relations:
  - relation: feeds_into
    target: s2p_008_payment_settlement_disbursement
    weight: 1.0
  - relation: exception_to
    target: s2p_006_goods_services_receipt
    weight: 1.0
    probability: 0.15
  - relation: governed_by
    target: sod_spending_limits_policy
    weight: 0.90
---

# Process Step: Invoice 3-Way Matching & Exception Handling

## Executive Summary
Ingests vendor invoices, executes automated 3-way matching (PO, GRN, Invoice line items), and routes price/quantity exceptions for resolution.

## 1. Strategic Intent & Outcome (Tier 1 - Executive Level)
- **Business Value**: Prevents duplicate payments, over-billing, fraudulent invoices, and unearned vendor claims.
- **Strategic Alignment**: Ensures financial ledger integrity and captures early payment cash discounts (e.g. 2/10 Net 30).
- **Risk Exposure**: Manual exception bottlenecks, missed discount windows, late payment penalties, or duplicate disbursements.

## 2. Operational Workflow & RACI (Tier 2 - Process Architect Level)
- **Workflow Sequence**:
  1. Supplier invoice ingested electronically (OCR or e-invoicing portal).
  2. ERP automated engine performs 3-way match across line item quantities, unit prices, and tax rates.
  3. Matched invoices auto-approved; exceptions (> $1,000 variance) routed to AP Clerk for resolution.
- **RACI Matrix**:
  - **Responsible**: `role_accounts_payable_clerk`
  - **Accountable**: `role_finance_controller`
  - **Consulted**: `role_procurement_specialist`
  - **Informed**: `role_supplier`
- **SLA**: 24.0 Hours.

## 3. Systems Math & Simulation Parameters (Tier 3 - Simulation Engineer Level)
```math
\text{Matching Cost} = \text{Baseline Cost} \times (1 - \text{Automation Rate}) + \text{Exception Overhead} \times \text{Error Rate} \times 100.0
```
- **Primary Data Entity**: Verified Invoice Voucher (`INVOICE_VOUCHER_v1`).
- **Asset Load**: `asset_erp_system`, `asset_eprocurement_portal`.
