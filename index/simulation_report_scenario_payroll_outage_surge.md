# Scenario Simulation Executive Report

**Scenario**: Payroll System Outage at Cutoff (`scenario_payroll_outage_surge`)
**Target Lifecycle**: `H2R`

## Executive Summary & Macro Outcomes

| Metric | Baseline | Shocked Scenario | Variance Delta |
| :--- | :--- | :--- | :--- |
| **Total Lifecycle Lead Time** | `497.3 hrs` (20.7 days) | `512.4 hrs` (21.3 days) | `+3.0%` |
| **Total Process Cost / Unit** | `$1789.40` | `$1793.00` | `+0.2%` |

## Element Breakdown & Bottleneck Sensitivity Analysis

| Process Element | Baseline Time | Shocked Time | Time Delta | Baseline Cost | Shocked Cost | Cost Delta |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Job Requisition Definition & Posting** (`h2r_001_job_requisition_posting`) | 50.4h | 50.4h | +0% | $126.00 | $126.00 | +0% |
| **Candidate Screening & Interview Execution** (`h2r_002_candidate_screening_interview`) | 193.2h | 193.2h | +0% | $920.00 | $920.00 | +0% |
| **Offer Letter Generation & Employee Onboarding** (`h2r_003_offer_letter_onboarding`) | 50.4h | 50.4h | +0% | $157.50 | $157.50 | +0% |
| **Payroll & Benefits Enrollment Processing** (`h2r_004_payroll_benefits_enrollment`) | 24.5h | 39.6h | 🔥 +62% | $45.90 | $49.50 | +8% |
| **Performance & Compensation Review** (`h2r_005_performance_compensation_review`) | 126.0h | 126.0h | +0% | $210.00 | $210.00 | +0% |
| **Separation, Offboarding & Final Settlement** (`h2r_006_separation_offboarding_settlement`) | 52.8h | 52.8h | +0% | $330.00 | $330.00 | +0% |
