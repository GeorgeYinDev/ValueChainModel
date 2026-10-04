# Scenario Simulation Executive Report

**Scenario**: Fiscal Year-End Financial Close Crunch & Manual Adjustment Surge (`scenario_close_period_crunch`)
**Target Lifecycle**: `R2R`

## Executive Summary & Macro Outcomes

| Metric | Baseline | Shocked Scenario | Variance Delta |
| :--- | :--- | :--- | :--- |
| **Total Lifecycle Lead Time** | `71.1 hrs` (3.0 days) | `203.3 hrs` (8.5 days) | `+186.1%` |
| **Total Process Cost / Unit** | `$216.09` | `$271.05` | `+25.4%` |

## Element Breakdown & Bottleneck Sensitivity Analysis

| Process Element | Baseline Time | Shocked Time | Time Delta | Baseline Cost | Shocked Cost | Cost Delta |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **General Ledger Journal Recording & Subledger Ingestion** (`r2r_001_journal_entry_recording`) | 8.1h | 33.6h | 🔥 +314% | $18.27 | $18.90 | +3% |
| **Intercompany Transaction Matching & Elimination** (`r2r_002_intercompany_reconciliation`) | 12.3h | 52.9h | 🔥 +330% | $35.88 | $90.20 | 💸 +151% |
| **Balance Sheet Account Substantiation & Reconciliation** (`r2r_003_balance_sheet_substantiation`) | 16.3h | 50.2h | 🔥 +208% | $45.90 | $45.90 | +0% |
| **Financial Close Orchestration & Group Consolidation** (`r2r_004_financial_close_consolidation`) | 20.2h | 52.5h | 🔥 +160% | $65.65 | $65.65 | +0% |
| **Statutory, Tax & Management Financial Reporting** (`r2r_005_statutory_financial_reporting`) | 14.1h | 14.1h | +0% | $50.40 | $50.40 | +0% |
