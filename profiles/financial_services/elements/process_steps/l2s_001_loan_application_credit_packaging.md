---
id: l2s_001_loan_application_credit_packaging
type: process_step
name: Loan Application & Credit Packaging
version: 1.0.0
lifecycles: [L2S]
lod_support: [tier_1, tier_2, tier_3]
tags: [loan_origination, credit_memo, spreading, lending, l2s]
apqc_pcf_id: "5.2.1.1"

raci:
  responsible: [role_relationship_manager]
  accountable: [role_credit_underwriter]
  consulted: [role_customer]
  informed: [role_chief_credit_officer]

daci:
  driver: [role_relationship_manager]
  approver: [role_credit_underwriter]
  contributor: [role_customer]
  informed: [role_chief_credit_officer]

attributes:
  baseline_cycle_time_hours: 12.0
  baseline_cost_per_unit: 380.0
  automation_rate: 0.55
  error_rate: 0.04
  sla_hours: 48.0
  approval_threshold_usd: 250000.0
  volume_per_period: 180
  capacity_fte: 6.0

asset_dependencies:
  - asset_crm_system
  - asset_loan_origination_system

graph_relations:
  - relation: feeds_into
    target: l2s_002_credit_underwriting_risk_rating
    weight: 1.0
  - relation: governed_by
    target: basel_credit_risk_underwriting_policy
    weight: 1.0
---

# Loan Application & Credit Packaging

Structures the commercial or retail credit facility request, ingests three years of audited borrower financial statements and tax returns into the Loan Origination System, performs standardized financial statement spreading, and assembles the preliminary Credit Approval Memorandum (CAM).
