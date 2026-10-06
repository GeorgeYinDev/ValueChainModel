---
id: e2c_002_resource_scheduling
type: process_step
name: Resource Scheduling & Allocation
version: 1.0.0
lifecycles: [E2C]
lod_support: [tier_1, tier_2]
tags: [resourcing, psa, capacity]

raci:
  responsible: [role_engagement_manager]
  accountable: [role_practice_director]
  consulted: [role_hr_business_partner]
  informed: [role_consultant]

attributes:
  baseline_cycle_time_hours: 12.0
  baseline_cost_per_unit: 800.0
  automation_rate: 0.40
  error_rate: 0.10

asset_dependencies:
  - asset_psa_system

graph_relations:
  - relation: feeds_into
    target: e2c_003_project_execution_delivery
    weight: 1.0
---
# Resource Scheduling & Allocation
Assigning specific consultants to project milestones based on skill requirements, availability, and geographic location using the PSA system.
