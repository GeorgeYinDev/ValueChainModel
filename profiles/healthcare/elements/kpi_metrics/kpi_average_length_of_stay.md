---
id: kpi_average_length_of_stay
type: kpi_metric
name: "Average Length of Stay (ALOS)"
version: "1.0.0"
lifecycles: ["P2D"]
lod_support: ["tier_1", "tier_2"]
tags: ["kpi", "clinical", "inpatient", "utilization", "healthcare"]

kpi_metric_details:
  formula: "Total Inpatient Bed Days / Total Inpatient Discharges"
  target: "<= 4.2 days"
  owner: "role_attending_physician"
  unit: "Days"

graph_relations:
  - relation: impacted_by
    target: p2d_005_discharge_planning_transition
    weight: 1.0
---

# KPI: Average Length of Stay (ALOS)

Measures inpatient bed utilization and operational throughput from initial clinical admission to definitive discharge disposition.
