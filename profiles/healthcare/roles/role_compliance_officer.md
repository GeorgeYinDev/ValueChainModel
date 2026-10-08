---
id: role_compliance_officer
type: role
name: Healthcare Compliance & Privacy Officer
department: "Corporate Integrity & Regulatory Compliance"
reports_to: role_internal_auditor
approval_limit_usd: 50000.0
version: 1.0.0
lod_support: [tier_2]
tags: [compliance, hipaa, privacy, regulatory, healthcare]

attributes:
  fte_cost_annual_usd: 175000
  approval_limit_usd: 50000.0
---
# Role Definition: Healthcare Compliance & Privacy Officer

- **Role ID**: `role_compliance_officer`
- **Department**: Corporate Integrity & Regulatory Compliance
- **Reports To**: `role_internal_auditor` / Audit Committee
- **Internal / External**: Internal

## Key Responsibilities
- Enforcing compliance with HIPAA Privacy & Security Rules, EMTALA, Stark Law, and anti-kickback statutes.
- Conducting regular audits of protected health information (PHI) disclosures, medical necessity documentation, and billing compliance.
- Investigating privacy incidents and authorizing breach remediation protocols.

## Required IT Systems Access
- `asset_ehr_system` (Role: Compliance & Access Audit Officer)
- `asset_rcm_clearinghouse` (Role: Billing Compliance Auditor)
