---
id: role_relationship_manager
type: role
name: Commercial Relationship Manager
department: "Commercial & Institutional Banking"
reports_to: role_chief_credit_officer
approval_limit_usd: 100000.0
version: 1.0.0
lod_support: [tier_2]
tags: [front_office, relationship_management, origination, banking]

attributes:
  fte_cost_annual_usd: 185000
  approval_limit_usd: 100000.0
---
# Role Definition: Commercial Relationship Manager

- **Role ID**: `role_relationship_manager`
- **Department**: Commercial & Institutional Banking
- **Reports To**: `role_chief_credit_officer`
- **Internal / External**: Internal

## Key Responsibilities
- Primary front-office coverage officer for commercial and institutional banking clients.
- Captures initial deposit onboarding applications, corporate hierarchy disclosures, and credit facility requests.
- Structures commercial loan term sheets and coordinates borrower financial covenants and pricing within delegated $100,000 USD fee/pricing authority.

## Required IT Systems Access
- `asset_crm_system` (Role: Commercial Banking Coverage)
- `asset_loan_origination_system` (Role: Loan Deal Sponsor)
- `asset_aml_kyc_screening_engine` (Role: Front-Office KYC Sponsor)
