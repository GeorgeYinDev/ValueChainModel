# ADR 0003: Order-to-Cash (O2C) Lifecycle Taxonomy and Boundary Design

- **Status**: Approved
- **Date**: 2026-10-03
- **Authors**: Enterprise Architecture Team / Antigravity AI

## Context
The Order-to-Cash (O2C) lifecycle is the core commercial engine of the enterprise, capturing customer demand, governing commercial credit risk, executing physical logistics fulfillment, issuing billing documents, and clearing inbound cash collections.

Following the success of the Source-to-Pay (S2P) reference model (ADR-0002), we need to establish standardized boundaries, milestone steps, RACI/DACI governance, and IT system bindings for O2C.

## Decision
We define the O2C lifecycle as a 5-step sequential and milestone-driven value chain:
1. `o2c_001_customer_quote_order_entry`: CPQ configuration, order validation, and booking into ERP.
2. `o2c_002_credit_check_approval`: Total exposure computation, automatic hold rules, and underwriting sign-off.
3. `o2c_003_inventory_allocation_fulfillment`: ATP reservation, WMS wave picking, carrier dispatch, and Post Goods Issue.
4. `o2c_004_billing_invoice_generation`: Tax determination, EDI 810 electronic invoice dispatch, and revenue posting.
5. `o2c_005_cash_collection_reconciliation`: Electronic bank statement reconciliation, cash application, and AR clearing.

### Enterprise Roles Included
- Sales Operations Specialist (`role_sales_ops_specialist`)
- Credit & Risk Manager (`role_credit_manager`)
- Warehouse & Fulfillment Supervisor (`role_warehouse_supervisor`)
- Billing & AR Specialist (`role_billing_specialist`)
- Finance Controller (`role_finance_controller`)
- Enterprise Customer (`role_customer`)

### Core Assets Included
- Enterprise Core ERP (`asset_erp_system`)
- Cloud CRM & CPQ Platform (`asset_crm_system`)
- Automated Warehouse Management System (`asset_wms_system`)
- Corporate Banking Payment Gateway (`asset_payment_gateway`)

## Consequences
- Enables cross-lifecycle analysis (comparing procurement lead times in S2P with customer fulfillment in O2C).
- Provides quantitative scenario simulations (e.g. credit hold bottlenecks, fulfillment wave delays).
- Integrates both RACI (operational execution) and DACI (decision governance) matrices across commercial milestones.
