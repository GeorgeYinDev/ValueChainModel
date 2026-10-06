---
id: kpi_project_gross_margin
type: kpi_metric
name: "Project Gross Margin Percentage"
version: "1.0.0"
lifecycles: ["E2C"]
lod_support: ["tier_1", "tier_2"]
tags: ["kpi", "margin", "profitability", "finance", "consulting"]

kpi_metric_details:
  formula: "((Recognized Engagement Revenue - Direct Labor and Expense Costs) / Recognized Engagement Revenue) * 100"
  target: ">= 45.0%"
  owner: "role_engagement_manager"
  unit: "Percentage"

graph_relations:
  - relation: impacted_by
    target: e2c_006_project_billing_invoicing
    weight: 1.0
---

# KPI: Project Gross Margin Percentage

Measures profitability of delivery engagements after deducting consultant labor rates and direct project expenses from invoiced revenue.
