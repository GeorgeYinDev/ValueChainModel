---
id: financial_close_reporting_stream
type: value_stream
name: Financial Close, Consolidation & Regulatory Reporting Stream
version: 1.0.0
lifecycles: [R2R]
lod_support: [tier_1, tier_2, tier_3]
tags: [value_stream, record_to_report, financial_close, consolidation, r2r]

raci:
  responsible: [role_general_ledger_accountant, role_consolidation_specialist]
  accountable: [role_finance_controller]
  consulted: [role_internal_auditor]
  informed: [role_internal_auditor]

daci:
  driver: [role_consolidation_specialist]
  approver: [role_finance_controller]
  contributor: [role_general_ledger_accountant, role_internal_auditor]
  informed: [role_internal_auditor]

attributes:
  baseline_cycle_time_hours: 70.0
  baseline_cost_per_unit: 213.00
  automation_rate: 0.76
  error_rate: 0.013
  sla_hours: 120.0

asset_dependencies:
  - asset_erp_system
  - asset_financial_consolidation_system

graph_relations:
  - relation: governed_by
    target: sox_financial_reporting_controls_policy
    weight: 1.0
---

# Value Stream: Record to Report (R2R)

## Executive Summary
Orchestrates the entire corporate financial accounting lifecycle, encompassing subledger transaction feeds, multi-entity intercompany eliminations, balance sheet account substantiation, group close consolidation, and certified external financial disclosures (Steps 001 - 005).

## 1. Strategic Outcomes (Tier 1 - Executive Level)
- **Accelerate Financial Close Velocity**: Compress total global close schedule to under 5 business days (120 hours).
- **Audit & Regulatory Compliance**: Ensure 100% compliance with Sarbanes-Oxley 404, US GAAP, and IFRS standards with zero material weaknesses.
- **Reporting Integrity & Accuracy**: Minimize manual adjustments and eliminate un-reconciled intercompany breaks prior to earnings release.

## 2. Included Steps & RACI Summary (Tier 2 - Process Architect Level)
1. `r2r_001_journal_entry_recording` - General Ledger Journal Recording & Subledger Ingestion
2. `r2r_002_intercompany_reconciliation` - Intercompany Transaction Matching & Elimination
3. `r2r_003_balance_sheet_substantiation` - Balance Sheet Account Substantiation & Reconciliation
4. `r2r_004_financial_close_consolidation` - Financial Close Orchestration & Group Consolidation
5. `r2r_005_statutory_financial_reporting` - Statutory, Tax & Management Financial Reporting
