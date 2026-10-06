---
id: procure_to_pay_stream
type: value_stream
name: Procure to Pay (P2P) Operational Value Stream
version: 1.0.0
lifecycles: [S2P]
lod_support: [tier_1, tier_2, tier_3]
tags: [value_stream, procure_to_pay, p2p]

raci:
  responsible: [role_procurement_specialist, role_accounts_payable_clerk]
  accountable: [role_finance_controller]
  consulted: [role_category_manager]
  informed: [role_supplier]

attributes:
  baseline_cycle_time_hours: 34.0
  baseline_cost_per_unit: 60.50
  automation_rate: 0.85
  error_rate: 0.018
  sla_hours: 56.0

asset_dependencies:
  - asset_erp_system
  - asset_eprocurement_portal
  - asset_payment_gateway

graph_relations:
  - relation: governed_by
    target: sod_spending_limits_policy
    weight: 1.0
---

# Value Stream: Procure to Pay (P2P)

## Executive Summary
Encompasses the transactional execution lifecycle from purchase requisition approval and PO dispatch through receiving, 3-way invoice matching, and final payment settlement (Steps 005 - 008).

## 1. Strategic Outcomes (Tier 1)
- Operational procurement efficiency and SLA compliance.
- 100% 3-way invoice match accuracy and discount capture.
- Treasury cash management and disbursement automation.

## 2. Included Steps & RACI Summary (Tier 2)
1. `s2p_005_purchase_requisition_po`
2. `s2p_006_goods_services_receipt`
3. `s2p_007_invoice_verification_matching`
4. `s2p_008_payment_settlement_disbursement`
