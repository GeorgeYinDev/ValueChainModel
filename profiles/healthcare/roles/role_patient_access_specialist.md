---
id: role_patient_access_specialist
type: role
name: Patient Access Specialist
department: "Patient Access & Front Revenue Cycle"
reports_to: role_rcm_director
approval_limit_usd: 5000.0
version: 1.0.0
lod_support: [tier_2]
tags: [front_rcm, scheduling, registration, eligibility]

attributes:
  fte_cost_annual_usd: 58000
  approval_limit_usd: 5000.0
---
# Role Definition: Patient Access Specialist

- **Role ID**: `role_patient_access_specialist`
- **Department**: Patient Access & Front Revenue Cycle
- **Reports To**: `role_rcm_director`
- **Internal / External**: Internal

## Key Responsibilities
- Capturing demographic, contact, and guarantor information during patient intake and scheduling.
- Executing real-time electronic insurance eligibility verification (EDI 270/271) and initiating prior-authorization requests (EDI 278).
- Collecting point-of-service copayments, coinsurance estimates, and initiating financial clearance.

## Required IT Systems Access
- `asset_ehr_system` (Role: Registration & Patient Access Registrar)
- `asset_rcm_clearinghouse` (Role: Real-time Eligibility & Clearance Specialist)
