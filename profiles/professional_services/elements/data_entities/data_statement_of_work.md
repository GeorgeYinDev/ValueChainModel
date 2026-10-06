---
id: data_statement_of_work
type: data_entity
name: "Statement of Work (SOW) & Engagement Contract"
version: "1.0.0"
lifecycles: ["L2C", "E2C"]
lod_support: ["tier_2", "tier_3"]
tags: ["data", "sow", "contract", "legal", "commercial"]

data_entity_details:
  system_of_record: "asset_crm_system"
  owner: "role_practice_director"

graph_relations:
  - relation: triggers
    target: e2c_001_project_kickoff
    weight: 1.0
---

# Data Entity: Statement of Work (SOW) & Engagement Contract

The formal commercial agreement executed between the consulting practice and the client. Defines engagement scope, milestone deliverables, staffing rate cards, billing schedules, and liability terms.
