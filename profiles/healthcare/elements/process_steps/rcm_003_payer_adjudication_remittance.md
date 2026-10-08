---
id: rcm_003_payer_adjudication_remittance
type: process_step
name: Payer Adjudication & Remittance
version: 1.0.0
lifecycles: [RCM]
lod_support: [tier_1, tier_2, tier_3]
tags: [adjudication, era, edi835, remittance, payer]

raci:
  responsible: [role_billing_specialist]
  accountable: [role_rcm_director]
  consulted: [role_medical_coder]
  informed: [role_finance_controller]

daci:
  driver: [role_billing_specialist]
  approver: [role_rcm_director]
  contributor: [role_medical_coder]
  informed: [role_finance_controller]

attributes:
  baseline_cycle_time_hours: 120.0
  baseline_cost_per_unit: 15.0
  automation_rate: 0.92
  error_rate: 0.06

asset_dependencies:
  - asset_rcm_clearinghouse

graph_relations:
  - relation: feeds_into
    target: rcm_004_denial_management_appeals
    weight: 1.0
  - relation: governed_by
    target: hipaa_phi_privacy_policy
    weight: 1.0
---

# Payer Adjudication & Remittance

Receives Electronic Remittance Advice (ERA / EDI 835) files from commercial health plans, Medicare Administrative Contractors (MAC), and Medicaid programs detailing allowed amounts, contractual discounts, and patient cost-shares.
