---
id: data_credit_facility_agreement
type: data_entity
name: "Executed Commercial Credit Agreement & Perfected Lien Package"
version: "1.0.0"
lifecycles: ["L2S"]
lod_support: ["tier_2", "tier_3"]
tags: ["data", "credit_agreement", "promissory_note", "ucc", "l2s", "banking"]

data_entity_details:
  system_of_record: "asset_loan_origination_system"
  owner: "role_chief_credit_officer"

graph_relations:
  - relation: triggers
    target: l2s_004_loan_booking_funding_disbursement
    weight: 1.0
---

# Data Entity: Executed Commercial Credit Agreement & Perfected Lien Package

Authoritative legal and credit artifact bundle containing the approved Credit Approval Memorandum (CAM), countersigned Credit Agreement, Promissory Note, FIRREA collateral appraisal, and recorded UCC-1 financing statement or mortgage lien required to authorize loan boarding and principal disbursement.
