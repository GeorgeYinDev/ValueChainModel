---
id: client_onboarding_kyc_stream
type: value_stream
name: Institutional Client Onboarding & KYC/AML Compliance Value Stream
version: 1.0.0
lifecycles: [C2A]
lod_support: [tier_1, tier_2, tier_3]
tags: [value_stream, onboarding, kyc, aml, banking, c2a]

raci:
  responsible: [role_relationship_manager, role_kyc_aml_analyst]
  accountable: [role_bsa_compliance_officer]
  consulted: [role_customer]
  informed: [role_treasury_operations_officer]

daci:
  driver: [role_kyc_aml_analyst]
  approver: [role_bsa_compliance_officer]
  contributor: [role_relationship_manager]
  informed: [role_treasury_operations_officer]

attributes:
  baseline_cycle_time_hours: 31.0
  baseline_cost_per_unit: 910.0
  automation_rate: 0.68
  error_rate: 0.03
  sla_hours: 72.0

asset_dependencies:
  - asset_crm_system
  - asset_aml_kyc_screening_engine
  - asset_core_banking_platform

graph_relations:
  - relation: governed_by
    target: bsa_aml_kyc_compliance_policy
    weight: 1.0
  - relation: feeds_into
    target: commercial_lending_servicing_stream
    weight: 1.0
---

# Value Stream: Institutional Client Onboarding & KYC/AML Compliance (C2A)

## Executive Summary
Orchestrates the end-to-end commercial and retail banking client onboarding journey—from front-office prospect application capture and tax residency certification, through CIP identity verification, UBO hierarchy resolution, OFAC/PEP screening, and Enhanced Due Diligence (EDD), culminating in core deposit account provisioning.

## 1. Strategic Outcomes (Tier 1 - Executive Level)
- **Zero Regulatory & Sanctions Breaches**: Enforce 100% USA PATRIOT Act CIP, FinCEN 25% Beneficial Ownership, and OFAC strict-liability screening prior to account activation.
- **Accelerated Client Time-to-Yes**: Compress institutional KYC onboarding cycle times while preserving full auditability.
- **Seamless Lending Readiness**: Establish a verified master Customer Information File (CIF) that directly enables commercial credit origination (`L2S`).

## 2. Included Steps & RACI Summary (Tier 2 - Process Architect Level)
1. `c2a_001_prospect_application_intake` - Prospect Application & Entity Intake
2. `c2a_002_kyc_cip_identity_verification` - KYC/CIP Identity & UBO Verification
3. `c2a_003_aml_sanctions_pep_screening` - AML Sanctions, PEP & Adverse Media Screening
4. `c2a_004_enhanced_due_diligence_compliance` - Enhanced Due Diligence (EDD) & BSA Approval
5. `c2a_005_account_provisioning_core_activation` - Core Account Provisioning & Treasury Activation

## 3. Systems Architecture (Tier 3 - Systems Engineer Level)
- **Financial Crime & CLM Backbone**: `asset_aml_kyc_screening_engine`
- **Core Account Ledger**: `asset_core_banking_platform`
