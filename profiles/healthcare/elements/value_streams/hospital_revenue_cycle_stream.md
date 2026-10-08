---
id: hospital_revenue_cycle_stream
type: value_stream
name: Hospital Revenue Cycle & Cash Reconciliation Value Stream
version: 1.0.0
lifecycles: [RCM]
lod_support: [tier_1, tier_2, tier_3]
tags: [value_stream, rcm, billing, cash_posting, finance, healthcare]

raci:
  responsible: [role_medical_coder, role_billing_specialist]
  accountable: [role_rcm_director]
  consulted: [role_attending_physician]
  informed: [role_finance_controller]

daci:
  driver: [role_medical_coder]
  approver: [role_rcm_director]
  contributor: [role_billing_specialist]
  informed: [role_finance_controller]

attributes:
  baseline_cycle_time_hours: 218.0
  baseline_cost_per_unit: 335.0
  automation_rate: 0.72
  error_rate: 0.05
  sla_hours: 240.0

asset_dependencies:
  - asset_rcm_clearinghouse
  - asset_ehr_system
  - asset_erp_system

graph_relations:
  - relation: governed_by
    target: clinical_prior_auth_medical_necessity_policy
    weight: 1.0
  - relation: feeds_into
    target: r2r_001_journal_entry_recording
    weight: 1.0
---

# Value Stream: Hospital Revenue Cycle & Cash Reconciliation (RCM)

## Executive Summary
Translates clinical inpatient and outpatient encounters into reimbursable claims, governs electronic transaction exchange with clearinghouses and payers, recovers denied revenue, and reconciles electronic funds transfers into corporate General Ledger accounting.

## 1. Strategic Outcomes (Tier 1 - Executive Level)
- **Accelerate Cash Liquidity & DSO Control**: Target net Days in A/R <= 38.0 days through automated claim scrubbing and electronic remittance posting.
- **Minimize Revenue Leakage**: Maintain Initial Claim Denial Rate <= 5.0% and achieve clean claim rates > 95%.
- **Core Financial Triad Integration**: Direct feed from cash posting (`rcm_006`) into General Ledger journal voucher recording (`r2r_001_journal_entry_recording`).

## 2. Included Steps & RACI Summary (Tier 2 - Process Architect Level)
1. `rcm_001_charge_capture_coding` - Clinical Charge Capture & ICD-10 Coding
2. `rcm_002_claim_scrubbing_submission` - EDI 837 Claim Transmission
3. `rcm_003_payer_adjudication_remittance` - EDI 835 Remittance Advice Ingestion
4. `rcm_004_denial_management_appeals` - Root-Cause Denial Appeals
5. `rcm_005_patient_billing_collections` - Patient Responsibility Invoicing
6. `rcm_006_cash_posting_reconciliation` - Bank Reconciliation & GL Journal Posting

## 3. Systems Architecture (Tier 3 - Systems Engineer Level)
- **Clearinghouse & EDI Gateway**: Revenue Cycle Platform (`asset_rcm_clearinghouse`).
- **Core Financial System**: Enterprise Resource Planning General Ledger (`asset_erp_system`).
