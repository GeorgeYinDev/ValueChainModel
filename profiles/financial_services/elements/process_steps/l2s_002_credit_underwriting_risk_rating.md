---
id: l2s_002_credit_underwriting_risk_rating
type: process_step
name: Credit Underwriting & PD/LGD Risk Rating
version: 1.0.0
lifecycles: [L2S]
lod_support: [tier_1, tier_2, tier_3]
tags: [underwriting, pd_lgd, dscr, credit_committee, basel, l2s]
apqc_pcf_id: "5.2.1.2"

raci:
  responsible: [role_credit_underwriter]
  accountable: [role_chief_credit_officer]
  consulted: [role_relationship_manager, role_credit_manager]
  informed: [role_customer]

daci:
  driver: [role_credit_underwriter]
  approver: [role_chief_credit_officer]
  contributor: [role_relationship_manager, role_credit_manager]
  informed: [role_customer]

attributes:
  baseline_cycle_time_hours: 24.0
  baseline_cost_per_unit: 820.0
  automation_rate: 0.45
  error_rate: 0.03
  sla_hours: 72.0
  approval_threshold_usd: 5000000.0
  volume_per_period: 180
  capacity_fte: 8.0

asset_dependencies:
  - asset_loan_origination_system

graph_relations:
  - relation: feeds_into
    target: l2s_003_collateral_valuation_lien_perfection
    weight: 1.0
  - relation: governed_by
    target: basel_credit_risk_underwriting_policy
    weight: 1.0
  - relation: exception_to
    target: l2s_001_loan_application_credit_packaging
    probability: 0.10
---

# Credit Underwriting & PD/LGD Risk Rating

Executes quantitative credit risk modeling to assign Basel III Probability of Default (PD) and Loss Given Default (LGD) grades, evaluates historical and projected Debt Service Coverage Ratio (DSCR >= 1.25x) and leverage limits, verifies Single Obligor concentration compliance, and secures Credit Committee adjudication.
