---
id: clinical_prior_auth_medical_necessity_policy
type: control_policy
name: Medical Necessity & Prior Authorization Governance Policy
version: 1.0.0
lifecycles: [P2D, RCM]
lod_support: [tier_1, tier_2, tier_3]
tags: [policy, prior_auth, medical_necessity, rcm, healthcare]

raci:
  responsible: [role_patient_access_specialist, role_medical_coder]
  accountable: [role_rcm_director]
  consulted: [role_attending_physician]
  informed: [role_compliance_officer]

daci:
  driver: [role_patient_access_specialist]
  approver: [role_rcm_director]
  contributor: [role_attending_physician]
  informed: [role_compliance_officer]

attributes:
  baseline_cycle_time_hours: 0.0
  baseline_cost_per_unit: 0.0
  automation_rate: 1.0
  error_rate: 0.0
  sla_hours: 0.0
  approval_threshold_usd: 250000.0

asset_dependencies:
  - asset_rcm_clearinghouse
  - asset_ehr_system

graph_relations: []
---

# Control Policy: Medical Necessity & Prior Authorization Governance Policy

## Executive Summary
Defines clinical authorization guidelines, payer medical policy validation standards, and pre-service financial clearance rules to prevent retroactive payer claim denials and ensure evidence-based care approval.

## 1. Governance Rules & Controls (Tier 1)
- **Mandatory Pre-Service Clearance**: Elective inpatient admissions, surgical procedures, and high-cost advanced imaging modalities mandate documented prior authorization (EDI 278) prior to clinical order fulfillment.
- **Peer-to-Peer Clinical Review Escalation**: When commercial or Medicare Advantage payers issue an initial denial of authorization, `role_attending_physician` must conduct a peer-to-peer clinical appeal within 5 business days.
- **Non-Covered Service Financial Disclosure**: When services do not meet payer medical necessity criteria, patients must receive an Advance Beneficiary Notice of Noncoverage (ABN) or CMS-compliant financial disclosure prior to service delivery.
- **Write-Off Authorization Ceilings**: Unappealable authorization denials exceeding $50,000 USD require formal write-down approval from `role_rcm_director`.
