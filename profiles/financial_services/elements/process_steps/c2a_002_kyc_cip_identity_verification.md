---
id: c2a_002_kyc_cip_identity_verification
type: process_step
name: KYC/CIP Identity & UBO Verification
version: 1.0.0
lifecycles: [C2A]
lod_support: [tier_1, tier_2, tier_3]
tags: [kyc, cip, ubo, identity_verification, fincen, c2a]
apqc_pcf_id: "3.5.1.2"

raci:
  responsible: [role_kyc_aml_analyst]
  accountable: [role_bsa_compliance_officer]
  consulted: [role_relationship_manager, role_customer]
  informed: [role_treasury_operations_officer]

daci:
  driver: [role_kyc_aml_analyst]
  approver: [role_bsa_compliance_officer]
  contributor: [role_relationship_manager, role_customer]
  informed: [role_treasury_operations_officer]

attributes:
  baseline_cycle_time_hours: 6.0
  baseline_cost_per_unit: 160.0
  automation_rate: 0.65
  error_rate: 0.04
  sla_hours: 24.0
  volume_per_period: 420
  capacity_fte: 8.0

asset_dependencies:
  - asset_aml_kyc_screening_engine

graph_relations:
  - relation: feeds_into
    target: c2a_003_aml_sanctions_pep_screening
    weight: 1.0
  - relation: governed_by
    target: bsa_aml_kyc_compliance_policy
    weight: 1.0
---

# KYC/CIP Identity & UBO Verification

Executes USA PATRIOT Act Section 326 Customer Identification Program (CIP) documentary and non-documentary verification, secretary-of-state registry checks, and FinCEN Customer Due Diligence (CDD) verification of all Ultimate Beneficial Owners (UBOs holding >= 25% equity) and one controlling executive officer.
