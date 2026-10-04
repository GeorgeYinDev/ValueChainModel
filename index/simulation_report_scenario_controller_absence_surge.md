# Scenario Simulation Executive Report

**Scenario**: Finance Controller Absence During Period Close (`scenario_controller_absence_surge`)
**Target Lifecycle**: `R2R`

## Executive Summary & Macro Outcomes

| Metric | Baseline | Shocked Scenario | Variance Delta |
| :--- | :--- | :--- | :--- |
| **Total Lifecycle Lead Time** | `71.1 hrs` (3.0 days) | `192.3 hrs` (8.0 days) | `+170.6%` |
| **Total Process Cost / Unit** | `$216.09` | `$216.09` | `+0.0%` |

## Element Breakdown & Bottleneck Sensitivity Analysis

| Process Element | Baseline Time | Shocked Time | Time Delta | Baseline Cost | Shocked Cost | Cost Delta |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **General Ledger Journal Recording & Subledger Ingestion** (`r2r_001_journal_entry_recording`) | 8.1h | 32.5h | 🔥 +300% | $18.27 | $18.27 | +0% |
| **Intercompany Transaction Matching & Elimination** (`r2r_002_intercompany_reconciliation`) | 12.3h | 12.3h | +0% | $35.88 | $35.88 | +0% |
| **Balance Sheet Account Substantiation & Reconciliation** (`r2r_003_balance_sheet_substantiation`) | 16.3h | 16.3h | +0% | $45.90 | $45.90 | +0% |
| **Financial Close Orchestration & Group Consolidation** (`r2r_004_financial_close_consolidation`) | 20.2h | 60.6h | 🔥 +200% | $65.65 | $65.65 | +0% |
| **Statutory, Tax & Management Financial Reporting** (`r2r_005_statutory_financial_reporting`) | 14.1h | 70.6h | 🔥 +400% | $50.40 | $50.40 | +0% |
