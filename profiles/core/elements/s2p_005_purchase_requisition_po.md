---
id: s2p_005_purchase_requisition_po
type: process_step
name: Purchase Requisition & PO Issuance
version: 1.0.0
lifecycles: [S2P]
lod_support: [tier_1, tier_2, tier_3]
tags: [purchasing, po, requisition, approval]

raci:
  responsible: [role_procurement_specialist]
  accountable: [role_category_manager]
  consulted: [role_finance_controller]
  informed: [role_supplier]

attributes:
  baseline_cycle_time_hours: 8.0
  baseline_cost_per_unit: 18.00
  automation_rate: 0.90
  error_rate: 0.01
  sla_hours: 12.0

asset_dependencies:
  - asset_eprocurement_portal
  - asset_erp_system

graph_relations:
  - relation: feeds_into
    target: s2p_006_goods_services_receipt
    weight: 1.0
  - relation: governed_by
    target: sod_spending_limits_policy
    weight: 1.0
---

# Process Step: Purchase Requisition & PO Issuance

## Executive Summary
Validates financial budget availability, routes Purchase Requisitions (PR) through approval matrix workflows, and dispatches official Purchase Orders (PO) to vendors.

## 1. Strategic Intent & Outcome (Tier 1 - Executive Level)
- **Business Value**: Enforces pre-commitment financial control, budget verification, and purchasing governance.
- **Strategic Alignment**: Prevents unbudgeted spending and enforces contractually negotiated pricing.
- **Risk Exposure**: Budget overruns, unauthorized spending limits, or manual PO dispatch delays.

## 2. Operational Workflow & RACI (Tier 2 - Process Architect Level)
- **Workflow Sequence**:
  1. Business user submits PR; automated budget check against ERP General Ledger performed.
  2. PR routed to appropriate approvers according to spending limit thresholds.
  3. Approved PR automatically converted to PO and dispatched via EDI/Portal to supplier.
- **RACI Matrix**:
  - **Responsible**: `role_procurement_specialist`
  - **Accountable**: `role_category_manager`
  - **Consulted**: `role_finance_controller`
  - **Informed**: `role_supplier`
- **SLA**: 12.0 Hours.

## 3. Systems Math & Simulation Parameters (Tier 3 - Simulation Engineer Level)
```math
\text{PO Cycle Time} = \text{Baseline Cycle Time} \times \left(1 - \text{Automation Rate}\right) + \text{Approval Delay}
```
- **Primary Data Entity**: Purchase Order (`PO_RECORD_v1`).
- **Asset Load**: `asset_erp_system`, `asset_eprocurement_portal`.
