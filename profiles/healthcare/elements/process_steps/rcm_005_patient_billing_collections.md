---
id: rcm_005_patient_billing_collections
type: process_step
name: Patient Billing & Collections
version: 1.0.0
lifecycles: [RCM]
lod_support: [tier_1, tier_2, tier_3]
tags: [patient_billing, statements, collections, rcm]

raci:
  responsible: [role_billing_specialist]
  accountable: [role_rcm_director]
  consulted: [role_patient]
  informed: [role_compliance_officer]

daci:
  driver: [role_billing_specialist]
  approver: [role_rcm_director]
  contributor: [role_patient]
  informed: [role_compliance_officer]

attributes:
  baseline_cycle_time_hours: 48.0
  baseline_cost_per_unit: 35.0
  automation_rate: 0.75
  error_rate: 0.04

asset_dependencies:
  - asset_rcm_clearinghouse
  - asset_ehr_system

graph_relations:
  - relation: feeds_into
    target: rcm_006_cash_posting_reconciliation
    weight: 1.0
  - relation: governed_by
    target: hipaa_phi_privacy_policy
    weight: 1.0
---

# Patient Billing & Collections

Calculates adjudicated patient out-of-pocket responsibility, issues paper and digital statements, administers financial assistance / sliding-scale charity care, and collects outstanding balances.
