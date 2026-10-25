# Scenario Simulation Executive Report

**Scenario**: Macroeconomic Rate Shock & Commercial Covenant Default Wave (`scenario_credit_default_covenant_wave`)
**Target Lifecycle**: `L2S`

## Executive Summary & Macro Outcomes

| Metric | Baseline | Shocked Scenario | Variance Delta |
| :--- | :--- | :--- | :--- |
| **Total Lifecycle Lead Time** | `76.1 hrs` (3.2 days) | `257.1 hrs` (10.7 days) | `+237.9%` |
| **Total Process Cost / Unit** | `$2457.50` | `$3232.70` | `+31.5%` |

## Element Breakdown & Bottleneck Sensitivity Analysis

| Process Element | Baseline Time | Shocked Time | Time Delta | Baseline Cost | Shocked Cost | Cost Delta |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Loan Application & Credit Packaging** (`l2s_001_loan_application_credit_packaging`) | 12.5h | 12.5h | +0% | $395.20 | $395.20 | +0% |
| **Credit Underwriting & PD/LGD Risk Rating** (`l2s_002_credit_underwriting_risk_rating`) | 24.7h | 68.0h | 🔥 +175% | $844.60 | $844.60 | +0% |
| **Collateral Valuation & Lien Perfection** (`l2s_003_collateral_valuation_lien_perfection`) | 18.5h | 65.5h | 🔥 +253% | $556.20 | $556.20 | +0% |
| **Loan Booking & Principal Funding Disbursement** (`l2s_004_loan_booking_funding_disbursement`) | 4.0h | 4.0h | +0% | $151.50 | $151.50 | +0% |
| **Repayment Servicing & Covenant Monitoring** (`l2s_005_repayment_servicing_covenant_monitoring`) | 6.1h | 34.7h | 🔥 +467% | $193.80 | $193.80 | +0% |
| **Delinquency Workout & Subledger Reconciliation** (`l2s_006_delinquency_workout_ledger_settlement`) | 10.2h | 72.4h | 🔥 +610% | $316.20 | $1091.40 | 💸 +245% |
