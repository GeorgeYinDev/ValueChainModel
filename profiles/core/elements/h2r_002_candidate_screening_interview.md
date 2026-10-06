---
id: h2r_002_candidate_screening_interview
type: process_step
name: "Candidate Screening & Interview Execution"
version: "1.0.0"
lifecycles: ["H2R"]
lod_support: ["tier_1", "tier_2", "tier_3"]
tags: ["hr", "recruitment", "interview"]

raci:
  responsible: [role_talent_acquisition_specialist]
  accountable: [role_hiring_manager]
  consulted: [role_hr_business_partner]
  informed: []

attributes:
  baseline_cycle_time_hours: 168.0
  baseline_cost_per_unit: 800.0
  automation_rate: 0.30
  error_rate: 0.15
  sla_hours: 240.0
  volume_per_period: 250
  capacity_fte: 5.0

asset_dependencies:
  - asset_hcm_platform

graph_relations:
  - relation: feeds_into
    target: h2r_003_offer_letter_onboarding
    weight: 0.20
  - relation: exception_to
    target: h2r_001_job_requisition_posting
    weight: 1.0
    probability: 0.10
---

# Process Step: Candidate Screening & Interview Execution

## Executive Summary
Sources applicants, screens resumes, coordinates interview panels, and synthesizes feedback to select a final candidate for an offer.

## 1. Strategic Intent & Outcome (Tier 1 - Executive Level)
- **Business Value**: Identifies top talent to drive enterprise objectives.
- **Risk Exposure**: High candidate drop-off rate or poor candidate experience.

## 2. Operational Workflow (Tier 2)
- Recruiter screens inbound applications and sourced prospects.
- Recruiter conducts phone screens and schedules panel interviews.
- Hiring manager and panel execute interviews and submit scorecards.
- Hiring decision is made; unselected candidates are notified.
