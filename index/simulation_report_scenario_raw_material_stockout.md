# Scenario Simulation Executive Report

**Scenario**: Raw Material Stockout due to Supplier Failure (`scenario_raw_material_stockout`)
**Target Lifecycle**: `P2M`

## Executive Summary & Macro Outcomes

| Metric | Baseline | Shocked Scenario | Variance Delta |
| :--- | :--- | :--- | :--- |
| **Total Lifecycle Lead Time** | `306.2 hrs` (12.8 days) | `773.6 hrs` (32.2 days) | `+152.6%` |
| **Total Process Cost / Unit** | `$1764.00` | `$2575.00` | `+46.0%` |

## Element Breakdown & Bottleneck Sensitivity Analysis

| Process Element | Baseline Time | Shocked Time | Time Delta | Baseline Cost | Shocked Cost | Cost Delta |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Statistical Demand Sensing & Forecasting** (`p2m_001_demand_sensing_forecasting`) | 193.2h | 193.2h | +0% | $57.50 | $57.50 | +0% |
| **Material Requirements Planning (MRP)** (`p2m_002_mrp_production_planning`) | 24.5h | 24.5h | +0% | $15.30 | $15.30 | +0% |
| **Production Order Sequencing & Release** (`p2m_003_production_order_release`) | 8.4h | 9.2h | +10% | $10.50 | $11.50 | +10% |
| **Manufacturing Execution & Yield Tracking** (`p2m_004_manufacturing_execution`) | 51.8h | 518.4h | 🔥 +900% | $1620.00 | $2430.00 | +50% |
| **Quality Inspection & Batch Release** (`p2m_005_quality_inspection_release`) | 24.2h | 24.2h | +0% | $50.50 | $50.50 | +0% |
| **Finished Goods Put-Away & ATP Update** (`p2m_006_finished_goods_putaway`) | 4.1h | 4.1h | +0% | $10.20 | $10.20 | +0% |
