---
id: h2r_003_offer_letter_onboarding
type: process_step
name: "Offer Letter Generation & Employee Onboarding"
version: "1.0.0"
lifecycles: ["H2R"]
lod_support: ["tier_1", "tier_2", "tier_3"]
tags: ["hr", "offer", "onboarding"]

raci:
  responsible: [role_talent_acquisition_specialist]
  accountable: [role_hiring_manager]
  consulted: [role_compensation_analyst]
  informed: [role_payroll_specialist]

attributes:
  baseline_cycle_time_hours: 48.0
  baseline_cost_per_unit: 150.0
  automation_rate: 0.70
  error_rate: 0.05
  sla_hours: 72.0
  volume_per_period: 50
  capacity_fte: 2.0

asset_dependencies:
  - asset_hcm_platform

graph_relations:
  - relation: feeds_into
    target: h2r_004_payroll_benefits_enrollment
    weight: 1.0
  - relation: exception_to
    target: h2r_002_candidate_screening_interview
    weight: 1.0
    probability: 0.15
---

# Process Step: Offer Letter Generation & Employee Onboarding

## Executive Summary
Drafts the formal employment offer, secures necessary compensation approvals, initiates background checks, and provisions the employee profile upon acceptance.

## 1. Strategic Intent & Outcome (Tier 1 - Executive Level)
- **Business Value**: Secures the candidate and ensures compliance with labor laws during provisioning.
- **Risk Exposure**: Offer rejection due to delays, or provisioning errors causing Day 1 productivity loss.

## 2. Operational Workflow (Tier 2)
- Recruiter drafts the offer package based on standard bands.
- Out-of-band offers route to `role_compensation_analyst`.
- Candidate digitally signs the offer.
- Background check clears and the worker profile is activated in HCM.
