# System Prompt: LLM Context Blueprint for Business Lifecycle [Order to Cash Lifecycle]

> Lifecycle ID: `O2C` | Version: `1.0.0`
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

### [Segregation of Duties & Financial Authority Policy] (`sod_spending_limits_policy`)
- **Type**: `control_policy` | **Tags**: `policy, governance, sod, compliance`
- **RACI**: `{}`
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

