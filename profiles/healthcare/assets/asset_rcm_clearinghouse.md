---
id: asset_rcm_clearinghouse
type: asset
name: Revenue Cycle EDI Clearinghouse & Billing Platform
version: 1.0.0
asset_type: it_application
status: operational
lod_support: [tier_2, tier_3]
tags: [rcm, edi, clearinghouse, billing, claims]

attributes:
  vendor: "Waystar / Change Healthcare / Availity"
  sla_uptime_percent: 99.95
  capacity_max_tps: 600.0
  integration_endpoints: ["asset_ehr_system", "asset_erp_system"]
---
# Revenue Cycle EDI Clearinghouse & Billing Platform

National healthcare transaction clearinghouse managing HIPAA EDI ANSI X12 standards (EDI 270/271 eligibility, EDI 278 prior authorization, EDI 837 claim submission, and EDI 835 remittance advice autoposting).
