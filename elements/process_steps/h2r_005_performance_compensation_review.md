---
id: h2r_005_performance_compensation_review
type: process_step
name: "Performance & Compensation Review"
version: "1.0.0"
lifecycles: ["H2R"]
lod_support: ["tier_1", "tier_2", "tier_3"]
tags: ["hr", "performance", "compensation"]

raci:
  responsible: [role_hiring_manager]
  accountable: [role_hiring_manager]
  consulted: [role_hr_business_partner, role_compensation_analyst]
  informed: [role_payroll_specialist]

attributes:
  baseline_cycle_time_hours: 120.0
  baseline_cost_per_unit: 200.0
  automation_rate: 0.40
  error_rate: 0.05
  sla_hours: 336.0
  volume_per_period: 1000
  capacity_fte: 10.0

asset_dependencies:
  - asset_hcm_platform

graph_relations:
  - relation: feeds_into
    target: h2r_006_separation_offboarding_settlement
    weight: 0.10

compensating_control: "HRBP facilitates calibration sessions to normalize ratings across managers."
---

# Process Step: Performance & Compensation Review

## Executive Summary
Executes the annual or bi-annual performance evaluation cycle, calibrates ratings, and applies merit increases or promotions.

## 1. Strategic Intent & Outcome (Tier 1 - Executive Level)
- **Business Value**: Drives talent retention, rewards high performers, and aligns compensation with market rates.
- **Risk Exposure**: Unfair evaluations, budget overruns on merit pools, or attrition of top talent.

## 2. Operational Workflow (Tier 2)
- Employee and manager complete self and manager evaluations.
- HRBP facilitates calibration sessions to normalize ratings.
- Compensation analyst distributes merit budget pools.
- Managers allocate merit and bonuses; HR approves final payout files.
