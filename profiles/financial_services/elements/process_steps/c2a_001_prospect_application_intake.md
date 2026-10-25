---
id: c2a_001_prospect_application_intake
type: process_step
name: Prospect Application & Entity Intake
version: 1.0.0
lifecycles: [C2A]
lod_support: [tier_1, tier_2, tier_3]
tags: [onboarding, intake, fatca, crs, banking, c2a]
apqc_pcf_id: "3.5.1.1"

raci:
  responsible: [role_relationship_manager]
  accountable: [role_bsa_compliance_officer]
  consulted: [role_customer]
  informed: [role_kyc_aml_analyst]

daci:
  driver: [role_relationship_manager]
  approver: [role_bsa_compliance_officer]
  contributor: [role_customer]
  informed: [role_kyc_aml_analyst]

attributes:
  baseline_cycle_time_hours: 2.0
  baseline_cost_per_unit: 85.0
  automation_rate: 0.75
  error_rate: 0.03
  sla_hours: 8.0
  volume_per_period: 420
  capacity_fte: 6.0

asset_dependencies:
  - asset_crm_system
  - asset_aml_kyc_screening_engine

graph_relations:
  - relation: feeds_into
    target: c2a_002_kyc_cip_identity_verification
    weight: 1.0
  - relation: governed_by
    target: bsa_aml_kyc_compliance_policy
    weight: 1.0
---

# Prospect Application & Entity Intake

Captures institutional and retail banking onboarding applications, legal entity formation documents, corporate ownership hierarchy charts, anticipated transaction volumes, and FATCA (W-9 / W-8BEN-E) & CRS tax residency self-certifications.
