---
id: asset_payment_gateway
name: Corporate Banking Payment Gateway & ISO 20022 Router
asset_type: api_gateway
version: 3.0.1
parent_asset_id: asset_erp_system
status: operational
sla_uptime_percent: 99.99
capacity_max_tps: 1500
---

# Enterprise Asset: Banking Payment Gateway

## Overview & Architecture
Secure payment router transmitting encrypted ISO 20022 XML disbursement files and ACH/WIRE settlement batches directly to host-to-host banking networks.

## Parent & Child Dependencies
- **Parent Asset**: `asset_erp_system`
- **Child Sub-Assets**: `null`

## Operational SLAs & Capacity Limits
- **Uptime SLA**: 99.99%
- **Throughput Capacity**: 1,500 transactions per second (TPS)
- **Recovery Time Objective (RTO)**: 1 hour
- **Recovery Point Objective (RPO)**: 0 minutes (Synchronous Replication)
