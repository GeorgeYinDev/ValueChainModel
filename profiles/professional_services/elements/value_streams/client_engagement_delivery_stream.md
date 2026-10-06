---
id: client_engagement_delivery_stream
type: value_stream
name: Client Engagement & Delivery Value Stream
version: 1.0.0
lifecycles: [L2C, E2C]
lod_support: [tier_1, tier_2, tier_3]
tags: [value_stream, consulting, delivery, professional_services, client_engagement]

raci:
  responsible: [role_account_executive, role_engagement_manager]
  accountable: [role_practice_director]
  consulted: [role_solution_architect, role_consultant]
  informed: [role_customer]

daci:
  driver: [role_engagement_manager]
  approver: [role_practice_director]
  contributor: [role_account_executive, role_solution_architect]
  informed: [role_customer]

attributes:
  baseline_cycle_time_hours: 288.0
  baseline_cost_per_unit: 24700.0
  automation_rate: 0.28
  error_rate: 0.08
  sla_hours: 360.0

asset_dependencies:
  - asset_crm_system
  - asset_psa_system

graph_relations:
  - relation: governed_by
    target: project_pricing_margin_policy
    weight: 1.0
---

# Value Stream: Client Engagement & Delivery (L2C / E2C)

## Executive Summary
Orchestrates the end-to-end commercial pursuit, statement of work negotiation, consultant staffing, milestone execution, and engagement closure lifecycle for professional services and management consulting organizations.

## 1. Strategic Outcomes (Tier 1 - Executive Level)
- **Accelerate Commercial Pipeline Velocity**: Compress sales and contracting cycle times while preserving healthy billing margins.
- **Optimize Consultant Utilization & Delivery Margins**: Ensure balanced allocation of billable resources, preventing bench spikes and margin dilution.
- **Mitigate Scope Creep & Delivery Risk**: Enforce structured milestone acceptance sign-offs before transitioning to subsequent phases.

## 2. Included Steps & RACI Summary (Tier 2 - Process Architect Level)
### Lead-to-Cash (L2C) Milestones:
1. `l2c_001_lead_qualification` - Opportunity Discovery & Qualification
2. `l2c_002_proposal_development` - Scoping, Effort Estimation & SOW Authoring
3. `l2c_003_contract_negotiation` - MSA & SOW Terms Negotiation
4. `l2c_004_deal_closure_handover` - Deal Won Booking & Delivery Handover

### Engagement-to-Cash (E2C) Milestones:
5. `e2c_001_project_kickoff` - Project Initiation & Team Onboarding
6. `e2c_002_resource_scheduling` - PSA Resource Scheduling & Capacity Matching
7. `e2c_003_project_execution_delivery` - Core Milestone Delivery & Deliverable Drafting
8. `e2c_004_time_expense_entry` - Weekly Timesheet & Reimbursable Expense Submission
9. `e2c_005_client_acceptance` - Formal Milestone Sign-Off & Client Acceptance
10. `e2c_006_project_billing_invoicing` - Invoicing & Revenue Recognition Feeds
11. `e2c_007_project_closure_lessons` - Post-Project Retrospective & Knowledge Capital Harvesting

## 3. Systems Math & Quantitative Parameters (Tier 3 - Systems Engineer Level)
```math
\text{Total Engagement Lead Time} = \sum_{i \in \text{L2C}} \text{LeadTime}_i + \sum_{j \in \text{E2C}} \text{LeadTime}_j
```
- **Primary Operational Assets**: CRM Engine (`asset_crm_system`), Professional Services Automation (`asset_psa_system`).
- **Baseline Automation Ratio**: 28% automated workflow orchestration across pipeline stages.
