---
id: e2c_004_time_expense_entry
type: process_step
name: Time & Expense Logging
version: 1.0.0
lifecycles: [E2C]
lod_support: [tier_1, tier_2]
tags: [timesheets, psa, compliance]

raci:
  responsible: [role_consultant]
  accountable: [role_engagement_manager]
  consulted: [role_billing_specialist]
  informed: [role_practice_director]

attributes:
  baseline_cycle_time_hours: 2.0
  baseline_cost_per_unit: 100.0
  automation_rate: 0.60
  error_rate: 0.05

asset_dependencies:
  - asset_psa_system

graph_relations:
  - relation: feeds_into
    target: e2c_005_client_acceptance
    weight: 1.0
---
# Time & Expense Logging
Consultants submit weekly timesheets and expense reports against specific project WBS codes for approval and capitalization.
