---
id: basel_credit_risk_underwriting_policy
type: control_policy
name: Basel III Credit Risk Underwriting, Concentration & CECL Policy
version: 1.0.0
lifecycles: [L2S]
lod_support: [tier_1, tier_2, tier_3]
tags: [policy, basel_iii, credit_risk, cecl, dscr, ltv, lending]

raci:
  responsible: [role_credit_underwriter, role_loan_servicing_specialist]
  accountable: [role_chief_credit_officer]
  consulted: [role_finance_controller]
  informed: [role_internal_auditor]

daci:
  driver: [role_credit_underwriter]
  approver: [role_chief_credit_officer]
  contributor: [role_finance_controller]
  informed: [role_internal_auditor]

attributes:
  baseline_cycle_time_hours: 0.0
  baseline_cost_per_unit: 0.0
  automation_rate: 1.0
  error_rate: 0.0
  sla_hours: 0.0
  approval_threshold_usd: 5000000.0

asset_dependencies:
  - asset_loan_origination_system
  - asset_core_banking_platform

graph_relations: []
---

# Control Policy: Basel III Credit Risk Underwriting, Concentration & CECL Policy

## Executive Summary
Establishes prudential credit underwriting standards, quantitative risk-rating governance, collateral valuation requirements, and ASC 326 Current Expected Credit Loss (CECL) provisioning rules across the commercial and retail lending portfolio.

## 1. Governance Rules & Controls (Tier 1)
- **Segregation of Origination & Credit Approval**: Front-office Relationship Managers (`role_relationship_manager`) are strictly prohibited from approving credit risk ratings, underwriting memos, or collateral exceptions.
- **Minimum Underwriting Metrics**: Commercial facilities require a minimum Debt Service Coverage Ratio (DSCR) of 1.25x and maximum Senior Leverage of 3.50x unless an explicit Credit Committee policy exception is approved by `role_chief_credit_officer`.
- **Collateral & Lien Perfection Prerequisite**: Facilities exceeding $250,000 USD require an independent FIRREA appraisal confirming LTV within asset-class caps (<= 75% commercial real estate; <= 80% equipment) and perfected UCC-1 or mortgage recording prior to funding release (`l2s_004`).
- **ASC 326 CECL & Non-Accrual Governance**: Loans past due >= 90 days must be placed on non-accrual status unless both well-secured and in the process of collection, with life-of-loan expected credit losses posted to `r2r_001_journal_entry_recording`.
