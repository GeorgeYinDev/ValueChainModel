---
id: role_finance_controller
type: role
name: "Finance Controller"
department: "Corporate Finance & Treasury"
approval_limit_usd: 999999999.0
---
# Role Definition: Finance Controller

- **Role ID**: `role_finance_controller`
- **Department**: Corporate Finance & Treasury
- **Reports To**: Chief Financial Officer (CFO)
- **Internal / External**: Internal

## Key Responsibilities
- Governance over corporate spending controls, Segregation of Duties (SoD), and financial delegation of authority.
- Authorize payment disbursement runs prepared by Accounts Payable.
- Monitor cash flow, working capital impacts, and early payment discount optimization.
- Accountable for internal audit compliance and general ledger posting accuracy.

## Decision Rights & Financial Approval Limits
- **Disbursement Approval Limit**: Unlimited (with dual signoff above $1,000,000 USD)
- **Capital Expenditure Sign-off Limit**: Up to $1,000,000 USD

## Required IT Systems Access
- `asset_erp_system` (Role: Finance Controller / General Ledger Superuser)
- `asset_payment_gateway` (Role: Authorized Dual Signer)
