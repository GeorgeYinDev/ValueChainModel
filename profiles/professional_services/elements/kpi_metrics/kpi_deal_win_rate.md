---
id: kpi_deal_win_rate
type: kpi_metric
name: "Professional Services Deal Win Rate"
version: "1.0.0"
lifecycles: ["L2C"]
lod_support: ["tier_1", "tier_2"]
tags: ["kpi", "sales", "win_rate", "pipeline", "commercial"]

kpi_metric_details:
  formula: "(Won Qualified Opportunities / Total Closed Qualified Opportunities) * 100"
  target: ">= 35.0%"
  owner: "role_account_executive"
  unit: "Percentage"

graph_relations:
  - relation: impacted_by
    target: l2c_004_deal_closure_handover
    weight: 1.0
---

# KPI: Professional Services Deal Win Rate

Measures the efficiency of the commercial sales and proposal development lifecycle in converting qualified pursuits into signed statements of work.
