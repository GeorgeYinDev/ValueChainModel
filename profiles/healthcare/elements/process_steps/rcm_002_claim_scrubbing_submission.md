---
id: rcm_002_claim_scrubbing_submission
type: process_step
name: Claim Scrubbing & Clearinghouse Submission
version: 1.0.0
lifecycles: [RCM]
lod_support: [tier_1, tier_2, tier_3]
tags: [claims, scrubbing, edi837, clearinghouse, billing]

raci:
  responsible: [role_medical_coder]
  accountable: [role_rcm_director]
  consulted: [role_patient_access_specialist]
  informed: [role_compliance_officer]

daci:
  driver: [role_medical_coder]
  approver: [role_rcm_director]
  contributor: [role_patient_access_specialist]
  informed: [role_compliance_officer]

attributes:
  baseline_cycle_time_hours: 6.0
  baseline_cost_per_unit: 40.0
  automation_rate: 0.88
  error_rate: 0.03

asset_dependencies:
  - asset_rcm_clearinghouse

graph_relations:
  - relation: feeds_into
    target: rcm_003_payer_adjudication_remittance
    weight: 1.0
  - relation: governed_by
    target: clinical_prior_auth_medical_necessity_policy
    weight: 1.0
---

# Claim Scrubbing & Clearinghouse Submission

Applies National Correct Coding Initiative (NCCI) edits, medical necessity validation checks, and commercial payer formatting rules prior to electronic EDI 837 claim transmission via the clearinghouse.
