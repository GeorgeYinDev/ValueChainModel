---
id: role_chief_credit_officer
type: role
name: Chief Credit Officer (CCO)
department: "Enterprise Credit Risk Management"
reports_to: role_finance_controller
approval_limit_usd: 25000000.0
version: 1.0.0
lod_support: [tier_2]
tags: [cco, credit_committee, risk_governance, workout, executive]

attributes:
  fte_cost_annual_usd: 295000
  approval_limit_usd: 25000000.0
---
# Role Definition: Chief Credit Officer (CCO)

- **Role ID**: `role_chief_credit_officer`
- **Department**: Enterprise Credit Risk Management
- **Reports To**: `role_finance_controller`
- **Internal / External**: Internal

## Key Responsibilities
- Chairs the Enterprise Credit Committee and holds ultimate credit approval authority up to $25,000,000 USD for commercial and institutional lending facilities.
- Governs Basel III credit risk appetite, Single Obligor Limits, industry concentration caps, and collateral LTV standards.
- Approves non-accrual classifications, troubled debt restructurings (TDR), and commercial loan charge-offs.

## Required IT Systems Access
- `asset_loan_origination_system` (Role: Credit Committee Chair / Executive Approver)
- `asset_core_banking_platform` (Role: Portfolio Risk Executive)
- `asset_erp_system` (Role: CECL Allowance Sign-Off)
