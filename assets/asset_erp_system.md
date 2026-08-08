---
id: asset_erp_system
name: Enterprise Core ERP (SAP S/4HANA)
asset_type: it_application
version: 2.1.0
parent_asset_id: null
status: operational
sla_uptime_percent: 99.95
capacity_max_tps: 2500
---

# Enterprise Asset: Core ERP System

## Overview & Architecture
The primary system of record for financial ledgers, purchase order execution, inventory management, and accounts payable processing.

## Parent & Child Dependencies
- **Parent Asset**: `null` (Root Enterprise IT Asset)
- **Child Sub-Assets**:
  - `asset_eprocurement_portal` (Cloud Integration Interface)
  - `asset_payment_gateway` (Banking Disbursement Interface)

## Operational SLAs & Capacity Limits
- **Uptime SLA**: 99.95%
- **Throughput Capacity**: 2,500 transactions per second (TPS)
- **Recovery Time Objective (RTO)**: 2 hours
- **Recovery Point Objective (RPO)**: 15 minutes
