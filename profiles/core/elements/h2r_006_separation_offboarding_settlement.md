---
id: h2r_006_separation_offboarding_settlement
type: process_step
name: "Separation, Offboarding & Final Settlement"
version: "1.0.0"
lifecycles: ["H2R"]
lod_support: ["tier_1", "tier_2", "tier_3"]
tags: ["hr", "offboarding", "payroll"]

raci:
  responsible: [role_hr_business_partner]
  accountable: [role_hr_business_partner]
  consulted: [role_hiring_manager]
  informed: [role_payroll_specialist]

attributes:
  baseline_cycle_time_hours: 48.0
  baseline_cost_per_unit: 300.0
  automation_rate: 0.50
  error_rate: 0.10
  sla_hours: 72.0
  volume_per_period: 20
  capacity_fte: 1.0

asset_dependencies:
  - asset_hcm_platform
  - asset_payroll_engine

graph_relations:
  - relation: feeds_into
    target: r2r_001_journal_entry_recording
    weight: 1.0

compensating_control: "Final offboarding settlements are validated by Legal and Payroll prior to execution."
---

# Process Step: Separation, Offboarding & Final Settlement

## Executive Summary
Manages the voluntary or involuntary termination process, disables systems access, and calculates final paycheck and severance settlements.

## 1. Strategic Intent & Outcome (Tier 1 - Executive Level)
- **Business Value**: Mitigates security risks by revoking access and ensures compliance with final pay labor laws.
- **Risk Exposure**: Data breaches from lingering access, or legal penalties for late final paychecks.

## 2. Operational Workflow (Tier 2)
- HRBP processes termination event in HCM platform.
- Automated triggers revoke IT access and notify facilities.
- Payroll calculates final accrued PTO, severance, and regular wages.
- Final settlement is paid and general ledger is updated.
