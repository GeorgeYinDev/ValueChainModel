---
id: l2c_001_lead_qualification
type: process_step
name: Lead Qualification & Discovery
version: 1.0.0
lifecycles: [L2C]
lod_support: [tier_1, tier_2, tier_3]
tags: [sales, pipeline, discovery]

raci:
  responsible: [role_account_executive]
  accountable: [role_practice_director]
  consulted: [role_solution_architect]
  informed: [role_sales_ops_specialist]

attributes:
  baseline_cycle_time_hours: 8.0
  baseline_cost_per_unit: 500.0
  automation_rate: 0.15
  error_rate: 0.05

asset_dependencies:
  - asset_crm_system

graph_relations:
  - relation: feeds_into
    target: l2c_002_proposal_development
    weight: 1.0
---
# Lead Qualification & Discovery
Initial engagement with a prospect to understand their business challenges, budget, and timeline to determine if there is a viable consulting opportunity.
