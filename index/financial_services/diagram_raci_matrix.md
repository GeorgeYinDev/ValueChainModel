# Enterprise RACI Governance Matrix [ALL]

> **RACI Legend**: **R** = Responsible (Executes) | **A** = Accountable (Approves) | **C** = Consulted (Inputs) | **I** = Informed (Notified)

## 1. Value Chain Process RACI Grid

| Step ID | Process Step Name | Accounts Payable Clerk | Billing & Accounts Receivable Specialist | BSA / AML Chief Compliance Officer | Category Manager | Chief Credit Officer (CCO) | Compensation Analyst | Financial Consolidation Specialist | Credit & Risk Manager | Commercial Credit Underwriter | Enterprise Customer | Finance Controller | General Ledger Accountant | Hiring Manager | HR Business Partner | Internal Auditor | KYC & AML Compliance Analyst | Loan Closing & Servicing Specialist | Payroll Specialist | Procurement Specialist | Commercial Relationship Manager | Sales Operations Specialist | Supplier / Vendor | Talent Acquisition Specialist | Treasury & Settlement Operations Officer |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `c2a_001_prospect_application_intake` | **Prospect Application & Entity Intake** | - | - | **A** | - | - | - | - | - | - | C | - | - | - | - | - | I | - | - | - | **R** | - | - | - | - |
| `c2a_002_kyc_cip_identity_verification` | **KYC/CIP Identity & UBO Verification** | - | - | **A** | - | - | - | - | - | - | C | - | - | - | - | - | **R** | - | - | - | C | - | - | - | I |
| `c2a_003_aml_sanctions_pep_screening` | **AML Sanctions, PEP & Adverse Media Screening** | - | - | **A** | - | - | - | - | - | - | - | - | - | - | - | C | **R** | - | - | - | I | - | - | - | - |
| `c2a_004_enhanced_due_diligence_compliance` | **Enhanced Due Diligence (EDD) & BSA Approval** | - | - | **A** | - | - | - | - | - | - | - | - | - | - | - | I | **R** | - | - | - | C | - | - | - | - |
| `c2a_005_account_provisioning_core_activation` | **Core Account Provisioning & Treasury Activation** | - | - | - | - | - | - | - | - | - | I | - | - | - | - | - | C | **R** | - | - | I | - | - | - | **A** |
| `h2r_001_job_requisition_posting` | **Job Requisition Definition & Posting** | - | - | - | - | - | C | - | - | - | - | - | - | **R**, **A** | C | - | - | - | - | - | - | - | - | I | - |
| `h2r_002_candidate_screening_interview` | **Candidate Screening & Interview Execution** | - | - | - | - | - | - | - | - | - | - | - | - | **A** | C | - | - | - | - | - | - | - | - | **R** | - |
| `h2r_003_offer_letter_onboarding` | **Offer Letter Generation & Employee Onboarding** | - | - | - | - | - | C | - | - | - | - | - | - | **A** | - | - | - | - | I | - | - | - | - | **R** | - |
| `h2r_004_payroll_benefits_enrollment` | **Payroll & Benefits Enrollment Processing** | - | - | - | - | - | - | - | - | - | - | I | - | - | C | - | - | - | **R**, **A** | - | - | - | - | - | - |
| `h2r_005_performance_compensation_review` | **Performance & Compensation Review** | - | - | - | - | - | C | - | - | - | - | - | - | **R**, **A** | C | - | - | - | I | - | - | - | - | - | - |
| `h2r_006_separation_offboarding_settlement` | **Separation, Offboarding & Final Settlement** | - | - | - | - | - | - | - | - | - | - | - | - | C | **R**, **A** | - | - | - | I | - | - | - | - | - | - |
| `l2s_001_loan_application_credit_packaging` | **Loan Application & Credit Packaging** | - | - | - | - | I | - | - | - | **A** | C | - | - | - | - | - | - | - | - | - | **R** | - | - | - | - |
| `l2s_002_credit_underwriting_risk_rating` | **Credit Underwriting & PD/LGD Risk Rating** | - | - | - | - | **A** | - | - | C | **R** | I | - | - | - | - | - | - | - | - | - | C | - | - | - | - |
| `l2s_003_collateral_valuation_lien_perfection` | **Collateral Valuation & Lien Perfection** | - | - | - | - | **A** | - | - | - | C | C | - | - | - | - | - | - | **R** | - | - | - | - | - | - | I |
| `l2s_004_loan_booking_funding_disbursement` | **Loan Booking & Principal Funding Disbursement** | - | - | - | - | - | - | - | - | C | I | - | - | - | - | - | - | **R** | - | - | I | - | - | - | **A** |
| `l2s_005_repayment_servicing_covenant_monitoring` | **Repayment Servicing & Covenant Monitoring** | - | - | - | - | **A** | - | - | - | **R** | I | I | - | - | - | - | - | **R** | - | - | C | - | - | - | - |
| `l2s_006_delinquency_workout_ledger_settlement` | **Delinquency Workout & Subledger Reconciliation** | - | - | - | - | C | - | - | - | - | - | **A** | I | - | - | I | - | **R** | - | - | - | - | - | - | C |
| `r2r_001_journal_entry_recording` | **General Ledger Journal Recording & Subledger Ingestion** | C | C | - | - | - | - | - | - | - | - | **A** | **R** | - | - | I | - | - | - | - | - | - | - | - | - |
| `r2r_002_intercompany_reconciliation` | **Intercompany Transaction Matching & Elimination** | - | - | - | - | - | - | **R** | - | - | - | **A** | C | - | - | I | - | - | - | - | - | - | - | - | - |
| `r2r_003_balance_sheet_substantiation` | **Balance Sheet Account Substantiation & Reconciliation** | - | - | - | - | - | - | C | - | - | - | **A** | **R** | - | - | I | - | - | - | - | - | - | - | - | - |
| `r2r_004_financial_close_consolidation` | **Financial Close Orchestration & Group Consolidation** | - | - | - | - | - | - | **R** | - | - | - | **A** | C | - | - | I | - | - | - | - | - | - | - | - | - |
| `r2r_005_statutory_financial_reporting` | **Statutory, Tax & Management Financial Reporting** | - | - | - | - | - | - | **R** | - | - | - | **A** | I | - | - | C | - | - | - | - | - | - | - | - | - |
| `s2p_001_spend_analysis_need_id` | **Spend Analysis & Need Identification** | - | - | - | **A** | - | - | - | - | - | - | C | - | - | - | - | - | - | - | **R** | - | - | I | - | - |
| `s2p_002_supplier_discovery_qualification` | **Supplier Discovery & Qualification** | - | - | - | **A** | - | - | - | - | - | - | C | - | - | - | - | - | - | - | **R** | - | - | I | - | - |
| `s2p_003_sourcing_rfx_auction` | **Strategic Sourcing & RFx Execution** | - | - | - | **A** | - | - | - | - | - | - | C | - | - | - | - | - | - | - | **R** | - | - | I | - | - |
| `s2p_004_contracting_sla_negotiation` | **Contracting & SLA Negotiation** | - | - | - | **R**, **A** | - | - | - | - | - | - | C | - | - | - | - | - | - | - | - | - | - | I | - | - |
| `s2p_005_purchase_requisition_po` | **Purchase Requisition & PO Issuance** | - | - | - | **A** | - | - | - | - | - | - | C | - | - | - | - | - | - | - | **R** | - | - | I | - | - |
| `s2p_006_goods_services_receipt` | **Goods & Services Receipt Verification** | C | - | - | **A** | - | - | - | - | - | - | - | - | - | - | - | - | - | - | **R** | - | - | I | - | - |
| `s2p_007_invoice_verification_matching` | **Invoice 3-Way Matching & Exception Handling** | **R** | - | - | - | - | - | - | - | - | - | **A** | - | - | - | - | - | - | - | C | - | - | I | - | - |
| `s2p_008_payment_settlement_disbursement` | **Payment Settlement & Disbursement** | **R** | - | - | C | - | - | - | - | - | - | **A** | - | - | - | - | - | - | - | - | - | - | I | - | - |

---

## 2. Role Workload & Touchpoint Distribution

| Enterprise Role | Responsible (R) | Accountable (A) | Consulted (C) | Informed (I) | Total Touchpoints | Operational Load |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Accounts Payable Clerk** (`role_accounts_payable_clerk`) | 2 | 0 | 2 | 0 | **4** | 🟡 Moderate |
| **Billing & Accounts Receivable Specialist** (`role_billing_specialist`) | 0 | 0 | 1 | 0 | **1** | 🟢 Low |
| **BSA / AML Chief Compliance Officer** (`role_bsa_compliance_officer`) | 0 | 4 | 0 | 0 | **4** | 🟡 Moderate |
| **Category Manager** (`role_category_manager`) | 1 | 6 | 1 | 0 | **8** | 🔴 High (Key Dependency) |
| **Chief Credit Officer (CCO)** (`role_chief_credit_officer`) | 0 | 3 | 1 | 1 | **5** | 🟡 Moderate |
| **Compensation Analyst** (`role_compensation_analyst`) | 0 | 0 | 3 | 0 | **3** | 🟢 Low |
| **Financial Consolidation Specialist** (`role_consolidation_specialist`) | 3 | 0 | 1 | 0 | **4** | 🔴 High (Key Dependency) |
| **Credit & Risk Manager** (`role_credit_manager`) | 0 | 0 | 1 | 0 | **1** | 🟢 Low |
| **Commercial Credit Underwriter** (`role_credit_underwriter`) | 2 | 1 | 2 | 0 | **5** | 🟡 Moderate |
| **Enterprise Customer** (`role_customer`) | 0 | 0 | 4 | 4 | **8** | 🔴 High (Key Dependency) |
| **Finance Controller** (`role_finance_controller`) | 0 | 8 | 5 | 2 | **15** | 🔴 High (Key Dependency) |
| **General Ledger Accountant** (`role_general_ledger_accountant`) | 2 | 0 | 2 | 2 | **6** | 🔴 High (Key Dependency) |
| **Hiring Manager** (`role_hiring_manager`) | 2 | 4 | 1 | 0 | **7** | 🔴 High (Key Dependency) |
| **HR Business Partner** (`role_hr_business_partner`) | 1 | 1 | 4 | 0 | **6** | 🔴 High (Key Dependency) |
| **Internal Auditor** (`role_internal_auditor`) | 0 | 0 | 2 | 6 | **8** | 🔴 High (Key Dependency) |
| **KYC & AML Compliance Analyst** (`role_kyc_aml_analyst`) | 3 | 0 | 1 | 1 | **5** | 🔴 High (Key Dependency) |
| **Loan Closing & Servicing Specialist** (`role_loan_servicing_specialist`) | 5 | 0 | 0 | 0 | **5** | 🔴 High (Key Dependency) |
| **Payroll Specialist** (`role_payroll_specialist`) | 1 | 1 | 0 | 3 | **5** | 🟡 Moderate |
| **Procurement Specialist** (`role_procurement_specialist`) | 5 | 0 | 1 | 0 | **6** | 🔴 High (Key Dependency) |
| **Commercial Relationship Manager** (`role_relationship_manager`) | 2 | 0 | 4 | 3 | **9** | 🔴 High (Key Dependency) |
| **Sales Operations Specialist** (`role_sales_ops_specialist`) | 0 | 0 | 0 | 0 | **0** | 🟢 Low |
| **Supplier / Vendor** (`role_supplier`) | 0 | 0 | 0 | 8 | **8** | 🔴 High (Key Dependency) |
| **Talent Acquisition Specialist** (`role_talent_acquisition_specialist`) | 2 | 0 | 0 | 1 | **3** | 🟡 Moderate |
| **Treasury & Settlement Operations Officer** (`role_treasury_operations_officer`) | 0 | 2 | 1 | 2 | **5** | 🟡 Moderate |

---

## 3. Segregation of Duties (SoD) & Conflict Analysis

⚠️ **Potential Segregation of Duties (SoD) Overlaps Detected:**

- **Step `h2r_001_job_requisition_posting` (Job Requisition Definition & Posting)**: Role `role_hiring_manager` is listed as both Responsible and Accountable.
- **Step `h2r_004_payroll_benefits_enrollment` (Payroll & Benefits Enrollment Processing)**: Role `role_payroll_specialist` is listed as both Responsible and Accountable.
- **Step `h2r_005_performance_compensation_review` (Performance & Compensation Review)**: Role `role_hiring_manager` is listed as both Responsible and Accountable.
- **Step `h2r_006_separation_offboarding_settlement` (Separation, Offboarding & Final Settlement)**: Role `role_hr_business_partner` is listed as both Responsible and Accountable.
- **Step `s2p_004_contracting_sla_negotiation` (Contracting & SLA Negotiation)**: Role `role_category_manager` is listed as both Responsible and Accountable.