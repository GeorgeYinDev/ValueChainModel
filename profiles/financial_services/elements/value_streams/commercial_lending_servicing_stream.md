---
id: commercial_lending_servicing_stream
type: value_stream
name: Commercial Loan Origination, Underwriting & Servicing Value Stream
version: 1.0.0
lifecycles: [L2S]
lod_support: [tier_1, tier_2, tier_3]
tags: [value_stream, lending, underwriting, servicing, credit_risk, l2s]

raci:
  responsible: [role_credit_underwriter, role_loan_servicing_specialist]
  accountable: [role_chief_credit_officer]
  consulted: [role_relationship_manager, role_treasury_operations_officer]
  informed: [role_finance_controller]

daci:
  driver: [role_credit_underwriter]
  approver: [role_chief_credit_officer]
  contributor: [role_loan_servicing_specialist, role_treasury_operations_officer]
  informed: [role_finance_controller]

attributes:
  baseline_cycle_time_hours: 74.0
  baseline_cost_per_unit: 2390.0
  automation_rate: 0.64
  error_rate: 0.03
  sla_hours: 120.0

asset_dependencies:
  - asset_loan_origination_system
  - asset_core_banking_platform
  - asset_payment_gateway
  - asset_erp_system

graph_relations:
  - relation: governed_by
    target: basel_credit_risk_underwriting_policy
    weight: 1.0
  - relation: feeds_into
    target: financial_close_reporting_stream
    weight: 1.0
---

# Value Stream: Commercial Loan Origination, Underwriting & Servicing (L2S)

## Executive Summary
Governs the lifecycle of commercial and retail credit facilities from initial application and financial spreading, through quantitative PD/LGD underwriting, independent collateral appraisal and UCC/mortgage lien perfection, core banking booking and Fedwire funding, ongoing covenant monitoring, and daily subledger-to-General-Ledger settlement.

## 1. Strategic Outcomes (Tier 1 - Executive Level)
- **Prudent Credit Risk & Capital Discipline**: Maintain Non-Performing Loan (NPL) ratios <= 1.25% and enforce Basel III risk-weighted asset (RWA) underwriting guardrails.
- **Perfected Collateral Protection**: Require verified LTV coverage and perfected first-priority liens before treasury principal disbursement.
- **Automated Subledger Integrity**: Reconcile interest accruals, fee recognition, principal repayments, and ASC 326 CECL credit loss provisions directly into `R2R`.

## 2. Included Steps & RACI Summary (Tier 2 - Process Architect Level)
1. `l2s_001_loan_application_credit_packaging` - Loan Application & Credit Packaging
2. `l2s_002_credit_underwriting_risk_rating` - Credit Underwriting & PD/LGD Risk Rating
3. `l2s_003_collateral_valuation_lien_perfection` - Collateral Valuation & Lien Perfection
4. `l2s_004_loan_booking_funding_disbursement` - Loan Booking & Principal Funding Disbursement
5. `l2s_005_repayment_servicing_covenant_monitoring` - Repayment Servicing & Covenant Monitoring
6. `l2s_006_delinquency_workout_ledger_settlement` - Delinquency Workout & Subledger Reconciliation

## 3. Systems Architecture (Tier 3 - Systems Engineer Level)
- **Credit Origination & Risk Platform**: `asset_loan_origination_system`
- **Loan Subledger & Treasury Rails**: `asset_core_banking_platform`, `asset_payment_gateway`
