# Scenario Simulation Executive Report

**Scenario**: EDI Clearinghouse Cyberattack & Claim Blackout Shock (`scenario_clearinghouse_cyberattack_outage`)
**Target Lifecycle**: `RCM`

## Executive Summary & Macro Outcomes

| Metric | Baseline | Shocked Scenario | Variance Delta |
| :--- | :--- | :--- | :--- |
| **Total Lifecycle Lead Time** | `229.7 hrs` (9.6 days) | `645.1 hrs` (26.9 days) | `+180.8%` |
| **Total Process Cost / Unit** | `$351.45` | `$509.09` | `+44.9%` |

## Element Breakdown & Bottleneck Sensitivity Analysis

| Process Element | Baseline Time | Shocked Time | Time Delta | Baseline Cost | Shocked Cost | Cost Delta |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Charge Capture & Medical Coding** (`rcm_001_charge_capture_coding`) | 12.6h | 12.6h | +0% | $89.25 | $89.25 | +0% |
| **Claim Scrubbing & Clearinghouse Submission** (`rcm_002_claim_scrubbing_submission`) | 6.2h | 79.1h | 🔥 +1180% | $41.20 | $45.84 | +11% |
| **Payer Adjudication & Remittance** (`rcm_003_payer_adjudication_remittance`) | 127.2h | 445.2h | 🔥 +250% | $15.90 | $15.90 | +0% |
| **Denial Management & Appeals** (`rcm_004_denial_management_appeals`) | 25.7h | 25.7h | +0% | $117.70 | $117.70 | +0% |
| **Patient Billing & Collections** (`rcm_005_patient_billing_collections`) | 49.9h | 49.9h | +0% | $36.40 | $36.40 | +0% |
| **Cash Posting & Subledger Reconciliation** (`rcm_006_cash_posting_reconciliation`) | 8.2h | 32.6h | 🔥 +300% | $51.00 | $204.00 | 💸 +300% |
