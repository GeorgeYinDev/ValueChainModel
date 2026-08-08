---
id: s2p_002_supplier_discovery_qualification
type: process_step
name: Supplier Discovery & Qualification
version: 1.0.0
lifecycles: [S2P]
lod_support: [tier_1, tier_2, tier_3]
tags: [vendor_management, compliance, risk]

raci:
  responsible: [role_procurement_specialist]
  accountable: [role_category_manager]
  consulted: [role_finance_controller]
  informed: [role_supplier]

attributes:
  baseline_cycle_time_hours: 48.0
  baseline_cost_per_unit: 120.00
  automation_rate: 0.50
  error_rate: 0.05
  sla_hours: 72.0

asset_dependencies:
  - asset_eprocurement_portal

graph_relations:
  - relation: feeds_into
    target: s2p_003_sourcing_rfx_auction
    weight: 1.0
  - relation: governed_by
    target: sod_spending_limits_policy
    weight: 0.90
---

# Process Step: Supplier Discovery & Qualification

## Executive Summary
Evaluates potential suppliers for financial stability, ESG compliance, regulatory sanctions, and operational capability prior to bid participation.

## 1. Strategic Intent & Outcome (Tier 1 - Executive Level)
- **Business Value**: Mitigates supply chain disruption, reputational risk, and regulatory non-compliance.
- **Strategic Alignment**: Ensures supplier diversity targets and ESG corporate governance metrics are met.
- **Risk Exposure**: Vendor bankruptcy, PEP/Sanction violations, or single-source dependency.

## 2. Operational Workflow & RACI (Tier 2 - Process Architect Level)
- **Workflow Sequence**:
  1. Vendor submits RFI (Request for Information) and compliance documentation via supplier portal.
  2. Financial risk scoring, credit checks, and Sanctions screening automated via third-party APIs.
  3. Category Manager reviews qualification score and admits vendor to approved master pool.
- **RACI Matrix**:
  - **Responsible**: `role_procurement_specialist`
  - **Accountable**: `role_category_manager`
  - **Consulted**: `role_finance_controller`
  - **Informed**: `role_supplier`
- **SLA**: 72.0 Hours.

## 3. Systems Math & Simulation Parameters (Tier 3 - Simulation Engineer Level)
```math
\text{Qualification Time} = \text{Baseline Cycle Time} + \left(1 - \text{Automation Rate}\right) \times \text{Vendor Risk Complexity Factor} \times 24.0
```
- **Primary Data Entity**: Qualified Vendor Record (`VENDOR_QUAL_v1`).
- **Asset Load**: `asset_eprocurement_portal`.
