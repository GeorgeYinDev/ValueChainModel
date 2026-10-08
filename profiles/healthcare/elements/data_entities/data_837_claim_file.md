---
id: data_837_claim_file
type: data_entity
name: "HIPAA ANSI X12N 837 Electronic Healthcare Claim"
version: "1.0.0"
lifecycles: ["RCM"]
lod_support: ["tier_2", "tier_3"]
tags: ["data", "claims", "edi837", "rcm", "billing", "healthcare"]

data_entity_details:
  system_of_record: "asset_rcm_clearinghouse"
  owner: "role_rcm_director"

graph_relations:
  - relation: triggers
    target: rcm_003_payer_adjudication_remittance
    weight: 1.0
---

# Data Entity: HIPAA ANSI X12N 837 Electronic Healthcare Claim

The electronic transaction file (837I for Institutional / Hospital billing or 837P for Professional billing) transmitting diagnosis codes, procedure codes, billed charges, and clinical service details to third-party payers.
