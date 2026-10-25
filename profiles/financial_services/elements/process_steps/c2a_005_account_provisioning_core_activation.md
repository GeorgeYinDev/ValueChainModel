---
id: c2a_005_account_provisioning_core_activation
type: process_step
name: Core Account Provisioning & Treasury Activation
version: 1.0.0
lifecycles: [C2A]
lod_support: [tier_1, tier_2, tier_3]
tags: [account_opening, core_banking, dda, treasury, activation, c2a]
apqc_pcf_id: "3.5.1.5"

raci:
  responsible: [role_loan_servicing_specialist]
  accountable: [role_treasury_operations_officer]
  consulted: [role_kyc_aml_analyst]
  informed: [role_relationship_manager, role_customer]

daci:
  driver: [role_loan_servicing_specialist]
  approver: [role_treasury_operations_officer]
  contributor: [role_kyc_aml_analyst]
  informed: [role_relationship_manager, role_customer]

attributes:
  baseline_cycle_time_hours: 3.0
  baseline_cost_per_unit: 95.0
  automation_rate: 0.85
  error_rate: 0.02
  sla_hours: 12.0
  volume_per_period: 400
  capacity_fte: 5.0

asset_dependencies:
  - asset_core_banking_platform
  - asset_payment_gateway

graph_relations:
  - relation: feeds_into
    target: l2s_001_loan_application_credit_packaging
    weight: 1.0
  - relation: governed_by
    target: bsa_aml_kyc_compliance_policy
    weight: 1.0
---

# Core Account Provisioning & Treasury Activation

Provisions Customer Information Files (CIF), Demand Deposit Accounts (DDA), and commercial treasury sweep structures in the Core Banking Platform, configures dual-control wire/ACH payment entitlements, and activates transaction monitoring profiles upon initial funding clearance.
