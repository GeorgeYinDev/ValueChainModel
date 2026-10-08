---
id: rcm_004_denial_management_appeals
type: process_step
name: Denial Management & Appeals
version: 1.0.0
lifecycles: [RCM]
lod_support: [tier_1, tier_2, tier_3]
tags: [denials, appeals, carc, rarc, rcm]

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
  baseline_cycle_time_hours: 24.0
  baseline_cost_per_unit: 110.0
  automation_rate: 0.35
  error_rate: 0.07

asset_dependencies:
  - asset_rcm_clearinghouse
  - asset_ehr_system

graph_relations:
  - relation: feeds_into
    target: rcm_005_patient_billing_collections
    weight: 1.0
  - relation: governed_by
    target: clinical_prior_auth_medical_necessity_policy
    weight: 1.0
---

# Denial Management & Appeals

Analyzes Claim Adjustment Reason Codes (CARC) and Remittance Advice Remark Codes (RARC), correcting technical billing errors, submitting clinical chart appeals, and coordinating peer-to-peer provider reviews.
