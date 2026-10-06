---
id: asset_crm_system
name: Enterprise Cloud CRM & CPQ Platform (Salesforce)
asset_type: it_application
version: 2.4.0
parent_asset_id: asset_erp_system
status: operational
sla_uptime_percent: 99.9
capacity_max_tps: 1200
---

# Enterprise Asset: Cloud CRM & CPQ Platform

## Overview & Architecture
Cloud-native Customer Relationship Management (CRM) and Configure-Price-Quote (CPQ) engine managing account hierarchies, sales pipelines, complex pricing rules, quote approvals, and commercial contract terms.

## Parent & Child Dependencies
- **Parent Asset**: `asset_erp_system` (Synchronizes customer master records, price books, and sales orders via bi-directional REST APIs).
- **Child Sub-Assets**: None.

## Operational SLAs & Capacity Limits
- **Uptime SLA**: 99.9%
- **Throughput Capacity**: 1,200 transactions per second (TPS)
- **Recovery Time Objective (RTO)**: 2.0 hours
