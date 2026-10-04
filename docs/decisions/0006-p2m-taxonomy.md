# ADR-0006: Manufacturing & Supply Chain (Plan-to-Make) Taxonomy

## Status
Accepted

## Context
Following the implementation of foundational financial (R2R), procurement (S2P), revenue (O2C), and human capital (H2R) lifecycles, the Enterprise Value Chain Modeling Engine must model physical manufacturing constraints. The Plan-to-Make (P2M) lifecycle bridges the gap between raw material procurement and finished goods sales, serving as the core of supply chain operations. 

## Decision
We establish the `P2M` (Plan to Make) lifecycle with the following boundaries and integration touchpoints:
- **Starting Point**: Statistical demand sensing and forecasting.
- **Ending Point**: Finished goods are put away into the warehouse and made available to promise (ATP).
- **Process Steps (Milestones)**:
  1. `p2m_001_demand_sensing_forecasting`
  2. `p2m_002_mrp_production_planning`
  3. `p2m_003_production_order_release`
  4. `p2m_004_manufacturing_execution`
  5. `p2m_005_quality_inspection_release`
  6. `p2m_006_finished_goods_putaway`
- **Integration Points**:
  - Ingests raw materials from `s2p_006_goods_services_receipt` (Procure-to-Pay).
  - Supplies Available-to-Promise (ATP) finished inventory to `o2c_003_inventory_allocation_fulfillment` (Order-to-Cash).

## Consequences
- Requires new manufacturing roles (Demand Planner, Production Scheduler, Manufacturing Supervisor, QA Engineer, Inventory Manager).
- Requires factory IT assets (`asset_mes_system`, `asset_aps_planner`).
- Introduces physical constraints (e.g., raw material stockouts) that can quantitatively impact O2C fulfillment times.
