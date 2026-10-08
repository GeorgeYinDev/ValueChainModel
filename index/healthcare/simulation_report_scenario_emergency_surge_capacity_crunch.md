# Scenario Simulation Executive Report

**Scenario**: Emergency Department Inpatient Surge Capacity Crunch (`scenario_emergency_surge_capacity_crunch`)
**Target Lifecycle**: `P2D`

## Executive Summary & Macro Outcomes

| Metric | Baseline | Shocked Scenario | Variance Delta |
| :--- | :--- | :--- | :--- |
| **Total Lifecycle Lead Time** | `59.0 hrs` (2.5 days) | `114.3 hrs` (4.8 days) | `+93.8%` |
| **Total Process Cost / Unit** | `$3241.40` | `$4224.32` | `+30.3%` |

## Element Breakdown & Bottleneck Sensitivity Analysis

| Process Element | Baseline Time | Shocked Time | Time Delta | Baseline Cost | Shocked Cost | Cost Delta |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Patient Registration & Scheduling** (`p2d_001_patient_registration_scheduling`) | 0.5h | 0.5h | +0% | $26.00 | $26.00 | +0% |
| **Insurance Verification & Prior Authorization** (`p2d_002_insurance_verification_prior_auth`) | 4.3h | 4.3h | +0% | $48.60 | $48.60 | +0% |
| **Clinical Admission & Triage** (`p2d_003_clinical_admission_triage`) | 1.5h | 9.6h | 🔥 +520% | $123.60 | $127.80 | +3% |
| **Care Delivery & Order Execution** (`p2d_004_care_delivery_order_execution`) | 49.0h | 85.7h | 🔥 +75% | $2856.00 | $3825.00 | +34% |
| **Discharge Planning & Care Transition** (`p2d_005_discharge_planning_transition`) | 3.6h | 14.2h | 🔥 +291% | $187.20 | $196.92 | +5% |
