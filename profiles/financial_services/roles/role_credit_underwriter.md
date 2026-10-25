---
id: role_credit_underwriter
type: role
name: Commercial Credit Underwriter
department: "Commercial Credit Risk Underwriting"
reports_to: role_chief_credit_officer
approval_limit_usd: 500000.0
version: 1.0.0
lod_support: [tier_2]
tags: [underwriting, credit_risk, pd_lgd, covenants, lending]

attributes:
  fte_cost_annual_usd: 145000
  approval_limit_usd: 500000.0
---
# Role Definition: Commercial Credit Underwriter

- **Role ID**: `role_credit_underwriter`
- **Department**: Commercial Credit Risk Underwriting
- **Reports To**: `role_chief_credit_officer`
- **Internal / External**: Internal

## Key Responsibilities
- Performs financial statement spreading, cash-flow stress testing, Debt Service Coverage Ratio (DSCR) analysis, and quantitative PD/LGD risk rating assignment.
- Conducts periodic borrower financial covenant reviews and calculates ASC 326 Current Expected Credit Loss (CECL) reserve adjustments.
- Holds delegated underwriting sign-off authority for standard commercial credit renewals up to $500,000 USD.

## Required IT Systems Access
- `asset_loan_origination_system` (Role: Senior Credit Underwriter)
- `asset_core_banking_platform` (Role: Credit Exposure & Subledger Inquiry)
