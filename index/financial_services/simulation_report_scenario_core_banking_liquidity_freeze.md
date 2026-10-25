# Scenario Simulation Executive Report

**Scenario**: Core Banking Subledger & Fedwire Settlement Outage (`scenario_core_banking_liquidity_freeze`)
**Target Lifecycle**: `L2S`

## Executive Summary & Macro Outcomes

| Metric | Baseline | Shocked Scenario | Variance Delta |
| :--- | :--- | :--- | :--- |
| **Total Lifecycle Lead Time** | `76.1 hrs` (3.2 days) | `145.5 hrs` (6.1 days) | `+91.2%` |
| **Total Process Cost / Unit** | `$2457.50` | `$2482.30` | `+1.0%` |

## Element Breakdown & Bottleneck Sensitivity Analysis

| Process Element | Baseline Time | Shocked Time | Time Delta | Baseline Cost | Shocked Cost | Cost Delta |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Loan Application & Credit Packaging** (`l2s_001_loan_application_credit_packaging`) | 12.5h | 12.5h | +0% | $395.20 | $395.20 | +0% |
| **Credit Underwriting & PD/LGD Risk Rating** (`l2s_002_credit_underwriting_risk_rating`) | 24.7h | 24.7h | +0% | $844.60 | $844.60 | +0% |
| **Collateral Valuation & Lien Perfection** (`l2s_003_collateral_valuation_lien_perfection`) | 18.5h | 18.5h | +0% | $556.20 | $556.20 | +0% |
| **Loan Booking & Principal Funding Disbursement** (`l2s_004_loan_booking_funding_disbursement`) | 4.0h | 36.4h | 🔥 +800% | $151.50 | $151.50 | +0% |
| **Repayment Servicing & Covenant Monitoring** (`l2s_005_repayment_servicing_covenant_monitoring`) | 6.1h | 6.1h | +0% | $193.80 | $193.80 | +0% |
| **Delinquency Workout & Subledger Reconciliation** (`l2s_006_delinquency_workout_ledger_settlement`) | 10.2h | 47.3h | 🔥 +364% | $316.20 | $341.00 | +8% |
