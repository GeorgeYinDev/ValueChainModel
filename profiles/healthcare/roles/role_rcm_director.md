---
id: role_rcm_director
type: role
name: Revenue Cycle Management Director
department: "Patient Financial Services & Revenue Cycle"
reports_to: role_finance_controller
approval_limit_usd: 250000.0
version: 1.0.0
lod_support: [tier_2]
tags: [rcm, revenue, billing, management]

attributes:
  fte_cost_annual_usd: 210000
  approval_limit_usd: 250000.0
---
# Role Definition: Revenue Cycle Management Director

- **Role ID**: `role_rcm_director`
- **Department**: Patient Financial Services & Revenue Cycle
- **Reports To**: `role_finance_controller`
- **Internal / External**: Internal

## Key Responsibilities
- Accountable for enterprise health system revenue cycle performance, cash collections, and Days in A/R.
- Authorizing billing adjustments, contractual allowance write-offs, and charity care write-downs up to $250,000 USD.
- Managing payer contract variances, commercial denial recovery workflows, and electronic clearinghouse performance.

## Required IT Systems Access
- `asset_rcm_clearinghouse` (Role: Executive RCM Director / Analytics)
- `asset_ehr_system` (Role: Revenue Cycle Administrator)
- `asset_erp_system` (Role: Healthcare Financial Reporting)
