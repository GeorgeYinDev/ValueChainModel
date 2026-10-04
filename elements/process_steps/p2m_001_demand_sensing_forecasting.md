---
id: p2m_001_demand_sensing_forecasting
type: process_step
name: "Statistical Demand Sensing & Forecasting"
version: "1.0.0"
lifecycles: ["P2M"]
lod_support: ["tier_1", "tier_2", "tier_3"]
tags: ["supply_chain", "planning", "forecasting"]

raci:
  responsible: [role_demand_planner]
  accountable: [role_demand_planner]
  consulted: [role_sales_ops_specialist]
  informed: [role_production_scheduler]

attributes:
  baseline_cycle_time_hours: 168.0
  baseline_cost_per_unit: 50.0
  automation_rate: 0.80
  error_rate: 0.15
  sla_hours: 336.0
  volume_per_period: 10
  capacity_fte: 2.0

asset_dependencies:
  - asset_aps_planner

graph_relations:
  - relation: feeds_into
    target: p2m_002_mrp_production_planning
    weight: 1.0

compensating_control: "S&OP executive committee formally signs off on the consensus demand plan."
---

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
