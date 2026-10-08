---
id: p2d_004_care_delivery_order_execution
type: process_step
name: Care Delivery & Order Execution
version: 1.0.0
lifecycles: [P2D]
lod_support: [tier_1, tier_2, tier_3]
tags: [clinical, cpoe, emar, care_delivery, bedside]

raci:
  responsible: [role_triage_nurse]
  accountable: [role_attending_physician]
  consulted: [role_medical_coder]
  informed: [role_patient]

daci:
  driver: [role_triage_nurse]
  approver: [role_attending_physician]
  contributor: [role_medical_coder]
  informed: [role_patient]

attributes:
  baseline_cycle_time_hours: 48.0
  baseline_cost_per_unit: 2800.0
  automation_rate: 0.35
  error_rate: 0.02

asset_dependencies:
  - asset_ehr_system
  - asset_pacs_lis_system

graph_relations:
  - relation: feeds_into
    target: p2d_005_discharge_planning_transition
    weight: 1.0
  - relation: governed_by
    target: hipaa_phi_privacy_policy
    weight: 1.0
---

# Care Delivery & Order Execution

Execution of inpatient physician order entry (CPOE), medication administration (eMAR barcode scanning), bedside nursing care, and diagnostic testing (radiology PACS and lab LIS).
