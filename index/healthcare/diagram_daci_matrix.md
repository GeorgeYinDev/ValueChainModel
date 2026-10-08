# Enterprise DACI Decision Governance Matrix [ALL]

> **DACI Legend**: **D** = Driver (Orchestrates/Leads) | **A** = Approver (Sole Sign-off/Veto) | **C** = Contributor (Advises/Consulted) | **I** = Informed (Notified)

## 1. Value Chain Process DACI Grid

| Step ID | Process Step Name | Accounts Payable Clerk | Billing Specialist | Category Manager | Compensation Analyst | Consolidation Specialist | Credit Manager | Customer | Finance Controller | General Ledger Accountant | Hiring Manager | Hr Business Partner | Internal Auditor | Payroll Specialist | Procurement Specialist | Sales Ops Specialist | Supplier | Talent Acquisition Specialist | Attending Physician | Compliance Officer | Medical Coder | Patient | Patient Access Specialist | Rcm Director | Triage Nurse |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `h2r_001_job_requisition_posting` | **Job Requisition Definition & Posting** | - | - | - | C | - | - | - | - | - | **D**, **A** | C | - | - | - | - | - | I | - | - | - | - | - | - | - |
| `h2r_002_candidate_screening_interview` | **Candidate Screening & Interview Execution** | - | - | - | - | - | - | - | - | - | **A** | C | - | - | - | - | - | **D** | - | - | - | - | - | - | - |
| `h2r_003_offer_letter_onboarding` | **Offer Letter Generation & Employee Onboarding** | - | - | - | C | - | - | - | - | - | **A** | - | - | I | - | - | - | **D** | - | - | - | - | - | - | - |
| `h2r_004_payroll_benefits_enrollment` | **Payroll & Benefits Enrollment Processing** | - | - | - | - | - | - | - | I | - | - | C | - | **D**, **A** | - | - | - | - | - | - | - | - | - | - | - |
| `h2r_005_performance_compensation_review` | **Performance & Compensation Review** | - | - | - | C | - | - | - | - | - | **D**, **A** | C | - | I | - | - | - | - | - | - | - | - | - | - | - |
| `h2r_006_separation_offboarding_settlement` | **Separation, Offboarding & Final Settlement** | - | - | - | - | - | - | - | - | - | C | **D**, **A** | - | I | - | - | - | - | - | - | - | - | - | - | - |
| `p2d_001_patient_registration_scheduling` | **Patient Registration & Scheduling** | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | C | **D** | **A** | I |
| `p2d_002_insurance_verification_prior_auth` | **Insurance Verification & Prior Authorization** | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | C | - | - | I | **D** | **A** | - |
| `p2d_003_clinical_admission_triage` | **Clinical Admission & Triage** | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | **A** | - | - | I | C | - | **D** |
| `p2d_004_care_delivery_order_execution` | **Care Delivery & Order Execution** | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | **A** | - | C | I | - | - | **D** |
| `p2d_005_discharge_planning_transition` | **Discharge Planning & Care Transition** | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | **A** | - | - | C | - | I | **D** |
| `r2r_001_journal_entry_recording` | **General Ledger Journal Recording & Subledger Ingestion** | C | C | - | - | - | - | - | **A** | **D** | - | - | I | - | - | - | - | - | - | - | - | - | - | - | - |
| `r2r_002_intercompany_reconciliation` | **Intercompany Transaction Matching & Elimination** | - | - | - | - | **D** | - | - | **A** | C | - | - | I | - | - | - | - | - | - | - | - | - | - | - | - |
| `r2r_003_balance_sheet_substantiation` | **Balance Sheet Account Substantiation & Reconciliation** | - | - | - | - | C | - | - | **A** | **D** | - | - | I | - | - | - | - | - | - | - | - | - | - | - | - |
| `r2r_004_financial_close_consolidation` | **Financial Close Orchestration & Group Consolidation** | - | - | - | - | **D** | - | - | **A** | C | - | - | I | - | - | - | - | - | - | - | - | - | - | - | - |
| `r2r_005_statutory_financial_reporting` | **Statutory, Tax & Management Financial Reporting** | - | - | - | - | **D** | - | - | **A** | I | - | - | C | - | - | - | - | - | - | - | - | - | - | - | - |
| `rcm_001_charge_capture_coding` | **Charge Capture & Medical Coding** | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | C | I | **D** | - | - | **A** | - |
| `rcm_002_claim_scrubbing_submission` | **Claim Scrubbing & Clearinghouse Submission** | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | I | **D** | - | C | **A** | - |
| `rcm_003_payer_adjudication_remittance` | **Payer Adjudication & Remittance** | - | **D** | - | - | - | - | - | I | - | - | - | - | - | - | - | - | - | - | - | C | - | - | **A** | - |
| `rcm_004_denial_management_appeals` | **Denial Management & Appeals** | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | C | I | **D** | - | - | **A** | - |
| `rcm_005_patient_billing_collections` | **Patient Billing & Collections** | - | **D** | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | I | - | C | - | **A** | - |
| `rcm_006_cash_posting_reconciliation` | **Cash Posting & Subledger Reconciliation** | - | **D** | - | - | - | - | - | **A** | I | - | - | - | - | - | - | - | - | - | - | - | - | - | C | - |
| `s2p_001_spend_analysis_need_id` | **Spend Analysis & Need Identification** | - | - | **A** | - | - | - | - | C | - | - | - | - | - | **D** | - | I | - | - | - | - | - | - | - | - |
| `s2p_002_supplier_discovery_qualification` | **Supplier Discovery & Qualification** | - | - | **A** | - | - | - | - | C | - | - | - | - | - | **D** | - | I | - | - | - | - | - | - | - | - |
| `s2p_003_sourcing_rfx_auction` | **Strategic Sourcing & RFx Execution** | - | - | **A** | - | - | - | - | C | - | - | - | - | - | **D** | - | I | - | - | - | - | - | - | - | - |
| `s2p_004_contracting_sla_negotiation` | **Contracting & SLA Negotiation** | - | - | **D**, **A** | - | - | - | - | C | - | - | - | - | - | - | - | I | - | - | - | - | - | - | - | - |
| `s2p_005_purchase_requisition_po` | **Purchase Requisition & PO Issuance** | - | - | **A** | - | - | - | - | C | - | - | - | - | - | **D** | - | I | - | - | - | - | - | - | - | - |
| `s2p_006_goods_services_receipt` | **Goods & Services Receipt Verification** | C | - | **A** | - | - | - | - | - | - | - | - | - | - | **D** | - | I | - | - | - | - | - | - | - | - |
| `s2p_007_invoice_verification_matching` | **Invoice 3-Way Matching & Exception Handling** | **D** | - | - | - | - | - | - | **A** | - | - | - | - | - | C | - | I | - | - | - | - | - | - | - | - |
| `s2p_008_payment_settlement_disbursement` | **Payment Settlement & Disbursement** | **D** | - | C | - | - | - | - | **A** | - | - | - | - | - | - | - | I | - | - | - | - | - | - | - | - |

---

## 2. Decision Authority & Driver Distribution

| Enterprise Role | Driver (D) | Approver (A) | Contributor (C) | Informed (I) | Total Decision Touchpoints | Governance Weight |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Accounts Payable Clerk** (`role_accounts_payable_clerk`) | 2 | 0 | 2 | 0 | **4** | 🟡 Operational Authority |
| **Billing Specialist** (`role_billing_specialist`) | 3 | 0 | 1 | 0 | **4** | 🔵 Primary Driver |
| **Category Manager** (`role_category_manager`) | 1 | 6 | 1 | 0 | **8** | 🚨 Key-Person Risk (Concentrated Approver) |
| **Compensation Analyst** (`role_compensation_analyst`) | 0 | 0 | 3 | 0 | **3** | 🟢 Advisory |
| **Consolidation Specialist** (`role_consolidation_specialist`) | 3 | 0 | 1 | 0 | **4** | 🔵 Primary Driver |
| **Credit Manager** (`role_credit_manager`) | 0 | 0 | 0 | 0 | **0** | 🟢 Advisory |
| **Customer** (`role_customer`) | 0 | 0 | 0 | 0 | **0** | 🟢 Advisory |
| **Finance Controller** (`role_finance_controller`) | 0 | 8 | 5 | 2 | **15** | 🚨 Key-Person Risk (Concentrated Approver) |
| **General Ledger Accountant** (`role_general_ledger_accountant`) | 2 | 0 | 2 | 2 | **6** | 🟡 Operational Authority |
| **Hiring Manager** (`role_hiring_manager`) | 2 | 4 | 1 | 0 | **7** | 🔴 Strategic Approver |
| **Hr Business Partner** (`role_hr_business_partner`) | 1 | 1 | 4 | 0 | **6** | 🟡 Operational Authority |
| **Internal Auditor** (`role_internal_auditor`) | 0 | 0 | 1 | 4 | **5** | 🟢 Advisory |
| **Payroll Specialist** (`role_payroll_specialist`) | 1 | 1 | 0 | 3 | **5** | 🟡 Operational Authority |
| **Procurement Specialist** (`role_procurement_specialist`) | 5 | 0 | 1 | 0 | **6** | 🔵 Primary Driver |
| **Sales Ops Specialist** (`role_sales_ops_specialist`) | 0 | 0 | 0 | 0 | **0** | 🟢 Advisory |
| **Supplier** (`role_supplier`) | 0 | 0 | 0 | 8 | **8** | 🟢 Advisory |
| **Talent Acquisition Specialist** (`role_talent_acquisition_specialist`) | 2 | 0 | 0 | 1 | **3** | 🟡 Operational Authority |
| **Attending Physician** (`role_attending_physician`) | 0 | 3 | 3 | 0 | **6** | 🔴 Strategic Approver |
| **Compliance Officer** (`role_compliance_officer`) | 0 | 0 | 0 | 4 | **4** | 🟢 Advisory |
| **Medical Coder** (`role_medical_coder`) | 3 | 0 | 2 | 0 | **5** | 🔵 Primary Driver |
| **Patient** (`role_patient`) | 0 | 0 | 3 | 3 | **6** | 🟢 Advisory |
| **Patient Access Specialist** (`role_patient_access_specialist`) | 2 | 0 | 2 | 0 | **4** | 🟡 Operational Authority |
| **Rcm Director** (`role_rcm_director`) | 0 | 7 | 1 | 1 | **9** | 🚨 Key-Person Risk (Concentrated Approver) |
| **Triage Nurse** (`role_triage_nurse`) | 3 | 0 | 0 | 1 | **4** | 🔵 Primary Driver |

---

## 3. Decision Governance & Single-Approver Rule Analysis

✅ **Single Approver Rule Upheld!**
Every decision milestone has exactly one designated Approver (A), preventing consensus deadlock.
