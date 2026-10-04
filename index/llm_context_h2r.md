# System Prompt: LLM Context Blueprint for Business Lifecycle [Hire to Retire Lifecycle]

> Lifecycle ID: `H2R` | Version: `1.0.0`
> Description: End-to-end human capital operations from job requisition and candidate screening through onboarding, payroll integration, performance review, and final offboarding.

## Milestone Process Sequence
- **Step 1**: `h2r_001_job_requisition_posting` (Job Requisition Definition & Posting)
- **Step 2**: `h2r_002_candidate_screening_interview` (Candidate Screening & Interview Execution)
- **Step 3**: `h2r_003_offer_letter_onboarding` (Offer Letter Generation & Employee Onboarding)
- **Step 4**: `h2r_004_payroll_benefits_enrollment` (Payroll & Benefits Enrollment Processing)
- **Step 5**: `h2r_005_performance_compensation_review` (Performance & Compensation Review)
- **Step 6**: `h2r_006_separation_offboarding_settlement` (Separation, Offboarding & Final Settlement)

## Key Performance Indicators (KPIs)
- `time_to_fill_days`
- `cost_per_hire`
- `first_year_attrition_rate`
- `payroll_accuracy_percentage`

## Active Value Chain Elements Knowledge Base

### [Performance & Compensation Review] (`h2r_005_performance_compensation_review`)
- **Type**: `process_step` | **Tags**: `hr, performance, compensation`
- **RACI**: `{"responsible": ["role_hiring_manager"], "accountable": ["role_hiring_manager"], "consulted": ["role_hr_business_partner", "role_compensation_analyst"], "informed": ["role_payroll_specialist"]}`
- **Assets**: `asset_hcm_platform`



# Process Step: Performance & Compensation Review

## Executive Summary
Executes the annual or bi-annual performance evaluation cycle, calibrates ratings, and applies merit increases or promotions.

## 1. Strategic Intent & Outcome (Tier 1 - Executive Level)
- **Business Value**: Drives talent retention, rewards high performers, and aligns compensation with market rates.
- **Risk Exposure**: Unfair evaluations, budget overruns on merit pools, or attrition of top talent.

## 2. Operational Workflow (Tier 2)
- Employee and manager complete self and manager evaluations.
- HRBP facilitates calibration sessions to normalize ratings.
- Compensation analyst distributes merit budget pools.
- Managers allocate merit and bonuses; HR approves final payout files.

---

### [Separation, Offboarding & Final Settlement] (`h2r_006_separation_offboarding_settlement`)
- **Type**: `process_step` | **Tags**: `hr, offboarding, payroll`
- **RACI**: `{"responsible": ["role_hr_business_partner"], "accountable": ["role_hr_business_partner"], "consulted": ["role_hiring_manager"], "informed": ["role_payroll_specialist"]}`
- **Assets**: `asset_hcm_platform, asset_payroll_engine`



# Process Step: Separation, Offboarding & Final Settlement

## Executive Summary
Manages the voluntary or involuntary termination process, disables systems access, and calculates final paycheck and severance settlements.

## 1. Strategic Intent & Outcome (Tier 1 - Executive Level)
- **Business Value**: Mitigates security risks by revoking access and ensures compliance with final pay labor laws.
- **Risk Exposure**: Data breaches from lingering access, or legal penalties for late final paychecks.

## 2. Operational Workflow (Tier 2)
- HRBP processes termination event in HCM platform.
- Automated triggers revoke IT access and notify facilities.
- Payroll calculates final accrued PTO, severance, and regular wages.
- Final settlement is paid and general ledger is updated.

---

### [Offer Letter Generation & Employee Onboarding] (`h2r_003_offer_letter_onboarding`)
- **Type**: `process_step` | **Tags**: `hr, offer, onboarding`
- **RACI**: `{"responsible": ["role_talent_acquisition_specialist"], "accountable": ["role_hiring_manager"], "consulted": ["role_compensation_analyst"], "informed": ["role_payroll_specialist"]}`
- **Assets**: `asset_hcm_platform`



# Process Step: Offer Letter Generation & Employee Onboarding

## Executive Summary
Drafts the formal employment offer, secures necessary compensation approvals, initiates background checks, and provisions the employee profile upon acceptance.

## 1. Strategic Intent & Outcome (Tier 1 - Executive Level)
- **Business Value**: Secures the candidate and ensures compliance with labor laws during provisioning.
- **Risk Exposure**: Offer rejection due to delays, or provisioning errors causing Day 1 productivity loss.

## 2. Operational Workflow (Tier 2)
- Recruiter drafts the offer package based on standard bands.
- Out-of-band offers route to `role_compensation_analyst`.
- Candidate digitally signs the offer.
- Background check clears and the worker profile is activated in HCM.

---

### [Job Requisition Definition & Posting] (`h2r_001_job_requisition_posting`)
- **Type**: `process_step` | **Tags**: `hr, recruitment, planning`
- **RACI**: `{"responsible": ["role_hiring_manager"], "accountable": ["role_hiring_manager"], "consulted": ["role_hr_business_partner", "role_compensation_analyst"], "informed": ["role_talent_acquisition_specialist"]}`
- **Assets**: `asset_hcm_platform`



# Process Step: Job Requisition Definition & Posting

## Executive Summary
Defines headcount requirements, establishes the compensation band, and opens the job requisition within the HCM platform to formally initiate the recruitment cycle.

## 1. Strategic Intent & Outcome (Tier 1 - Executive Level)
- **Business Value**: Ensures headcount growth aligns with approved budget plans.
- **Risk Exposure**: Unbudgeted hiring or misaligned compensation benchmarking leading to pay inequity.

## 2. Operational Workflow (Tier 2)
- Hiring manager drafts the job description and submits the requisition.
- Compensation analyst reviews and attaches a salary band.
- Requisition goes live on internal and external career portals.

---

### [Payroll & Benefits Enrollment Processing] (`h2r_004_payroll_benefits_enrollment`)
- **Type**: `process_step` | **Tags**: `hr, payroll, benefits, finance`
- **RACI**: `{"responsible": ["role_payroll_specialist"], "accountable": ["role_payroll_specialist"], "consulted": ["role_hr_business_partner"], "informed": ["role_finance_controller"]}`
- **Assets**: `asset_payroll_engine, asset_hcm_platform`



# Process Step: Payroll & Benefits Enrollment Processing

## Executive Summary
Establishes the employee's direct deposit, tax withholdings, and benefits elections, integrating them into the ongoing payroll cycles.

## 1. Strategic Intent & Outcome (Tier 1 - Executive Level)
- **Business Value**: Ensures accurate and timely compensation, maintaining employee trust and regulatory compliance.
- **Risk Exposure**: Incorrect tax withholdings, missed benefit enrollments, or payroll errors causing financial misstatements.

## 2. Operational Workflow (Tier 2)
- Employee completes self-service onboarding forms (W-4, I-9, benefits).
- Payroll specialist verifies data flow from HCM to Payroll Engine.
- Payroll engine calculates gross-to-net and triggers disbursement.
- Payroll generates aggregated expense and liability journals, feeding into `r2r_001_journal_entry_recording`.

---

### [Candidate Screening & Interview Execution] (`h2r_002_candidate_screening_interview`)
- **Type**: `process_step` | **Tags**: `hr, recruitment, interview`
- **RACI**: `{"responsible": ["role_talent_acquisition_specialist"], "accountable": ["role_hiring_manager"], "consulted": ["role_hr_business_partner"], "informed": []}`
- **Assets**: `asset_hcm_platform`



# Process Step: Candidate Screening & Interview Execution

## Executive Summary
Sources applicants, screens resumes, coordinates interview panels, and synthesizes feedback to select a final candidate for an offer.

## 1. Strategic Intent & Outcome (Tier 1 - Executive Level)
- **Business Value**: Identifies top talent to drive enterprise objectives.
- **Risk Exposure**: High candidate drop-off rate or poor candidate experience.

## 2. Operational Workflow (Tier 2)
- Recruiter screens inbound applications and sourced prospects.
- Recruiter conducts phone screens and schedules panel interviews.
- Hiring manager and panel execute interviews and submit scorecards.
- Hiring decision is made; unselected candidates are notified.

---

