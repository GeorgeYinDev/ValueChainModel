---
id: role_kyc_aml_analyst
type: role
name: KYC & AML Compliance Analyst
department: "Financial Crime Compliance Operations"
reports_to: role_bsa_compliance_officer
approval_limit_usd: 50000.0
version: 1.0.0
lod_support: [tier_2]
tags: [kyc, aml, cip, ubo, sanctions, compliance]

attributes:
  fte_cost_annual_usd: 105000
  approval_limit_usd: 50000.0
---
# Role Definition: KYC & AML Compliance Analyst

- **Role ID**: `role_kyc_aml_analyst`
- **Department**: Financial Crime Compliance Operations
- **Reports To**: `role_bsa_compliance_officer`
- **Internal / External**: Internal

## Key Responsibilities
- Executes Customer Identification Program (CIP) documentary and non-documentary verification and FinCEN Ultimate Beneficial Ownership (UBO >= 25%) validation.
- Investigates and dispositions L1/L2 OFAC sanctions, Politically Exposed Person (PEP), and adverse media screening alerts.
- Compiles Enhanced Due Diligence (EDD) dossiers and Source of Wealth (SoW) corroboration packages for high-risk clients.

## Required IT Systems Access
- `asset_aml_kyc_screening_engine` (Role: Financial Crime Investigator)
- `asset_core_banking_platform` (Role: Read-Only Customer Master Inquiry)
