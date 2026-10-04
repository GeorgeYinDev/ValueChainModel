# Enterprise RACI Governance Matrix [ALL]

> **RACI Legend**: **R** = Responsible (Executes) | **A** = Accountable (Approves) | **C** = Consulted (Inputs) | **I** = Informed (Notified)

## 1. Value Chain Process RACI Grid

| Step ID | Process Step Name | Warehouse & Fulfillment Supervisor | Sales Operations Specialist | Billing & Accounts Receivable Specialist | Finance Controller | Supplier / Vendor | Category Manager | General Ledger Accountant | Credit & Risk Manager | Procurement Specialist | Financial Consolidation Specialist | Enterprise Customer | Accounts Payable Clerk | Internal Auditor |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `o2c_001_customer_quote_order_entry` | **Quote Generation & Order Capture** | - | **R**, **A** | - | - | - | - | - | I | - | - | C | - | - |
| `o2c_002_credit_check_approval` | **Customer Credit Assessment & Exposure Check** | - | C | - | **A** | - | - | - | **R** | - | - | I | - | - |
| `o2c_003_inventory_allocation_fulfillment` | **Inventory Allocation & Warehouse Fulfillment** | **R**, **A** | C | - | - | - | - | - | - | - | - | I | - | - |
| `o2c_004_billing_invoice_generation` | **Customer Billing & Electronic Invoicing** | - | C | **R** | **A** | - | - | - | - | - | - | I | - | - |
| `o2c_005_cash_collection_reconciliation` | **Cash Collection & Accounts Receivable Reconciliation** | - | I | **R** | **A** | - | - | - | - | - | - | C | - | - |
| `r2r_001_journal_entry_recording` | **General Ledger Journal Recording & Subledger Ingestion** | - | - | C | **A** | - | - | **R** | - | - | - | - | C | I |
| `r2r_002_intercompany_reconciliation` | **Intercompany Transaction Matching & Elimination** | - | - | - | **A** | - | - | C | - | - | **R** | - | - | I |
| `r2r_003_balance_sheet_substantiation` | **Balance Sheet Account Substantiation & Reconciliation** | - | - | - | **A** | - | - | **R** | - | - | C | - | - | I |
| `r2r_004_financial_close_consolidation` | **Financial Close Orchestration & Group Consolidation** | - | - | - | **A** | - | - | C | - | - | **R** | - | - | I |
| `r2r_005_statutory_financial_reporting` | **Statutory, Tax & Management Financial Reporting** | - | - | - | **A** | - | - | I | - | - | **R** | - | - | C |
| `s2p_001_spend_analysis_need_id` | **Spend Analysis & Need Identification** | - | - | - | C | I | **A** | - | - | **R** | - | - | - | - |
| `s2p_002_supplier_discovery_qualification` | **Supplier Discovery & Qualification** | - | - | - | C | I | **A** | - | - | **R** | - | - | - | - |
| `s2p_003_sourcing_rfx_auction` | **Strategic Sourcing & RFx Execution** | - | - | - | C | I | **A** | - | - | **R** | - | - | - | - |
| `s2p_004_contracting_sla_negotiation` | **Contracting & SLA Negotiation** | - | - | - | C | I | **R**, **A** | - | - | - | - | - | - | - |
| `s2p_005_purchase_requisition_po` | **Purchase Requisition & PO Issuance** | - | - | - | C | I | **A** | - | - | **R** | - | - | - | - |
| `s2p_006_goods_services_receipt` | **Goods & Services Receipt Verification** | - | - | - | - | I | **A** | - | - | **R** | - | - | C | - |
| `s2p_007_invoice_verification_matching` | **Invoice 3-Way Matching & Exception Handling** | - | - | - | **A** | I | - | - | - | C | - | - | **R** | - |
| `s2p_008_payment_settlement_disbursement` | **Payment Settlement & Disbursement** | - | - | - | **A** | I | C | - | - | - | - | - | **R** | - |

---

## 2. Role Workload & Touchpoint Distribution

| Enterprise Role | Responsible (R) | Accountable (A) | Consulted (C) | Informed (I) | Total Touchpoints | Operational Load |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Warehouse & Fulfillment Supervisor** (`role_warehouse_supervisor`) | 1 | 1 | 0 | 0 | **2** | 🟢 Low |
| **Sales Operations Specialist** (`role_sales_ops_specialist`) | 1 | 1 | 3 | 1 | **6** | 🔴 High (Key Dependency) |
| **Billing & Accounts Receivable Specialist** (`role_billing_specialist`) | 2 | 0 | 1 | 0 | **3** | 🟡 Moderate |
| **Finance Controller** (`role_finance_controller`) | 0 | 10 | 5 | 0 | **15** | 🔴 High (Key Dependency) |
| **Supplier / Vendor** (`role_supplier`) | 0 | 0 | 0 | 8 | **8** | 🔴 High (Key Dependency) |
| **Category Manager** (`role_category_manager`) | 1 | 6 | 1 | 0 | **8** | 🔴 High (Key Dependency) |
| **General Ledger Accountant** (`role_general_ledger_accountant`) | 2 | 0 | 2 | 1 | **5** | 🟡 Moderate |
| **Credit & Risk Manager** (`role_credit_manager`) | 1 | 0 | 0 | 1 | **2** | 🟢 Low |
| **Procurement Specialist** (`role_procurement_specialist`) | 5 | 0 | 1 | 0 | **6** | 🔴 High (Key Dependency) |
| **Financial Consolidation Specialist** (`role_consolidation_specialist`) | 3 | 0 | 1 | 0 | **4** | 🔴 High (Key Dependency) |
| **Enterprise Customer** (`role_customer`) | 0 | 0 | 2 | 3 | **5** | 🟡 Moderate |
| **Accounts Payable Clerk** (`role_accounts_payable_clerk`) | 2 | 0 | 2 | 0 | **4** | 🟡 Moderate |
| **Internal Auditor** (`role_internal_auditor`) | 0 | 0 | 1 | 4 | **5** | 🟡 Moderate |

---

## 3. Segregation of Duties (SoD) & Conflict Analysis

⚠️ **Potential Segregation of Duties (SoD) Overlaps Detected:**

- **Step `o2c_001_customer_quote_order_entry` (Quote Generation & Order Capture)**: Role `role_sales_ops_specialist` is listed as both Responsible and Accountable.
- **Step `o2c_003_inventory_allocation_fulfillment` (Inventory Allocation & Warehouse Fulfillment)**: Role `role_warehouse_supervisor` is listed as both Responsible and Accountable.
- **Step `s2p_004_contracting_sla_negotiation` (Contracting & SLA Negotiation)**: Role `role_category_manager` is listed as both Responsible and Accountable.