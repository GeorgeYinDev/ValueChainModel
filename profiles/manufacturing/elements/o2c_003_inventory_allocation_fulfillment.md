---
id: o2c_003_inventory_allocation_fulfillment
type: process_step
name: Inventory Allocation & Warehouse Fulfillment
version: 1.0.0
lifecycles: [O2C]
lod_support: [tier_1, tier_2, tier_3]
tags: [warehouse, logistics, inventory, shipping, fulfillment]

raci:
  responsible: [role_warehouse_supervisor]
  accountable: [role_warehouse_supervisor]
  consulted: [role_sales_ops_specialist]
  informed: [role_customer]

daci:
  driver: [role_warehouse_supervisor]
  approver: [role_warehouse_supervisor]
  contributor: [role_sales_ops_specialist]
  informed: [role_customer]

attributes:
  baseline_cycle_time_hours: 24.0
  baseline_cost_per_unit: 65.00
  automation_rate: 0.65
  error_rate: 0.015
  sla_hours: 48.0

asset_dependencies:
  - asset_wms_system
  - asset_erp_system
compensating_control: "WMS requires physical barcode scan and matches to ERP pick ticket before dispatch."

graph_relations:
  - relation: feeds_into
    target: o2c_004_billing_invoice_generation
    weight: 1.0
---

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
