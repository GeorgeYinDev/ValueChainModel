---
id: p2d_002_insurance_verification_prior_auth
type: process_step
name: Insurance Verification & Prior Authorization
version: 1.0.0
lifecycles: [P2D]
lod_support: [tier_1, tier_2, tier_3]
tags: [eligibility, prior_auth, clearance, insurance, rcm]

raci:
  responsible: [role_patient_access_specialist]
  accountable: [role_rcm_director]
  consulted: [role_attending_physician]
  informed: [role_patient]

daci:
  driver: [role_patient_access_specialist]
  approver: [role_rcm_director]
  contributor: [role_attending_physician]
  informed: [role_patient]

attributes:
  baseline_cycle_time_hours: 4.0
  baseline_cost_per_unit: 45.0
  automation_rate: 0.70
  error_rate: 0.08

asset_dependencies:
  - asset_ehr_system
  - asset_rcm_clearinghouse

graph_relations:
  - relation: feeds_into
    target: p2d_003_clinical_admission_triage
    weight: 1.0
  - relation: governed_by
    target: clinical_prior_auth_medical_necessity_policy
    weight: 1.0
---

# Insurance Verification & Prior Authorization

Queries electronic clearinghouse via EDI 270/271 for copay, deductible, and benefit limits; submits electronic prior authorization requests (EDI 278) for high-acuity interventions.
