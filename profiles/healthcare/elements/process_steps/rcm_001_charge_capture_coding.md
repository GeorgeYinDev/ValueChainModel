---
id: rcm_001_charge_capture_coding
type: process_step
name: Charge Capture & Medical Coding
version: 1.0.0
lifecycles: [RCM]
lod_support: [tier_1, tier_2, tier_3]
tags: [coding, him, icd10, cpt, charges, rcm]

raci:
  responsible: [role_medical_coder]
  accountable: [role_rcm_director]
  consulted: [role_attending_physician]
  informed: [role_compliance_officer]

daci:
  driver: [role_medical_coder]
  approver: [role_rcm_director]
  contributor: [role_attending_physician]
  informed: [role_compliance_officer]

attributes:
  baseline_cycle_time_hours: 12.0
  baseline_cost_per_unit: 85.0
  automation_rate: 0.60
  error_rate: 0.05

asset_dependencies:
  - asset_ehr_system
  - asset_rcm_clearinghouse

graph_relations:
  - relation: feeds_into
    target: rcm_002_claim_scrubbing_submission
    weight: 1.0
  - relation: governed_by
    target: hipaa_phi_privacy_policy
    weight: 1.0
---

# Charge Capture & Medical Coding

Aggregates clinical documentation, surgical operative notes, and pharmacy charges to assign compliant ICD-10-CM diagnosis codes, ICD-10-PCS / CPT procedure codes, and MS-DRG grouping.
