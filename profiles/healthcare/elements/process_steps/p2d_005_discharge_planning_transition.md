---
id: p2d_005_discharge_planning_transition
type: process_step
name: Discharge Planning & Care Transition
version: 1.0.0
lifecycles: [P2D]
lod_support: [tier_1, tier_2, tier_3]
tags: [discharge, transition_of_care, reconciliation, clinical]

raci:
  responsible: [role_triage_nurse]
  accountable: [role_attending_physician]
  consulted: [role_patient]
  informed: [role_rcm_director]

daci:
  driver: [role_triage_nurse]
  approver: [role_attending_physician]
  contributor: [role_patient]
  informed: [role_rcm_director]

attributes:
  baseline_cycle_time_hours: 3.5
  baseline_cost_per_unit: 180.0
  automation_rate: 0.50
  error_rate: 0.04

asset_dependencies:
  - asset_ehr_system

graph_relations:
  - relation: feeds_into
    target: rcm_001_charge_capture_coding
    weight: 1.0
  - relation: governed_by
    target: hipaa_phi_privacy_policy
    weight: 1.0
---

# Discharge Planning & Care Transition

Coordinates inpatient discharge disposition, medication reconciliation, patient education, and transmission of Continuity of Care Documents (CCD), triggering encounter closure and clinical charge capture.
