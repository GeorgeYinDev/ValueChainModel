---
id: role_attending_physician
type: role
name: Attending Physician
department: "Clinical Inpatient Medicine"
reports_to: role_rcm_director
approval_limit_usd: 10000.0
version: 1.0.0
lod_support: [tier_2]
tags: [clinical, physician, provider, medical]

attributes:
  fte_cost_annual_usd: 320000
  approval_limit_usd: 10000.0
---
# Role Definition: Attending Physician

- **Role ID**: `role_attending_physician`
- **Department**: Clinical Inpatient Medicine
- **Reports To**: Chief Medical Officer / Clinical Department Chair
- **Internal / External**: Internal

## Key Responsibilities
- Accountable for medical decision-making, patient diagnoses, and clinical order entry (CPOE).
- Authorizing medication administration regimens, diagnostic testing plans, and patient discharge orders.
- Clinical documentation in the electronic health record to ensure accurate ICD-10 medical coding and medical necessity substantiation.

## Required IT Systems Access
- `asset_ehr_system` (Role: Ordering Provider / Clinical Attending)
- `asset_pacs_lis_system` (Role: Diagnostic Order Reviewer)
