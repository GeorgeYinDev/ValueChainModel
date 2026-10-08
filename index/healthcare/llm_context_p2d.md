# System Prompt: LLM Context Blueprint for Business Lifecycle [Patient to Discharge]

> Profile: `healthcare` | Lifecycle ID: `P2D` | Version: `1.0.0` | Source Layer: `healthcare`
> Description: Patient access, eligibility verification, clinical admission, acute care delivery, and safe discharge transitions.

## Milestone Process Sequence
- **Step 1**: `p2d_001_patient_registration_scheduling` (Patient Registration & Scheduling)
- **Step 2**: `p2d_002_insurance_verification_prior_auth` (Insurance Verification & Prior Authorization)
- **Step 3**: `p2d_003_clinical_admission_triage` (Clinical Admission & Triage)
- **Step 4**: `p2d_004_care_delivery_order_execution` (Care Delivery & Order Execution)
- **Step 5**: `p2d_005_discharge_planning_transition` (Discharge Planning & Care Transition)

## Key Performance Indicators (KPIs)
- `Average Length of Stay (ALOS)`
- `Bed Turnover Rate`
- `Time to Triage`
- `30-Day Readmission Rate`

## Active Value Chain Elements Knowledge Base

### [Medical Necessity & Prior Authorization Governance Policy] (`clinical_prior_auth_medical_necessity_policy`) [Layer: `healthcare`]
- **Type**: `control_policy` | **Tags**: `policy, prior_auth, medical_necessity, rcm, healthcare`
- **RACI**: `{"responsible": ["role_patient_access_specialist", "role_medical_coder"], "accountable": ["role_rcm_director"], "consulted": ["role_attending_physician"], "informed": ["role_compliance_officer"]}`
- **Assets**: `asset_rcm_clearinghouse, asset_ehr_system`

# Control Policy: Medical Necessity & Prior Authorization Governance Policy

## Executive Summary
Defines clinical authorization guidelines, payer medical policy validation standards, and pre-service financial clearance rules to prevent retroactive payer claim denials and ensure evidence-based care approval.

## 1. Governance Rules & Controls (Tier 1)
- **Mandatory Pre-Service Clearance**: Elective inpatient admissions, surgical procedures, and high-cost advanced imaging modalities mandate documented prior authorization (EDI 278) prior to clinical order fulfillment.
- **Peer-to-Peer Clinical Review Escalation**: When commercial or Medicare Advantage payers issue an initial denial of authorization, `role_attending_physician` must conduct a peer-to-peer clinical appeal within 5 business days.
- **Non-Covered Service Financial Disclosure**: When services do not meet payer medical necessity criteria, patients must receive an Advance Beneficiary Notice of Noncoverage (ABN) or CMS-compliant financial disclosure prior to service delivery.
- **Write-Off Authorization Ceilings**: Unappealable authorization denials exceeding $50,000 USD require formal write-down approval from `role_rcm_director`.
---

### [HIPAA Security, Privacy & PHI Governance Policy] (`hipaa_phi_privacy_policy`) [Layer: `healthcare`]
- **Type**: `control_policy` | **Tags**: `policy, hipaa, phi, privacy, compliance, healthcare`
- **RACI**: `{"responsible": ["role_patient_access_specialist", "role_triage_nurse", "role_medical_coder"], "accountable": ["role_compliance_officer"], "consulted": ["role_rcm_director"], "informed": ["role_attending_physician"]}`
- **Assets**: `asset_ehr_system, asset_rcm_clearinghouse`

# Control Policy: HIPAA Security, Privacy & PHI Governance Policy

## Executive Summary
Enforces regulatory compliance under the Health Insurance Portability and Accountability Act (HIPAA) Privacy and Security Rules across all patient access, clinical care documentation, and electronic revenue cycle transactions.

## 1. Governance Rules & Controls (Tier 1)
- **Minimum Necessary Standard**: Workforce members may access only the minimum protected health information (PHI) required to perform clinical duties or billing adjudication.
- **Audit Trail & Access Telemetry**: All clinical chart accesses, electronic claim queries, and diagnostic reviews are logged with immutable audit timestamps in `asset_ehr_system`.
- **Business Associate Agreement (BAA) Verification**: No electronic data exchange (EDI 837/835) may occur with third-party clearinghouses or billing partners without an active, countersigned BAA.
- **Incident Escalation**: Suspected unauthorized PHI disclosures exceeding 500 individuals mandate notification to HHS Office for Civil Rights (OCR) within 60 calendar days under direct oversight of `role_compliance_officer`.
---

### [Longitudinal Electronic Health Record (EHR / FHIR)] (`data_electronic_health_record`) [Layer: `healthcare`]
- **Type**: `data_entity` | **Tags**: `data, ehr, clinical, chart, fhir, healthcare`
- **RACI**: `{}`
- **Assets**: ``

# Data Entity: Longitudinal Electronic Health Record (EHR / FHIR)

The clinical source of truth containing patient demographic profile, encounter documentation, provider orders, lab results, medication history, and discharge instructions.
---

### [Average Length of Stay (ALOS)] (`kpi_average_length_of_stay`) [Layer: `healthcare`]
- **Type**: `kpi_metric` | **Tags**: `kpi, clinical, inpatient, utilization, healthcare`
- **RACI**: `{}`
- **Assets**: ``

# KPI: Average Length of Stay (ALOS)

Measures inpatient bed utilization and operational throughput from initial clinical admission to definitive discharge disposition.
---

### [Patient Registration & Scheduling] (`p2d_001_patient_registration_scheduling`) [Layer: `healthcare`]
- **Type**: `process_step` | **Tags**: `scheduling, registration, intake, patient_access`
- **RACI**: `{"responsible": ["role_patient_access_specialist"], "accountable": ["role_rcm_director"], "consulted": ["role_patient"], "informed": ["role_triage_nurse"]}`
- **Assets**: `asset_ehr_system`

# Patient Registration & Scheduling

Captures patient demographics, contact details, identity verification, and primary insurance carrier details during outpatient booking or pre-admission intake.
---

### [Insurance Verification & Prior Authorization] (`p2d_002_insurance_verification_prior_auth`) [Layer: `healthcare`]
- **Type**: `process_step` | **Tags**: `eligibility, prior_auth, clearance, insurance, rcm`
- **RACI**: `{"responsible": ["role_patient_access_specialist"], "accountable": ["role_rcm_director"], "consulted": ["role_attending_physician"], "informed": ["role_patient"]}`
- **Assets**: `asset_ehr_system, asset_rcm_clearinghouse`

# Insurance Verification & Prior Authorization

Queries electronic clearinghouse via EDI 270/271 for copay, deductible, and benefit limits; submits electronic prior authorization requests (EDI 278) for high-acuity interventions.
---

### [Clinical Admission & Triage] (`p2d_003_clinical_admission_triage`) [Layer: `healthcare`]
- **Type**: `process_step` | **Tags**: `clinical, triage, admission, nursing, emergency`
- **RACI**: `{"responsible": ["role_triage_nurse"], "accountable": ["role_attending_physician"], "consulted": ["role_patient_access_specialist"], "informed": ["role_patient"]}`
- **Assets**: `asset_ehr_system`

# Clinical Admission & Triage

Performs initial clinical acuity evaluation (Emergency Severity Index), baseline vitals collection, and room/bed assignment for inpatient admission or ambulatory placement.
---

### [Care Delivery & Order Execution] (`p2d_004_care_delivery_order_execution`) [Layer: `healthcare`]
- **Type**: `process_step` | **Tags**: `clinical, cpoe, emar, care_delivery, bedside`
- **RACI**: `{"responsible": ["role_triage_nurse"], "accountable": ["role_attending_physician"], "consulted": ["role_medical_coder"], "informed": ["role_patient"]}`
- **Assets**: `asset_ehr_system, asset_pacs_lis_system`

# Care Delivery & Order Execution

Execution of inpatient physician order entry (CPOE), medication administration (eMAR barcode scanning), bedside nursing care, and diagnostic testing (radiology PACS and lab LIS).
---

### [Discharge Planning & Care Transition] (`p2d_005_discharge_planning_transition`) [Layer: `healthcare`]
- **Type**: `process_step` | **Tags**: `discharge, transition_of_care, reconciliation, clinical`
- **RACI**: `{"responsible": ["role_triage_nurse"], "accountable": ["role_attending_physician"], "consulted": ["role_patient"], "informed": ["role_rcm_director"]}`
- **Assets**: `asset_ehr_system`

# Discharge Planning & Care Transition

Coordinates inpatient discharge disposition, medication reconciliation, patient education, and transmission of Continuity of Care Documents (CCD), triggering encounter closure and clinical charge capture.
---

### [Clinical Patient Access & Inpatient Care Delivery Value Stream] (`clinical_patient_care_stream`) [Layer: `healthcare`]
- **Type**: `value_stream` | **Tags**: `value_stream, clinical, inpatient, care_delivery, healthcare`
- **RACI**: `{"responsible": ["role_triage_nurse", "role_patient_access_specialist"], "accountable": ["role_attending_physician"], "consulted": ["role_patient"], "informed": ["role_rcm_director"]}`
- **Assets**: `asset_ehr_system, asset_rcm_clearinghouse, asset_pacs_lis_system`

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
---

