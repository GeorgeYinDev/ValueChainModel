---
id: role_loan_servicing_specialist
type: role
name: Loan Closing & Servicing Specialist
department: "Commercial Loan Operations & Servicing"
reports_to: role_treasury_operations_officer
approval_limit_usd: 250000.0
version: 1.0.0
lod_support: [tier_2]
tags: [loan_servicing, collateral, lien, boarding, operations]

attributes:
  fte_cost_annual_usd: 95000
  approval_limit_usd: 250000.0
---
# Role Definition: Loan Closing & Servicing Specialist

- **Role ID**: `role_loan_servicing_specialist`
- **Department**: Commercial Loan Operations & Servicing
- **Reports To**: `role_treasury_operations_officer`
- **Internal / External**: Internal

## Key Responsibilities
- Verifies independent collateral appraisals, insurance certificates, and UCC-1 / mortgage lien filings prior to loan closing.
- Boards approved credit facilities, amortization schedules, and SOFR rate-reset rules into `asset_core_banking_platform`.
- Administers scheduled principal and interest (P&I) billing, escrow disbursements, and payoff lien releases.

## Required IT Systems Access
- `asset_core_banking_platform` (Role: Loan Servicing Administrator)
- `asset_loan_origination_system` (Role: Closing & Collateral Specialist)
