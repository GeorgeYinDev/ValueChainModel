---
id: kpi_kyc_onboarding_time_to_yes
type: kpi_metric
name: "KYC Client Onboarding Time-to-Yes"
version: "1.0.0"
lifecycles: ["C2A"]
lod_support: ["tier_1", "tier_2"]
tags: ["kpi", "c2a", "kyc", "onboarding", "cycle_time", "banking"]

kpi_metric_details:
  formula: "Sum(Timestamp_Core_Account_Activated - Timestamp_Application_Intake) / Total_Onboarded_Clients"
  target: "<= 36.0 Hours"
  owner: "role_bsa_compliance_officer"
  unit: "Hours"

graph_relations:
  - relation: impacted_by
    target: c2a_004_enhanced_due_diligence_compliance
    weight: 1.0
  - relation: impacted_by
    target: c2a_005_account_provisioning_core_activation
    weight: 1.0
---

# KPI: KYC Client Onboarding Time-to-Yes

Measures the average elapsed cycle time from initial institutional or retail client application intake (`c2a_001`) through CIP/UBO verification, sanctions clearance, and Enhanced Due Diligence to active core deposit account provisioning (`c2a_005`).
