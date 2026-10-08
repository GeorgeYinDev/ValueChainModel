---
id: p2d_001_patient_registration_scheduling
type: process_step
name: Patient Registration & Scheduling
version: 1.0.0
lifecycles: [P2D]
lod_support: [tier_1, tier_2, tier_3]
tags: [scheduling, registration, intake, patient_access]

raci:
  responsible: [role_patient_access_specialist]
  accountable: [role_rcm_director]
  consulted: [role_patient]
  informed: [role_triage_nurse]

daci:
  driver: [role_patient_access_specialist]
  approver: [role_rcm_director]
  contributor: [role_patient]
  informed: [role_triage_nurse]

attributes:
  baseline_cycle_time_hours: 0.5
  baseline_cost_per_unit: 25.0
  automation_rate: 0.65
  error_rate: 0.04

asset_dependencies:
  - asset_ehr_system

graph_relations:
  - relation: feeds_into
    target: p2d_002_insurance_verification_prior_auth
    weight: 1.0
  - relation: governed_by
    target: hipaa_phi_privacy_policy
    weight: 1.0
---

# Patient Registration & Scheduling

Captures patient demographics, contact details, identity verification, and primary insurance carrier details during outpatient booking or pre-admission intake.
