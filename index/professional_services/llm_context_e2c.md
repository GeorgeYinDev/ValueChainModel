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

