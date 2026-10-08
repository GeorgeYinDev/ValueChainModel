---
id: role_patient
type: role
name: Patient / Healthcare Consumer
department: "External Beneficiary"
reports_to: null
approval_limit_usd: 0.0
version: 1.0.0
lod_support: [tier_2]
tags: [external, patient, consumer, guarantor]

attributes:
  fte_cost_annual_usd: 0
  approval_limit_usd: 0.0
---
# Role Definition: Patient / Healthcare Consumer

- **Role ID**: `role_patient`
- **Department**: External Beneficiary
- **Reports To**: N/A
- **Internal / External**: External

## Key Responsibilities
- Participating in clinical decision-making, providing medical history, and consenting to treatment regimens.
- Authorizing insurance benefit assignment and acting as financial guarantor for patient balances.
- Settling out-of-pocket patient responsibility (deductibles, copayments, coinsurance).

## Required IT Systems Access
- `asset_ehr_system` (Role: Patient Portal Consumer / MyChart)
