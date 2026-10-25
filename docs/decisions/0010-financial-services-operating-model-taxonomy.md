# ADR 0010: Financial Services & Banking Operating Model Taxonomy Design

## Status
Accepted

## Context
Following the establishment of the Multi-Industry Profiles Architecture (ADR-0007), Professional Services (ADR-0008), and Healthcare Provider Operations (ADR-0009), the Enterprise Value Chain Modeling Engine requires a domain overlay for **Financial Services & Commercial/Retail Banking** (`profiles/financial_services/`).

Banking institutions operate under strict statutory and prudential supervision (Bank Secrecy Act / Anti-Money Laundering, USA PATRIOT Act Customer Identification Program, FinCEN Beneficial Ownership, OFAC Sanctions, Basel III capital adequacy, and ASC 326 CECL credit loss accounting). Their primary value streams revolve around compliant client onboarding, deposit account provisioning, credit underwriting, collateral perfection, loan servicing, and real-time subledger-to-General-Ledger reconciliation.

## Decision
We establish the Financial Services & Banking taxonomy overlay (`profiles/financial_services/`), extending `profiles/core` with two banking lifecycles (`C2A` and `L2S`), specialized banking & compliance roles, core banking IT assets, value streams, regulatory control policies, KPIs, data entities, and stress-test scenarios:

### 1. Lifecycles
- **Client to Account (`C2A` — Client Onboarding & KYC/AML)**:
  - `c2a_001_prospect_application_intake`: Institutional and retail onboarding application capture, legal entity hierarchy mapping, and FATCA/CRS tax self-certification.
  - `c2a_002_kyc_cip_identity_verification`: Customer Identification Program (CIP) documentary/non-documentary verification and FinCEN Ultimate Beneficial Ownership (UBO >= 25%) validation.
  - `c2a_003_aml_sanctions_pep_screening`: Automated OFAC/UN/EU sanctions screening, Politically Exposed Person (PEP) & adverse media checks, and dynamic Customer Risk Rating (CRR).
  - `c2a_004_enhanced_due_diligence_compliance`: Enhanced Due Diligence (EDD) investigation for high-risk clients, Source of Wealth (SoW) / Source of Funds (SoF) corroboration, and BSA/AML Compliance Officer sign-off.
  - `c2a_005_account_provisioning_core_activation`: Demand Deposit Account (DDA) and treasury master account provisioning in the Core Banking Platform, payment channel entitlement setup, and initial funding activation.
- **Loan to Settlement (`L2S` — Loan Origination & Servicing)**:
  - `l2s_001_loan_application_credit_packaging`: Credit facility application intake, audited financial statement spreading, and credit memo assembly.
  - `l2s_002_credit_underwriting_risk_rating`: Quantitative PD/LGD credit risk modeling, Debt Service Coverage Ratio (DSCR) & leverage analysis, and Credit Committee adjudication.
  - `l2s_003_collateral_valuation_lien_perfection`: Independent collateral appraisal review, Loan-to-Value (LTV) validation, UCC-1 / mortgage lien filing, and credit agreement execution.
  - `l2s_004_loan_booking_funding_disbursement`: Core banking credit facility boarding, credit limit reservation, and Fedwire/ACH principal disbursement.
  - `l2s_005_repayment_servicing_covenant_monitoring`: Automated P&I billing, floating-rate SOFR reset processing, periodic financial covenant testing, and CECL (ASC 326) expected credit loss provisioning.
  - `l2s_006_delinquency_workout_ledger_settlement`: Early delinquency collections, troubled debt restructuring (TDR) / workout execution, payoff lien release, and daily loan subledger-to-GL reconciliation.

### 2. Roles & Governance
- `role_relationship_manager`: Front-office commercial & institutional client coverage, credit origination structuring, and fee waiver authority ($100,000 USD limit).
- `role_kyc_aml_analyst`: Financial crime operations specialist executing CIP verification, UBO mapping, sanctions alert disposition, and EDD case assembly.
- `role_bsa_compliance_officer`: Statutory BSA/AML & OFAC Compliance Officer with final authority over high-risk EDD approvals, SAR filings, and regulatory freezes ($1,000,000 USD authority).
- `role_credit_underwriter`: Credit risk analyst performing financial spreading, PD/LGD rating calibration, and ongoing covenant compliance monitoring ($500,000 USD limit).
- `role_chief_credit_officer`: Executive credit authority presiding over the Credit Committee, commercial facility approvals, and workout restructurings ($25,000,000 USD approval limit).
- `role_loan_servicing_specialist`: Back-office lending operations specialist managing collateral lien filings, loan boarding, rate resets, and P&I payment application.
- `role_treasury_operations_officer`: Treasury & settlement officer responsible for liquidity verification, wire disbursement release, and subledger cash reconciliation ($5,000,000 USD limit).

### 3. IT Assets
- `asset_core_banking_platform`: Core Banking & Subledger Engine (e.g., Temenos Transact, FIS Modern Banking Platform) managing deposit accounts, loan subledgers, interest accruals, and payment rails.
- `asset_aml_kyc_screening_engine`: Financial Crime, KYC CLM & Sanctions Screening Platform (e.g., Nice Actimize, Fenergo, LexisNexis Bridger) automating identity verification, UBO graphs, and real-time OFAC/PEP screening.
- `asset_loan_origination_system`: Commercial Loan Origination & Risk Rating Platform (e.g., nCino, Moody's CreditLens) supporting financial spreading, PD/LGD models, collateral tracking, and credit committee workflows.

### 4. Integration with Core Financial Triad
- `c2a_005_account_provisioning_core_activation` feeds directly into `l2s_001_loan_application_credit_packaging`, ensuring no credit facility is originated without an active, KYC-cleared master client profile.
- `l2s_006_delinquency_workout_ledger_settlement` feeds directly into `r2r_001_journal_entry_recording` in the core Record-to-Report ledger for automated posting of interest income, fee recognition, principal settlements, and CECL allowance adjustments.
- Inherited `s2p_004_contracting_sla_negotiation` patches into `l2s_003_collateral_valuation_lien_perfection` to govern third-party appraisal and legal panel vendor onboarding.

## Consequences
- Extends the multi-industry architecture to support commercial, institutional, and retail banking operating models alongside manufacturing, professional services, and healthcare.
- Enforces strict Segregation of Duties (SoD) between front-office origination (`role_relationship_manager`), independent credit/compliance risk (`role_chief_credit_officer`, `role_bsa_compliance_officer`), and back-office treasury settlement (`role_treasury_operations_officer`).
