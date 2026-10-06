---
id: h2r_004_payroll_benefits_enrollment
type: process_step
name: "Payroll & Benefits Enrollment Processing"
version: "1.0.0"
lifecycles: ["H2R"]
lod_support: ["tier_1", "tier_2", "tier_3"]
tags: ["hr", "payroll", "benefits", "finance"]

raci:
  responsible: [role_payroll_specialist]
  accountable: [role_payroll_specialist]
  consulted: [role_hr_business_partner]
  informed: [role_finance_controller]

attributes:
  baseline_cycle_time_hours: 24.0
  baseline_cost_per_unit: 45.0
  automation_rate: 0.85
  error_rate: 0.02
  sla_hours: 48.0
  volume_per_period: 50
  capacity_fte: 1.5

asset_dependencies:
  - asset_payroll_engine
  - asset_hcm_platform

graph_relations:
  - relation: feeds_into
    target: h2r_005_performance_compensation_review
    weight: 1.0
  - relation: feeds_into
    target: r2r_001_journal_entry_recording
    weight: 1.0

compensating_control: "Payroll processing outputs are formally audited by Finance Controller prior to disbursement."
---

# Process Step: Payroll & Benefits Enrollment Processing

## Executive Summary
Establishes the employee's direct deposit, tax withholdings, and benefits elections, integrating them into the ongoing payroll cycles.

## 1. Strategic Intent & Outcome (Tier 1 - Executive Level)
- **Business Value**: Ensures accurate and timely compensation, maintaining employee trust and regulatory compliance.
- **Risk Exposure**: Incorrect tax withholdings, missed benefit enrollments, or payroll errors causing financial misstatements.

## 2. Operational Workflow (Tier 2)
- Employee completes self-service onboarding forms (W-4, I-9, benefits).
- Payroll specialist verifies data flow from HCM to Payroll Engine.
- Payroll engine calculates gross-to-net and triggers disbursement.
- Payroll generates aggregated expense and liability journals, feeding into `r2r_001_journal_entry_recording`.
