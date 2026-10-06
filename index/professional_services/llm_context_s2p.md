# System Prompt: LLM Context Blueprint for Business Lifecycle [Source to Pay Lifecycle]

> Profile: `professional_services` | Lifecycle ID: `S2P` | Version: `1.0.0` | Source Layer: `core`
> Description: End-to-end procurement lifecycle from spend identification and vendor sourcing through contract execution, PO issuance, invoice processing, and financial settlement.

## Milestone Process Sequence
- **Step 1**: `s2p_001_spend_analysis_need_id` (Spend Analysis & Need Identification)
- **Step 2**: `s2p_002_supplier_discovery_qualification` (Supplier Discovery & Qualification)
- **Step 3**: `s2p_003_sourcing_rfx_auction` (Strategic Sourcing & RFx Execution)
- **Step 4**: `s2p_004_contracting_sla_negotiation` (Contracting & SLA Negotiation)
- **Step 5**: `s2p_005_purchase_requisition_po` (Purchase Requisition & PO Issuance)
- **Step 6**: `s2p_006_goods_services_receipt` (Goods & Services Receipt Verification)
- **Step 7**: `s2p_007_invoice_verification_matching` (Invoice 3-Way Matching & Exception Handling)
- **Step 8**: `s2p_008_payment_settlement_disbursement` (Payment Settlement & Disbursement)

## Key Performance Indicators (KPIs)
- `s2p_cycle_time_days`
- `po_automation_percentage`
- `first_pass_match_rate`
- `early_payment_discount_capture`

## Active Value Chain Elements Knowledge Base

### [Procure to Pay (P2P) Operational Value Stream] (`procure_to_pay_stream`) [Layer: `core`]
- **Type**: `value_stream` | **Tags**: `value_stream, procure_to_pay, p2p`
- **RACI**: `{"responsible": ["role_procurement_specialist", "role_accounts_payable_clerk"], "accountable": ["role_finance_controller"], "consulted": ["role_category_manager"], "informed": ["role_supplier"]}`
- **Assets**: `asset_erp_system, asset_eprocurement_portal, asset_payment_gateway`

# Value Stream: Procure to Pay (P2P)

## Executive Summary
Encompasses the transactional execution lifecycle from purchase requisition approval and PO dispatch through receiving, 3-way invoice matching, and final payment settlement (Steps 005 - 008).

## 1. Strategic Outcomes (Tier 1)
- Operational procurement efficiency and SLA compliance.
- 100% 3-way invoice match accuracy and discount capture.
- Treasury cash management and disbursement automation.

## 2. Included Steps & RACI Summary (Tier 2)
1. `s2p_005_purchase_requisition_po`
2. `s2p_006_goods_services_receipt`
3. `s2p_007_invoice_verification_matching`
4. `s2p_008_payment_settlement_disbursement`
---

### [Spend Analysis & Need Identification] (`s2p_001_spend_analysis_need_id`) [Layer: `core`]
- **Type**: `process_step` | **Tags**: `procurement, analytics, requisition`
- **RACI**: `{"responsible": ["role_procurement_specialist"], "accountable": ["role_category_manager"], "consulted": ["role_finance_controller"], "informed": ["role_supplier"]}`
- **Assets**: `asset_eprocurement_portal, asset_erp_system`

# Process Step: Spend Analysis & Need Identification

## Executive Summary
Initiates the Source-to-Pay lifecycle by aggregating historical spend data, identifying business procurement requirements, and creating initial demand requests.

## 1. Strategic Intent & Outcome (Tier 1 - Executive Level)
- **Business Value**: Eliminates maverick spending, consolidates demand leverage, and aligns sourcing projects with budgetary constraints.
- **Strategic Alignment**: Directly supports corporate EBITDA optimization and working capital management.
- **Risk Exposure**: Inaccurate demand forecasting or unapproved off-contract purchasing.

## 2. Operational Workflow & RACI (Tier 2 - Process Architect Level)
- **Workflow Sequence**:
  1. Business unit submits business need or automated reorder threshold triggers requisition.
  2. Procurement Analytics engine matches demand against existing preferred supplier catalogs.
  3. Requisition details (UNSPSC commodity code, budget center, target lead time) validated.
- **RACI Matrix**:
  - **Responsible**: `role_procurement_specialist`
  - **Accountable**: `role_category_manager`
  - **Consulted**: `role_finance_controller`
  - **Informed**: `role_supplier`
- **SLA**: 24.0 Hours.

## 3. Systems Math & Simulation Parameters (Tier 3 - Simulation Engineer Level)
```math
\text{Need Identification Latency} = \text{Baseline Cycle Time} \times \left(1 + \frac{\text{Unmapped Spend Ratio}}{\text{Automation Rate}}\right)
```
- **Primary Data Entity**: Purchase Requisition Draft (`PR_DRAFT_v1`).
- **Asset Load**: Interrogates ERP Master Ledger via `asset_eprocurement_portal`.
---

### [Supplier Discovery & Qualification] (`s2p_002_supplier_discovery_qualification`) [Layer: `core`]
- **Type**: `process_step` | **Tags**: `vendor_management, compliance, risk`
- **RACI**: `{"responsible": ["role_procurement_specialist"], "accountable": ["role_category_manager"], "consulted": ["role_finance_controller"], "informed": ["role_supplier"]}`
- **Assets**: `asset_eprocurement_portal`

# Process Step: Supplier Discovery & Qualification

## Executive Summary
Evaluates potential suppliers for financial stability, ESG compliance, regulatory sanctions, and operational capability prior to bid participation.

## 1. Strategic Intent & Outcome (Tier 1 - Executive Level)
- **Business Value**: Mitigates supply chain disruption, reputational risk, and regulatory non-compliance.
- **Strategic Alignment**: Ensures supplier diversity targets and ESG corporate governance metrics are met.
- **Risk Exposure**: Vendor bankruptcy, PEP/Sanction violations, or single-source dependency.

## 2. Operational Workflow & RACI (Tier 2 - Process Architect Level)
- **Workflow Sequence**:
  1. Vendor submits RFI (Request for Information) and compliance documentation via supplier portal.
  2. Financial risk scoring, credit checks, and Sanctions screening automated via third-party APIs.
  3. Category Manager reviews qualification score and admits vendor to approved master pool.
- **RACI Matrix**:
  - **Responsible**: `role_procurement_specialist`
  - **Accountable**: `role_category_manager`
  - **Consulted**: `role_finance_controller`
  - **Informed**: `role_supplier`
- **SLA**: 72.0 Hours.

## 3. Systems Math & Simulation Parameters (Tier 3 - Simulation Engineer Level)
```math
\text{Qualification Time} = \text{Baseline Cycle Time} + \left(1 - \text{Automation Rate}\right) \times \text{Vendor Risk Complexity Factor} \times 24.0
```
- **Primary Data Entity**: Qualified Vendor Record (`VENDOR_QUAL_v1`).
- **Asset Load**: `asset_eprocurement_portal`.
---

### [Strategic Sourcing & RFx Execution] (`s2p_003_sourcing_rfx_auction`) [Layer: `core`]
- **Type**: `process_step` | **Tags**: `sourcing, rfp, rfq, negotiation`
- **RACI**: `{"responsible": ["role_procurement_specialist"], "accountable": ["role_category_manager"], "consulted": ["role_finance_controller"], "informed": ["role_supplier"]}`
- **Assets**: `asset_eprocurement_portal`

# Process Step: Strategic Sourcing & RFx Execution

## Executive Summary
Executes competitive bidding events (RFP, RFQ, e-Auctions) to negotiate optimal commercial terms, pricing structures, and SLA commitments.

## 1. Strategic Intent & Outcome (Tier 1 - Executive Level)
- **Business Value**: Drives competitive cost reduction and secures favorable pricing and delivery terms.
- **Strategic Alignment**: Directly achieves annual procurement savings milestones.
- **Risk Exposure**: Uncompetitive bidding, vendor collusion, or flawed bid evaluation criteria.

## 2. Operational Workflow & RACI (Tier 2 - Process Architect Level)
- **Workflow Sequence**:
  1. RFx payload configured with technical specifications and pricing breakdown requirements.
  2. Bids invited from qualified vendors on `asset_eprocurement_portal`.
  3. Weighted scoring algorithm evaluates commercial proposals and selects awarded vendor.
- **RACI Matrix**:
  - **Responsible**: `role_procurement_specialist`
  - **Accountable**: `role_category_manager`
  - **Consulted**: `role_finance_controller`
  - **Informed**: `role_supplier`
- **SLA**: 120.0 Hours.

## 3. Systems Math & Simulation Parameters (Tier 3 - Simulation Engineer Level)
```math
\text{Sourcing Savings} = \text{Baseline Spend} \times \left(\text{Competition Index} \times 0.08\right)
```
- **Primary Data Entity**: Sourcing Event Award (`RFX_AWARD_v1`).
- **Asset Load**: `asset_eprocurement_portal`.
---

### [Contracting & SLA Negotiation] (`s2p_004_contracting_sla_negotiation`) [Layer: `core`]
- **Type**: `process_step` | **Tags**: `contracting, legal, slas`
- **RACI**: `{"responsible": ["role_category_manager"], "accountable": ["role_category_manager"], "consulted": ["role_finance_controller"], "informed": ["role_supplier"]}`
- **Assets**: `asset_eprocurement_portal, asset_erp_system`

# Process Step: Contracting & SLA Negotiation

## Executive Summary
Drafts, negotiates, and executes legally binding commercial contracts, Master Services Agreements (MSAs), and SLA penalty structures.

## 1. Strategic Intent & Outcome (Tier 1 - Executive Level)
- **Business Value**: Enforces legal protections, IP ownership, liability caps, and guaranteed performance metrics.
- **Strategic Alignment**: Ensures governance, risk management, and compliance (GRC) policies are bound.
- **Risk Exposure**: Unfavorable liability clauses, ambiguous SLA penalties, or contract lifecycle leakage.

## 2. Operational Workflow & RACI (Tier 2 - Process Architect Level)
- **Workflow Sequence**:
  1. Standard contract template generated from clause library in `asset_eprocurement_portal`.
  2. Redlining and legal reviews executed between legal counsel and vendor.
  3. Digital signatures captured and contract master published to ERP.
- **RACI Matrix**:
  - **Responsible**: `role_category_manager`
  - **Accountable**: `role_category_manager`
  - **Consulted**: `role_finance_controller`
  - **Informed**: `role_supplier`
- **SLA**: 96.0 Hours.

## 3. Systems Math & Simulation Parameters (Tier 3 - Simulation Engineer Level)
```math
\text{Contract Execution Latency} = \text{Baseline Cycle Time} \times \left(1 + \frac{\text{Redline Iterations}}{\text{Automation Rate}}\right)
```
- **Primary Data Entity**: Master Agreement Record (`CONTRACT_MASTER_v1`).
- **Asset Load**: `asset_eprocurement_portal`, `asset_erp_system`.
---

### [Purchase Requisition & PO Issuance] (`s2p_005_purchase_requisition_po`) [Layer: `core`]
- **Type**: `process_step` | **Tags**: `purchasing, po, requisition, approval`
- **RACI**: `{"responsible": ["role_procurement_specialist"], "accountable": ["role_category_manager"], "consulted": ["role_finance_controller"], "informed": ["role_supplier"]}`
- **Assets**: `asset_eprocurement_portal, asset_erp_system`

# Process Step: Purchase Requisition & PO Issuance

## Executive Summary
Validates financial budget availability, routes Purchase Requisitions (PR) through approval matrix workflows, and dispatches official Purchase Orders (PO) to vendors.

## 1. Strategic Intent & Outcome (Tier 1 - Executive Level)
- **Business Value**: Enforces pre-commitment financial control, budget verification, and purchasing governance.
- **Strategic Alignment**: Prevents unbudgeted spending and enforces contractually negotiated pricing.
- **Risk Exposure**: Budget overruns, unauthorized spending limits, or manual PO dispatch delays.

## 2. Operational Workflow & RACI (Tier 2 - Process Architect Level)
- **Workflow Sequence**:
  1. Business user submits PR; automated budget check against ERP General Ledger performed.
  2. PR routed to appropriate approvers according to spending limit thresholds.
  3. Approved PR automatically converted to PO and dispatched via EDI/Portal to supplier.
- **RACI Matrix**:
  - **Responsible**: `role_procurement_specialist`
  - **Accountable**: `role_category_manager`
  - **Consulted**: `role_finance_controller`
  - **Informed**: `role_supplier`
- **SLA**: 12.0 Hours.

## 3. Systems Math & Simulation Parameters (Tier 3 - Simulation Engineer Level)
```math
\text{PO Cycle Time} = \text{Baseline Cycle Time} \times \left(1 - \text{Automation Rate}\right) + \text{Approval Delay}
```
- **Primary Data Entity**: Purchase Order (`PO_RECORD_v1`).
- **Asset Load**: `asset_erp_system`, `asset_eprocurement_portal`.
---

### [Goods & Services Receipt Verification] (`s2p_006_goods_services_receipt`) [Layer: `core`]
- **Type**: `process_step` | **Tags**: `receiving, inventory, quality, grn`
- **RACI**: `{"responsible": ["role_procurement_specialist"], "accountable": ["role_category_manager"], "consulted": ["role_accounts_payable_clerk"], "informed": ["role_supplier"]}`
- **Assets**: `asset_erp_system`

# Process Step: Goods & Services Receipt Verification

## Executive Summary
Verifies physical delivery of goods or completion of service deliverables, logs quality inspection results, and generates Goods Receipt Notes (GRN) in ERP.

## 1. Strategic Intent & Outcome (Tier 1 - Executive Level)
- **Business Value**: Ensures pay-for-performance discipline and confirms fulfillment prior to financial disbursement.
- **Strategic Alignment**: Safeguards inventory accuracy and working capital valuation.
- **Risk Exposure**: Damaged goods, short shipments, unverified service completion, or ghost inventory.

## 2. Operational Workflow & RACI (Tier 2 - Process Architect Level)
- **Workflow Sequence**:
  1. Receiving dock scans shipment barcode or service owner confirms deliverable milestone completion.
  2. Inspection team checks quantity and quality specification against PO parameters.
  3. Goods Receipt Note (GRN) posted to ERP; inventory records incremented.
- **RACI Matrix**:
  - **Responsible**: `role_procurement_specialist`
  - **Accountable**: `role_category_manager`
  - **Consulted**: `role_accounts_payable_clerk`
  - **Informed**: `role_supplier`
- **SLA**: 12.0 Hours.

## 3. Systems Math & Simulation Parameters (Tier 3 - Simulation Engineer Level)
```math
\text{Receipt Processing Time} = \text{Baseline Cycle Time} \times \left(1 + \text{Inspection Discrepancy Rate}\right)
```
- **Primary Data Entity**: Goods Receipt Record (`GRN_RECORD_v1`).
- **Asset Load**: `asset_erp_system`.
---

### [Invoice 3-Way Matching & Exception Handling] (`s2p_007_invoice_verification_matching`) [Layer: `core`]
- **Type**: `process_step` | **Tags**: `invoicing, ap, matching, finance`
- **RACI**: `{"responsible": ["role_accounts_payable_clerk"], "accountable": ["role_finance_controller"], "consulted": ["role_procurement_specialist"], "informed": ["role_supplier"]}`
- **Assets**: `asset_erp_system, asset_eprocurement_portal`

# Process Step: Invoice 3-Way Matching & Exception Handling

## Executive Summary
Ingests vendor invoices, executes automated 3-way matching (PO, GRN, Invoice line items), and routes price/quantity exceptions for resolution.

## 1. Strategic Intent & Outcome (Tier 1 - Executive Level)
- **Business Value**: Prevents duplicate payments, over-billing, fraudulent invoices, and unearned vendor claims.
- **Strategic Alignment**: Ensures financial ledger integrity and captures early payment cash discounts (e.g. 2/10 Net 30).
- **Risk Exposure**: Manual exception bottlenecks, missed discount windows, late payment penalties, or duplicate disbursements.

## 2. Operational Workflow & RACI (Tier 2 - Process Architect Level)
- **Workflow Sequence**:
  1. Supplier invoice ingested electronically (OCR or e-invoicing portal).
  2. ERP automated engine performs 3-way match across line item quantities, unit prices, and tax rates.
  3. Matched invoices auto-approved; exceptions (> $1,000 variance) routed to AP Clerk for resolution.
- **RACI Matrix**:
  - **Responsible**: `role_accounts_payable_clerk`
  - **Accountable**: `role_finance_controller`
  - **Consulted**: `role_procurement_specialist`
  - **Informed**: `role_supplier`
- **SLA**: 24.0 Hours.

## 3. Systems Math & Simulation Parameters (Tier 3 - Simulation Engineer Level)
```math
\text{Matching Cost} = \text{Baseline Cost} \times (1 - \text{Automation Rate}) + \text{Exception Overhead} \times \text{Error Rate} \times 100.0
```
- **Primary Data Entity**: Verified Invoice Voucher (`INVOICE_VOUCHER_v1`).
- **Asset Load**: `asset_erp_system`, `asset_eprocurement_portal`.
---

### [Payment Settlement & Disbursement] (`s2p_008_payment_settlement_disbursement`) [Layer: `core`]
- **Type**: `process_step` | **Tags**: `payment, treasury, disbursement, banking`
- **RACI**: `{"responsible": ["role_accounts_payable_clerk"], "accountable": ["role_finance_controller"], "consulted": ["role_category_manager"], "informed": ["role_supplier"]}`
- **Assets**: `asset_erp_system, asset_payment_gateway`

# Process Step: Payment Settlement & Disbursement

## Executive Summary
Executes final treasury disbursement runs, transmits ISO 20022 XML files via banking gateway, and sends remittance advice notifications to suppliers.

## 1. Strategic Intent & Outcome (Tier 1 - Executive Level)
- **Business Value**: Optimizes working capital, preserves corporate credit rating, and maintains strong vendor relationships.
- **Strategic Alignment**: Realizes Treasury cash flow forecasting and payment run efficiency targets.
- **Risk Exposure**: Payment fraud, erroneous ACH routing, unauthorized disbursement, or banking gateway transmission failure.

## 2. Operational Workflow & RACI (Tier 2 - Process Architect Level)
- **Workflow Sequence**:
  1. AP Clerk compiles payment proposal batch due according to payment terms (Net 30/60).
  2. Finance Controller reviews batch and performs dual digital signoff.
  3. Encrypted ISO 20022 payment payload transmitted via `asset_payment_gateway` to bank network.
- **RACI Matrix**:
  - **Responsible**: `role_accounts_payable_clerk`
  - **Accountable**: `role_finance_controller`
  - **Consulted**: `role_category_manager`
  - **Informed**: `role_supplier`
- **SLA**: 8.0 Hours.

## 3. Systems Math & Simulation Parameters (Tier 3 - Simulation Engineer Level)
```math
\text{Disbursement Throughput} = \text{Batch Volume} \times \text{Automation Rate} \times \text{Gateway TPS Limit}
```
- **Primary Data Entity**: Payment Disbursement Record (`DISBURSEMENT_REC_v1`).
- **Asset Load**: `asset_erp_system`, `asset_payment_gateway`.
---

### [Segregation of Duties & Financial Authority Policy] (`sod_spending_limits_policy`) [Layer: `core`]
- **Type**: `control_policy` | **Tags**: `policy, governance, sod, compliance`
- **RACI**: `{"responsible": ["role_finance_controller"], "accountable": ["role_finance_controller"], "consulted": ["role_category_manager"], "informed": ["role_procurement_specialist", "role_accounts_payable_clerk"]}`
- **Assets**: `asset_erp_system`

# Control Policy: Segregation of Duties (SoD) & Spending Limits

## Executive Summary
Establishes enterprise internal control policies mandating that no single individual can initiate a purchase, approve the purchase order, verify goods receipt, and execute payment disbursement.

## 1. Governance Rules & Controls (Tier 1)
- **Rule 1 (SoD Incompatibility)**: A single user cannot hold both `role_procurement_specialist` (PO creation) and `role_accounts_payable_clerk` (Invoice voucher creation).
- **Rule 2 (Dual Disbursement Signoff)**: Payments exceeding $100,000 USD require dual approval from `role_finance_controller`.
- **Rule 3 (Spending Threshold Hierarchy)**:
  - Buyer: up to $50,000 USD.
  - Category Manager: up to $500,000 USD.
  - Finance Controller: unlimited.
---

### [Strategic Sourcing & Contracting Value Stream] (`strategic_sourcing_stream`) [Layer: `core`]
- **Type**: `value_stream` | **Tags**: `value_stream, strategic_sourcing`
- **RACI**: `{"responsible": ["role_category_manager"], "accountable": ["role_category_manager"], "consulted": ["role_finance_controller"], "informed": ["role_supplier"]}`
- **Assets**: `asset_eprocurement_portal, asset_erp_system`

# Value Stream: Strategic Sourcing & Contracting

## Executive Summary
Encompasses the upstream strategic procurement lifecycle from initial demand identification and vendor qualification through RFx event negotiation and master contract execution (Steps 001 - 004).

## 1. Strategic Outcomes (Tier 1)
- Market competitive pricing discovery.
- Vendor risk mitigation and compliance enforcement.
- Long-term contractual relationship management.

## 2. Included Steps & RACI Summary (Tier 2)
1. `s2p_001_spend_analysis_need_id`
2. `s2p_002_supplier_discovery_qualification`
3. `s2p_003_sourcing_rfx_auction`
4. `s2p_004_contracting_sla_negotiation`
---

