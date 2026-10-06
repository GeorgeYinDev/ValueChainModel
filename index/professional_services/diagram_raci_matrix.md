# Enterprise RACI Governance Matrix [ALL]

> **RACI Legend**: **R** = Responsible (Executes) | **A** = Accountable (Approves) | **C** = Consulted (Inputs) | **I** = Informed (Notified)

## 1. Value Chain Process RACI Grid

| Step ID | Process Step Name | Accounts Payable Clerk | Billing Specialist | Category Manager | Compensation Analyst | Consolidation Specialist | Credit Manager | Customer | Finance Controller | General Ledger Accountant | Hiring Manager | Hr Business Partner | Internal Auditor | Payroll Specialist | Procurement Specialist | Sales Ops Specialist | Supplier | Talent Acquisition Specialist | Account Executive | Consultant | Engagement Manager | Practice Director | Solution Architect |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `e2c_001_project_kickoff` | **Project Kickoff & Resource Allocation** | - | - | - | - | - | - | I | - | - | - | - | - | - | - | - | - | - | - | C | **R** | **A** | - |
| `e2c_002_resource_scheduling` | **Resource Scheduling & Allocation** | - | - | - | - | - | - | - | - | - | - | C | - | - | - | - | - | - | - | I | **R** | **A** | - |
| `e2c_003_project_execution_delivery` | **Project Execution & Milestone Delivery** | - | - | - | - | - | - | I | - | - | - | - | - | - | - | - | - | - | - | **R** | **A** | - | C |
| `e2c_004_time_expense_entry` | **Time & Expense Logging** | - | C | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | **R** | **A** | I | - |
| `e2c_005_client_acceptance` | **Client Review & Deliverable Acceptance** | - | I | - | - | - | - | C | - | - | - | - | - | - | - | - | - | - | - | - | **R**, **A** | - | - |
| `e2c_006_project_billing_invoicing` | **Project Billing & Invoicing** | - | **R** | - | - | - | - | I | **A** | - | - | - | - | - | - | - | - | - | - | - | C | - | - |
| `e2c_007_project_closure_lessons` | **Project Closure & Lessons Learned** | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | I | C | **R** | **A** | - |
| `h2r_001_job_requisition_posting` | **Job Requisition Definition & Posting** | - | - | - | C | - | - | - | - | - | **R**, **A** | C | - | - | - | - | - | I | - | - | - | - | - |
| `h2r_002_candidate_screening_interview` | **Candidate Screening & Interview Execution** | - | - | - | - | - | - | - | - | - | **A** | C | - | - | - | - | - | **R** | - | - | - | - | - |
| `h2r_003_offer_letter_onboarding` | **Offer Letter Generation & Employee Onboarding** | - | - | - | C | - | - | - | - | - | **A** | - | - | I | - | - | - | **R** | - | - | - | - | - |
| `h2r_004_payroll_benefits_enrollment` | **Payroll & Benefits Enrollment Processing** | - | - | - | - | - | - | - | I | - | - | C | - | **R**, **A** | - | - | - | - | - | - | - | - | - |
| `h2r_005_performance_compensation_review` | **Performance & Compensation Review** | - | - | - | C | - | - | - | - | - | **R**, **A** | C | - | I | - | - | - | - | - | - | - | - | - |
| `h2r_006_separation_offboarding_settlement` | **Separation, Offboarding & Final Settlement** | - | - | - | - | - | - | - | - | - | C | **R**, **A** | - | I | - | - | - | - | - | - | - | - | - |
| `l2c_001_lead_qualification` | **Lead Qualification & Discovery** | - | - | - | - | - | - | - | - | - | - | - | - | - | - | I | - | - | **R** | - | - | **A** | C |
| `l2c_002_proposal_development` | **Proposal Development & Scoping** | - | - | - | - | - | - | I | - | - | - | - | - | - | - | - | - | - | - | - | C | **A** | **R** |
| `l2c_003_contract_negotiation` | **Contract Negotiation & Legal Review** | - | - | - | - | - | - | - | C | - | - | - | - | - | - | - | - | - | **R** | - | I | **A** | - |
| `l2c_004_deal_closure_handover` | **Deal Closure & Delivery Handover** | - | - | - | - | - | - | - | - | - | - | - | - | - | - | I | - | - | **R** | - | **A** | - | C |
| `r2r_001_journal_entry_recording` | **General Ledger Journal Recording & Subledger Ingestion** | C | C | - | - | - | - | - | **A** | **R** | - | - | I | - | - | - | - | - | - | - | - | - | - |
| `r2r_002_intercompany_reconciliation` | **Intercompany Transaction Matching & Elimination** | - | - | - | - | **R** | - | - | **A** | C | - | - | I | - | - | - | - | - | - | - | - | - | - |
| `r2r_003_balance_sheet_substantiation` | **Balance Sheet Account Substantiation & Reconciliation** | - | - | - | - | C | - | - | **A** | **R** | - | - | I | - | - | - | - | - | - | - | - | - | - |
| `r2r_004_financial_close_consolidation` | **Financial Close Orchestration & Group Consolidation** | - | - | - | - | **R** | - | - | **A** | C | - | - | I | - | - | - | - | - | - | - | - | - | - |
| `r2r_005_statutory_financial_reporting` | **Statutory, Tax & Management Financial Reporting** | - | - | - | - | **R** | - | - | **A** | I | - | - | C | - | - | - | - | - | - | - | - | - | - |
| `s2p_001_spend_analysis_need_id` | **Spend Analysis & Need Identification** | - | - | **A** | - | - | - | - | C | - | - | - | - | - | **R** | - | I | - | - | - | - | - | - |
| `s2p_002_supplier_discovery_qualification` | **Supplier Discovery & Qualification** | - | - | **A** | - | - | - | - | C | - | - | - | - | - | **R** | - | I | - | - | - | - | - | - |
| `s2p_003_sourcing_rfx_auction` | **Strategic Sourcing & RFx Execution** | - | - | **A** | - | - | - | - | C | - | - | - | - | - | **R** | - | I | - | - | - | - | - | - |
| `s2p_004_contracting_sla_negotiation` | **Contracting & SLA Negotiation** | - | - | **R**, **A** | - | - | - | - | C | - | - | - | - | - | - | - | I | - | - | - | - | - | - |
| `s2p_005_purchase_requisition_po` | **Purchase Requisition & PO Issuance** | - | - | **A** | - | - | - | - | C | - | - | - | - | - | **R** | - | I | - | - | - | - | - | - |
| `s2p_006_goods_services_receipt` | **Goods & Services Receipt Verification** | C | - | **A** | - | - | - | - | - | - | - | - | - | - | **R** | - | I | - | - | - | - | - | - |
| `s2p_007_invoice_verification_matching` | **Invoice 3-Way Matching & Exception Handling** | **R** | - | - | - | - | - | - | **A** | - | - | - | - | - | C | - | I | - | - | - | - | - | - |
| `s2p_008_payment_settlement_disbursement` | **Payment Settlement & Disbursement** | **R** | - | C | - | - | - | - | **A** | - | - | - | - | - | - | - | I | - | - | - | - | - | - |

---

## 2. Role Workload & Touchpoint Distribution

| Enterprise Role | Responsible (R) | Accountable (A) | Consulted (C) | Informed (I) | Total Touchpoints | Operational Load |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Accounts Payable Clerk** (`role_accounts_payable_clerk`) | 2 | 0 | 2 | 0 | **4** | 🟡 Moderate |
| **Billing Specialist** (`role_billing_specialist`) | 1 | 0 | 2 | 1 | **4** | 🟡 Moderate |
| **Category Manager** (`role_category_manager`) | 1 | 6 | 1 | 0 | **8** | 🔴 High (Key Dependency) |
| **Compensation Analyst** (`role_compensation_analyst`) | 0 | 0 | 3 | 0 | **3** | 🟢 Low |
| **Consolidation Specialist** (`role_consolidation_specialist`) | 3 | 0 | 1 | 0 | **4** | 🔴 High (Key Dependency) |
| **Credit Manager** (`role_credit_manager`) | 0 | 0 | 0 | 0 | **0** | 🟢 Low |
| **Customer** (`role_customer`) | 0 | 0 | 1 | 4 | **5** | 🟡 Moderate |
| **Finance Controller** (`role_finance_controller`) | 0 | 8 | 6 | 1 | **15** | 🔴 High (Key Dependency) |
| **General Ledger Accountant** (`role_general_ledger_accountant`) | 2 | 0 | 2 | 1 | **5** | 🟡 Moderate |
| **Hiring Manager** (`role_hiring_manager`) | 2 | 4 | 1 | 0 | **7** | 🔴 High (Key Dependency) |
| **Hr Business Partner** (`role_hr_business_partner`) | 1 | 1 | 5 | 0 | **7** | 🔴 High (Key Dependency) |
| **Internal Auditor** (`role_internal_auditor`) | 0 | 0 | 1 | 4 | **5** | 🟡 Moderate |
| **Payroll Specialist** (`role_payroll_specialist`) | 1 | 1 | 0 | 3 | **5** | 🟡 Moderate |
| **Procurement Specialist** (`role_procurement_specialist`) | 5 | 0 | 1 | 0 | **6** | 🔴 High (Key Dependency) |
| **Sales Ops Specialist** (`role_sales_ops_specialist`) | 0 | 0 | 0 | 2 | **2** | 🟢 Low |
| **Supplier** (`role_supplier`) | 0 | 0 | 0 | 8 | **8** | 🔴 High (Key Dependency) |
| **Talent Acquisition Specialist** (`role_talent_acquisition_specialist`) | 2 | 0 | 0 | 1 | **3** | 🟡 Moderate |
| **Account Executive** (`role_account_executive`) | 3 | 0 | 0 | 1 | **4** | 🔴 High (Key Dependency) |
| **Consultant** (`role_consultant`) | 2 | 0 | 2 | 1 | **5** | 🟡 Moderate |
| **Engagement Manager** (`role_engagement_manager`) | 4 | 4 | 2 | 1 | **11** | 🔴 High (Key Dependency) |
| **Practice Director** (`role_practice_director`) | 0 | 6 | 0 | 1 | **7** | 🔴 High (Key Dependency) |
| **Solution Architect** (`role_solution_architect`) | 1 | 0 | 3 | 0 | **4** | 🟡 Moderate |

---

## 3. Segregation of Duties (SoD) & Conflict Analysis

⚠️ **Potential Segregation of Duties (SoD) Overlaps Detected:**

- **Step `e2c_005_client_acceptance` (Client Review & Deliverable Acceptance)**: Role `role_engagement_manager` is listed as both Responsible and Accountable.
- **Step `h2r_001_job_requisition_posting` (Job Requisition Definition & Posting)**: Role `role_hiring_manager` is listed as both Responsible and Accountable.
- **Step `h2r_004_payroll_benefits_enrollment` (Payroll & Benefits Enrollment Processing)**: Role `role_payroll_specialist` is listed as both Responsible and Accountable.
- **Step `h2r_005_performance_compensation_review` (Performance & Compensation Review)**: Role `role_hiring_manager` is listed as both Responsible and Accountable.
- **Step `h2r_006_separation_offboarding_settlement` (Separation, Offboarding & Final Settlement)**: Role `role_hr_business_partner` is listed as both Responsible and Accountable.
- **Step `s2p_004_contracting_sla_negotiation` (Contracting & SLA Negotiation)**: Role `role_category_manager` is listed as both Responsible and Accountable.