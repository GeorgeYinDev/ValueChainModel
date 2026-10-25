---
id: l2s_004_loan_booking_funding_disbursement
type: process_step
name: Loan Booking & Principal Funding Disbursement
version: 1.0.0
lifecycles: [L2S]
lod_support: [tier_1, tier_2, tier_3]
tags: [loan_booking, funding, fedwire, disbursement, core_banking, l2s]
apqc_pcf_id: "5.2.1.4"

raci:
  responsible: [role_loan_servicing_specialist]
  accountable: [role_treasury_operations_officer]
  consulted: [role_credit_underwriter]
  informed: [role_relationship_manager, role_customer]

daci:
  driver: [role_loan_servicing_specialist]
  approver: [role_treasury_operations_officer]
  contributor: [role_credit_underwriter]
  informed: [role_relationship_manager, role_customer]

attributes:
  baseline_cycle_time_hours: 4.0
  baseline_cost_per_unit: 150.0
  automation_rate: 0.85
  error_rate: 0.01
  sla_hours: 8.0
  approval_threshold_usd: 2500000.0
  volume_per_period: 165
  capacity_fte: 4.0

asset_dependencies:
  - asset_core_banking_platform
  - asset_payment_gateway

graph_relations:
  - relation: feeds_into
    target: l2s_005_repayment_servicing_covenant_monitoring
    weight: 1.0
  - relation: governed_by
    target: basel_credit_risk_underwriting_policy
    weight: 1.0
  - relation: governed_by
    target: bsa_aml_kyc_compliance_policy
    weight: 1.0
---

# Loan Booking & Principal Funding Disbursement

Boards the executed credit facility, commitment limits, SOFR margin schedules, and fee amortization rules onto the Core Banking Platform, verifies intraday treasury liquidity, and releases principal funding via Fedwire or ACH under dual-officer settlement authorization.
