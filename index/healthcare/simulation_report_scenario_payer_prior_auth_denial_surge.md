# Scenario Simulation Executive Report

**Scenario**: Payer Algorithmic Prior-Authorization & Denial Surge (`scenario_payer_prior_auth_denial_surge`)
**Target Lifecycle**: `RCM`

## Executive Summary & Macro Outcomes

| Metric | Baseline | Shocked Scenario | Variance Delta |
| :--- | :--- | :--- | :--- |
| **Total Lifecycle Lead Time** | `229.7 hrs` (9.6 days) | `344.4 hrs` (14.4 days) | `+49.9%` |
| **Total Process Cost / Unit** | `$351.45` | `$565.80` | `+61.0%` |

## Element Breakdown & Bottleneck Sensitivity Analysis

| Process Element | Baseline Time | Shocked Time | Time Delta | Baseline Cost | Shocked Cost | Cost Delta |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Charge Capture & Medical Coding** (`rcm_001_charge_capture_coding`) | 12.6h | 12.6h | +0% | $89.25 | $89.25 | +0% |
| **Claim Scrubbing & Clearinghouse Submission** (`rcm_002_claim_scrubbing_submission`) | 6.2h | 6.2h | +0% | $41.20 | $41.20 | +0% |
| **Payer Adjudication & Remittance** (`rcm_003_payer_adjudication_remittance`) | 127.2h | 127.2h | +0% | $15.90 | $15.90 | +0% |
| **Denial Management & Appeals** (`rcm_004_denial_management_appeals`) | 25.7h | 101.7h | 🔥 +296% | $117.70 | $332.05 | 💸 +182% |
| **Patient Billing & Collections** (`rcm_005_patient_billing_collections`) | 49.9h | 88.6h | 🔥 +77% | $36.40 | $36.40 | +0% |
| **Cash Posting & Subledger Reconciliation** (`rcm_006_cash_posting_reconciliation`) | 8.2h | 8.2h | +0% | $51.00 | $51.00 | +0% |
