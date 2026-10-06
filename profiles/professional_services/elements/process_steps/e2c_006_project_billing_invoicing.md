---
id: e2c_006_project_billing_invoicing
type: process_step
name: Project Billing & Invoicing
version: 1.0.0
lifecycles: [E2C]
lod_support: [tier_1, tier_2, tier_3]
tags: [billing, revenue, finance]

raci:
  responsible: [role_billing_specialist]
  accountable: [role_finance_controller]
  consulted: [role_engagement_manager]
  informed: [role_customer]

attributes:
  baseline_cycle_time_hours: 8.0
  baseline_cost_per_unit: 150.0
  automation_rate: 0.70
  error_rate: 0.05

asset_dependencies:
  - asset_psa_system
  - asset_erp_system

graph_relations:
  - relation: feeds_into
    target: e2c_007_project_closure_lessons
    weight: 1.0
  - relation: feeds_into
    target: r2r_001_journal_entry_recording
    weight: 1.0
  - relation: governed_by
    target: time_expense_compliance_policy
    weight: 1.0
---
# Project Billing & Invoicing
Generation of client invoices based on T&M actuals or fixed-fee milestones, posting receivables to the general ledger.
