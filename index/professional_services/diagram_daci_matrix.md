# Enterprise DACI Decision Governance Matrix [ALL]

> **DACI Legend**: **D** = Driver (Orchestrates/Leads) | **A** = Approver (Sole Sign-off/Veto) | **C** = Contributor (Advises/Consulted) | **I** = Informed (Notified)

## 1. Value Chain Process DACI Grid

| Step ID | Process Step Name | Account Executive | Accounts Payable Clerk | Billing & Accounts Receivable Specialist | Category Manager | Compensation Analyst | Financial Consolidation Specialist | Consultant | Credit & Risk Manager | Enterprise Customer | Engagement Manager | Finance Controller | General Ledger Accountant | Hiring Manager | HR Business Partner | Internal Auditor | Payroll Specialist | Practice Director | Procurement Specialist | Sales Operations Specialist | Solution Architect | Supplier / Vendor | Talent Acquisition Specialist |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `e2c_001_project_kickoff` | **Project Kickoff & Resource Allocation** | - | - | - | - | - | - | C | - | I | **D** | - | - | - | - | - | - | **A** | - | - | - | - | - |
| `e2c_002_resource_scheduling` | **Resource Scheduling & Allocation** | - | - | - | - | - | - | I | - | - | **D** | - | - | - | C | - | - | **A** | - | - | - | - | - |
| `e2c_003_project_execution_delivery` | **Project Execution & Milestone Delivery** | - | - | - | - | - | - | **D** | - | I | **A** | - | - | - | - | - | - | - | - | - | C | - | - |
| `e2c_004_time_expense_entry` | **Time & Expense Logging** | - | - | C | - | - | - | **D** | - | - | **A** | - | - | - | - | - | - | I | - | - | - | - | - |
| `e2c_005_client_acceptance` | **Client Review & Deliverable Acceptance** | - | - | I | - | - | - | - | - | C | **D**, **A** | - | - | - | - | - | - | - | - | - | - | - | - |
| `e2c_006_project_billing_invoicing` | **Project Billing & Invoicing** | - | - | **D** | - | - | - | - | - | I | C | **A** | - | - | - | - | - | - | - | - | - | - | - |
| `e2c_007_project_closure_lessons` | **Project Closure & Lessons Learned** | I | - | - | - | - | - | C | - | - | **D** | - | - | - | - | - | - | **A** | - | - | - | - | - |
| `h2r_001_job_requisition_posting` | **Job Requisition Definition & Posting** | - | - | - | - | C | - | - | - | - | - | - | - | **D**, **A** | C | - | - | - | - | - | - | - | I |
| `h2r_002_candidate_screening_interview` | **Candidate Screening & Interview Execution** | - | - | - | - | - | - | - | - | - | - | - | - | **A** | C | - | - | - | - | - | - | - | **D** |
| `h2r_003_offer_letter_onboarding` | **Offer Letter Generation & Employee Onboarding** | - | - | - | - | C | - | - | - | - | - | - | - | **A** | - | - | I | - | - | - | - | - | **D** |
| `h2r_004_payroll_benefits_enrollment` | **Payroll & Benefits Enrollment Processing** | - | - | - | - | - | - | - | - | - | - | I | - | - | C | - | **D**, **A** | - | - | - | - | - | - |
| `h2r_005_performance_compensation_review` | **Performance & Compensation Review** | - | - | - | - | C | - | - | - | - | - | - | - | **D**, **A** | C | - | I | - | - | - | - | - | - |
| `h2r_006_separation_offboarding_settlement` | **Separation, Offboarding & Final Settlement** | - | - | - | - | - | - | - | - | - | - | - | - | C | **D**, **A** | - | I | - | - | - | - | - | - |
| `l2c_001_lead_qualification` | **Lead Qualification & Discovery** | **D** | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | **A** | - | I | C | - | - |
| `l2c_002_proposal_development` | **Proposal Development & Scoping** | - | - | - | - | - | - | - | - | I | C | - | - | - | - | - | - | **A** | - | - | **D** | - | - |
| `l2c_003_contract_negotiation` | **Contract Negotiation & Legal Review** | **D** | - | - | - | - | - | - | - | - | I | C | - | - | - | - | - | **A** | - | - | - | - | - |
| `l2c_004_deal_closure_handover` | **Deal Closure & Delivery Handover** | **D** | - | - | - | - | - | - | - | - | **A** | - | - | - | - | - | - | - | - | I | C | - | - |
| `r2r_001_journal_entry_recording` | **General Ledger Journal Recording & Subledger Ingestion** | - | C | C | - | - | - | - | - | - | - | **A** | **D** | - | - | I | - | - | - | - | - | - | - |
| `r2r_002_intercompany_reconciliation` | **Intercompany Transaction Matching & Elimination** | - | - | - | - | - | **D** | - | - | - | - | **A** | C | - | - | I | - | - | - | - | - | - | - |
| `r2r_003_balance_sheet_substantiation` | **Balance Sheet Account Substantiation & Reconciliation** | - | - | - | - | - | C | - | - | - | - | **A** | **D** | - | - | I | - | - | - | - | - | - | - |
| `r2r_004_financial_close_consolidation` | **Financial Close Orchestration & Group Consolidation** | - | - | - | - | - | **D** | - | - | - | - | **A** | C | - | - | I | - | - | - | - | - | - | - |
| `r2r_005_statutory_financial_reporting` | **Statutory, Tax & Management Financial Reporting** | - | - | - | - | - | **D** | - | - | - | - | **A** | I | - | - | C | - | - | - | - | - | - | - |
| `s2p_001_spend_analysis_need_id` | **Spend Analysis & Need Identification** | - | - | - | **A** | - | - | - | - | - | - | C | - | - | - | - | - | - | **D** | - | - | I | - |
| `s2p_002_supplier_discovery_qualification` | **Supplier Discovery & Qualification** | - | - | - | **A** | - | - | - | - | - | - | C | - | - | - | - | - | - | **D** | - | - | I | - |
| `s2p_003_sourcing_rfx_auction` | **Strategic Sourcing & RFx Execution** | - | - | - | **A** | - | - | - | - | - | - | C | - | - | - | - | - | - | **D** | - | - | I | - |
| `s2p_004_contracting_sla_negotiation` | **Contracting & SLA Negotiation** | - | - | - | **D**, **A** | - | - | - | - | - | - | C | - | - | - | - | - | - | - | - | - | I | - |
| `s2p_005_purchase_requisition_po` | **Purchase Requisition & PO Issuance** | - | - | - | **A** | - | - | - | - | - | - | C | - | - | - | - | - | - | **D** | - | - | I | - |
| `s2p_006_goods_services_receipt` | **Goods & Services Receipt Verification** | - | C | - | **A** | - | - | - | - | - | - | - | - | - | - | - | - | - | **D** | - | - | I | - |
| `s2p_007_invoice_verification_matching` | **Invoice 3-Way Matching & Exception Handling** | - | **D** | - | - | - | - | - | - | - | - | **A** | - | - | - | - | - | - | C | - | - | I | - |
| `s2p_008_payment_settlement_disbursement` | **Payment Settlement & Disbursement** | - | **D** | - | C | - | - | - | - | - | - | **A** | - | - | - | - | - | - | - | - | - | I | - |

---

## 2. Decision Authority & Driver Distribution

| Enterprise Role | Driver (D) | Approver (A) | Contributor (C) | Informed (I) | Total Decision Touchpoints | Governance Weight |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Account Executive** (`role_account_executive`) | 3 | 0 | 0 | 1 | **4** | 🔵 Primary Driver |
| **Accounts Payable Clerk** (`role_accounts_payable_clerk`) | 2 | 0 | 2 | 0 | **4** | 🟡 Operational Authority |
| **Billing & Accounts Receivable Specialist** (`role_billing_specialist`) | 1 | 0 | 2 | 1 | **4** | 🟡 Operational Authority |
| **Category Manager** (`role_category_manager`) | 1 | 6 | 1 | 0 | **8** | 🚨 Key-Person Risk (Concentrated Approver) |
| **Compensation Analyst** (`role_compensation_analyst`) | 0 | 0 | 3 | 0 | **3** | 🟢 Advisory |
| **Financial Consolidation Specialist** (`role_consolidation_specialist`) | 3 | 0 | 1 | 0 | **4** | 🔵 Primary Driver |
| **Consultant** (`role_consultant`) | 2 | 0 | 2 | 1 | **5** | 🟡 Operational Authority |
| **Credit & Risk Manager** (`role_credit_manager`) | 0 | 0 | 0 | 0 | **0** | 🟢 Advisory |
| **Enterprise Customer** (`role_customer`) | 0 | 0 | 1 | 4 | **5** | 🟢 Advisory |
| **Engagement Manager** (`role_engagement_manager`) | 4 | 4 | 2 | 1 | **11** | 🔴 Strategic Approver |
| **Finance Controller** (`role_finance_controller`) | 0 | 8 | 6 | 1 | **15** | 🚨 Key-Person Risk (Concentrated Approver) |
| **General Ledger Accountant** (`role_general_ledger_accountant`) | 2 | 0 | 2 | 1 | **5** | 🟡 Operational Authority |
| **Hiring Manager** (`role_hiring_manager`) | 2 | 4 | 1 | 0 | **7** | 🔴 Strategic Approver |
| **HR Business Partner** (`role_hr_business_partner`) | 1 | 1 | 5 | 0 | **7** | 🟡 Operational Authority |
| **Internal Auditor** (`role_internal_auditor`) | 0 | 0 | 1 | 4 | **5** | 🟢 Advisory |
| **Payroll Specialist** (`role_payroll_specialist`) | 1 | 1 | 0 | 3 | **5** | 🟡 Operational Authority |
| **Practice Director** (`role_practice_director`) | 0 | 6 | 0 | 1 | **7** | 🚨 Key-Person Risk (Concentrated Approver) |
| **Procurement Specialist** (`role_procurement_specialist`) | 5 | 0 | 1 | 0 | **6** | 🔵 Primary Driver |
| **Sales Operations Specialist** (`role_sales_ops_specialist`) | 0 | 0 | 0 | 2 | **2** | 🟢 Advisory |
| **Solution Architect** (`role_solution_architect`) | 1 | 0 | 3 | 0 | **4** | 🟡 Operational Authority |
| **Supplier / Vendor** (`role_supplier`) | 0 | 0 | 0 | 8 | **8** | 🟢 Advisory |
| **Talent Acquisition Specialist** (`role_talent_acquisition_specialist`) | 2 | 0 | 0 | 1 | **3** | 🟡 Operational Authority |

---

## 3. Decision Governance & Single-Approver Rule Analysis

✅ **Single Approver Rule Upheld!**
Every decision milestone has exactly one designated Approver (A), preventing consensus deadlock.
