---
id: bsa_aml_kyc_compliance_policy
type: control_policy
name: BSA/AML, USA PATRIOT Act CIP & OFAC Sanctions Governance Policy
version: 1.0.0
lifecycles: [C2A, L2S]
lod_support: [tier_1, tier_2, tier_3]
tags: [policy, bsa, aml, kyc, ofac, fincen, banking]

raci:
  responsible: [role_kyc_aml_analyst, role_relationship_manager]
  accountable: [role_bsa_compliance_officer]
  consulted: [role_internal_auditor]
  informed: [role_chief_credit_officer]

daci:
  driver: [role_kyc_aml_analyst]
  approver: [role_bsa_compliance_officer]
  contributor: [role_internal_auditor]
  informed: [role_chief_credit_officer]

attributes:
  baseline_cycle_time_hours: 0.0
  baseline_cost_per_unit: 0.0
  automation_rate: 1.0
  error_rate: 0.0
  sla_hours: 0.0
  approval_threshold_usd: 250000.0

asset_dependencies:
  - asset_aml_kyc_screening_engine
  - asset_core_banking_platform

graph_relations: []
---

# Control Policy: BSA/AML, USA PATRIOT Act CIP & OFAC Sanctions Governance Policy

## Executive Summary
Enforces statutory compliance under the Bank Secrecy Act (BSA), USA PATRIOT Act Section 326 Customer Identification Program (CIP), FinCEN Customer Due Diligence (CDD) Beneficial Ownership Rule, and Office of Foreign Assets Control (OFAC) strict-liability sanctions regimes across all client onboarding and funding workflows.

## 1. Governance Rules & Controls (Tier 1)
- **Mandatory CIP & 25% UBO Identification**: No deposit account or credit facility may be activated in `asset_core_banking_platform` without verified identity documentation for the legal entity, all natural persons owning >= 25% equity, and one controlling executive officer.
- **OFAC Strict-Liability Screening Gate**: Real-time sanctions screening must execute at onboarding (`c2a_003`) and prior to every outbound wire disbursement (`l2s_004`). Confirmed positive matches trigger an immediate system block and OFAC compliance hold.
- **Enhanced Due Diligence (EDD) Escalation**: Politically Exposed Persons (PEPs), high-risk FATF jurisdictions, and entities with complex offshore ownership require documented Source of Wealth (SoW) corroboration and explicit sign-off by `role_bsa_compliance_officer`.
- **SAR Filing & Confidentiality Mandate**: Suspicious transactions >= $5,000 USD involving potential money laundering or BSA violations require Suspicious Activity Report (SAR) filing with FinCEN within 30 calendar days.
