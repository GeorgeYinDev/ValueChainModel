---
id: role_treasury_operations_officer
type: role
name: Treasury & Settlement Operations Officer
department: "Treasury & Banking Operations"
reports_to: role_finance_controller
approval_limit_usd: 5000000.0
version: 1.0.0
lod_support: [tier_2]
tags: [treasury, settlement, fedwire, ach, core_operations]

attributes:
  fte_cost_annual_usd: 165000
  approval_limit_usd: 5000000.0
---
# Role Definition: Treasury & Settlement Operations Officer

- **Role ID**: `role_treasury_operations_officer`
- **Department**: Treasury & Banking Operations
- **Reports To**: `role_finance_controller`
- **Internal / External**: Internal

## Key Responsibilities
- Accountable for core deposit account activation, treasury entitlement verification, and intraday liquidity positioning.
- Authorizes outbound Fedwire and ACH principal funding disbursements up to $5,000,000 USD under dual-control treasury protocols.
- Oversees daily nostros, clearing suspense accounts, and automated loan/deposit subledger feeds into the General Ledger.

## Required IT Systems Access
- `asset_core_banking_platform` (Role: Treasury Settlement Approver)
- `asset_payment_gateway` (Role: Fedwire / SWIFT Release Officer)
- `asset_erp_system` (Role: Treasury Subledger Controller)
