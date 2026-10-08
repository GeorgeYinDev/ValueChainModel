---
id: role_triage_nurse
type: role
name: Triage & Bedside Registered Nurse
department: "Nursing Operations & Emergency Services"
reports_to: role_attending_physician
approval_limit_usd: 0.0
version: 1.0.0
lod_support: [tier_2]
tags: [clinical, nursing, inpatient, triage]

attributes:
  fte_cost_annual_usd: 105000
  approval_limit_usd: 0.0
---
# Role Definition: Triage & Bedside Registered Nurse

- **Role ID**: `role_triage_nurse`
- **Department**: Nursing Operations & Emergency Services
- **Reports To**: Nurse Manager / `role_attending_physician`
- **Internal / External**: Internal

## Key Responsibilities
- Conducting clinical intake assessments, triage acuity scoring (Emergency Severity Index - ESI), and vital sign evaluation.
- Administering prescribed medications via barcode electronic medication administration records (eMAR).
- Coordinating bedside patient transitions, discharge education, and nursing handoffs.

## Required IT Systems Access
- `asset_ehr_system` (Role: Inpatient Nurse / Bedside Clinician)
