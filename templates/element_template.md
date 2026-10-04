---
id: element_id_001
type: process_step # [process_step, value_stream, control_policy, kpi_metric, data_entity]
name: Name of Value Chain Element
version: 1.0.0
lifecycles: [S2P] # [S2P, O2C, H2R, R2R, P2P]
lod_support: [tier_1, tier_2, tier_3]
tags: [procurement, approval, financial]

raci:
  responsible: [role_procurement_specialist]
  accountable: [role_category_manager]
  consulted: [role_finance_controller]
  informed: [role_supplier]

daci:
  driver: [role_procurement_specialist]
  approver: [role_category_manager]
  contributor: [role_finance_controller]
  informed: [role_supplier]

attributes:
  baseline_cycle_time_hours: 24.0
  baseline_cost_per_unit: 15.50
  automation_rate: 0.85
  error_rate: 0.02
  sla_hours: 48.0

asset_dependencies:
  - asset_erp_system
  - asset_eprocurement_portal

graph_relations:
  - relation: feeds_into
    target: target_element_id_002
    weight: 1.0
  - relation: governed_by
    target: sod_spending_limits_policy
    weight: 0.90
---

# Name of Value Chain Element

## Executive Summary
Concise 2-3 sentence strategic summary of this process step for executive RAG indexing.

## 1. Strategic Intent & Outcome (Tier 1 - Executive Level)
- **Business Value**: Core outcome achieved by this step.
- **Strategic Alignment**: Supporting enterprise objectives (cost reduction, compliance, agility).
- **Risk Exposure**: Operational, regulatory, or financial risk profile.

## 2. Operational Workflow & RACI (Tier 2 - Process Architect Level)
- **Detailed Steps**: Sequential tasks executed in this node.
- **RACI Assignment Matrix**:
  - **Responsible (R)**: Operational execution role.
  - **Accountable (A)**: Signoff authority role.
  - **Consulted (C)**: Reviewers and subject matter experts.
  - **Informed (I)**: Stakeholders notified on completion.
- **Service Level Agreements (SLAs)**: Target cycle time and threshold metrics.
- **Business Rules & Exceptions**: Conditional branching logic.

## 3. Systems Math & Simulation Parameters (Tier 3 - Simulation Engineer Level)
```math
\text{Total Step Cost} = \text{Baseline Cost} \times (1 + \text{Error Rate}) + \frac{\text{Queue Delay}}{\text{Automation Rate}}
```
- **Inputs**: Primary data entities consumed.
- **Outputs**: Primary artifacts generated.
- **Bottleneck Sensitivity**: Operational behavior under volume spikes or asset degradation.
