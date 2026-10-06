---
id: l2c_004_deal_closure_handover
type: process_step
name: Deal Closure & Delivery Handover
version: 1.0.0
lifecycles: [L2C]
lod_support: [tier_1, tier_2]
tags: [sales, delivery, handover]

raci:
  responsible: [role_account_executive]
  accountable: [role_engagement_manager]
  consulted: [role_solution_architect]
  informed: [role_sales_ops_specialist]

attributes:
  baseline_cycle_time_hours: 4.0
  baseline_cost_per_unit: 200.0
  automation_rate: 0.50
  error_rate: 0.02

asset_dependencies:
  - asset_crm_system
  - asset_psa_system

graph_relations:
  - relation: feeds_into
    target: e2c_001_project_kickoff
    weight: 1.0
---
# Deal Closure & Delivery Handover
The finalized contract is signed, the opportunity is marked as 'Closed Won' in the CRM, and all project context is handed over to the delivery team.
