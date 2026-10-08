# System Prompt: LLM Context Blueprint for Business Lifecycle [Revenue Cycle Management]

> Profile: `healthcare` | Lifecycle ID: `RCM` | Version: `1.0.0` | Source Layer: `healthcare`
> Description: Charge capture, medical coding, electronic claim clearinghouse scrubbing, remittance processing, and cash reconciliation.

## Milestone Process Sequence
- **Step 1**: `rcm_001_charge_capture_coding` (Charge Capture & Medical Coding)
- **Step 2**: `rcm_002_claim_scrubbing_submission` (Claim Scrubbing & Clearinghouse Submission)
- **Step 3**: `rcm_003_payer_adjudication_remittance` (Payer Adjudication & Remittance)
- **Step 4**: `rcm_004_denial_management_appeals` (Denial Management & Appeals)
- **Step 5**: `rcm_005_patient_billing_collections` (Patient Billing & Collections)
- **Step 6**: `rcm_006_cash_posting_reconciliation` (Cash Posting & Subledger Reconciliation)

## Key Performance Indicators (KPIs)
- `Days in Accounts Receivable (A/R)`
- `Initial Claim Denial Rate`
- `Clean Claim Rate`
- `Net Collection Rate`

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

### [HIPAA ANSI X12N 837 Electronic Healthcare Claim] (`data_837_claim_file`) [Layer: `healthcare`]
- **Type**: `data_entity` | **Tags**: `data, claims, edi837, rcm, billing, healthcare`
- **RACI**: `{}`
- **Assets**: ``

# Data Entity: HIPAA ANSI X12N 837 Electronic Healthcare Claim

The electronic transaction file (837I for Institutional / Hospital billing or 837P for Professional billing) transmitting diagnosis codes, procedure codes, billed charges, and clinical service details to third-party payers.
---

### [Net Days in Accounts Receivable (A/R)] (`kpi_days_in_ar`) [Layer: `healthcare`]
- **Type**: `kpi_metric` | **Tags**: `kpi, rcm, ar_days, cash_flow, healthcare`
- **RACI**: `{}`
- **Assets**: ``

# KPI: Net Days in Accounts Receivable (A/R)

Measures the average number of calendar days between discharge/service delivery and the final cash settlement and remittance reconciliation of patient and payer balances.
---

### [Initial Claim Denial Rate] (`kpi_initial_denial_rate`) [Layer: `healthcare`]
- **Type**: `kpi_metric` | **Tags**: `kpi, rcm, denials, claims, healthcare`
- **RACI**: `{}`
- **Assets**: ``

# KPI: Initial Claim Denial Rate

Measures the percentage of submitted electronic healthcare claims that are initially denied or rejected upon first adjudication by commercial or government payers.
---

### [Charge Capture & Medical Coding] (`rcm_001_charge_capture_coding`) [Layer: `healthcare`]
- **Type**: `process_step` | **Tags**: `coding, him, icd10, cpt, charges, rcm`
- **RACI**: `{"responsible": ["role_medical_coder"], "accountable": ["role_rcm_director"], "consulted": ["role_attending_physician"], "informed": ["role_compliance_officer"]}`
- **Assets**: `asset_ehr_system, asset_rcm_clearinghouse`

# Charge Capture & Medical Coding

Aggregates clinical documentation, surgical operative notes, and pharmacy charges to assign compliant ICD-10-CM diagnosis codes, ICD-10-PCS / CPT procedure codes, and MS-DRG grouping.
---

### [Claim Scrubbing & Clearinghouse Submission] (`rcm_002_claim_scrubbing_submission`) [Layer: `healthcare`]
- **Type**: `process_step` | **Tags**: `claims, scrubbing, edi837, clearinghouse, billing`
- **RACI**: `{"responsible": ["role_medical_coder"], "accountable": ["role_rcm_director"], "consulted": ["role_patient_access_specialist"], "informed": ["role_compliance_officer"]}`
- **Assets**: `asset_rcm_clearinghouse`

# Claim Scrubbing & Clearinghouse Submission

Applies National Correct Coding Initiative (NCCI) edits, medical necessity validation checks, and commercial payer formatting rules prior to electronic EDI 837 claim transmission via the clearinghouse.
---

### [Payer Adjudication & Remittance] (`rcm_003_payer_adjudication_remittance`) [Layer: `healthcare`]
- **Type**: `process_step` | **Tags**: `adjudication, era, edi835, remittance, payer`
- **RACI**: `{"responsible": ["role_billing_specialist"], "accountable": ["role_rcm_director"], "consulted": ["role_medical_coder"], "informed": ["role_finance_controller"]}`
- **Assets**: `asset_rcm_clearinghouse`

# Payer Adjudication & Remittance

Receives Electronic Remittance Advice (ERA / EDI 835) files from commercial health plans, Medicare Administrative Contractors (MAC), and Medicaid programs detailing allowed amounts, contractual discounts, and patient cost-shares.
---

### [Denial Management & Appeals] (`rcm_004_denial_management_appeals`) [Layer: `healthcare`]
- **Type**: `process_step` | **Tags**: `denials, appeals, carc, rarc, rcm`
- **RACI**: `{"responsible": ["role_medical_coder"], "accountable": ["role_rcm_director"], "consulted": ["role_attending_physician"], "informed": ["role_compliance_officer"]}`
- **Assets**: `asset_rcm_clearinghouse, asset_ehr_system`

# Denial Management & Appeals

Analyzes Claim Adjustment Reason Codes (CARC) and Remittance Advice Remark Codes (RARC), correcting technical billing errors, submitting clinical chart appeals, and coordinating peer-to-peer provider reviews.
---

### [Patient Billing & Collections] (`rcm_005_patient_billing_collections`) [Layer: `healthcare`]
- **Type**: `process_step` | **Tags**: `patient_billing, statements, collections, rcm`
- **RACI**: `{"responsible": ["role_billing_specialist"], "accountable": ["role_rcm_director"], "consulted": ["role_patient"], "informed": ["role_compliance_officer"]}`
- **Assets**: `asset_rcm_clearinghouse, asset_ehr_system`

# Patient Billing & Collections

Calculates adjudicated patient out-of-pocket responsibility, issues paper and digital statements, administers financial assistance / sliding-scale charity care, and collects outstanding balances.
---

### [Cash Posting & Subledger Reconciliation] (`rcm_006_cash_posting_reconciliation`) [Layer: `healthcare`]
- **Type**: `process_step` | **Tags**: `cash_posting, reconciliation, subledger, r2r, rcm`
- **RACI**: `{"responsible": ["role_billing_specialist"], "accountable": ["role_finance_controller"], "consulted": ["role_rcm_director"], "informed": ["role_general_ledger_accountant"]}`
- **Assets**: `asset_rcm_clearinghouse, asset_erp_system`

# Cash Posting & Subledger Reconciliation

Matches electronic lockbox and electronic funds transfers (EFT) against 835 remittance data, posts adjustments/contractuals, balances hospital patient accounting subledgers, and posts cash journal entries to the corporate General Ledger.
---

### [Hospital Revenue Cycle & Cash Reconciliation Value Stream] (`hospital_revenue_cycle_stream`) [Layer: `healthcare`]
- **Type**: `value_stream` | **Tags**: `value_stream, rcm, billing, cash_posting, finance, healthcare`
- **RACI**: `{"responsible": ["role_medical_coder", "role_billing_specialist"], "accountable": ["role_rcm_director"], "consulted": ["role_attending_physician"], "informed": ["role_finance_controller"]}`
- **Assets**: `asset_rcm_clearinghouse, asset_ehr_system, asset_erp_system`

# Value Stream: Hospital Revenue Cycle & Cash Reconciliation (RCM)

## Executive Summary
Translates clinical inpatient and outpatient encounters into reimbursable claims, governs electronic transaction exchange with clearinghouses and payers, recovers denied revenue, and reconciles electronic funds transfers into corporate General Ledger accounting.

## 1. Strategic Outcomes (Tier 1 - Executive Level)
- **Accelerate Cash Liquidity & DSO Control**: Target net Days in A/R <= 38.0 days through automated claim scrubbing and electronic remittance posting.
- **Minimize Revenue Leakage**: Maintain Initial Claim Denial Rate <= 5.0% and achieve clean claim rates > 95%.
- **Core Financial Triad Integration**: Direct feed from cash posting (`rcm_006`) into General Ledger journal voucher recording (`r2r_001_journal_entry_recording`).

## 2. Included Steps & RACI Summary (Tier 2 - Process Architect Level)
1. `rcm_001_charge_capture_coding` - Clinical Charge Capture & ICD-10 Coding
2. `rcm_002_claim_scrubbing_submission` - EDI 837 Claim Transmission
3. `rcm_003_payer_adjudication_remittance` - EDI 835 Remittance Advice Ingestion
4. `rcm_004_denial_management_appeals` - Root-Cause Denial Appeals
5. `rcm_005_patient_billing_collections` - Patient Responsibility Invoicing
6. `rcm_006_cash_posting_reconciliation` - Bank Reconciliation & GL Journal Posting

## 3. Systems Architecture (Tier 3 - Systems Engineer Level)
- **Clearinghouse & EDI Gateway**: Revenue Cycle Platform (`asset_rcm_clearinghouse`).
- **Core Financial System**: Enterprise Resource Planning General Ledger (`asset_erp_system`).
---

