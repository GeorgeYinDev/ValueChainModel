---
id: sox_financial_reporting_controls_policy
type: control_policy
name: SOX 404 Financial Reporting Internal Controls & Materiality Thresholds Policy
version: 1.0.0
lifecycles: [R2R]
lod_support: [tier_1, tier_2, tier_3]
tags: [policy, sox, compliance, internal_controls, financial_reporting, r2r]

raci:
  responsible: [role_general_ledger_accountant]
  accountable: [role_finance_controller]
  consulted: [role_consolidation_specialist, role_internal_auditor]
  informed: [role_internal_auditor]

daci:
  driver: [role_general_ledger_accountant]
  approver: [role_finance_controller]
  contributor: [role_consolidation_specialist, role_internal_auditor]
  informed: [role_internal_auditor]

attributes:
  baseline_cycle_time_hours: 0.0
  baseline_cost_per_unit: 0.0
  automation_rate: 1.0
  error_rate: 0.0
  sla_hours: 0.0

asset_dependencies:
  - asset_erp_system
  - asset_financial_consolidation_system

---

# Control Policy: SOX 404 Financial Reporting Internal Controls

## Executive Summary
Establishes enterprise internal controls over financial reporting (ICFR) pursuant to Sarbanes-Oxley Act Section 404, defining segregation of duties, journal entry approval thresholds, balance sheet substantiation deadlines, and financial consolidation audit trails.

## 1. Governance Rules & Controls (Tier 1 - Strategic Level)
- **Control 1 (Dual Sign-Off on Manual Journals)**: All non-system manual journal entries exceeding $50,000 USD require explicit electronic dual sign-off from `role_finance_controller` prior to general ledger posting.
- **Control 2 (Segregation of Duties - SoD)**: Under no operational circumstances may the individual creating a journal entry approve or post the identical entry in `asset_erp_system`.
- **Control 3 (Balance Sheet Substantiation Deadline)**: 100% of high-risk balance sheet accounts (cash, inventory, intercompany, debt) must be reconciled with third-party statements by T+3 business days following period-end.
- **Control 4 (Consolidation Elimination Auditability)**: Top-side consolidation adjustments executed in `asset_financial_consolidation_system` must possess documented business justification and formal Controller sign-off.
- **Control 5 (Internal Audit Independent Testing)**: Quarterly independent sampling by `role_internal_auditor` to certify design and operating effectiveness of controls.
