---
id: role_bsa_compliance_officer
type: role
name: BSA / AML Chief Compliance Officer
department: "Enterprise Risk & Regulatory Compliance"
reports_to: role_finance_controller
approval_limit_usd: 1000000.0
version: 1.0.0
lod_support: [tier_2]
tags: [bsa, aml, ofac, edd, compliance_officer, banking]

attributes:
  fte_cost_annual_usd: 235000
  approval_limit_usd: 1000000.0
---
# Role Definition: BSA / AML Chief Compliance Officer

- **Role ID**: `role_bsa_compliance_officer`
- **Department**: Enterprise Risk & Regulatory Compliance
- **Reports To**: `role_finance_controller`
- **Internal / External**: Internal

## Key Responsibilities
- Designated statutory Bank Secrecy Act (BSA) and OFAC Compliance Officer accountable for financial crime governance.
- Holds sole sign-off authority on Enhanced Due Diligence (EDD) onboarding for high-risk entities, PEPs, and correspondent accounts.
- Authorizes Suspicious Activity Report (SAR) filings, OFAC asset freeze directives, and regulatory risk policy exceptions up to $1,000,000 USD.

## Required IT Systems Access
- `asset_aml_kyc_screening_engine` (Role: BSA Officer / Final Approver)
- `asset_core_banking_platform` (Role: Compliance Hold & Restriction Controller)
