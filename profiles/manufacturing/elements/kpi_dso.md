---
id: kpi_dso
type: kpi_metric
name: "Days Sales Outstanding (DSO)"
version: "1.0.0"
lifecycles: ["O2C"]
lod_support: ["tier_1", "tier_2"]
tags: ["kpi", "receivables", "cash_flow"]

kpi_metric_details:
  formula: "(Accounts Receivable / Total Credit Sales) * Number of Days"
  target: "< 35 days"
  owner: "role_finance_controller"
  unit: "Days"

graph_relations:
  - relation: impacted_by
    target: o2c_005_cash_collection_reconciliation
    weight: 1.0
---

# KPI: Days Sales Outstanding (DSO)

Measures the average number of days that it takes a company to collect payment after a sale has been made. Critical metric for evaluating cash flow and accounts receivable efficiency in the Order-to-Cash lifecycle.
