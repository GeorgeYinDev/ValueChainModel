---
id: data_consultant_timesheet
type: data_entity
name: "Consultant Time & Expense Record"
version: "1.0.0"
lifecycles: ["E2C"]
lod_support: ["tier_2", "tier_3"]
tags: ["data", "timesheet", "psa", "billing", "labor"]

data_entity_details:
  system_of_record: "asset_psa_system"
  owner: "role_engagement_manager"

graph_relations:
  - relation: triggers
    target: e2c_006_project_billing_invoicing
    weight: 1.0
---

# Data Entity: Consultant Time & Expense Record

The operational unit of delivery effort and project expenditure. Captures daily consultant billable and non-billable hours booked to project WBS work breakdown codes alongside reimbursable client expenses.
