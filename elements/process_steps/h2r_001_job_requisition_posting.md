---
id: h2r_001_job_requisition_posting
type: process_step
name: "Job Requisition Definition & Posting"
version: "1.0.0"
lifecycles: ["H2R"]
lod_support: ["tier_1", "tier_2", "tier_3"]
tags: ["hr", "recruitment", "planning"]

raci:
  responsible: [role_hiring_manager]
  accountable: [role_hiring_manager]
  consulted: [role_hr_business_partner, role_compensation_analyst]
  informed: [role_talent_acquisition_specialist]

attributes:
  baseline_cycle_time_hours: 48.0
  baseline_cost_per_unit: 120.0
  automation_rate: 0.10
  error_rate: 0.05
  sla_hours: 72.0
  volume_per_period: 50
  capacity_fte: 2.0

asset_dependencies:
  - asset_hcm_platform

graph_relations:
  - relation: feeds_into
    target: h2r_002_candidate_screening_interview
    weight: 1.0

compensating_control: "HRBP formally approves the headcount budget prior to posting."
---

# Process Step: Job Requisition Definition & Posting

## Executive Summary
Defines headcount requirements, establishes the compensation band, and opens the job requisition within the HCM platform to formally initiate the recruitment cycle.

## 1. Strategic Intent & Outcome (Tier 1 - Executive Level)
- **Business Value**: Ensures headcount growth aligns with approved budget plans.
- **Risk Exposure**: Unbudgeted hiring or misaligned compensation benchmarking leading to pay inequity.

## 2. Operational Workflow (Tier 2)
- Hiring manager drafts the job description and submits the requisition.
- Compensation analyst reviews and attaches a salary band.
- Requisition goes live on internal and external career portals.
