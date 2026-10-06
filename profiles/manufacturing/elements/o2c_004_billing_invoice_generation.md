---
id: o2c_004_billing_invoice_generation
type: process_step
name: Customer Billing & Electronic Invoicing
version: 1.0.0
lifecycles: [O2C]
lod_support: [tier_1, tier_2, tier_3]
tags: [billing, invoicing, revenue, accounting]

raci:
  responsible: [role_billing_specialist]
  accountable: [role_finance_controller]
  consulted: [role_sales_ops_specialist]
  informed: [role_customer]

daci:
  driver: [role_billing_specialist]
  approver: [role_finance_controller]
  contributor: [role_sales_ops_specialist]
  informed: [role_customer]

attributes:
  baseline_cycle_time_hours: 2.0
  baseline_cost_per_unit: 6.50
  automation_rate: 0.95
  error_rate: 0.005
  sla_hours: 4.0

asset_dependencies:
  - asset_erp_system
  - asset_crm_system

graph_relations:
  - relation: feeds_into
    target: o2c_005_cash_collection_reconciliation
    weight: 1.0
  - relation: governed_by
    target: sod_spending_limits_policy
    weight: 0.90
---

# Process Step: Customer Billing & Electronic Invoicing

## Executive Summary
Generates legally compliant tax invoices upon confirmation of delivery, determines jurisdiction sales taxes, and dispatches electronic invoices via EDI, customer portals, or Peppol e-delivery.

## 1. Strategic Intent & Outcome (Tier 1 - Executive Level)
- **Business Value**: Accelerates revenue recognition, shortens billing cycles, and minimizes Days Sales Outstanding (DSO).
- **Strategic Alignment**: Directly aligns with ASC 606 revenue recognition standards, global e-invoicing mandates, and statutory tax compliance.
- **Risk Exposure**: Tax jurisdiction determination errors, invoicing disputes, or delivery-to-billing lead time leakage.

## 2. Operational Workflow & RACI (Tier 2 - Process Architect Level)
- **Workflow Sequence**:
  1. Post Goods Issue (PGI) event triggers automated billing due-list in `asset_erp_system`.
  2. Automated Vertex/Avalara tax engine computes state, local, or VAT taxes based on ship-to location.
  3. Formal electronic billing document (EDI 810 / XML) generated and dispatched to `role_customer`.
  4. General ledger updates Accounts Receivable asset account and credits earned revenue.
- **RACI Assignment Matrix**:
  - **Responsible**: `role_billing_specialist`
  - **Accountable**: `role_finance_controller`
  - **Consulted**: `role_sales_ops_specialist`
  - **Informed**: `role_customer`
- **Service Level Agreement (SLA)**: 4.0 Hours.

## 3. Systems Math & Simulation Parameters (Tier 3 - Simulation Engineer Level)
```math
\text{Billing Unit Cost} = \text{Baseline Cost} \times (1 + \text{Error Rate}) + \frac{\text{Manual Exception Hours}}{\text{Automation Rate}}
```
- **Primary Data Entity**: Customer Tax Invoice Document (`CUSTOMER_INVOICE_v1`).
- **Asset Load**: Core billing document generated in `asset_erp_system` and archived in `asset_crm_system`.
