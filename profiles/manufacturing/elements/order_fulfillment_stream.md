---
id: order_fulfillment_stream
type: value_stream
name: Order-to-Fulfillment & Cash Revenue Stream
version: 1.0.0
lifecycles: [O2C]
lod_support: [tier_1, tier_2, tier_3]
tags: [value_stream, order_to_cash, fulfillment, o2c]

raci:
  responsible: [role_sales_ops_specialist, role_warehouse_supervisor, role_billing_specialist]
  accountable: [role_finance_controller]
  consulted: [role_credit_manager]
  informed: [role_customer]

daci:
  driver: [role_sales_ops_specialist]
  approver: [role_finance_controller]
  contributor: [role_credit_manager]
  informed: [role_customer]

attributes:
  baseline_cycle_time_hours: 44.0
  baseline_cost_per_unit: 123.50
  automation_rate: 0.83
  error_rate: 0.012
  sla_hours: 96.0

asset_dependencies:
  - asset_erp_system
  - asset_crm_system
  - asset_wms_system
  - asset_payment_gateway

graph_relations:
  - relation: governed_by
    target: credit_limit_risk_policy
    weight: 1.0
  - relation: governed_by
    target: sod_spending_limits_policy
    weight: 0.95
---

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
