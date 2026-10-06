# System Prompt: LLM Context Blueprint for Business Lifecycle [Plan to Make Lifecycle]

> Profile: `manufacturing` | Lifecycle ID: `P2M` | Version: `1.0.0` | Source Layer: `manufacturing`
> Description: End-to-end manufacturing process from demand forecasting to production execution, quality release, and final inventory availability.

## Milestone Process Sequence
- **Step 1**: `p2m_001_demand_sensing_forecasting` (Statistical Demand Sensing & Forecasting)
- **Step 2**: `p2m_002_mrp_production_planning` (Material Requirements Planning (MRP))
- **Step 3**: `p2m_003_production_order_release` (Production Order Sequencing & Release)
- **Step 4**: `p2m_004_manufacturing_execution` (Manufacturing Execution & Yield Tracking)
- **Step 5**: `p2m_005_quality_inspection_release` (Quality Inspection & Batch Release)
- **Step 6**: `p2m_006_finished_goods_putaway` (Finished Goods Put-Away & ATP Update)

## Key Performance Indicators (KPIs)
- `forecast_accuracy`
- `overall_equipment_effectiveness_oee`
- `first_pass_yield`
- `on_time_in_full_otif`

## Active Value Chain Elements Knowledge Base

### [Statistical Demand Sensing & Forecasting] (`p2m_001_demand_sensing_forecasting`) [Layer: `manufacturing`]
- **Type**: `process_step` | **Tags**: `supply_chain, planning, forecasting`
- **RACI**: `{"responsible": ["role_demand_planner"], "accountable": ["role_demand_planner"], "consulted": ["role_sales_ops_specialist"], "informed": ["role_production_scheduler"]}`
- **Assets**: `asset_aps_planner`

# Process Step: Statistical Demand Sensing & Forecasting

## Executive Summary
Aggregates historical sales, market trends, and predictive analytics to generate the baseline demand forecast for manufacturing planning.

## 1. Strategic Intent & Outcome (Tier 1 - Executive Level)
- **Business Value**: Minimizes working capital tied up in excess inventory while preventing lost revenue from stockouts.
- **Risk Exposure**: Inaccurate forecasts leading to the "bullwhip effect", excess obsolescence, or unfilled customer orders.

## 2. Operational Workflow (Tier 2)
- APS engine ingests point-of-sale data and historical shipments.
- Demand Planner applies statistical smoothing models.
- Sales Ops provides qualitative overrides for promotions.
- Consensus forecast is published to the MRP engine.
---

### [Material Requirements Planning (MRP)] (`p2m_002_mrp_production_planning`) [Layer: `manufacturing`]
- **Type**: `process_step` | **Tags**: `supply_chain, planning, mrp`
- **RACI**: `{"responsible": ["role_production_scheduler"], "accountable": ["role_production_scheduler"], "consulted": ["role_inventory_manager"], "informed": ["role_procurement_specialist"]}`
- **Assets**: `asset_erp_system, asset_aps_planner`

# Process Step: Material Requirements Planning (MRP)

## Executive Summary
Explodes the consensus demand forecast through the Bill of Materials (BOM) to determine exact raw material requirements and sub-assembly schedules.

## 1. Strategic Intent & Outcome (Tier 1 - Executive Level)
- **Business Value**: Ensures the right materials are available at the right time for factory consumption.
- **Risk Exposure**: Misconfigured BOMs or lead-time data causing line stoppages due to missing components.

## 2. Operational Workflow (Tier 2)
- ERP engine runs overnight MRP batch job against the forecast and current inventory.
- Scheduler reviews planned orders and exception messages (expedite/defer).
- MRP triggers purchase requisitions (`s2p_001`) for missing raw materials.
- Master Production Schedule (MPS) is finalized.
---

### [Production Order Sequencing & Release] (`p2m_003_production_order_release`) [Layer: `manufacturing`]
- **Type**: `process_step` | **Tags**: `manufacturing, scheduling`
- **RACI**: `{"responsible": ["role_production_scheduler"], "accountable": ["role_manufacturing_supervisor"], "consulted": ["role_inventory_manager"], "informed": []}`
- **Assets**: `asset_erp_system, asset_mes_system`

# Process Step: Production Order Sequencing & Release

## Executive Summary
Commits planned orders into active production orders, sequencing them on the shop floor to minimize changeover and setup times.

## 1. Strategic Intent & Outcome (Tier 1 - Executive Level)
- **Business Value**: Maximizes Overall Equipment Effectiveness (OEE) and throughput.
- **Risk Exposure**: Inefficient sequencing causing excessive machine downtime or failure to meet critical customer orders.

## 2. Operational Workflow (Tier 2)
- Scheduler converts planned orders to production orders.
- Orders are sequenced based on physical constraints (e.g., color wheels, allergen washdowns).
- Bill of Materials and routing instructions are dispatched to the MES.
- Components are staged from the warehouse to the line.
---

### [Manufacturing Execution & Yield Tracking] (`p2m_004_manufacturing_execution`) [Layer: `manufacturing`]
- **Type**: `process_step` | **Tags**: `manufacturing, shop_floor`
- **RACI**: `{"responsible": ["role_manufacturing_supervisor"], "accountable": ["role_manufacturing_supervisor"], "consulted": ["role_quality_assurance_engineer"], "informed": ["role_production_scheduler"]}`
- **Assets**: `asset_mes_system`

# Process Step: Manufacturing Execution & Yield Tracking

## Executive Summary
The physical transformation of raw materials into finished goods, consuming labor and machine hours while recording actual yields and scrap rates.

## 1. Strategic Intent & Outcome (Tier 1 - Executive Level)
- **Business Value**: Core value creation step. Converts inputs into sellable revenue-generating products.
- **Risk Exposure**: Machine breakdowns, labor shortages, or poor yields destroying gross margin.

## 2. Operational Workflow (Tier 2)
- Operators clock into the production order in the MES.
- Machines execute routing steps (mixing, assembly, packaging).
- Actual material consumption and scrap are recorded.
- Finished pallets are declared off the end of the line.
---

### [Quality Inspection & Batch Release] (`p2m_005_quality_inspection_release`) [Layer: `manufacturing`]
- **Type**: `process_step` | **Tags**: `manufacturing, quality`
- **RACI**: `{"responsible": ["role_quality_assurance_engineer"], "accountable": ["role_quality_assurance_engineer"], "consulted": ["role_manufacturing_supervisor"], "informed": ["role_inventory_manager"]}`
- **Assets**: `asset_erp_system, asset_mes_system`

# Process Step: Quality Inspection & Batch Release

## Executive Summary
Verifies that manufactured goods meet all engineering and regulatory specifications before they are allowed into sellable inventory.

## 1. Strategic Intent & Outcome (Tier 1 - Executive Level)
- **Business Value**: Protects brand reputation and prevents costly customer returns or regulatory recalls.
- **Risk Exposure**: Releasing defective products to the market, or delaying good product in quarantine.

## 2. Operational Workflow (Tier 2)
- Samples are drawn from the finished batch.
- Physical, chemical, or functional testing is performed.
- Batch is designated as 'Unrestricted Use', 'Blocked', or 'Scrap'.
- Blocked items route back to manufacturing for rework if possible.
---

### [Finished Goods Put-Away & ATP Update] (`p2m_006_finished_goods_putaway`) [Layer: `manufacturing`]
- **Type**: `process_step` | **Tags**: `warehouse, inventory, atp`
- **RACI**: `{"responsible": ["role_inventory_manager"], "accountable": ["role_inventory_manager"], "consulted": [], "informed": ["role_sales_ops_specialist"]}`
- **Assets**: `asset_wms_system, asset_erp_system`

# Process Step: Finished Goods Put-Away & ATP Update

## Executive Summary
Physically moves cleared goods into warehouse storage and updates the Available-to-Promise (ATP) inventory ledger so sales can fulfill orders.

## 1. Strategic Intent & Outcome (Tier 1 - Executive Level)
- **Business Value**: Makes the manufactured product instantly available for revenue realization.
- **Risk Exposure**: Misplaced inventory ("phantom inventory") leading to order fulfillment failures.

## 2. Operational Workflow (Tier 2)
- Forklift driver receives put-away task via RF scanner.
- Pallet is scanned and placed in the designated storage bin.
- WMS updates ERP inventory levels.
- ATP quantity is incremented, feeding into the O2C cycle.
---

