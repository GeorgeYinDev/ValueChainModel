---
id: asset_wms_system
name: Automated Warehouse Management & Dispatch System (SAP EWM)
asset_type: it_application
version: 3.1.2
parent_asset_id: asset_erp_system
status: operational
sla_uptime_percent: 99.95
capacity_max_tps: 600
---

# Enterprise Asset: Automated Warehouse Management System (WMS)

## Overview & Architecture
High-throughput warehouse management and execution platform coordinating automated storage and retrieval systems (ASRS), RF barcode scanners, conveyor routing, and dispatch dock assignments.

## Parent & Child Dependencies
- **Parent Asset**: `asset_erp_system` (Ingests outbound deliveries and posts goods issues back to inventory ledger).
- **Child Sub-Assets**: None.

## Operational SLAs & Capacity Limits
- **Uptime SLA**: 99.95%
- **Throughput Capacity**: 600 transactions per second (TPS)
- **Recovery Time Objective (RTO)**: 1.0 hour
