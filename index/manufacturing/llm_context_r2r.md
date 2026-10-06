# System Prompt: LLM Context Blueprint for Business Lifecycle [Record to Report Lifecycle]

> Profile: `manufacturing` | Lifecycle ID: `R2R` | Version: `1.0.0` | Source Layer: `core`
> Description: End-to-end financial accounting and reporting lifecycle from subledger transaction ingestion and intercompany eliminations to balance sheet account reconciliation, financial close orchestration, group consolidation, and regulatory/statutory disclosures.

## Milestone Process Sequence
- **Step 1**: `r2r_001_journal_entry_recording` (General Ledger Journal Recording & Subledger Ingestion)
- **Step 2**: `r2r_002_intercompany_reconciliation` (Intercompany Transaction Matching & Elimination)
- **Step 3**: `r2r_003_balance_sheet_substantiation` (Balance Sheet Account Substantiation & Reconciliation)
- **Step 4**: `r2r_004_financial_close_consolidation` (Financial Close Orchestration & Group Consolidation)
- **Step 5**: `r2r_005_statutory_financial_reporting` (Statutory, Tax & Management Financial Reporting)

## Key Performance Indicators (KPIs)
- `days_to_close_financial_books`
- `manual_journal_entry_ratio`
- `intercompany_out_of_balance_amount`
- `first_time_right_reconciliation_rate`
- `sox_internal_control_deficiencies`

## Active Value Chain Elements Knowledge Base

### [General Ledger Journal Entry] (`data_journal_entry`) [Layer: `core`]
- **Type**: `data_entity` | **Tags**: `data, finance, ledger`
- **RACI**: `{}`
- **Assets**: ``

# Data Entity: General Ledger Journal Entry

The core transactional artifact for accounting ledgers. Contains the debits, credits, accounting date, Chart of Accounts segment string, and business justification for financial recording.
---

### [Financial Close, Consolidation & Regulatory Reporting Stream] (`financial_close_reporting_stream`) [Layer: `core`]
- **Type**: `value_stream` | **Tags**: `value_stream, record_to_report, financial_close, consolidation, r2r`
- **RACI**: `{"responsible": ["role_general_ledger_accountant", "role_consolidation_specialist"], "accountable": ["role_finance_controller"], "consulted": ["role_internal_auditor"], "informed": ["role_internal_auditor"]}`
- **Assets**: `asset_erp_system, asset_financial_consolidation_system`

# Value Stream: Record to Report (R2R)

## Executive Summary
Orchestrates the entire corporate financial accounting lifecycle, encompassing subledger transaction feeds, multi-entity intercompany eliminations, balance sheet account substantiation, group close consolidation, and certified external financial disclosures (Steps 001 - 005).

## 1. Strategic Outcomes (Tier 1 - Executive Level)
- **Accelerate Financial Close Velocity**: Compress total global close schedule to under 5 business days (120 hours).
- **Audit & Regulatory Compliance**: Ensure 100% compliance with Sarbanes-Oxley 404, US GAAP, and IFRS standards with zero material weaknesses.
- **Reporting Integrity & Accuracy**: Minimize manual adjustments and eliminate un-reconciled intercompany breaks prior to earnings release.

## 2. Included Steps & RACI Summary (Tier 2 - Process Architect Level)
1. `r2r_001_journal_entry_recording` - General Ledger Journal Recording & Subledger Ingestion
2. `r2r_002_intercompany_reconciliation` - Intercompany Transaction Matching & Elimination
3. `r2r_003_balance_sheet_substantiation` - Balance Sheet Account Substantiation & Reconciliation
4. `r2r_004_financial_close_consolidation` - Financial Close Orchestration & Group Consolidation
5. `r2r_005_statutory_financial_reporting` - Statutory, Tax & Management Financial Reporting
---

### [General Ledger Journal Recording & Subledger Ingestion] (`r2r_001_journal_entry_recording`) [Layer: `core`]
- **Type**: `process_step` | **Tags**: `journal_entry, general_ledger, subledger, ingestion, accounting`
- **RACI**: `{"responsible": ["role_general_ledger_accountant"], "accountable": ["role_finance_controller"], "consulted": ["role_accounts_payable_clerk", "role_billing_specialist"], "informed": ["role_internal_auditor"]}`
- **Assets**: `asset_erp_system`

# Process Step: General Ledger Journal Recording & Subledger Ingestion

## Executive Summary
Captures and posts daily accounting transactions into the General Ledger (GL), ingests automated feeder batches from operational subledgers (Accounts Payable from S2P and Accounts Receivable from O2C), and validates supporting documentation for non-standard manual journal vouchers.

## 1. Strategic Intent & Outcome (Tier 1 - Executive Level)
- **Business Value**: Provides the unified single source of financial truth, ensuring transaction completeness and real-time accounting visibility.
- **Strategic Alignment**: Directly underpins audit readiness, operational expense control, and fiscal closing timelines.
- **Risk Exposure**: Unrecorded liabilities, unauthorized manual journal overrides, duplicate subledger postings, or misclassified account strings.

## 2. Operational Workflow & RACI (Tier 2 - Process Architect Level)
- **Workflow Sequence**:
  1. Feeder subledgers (AP disbursements from `s2p_008`, AR billing from `o2c_004`, cash clearing from `o2c_005`, and payroll expense from `h2r_004`) transmit daily batched postings to General Ledger.
  2. ERP validation rules verify debit/credit balance equality, valid Chart of Accounts (COA) segment combinations, and open accounting fiscal periods.
  3. Operational accounting staff submit manual adjustment vouchers with attached business substantiation.
  4. Workflows automatically route manual entries exceeding materiality thresholds ($50,000 USD) to `role_finance_controller` for electronic sign-off.
  5. Validated journals commit to the GL transaction table in `asset_erp_system`.
- **RACI Assignment Matrix**:
  - **Responsible**: `role_general_ledger_accountant`
  - **Accountable**: `role_finance_controller`
  - **Consulted**: `role_accounts_payable_clerk`, `role_billing_specialist`
  - **Informed**: `role_internal_auditor`
- **Service Level Agreement (SLA)**: 16.0 Hours.

## 3. Systems Math & Simulation Parameters (Tier 3 - Simulation Engineer Level)
```math
\text{Ingestion Latency} = \text{Baseline Cycle Time} \times \left(1 + \frac{\text{Manual Journal Surge Rate}}{\text{Automated Posting Ratio}}\right)
```
- **Primary Data Entity**: General Ledger Journal Voucher (`GL_JOURNAL_ENTRY_v1`).
- **Asset Load**: Core ERP Ledger Engine (`asset_erp_system`).
---

### [Intercompany Transaction Matching & Elimination] (`r2r_002_intercompany_reconciliation`) [Layer: `core`]
- **Type**: `process_step` | **Tags**: `intercompany, elimination, matching, netting, consolidation`
- **RACI**: `{"responsible": ["role_consolidation_specialist"], "accountable": ["role_finance_controller"], "consulted": ["role_general_ledger_accountant"], "informed": ["role_internal_auditor"]}`
- **Assets**: `asset_erp_system, asset_financial_consolidation_system`

# Process Step: Intercompany Transaction Matching & Elimination

## Executive Summary
Identifies, matches, and eliminates reciprocal intercompany receivables, payables, revenues, and expenses across corporate legal entities, resolving cross-border FX discrepancies and out-of-balance transaction disputes.

## 1. Strategic Intent & Outcome (Tier 1 - Executive Level)
- **Business Value**: Eliminates artificial internal revenue inflation, guarantees consolidated balance sheet accuracy, and ensures compliance with transfer pricing tax regulations.
- **Strategic Alignment**: Directly drives the acceleration of financial close by eliminating intercompany reconciliation bottlenecks.
- **Risk Exposure**: Unbalanced intercompany balances, cross-border currency conversion friction, tax authority scrutiny, and delayed group reporting.

## 2. Operational Workflow & RACI (Tier 2 - Process Architect Level)
- **Workflow Sequence**:
  1. Automated matching engine in `asset_financial_consolidation_system` extracts intercompany AR/AP and buy/sell transaction pairs from `asset_erp_system`.
  2. Transactional matching rules identify exact invoice references and resolve allowable threshold variances (<$100 USD).
  3. Out-of-balance breaks exceeding materiality thresholds route to local entity accountants for dispute resolution.
  4. Reciprocal intercompany balances are netted and automated bilateral elimination entries are generated for corporate group roll-up.
- **RACI Assignment Matrix**:
  - **Responsible**: `role_consolidation_specialist`
  - **Accountable**: `role_finance_controller`
  - **Consulted**: `role_general_ledger_accountant`
  - **Informed**: `role_internal_auditor`
- **Service Level Agreement (SLA)**: 24.0 Hours.

## 3. Systems Math & Simulation Parameters (Tier 3 - Simulation Engineer Level)
```math
\text{Reconciliation Variance} = \sum |\text{Entity A AR} - \text{Entity B AP} \times \text{FX Spot Rate}|
```
- **Primary Data Entity**: Intercompany Matching Reconciliation Voucher (`IC_RECON_VOUCHER_v1`).
- **Asset Load**: Ingestion from `asset_erp_system` into `asset_financial_consolidation_system`.
---

### [Balance Sheet Account Substantiation & Reconciliation] (`r2r_003_balance_sheet_substantiation`) [Layer: `core`]
- **Type**: `process_step` | **Tags**: `reconciliation, balance_sheet, substantiation, blackline, audit`
- **RACI**: `{"responsible": ["role_general_ledger_accountant"], "accountable": ["role_finance_controller"], "consulted": ["role_consolidation_specialist"], "informed": ["role_internal_auditor"]}`
- **Assets**: `asset_erp_system, asset_financial_consolidation_system`

# Process Step: Balance Sheet Account Substantiation & Reconciliation

## Executive Summary
Substantiates and certifies general ledger asset, liability, and equity account balances against independent external sources (bank statements, inventory physical counts, subledger aging schedules, and debt amortizations) in compliance with SOX 404.

## 1. Strategic Intent & Outcome (Tier 1 - Executive Level)
- **Business Value**: Guarantees the integrity and auditability of the corporate balance sheet, preventing hidden write-downs, fraudulent asset misstatements, and material control deficiencies.
- **Strategic Alignment**: Core pillar of financial governance and external auditor certification under PCAOB standards.
- **Risk Exposure**: Unreconciled suspense accounts, undetected asset impairments, overstated receivables, and auditor qualification findings.

## 2. Operational Workflow & RACI (Tier 2 - Process Architect Level)
- **Workflow Sequence**:
  1. Automated reconciliation module extracts trial balance balances from `asset_erp_system` and pairs them with external data feeds.
  2. GL Accountants attach supporting schedules, third-party confirmations, and variance documentation.
  3. Reconciling items and timing differences are classified and scheduled for resolution within 30 days.
  4. Substantiation packages route to `role_finance_controller` for formal review and digital approval.
  5. Account status moves to "Substantiated and Locked" for period close.
- **RACI Assignment Matrix**:
  - **Responsible**: `role_general_ledger_accountant`
  - **Accountable**: `role_finance_controller`
  - **Consulted**: `role_consolidation_specialist`
  - **Informed**: `role_internal_auditor`
- **Service Level Agreement (SLA)**: 36.0 Hours.

## 3. Systems Math & Simulation Parameters (Tier 3 - Simulation Engineer Level)
```math
\text{Unsubstantiated Balance Exposure} = \sum_{\text{Unreconciled}} \left|\text{GL Balance} - \text{External Source Balance}\right|
```
- **Primary Data Entity**: Account Substantiation Dossier (`BALANCE_SHEET_SUBSTANTIATION_v1`).
- **Asset Load**: `asset_erp_system`, `asset_financial_consolidation_system`.
---

### [Financial Close Orchestration & Group Consolidation] (`r2r_004_financial_close_consolidation`) [Layer: `core`]
- **Type**: `process_step` | **Tags**: `financial_close, consolidation, currency_translation, trial_balance, group_reporting`
- **RACI**: `{"responsible": ["role_consolidation_specialist"], "accountable": ["role_finance_controller"], "consulted": ["role_general_ledger_accountant"], "informed": ["role_internal_auditor"]}`
- **Assets**: `asset_erp_system, asset_financial_consolidation_system`

# Process Step: Financial Close Orchestration & Group Consolidation

## Executive Summary
Orchestrates period-end ledger closing tasks, locks transactional subledgers, executes foreign currency revaluation and translation, applies top-side consolidation journal adjustments, and produces the consolidated group trial balance.

## 1. Strategic Intent & Outcome (Tier 1 - Executive Level)
- **Business Value**: Delivers rapid, audit-certified global financial consolidation across multiple currencies, tax jurisdictions, and legal structures.
- **Strategic Alignment**: Directly dictates the corporate earnings release calendar, investor communication timelines, and executive board governance.
- **Risk Exposure**: Delayed close milestones, flawed currency conversion gains/losses, unauthorized post-close adjustments, or consolidation calculation errors.

## 2. Operational Workflow & RACI (Tier 2 - Process Architect Level)
- **Workflow Sequence**:
  1. Period-end close checklist enforces hard close cutoff and locks local general ledgers in `asset_erp_system`.
  2. Local entity trial balances ingest into `asset_financial_consolidation_system`.
  3. Automated translation routines apply closing FX spot rates (balance sheet) and monthly average FX rates (income statement).
  4. Top-side group eliminations, minority interest allocations, and equity pickup journals are computed and posted.
  5. Consolidated trial balance is validated, verified against SoX controls, and locked by `role_finance_controller`.
- **RACI Assignment Matrix**:
  - **Responsible**: `role_consolidation_specialist`
  - **Accountable**: `role_finance_controller`
  - **Consulted**: `role_general_ledger_accountant`
  - **Informed**: `role_internal_auditor`
- **Service Level Agreement (SLA)**: 48.0 Hours.

## 3. Systems Math & Simulation Parameters (Tier 3 - Simulation Engineer Level)
```math
\text{Consolidation Duration} = \text{Base Run Time} + \sum_{i=1}^{N_{\text{Entities}}} \left(\text{Data Transfer Time}_i + \text{FX Translation Delay}_i\right)
```
- **Primary Data Entity**: Consolidated Financial Trial Balance (`CONSOLIDATED_TRIAL_BALANCE_v1`).
- **Asset Load**: Heavy compute workload in `asset_financial_consolidation_system`, batch extracts from `asset_erp_system`.
---

### [Statutory, Tax & Management Financial Reporting] (`r2r_005_statutory_financial_reporting`) [Layer: `core`]
- **Type**: `process_step` | **Tags**: `statutory_reporting, sec_filing, 10k, management_reporting, disclosure`
- **RACI**: `{"responsible": ["role_consolidation_specialist"], "accountable": ["role_finance_controller"], "consulted": ["role_internal_auditor"], "informed": ["role_general_ledger_accountant"]}`
- **Assets**: `asset_financial_consolidation_system`

# Process Step: Statutory, Tax & Management Financial Reporting

## Executive Summary
Generates external statutory financial filings (SEC Form 10-K / 10-Q under US GAAP / IFRS), local statutory annual accounts, tax provision schedules, and executive C-suite management reporting packages.

## 1. Strategic Intent & Outcome (Tier 1 - Executive Level)
- **Business Value**: Delivers transparent, compliant regulatory disclosures to capital markets, ensuring investor confidence and preventing legal or SEC sanctions.
- **Strategic Alignment**: Directly enables CFO earnings calls, Board Audit Committee reviews, and external credit rating evaluations.
- **Risk Exposure**: Inaccurate financial statement footnotes, regulatory filing delays, restatements, or non-compliance penalties.

## 2. Operational Workflow & RACI (Tier 2 - Process Architect Level)
- **Workflow Sequence**:
  1. Consolidated financial statements (Income Statement, Balance Sheet, Cash Flows, Equity) generated in `asset_financial_consolidation_system`.
  2. Disclosure management tools aggregate footnote schedules, debt maturity profiles, and segment reporting.
  3. `role_internal_auditor` and external auditors execute tie-out and substantive sampling of reporting schedules.
  4. Final financial statements and MD&A packages route to `role_finance_controller` and CFO for certification sign-off.
  5. SEC Edgar / XBRL filing packages and executive board binders are published.
- **RACI Assignment Matrix**:
  - **Responsible**: `role_consolidation_specialist`
  - **Accountable**: `role_finance_controller`
  - **Consulted**: `role_internal_auditor`
  - **Informed**: `role_general_ledger_accountant`
- **Service Level Agreement (SLA)**: 32.0 Hours.

## 3. Systems Math & Simulation Parameters (Tier 3 - Simulation Engineer Level)
```math
\text{Reporting Accuracy Confidence} = 1 - \sum \left(\text{Footnote Tie-Out Variances} + \text{XBRL Tagging Errors}\right)
```
- **Primary Data Entity**: Statutory Financial Report & Filing Package (`STATUTORY_REPORTING_PACK_v1`).
- **Asset Load**: `asset_financial_consolidation_system`.
---

### [SOX 404 Financial Reporting Internal Controls & Materiality Thresholds Policy] (`sox_financial_reporting_controls_policy`) [Layer: `core`]
- **Type**: `control_policy` | **Tags**: `policy, sox, compliance, internal_controls, financial_reporting, r2r`
- **RACI**: `{"responsible": ["role_general_ledger_accountant"], "accountable": ["role_finance_controller"], "consulted": ["role_consolidation_specialist", "role_internal_auditor"], "informed": ["role_internal_auditor"]}`
- **Assets**: `asset_erp_system, asset_financial_consolidation_system`

# Control Policy: SOX 404 Financial Reporting Internal Controls

## Executive Summary
Establishes enterprise internal controls over financial reporting (ICFR) pursuant to Sarbanes-Oxley Act Section 404, defining segregation of duties, journal entry approval thresholds, balance sheet substantiation deadlines, and financial consolidation audit trails.

## 1. Governance Rules & Controls (Tier 1 - Strategic Level)
- **Control 1 (Dual Sign-Off on Manual Journals)**: All non-system manual journal entries exceeding $50,000 USD require explicit electronic dual sign-off from `role_finance_controller` prior to general ledger posting.
- **Control 2 (Segregation of Duties - SoD)**: Under no operational circumstances may the individual creating a journal entry approve or post the identical entry in `asset_erp_system`.
- **Control 3 (Balance Sheet Substantiation Deadline)**: 100% of high-risk balance sheet accounts (cash, inventory, intercompany, debt) must be reconciled with third-party statements by T+3 business days following period-end.
- **Control 4 (Consolidation Elimination Auditability)**: Top-side consolidation adjustments executed in `asset_financial_consolidation_system` must possess documented business justification and formal Controller sign-off.
- **Control 5 (Internal Audit Independent Testing)**: Quarterly independent sampling by `role_internal_auditor` to certify design and operating effectiveness of controls.
---

