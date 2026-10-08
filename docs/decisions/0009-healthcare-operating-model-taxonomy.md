# ADR 0009: Healthcare Provider & Clinical Operations Taxonomy Design

## Status
Accepted

## Context
Following the establishment of the Multi-Industry Profiles Architecture (ADR-0007) and the Professional Services Domain Model (ADR-0008), the Enterprise Value Chain engine requires an operating model for the Healthcare industry (hospitals, integrated health systems, and ambulatory networks).

Unlike discrete manufacturing or professional services, healthcare operations are centered around clinical patient care delivery, clinical safety protocols, patient access, stringent regulatory mandates (HIPAA, Joint Commission, EMTALA), and the complex clinical-financial integration known as Revenue Cycle Management (RCM).

## Decision
We establish the Healthcare taxonomy overlay (`profiles/healthcare/`), defining two dedicated lifecycles, supporting healthcare roles, specialized clinical and administrative assets, value streams, governance policies, and financial triad integration points:

### 1. Lifecycles
- **Patient Access & Care Delivery (P2D)**: Clinical care delivery and patient journey:
  - `p2d_001_patient_registration_scheduling`: Patient identity verification, Enterprise Master Patient Index (EMPI) lookup, and appointment scheduling.
  - `p2d_002_insurance_verification_prior_auth`: Real-time insurance eligibility (EDI 270/271) and clinical prior authorization (EDI 278).
  - `p2d_003_clinical_admission_triage`: Emergency triage (ESI score), clinical intake assessment, and inpatient bed placement.
  - `p2d_004_care_delivery_order_execution`: Computerized Provider Order Entry (CPOE), medication administration (eMAR), diagnostic imaging, and bedside care.
  - `p2d_005_discharge_planning_transition`: Discharge coordination, medication reconciliation, transition of care summary, and discharge disposition.
- **Revenue Cycle Management (RCM)**: Clinical-financial translation and claim-to-remittance lifecycle:
  - `rcm_001_charge_capture_coding`: Clinical documentation improvement (CDI), charge reconciliation, and ICD-10-CM/PCS & CPT/HCPCS medical coding.
  - `rcm_002_claim_scrubbing_submission`: NCCI and payer edit validation, electronic 837 claim batching, and clearinghouse submission.
  - `rcm_003_payer_adjudication_remittance`: Payer adjudication, electronic remittance advice (ERA / EDI 835) ingestion, and contractual allowance posting.
  - `rcm_004_denial_management_appeals`: CARC/RARC denial triage, clinical appeals submission, and underpayment recovery.
  - `rcm_005_patient_billing_collections`: Patient financial balance calculation, statement generation, payment plans, and charity care evaluation.
  - `rcm_006_cash_posting_reconciliation`: Bank deposit reconciliation, zero-balance write-offs, and automated subledger posting to General Ledger.

### 2. Roles & Governance
- `role_attending_physician`: Clinical care authority, CPOE order placement, and clinical discharge certification.
- `role_triage_nurse`: Bedside clinical assessment, triage acuity scoring, and bedside medication administration.
- `role_patient_access_specialist`: Patient demographic registration, copay collection, and insurance eligibility validation.
- `role_medical_coder`: HIM medical coding, chart review, DRG/APC optimization, and coding denial resolution.
- `role_rcm_director`: Revenue cycle operations, financial adjustment and bad debt write-off authorization ($250,000 USD limit).
- `role_compliance_officer`: HIPAA privacy, EMTALA oversight, and billing compliance audit authority.
- `role_patient`: Healthcare consumer receiving clinical care and receiving patient balance statements.

### 3. IT Assets
- `asset_ehr_system`: Electronic Health Record platform (e.g. Epic Systems, Oracle Health / Cerner) providing clinical documentation, CPOE, and inpatient tracking.
- `asset_rcm_clearinghouse`: Healthcare EDI clearinghouse & revenue cycle platform (e.g. Waystar, Change Healthcare, Availity) managing EDI 270/271, 278, 837, and 835 transactions.
- `asset_pacs_lis_system`: Diagnostic Picture Archiving and Communication System (PACS) & Laboratory Information System (LIS).

### 4. Integration with Core Financial Triad
- `rcm_006_cash_posting_reconciliation` feeds directly into `r2r_001_journal_entry_recording` in the core Record-to-Report ledger.
- Inherited `s2p_006_goods_services_receipt` patches directly into `p2d_004_care_delivery_order_execution` for medical and surgical supplies.
- Inherited `h2r_004_payroll_benefits_enrollment` supports clinical nursing and medical staff payroll operations.

## Consequences
- Extends the multi-industry architecture to support healthcare providers and clinical health systems alongside manufacturing and professional services.
- Maintains schema compliance and full compatibility with existing simulation, visualizer, and validation tools.
