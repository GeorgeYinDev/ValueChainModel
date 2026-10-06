---
id: s2p_001_spend_analysis_need_id
type: process_step
name: Spend Analysis & Need Identification
version: 1.0.0
lifecycles: [S2P]
lod_support: [tier_1, tier_2, tier_3]
tags: [procurement, analytics, requisition]

raci:
  responsible: [role_procurement_specialist]
  accountable: [role_category_manager]
  consulted: [role_finance_controller]
  informed: [role_supplier]

attributes:
  baseline_cycle_time_hours: 12.0
  baseline_cost_per_unit: 45.00
  automation_rate: 0.70
  error_rate: 0.03
  sla_hours: 24.0

asset_dependencies:
  - asset_eprocurement_portal
  - asset_erp_system

graph_relations:
  - relation: feeds_into
    target: s2p_002_supplier_discovery_qualification
    weight: 1.0
  - relation: governed_by
    target: sod_spending_limits_policy
    weight: 0.85
---

# Process Step: Spend Analysis & Need Identification

## Executive Summary
Initiates the Source-to-Pay lifecycle by aggregating historical spend data, identifying business procurement requirements, and creating initial demand requests.

## 1. Strategic Intent & Outcome (Tier 1 - Executive Level)
- **Business Value**: Eliminates maverick spending, consolidates demand leverage, and aligns sourcing projects with budgetary constraints.
- **Strategic Alignment**: Directly supports corporate EBITDA optimization and working capital management.
- **Risk Exposure**: Inaccurate demand forecasting or unapproved off-contract purchasing.

## 2. Operational Workflow & RACI (Tier 2 - Process Architect Level)
- **Workflow Sequence**:
  1. Business unit submits business need or automated reorder threshold triggers requisition.
  2. Procurement Analytics engine matches demand against existing preferred supplier catalogs.
  3. Requisition details (UNSPSC commodity code, budget center, target lead time) validated.
- **RACI Matrix**:
  - **Responsible**: `role_procurement_specialist`
  - **Accountable**: `role_category_manager`
  - **Consulted**: `role_finance_controller`
  - **Informed**: `role_supplier`
- **SLA**: 24.0 Hours.

## 3. Systems Math & Simulation Parameters (Tier 3 - Simulation Engineer Level)
```math
\text{Need Identification Latency} = \text{Baseline Cycle Time} \times \left(1 + \frac{\text{Unmapped Spend Ratio}}{\text{Automation Rate}}\right)
```
- **Primary Data Entity**: Purchase Requisition Draft (`PR_DRAFT_v1`).
- **Asset Load**: Interrogates ERP Master Ledger via `asset_eprocurement_portal`.
