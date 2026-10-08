---
id: data_electronic_health_record
type: data_entity
name: "Longitudinal Electronic Health Record (EHR / FHIR)"
version: "1.0.0"
lifecycles: ["P2D"]
lod_support: ["tier_2", "tier_3"]
tags: ["data", "ehr", "clinical", "chart", "fhir", "healthcare"]

data_entity_details:
  system_of_record: "asset_ehr_system"
  owner: "role_attending_physician"

graph_relations:
  - relation: triggers
    target: p2d_005_discharge_planning_transition
    weight: 1.0
---

# Data Entity: Longitudinal Electronic Health Record (EHR / FHIR)

The clinical source of truth containing patient demographic profile, encounter documentation, provider orders, lab results, medication history, and discharge instructions.
