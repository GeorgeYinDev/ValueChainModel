---
id: asset_financial_consolidation_system
name: Enterprise Financial Consolidation & Reporting System (SAP Group Reporting / OneStream)
asset_type: it_application
version: 3.4.0
parent_asset_id: asset_erp_system
status: operational
sla_uptime_percent: 99.90
capacity_max_tps: 500
---

# Enterprise Asset: Financial Consolidation & Reporting System

## Overview & Architecture
The enterprise platform dedicated to corporate financial consolidation, statutory reporting, intercompany matching, foreign currency translation, and financial disclosure orchestration across all legal entities.

## Parent & Child Dependencies
- **Parent Asset**: `asset_erp_system` (Core ERP Ledger Feeder)
- **Child Sub-Assets**: None (Specialized Enterprise Reporting Node)

## Operational SLAs & Capacity Limits
- **Uptime SLA**: 99.90%
- **Throughput Capacity**: 500 transactions per second (Consolidation Calculation & Data Ingestion)
- **Recovery Time Objective (RTO)**: 4 hours
- **Recovery Point Objective (RPO)**: 30 minutes
