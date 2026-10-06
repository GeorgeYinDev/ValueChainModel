---
id: l2c_002_proposal_development
type: process_step
name: Proposal Development & Scoping
version: 1.0.0
lifecycles: [L2C]
lod_support: [tier_1, tier_2]
tags: [presales, proposal, estimation]

raci:
  responsible: [role_solution_architect]
  accountable: [role_practice_director]
  consulted: [role_engagement_manager]
  informed: [role_customer]

attributes:
  baseline_cycle_time_hours: 40.0
  baseline_cost_per_unit: 1500.0
  automation_rate: 0.10
  error_rate: 0.05

asset_dependencies:
  - asset_crm_system

graph_relations:
  - relation: feeds_into
    target: l2c_003_contract_negotiation
    weight: 1.0
---
# Proposal Development & Scoping
The process of capturing client requirements, estimating effort, defining timelines, and generating the Statement of Work (SOW).
