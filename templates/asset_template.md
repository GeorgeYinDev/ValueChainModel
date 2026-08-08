---
id: asset_id_001
name: Asset Name
asset_type: it_application # [it_application, erp_module, database, api_gateway, financial_asset, physical_facility]
version: 1.0.0
parent_asset_id: null
status: operational
sla_uptime_percent: 99.9
capacity_max_tps: 500
---

# Enterprise Asset: [Asset Name]

## Overview & Architecture
Strategic overview of the asset, vendor platform, hosting environment, and capabilities.

## Parent & Child Dependencies
- **Parent Asset**: `parent_asset_id`
- **Child Sub-Assets**:
  - `child_asset_001`
  - `child_asset_002`

## Operational SLAs & Capacity Limits
- **Uptime SLA**: 99.9%
- **Throughput Capacity**: 500 transactions per second (TPS)
- **Recovery Time Objective (RTO)**: 4 hours
