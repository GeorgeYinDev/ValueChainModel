# System Prompt: LLM Context Blueprint for Business Lifecycle [Lead to Cash]

> Profile: `professional_services` | Lifecycle ID: `L2C` | Version: `1.1.0` | Source Layer: `professional_services`
> Description: Sales pipeline generation, proposal development, and contract closure.

## Milestone Process Sequence
- **Step 1**: `l2c_001_lead_qualification` (Lead Qualification)
- **Step 2**: `l2c_002_proposal_development` (Proposal Development)
- **Step 3**: `l2c_003_contract_negotiation` (Contract Negotiation)
- **Step 4**: `l2c_004_deal_closure_handover` (Deal Closure)

## Key Performance Indicators (KPIs)
- `Win Rate`
- `Time to Close`
- `Pipeline Velocity`

## Active Value Chain Elements Knowledge Base

### [Project Pricing & Target Gross Margin Governance Policy] (`project_pricing_margin_policy`) [Layer: `professional_services`]
- **Type**: `control_policy` | **Tags**: `policy, pricing, margin, governance, professional_services`
- **RACI**: `{"responsible": ["role_solution_architect"], "accountable": ["role_practice_director"], "consulted": ["role_account_executive"], "informed": ["role_engagement_manager"]}`
- **Assets**: `asset_crm_system, asset_psa_system`

# Control Policy: Project Pricing & Target Gross Margin Governance

## Executive Summary
Defines corporate governance standards for pricing client engagements, validating rate card compliance, setting mandatory gross margin hurdle rates, and enforcing escalation workflows for non-standard commercial concessions.

## 1. Governance Rules & Controls (Tier 1)
- **Rule 1 (Minimum Margin Hurdle Rate)**: All proposed client engagements (fixed-fee and time-and-materials) must meet or exceed a baseline projected Gross Margin of 45.0%.
- **Rule 2 (Rate Card Discounting Limits)**:
  - Discounts <= 10.0% against standard master rate cards: Authorized by `role_account_executive`.
  - Discounts 10.1% to 20.0%: Mandates sign-off from `role_practice_director` (up to approval limit of $250,000 USD).
  - Discounts > 20.0%: Mandates executive exception sign-off from `role_finance_controller`.
- **Rule 3 (Fixed-Fee Scope Contingency Buffer)**: Fixed-price contracts must incorporate a mandatory 15.0% scope contingency risk buffer in effort estimation models before proposal delivery.
---

### [Statement of Work (SOW) & Engagement Contract] (`data_statement_of_work`) [Layer: `professional_services`]
- **Type**: `data_entity` | **Tags**: `data, sow, contract, legal, commercial`
- **RACI**: `{}`
- **Assets**: ``

# Data Entity: Statement of Work (SOW) & Engagement Contract

The formal commercial agreement executed between the consulting practice and the client. Defines engagement scope, milestone deliverables, staffing rate cards, billing schedules, and liability terms.
---

### [Professional Services Deal Win Rate] (`kpi_deal_win_rate`) [Layer: `professional_services`]
- **Type**: `kpi_metric` | **Tags**: `kpi, sales, win_rate, pipeline, commercial`
- **RACI**: `{}`
- **Assets**: ``

# KPI: Professional Services Deal Win Rate

Measures the efficiency of the commercial sales and proposal development lifecycle in converting qualified pursuits into signed statements of work.
---

### [Lead Qualification & Discovery] (`l2c_001_lead_qualification`) [Layer: `professional_services`]
- **Type**: `process_step` | **Tags**: `sales, pipeline, discovery`
- **RACI**: `{"responsible": ["role_account_executive"], "accountable": ["role_practice_director"], "consulted": ["role_solution_architect"], "informed": ["role_sales_ops_specialist"]}`
- **Assets**: `asset_crm_system`

# Lead Qualification & Discovery
Initial engagement with a prospect to understand their business challenges, budget, and timeline to determine if there is a viable consulting opportunity.
---

### [Proposal Development & Scoping] (`l2c_002_proposal_development`) [Layer: `professional_services`]
- **Type**: `process_step` | **Tags**: `presales, proposal, estimation`
- **RACI**: `{"responsible": ["role_solution_architect"], "accountable": ["role_practice_director"], "consulted": ["role_engagement_manager"], "informed": ["role_customer"]}`
- **Assets**: `asset_crm_system`

# Proposal Development & Scoping
The process of capturing client requirements, estimating effort, defining timelines, and generating the Statement of Work (SOW).
---

### [Contract Negotiation & Legal Review] (`l2c_003_contract_negotiation`) [Layer: `professional_services`]
- **Type**: `process_step` | **Tags**: `legal, sales, contracting`
- **RACI**: `{"responsible": ["role_account_executive"], "accountable": ["role_practice_director"], "consulted": ["role_finance_controller"], "informed": ["role_engagement_manager"]}`
- **Assets**: `asset_crm_system`

# Contract Negotiation & Legal Review
Review of MSAs, NDAs, and SOW terms and conditions between the firm's legal team and the client.
---

### [Deal Closure & Delivery Handover] (`l2c_004_deal_closure_handover`) [Layer: `professional_services`]
- **Type**: `process_step` | **Tags**: `sales, delivery, handover`
- **RACI**: `{"responsible": ["role_account_executive"], "accountable": ["role_engagement_manager"], "consulted": ["role_solution_architect"], "informed": ["role_sales_ops_specialist"]}`
- **Assets**: `asset_crm_system, asset_psa_system`

# Deal Closure & Delivery Handover
The finalized contract is signed, the opportunity is marked as 'Closed Won' in the CRM, and all project context is handed over to the delivery team.
---

### [Client Engagement & Delivery Value Stream] (`client_engagement_delivery_stream`) [Layer: `professional_services`]
- **Type**: `value_stream` | **Tags**: `value_stream, consulting, delivery, professional_services, client_engagement`
- **RACI**: `{"responsible": ["role_account_executive", "role_engagement_manager"], "accountable": ["role_practice_director"], "consulted": ["role_solution_architect", "role_consultant"], "informed": ["role_customer"]}`
- **Assets**: `asset_crm_system, asset_psa_system`

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
---

