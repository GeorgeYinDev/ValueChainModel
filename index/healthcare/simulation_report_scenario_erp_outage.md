# Scenario Simulation Executive Report

**Scenario**: Core ERP System Outage (`scenario_erp_outage`)
**Target Lifecycle**: `S2P`

## Executive Summary & Macro Outcomes

| Metric | Baseline | Shocked Scenario | Variance Delta |
| :--- | :--- | :--- | :--- |
| **Total Lifecycle Lead Time** | `270.4 hrs` (11.3 days) | `318.9 hrs` (13.3 days) | `+17.9%` |
| **Total Process Cost / Unit** | `$801.70` | `$801.70` | `+0.0%` |

## Element Breakdown & Bottleneck Sensitivity Analysis

| Process Element | Baseline Time | Shocked Time | Time Delta | Baseline Cost | Shocked Cost | Cost Delta |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Spend Analysis & Need Identification** (`s2p_001_spend_analysis_need_id`) | 12.4h | 12.4h | +0% | $46.35 | $46.35 | +0% |
| **Supplier Discovery & Qualification** (`s2p_002_supplier_discovery_qualification`) | 50.4h | 50.4h | +0% | $126.00 | $126.00 | +0% |
| **Strategic Sourcing & RFx Execution** (`s2p_003_sourcing_rfx_auction`) | 97.9h | 97.9h | +0% | $255.00 | $255.00 | +0% |
| **Contracting & SLA Negotiation** (`s2p_004_contracting_sla_negotiation`) | 74.9h | 74.9h | +0% | $312.00 | $312.00 | +0% |
| **Purchase Requisition & PO Issuance** (`s2p_005_purchase_requisition_po`) | 8.1h | 56.6h | 🔥 +600% | $18.18 | $18.18 | +0% |
| **Goods & Services Receipt Verification** (`s2p_006_goods_services_receipt`) | 6.1h | 6.1h | +0% | $12.75 | $12.75 | +0% |
| **Invoice 3-Way Matching & Exception Handling** (`s2p_007_invoice_verification_matching`) | 16.6h | 16.6h | +0% | $22.88 | $22.88 | +0% |
| **Payment Settlement & Disbursement** (`s2p_008_payment_settlement_disbursement`) | 4.0h | 4.0h | +0% | $8.54 | $8.54 | +0% |
