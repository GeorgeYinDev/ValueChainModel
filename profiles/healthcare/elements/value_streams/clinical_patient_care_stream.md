---
id: clinical_patient_care_stream
type: value_stream
name: Clinical Patient Access & Inpatient Care Delivery Value Stream
version: 1.0.0
lifecycles: [P2D]
lod_support: [tier_1, tier_2, tier_3]
tags: [value_stream, clinical, inpatient, care_delivery, healthcare]

raci:
  responsible: [role_triage_nurse, role_patient_access_specialist]
  accountable: [role_attending_physician]
  consulted: [role_patient]
  informed: [role_rcm_director]

daci:
  driver: [role_triage_nurse]
  approver: [role_attending_physician]
  contributor: [role_patient_access_specialist]
  informed: [role_rcm_director]

attributes:
  baseline_cycle_time_hours: 57.5
  baseline_cost_per_unit: 3170.0
  automation_rate: 0.45
  error_rate: 0.03
  sla_hours: 72.0

asset_dependencies:
  - asset_ehr_system
  - asset_rcm_clearinghouse
  - asset_pacs_lis_system

graph_relations:
  - relation: governed_by
    target: hipaa_phi_privacy_policy
    weight: 1.0
  - relation: feeds_into
    target: hospital_revenue_cycle_stream
    weight: 1.0
---

# Value Stream: Clinical Patient Access & Inpatient Care Delivery (P2D)

## Executive Summary
Encompasses the holistic patient journey through acute care operations—from initial scheduling, identity validation, and insurance clearance, through bedside clinical nursing, provider order entry, and structured transition of care.

## 1. Strategic Outcomes (Tier 1 - Executive Level)
- **Clinical Safety & Zero Preventable Harm**: Enforce barcoded medication verification (eMAR) and closed-loop diagnostic tracking.
- **Throughput & Capacity Optimization**: Minimize Emergency Department boarding times and manage Average Length of Stay (ALOS <= 4.2 days).
- **Seamless Clinical-Financial Bridge**: Automated capture of encounters, diagnoses, and orders upon discharge transition feeding the hospital revenue cycle.

## 2. Included Steps & RACI Summary (Tier 2 - Process Architect Level)
1. `p2d_001_patient_registration_scheduling` - Scheduling & Demographic Intake
2. `p2d_002_insurance_verification_prior_auth` - Insurance Clearance & Prior Authorization
3. `p2d_003_clinical_admission_triage` - Bedside Triage & Inpatient Bed Placement
4. `p2d_004_care_delivery_order_execution` - Acute Care Delivery & CPOE Order Fulfillment
5. `p2d_005_discharge_planning_transition` - Care Transition & Encounter Closeout

## 3. Systems Architecture (Tier 3 - Systems Engineer Level)
- **Core Clinical Platform**: Electronic Health Record (`asset_ehr_system`).
- **Diagnostic Interoperability**: DICOM PACS and Laboratory Information System (`asset_pacs_lis_system`).
