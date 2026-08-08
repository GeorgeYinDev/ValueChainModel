# ADR 0002: Source-to-Pay (S2P) Lifecycle Taxonomy and Boundary Design

- **Status**: Approved
- **Date**: 2026-08-08
- **Authors**: Enterprise Architecture Team / Antigravity AI

## Context
The Source-to-Pay (S2P) lifecycle is a foundational enterprise business process spanning strategic procurement, vendor onboarding, contract execution, purchasing, goods receipt, invoice processing, and financial disbursement.

To build an initial production reference model, we must establish clear process boundaries, milestone steps, RACI roles, and asset linkages.

## Decision
We define the S2P lifecycle as an 8-step sequential and milestone-driven value chain:
1. `s2p_001_spend_analysis_need_id`: Spend analytics and purchase requisition initiation.
2. `s2p_002_supplier_discovery_qualification`: Vendor master onboarding, risk profiling, compliance checks.
3. `s2p_003_sourcing_rfx_auction`: RFQ/RFP event execution and bid evaluation.
4. `s2p_004_contracting_sla_negotiation`: Master Services Agreement (MSA) and SLA finalization.
5. `s2p_005_purchase_requisition_po`: Purchase Requisition approval and PO dispatch.
6. `s2p_006_goods_services_receipt`: Receiving dock inspection and Goods Receipt (GR) booking.
7. `s2p_007_invoice_verification_matching`: 3-way matching (PO, GR, Invoice) and exception management.
8. `s2p_008_payment_settlement_disbursement`: Treasury payment execution and remittance advice.

### Roles Included
- Category Manager
- Procurement Specialist
- Accounts Payable Clerk
- Finance Controller
- Supplier / Vendor

### Core Assets Included
- Enterprise ERP Core (`asset_erp_system`)
- Cloud e-Procurement Portal (`asset_eprocurement_portal`)
- Banking Payment Gateway (`asset_payment_gateway`)

## Consequences
- Standardized baseline for S2P benchmarking across industries.
- Enables clear scenario simulations (e.g. supplier disruption, invoice bottleneck, ERP outage).
