---
id: l2s_003_collateral_valuation_lien_perfection
type: process_step
name: Collateral Valuation & Lien Perfection
version: 1.0.0
lifecycles: [L2S]
lod_support: [tier_1, tier_2, tier_3]
tags: [collateral, appraisal, ltv, ucc, closing, l2s]
apqc_pcf_id: "5.2.1.3"

raci:
  responsible: [role_loan_servicing_specialist]
  accountable: [role_chief_credit_officer]
  consulted: [role_credit_underwriter, role_customer]
  informed: [role_treasury_operations_officer]

daci:
  driver: [role_loan_servicing_specialist]
  approver: [role_chief_credit_officer]
  contributor: [role_credit_underwriter, role_customer]
  informed: [role_treasury_operations_officer]

attributes:
  baseline_cycle_time_hours: 18.0
  baseline_cost_per_unit: 540.0
  automation_rate: 0.50
  error_rate: 0.03
  sla_hours: 48.0
  volume_per_period: 165
  capacity_fte: 6.0

asset_dependencies:
  - asset_loan_origination_system

graph_relations:
  - relation: feeds_into
    target: l2s_004_loan_booking_funding_disbursement
    weight: 1.0
  - relation: produces_artifact
    target: data_credit_facility_agreement
    weight: 1.0
  - relation: governed_by
    target: basel_credit_risk_underwriting_policy
    weight: 1.0
---

# Collateral Valuation & Lien Perfection

Validates independent FIRREA-compliant real estate or equipment appraisals, confirms Loan-to-Value (LTV) policy thresholds, executes UCC-1 financing statement filings or first-priority mortgage recordings, and completes legal closing of the Credit Agreement and Promissory Note.
