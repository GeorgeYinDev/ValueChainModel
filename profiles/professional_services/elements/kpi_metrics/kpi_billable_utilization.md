---
id: kpi_billable_utilization
type: kpi_metric
name: "Billable Consultant Utilization Rate"
version: "1.0.0"
lifecycles: ["E2C"]
lod_support: ["tier_1", "tier_2"]
tags: ["kpi", "utilization", "capacity", "consulting", "psa"]

kpi_metric_details:
  formula: "(Total Billable Hours Delivered / Total Available Standard Working Hours) * 100"
  target: ">= 78.5%"
  owner: "role_practice_director"
  unit: "Percentage"

graph_relations:
  - relation: impacted_by
    target: e2c_004_time_expense_entry
    weight: 1.0
---

# KPI: Billable Consultant Utilization Rate

Measures the proportion of available consultant working hours billed to client engagements versus administrative, bench, or internal time. Vital operational health metric tracked within the PSA platform.
