# System Prompt: LLM Context Blueprint for Business Lifecycle [Client to Account]

> Profile: `financial_services` | Lifecycle ID: `C2A` | Version: `1.0.0` | Source Layer: `financial_services`
> Description: End-to-end banking client onboarding, Customer Identification Program (CIP), Beneficial Ownership (UBO), OFAC/PEP sanctions screening, Enhanced Due Diligence (EDD), and core account provisioning.

## Milestone Process Sequence
- **Step 1**: `c2a_001_prospect_application_intake` (Prospect Application & Entity Intake)
- **Step 2**: `c2a_002_kyc_cip_identity_verification` (KYC/CIP Identity & UBO Verification)
- **Step 3**: `c2a_003_aml_sanctions_pep_screening` (AML Sanctions, PEP & Adverse Media Screening)
- **Step 4**: `c2a_004_enhanced_due_diligence_compliance` (Enhanced Due Diligence (EDD) & BSA Approval)
- **Step 5**: `c2a_005_account_provisioning_core_activation` (Core Account Provisioning & Treasury Activation)

## Key Performance Indicators (KPIs)
- `KYC Onboarding Time-to-Yes (Hours)`
- `First-Time-Right KYC Documentation Rate`
- `Sanctions Alert False-Positive Rate`
- `EDD SLA Compliance Rate`

## Active Value Chain Elements Knowledge Base

### [BSA/AML, USA PATRIOT Act CIP & OFAC Sanctions Governance Policy] (`bsa_aml_kyc_compliance_policy`) [Layer: `financial_services`]
- **Type**: `control_policy` | **Tags**: `policy, bsa, aml, kyc, ofac, fincen, banking`
- **RACI**: `{"responsible": ["role_kyc_aml_analyst", "role_relationship_manager"], "accountable": ["role_bsa_compliance_officer"], "consulted": ["role_internal_auditor"], "informed": ["role_chief_credit_officer"]}`
- **Assets**: `asset_aml_kyc_screening_engine, asset_core_banking_platform`

# Control Policy: BSA/AML, USA PATRIOT Act CIP & OFAC Sanctions Governance Policy

## Executive Summary
Enforces statutory compliance under the Bank Secrecy Act (BSA), USA PATRIOT Act Section 326 Customer Identification Program (CIP), FinCEN Customer Due Diligence (CDD) Beneficial Ownership Rule, and Office of Foreign Assets Control (OFAC) strict-liability sanctions regimes across all client onboarding and funding workflows.

## 1. Governance Rules & Controls (Tier 1)
- **Mandatory CIP & 25% UBO Identification**: No deposit account or credit facility may be activated in `asset_core_banking_platform` without verified identity documentation for the legal entity, all natural persons owning >= 25% equity, and one controlling executive officer.
- **OFAC Strict-Liability Screening Gate**: Real-time sanctions screening must execute at onboarding (`c2a_003`) and prior to every outbound wire disbursement (`l2s_004`). Confirmed positive matches trigger an immediate system block and OFAC compliance hold.
- **Enhanced Due Diligence (EDD) Escalation**: Politically Exposed Persons (PEPs), high-risk FATF jurisdictions, and entities with complex offshore ownership require documented Source of Wealth (SoW) corroboration and explicit sign-off by `role_bsa_compliance_officer`.
- **SAR Filing & Confidentiality Mandate**: Suspicious transactions >= $5,000 USD involving potential money laundering or BSA violations require Suspicious Activity Report (SAR) filing with FinCEN within 30 calendar days.
---

### [Verified KYC/CDD & Beneficial Ownership Compliance Dossier] (`data_kyc_cdd_dossier`) [Layer: `financial_services`]
- **Type**: `data_entity` | **Tags**: `data, kyc, cdd, ubo, c2a, banking`
- **RACI**: `{}`
- **Assets**: ``

# Data Entity: Verified KYC/CDD & Beneficial Ownership Compliance Dossier

Immutable regulatory compliance record containing verified Customer Identification Program (CIP) evidence, FinCEN Ultimate Beneficial Ownership (UBO >= 25%) hierarchy attestations, OFAC/PEP screening dispositions, Customer Risk Rating (CRR) scorecards, and BSA Officer EDD sign-off.
---

### [KYC Client Onboarding Time-to-Yes] (`kpi_kyc_onboarding_time_to_yes`) [Layer: `financial_services`]
- **Type**: `kpi_metric` | **Tags**: `kpi, c2a, kyc, onboarding, cycle_time, banking`
- **RACI**: `{}`
- **Assets**: ``

# KPI: KYC Client Onboarding Time-to-Yes

Measures the average elapsed cycle time from initial institutional or retail client application intake (`c2a_001`) through CIP/UBO verification, sanctions clearance, and Enhanced Due Diligence to active core deposit account provisioning (`c2a_005`).
---

### [Prospect Application & Entity Intake] (`c2a_001_prospect_application_intake`) [Layer: `financial_services`]
- **Type**: `process_step` | **Tags**: `onboarding, intake, fatca, crs, banking, c2a`
- **RACI**: `{"responsible": ["role_relationship_manager"], "accountable": ["role_bsa_compliance_officer"], "consulted": ["role_customer"], "informed": ["role_kyc_aml_analyst"]}`
- **Assets**: `asset_crm_system, asset_aml_kyc_screening_engine`

# Prospect Application & Entity Intake

Captures institutional and retail banking onboarding applications, legal entity formation documents, corporate ownership hierarchy charts, anticipated transaction volumes, and FATCA (W-9 / W-8BEN-E) & CRS tax residency self-certifications.
---

### [KYC/CIP Identity & UBO Verification] (`c2a_002_kyc_cip_identity_verification`) [Layer: `financial_services`]
- **Type**: `process_step` | **Tags**: `kyc, cip, ubo, identity_verification, fincen, c2a`
- **RACI**: `{"responsible": ["role_kyc_aml_analyst"], "accountable": ["role_bsa_compliance_officer"], "consulted": ["role_relationship_manager", "role_customer"], "informed": ["role_treasury_operations_officer"]}`
- **Assets**: `asset_aml_kyc_screening_engine`

# KYC/CIP Identity & UBO Verification

Executes USA PATRIOT Act Section 326 Customer Identification Program (CIP) documentary and non-documentary verification, secretary-of-state registry checks, and FinCEN Customer Due Diligence (CDD) verification of all Ultimate Beneficial Owners (UBOs holding >= 25% equity) and one controlling executive officer.
---

### [AML Sanctions, PEP & Adverse Media Screening] (`c2a_003_aml_sanctions_pep_screening`) [Layer: `financial_services`]
- **Type**: `process_step` | **Tags**: `aml, ofac, sanctions, pep, adverse_media, c2a`
- **RACI**: `{"responsible": ["role_kyc_aml_analyst"], "accountable": ["role_bsa_compliance_officer"], "consulted": ["role_internal_auditor"], "informed": ["role_relationship_manager"]}`
- **Assets**: `asset_aml_kyc_screening_engine`

# AML Sanctions, PEP & Adverse Media Screening

Screens the legal entity, directors, signatories, and beneficial owners against OFAC SDN, UN, EU, and UK HM Treasury sanctions lists, Politically Exposed Person (PEP) registries, and global adverse media databases to compute a composite Customer Risk Rating (CRR).
---

### [Enhanced Due Diligence (EDD) & BSA Approval] (`c2a_004_enhanced_due_diligence_compliance`) [Layer: `financial_services`]
- **Type**: `process_step` | **Tags**: `edd, bsa, source_of_wealth, high_risk, compliance, c2a`
- **RACI**: `{"responsible": ["role_kyc_aml_analyst"], "accountable": ["role_bsa_compliance_officer"], "consulted": ["role_relationship_manager"], "informed": ["role_internal_auditor"]}`
- **Assets**: `asset_aml_kyc_screening_engine`

# Enhanced Due Diligence (EDD) & BSA Approval

Conducts deep-dive Enhanced Due Diligence (EDD) for high-risk jurisdictions, PEPs, cash-intensive businesses, and complex offshore structures, corroborating independent Source of Wealth (SoW) and Source of Funds (SoF) evidence prior to formal BSA/AML Compliance Officer sign-off.
---

### [Core Account Provisioning & Treasury Activation] (`c2a_005_account_provisioning_core_activation`) [Layer: `financial_services`]
- **Type**: `process_step` | **Tags**: `account_opening, core_banking, dda, treasury, activation, c2a`
- **RACI**: `{"responsible": ["role_loan_servicing_specialist"], "accountable": ["role_treasury_operations_officer"], "consulted": ["role_kyc_aml_analyst"], "informed": ["role_relationship_manager", "role_customer"]}`
- **Assets**: `asset_core_banking_platform, asset_payment_gateway`

# Core Account Provisioning & Treasury Activation

Provisions Customer Information Files (CIF), Demand Deposit Accounts (DDA), and commercial treasury sweep structures in the Core Banking Platform, configures dual-control wire/ACH payment entitlements, and activates transaction monitoring profiles upon initial funding clearance.
---

### [Institutional Client Onboarding & KYC/AML Compliance Value Stream] (`client_onboarding_kyc_stream`) [Layer: `financial_services`]
- **Type**: `value_stream` | **Tags**: `value_stream, onboarding, kyc, aml, banking, c2a`
- **RACI**: `{"responsible": ["role_relationship_manager", "role_kyc_aml_analyst"], "accountable": ["role_bsa_compliance_officer"], "consulted": ["role_customer"], "informed": ["role_treasury_operations_officer"]}`
- **Assets**: `asset_crm_system, asset_aml_kyc_screening_engine, asset_core_banking_platform`

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
---

