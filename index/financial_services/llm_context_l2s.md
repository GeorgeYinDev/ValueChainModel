# System Prompt: LLM Context Blueprint for Business Lifecycle [Loan to Settlement]

> Profile: `financial_services` | Lifecycle ID: `L2S` | Version: `1.0.0` | Source Layer: `financial_services`
> Description: Commercial and retail loan origination, credit risk underwriting, collateral perfection, core facility funding, ongoing covenant servicing, and subledger-to-GL reconciliation.

## Milestone Process Sequence
- **Step 1**: `l2s_001_loan_application_credit_packaging` (Loan Application & Credit Packaging)
- **Step 2**: `l2s_002_credit_underwriting_risk_rating` (Credit Underwriting & PD/LGD Risk Rating)
- **Step 3**: `l2s_003_collateral_valuation_lien_perfection` (Collateral Valuation & Lien Perfection)
- **Step 4**: `l2s_004_loan_booking_funding_disbursement` (Loan Booking & Principal Funding Disbursement)
- **Step 5**: `l2s_005_repayment_servicing_covenant_monitoring` (Repayment Servicing & Covenant Monitoring)
- **Step 6**: `l2s_006_delinquency_workout_ledger_settlement` (Delinquency Workout & Subledger Reconciliation)

## Key Performance Indicators (KPIs)
- `Non-Performing Loan (NPL) Ratio`
- `Net Interest Margin (NIM)`
- `Credit Application-to-Funding Cycle Time`
- `Covenant Review On-Time Completion Rate`

## Active Value Chain Elements Knowledge Base

### [Basel III Credit Risk Underwriting, Concentration & CECL Policy] (`basel_credit_risk_underwriting_policy`) [Layer: `financial_services`]
- **Type**: `control_policy` | **Tags**: `policy, basel_iii, credit_risk, cecl, dscr, ltv, lending`
- **RACI**: `{"responsible": ["role_credit_underwriter", "role_loan_servicing_specialist"], "accountable": ["role_chief_credit_officer"], "consulted": ["role_finance_controller"], "informed": ["role_internal_auditor"]}`
- **Assets**: `asset_loan_origination_system, asset_core_banking_platform`

# Control Policy: Basel III Credit Risk Underwriting, Concentration & CECL Policy

## Executive Summary
Establishes prudential credit underwriting standards, quantitative risk-rating governance, collateral valuation requirements, and ASC 326 Current Expected Credit Loss (CECL) provisioning rules across the commercial and retail lending portfolio.

## 1. Governance Rules & Controls (Tier 1)
- **Segregation of Origination & Credit Approval**: Front-office Relationship Managers (`role_relationship_manager`) are strictly prohibited from approving credit risk ratings, underwriting memos, or collateral exceptions.
- **Minimum Underwriting Metrics**: Commercial facilities require a minimum Debt Service Coverage Ratio (DSCR) of 1.25x and maximum Senior Leverage of 3.50x unless an explicit Credit Committee policy exception is approved by `role_chief_credit_officer`.
- **Collateral & Lien Perfection Prerequisite**: Facilities exceeding $250,000 USD require an independent FIRREA appraisal confirming LTV within asset-class caps (<= 75% commercial real estate; <= 80% equipment) and perfected UCC-1 or mortgage recording prior to funding release (`l2s_004`).
- **ASC 326 CECL & Non-Accrual Governance**: Loans past due >= 90 days must be placed on non-accrual status unless both well-secured and in the process of collection, with life-of-loan expected credit losses posted to `r2r_001_journal_entry_recording`.
---

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

### [Executed Commercial Credit Agreement & Perfected Lien Package] (`data_credit_facility_agreement`) [Layer: `financial_services`]
- **Type**: `data_entity` | **Tags**: `data, credit_agreement, promissory_note, ucc, l2s, banking`
- **RACI**: `{}`
- **Assets**: ``

# Data Entity: Executed Commercial Credit Agreement & Perfected Lien Package

Authoritative legal and credit artifact bundle containing the approved Credit Approval Memorandum (CAM), countersigned Credit Agreement, Promissory Note, FIRREA collateral appraisal, and recorded UCC-1 financing statement or mortgage lien required to authorize loan boarding and principal disbursement.
---

### [Net Interest Margin (NIM)] (`kpi_net_interest_margin`) [Layer: `financial_services`]
- **Type**: `kpi_metric` | **Tags**: `kpi, l2s, nim, profitability, treasury, banking`
- **RACI**: `{}`
- **Assets**: ``

# KPI: Net Interest Margin (NIM)

Measures net yield on interest-earning assets by comparing interest income generated by commercial and retail credit facilities (`L2S`) against interest expense paid on demand deposits (`C2A`) and wholesale funding.
---

### [Non-Performing Loan (NPL) Ratio] (`kpi_non_performing_loan_ratio`) [Layer: `financial_services`]
- **Type**: `kpi_metric` | **Tags**: `kpi, l2s, npl, credit_risk, delinquency, banking`
- **RACI**: `{}`
- **Assets**: ``

# KPI: Non-Performing Loan (NPL) Ratio

Measures credit portfolio asset quality as the percentage of gross commercial and retail loans that are in default, on non-accrual status, or >= 90 days past due on scheduled principal or interest payments.
---

### [Loan Application & Credit Packaging] (`l2s_001_loan_application_credit_packaging`) [Layer: `financial_services`]
- **Type**: `process_step` | **Tags**: `loan_origination, credit_memo, spreading, lending, l2s`
- **RACI**: `{"responsible": ["role_relationship_manager"], "accountable": ["role_credit_underwriter"], "consulted": ["role_customer"], "informed": ["role_chief_credit_officer"]}`
- **Assets**: `asset_crm_system, asset_loan_origination_system`

# Loan Application & Credit Packaging

Structures the commercial or retail credit facility request, ingests three years of audited borrower financial statements and tax returns into the Loan Origination System, performs standardized financial statement spreading, and assembles the preliminary Credit Approval Memorandum (CAM).
---

### [Credit Underwriting & PD/LGD Risk Rating] (`l2s_002_credit_underwriting_risk_rating`) [Layer: `financial_services`]
- **Type**: `process_step` | **Tags**: `underwriting, pd_lgd, dscr, credit_committee, basel, l2s`
- **RACI**: `{"responsible": ["role_credit_underwriter"], "accountable": ["role_chief_credit_officer"], "consulted": ["role_relationship_manager", "role_credit_manager"], "informed": ["role_customer"]}`
- **Assets**: `asset_loan_origination_system`

# Credit Underwriting & PD/LGD Risk Rating

Executes quantitative credit risk modeling to assign Basel III Probability of Default (PD) and Loss Given Default (LGD) grades, evaluates historical and projected Debt Service Coverage Ratio (DSCR >= 1.25x) and leverage limits, verifies Single Obligor concentration compliance, and secures Credit Committee adjudication.
---

### [Collateral Valuation & Lien Perfection] (`l2s_003_collateral_valuation_lien_perfection`) [Layer: `financial_services`]
- **Type**: `process_step` | **Tags**: `collateral, appraisal, ltv, ucc, closing, l2s`
- **RACI**: `{"responsible": ["role_loan_servicing_specialist"], "accountable": ["role_chief_credit_officer"], "consulted": ["role_credit_underwriter", "role_customer"], "informed": ["role_treasury_operations_officer"]}`
- **Assets**: `asset_loan_origination_system`

# Collateral Valuation & Lien Perfection

Validates independent FIRREA-compliant real estate or equipment appraisals, confirms Loan-to-Value (LTV) policy thresholds, executes UCC-1 financing statement filings or first-priority mortgage recordings, and completes legal closing of the Credit Agreement and Promissory Note.
---

### [Loan Booking & Principal Funding Disbursement] (`l2s_004_loan_booking_funding_disbursement`) [Layer: `financial_services`]
- **Type**: `process_step` | **Tags**: `loan_booking, funding, fedwire, disbursement, core_banking, l2s`
- **RACI**: `{"responsible": ["role_loan_servicing_specialist"], "accountable": ["role_treasury_operations_officer"], "consulted": ["role_credit_underwriter"], "informed": ["role_relationship_manager", "role_customer"]}`
- **Assets**: `asset_core_banking_platform, asset_payment_gateway`

# Loan Booking & Principal Funding Disbursement

Boards the executed credit facility, commitment limits, SOFR margin schedules, and fee amortization rules onto the Core Banking Platform, verifies intraday treasury liquidity, and releases principal funding via Fedwire or ACH under dual-officer settlement authorization.
---

### [Repayment Servicing & Covenant Monitoring] (`l2s_005_repayment_servicing_covenant_monitoring`) [Layer: `financial_services`]
- **Type**: `process_step` | **Tags**: `servicing, covenants, cecl, interest_accrual, payments, l2s`
- **RACI**: `{"responsible": ["role_loan_servicing_specialist", "role_credit_underwriter"], "accountable": ["role_chief_credit_officer"], "consulted": ["role_relationship_manager"], "informed": ["role_finance_controller", "role_customer"]}`
- **Assets**: `asset_core_banking_platform, asset_loan_origination_system`

# Repayment Servicing & Covenant Monitoring

Processes daily interest accruals, SOFR rate resets, and scheduled Principal & Interest (P&I) collections, tracks quarterly borrower financial covenant compliance certificates, and updates ASC 326 Current Expected Credit Loss (CECL) reserve classifications.
---

### [Delinquency Workout & Subledger Reconciliation] (`l2s_006_delinquency_workout_ledger_settlement`) [Layer: `financial_services`]
- **Type**: `process_step` | **Tags**: `workout, delinquency, subledger, reconciliation, r2r, l2s`
- **RACI**: `{"responsible": ["role_loan_servicing_specialist"], "accountable": ["role_finance_controller"], "consulted": ["role_chief_credit_officer", "role_treasury_operations_officer"], "informed": ["role_general_ledger_accountant", "role_internal_auditor"]}`
- **Assets**: `asset_core_banking_platform, asset_erp_system`

# Delinquency Workout & Subledger Reconciliation

Manages past-due borrower collections, executes Special Assets workout restructurings or non-accrual transfers, releases perfected collateral liens upon facility payoff, and reconciles daily loan/deposit subledger balances (interest income, fee amortization, principal settlements, and CECL provisions) into the corporate General Ledger.
---

### [Commercial Loan Origination, Underwriting & Servicing Value Stream] (`commercial_lending_servicing_stream`) [Layer: `financial_services`]
- **Type**: `value_stream` | **Tags**: `value_stream, lending, underwriting, servicing, credit_risk, l2s`
- **RACI**: `{"responsible": ["role_credit_underwriter", "role_loan_servicing_specialist"], "accountable": ["role_chief_credit_officer"], "consulted": ["role_relationship_manager", "role_treasury_operations_officer"], "informed": ["role_finance_controller"]}`
- **Assets**: `asset_loan_origination_system, asset_core_banking_platform, asset_payment_gateway, asset_erp_system`

# Value Stream: Commercial Loan Origination, Underwriting & Servicing (L2S)

## Executive Summary
Governs the lifecycle of commercial and retail credit facilities from initial application and financial spreading, through quantitative PD/LGD underwriting, independent collateral appraisal and UCC/mortgage lien perfection, core banking booking and Fedwire funding, ongoing covenant monitoring, and daily subledger-to-General-Ledger settlement.

## 1. Strategic Outcomes (Tier 1 - Executive Level)
- **Prudent Credit Risk & Capital Discipline**: Maintain Non-Performing Loan (NPL) ratios <= 1.25% and enforce Basel III risk-weighted asset (RWA) underwriting guardrails.
- **Perfected Collateral Protection**: Require verified LTV coverage and perfected first-priority liens before treasury principal disbursement.
- **Automated Subledger Integrity**: Reconcile interest accruals, fee recognition, principal repayments, and ASC 326 CECL credit loss provisions directly into `R2R`.

## 2. Included Steps & RACI Summary (Tier 2 - Process Architect Level)
1. `l2s_001_loan_application_credit_packaging` - Loan Application & Credit Packaging
2. `l2s_002_credit_underwriting_risk_rating` - Credit Underwriting & PD/LGD Risk Rating
3. `l2s_003_collateral_valuation_lien_perfection` - Collateral Valuation & Lien Perfection
4. `l2s_004_loan_booking_funding_disbursement` - Loan Booking & Principal Funding Disbursement
5. `l2s_005_repayment_servicing_covenant_monitoring` - Repayment Servicing & Covenant Monitoring
6. `l2s_006_delinquency_workout_ledger_settlement` - Delinquency Workout & Subledger Reconciliation

## 3. Systems Architecture (Tier 3 - Systems Engineer Level)
- **Credit Origination & Risk Platform**: `asset_loan_origination_system`
- **Loan Subledger & Treasury Rails**: `asset_core_banking_platform`, `asset_payment_gateway`
---

