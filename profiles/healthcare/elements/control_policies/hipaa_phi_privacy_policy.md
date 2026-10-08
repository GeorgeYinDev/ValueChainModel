---
id: hipaa_phi_privacy_policy
type: control_policy
name: HIPAA Security, Privacy & PHI Governance Policy
version: 1.0.0
lifecycles: [P2D, RCM]
lod_support: [tier_1, tier_2, tier_3]
tags: [policy, hipaa, phi, privacy, compliance, healthcare]

raci:
  responsible: [role_patient_access_specialist, role_triage_nurse, role_medical_coder]
  accountable: [role_compliance_officer]
  consulted: [role_rcm_director]
  informed: [role_attending_physician]

daci:
  driver: [role_patient_access_specialist]
  approver: [role_compliance_officer]
  contributor: [role_rcm_director]
  informed: [role_attending_physician]

attributes:
  baseline_cycle_time_hours: 0.0
  baseline_cost_per_unit: 0.0
  automation_rate: 1.0
  error_rate: 0.0
  sla_hours: 0.0
  approval_threshold_usd: 50000.0

asset_dependencies:
  - asset_ehr_system
  - asset_rcm_clearinghouse

graph_relations: []
---

# Control Policy: HIPAA Security, Privacy & PHI Governance Policy

## Executive Summary
Enforces regulatory compliance under the Health Insurance Portability and Accountability Act (HIPAA) Privacy and Security Rules across all patient access, clinical care documentation, and electronic revenue cycle transactions.

## 1. Governance Rules & Controls (Tier 1)
- **Minimum Necessary Standard**: Workforce members may access only the minimum protected health information (PHI) required to perform clinical duties or billing adjudication.
- **Audit Trail & Access Telemetry**: All clinical chart accesses, electronic claim queries, and diagnostic reviews are logged with immutable audit timestamps in `asset_ehr_system`.
- **Business Associate Agreement (BAA) Verification**: No electronic data exchange (EDI 837/835) may occur with third-party clearinghouses or billing partners without an active, countersigned BAA.
- **Incident Escalation**: Suspected unauthorized PHI disclosures exceeding 500 individuals mandate notification to HHS Office for Civil Rights (OCR) within 60 calendar days under direct oversight of `role_compliance_officer`.
