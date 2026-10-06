---
id: e2c_001_project_kickoff
type: process_step
name: Project Kickoff & Resource Allocation
version: 1.0.0
lifecycles: [E2C]
lod_support: [tier_1, tier_2]
tags: [delivery, staffing, kickoff]

raci:
  responsible: [role_engagement_manager]
  accountable: [role_practice_director]
  consulted: [role_consultant]
  informed: [role_customer]

attributes:
  baseline_cycle_time_hours: 16.0
  baseline_cost_per_unit: 500.0
  automation_rate: 0.20
  error_rate: 0.02

asset_dependencies:
  - asset_psa_system

graph_relations:
  - relation: feeds_into
    target: e2c_002_resource_scheduling
    weight: 1.0
---
# Project Kickoff & Resource Allocation
Onboarding the project team, assigning consultants to billable tasks in the PSA system, and conducting the client kickoff meeting.
