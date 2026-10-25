---
id: data_kyc_cdd_dossier
type: data_entity
name: "Verified KYC/CDD & Beneficial Ownership Compliance Dossier"
version: "1.0.0"
lifecycles: ["C2A"]
lod_support: ["tier_2", "tier_3"]
tags: ["data", "kyc", "cdd", "ubo", "c2a", "banking"]

data_entity_details:
  system_of_record: "asset_aml_kyc_screening_engine"
  owner: "role_bsa_compliance_officer"

graph_relations:
  - relation: triggers
    target: c2a_005_account_provisioning_core_activation
    weight: 1.0
---

# Data Entity: Verified KYC/CDD & Beneficial Ownership Compliance Dossier

Immutable regulatory compliance record containing verified Customer Identification Program (CIP) evidence, FinCEN Ultimate Beneficial Ownership (UBO >= 25%) hierarchy attestations, OFAC/PEP screening dispositions, Customer Risk Rating (CRR) scorecards, and BSA Officer EDD sign-off.
