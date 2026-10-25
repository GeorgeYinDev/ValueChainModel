---
id: kpi_non_performing_loan_ratio
type: kpi_metric
name: "Non-Performing Loan (NPL) Ratio"
version: "1.0.0"
lifecycles: ["L2S"]
lod_support: ["tier_1", "tier_2"]
tags: ["kpi", "l2s", "npl", "credit_risk", "delinquency", "banking"]

kpi_metric_details:
  formula: "(Total Non-Accrual & >=90-Day Past-Due Loans / Total Gross Loan Portfolio) * 100"
  target: "<= 1.25%"
  owner: "role_chief_credit_officer"
  unit: "Percentage"

graph_relations:
  - relation: impacted_by
    target: l2s_002_credit_underwriting_risk_rating
    weight: 1.0
  - relation: impacted_by
    target: l2s_006_delinquency_workout_ledger_settlement
    weight: 1.0
---

# KPI: Non-Performing Loan (NPL) Ratio

Measures credit portfolio asset quality as the percentage of gross commercial and retail loans that are in default, on non-accrual status, or >= 90 days past due on scheduled principal or interest payments.
