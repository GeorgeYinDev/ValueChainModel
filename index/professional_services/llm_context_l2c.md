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

