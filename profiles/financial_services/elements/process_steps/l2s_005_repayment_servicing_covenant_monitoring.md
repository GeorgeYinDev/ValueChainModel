---
id: l2s_005_repayment_servicing_covenant_monitoring
type: process_step
name: Repayment Servicing & Covenant Monitoring
version: 1.0.0
lifecycles: [L2S]
lod_support: [tier_1, tier_2, tier_3]
tags: [servicing, covenants, cecl, interest_accrual, payments, l2s]
apqc_pcf_id: "5.2.2.1"

raci:
  responsible: [role_loan_servicing_specialist, role_credit_underwriter]
  accountable: [role_chief_credit_officer]
  consulted: [role_relationship_manager]
  informed: [role_finance_controller, role_customer]

daci:
  driver: [role_loan_servicing_specialist]
  approver: [role_chief_credit_officer]
  contributor: [role_credit_underwriter, role_relationship_manager]
  informed: [role_finance_controller, role_customer]

attributes:
  baseline_cycle_time_hours: 6.0
  baseline_cost_per_unit: 190.0
  automation_rate: 0.80
  error_rate: 0.02
  sla_hours: 24.0
  volume_per_period: 1200
  capacity_fte: 7.0

asset_dependencies:
  - asset_core_banking_platform
  - asset_loan_origination_system

graph_relations:
  - relation: feeds_into
    target: l2s_006_delinquency_workout_ledger_settlement
    weight: 1.0
  - relation: governed_by
    target: basel_credit_risk_underwriting_policy
    weight: 1.0
---

# Repayment Servicing & Covenant Monitoring

Processes daily interest accruals, SOFR rate resets, and scheduled Principal & Interest (P&I) collections, tracks quarterly borrower financial covenant compliance certificates, and updates ASC 326 Current Expected Credit Loss (CECL) reserve classifications.
