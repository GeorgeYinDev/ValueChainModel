# Enterprise DACI Decision Governance Matrix [ALL]

> **DACI Legend**: **D** = Driver (Orchestrates/Leads) | **A** = Approver (Sole Sign-off/Veto) | **C** = Contributor (Advises/Consulted) | **I** = Informed (Notified)

## 1. Value Chain Process DACI Grid

| Step ID | Process Step Name | Accounts Payable Clerk | Billing & Accounts Receivable Specialist | BSA / AML Chief Compliance Officer | Category Manager | Chief Credit Officer (CCO) | Compensation Analyst | Financial Consolidation Specialist | Credit & Risk Manager | Commercial Credit Underwriter | Enterprise Customer | Finance Controller | General Ledger Accountant | Hiring Manager | HR Business Partner | Internal Auditor | KYC & AML Compliance Analyst | Loan Closing & Servicing Specialist | Payroll Specialist | Procurement Specialist | Commercial Relationship Manager | Sales Operations Specialist | Supplier / Vendor | Talent Acquisition Specialist | Treasury & Settlement Operations Officer |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `c2a_001_prospect_application_intake` | **Prospect Application & Entity Intake** | - | - | **A** | - | - | - | - | - | - | C | - | - | - | - | - | I | - | - | - | **D** | - | - | - | - |
| `c2a_002_kyc_cip_identity_verification` | **KYC/CIP Identity & UBO Verification** | - | - | **A** | - | - | - | - | - | - | C | - | - | - | - | - | **D** | - | - | - | C | - | - | - | I |
| `c2a_003_aml_sanctions_pep_screening` | **AML Sanctions, PEP & Adverse Media Screening** | - | - | **A** | - | - | - | - | - | - | - | - | - | - | - | C | **D** | - | - | - | I | - | - | - | - |
| `c2a_004_enhanced_due_diligence_compliance` | **Enhanced Due Diligence (EDD) & BSA Approval** | - | - | **A** | - | - | - | - | - | - | - | - | - | - | - | I | **D** | - | - | - | C | - | - | - | - |
| `c2a_005_account_provisioning_core_activation` | **Core Account Provisioning & Treasury Activation** | - | - | - | - | - | - | - | - | - | I | - | - | - | - | - | C | **D** | - | - | I | - | - | - | **A** |
| `h2r_001_job_requisition_posting` | **Job Requisition Definition & Posting** | - | - | - | - | - | C | - | - | - | - | - | - | **D**, **A** | C | - | - | - | - | - | - | - | - | I | - |
| `h2r_002_candidate_screening_interview` | **Candidate Screening & Interview Execution** | - | - | - | - | - | - | - | - | - | - | - | - | **A** | C | - | - | - | - | - | - | - | - | **D** | - |
| `h2r_003_offer_letter_onboarding` | **Offer Letter Generation & Employee Onboarding** | - | - | - | - | - | C | - | - | - | - | - | - | **A** | - | - | - | - | I | - | - | - | - | **D** | - |
| `h2r_004_payroll_benefits_enrollment` | **Payroll & Benefits Enrollment Processing** | - | - | - | - | - | - | - | - | - | - | I | - | - | C | - | - | - | **D**, **A** | - | - | - | - | - | - |
| `h2r_005_performance_compensation_review` | **Performance & Compensation Review** | - | - | - | - | - | C | - | - | - | - | - | - | **D**, **A** | C | - | - | - | I | - | - | - | - | - | - |
| `h2r_006_separation_offboarding_settlement` | **Separation, Offboarding & Final Settlement** | - | - | - | - | - | - | - | - | - | - | - | - | C | **D**, **A** | - | - | - | I | - | - | - | - | - | - |
| `l2s_001_loan_application_credit_packaging` | **Loan Application & Credit Packaging** | - | - | - | - | I | - | - | - | **A** | C | - | - | - | - | - | - | - | - | - | **D** | - | - | - | - |
| `l2s_002_credit_underwriting_risk_rating` | **Credit Underwriting & PD/LGD Risk Rating** | - | - | - | - | **A** | - | - | C | **D** | I | - | - | - | - | - | - | - | - | - | C | - | - | - | - |
| `l2s_003_collateral_valuation_lien_perfection` | **Collateral Valuation & Lien Perfection** | - | - | - | - | **A** | - | - | - | C | C | - | - | - | - | - | - | **D** | - | - | - | - | - | - | I |
| `l2s_004_loan_booking_funding_disbursement` | **Loan Booking & Principal Funding Disbursement** | - | - | - | - | - | - | - | - | C | I | - | - | - | - | - | - | **D** | - | - | I | - | - | - | **A** |
| `l2s_005_repayment_servicing_covenant_monitoring` | **Repayment Servicing & Covenant Monitoring** | - | - | - | - | **A** | - | - | - | C | I | I | - | - | - | - | - | **D** | - | - | C | - | - | - | - |
| `l2s_006_delinquency_workout_ledger_settlement` | **Delinquency Workout & Subledger Reconciliation** | - | - | - | - | C | - | - | - | - | - | **A** | I | - | - | I | - | **D** | - | - | - | - | - | - | C |
| `r2r_001_journal_entry_recording` | **General Ledger Journal Recording & Subledger Ingestion** | C | C | - | - | - | - | - | - | - | - | **A** | **D** | - | - | I | - | - | - | - | - | - | - | - | - |
| `r2r_002_intercompany_reconciliation` | **Intercompany Transaction Matching & Elimination** | - | - | - | - | - | - | **D** | - | - | - | **A** | C | - | - | I | - | - | - | - | - | - | - | - | - |
| `r2r_003_balance_sheet_substantiation` | **Balance Sheet Account Substantiation & Reconciliation** | - | - | - | - | - | - | C | - | - | - | **A** | **D** | - | - | I | - | - | - | - | - | - | - | - | - |
| `r2r_004_financial_close_consolidation` | **Financial Close Orchestration & Group Consolidation** | - | - | - | - | - | - | **D** | - | - | - | **A** | C | - | - | I | - | - | - | - | - | - | - | - | - |
| `r2r_005_statutory_financial_reporting` | **Statutory, Tax & Management Financial Reporting** | - | - | - | - | - | - | **D** | - | - | - | **A** | I | - | - | C | - | - | - | - | - | - | - | - | - |
| `s2p_001_spend_analysis_need_id` | **Spend Analysis & Need Identification** | - | - | - | **A** | - | - | - | - | - | - | C | - | - | - | - | - | - | - | **D** | - | - | I | - | - |
| `s2p_002_supplier_discovery_qualification` | **Supplier Discovery & Qualification** | - | - | - | **A** | - | - | - | - | - | - | C | - | - | - | - | - | - | - | **D** | - | - | I | - | - |
| `s2p_003_sourcing_rfx_auction` | **Strategic Sourcing & RFx Execution** | - | - | - | **A** | - | - | - | - | - | - | C | - | - | - | - | - | - | - | **D** | - | - | I | - | - |
| `s2p_004_contracting_sla_negotiation` | **Contracting & SLA Negotiation** | - | - | - | **D**, **A** | - | - | - | - | - | - | C | - | - | - | - | - | - | - | - | - | - | I | - | - |
| `s2p_005_purchase_requisition_po` | **Purchase Requisition & PO Issuance** | - | - | - | **A** | - | - | - | - | - | - | C | - | - | - | - | - | - | - | **D** | - | - | I | - | - |
| `s2p_006_goods_services_receipt` | **Goods & Services Receipt Verification** | C | - | - | **A** | - | - | - | - | - | - | - | - | - | - | - | - | - | - | **D** | - | - | I | - | - |
| `s2p_007_invoice_verification_matching` | **Invoice 3-Way Matching & Exception Handling** | **D** | - | - | - | - | - | - | - | - | - | **A** | - | - | - | - | - | - | - | C | - | - | I | - | - |
| `s2p_008_payment_settlement_disbursement` | **Payment Settlement & Disbursement** | **D** | - | - | C | - | - | - | - | - | - | **A** | - | - | - | - | - | - | - | - | - | - | I | - | - |

---

## 2. Decision Authority & Driver Distribution

| Enterprise Role | Driver (D) | Approver (A) | Contributor (C) | Informed (I) | Total Decision Touchpoints | Governance Weight |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Accounts Payable Clerk** (`role_accounts_payable_clerk`) | 2 | 0 | 2 | 0 | **4** | 🟡 Operational Authority |
| **Billing & Accounts Receivable Specialist** (`role_billing_specialist`) | 0 | 0 | 1 | 0 | **1** | 🟢 Advisory |
| **BSA / AML Chief Compliance Officer** (`role_bsa_compliance_officer`) | 0 | 4 | 0 | 0 | **4** | 🔴 Strategic Approver |
| **Category Manager** (`role_category_manager`) | 1 | 6 | 1 | 0 | **8** | 🚨 Key-Person Risk (Concentrated Approver) |
| **Chief Credit Officer (CCO)** (`role_chief_credit_officer`) | 0 | 3 | 1 | 1 | **5** | 🔴 Strategic Approver |
| **Compensation Analyst** (`role_compensation_analyst`) | 0 | 0 | 3 | 0 | **3** | 🟢 Advisory |
| **Financial Consolidation Specialist** (`role_consolidation_specialist`) | 3 | 0 | 1 | 0 | **4** | 🔵 Primary Driver |
| **Credit & Risk Manager** (`role_credit_manager`) | 0 | 0 | 1 | 0 | **1** | 🟢 Advisory |
| **Commercial Credit Underwriter** (`role_credit_underwriter`) | 1 | 1 | 3 | 0 | **5** | 🟡 Operational Authority |
| **Enterprise Customer** (`role_customer`) | 0 | 0 | 4 | 4 | **8** | 🟢 Advisory |
| **Finance Controller** (`role_finance_controller`) | 0 | 8 | 5 | 2 | **15** | 🚨 Key-Person Risk (Concentrated Approver) |
| **General Ledger Accountant** (`role_general_ledger_accountant`) | 2 | 0 | 2 | 2 | **6** | 🟡 Operational Authority |
| **Hiring Manager** (`role_hiring_manager`) | 2 | 4 | 1 | 0 | **7** | 🔴 Strategic Approver |
| **HR Business Partner** (`role_hr_business_partner`) | 1 | 1 | 4 | 0 | **6** | 🟡 Operational Authority |
| **Internal Auditor** (`role_internal_auditor`) | 0 | 0 | 2 | 6 | **8** | 🟢 Advisory |
| **KYC & AML Compliance Analyst** (`role_kyc_aml_analyst`) | 3 | 0 | 1 | 1 | **5** | 🔵 Primary Driver |
| **Loan Closing & Servicing Specialist** (`role_loan_servicing_specialist`) | 5 | 0 | 0 | 0 | **5** | 🔵 Primary Driver |
| **Payroll Specialist** (`role_payroll_specialist`) | 1 | 1 | 0 | 3 | **5** | 🟡 Operational Authority |
| **Procurement Specialist** (`role_procurement_specialist`) | 5 | 0 | 1 | 0 | **6** | 🔵 Primary Driver |
| **Commercial Relationship Manager** (`role_relationship_manager`) | 2 | 0 | 4 | 3 | **9** | 🟡 Operational Authority |
| **Sales Operations Specialist** (`role_sales_ops_specialist`) | 0 | 0 | 0 | 0 | **0** | 🟢 Advisory |
| **Supplier / Vendor** (`role_supplier`) | 0 | 0 | 0 | 8 | **8** | 🟢 Advisory |
| **Talent Acquisition Specialist** (`role_talent_acquisition_specialist`) | 2 | 0 | 0 | 1 | **3** | 🟡 Operational Authority |
| **Treasury & Settlement Operations Officer** (`role_treasury_operations_officer`) | 0 | 2 | 1 | 2 | **5** | 🟡 Operational Authority |

---

## 3. Decision Governance & Single-Approver Rule Analysis

✅ **Single Approver Rule Upheld!**
Every decision milestone has exactly one designated Approver (A), preventing consensus deadlock.
