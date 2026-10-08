---
id: kpi_initial_denial_rate
type: kpi_metric
name: "Initial Claim Denial Rate"
version: "1.0.0"
lifecycles: ["RCM"]
lod_support: ["tier_1", "tier_2"]
tags: ["kpi", "rcm", "denials", "claims", "healthcare"]

kpi_metric_details:
  formula: "(Total Initial Claims Denied / Total Claims Submitted to Payers) * 100"
  target: "<= 5.0%"
  owner: "role_rcm_director"
  unit: "Percentage"

graph_relations:
  - relation: impacted_by
    target: rcm_004_denial_management_appeals
    weight: 1.0
---

# KPI: Initial Claim Denial Rate

Measures the percentage of submitted electronic healthcare claims that are initially denied or rejected upon first adjudication by commercial or government payers.
