# Scenario Simulation Executive Report

**Scenario**: Core ERP System Outage (`scenario_erp_outage`)
**Target Lifecycle**: `S2P`

## Executive Summary & Macro Outcomes

| Metric | Baseline | Shocked Scenario | Variance Delta |
| :--- | :--- | :--- | :--- |
| **Total Lifecycle Lead Time** | `524.0 hrs` (21.8 days) | `572.0 hrs` (23.8 days) | `+9.2%` |
| **Total Process Cost / Unit** | `$1551.50` | `$1551.50` | `+0.0%` |

## Element Breakdown & Bottleneck Sensitivity Analysis

| Process Element | Baseline Time | Shocked Time | Time Delta | Baseline Cost | Shocked Cost | Cost Delta |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Procure to Pay (P2P) Operational Value Stream** (`procure_to_pay_stream`) | 34.0h | 34.0h | +0% | $60.50 | $60.50 | +0% |
| **Spend Analysis & Need Identification** (`s2p_001_spend_analysis_need_id`) | 12.0h | 12.0h | +0% | $45.00 | $45.00 | +0% |
| **Supplier Discovery & Qualification** (`s2p_002_supplier_discovery_qualification`) | 48.0h | 48.0h | +0% | $120.00 | $120.00 | +0% |
| **Strategic Sourcing & RFx Execution** (`s2p_003_sourcing_rfx_auction`) | 96.0h | 96.0h | +0% | $250.00 | $250.00 | +0% |
| **Contracting & SLA Negotiation** (`s2p_004_contracting_sla_negotiation`) | 72.0h | 72.0h | +0% | $300.00 | $300.00 | +0% |
| **Purchase Requisition & PO Issuance** (`s2p_005_purchase_requisition_po`) | 8.0h | 56.0h | 🔥 +600% | $18.00 | $18.00 | +0% |
| **Goods & Services Receipt Verification** (`s2p_006_goods_services_receipt`) | 6.0h | 6.0h | +0% | $12.50 | $12.50 | +0% |
| **Invoice 3-Way Matching & Exception Handling** (`s2p_007_invoice_verification_matching`) | 16.0h | 16.0h | +0% | $22.00 | $22.00 | +0% |
| **Payment Settlement & Disbursement** (`s2p_008_payment_settlement_disbursement`) | 4.0h | 4.0h | +0% | $8.50 | $8.50 | +0% |
| **Segregation of Duties & Financial Authority Policy** (`sod_spending_limits_policy`) | 0.0h | 0.0h | +0% | $0.00 | $0.00 | +0% |
| **Strategic Sourcing & Contracting Value Stream** (`strategic_sourcing_stream`) | 228.0h | 228.0h | +0% | $715.00 | $715.00 | +0% |
