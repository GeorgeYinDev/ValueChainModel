---
id: e2c_005_client_acceptance
type: process_step
name: Client Review & Deliverable Acceptance
version: 1.0.0
lifecycles: [E2C]
lod_support: [tier_1, tier_2]
tags: [quality, acceptance, signoff]

raci:
  responsible: [role_engagement_manager]
  accountable: [role_engagement_manager]
  consulted: [role_customer]
  informed: [role_billing_specialist]

attributes:
  baseline_cycle_time_hours: 48.0
  baseline_cost_per_unit: 500.0
  automation_rate: 0.10
  error_rate: 0.20
compensating_control: "Secondary audit of client sign-off documents by Practice Director."

asset_dependencies:
  - asset_psa_system

graph_relations:
  - relation: feeds_into
    target: e2c_006_project_billing_invoicing
    weight: 1.0
---
# Client Review & Deliverable Acceptance
Formal client sign-off on completed milestones or monthly timesheets, triggering revenue recognition and billing events.
