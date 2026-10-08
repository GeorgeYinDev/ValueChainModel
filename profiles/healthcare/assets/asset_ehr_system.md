---
id: asset_ehr_system
type: asset
name: Electronic Health Record Platform (EHR)
version: 1.0.0
asset_type: it_application
status: operational
lod_support: [tier_2, tier_3]
tags: [clinical, ehr, cpoe, emar, epic, cerner]

attributes:
  vendor: "Epic Systems / Oracle Health"
  sla_uptime_percent: 99.99
  capacity_max_tps: 850.0
  integration_endpoints: ["asset_rcm_clearinghouse", "asset_pacs_lis_system", "asset_erp_system"]
---
# Electronic Health Record Platform (EHR)

Centralized clinical information backbone managing longitudinal patient health records, inpatient bed tracking, computerized provider order entry (CPOE), electronic medication administration (eMAR), and clinical documentation.
