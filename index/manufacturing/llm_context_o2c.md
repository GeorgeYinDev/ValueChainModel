# System Prompt: LLM Context Blueprint for Business Lifecycle [Order to Cash Lifecycle]

> Profile: `manufacturing` | Lifecycle ID: `O2C` | Version: `1.0.0` | Source Layer: `manufacturing`
> Description: End-to-end sales lifecycle from customer quote and order entry through order fulfillment, billing, credit management, and cash collection.

## Milestone Process Sequence
- **Step 1**: `o2c_001_customer_quote_order_entry` (Quote Generation & Order Capture)
- **Step 2**: `o2c_002_credit_check_approval` (Customer Credit Assessment)
- **Step 3**: `o2c_003_inventory_allocation_fulfillment` (Inventory Allocation & Warehousing)
- **Step 4**: `o2c_004_billing_invoice_generation` (Customer Billing & Invoicing)
- **Step 5**: `o2c_005_cash_collection_reconciliation` (Cash Collection & Accounts Receivable Match)

## Key Performance Indicators (KPIs)
- `days_sales_outstanding_dso`
- `order_fulfillment_lead_time`
- `perfect_order_rate`

## Active Value Chain Elements Knowledge Base

### [Segregation of Duties & Financial Authority Policy] (`sod_spending_limits_policy`) [Layer: `core`]
- **Type**: `control_policy` | **Tags**: `policy, governance, sod, compliance`
- **RACI**: `{"responsible": ["role_finance_controller"], "accountable": ["role_finance_controller"], "consulted": ["role_category_manager"], "informed": ["role_procurement_specialist", "role_accounts_payable_clerk"]}`
- **Assets**: `asset_erp_system`

# Control Policy: Segregation of Duties (SoD) & Spending Limits

## Executive Summary
Establishes enterprise internal control policies mandating that no single individual can initiate a purchase, approve the purchase order, verify goods receipt, and execute payment disbursement.

## 1. Governance Rules & Controls (Tier 1)
- **Rule 1 (SoD Incompatibility)**: A single user cannot hold both `role_procurement_specialist` (PO creation) and `role_accounts_payable_clerk` (Invoice voucher creation).
- **Rule 2 (Dual Disbursement Signoff)**: Payments exceeding $100,000 USD require dual approval from `role_finance_controller`.
- **Rule 3 (Spending Threshold Hierarchy)**:
  - Buyer: up to $50,000 USD.
  - Category Manager: up to $500,000 USD.
  - Finance Controller: unlimited.
---

### [Commercial Credit Limit & Customer Risk Exposure Policy] (`credit_limit_risk_policy`) [Layer: `manufacturing`]
- **Type**: `control_policy` | **Tags**: `policy, credit, risk, compliance`
- **RACI**: `{"responsible": ["role_credit_manager"], "accountable": ["role_finance_controller"], "consulted": ["role_sales_ops_specialist"], "informed": ["role_customer"]}`
- **Assets**: `asset_erp_system, asset_crm_system`

# Control Policy: Commercial Credit Limit & Risk Exposure

## Executive Summary
Defines corporate governance standards for underwriting customer credit limits, monitoring rolling accounts receivable exposures, and enforcing automatic order holds to prevent bad debt default.

## 1. Governance Rules & Controls (Tier 1)
- **Rule 1 (Automatic Credit Hold)**: Orders exceeding a customer's approved credit limit or accounts with past-due balances >60 days are automatically placed on credit hold in `asset_erp_system`.
- **Rule 2 (Single Underwriter Limit)**: Orders under credit hold up to $250,000 USD can be released solely by `role_credit_manager`.
- **Rule 3 (Executive Exception Approval)**: Overrides exceeding $250,000 USD mandate formal sign-off from `role_finance_controller` with collateral or parent company guarantee.
---

### [Days Sales Outstanding (DSO)] (`kpi_dso`) [Layer: `manufacturing`]
- **Type**: `kpi_metric` | **Tags**: `kpi, receivables, cash_flow`
- **RACI**: `{}`
- **Assets**: ``

# KPI: Days Sales Outstanding (DSO)

Measures the average number of days that it takes a company to collect payment after a sale has been made. Critical metric for evaluating cash flow and accounts receivable efficiency in the Order-to-Cash lifecycle.
---

### [Quote Generation & Order Capture] (`o2c_001_customer_quote_order_entry`) [Layer: `manufacturing`]
- **Type**: `process_step` | **Tags**: `order_management, sales, quoting, cpq`
- **RACI**: `{"responsible": ["role_sales_ops_specialist"], "accountable": ["role_sales_ops_specialist"], "consulted": ["role_customer"], "informed": ["role_credit_manager"]}`
- **Assets**: `asset_crm_system, asset_erp_system`

# Process Step: Quote Generation & Order Capture

## Executive Summary
Captures customer demand, configures products and services via Configure-Price-Quote (CPQ), validates contractual discounting, and converts signed quotes into formal enterprise sales orders.

## 1. Strategic Intent & Outcome (Tier 1 - Executive Level)
- **Business Value**: Drives top-line revenue velocity, eliminates order entry errors, and guarantees price-book and margin governance.
- **Strategic Alignment**: Directly supports commercial growth, customer satisfaction (CSAT), and revenue predictability.
- **Risk Exposure**: Inaccurate pricing terms, unapproved contract liabilities, or catalog configuration mismatches.

## 2. Operational Workflow & RACI (Tier 2 - Process Architect Level)
- **Workflow Sequence**:
  1. Customer submits Request for Quotation (RFQ) or digital purchase order through portal or EDI.
  2. CPQ rules engine validates product compatibility, lead-time availability, and volume discount schedule.
  3. Pricing exceptions outside standard authority matrix route to sales leadership for approval.
  4. Confirmed order payload creates open Sales Order header and line items in `asset_erp_system`.
- **RACI Assignment Matrix**:
  - **Responsible**: `role_sales_ops_specialist`
  - **Accountable**: `role_sales_ops_specialist`
  - **Consulted**: `role_customer`
  - **Informed**: `role_credit_manager`
- **Service Level Agreement (SLA)**: 12.0 Hours.

## 3. Systems Math & Simulation Parameters (Tier 3 - Simulation Engineer Level)
```math
\text{Order Capture Latency} = \text{Baseline Cycle Time} \times \left(1 + \frac{\text{Pricing Exception Rate}}{\text{CPQ Automation Rate}}\right)
```
- **Primary Data Entity**: Sales Order Document (`SALES_ORDER_v1`).
- **Asset Load**: Interrogates Salesforce CPQ via `asset_crm_system` and persists to SAP S/4HANA via `asset_erp_system`.
---

### [Customer Credit Assessment & Exposure Check] (`o2c_002_credit_check_approval`) [Layer: `manufacturing`]
- **Type**: `process_step` | **Tags**: `credit, risk, underwriting, compliance`
- **RACI**: `{"responsible": ["role_credit_manager"], "accountable": ["role_finance_controller"], "consulted": ["role_sales_ops_specialist"], "informed": ["role_customer"]}`
- **Assets**: `asset_erp_system, asset_crm_system`

# Process Step: Customer Credit Assessment & Exposure Check

## Executive Summary
Evaluates customer commercial creditworthiness, computes rolling accounts receivable exposures, and adjudicates automated or manual credit holds prior to physical inventory commitment.

## 1. Strategic Intent & Outcome (Tier 1 - Executive Level)
- **Business Value**: Safeguards corporate balance sheet liquidity, prevents bad debt write-offs, and enforces disciplined working capital management.
- **Strategic Alignment**: Directly supports risk governance, SOX financial reporting controls, and corporate cash conversion cycle targets.
- **Risk Exposure**: Insolvent buyer default, uncollectible revenue, or commercial sales friction due to unwarranted credit holds.

## 2. Operational Workflow & RACI (Tier 2 - Process Architect Level)
- **Workflow Sequence**:
  1. Sales order creation triggers automated credit check evaluating total exposure (Open AR + Unbilled Deliveries + Current Order).
  2. If total exposure is within approved credit line and no invoices are >60 days past due, order is automatically released.
  3. If credit limit is breached, an automated credit hold lock is applied in `asset_erp_system`.
  4. Credit Underwriter reviews financial statements, payment history, and either requests payment or secures controller override.
- **RACI Assignment Matrix**:
  - **Responsible**: `role_credit_manager`
  - **Accountable**: `role_finance_controller`
  - **Consulted**: `role_sales_ops_specialist`
  - **Informed**: `role_customer`
- **Service Level Agreement (SLA)**: 8.0 Hours.

## 3. Systems Math & Simulation Parameters (Tier 3 - Simulation Engineer Level)
```math
\text{Total Exposure} = \text{Open AR Balance} + \sum \text{Unbilled Shipments} + \text{Order Value}
```
```math
\text{Credit Verification Delay} = \text{Baseline Cycle Time} \times \left(1 + \frac{\text{Credit Exception Ratio}}{\text{Auto-Approval Rate}}\right)
```
- **Primary Data Entity**: Credit Decision Record (`CREDIT_DECISION_v1`).
- **Asset Load**: ERP Credit Management module in `asset_erp_system` with credit score feed from `asset_crm_system`.
---

### [Inventory Allocation & Warehouse Fulfillment] (`o2c_003_inventory_allocation_fulfillment`) [Layer: `manufacturing`]
- **Type**: `process_step` | **Tags**: `warehouse, logistics, inventory, shipping, fulfillment`
- **RACI**: `{"responsible": ["role_warehouse_supervisor"], "accountable": ["role_warehouse_supervisor"], "consulted": ["role_sales_ops_specialist"], "informed": ["role_customer"]}`
- **Assets**: `asset_wms_system, asset_erp_system`

# Process Step: Inventory Allocation & Warehouse Fulfillment

## Executive Summary
Reserves available stock, schedules warehouse wave fulfillment, executes pick-pack-ship operations, and dispatches freight carriers with validated Proof of Delivery tracking.

## 1. Strategic Intent & Outcome (Tier 1 - Executive Level)
- **Business Value**: Guarantees On-Time In-Full (OTIF) customer fulfillment, minimizes carrying costs, and eliminates shipping discrepancies.
- **Strategic Alignment**: Directly drives customer net promoter score (NPS), carrier SLA adherence, and operational logistics efficiency.
- **Risk Exposure**: Stockouts, shipping delays, picking inaccuracies, or transit damage claims.

## 2. Operational Workflow & RACI (Tier 2 - Process Architect Level)
- **Workflow Sequence**:
  1. Credit-approved sales orders trigger an Available-to-Promise (ATP) hard reservation in ERP.
  2. Outbound delivery document dispatches to `asset_wms_system` for wave planning.
  3. Warehouse automated guided vehicles (AGVs) or pickers pull items against barcode scan verification.
  4. Packaging station weighs pallets, generates Bill of Lading (BOL), and applies carrier tracking barcodes.
  5. Carrier pickup confirms physical dispatch and triggers Post Goods Issue (PGI) in `asset_erp_system`.
- **RACI Assignment Matrix**:
  - **Responsible**: `role_warehouse_supervisor`
  - **Accountable**: `role_warehouse_supervisor`
  - **Consulted**: `role_sales_ops_specialist`
  - **Informed**: `role_customer`
- **Service Level Agreement (SLA)**: 48.0 Hours.

## 3. Systems Math & Simulation Parameters (Tier 3 - Simulation Engineer Level)
```math
\text{Fulfillment Lead Time} = \text{Wave Scheduling Latency} + \frac{\text{Pick Time}}{\text{Automation Rate}} + \text{Carrier Dock Dwell Time}
```
- **Primary Data Entity**: Outbound Delivery Document (`DELIVERY_ORDER_v1`).
- **Asset Load**: Execution orchestrated via `asset_wms_system` and committed to inventory ledger in `asset_erp_system`.
---

### [Customer Billing & Electronic Invoicing] (`o2c_004_billing_invoice_generation`) [Layer: `manufacturing`]
- **Type**: `process_step` | **Tags**: `billing, invoicing, revenue, accounting`
- **RACI**: `{"responsible": ["role_billing_specialist"], "accountable": ["role_finance_controller"], "consulted": ["role_sales_ops_specialist"], "informed": ["role_customer"]}`
- **Assets**: `asset_erp_system, asset_crm_system`

# Process Step: Customer Billing & Electronic Invoicing

## Executive Summary
Generates legally compliant tax invoices upon confirmation of delivery, determines jurisdiction sales taxes, and dispatches electronic invoices via EDI, customer portals, or Peppol e-delivery.

## 1. Strategic Intent & Outcome (Tier 1 - Executive Level)
- **Business Value**: Accelerates revenue recognition, shortens billing cycles, and minimizes Days Sales Outstanding (DSO).
- **Strategic Alignment**: Directly aligns with ASC 606 revenue recognition standards, global e-invoicing mandates, and statutory tax compliance.
- **Risk Exposure**: Tax jurisdiction determination errors, invoicing disputes, or delivery-to-billing lead time leakage.

## 2. Operational Workflow & RACI (Tier 2 - Process Architect Level)
- **Workflow Sequence**:
  1. Post Goods Issue (PGI) event triggers automated billing due-list in `asset_erp_system`.
  2. Automated Vertex/Avalara tax engine computes state, local, or VAT taxes based on ship-to location.
  3. Formal electronic billing document (EDI 810 / XML) generated and dispatched to `role_customer`.
  4. General ledger updates Accounts Receivable asset account and credits earned revenue.
- **RACI Assignment Matrix**:
  - **Responsible**: `role_billing_specialist`
  - **Accountable**: `role_finance_controller`
  - **Consulted**: `role_sales_ops_specialist`
  - **Informed**: `role_customer`
- **Service Level Agreement (SLA)**: 4.0 Hours.

## 3. Systems Math & Simulation Parameters (Tier 3 - Simulation Engineer Level)
```math
\text{Billing Unit Cost} = \text{Baseline Cost} \times (1 + \text{Error Rate}) + \frac{\text{Manual Exception Hours}}{\text{Automation Rate}}
```
- **Primary Data Entity**: Customer Tax Invoice Document (`CUSTOMER_INVOICE_v1`).
- **Asset Load**: Core billing document generated in `asset_erp_system` and archived in `asset_crm_system`.
---

### [Cash Collection & Accounts Receivable Reconciliation] (`o2c_005_cash_collection_reconciliation`) [Layer: `manufacturing`]
- **Type**: `process_step` | **Tags**: `treasury, cash_application, ar, reconciliation, banking`
- **RACI**: `{"responsible": ["role_billing_specialist"], "accountable": ["role_finance_controller"], "consulted": ["role_customer"], "informed": ["role_sales_ops_specialist"]}`
- **Assets**: `asset_erp_system, asset_payment_gateway`

# Process Step: Cash Collection & Accounts Receivable Match

## Executive Summary
Matches inbound electronic bank remittances (ACH, wire, credit card) against open customer invoices, applies payment settlements, and resolves deductions or short-payment exceptions.

## 1. Strategic Intent & Outcome (Tier 1 - Executive Level)
- **Business Value**: Optimizes cash liquidity, minimizes unapplied cash balances, and ensures rapid restoration of customer credit availability.
- **Strategic Alignment**: Directly drives operating cash flow (OCF), working capital velocity, and bad debt reserve reduction.
- **Risk Exposure**: Unapplied cash backlogs, unearned discount taking by clients, or undetected customer solvency crises.

## 2. Operational Workflow & RACI (Tier 2 - Process Architect Level)
- **Workflow Sequence**:
  1. Electronic bank statements (BAI2 / ISO 20022 CAMT.053) received daily via `asset_payment_gateway`.
  2. Cash application engine automatically reconciles remittance advice against open invoice numbers.
  3. Fully matched line items post clearing entries, clearing Accounts Receivable and debiting Operating Cash.
  4. Discrepancies (unidentified deposits, short-payments) route to AR specialist for deduction management.
- **RACI Assignment Matrix**:
  - **Responsible**: `role_billing_specialist`
  - **Accountable**: `role_finance_controller`
  - **Consulted**: `role_customer`
  - **Informed**: `role_sales_ops_specialist`
- **Service Level Agreement (SLA)**: 24.0 Hours.

## 3. Systems Math & Simulation Parameters (Tier 3 - Simulation Engineer Level)
```math
\text{DSO Reduction Delta} = \frac{\text{Total Open AR}}{\text{Daily Gross Sales}} \times \left(1 - \text{Auto-Match Rate}\right)
```
- **Primary Data Entity**: Remittance Clearing Voucher (`CASH_SETTLEMENT_v1`).
- **Asset Load**: Inbound bank feed processed via `asset_payment_gateway` and matched into `asset_erp_system`.
---

### [Order-to-Fulfillment & Cash Revenue Stream] (`order_fulfillment_stream`) [Layer: `manufacturing`]
- **Type**: `value_stream` | **Tags**: `value_stream, order_to_cash, fulfillment, o2c`
- **RACI**: `{"responsible": ["role_sales_ops_specialist", "role_warehouse_supervisor", "role_billing_specialist"], "accountable": ["role_finance_controller"], "consulted": ["role_credit_manager"], "informed": ["role_customer"]}`
- **Assets**: `asset_erp_system, asset_crm_system, asset_wms_system, asset_payment_gateway`

# Value Stream: Order to Cash (O2C)

## Executive Summary
Encompasses the complete customer commercial lifecycle from quote capture and credit adjudication through automated inventory allocation, physical delivery, billing, and cash reconciliation (Steps 001 - 005).

## 1. Strategic Outcomes (Tier 1)
- Accelerate Days Sales Outstanding (DSO) and optimize working capital.
- Ensure perfect order delivery rate (>98%) with real-time shipment visibility.
- Prevent revenue leakage and eliminate bad debt write-offs through automated credit holds.

## 2. Included Steps & RACI Summary (Tier 2)
1. `o2c_001_customer_quote_order_entry`
2. `o2c_002_credit_check_approval`
3. `o2c_003_inventory_allocation_fulfillment`
4. `o2c_004_billing_invoice_generation`
5. `o2c_005_cash_collection_reconciliation`
---

