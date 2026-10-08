---
id: kpi_days_in_ar
type: kpi_metric
name: "Net Days in Accounts Receivable (A/R)"
version: "1.0.0"
lifecycles: ["RCM"]
lod_support: ["tier_1", "tier_2"]
tags: ["kpi", "rcm", "ar_days", "cash_flow", "healthcare"]

kpi_metric_details:
  formula: "(Total Net Accounts Receivable / Average Daily Net Patient Revenue)"
  target: "<= 38.0 days"
  owner: "role_rcm_director"
  unit: "Days"

graph_relations:
  - relation: impacted_by
    target: rcm_006_cash_posting_reconciliation
    weight: 1.0
---

# KPI: Net Days in Accounts Receivable (A/R)

Measures the average number of calendar days between discharge/service delivery and the final cash settlement and remittance reconciliation of patient and payer balances.
