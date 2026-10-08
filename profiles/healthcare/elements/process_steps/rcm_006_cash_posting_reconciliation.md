---
id: rcm_006_cash_posting_reconciliation
type: process_step
name: Cash Posting & Subledger Reconciliation
version: 1.0.0
lifecycles: [RCM]
lod_support: [tier_1, tier_2, tier_3]
tags: [cash_posting, reconciliation, subledger, r2r, rcm]

raci:
  responsible: [role_billing_specialist]
  accountable: [role_finance_controller]
  consulted: [role_rcm_director]
  informed: [role_general_ledger_accountant]

daci:
  driver: [role_billing_specialist]
  approver: [role_finance_controller]
  contributor: [role_rcm_director]
  informed: [role_general_ledger_accountant]

attributes:
  baseline_cycle_time_hours: 8.0
  baseline_cost_per_unit: 50.0
  automation_rate: 0.85
  error_rate: 0.02

asset_dependencies:
  - asset_rcm_clearinghouse
  - asset_erp_system

graph_relations:
  - relation: feeds_into
    target: r2r_001_journal_entry_recording
    weight: 1.0
  - relation: governed_by
    target: hipaa_phi_privacy_policy
    weight: 1.0
---

# Cash Posting & Subledger Reconciliation

Matches electronic lockbox and electronic funds transfers (EFT) against 835 remittance data, posts adjustments/contractuals, balances hospital patient accounting subledgers, and posts cash journal entries to the corporate General Ledger.
