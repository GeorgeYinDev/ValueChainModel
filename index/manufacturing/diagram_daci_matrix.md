# Enterprise DACI Decision Governance Matrix [ALL]

> **DACI Legend**: **D** = Driver (Orchestrates/Leads) | **A** = Approver (Sole Sign-off/Veto) | **C** = Contributor (Advises/Consulted) | **I** = Informed (Notified)

## 1. Value Chain Process DACI Grid

| Step ID | Process Step Name | Accounts Payable Clerk | Billing Specialist | Category Manager | Compensation Analyst | Consolidation Specialist | Credit Manager | Customer | Finance Controller | General Ledger Accountant | Hiring Manager | Hr Business Partner | Internal Auditor | Payroll Specialist | Procurement Specialist | Sales Ops Specialist | Supplier | Talent Acquisition Specialist | Demand Planner | Inventory Manager | Manufacturing Supervisor | Production Scheduler | Quality Assurance Engineer | Warehouse Supervisor |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `h2r_001_job_requisition_posting` | **Job Requisition Definition & Posting** | - | - | - | C | - | - | - | - | - | **D**, **A** | C | - | - | - | - | - | I | - | - | - | - | - | - |
| `h2r_002_candidate_screening_interview` | **Candidate Screening & Interview Execution** | - | - | - | - | - | - | - | - | - | **A** | C | - | - | - | - | - | **D** | - | - | - | - | - | - |
| `h2r_003_offer_letter_onboarding` | **Offer Letter Generation & Employee Onboarding** | - | - | - | C | - | - | - | - | - | **A** | - | - | I | - | - | - | **D** | - | - | - | - | - | - |
| `h2r_004_payroll_benefits_enrollment` | **Payroll & Benefits Enrollment Processing** | - | - | - | - | - | - | - | I | - | - | C | - | **D**, **A** | - | - | - | - | - | - | - | - | - | - |
| `h2r_005_performance_compensation_review` | **Performance & Compensation Review** | - | - | - | C | - | - | - | - | - | **D**, **A** | C | - | I | - | - | - | - | - | - | - | - | - | - |
| `h2r_006_separation_offboarding_settlement` | **Separation, Offboarding & Final Settlement** | - | - | - | - | - | - | - | - | - | C | **D**, **A** | - | I | - | - | - | - | - | - | - | - | - | - |
| `o2c_001_customer_quote_order_entry` | **Quote Generation & Order Capture** | - | - | - | - | - | I | C | - | - | - | - | - | - | - | **D**, **A** | - | - | - | - | - | - | - | - |
| `o2c_002_credit_check_approval` | **Customer Credit Assessment & Exposure Check** | - | - | - | - | - | **D** | I | **A** | - | - | - | - | - | - | C | - | - | - | - | - | - | - | - |
| `o2c_003_inventory_allocation_fulfillment` | **Inventory Allocation & Warehouse Fulfillment** | - | - | - | - | - | - | I | - | - | - | - | - | - | - | C | - | - | - | - | - | - | - | **D**, **A** |
| `o2c_004_billing_invoice_generation` | **Customer Billing & Electronic Invoicing** | - | **D** | - | - | - | - | I | **A** | - | - | - | - | - | - | C | - | - | - | - | - | - | - | - |
| `o2c_005_cash_collection_reconciliation` | **Cash Collection & Accounts Receivable Reconciliation** | - | **D** | - | - | - | - | C | **A** | - | - | - | - | - | - | I | - | - | - | - | - | - | - | - |
| `p2m_001_demand_sensing_forecasting` | **Statistical Demand Sensing & Forecasting** | - | - | - | - | - | - | - | - | - | - | - | - | - | - | C | - | - | **D**, **A** | - | - | I | - | - |
| `p2m_002_mrp_production_planning` | **Material Requirements Planning (MRP)** | - | - | - | - | - | - | - | - | - | - | - | - | - | I | - | - | - | - | C | - | **D**, **A** | - | - |
| `p2m_003_production_order_release` | **Production Order Sequencing & Release** | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | C | **A** | **D** | - | - |
| `p2m_004_manufacturing_execution` | **Manufacturing Execution & Yield Tracking** | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | **D**, **A** | I | C | - |
| `p2m_005_quality_inspection_release` | **Quality Inspection & Batch Release** | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | I | C | - | **D**, **A** | - |
| `p2m_006_finished_goods_putaway` | **Finished Goods Put-Away & ATP Update** | - | - | - | - | - | - | - | - | - | - | - | - | - | - | I | - | - | - | **D**, **A** | - | - | - | - |
| `r2r_001_journal_entry_recording` | **General Ledger Journal Recording & Subledger Ingestion** | C | C | - | - | - | - | - | **A** | **D** | - | - | I | - | - | - | - | - | - | - | - | - | - | - |
| `r2r_002_intercompany_reconciliation` | **Intercompany Transaction Matching & Elimination** | - | - | - | - | **D** | - | - | **A** | C | - | - | I | - | - | - | - | - | - | - | - | - | - | - |
| `r2r_003_balance_sheet_substantiation` | **Balance Sheet Account Substantiation & Reconciliation** | - | - | - | - | C | - | - | **A** | **D** | - | - | I | - | - | - | - | - | - | - | - | - | - | - |
| `r2r_004_financial_close_consolidation` | **Financial Close Orchestration & Group Consolidation** | - | - | - | - | **D** | - | - | **A** | C | - | - | I | - | - | - | - | - | - | - | - | - | - | - |
| `r2r_005_statutory_financial_reporting` | **Statutory, Tax & Management Financial Reporting** | - | - | - | - | **D** | - | - | **A** | I | - | - | C | - | - | - | - | - | - | - | - | - | - | - |
| `s2p_001_spend_analysis_need_id` | **Spend Analysis & Need Identification** | - | - | **A** | - | - | - | - | C | - | - | - | - | - | **D** | - | I | - | - | - | - | - | - | - |
| `s2p_002_supplier_discovery_qualification` | **Supplier Discovery & Qualification** | - | - | **A** | - | - | - | - | C | - | - | - | - | - | **D** | - | I | - | - | - | - | - | - | - |
| `s2p_003_sourcing_rfx_auction` | **Strategic Sourcing & RFx Execution** | - | - | **A** | - | - | - | - | C | - | - | - | - | - | **D** | - | I | - | - | - | - | - | - | - |
| `s2p_004_contracting_sla_negotiation` | **Contracting & SLA Negotiation** | - | - | **D**, **A** | - | - | - | - | C | - | - | - | - | - | - | - | I | - | - | - | - | - | - | - |
| `s2p_005_purchase_requisition_po` | **Purchase Requisition & PO Issuance** | - | - | **A** | - | - | - | - | C | - | - | - | - | - | **D** | - | I | - | - | - | - | - | - | - |
| `s2p_006_goods_services_receipt` | **Goods & Services Receipt Verification** | C | - | **A** | - | - | - | - | - | - | - | - | - | - | **D** | - | I | - | - | - | - | - | - | - |
| `s2p_007_invoice_verification_matching` | **Invoice 3-Way Matching & Exception Handling** | **D** | - | - | - | - | - | - | **A** | - | - | - | - | - | C | - | I | - | - | - | - | - | - | - |
| `s2p_008_payment_settlement_disbursement` | **Payment Settlement & Disbursement** | **D** | - | C | - | - | - | - | **A** | - | - | - | - | - | - | - | I | - | - | - | - | - | - | - |

---

## 2. Decision Authority & Driver Distribution

| Enterprise Role | Driver (D) | Approver (A) | Contributor (C) | Informed (I) | Total Decision Touchpoints | Governance Weight |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Accounts Payable Clerk** (`role_accounts_payable_clerk`) | 2 | 0 | 2 | 0 | **4** | 🟡 Operational Authority |
| **Billing Specialist** (`role_billing_specialist`) | 2 | 0 | 1 | 0 | **3** | 🟡 Operational Authority |
| **Category Manager** (`role_category_manager`) | 1 | 6 | 1 | 0 | **8** | 🚨 Key-Person Risk (Concentrated Approver) |
| **Compensation Analyst** (`role_compensation_analyst`) | 0 | 0 | 3 | 0 | **3** | 🟢 Advisory |
| **Consolidation Specialist** (`role_consolidation_specialist`) | 3 | 0 | 1 | 0 | **4** | 🔵 Primary Driver |
| **Credit Manager** (`role_credit_manager`) | 1 | 0 | 0 | 1 | **2** | 🟡 Operational Authority |
| **Customer** (`role_customer`) | 0 | 0 | 2 | 3 | **5** | 🟢 Advisory |
| **Finance Controller** (`role_finance_controller`) | 0 | 10 | 5 | 1 | **16** | 🚨 Key-Person Risk (Concentrated Approver) |
| **General Ledger Accountant** (`role_general_ledger_accountant`) | 2 | 0 | 2 | 1 | **5** | 🟡 Operational Authority |
| **Hiring Manager** (`role_hiring_manager`) | 2 | 4 | 1 | 0 | **7** | 🔴 Strategic Approver |
| **Hr Business Partner** (`role_hr_business_partner`) | 1 | 1 | 4 | 0 | **6** | 🟡 Operational Authority |
| **Internal Auditor** (`role_internal_auditor`) | 0 | 0 | 1 | 4 | **5** | 🟢 Advisory |
| **Payroll Specialist** (`role_payroll_specialist`) | 1 | 1 | 0 | 3 | **5** | 🟡 Operational Authority |
| **Procurement Specialist** (`role_procurement_specialist`) | 5 | 0 | 1 | 1 | **7** | 🔵 Primary Driver |
| **Sales Ops Specialist** (`role_sales_ops_specialist`) | 1 | 1 | 4 | 2 | **8** | 🟡 Operational Authority |
| **Supplier** (`role_supplier`) | 0 | 0 | 0 | 8 | **8** | 🟢 Advisory |
| **Talent Acquisition Specialist** (`role_talent_acquisition_specialist`) | 2 | 0 | 0 | 1 | **3** | 🟡 Operational Authority |
| **Demand Planner** (`role_demand_planner`) | 1 | 1 | 0 | 0 | **2** | 🟡 Operational Authority |
| **Inventory Manager** (`role_inventory_manager`) | 1 | 1 | 2 | 1 | **5** | 🟡 Operational Authority |
| **Manufacturing Supervisor** (`role_manufacturing_supervisor`) | 1 | 2 | 1 | 0 | **4** | 🟡 Operational Authority |
| **Production Scheduler** (`role_production_scheduler`) | 2 | 1 | 0 | 2 | **5** | 🟡 Operational Authority |
| **Quality Assurance Engineer** (`role_quality_assurance_engineer`) | 1 | 1 | 1 | 0 | **3** | 🟡 Operational Authority |
| **Warehouse Supervisor** (`role_warehouse_supervisor`) | 1 | 1 | 0 | 0 | **2** | 🟡 Operational Authority |

---

## 3. Decision Governance & Single-Approver Rule Analysis

✅ **Single Approver Rule Upheld!**
Every decision milestone has exactly one designated Approver (A), preventing consensus deadlock.
