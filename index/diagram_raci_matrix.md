# Enterprise RACI Governance Matrix [ALL]

> **RACI Legend**: **R** = Responsible (Executes) | **A** = Accountable (Approves) | **C** = Consulted (Inputs) | **I** = Informed (Notified)

## 1. Value Chain Process RACI Grid

| Step ID | Process Step Name | Manufacturing Supervisor | HR Business Partner (HRBP) | Warehouse & Fulfillment Supervisor | Talent Acquisition Specialist | Sales Operations Specialist | Inventory Manager | Demand Planner | Compensation Analyst | Billing & Accounts Receivable Specialist | Production Scheduler | Finance Controller | Supplier / Vendor | Category Manager | General Ledger Accountant | Hiring Manager | Credit & Risk Manager | Procurement Specialist | Financial Consolidation Specialist | Enterprise Customer | Accounts Payable Clerk | Payroll Specialist | Internal Auditor | Quality Assurance Engineer |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `h2r_001_job_requisition_posting` | **Job Requisition Definition & Posting** | - | C | - | I | - | - | - | C | - | - | - | - | - | - | **R**, **A** | - | - | - | - | - | - | - | - |
| `h2r_002_candidate_screening_interview` | **Candidate Screening & Interview Execution** | - | C | - | **R** | - | - | - | - | - | - | - | - | - | - | **A** | - | - | - | - | - | - | - | - |
| `h2r_003_offer_letter_onboarding` | **Offer Letter Generation & Employee Onboarding** | - | - | - | **R** | - | - | - | C | - | - | - | - | - | - | **A** | - | - | - | - | - | I | - | - |
| `h2r_004_payroll_benefits_enrollment` | **Payroll & Benefits Enrollment Processing** | - | C | - | - | - | - | - | - | - | - | I | - | - | - | - | - | - | - | - | - | **R**, **A** | - | - |
| `h2r_005_performance_compensation_review` | **Performance & Compensation Review** | - | C | - | - | - | - | - | C | - | - | - | - | - | - | **R**, **A** | - | - | - | - | - | I | - | - |
| `h2r_006_separation_offboarding_settlement` | **Separation, Offboarding & Final Settlement** | - | **R**, **A** | - | - | - | - | - | - | - | - | - | - | - | - | C | - | - | - | - | - | I | - | - |
| `o2c_001_customer_quote_order_entry` | **Quote Generation & Order Capture** | - | - | - | - | **R**, **A** | - | - | - | - | - | - | - | - | - | - | I | - | - | C | - | - | - | - |
| `o2c_002_credit_check_approval` | **Customer Credit Assessment & Exposure Check** | - | - | - | - | C | - | - | - | - | - | **A** | - | - | - | - | **R** | - | - | I | - | - | - | - |
| `o2c_003_inventory_allocation_fulfillment` | **Inventory Allocation & Warehouse Fulfillment** | - | - | **R**, **A** | - | C | - | - | - | - | - | - | - | - | - | - | - | - | - | I | - | - | - | - |
| `o2c_004_billing_invoice_generation` | **Customer Billing & Electronic Invoicing** | - | - | - | - | C | - | - | - | **R** | - | **A** | - | - | - | - | - | - | - | I | - | - | - | - |
| `o2c_005_cash_collection_reconciliation` | **Cash Collection & Accounts Receivable Reconciliation** | - | - | - | - | I | - | - | - | **R** | - | **A** | - | - | - | - | - | - | - | C | - | - | - | - |
| `p2m_001_demand_sensing_forecasting` | **Statistical Demand Sensing & Forecasting** | - | - | - | - | C | - | **R**, **A** | - | - | I | - | - | - | - | - | - | - | - | - | - | - | - | - |
| `p2m_002_mrp_production_planning` | **Material Requirements Planning (MRP)** | - | - | - | - | - | C | - | - | - | **R**, **A** | - | - | - | - | - | - | I | - | - | - | - | - | - |
| `p2m_003_production_order_release` | **Production Order Sequencing & Release** | **A** | - | - | - | - | C | - | - | - | **R** | - | - | - | - | - | - | - | - | - | - | - | - | - |
| `p2m_004_manufacturing_execution` | **Manufacturing Execution & Yield Tracking** | **R**, **A** | - | - | - | - | - | - | - | - | I | - | - | - | - | - | - | - | - | - | - | - | - | C |
| `p2m_005_quality_inspection_release` | **Quality Inspection & Batch Release** | C | - | - | - | - | I | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | **R**, **A** |
| `p2m_006_finished_goods_putaway` | **Finished Goods Put-Away & ATP Update** | - | - | - | - | I | **R**, **A** | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| `r2r_001_journal_entry_recording` | **General Ledger Journal Recording & Subledger Ingestion** | - | - | - | - | - | - | - | - | C | - | **A** | - | - | **R** | - | - | - | - | - | C | - | I | - |
| `r2r_002_intercompany_reconciliation` | **Intercompany Transaction Matching & Elimination** | - | - | - | - | - | - | - | - | - | - | **A** | - | - | C | - | - | - | **R** | - | - | - | I | - |
| `r2r_003_balance_sheet_substantiation` | **Balance Sheet Account Substantiation & Reconciliation** | - | - | - | - | - | - | - | - | - | - | **A** | - | - | **R** | - | - | - | C | - | - | - | I | - |
| `r2r_004_financial_close_consolidation` | **Financial Close Orchestration & Group Consolidation** | - | - | - | - | - | - | - | - | - | - | **A** | - | - | C | - | - | - | **R** | - | - | - | I | - |
| `r2r_005_statutory_financial_reporting` | **Statutory, Tax & Management Financial Reporting** | - | - | - | - | - | - | - | - | - | - | **A** | - | - | I | - | - | - | **R** | - | - | - | C | - |
| `s2p_001_spend_analysis_need_id` | **Spend Analysis & Need Identification** | - | - | - | - | - | - | - | - | - | - | C | I | **A** | - | - | - | **R** | - | - | - | - | - | - |
| `s2p_002_supplier_discovery_qualification` | **Supplier Discovery & Qualification** | - | - | - | - | - | - | - | - | - | - | C | I | **A** | - | - | - | **R** | - | - | - | - | - | - |
| `s2p_003_sourcing_rfx_auction` | **Strategic Sourcing & RFx Execution** | - | - | - | - | - | - | - | - | - | - | C | I | **A** | - | - | - | **R** | - | - | - | - | - | - |
| `s2p_004_contracting_sla_negotiation` | **Contracting & SLA Negotiation** | - | - | - | - | - | - | - | - | - | - | C | I | **R**, **A** | - | - | - | - | - | - | - | - | - | - |
| `s2p_005_purchase_requisition_po` | **Purchase Requisition & PO Issuance** | - | - | - | - | - | - | - | - | - | - | C | I | **A** | - | - | - | **R** | - | - | - | - | - | - |
| `s2p_006_goods_services_receipt` | **Goods & Services Receipt Verification** | - | - | - | - | - | - | - | - | - | - | - | I | **A** | - | - | - | **R** | - | - | C | - | - | - |
| `s2p_007_invoice_verification_matching` | **Invoice 3-Way Matching & Exception Handling** | - | - | - | - | - | - | - | - | - | - | **A** | I | - | - | - | - | C | - | - | **R** | - | - | - |
| `s2p_008_payment_settlement_disbursement` | **Payment Settlement & Disbursement** | - | - | - | - | - | - | - | - | - | - | **A** | I | C | - | - | - | - | - | - | **R** | - | - | - |

---

## 2. Role Workload & Touchpoint Distribution

| Enterprise Role | Responsible (R) | Accountable (A) | Consulted (C) | Informed (I) | Total Touchpoints | Operational Load |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Manufacturing Supervisor** (`role_manufacturing_supervisor`) | 1 | 2 | 1 | 0 | **4** | 🟡 Moderate |
| **HR Business Partner (HRBP)** (`role_hr_business_partner`) | 1 | 1 | 4 | 0 | **6** | 🔴 High (Key Dependency) |
| **Warehouse & Fulfillment Supervisor** (`role_warehouse_supervisor`) | 1 | 1 | 0 | 0 | **2** | 🟢 Low |
| **Talent Acquisition Specialist** (`role_talent_acquisition_specialist`) | 2 | 0 | 0 | 1 | **3** | 🟡 Moderate |
| **Sales Operations Specialist** (`role_sales_ops_specialist`) | 1 | 1 | 4 | 2 | **8** | 🔴 High (Key Dependency) |
| **Inventory Manager** (`role_inventory_manager`) | 1 | 1 | 2 | 1 | **5** | 🟡 Moderate |
| **Demand Planner** (`role_demand_planner`) | 1 | 1 | 0 | 0 | **2** | 🟢 Low |
| **Compensation Analyst** (`role_compensation_analyst`) | 0 | 0 | 3 | 0 | **3** | 🟢 Low |
| **Billing & Accounts Receivable Specialist** (`role_billing_specialist`) | 2 | 0 | 1 | 0 | **3** | 🟡 Moderate |
| **Production Scheduler** (`role_production_scheduler`) | 2 | 1 | 0 | 2 | **5** | 🟡 Moderate |
| **Finance Controller** (`role_finance_controller`) | 0 | 10 | 5 | 1 | **16** | 🔴 High (Key Dependency) |
| **Supplier / Vendor** (`role_supplier`) | 0 | 0 | 0 | 8 | **8** | 🔴 High (Key Dependency) |
| **Category Manager** (`role_category_manager`) | 1 | 6 | 1 | 0 | **8** | 🔴 High (Key Dependency) |
| **General Ledger Accountant** (`role_general_ledger_accountant`) | 2 | 0 | 2 | 1 | **5** | 🟡 Moderate |
| **Hiring Manager** (`role_hiring_manager`) | 2 | 4 | 1 | 0 | **7** | 🔴 High (Key Dependency) |
| **Credit & Risk Manager** (`role_credit_manager`) | 1 | 0 | 0 | 1 | **2** | 🟢 Low |
| **Procurement Specialist** (`role_procurement_specialist`) | 5 | 0 | 1 | 1 | **7** | 🔴 High (Key Dependency) |
| **Financial Consolidation Specialist** (`role_consolidation_specialist`) | 3 | 0 | 1 | 0 | **4** | 🔴 High (Key Dependency) |
| **Enterprise Customer** (`role_customer`) | 0 | 0 | 2 | 3 | **5** | 🟡 Moderate |
| **Accounts Payable Clerk** (`role_accounts_payable_clerk`) | 2 | 0 | 2 | 0 | **4** | 🟡 Moderate |
| **Payroll Specialist** (`role_payroll_specialist`) | 1 | 1 | 0 | 3 | **5** | 🟡 Moderate |
| **Internal Auditor** (`role_internal_auditor`) | 0 | 0 | 1 | 4 | **5** | 🟡 Moderate |
| **Quality Assurance Engineer** (`role_quality_assurance_engineer`) | 1 | 1 | 1 | 0 | **3** | 🟢 Low |

---

## 3. Segregation of Duties (SoD) & Conflict Analysis

⚠️ **Potential Segregation of Duties (SoD) Overlaps Detected:**

- **Step `h2r_001_job_requisition_posting` (Job Requisition Definition & Posting)**: Role `role_hiring_manager` is listed as both Responsible and Accountable.
- **Step `h2r_004_payroll_benefits_enrollment` (Payroll & Benefits Enrollment Processing)**: Role `role_payroll_specialist` is listed as both Responsible and Accountable.
- **Step `h2r_005_performance_compensation_review` (Performance & Compensation Review)**: Role `role_hiring_manager` is listed as both Responsible and Accountable.
- **Step `h2r_006_separation_offboarding_settlement` (Separation, Offboarding & Final Settlement)**: Role `role_hr_business_partner` is listed as both Responsible and Accountable.
- **Step `o2c_001_customer_quote_order_entry` (Quote Generation & Order Capture)**: Role `role_sales_ops_specialist` is listed as both Responsible and Accountable.
- **Step `o2c_003_inventory_allocation_fulfillment` (Inventory Allocation & Warehouse Fulfillment)**: Role `role_warehouse_supervisor` is listed as both Responsible and Accountable.
- **Step `p2m_001_demand_sensing_forecasting` (Statistical Demand Sensing & Forecasting)**: Role `role_demand_planner` is listed as both Responsible and Accountable.
- **Step `p2m_002_mrp_production_planning` (Material Requirements Planning (MRP))**: Role `role_production_scheduler` is listed as both Responsible and Accountable.
- **Step `p2m_004_manufacturing_execution` (Manufacturing Execution & Yield Tracking)**: Role `role_manufacturing_supervisor` is listed as both Responsible and Accountable.
- **Step `p2m_005_quality_inspection_release` (Quality Inspection & Batch Release)**: Role `role_quality_assurance_engineer` is listed as both Responsible and Accountable.
- **Step `p2m_006_finished_goods_putaway` (Finished Goods Put-Away & ATP Update)**: Role `role_inventory_manager` is listed as both Responsible and Accountable.
- **Step `s2p_004_contracting_sla_negotiation` (Contracting & SLA Negotiation)**: Role `role_category_manager` is listed as both Responsible and Accountable.