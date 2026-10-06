---
id: l2c_003_contract_negotiation
type: process_step
name: Contract Negotiation & Legal Review
version: 1.0.0
lifecycles: [L2C]
lod_support: [tier_1, tier_2]
tags: [legal, sales, contracting]

raci:
  responsible: [role_account_executive]
  accountable: [role_practice_director]
  consulted: [role_finance_controller]
  informed: [role_engagement_manager]

attributes:
  baseline_cycle_time_hours: 48.0
  baseline_cost_per_unit: 1200.0
  automation_rate: 0.05
  error_rate: 0.10

asset_dependencies:
  - asset_crm_system

graph_relations:
  - relation: feeds_into
    target: l2c_004_deal_closure_handover
    weight: 1.0
---
# Contract Negotiation & Legal Review
Review of MSAs, NDAs, and SOW terms and conditions between the firm's legal team and the client.
