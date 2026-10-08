---
id: p2d_003_clinical_admission_triage
type: process_step
name: Clinical Admission & Triage
version: 1.0.0
lifecycles: [P2D]
lod_support: [tier_1, tier_2, tier_3]
tags: [clinical, triage, admission, nursing, emergency]

raci:
  responsible: [role_triage_nurse]
  accountable: [role_attending_physician]
  consulted: [role_patient_access_specialist]
  informed: [role_patient]

daci:
  driver: [role_triage_nurse]
  approver: [role_attending_physician]
  contributor: [role_patient_access_specialist]
  informed: [role_patient]

attributes:
  baseline_cycle_time_hours: 1.5
  baseline_cost_per_unit: 120.0
  automation_rate: 0.25
  error_rate: 0.03

asset_dependencies:
  - asset_ehr_system

graph_relations:
  - relation: feeds_into
    target: p2d_004_care_delivery_order_execution
    weight: 1.0
  - relation: governed_by
    target: hipaa_phi_privacy_policy
    weight: 1.0
---

# Clinical Admission & Triage

Performs initial clinical acuity evaluation (Emergency Severity Index), baseline vitals collection, and room/bed assignment for inpatient admission or ambulatory placement.
