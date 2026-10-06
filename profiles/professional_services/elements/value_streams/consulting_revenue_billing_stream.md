---
id: consulting_revenue_billing_stream
type: value_stream
name: Consulting Time, Expense & Revenue Billing Stream
version: 1.0.0
lifecycles: [E2C]
lod_support: [tier_1, tier_2, tier_3]
tags: [value_stream, billing, time_and_expense, revenue, professional_services]

raci:
  responsible: [role_consultant, role_billing_specialist]
  accountable: [role_engagement_manager]
  consulted: [role_practice_director]
  informed: [role_finance_controller]

daci:
  driver: [role_billing_specialist]
  approver: [role_engagement_manager]
  contributor: [role_consultant]
  informed: [role_finance_controller]

attributes:
  baseline_cycle_time_hours: 58.0
  baseline_cost_per_unit: 750.0
  automation_rate: 0.52
  error_rate: 0.09
  sla_hours: 72.0

asset_dependencies:
  - asset_psa_system
  - asset_erp_system

graph_relations:
  - relation: governed_by
    target: time_expense_compliance_policy
    weight: 1.0
  - relation: feeds_into
    target: r2r_001_journal_entry_recording
    weight: 1.0
---

# Value Stream: Consulting Time, Expense & Revenue Billing Stream (E2C)

## Executive Summary
Encompasses the operational revenue cycle of professional services engagements, starting with consultant time and expense capture, progressing through client acceptance, and culminating in invoice dispatch and subledger ingestion into corporate General Ledger accounting.

## 1. Strategic Outcomes (Tier 1 - Executive Level)
- **Accelerate Cash Conversion & DSO Reduction**: Shorten cycle times from milestone delivery to invoice issuance and cash collection.
- **Prevent Revenue Leakage & Disputed Invoices**: Enforce pre-invoicing client sign-off to minimize write-offs, credit notes, and invoice revisions.
- **Unified Financial Triad Ingestion**: Direct electronic feeding of professional services invoices into R2R General Ledger journal vouchers (`r2r_001_journal_entry_recording`).

## 2. Included Steps & RACI Summary (Tier 2 - Process Architect Level)
1. `e2c_004_time_expense_entry` - Time & Expense Logging
2. `e2c_005_client_acceptance` - Client Deliverable Review & Acceptance Sign-off
3. `e2c_006_project_billing_invoicing` - Project Invoicing & AR Subledger Ingestion
4. Core Integration: Postings feed directly to `r2r_001_journal_entry_recording` in the core Record-to-Report ledger.

## 3. Systems Math & Quantitative Parameters (Tier 3 - Systems Engineer Level)
```math
\text{Billing Cycle Latency} = \text{TimeEntryToApproval} + \text{ClientSignoffLag} + \text{InvoiceBatchProcessing}
```
- **Primary Operational Assets**: Professional Services Automation (`asset_psa_system`), Core ERP Financial Ledger (`asset_erp_system`).
- **Automation Pipeline**: 52% baseline automated workflow from approved timesheets to draft ERP invoices.
