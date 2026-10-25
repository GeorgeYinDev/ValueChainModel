---
id: asset_core_banking_platform
type: asset
name: Core Banking & Subledger Platform
version: 1.0.0
asset_type: it_application
status: operational
lod_support: [tier_2, tier_3]
tags: [core_banking, deposits, loan_subledger, temenos, fis, payments]

attributes:
  vendor: "Temenos Transact / FIS Modern Banking Platform"
  sla_uptime_percent: 99.995
  capacity_max_tps: 2500.0
  integration_endpoints: ["asset_aml_kyc_screening_engine", "asset_loan_origination_system", "asset_payment_gateway", "asset_erp_system"]
---
# Core Banking & Subledger Platform

System of record for demand deposit accounts (DDA), commercial loan facilities, interest accrual schedules, real-time account balances, and daily subledger-to-General-Ledger postings.
