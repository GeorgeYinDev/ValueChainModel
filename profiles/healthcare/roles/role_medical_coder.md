---
id: role_medical_coder
type: role
name: Certified Medical Coder
department: "Health Information Management (HIM)"
reports_to: role_rcm_director
approval_limit_usd: 15000.0
version: 1.0.0
lod_support: [tier_2]
tags: [coding, him, icd10, cpt, rcm]

attributes:
  fte_cost_annual_usd: 72000
  approval_limit_usd: 15000.0
---
# Role Definition: Certified Medical Coder

- **Role ID**: `role_medical_coder`
- **Department**: Health Information Management (HIM)
- **Reports To**: `role_rcm_director`
- **Internal / External**: Internal

## Key Responsibilities
- Reviewing clinical notes, provider documentation, operative reports, and discharge summaries.
- Assigning standardized ICD-10-CM/PCS diagnosis/procedure codes and CPT/HCPCS modifier combinations.
- Resolving National Correct Coding Initiative (NCCI) edits and clinical documentation queries (CDI).

## Required IT Systems Access
- `asset_ehr_system` (Role: HIM Medical Coding Specialist)
- `asset_rcm_clearinghouse` (Role: Claim Scrubber & Coding Validation)
