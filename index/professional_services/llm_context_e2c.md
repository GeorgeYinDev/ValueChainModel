# System Prompt: LLM Context Blueprint for Business Lifecycle [Engagement to Cash]

> Profile: `professional_services` | Lifecycle ID: `E2C` | Version: `1.1.0` | Source Layer: `professional_services`
> Description: Project delivery, resource allocation, time tracking, and billing.

## Milestone Process Sequence
- **Step 1**: `e2c_001_project_kickoff` (Project Kickoff)
- **Step 2**: `e2c_002_resource_scheduling` (Resource Scheduling)
- **Step 3**: `e2c_003_project_execution_delivery` (Project Execution)
- **Step 4**: `e2c_004_time_expense_entry` (Time & Expense Entry)
- **Step 5**: `e2c_005_client_acceptance` (Client Acceptance)
- **Step 6**: `e2c_006_project_billing_invoicing` (Project Billing)
- **Step 7**: `e2c_007_project_closure_lessons` (Project Closure)

## Key Performance Indicators (KPIs)
- `Utilization Rate`
- `Project Margin`
- `Days Sales Outstanding (DSO)`

## Active Value Chain Elements Knowledge Base

### [Consultant Time & Expense Submission Compliance Policy] (`time_expense_compliance_policy`) [Layer: `professional_services`]
- **Type**: `control_policy` | **Tags**: `policy, compliance, timesheets, expenses, governance`
- **RACI**: `{"responsible": ["role_consultant"], "accountable": ["role_engagement_manager"], "consulted": ["role_billing_specialist"], "informed": ["role_practice_director"]}`
- **Assets**: `asset_psa_system`

# Control Policy: Consultant Time & Expense Submission Compliance

## Executive Summary
Establishes operating rules and governance controls for logging, substantiating, and approving billable and non-billable hours and project-related reimbursable expenses in the PSA platform.

## 1. Governance Rules & Controls (Tier 1)
- **Rule 1 (Weekly Submission Cutoff SLA)**: All consultants must submit complete weekly timesheets and expense records in `asset_psa_system` by 10:00 AM local time each Monday.
- **Rule 2 (Itemized Expense Substantiation)**: All single-item expense claims exceeding $25.00 USD require an attached, legible electronic receipt and documented business purpose.
- **Rule 3 (Manager Approval SLA)**: Engagement Managers must review and sign off or reject timesheets within 24 hours of submission to prevent month-end billing crunch delays.
---

### [Consultant Time & Expense Record] (`data_consultant_timesheet`) [Layer: `professional_services`]
- **Type**: `data_entity` | **Tags**: `data, timesheet, psa, billing, labor`
- **RACI**: `{}`
- **Assets**: ``

# Data Entity: Consultant Time & Expense Record

The operational unit of delivery effort and project expenditure. Captures daily consultant billable and non-billable hours booked to project WBS work breakdown codes alongside reimbursable client expenses.
---

### [Statement of Work (SOW) & Engagement Contract] (`data_statement_of_work`) [Layer: `professional_services`]
- **Type**: `data_entity` | **Tags**: `data, sow, contract, legal, commercial`
- **RACI**: `{}`
- **Assets**: ``

# Data Entity: Statement of Work (SOW) & Engagement Contract

The formal commercial agreement executed between the consulting practice and the client. Defines engagement scope, milestone deliverables, staffing rate cards, billing schedules, and liability terms.
---

### [Billable Consultant Utilization Rate] (`kpi_billable_utilization`) [Layer: `professional_services`]
- **Type**: `kpi_metric` | **Tags**: `kpi, utilization, capacity, consulting, psa`
- **RACI**: `{}`
- **Assets**: ``

# KPI: Billable Consultant Utilization Rate

Measures the proportion of available consultant working hours billed to client engagements versus administrative, bench, or internal time. Vital operational health metric tracked within the PSA platform.
---

### [Project Gross Margin Percentage] (`kpi_project_gross_margin`) [Layer: `professional_services`]
- **Type**: `kpi_metric` | **Tags**: `kpi, margin, profitability, finance, consulting`
- **RACI**: `{}`
- **Assets**: ``

# KPI: Project Gross Margin Percentage

Measures profitability of delivery engagements after deducting consultant labor rates and direct project expenses from invoiced revenue.
---

### [Project Kickoff & Resource Allocation] (`e2c_001_project_kickoff`) [Layer: `professional_services`]
- **Type**: `process_step` | **Tags**: `delivery, staffing, kickoff`
- **RACI**: `{"responsible": ["role_engagement_manager"], "accountable": ["role_practice_director"], "consulted": ["role_consultant"], "informed": ["role_customer"]}`
- **Assets**: `asset_psa_system`

# Project Kickoff & Resource Allocation
Onboarding the project team, assigning consultants to billable tasks in the PSA system, and conducting the client kickoff meeting.
---

### [Resource Scheduling & Allocation] (`e2c_002_resource_scheduling`) [Layer: `professional_services`]
- **Type**: `process_step` | **Tags**: `resourcing, psa, capacity`
- **RACI**: `{"responsible": ["role_engagement_manager"], "accountable": ["role_practice_director"], "consulted": ["role_hr_business_partner"], "informed": ["role_consultant"]}`
- **Assets**: `asset_psa_system`

# Resource Scheduling & Allocation
Assigning specific consultants to project milestones based on skill requirements, availability, and geographic location using the PSA system.
---

### [Project Execution & Milestone Delivery] (`e2c_003_project_execution_delivery`) [Layer: `professional_services`]
- **Type**: `process_step` | **Tags**: `delivery, consulting, engineering`
- **RACI**: `{"responsible": ["role_consultant"], "accountable": ["role_engagement_manager"], "consulted": ["role_solution_architect"], "informed": ["role_customer"]}`
- **Assets**: ``

# Project Execution & Milestone Delivery
The core delivery of consulting services, encompassing analysis, design, build, test, and advisory activities as defined in the SOW.
---

### [Time & Expense Logging] (`e2c_004_time_expense_entry`) [Layer: `professional_services`]
- **Type**: `process_step` | **Tags**: `timesheets, psa, compliance`
- **RACI**: `{"responsible": ["role_consultant"], "accountable": ["role_engagement_manager"], "consulted": ["role_billing_specialist"], "informed": ["role_practice_director"]}`
- **Assets**: `asset_psa_system`

# Time & Expense Logging
Consultants submit weekly timesheets and expense reports against specific project WBS codes for approval and capitalization.
---

### [Client Review & Deliverable Acceptance] (`e2c_005_client_acceptance`) [Layer: `professional_services`]
- **Type**: `process_step` | **Tags**: `quality, acceptance, signoff`
- **RACI**: `{"responsible": ["role_engagement_manager"], "accountable": ["role_engagement_manager"], "consulted": ["role_customer"], "informed": ["role_billing_specialist"]}`
- **Assets**: `asset_psa_system`

# Client Review & Deliverable Acceptance
Formal client sign-off on completed milestones or monthly timesheets, triggering revenue recognition and billing events.
---

### [Project Billing & Invoicing] (`e2c_006_project_billing_invoicing`) [Layer: `professional_services`]
- **Type**: `process_step` | **Tags**: `billing, revenue, finance`
- **RACI**: `{"responsible": ["role_billing_specialist"], "accountable": ["role_finance_controller"], "consulted": ["role_engagement_manager"], "informed": ["role_customer"]}`
- **Assets**: `asset_psa_system, asset_erp_system`

# Project Billing & Invoicing
Generation of client invoices based on T&M actuals or fixed-fee milestones, posting receivables to the general ledger.
---

### [Project Closure & Lessons Learned] (`e2c_007_project_closure_lessons`) [Layer: `professional_services`]
- **Type**: `process_step` | **Tags**: `closure, knowledge, retrospective`
- **RACI**: `{"responsible": ["role_engagement_manager"], "accountable": ["role_practice_director"], "consulted": ["role_consultant"], "informed": ["role_account_executive"]}`
- **Assets**: `asset_psa_system`

# Project Closure & Lessons Learned
Archiving project artifacts, releasing remaining consultants to the bench, and conducting retrospective reviews to harvest IP and update delivery methodologies.
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

### [Consulting Time, Expense & Revenue Billing Stream] (`consulting_revenue_billing_stream`) [Layer: `professional_services`]
- **Type**: `value_stream` | **Tags**: `value_stream, billing, time_and_expense, revenue, professional_services`
- **RACI**: `{"responsible": ["role_consultant", "role_billing_specialist"], "accountable": ["role_engagement_manager"], "consulted": ["role_practice_director"], "informed": ["role_finance_controller"]}`
- **Assets**: `asset_psa_system, asset_erp_system`

# Value Stream: Consulting Time, Expense & Revenue Billing Stream (E2C)

## Executive Summary
Encompasses the operational revenue cycle of professional services engagements, starting with consultant time and expense capture, progressing through client acceptance, and culminating in invoice dispatch and subledger ingestion into corporate General Ledger accounting.

## 1. Strategic Outcomes (Tier 1 - Executive Level)
- **Accelerate Cash Conversion & DSO Reduction**: Shorten cycle times from milestone delivery to invoice issuance and cash collection.
- **Prevent Revenue Leakage & Disputed Invoices**: Enforce pre-invoicing client sign-off to minimize write-offs, credit notes, and invoice revisions.
- **Unified Financial Triad Ingestion**: Direct electronic feeding of professional services invoices into R2R General Ledger journal vouchers (`r2r_001_journal_entry_recording`).

## 2. Included Steps & RACI Summary (Tier 2 - Process Architect Level)
1. `e2c_004_time_expense_entry` - Time & Expense Logging
2. `e2c_005_client_acceptance` - Client Deliverable Review & Acceptance Sign-off
3. `e2c_006_project_billing_invoicing` - Project Invoicing & AR Subledger Ingestion
4. Core Integration: Postings feed directly to `r2r_001_journal_entry_recording` in the core Record-to-Report ledger.

## 3. Systems Math & Quantitative Parameters (Tier 3 - Systems Engineer Level)
```math
\text{Billing Cycle Latency} = \text{TimeEntryToApproval} + \text{ClientSignoffLag} + \text{InvoiceBatchProcessing}
```
- **Primary Operational Assets**: Professional Services Automation (`asset_psa_system`), Core ERP Financial Ledger (`asset_erp_system`).
- **Automation Pipeline**: 52% baseline automated workflow from approved timesheets to draft ERP invoices.
---

