---
id: l2s_006_delinquency_workout_ledger_settlement
type: process_step
name: Delinquency Workout & Subledger Reconciliation
version: 1.0.0
lifecycles: [L2S]
lod_support: [tier_1, tier_2, tier_3]
tags: [workout, delinquency, subledger, reconciliation, r2r, l2s]
apqc_pcf_id: "5.2.2.2"

raci:
  responsible: [role_loan_servicing_specialist]
  accountable: [role_finance_controller]
  consulted: [role_chief_credit_officer, role_treasury_operations_officer]
  informed: [role_general_ledger_accountant, role_internal_auditor]

daci:
  driver: [role_loan_servicing_specialist]
  approver: [role_finance_controller]
  contributor: [role_chief_credit_officer, role_treasury_operations_officer]
  informed: [role_general_ledger_accountant, role_internal_auditor]

attributes:
  baseline_cycle_time_hours: 10.0
  baseline_cost_per_unit: 310.0
  automation_rate: 0.70
  error_rate: 0.02
  sla_hours: 24.0
  volume_per_period: 250
  capacity_fte: 5.0

asset_dependencies:
  - asset_core_banking_platform
  - asset_erp_system

graph_relations:
  - relation: feeds_into
    target: r2r_001_journal_entry_recording
    weight: 1.0
  - relation: governed_by
    target: basel_credit_risk_underwriting_policy
    weight: 1.0
---

# Delinquency Workout & Subledger Reconciliation

Manages past-due borrower collections, executes Special Assets workout restructurings or non-accrual transfers, releases perfected collateral liens upon facility payoff, and reconciles daily loan/deposit subledger balances (interest income, fee amortization, principal settlements, and CECL provisions) into the corporate General Ledger.
