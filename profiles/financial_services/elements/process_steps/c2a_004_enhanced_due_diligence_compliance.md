---
id: c2a_004_enhanced_due_diligence_compliance
type: process_step
name: Enhanced Due Diligence (EDD) & BSA Approval
version: 1.0.0
lifecycles: [C2A]
lod_support: [tier_1, tier_2, tier_3]
tags: [edd, bsa, source_of_wealth, high_risk, compliance, c2a]
apqc_pcf_id: "3.5.1.4"

raci:
  responsible: [role_kyc_aml_analyst]
  accountable: [role_bsa_compliance_officer]
  consulted: [role_relationship_manager]
  informed: [role_internal_auditor]

daci:
  driver: [role_kyc_aml_analyst]
  approver: [role_bsa_compliance_officer]
  contributor: [role_relationship_manager]
  informed: [role_internal_auditor]

attributes:
  baseline_cycle_time_hours: 16.0
  baseline_cost_per_unit: 450.0
  automation_rate: 0.35
  error_rate: 0.03
  sla_hours: 48.0
  approval_threshold_usd: 250000.0
  volume_per_period: 120
  capacity_fte: 5.0

asset_dependencies:
  - asset_aml_kyc_screening_engine

graph_relations:
  - relation: feeds_into
    target: c2a_005_account_provisioning_core_activation
    weight: 1.0
  - relation: produces_artifact
    target: data_kyc_cdd_dossier
    weight: 1.0
  - relation: governed_by
    target: bsa_aml_kyc_compliance_policy
    weight: 1.0
  - relation: exception_to
    target: c2a_002_kyc_cip_identity_verification
    probability: 0.08
---

# Enhanced Due Diligence (EDD) & BSA Approval

Conducts deep-dive Enhanced Due Diligence (EDD) for high-risk jurisdictions, PEPs, cash-intensive businesses, and complex offshore structures, corroborating independent Source of Wealth (SoW) and Source of Funds (SoF) evidence prior to formal BSA/AML Compliance Officer sign-off.
