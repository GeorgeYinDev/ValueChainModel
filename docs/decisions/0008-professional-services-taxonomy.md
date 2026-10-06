# ADR 0008: Professional Services Operating Model & Taxonomy Design

## Status
Accepted

## Context
Following the implementation of the Multi-Industry Profiles Architecture (ADR-0007), the Enterprise Value Chain engine requires an operating model for professional services, management consulting, and systems integration organizations. Unlike discrete manufacturing, revenue and fulfillment in professional services are driven by human capital allocation, statements of work (SOW), time and expense capture, milestone deliverable acceptance, and billable utilization.

## Decision
We established the Professional Services taxonomy overlay (`profiles/professional_services/`), defining two dedicated lifecycles and supporting assets, roles, and governance touchpoints:

### 1. Lifecycles
- **Lead-to-Cash (L2C)**: Commercial pipeline management for services engagements:
  - `l2c_001_lead_qualification`: Opportunity discovery and scoping against capability offerings.
  - `l2c_002_proposal_development`: Statement of Work (SOW) drafting, estimation, rate card application, and pricing committee review.
  - `l2c_003_contract_negotiation`: Master Services Agreement (MSA) and SOW legal review, SLA definition, liability caps.
  - `l2c_004_deal_closure_handover`: SOW signature, CRM deal booking, delivery practice handover.
- **Engagement-to-Cash (E2C)**: Service fulfillment and billing:
  - `e2c_001_project_kickoff`: Project charter, milestone schedule, client kickoff.
  - `e2c_002_resource_scheduling`: Staffing, consultant allocation, skill matching via PSA platform.
  - `e2c_003_project_execution_delivery`: Agile sprint/milestone execution, deliverable development.
  - `e2c_004_time_expense_entry`: Consultant timesheet and travel expense submission.
  - `e2c_005_client_acceptance`: Deliverable formal sign-off and milestone acceptance certificates.
  - `e2c_006_project_billing_invoicing`: Time-and-materials (T&M) or fixed-fee invoice generation and integration into AR.
  - `e2c_007_project_closure_lessons`: Engagement closeout, retrospective, IP harvesting, knowledge capital capture.

### 2. Roles & Governance
- `role_account_executive`: Commercial account management and deal closing.
- `role_solution_architect`: Technical scoping, estimation, and architectural proposal design.
- `role_practice_director`: Resource practice governance, revenue targets, and contract margin approvals.
- `role_engagement_manager`: Delivery execution, client stakeholder management, project profitability, and invoice review.
- `role_consultant`: Delivery execution, timesheet logging, deliverable drafting.

### 3. IT Assets
- `asset_psa_system`: Professional Services Automation platform (e.g. Certinia / FinancialForce, Kantata, SAP Cloud for Projects) managing resource utilization, staffing forecasts, and project billing rules.

## Consequences
- Expands the engine to support pure services firms alongside discrete manufacturing.
- Inherits core back-office processes (R2R financial close, S2P vendor procurement, H2R talent onboarding) from `profiles/core`.
