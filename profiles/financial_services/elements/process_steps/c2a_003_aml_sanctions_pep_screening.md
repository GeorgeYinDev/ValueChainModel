---
id: c2a_003_aml_sanctions_pep_screening
type: process_step
name: AML Sanctions, PEP & Adverse Media Screening
version: 1.0.0
lifecycles: [C2A]
lod_support: [tier_1, tier_2, tier_3]
tags: [aml, ofac, sanctions, pep, adverse_media, c2a]
apqc_pcf_id: "3.5.1.3"

raci:
  responsible: [role_kyc_aml_analyst]
  accountable: [role_bsa_compliance_officer]
  consulted: [role_internal_auditor]
  informed: [role_relationship_manager]

daci:
  driver: [role_kyc_aml_analyst]
  approver: [role_bsa_compliance_officer]
  contributor: [role_internal_auditor]
  informed: [role_relationship_manager]

attributes:
  baseline_cycle_time_hours: 4.0
  baseline_cost_per_unit: 120.0
  automation_rate: 0.80
  error_rate: 0.05
  sla_hours: 12.0
  volume_per_period: 420
  capacity_fte: 7.0

asset_dependencies:
  - asset_aml_kyc_screening_engine

graph_relations:
  - relation: feeds_into
    target: c2a_004_enhanced_due_diligence_compliance
    weight: 1.0
  - relation: governed_by
    target: bsa_aml_kyc_compliance_policy
    weight: 1.0
---

# AML Sanctions, PEP & Adverse Media Screening

Screens the legal entity, directors, signatories, and beneficial owners against OFAC SDN, UN, EU, and UK HM Treasury sanctions lists, Politically Exposed Person (PEP) registries, and global adverse media databases to compute a composite Customer Risk Rating (CRR).
