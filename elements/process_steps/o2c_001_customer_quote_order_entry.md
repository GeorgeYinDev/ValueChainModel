---
id: o2c_001_customer_quote_order_entry
type: process_step
name: Quote Generation & Order Capture
version: 1.0.0
lifecycles: [O2C]
lod_support: [tier_1, tier_2, tier_3]
tags: [order_management, sales, quoting, cpq]

raci:
  responsible: [role_sales_ops_specialist]
  accountable: [role_sales_ops_specialist]
  consulted: [role_customer]
  informed: [role_credit_manager]

daci:
  driver: [role_sales_ops_specialist]
  approver: [role_sales_ops_specialist]
  contributor: [role_customer]
  informed: [role_credit_manager]

attributes:
  baseline_cycle_time_hours: 6.0
  baseline_cost_per_unit: 25.00
  automation_rate: 0.80
  error_rate: 0.02
  sla_hours: 12.0

asset_dependencies:
  - asset_crm_system
  - asset_erp_system
compensating_control: "CPQ system automatically enforces price floors and prevents margin erosion. Deviations route to Sales VP."

graph_relations:
  - relation: feeds_into
    target: o2c_002_credit_check_approval
    weight: 1.0
  - relation: governed_by
    target: credit_limit_risk_policy
    weight: 0.85
---

# Process Step: Quote Generation & Order Capture

## Executive Summary
Captures customer demand, configures products and services via Configure-Price-Quote (CPQ), validates contractual discounting, and converts signed quotes into formal enterprise sales orders.

## 1. Strategic Intent & Outcome (Tier 1 - Executive Level)
- **Business Value**: Drives top-line revenue velocity, eliminates order entry errors, and guarantees price-book and margin governance.
- **Strategic Alignment**: Directly supports commercial growth, customer satisfaction (CSAT), and revenue predictability.
- **Risk Exposure**: Inaccurate pricing terms, unapproved contract liabilities, or catalog configuration mismatches.

## 2. Operational Workflow & RACI (Tier 2 - Process Architect Level)
- **Workflow Sequence**:
  1. Customer submits Request for Quotation (RFQ) or digital purchase order through portal or EDI.
  2. CPQ rules engine validates product compatibility, lead-time availability, and volume discount schedule.
  3. Pricing exceptions outside standard authority matrix route to sales leadership for approval.
  4. Confirmed order payload creates open Sales Order header and line items in `asset_erp_system`.
- **RACI Assignment Matrix**:
  - **Responsible**: `role_sales_ops_specialist`
  - **Accountable**: `role_sales_ops_specialist`
  - **Consulted**: `role_customer`
  - **Informed**: `role_credit_manager`
- **Service Level Agreement (SLA)**: 12.0 Hours.

## 3. Systems Math & Simulation Parameters (Tier 3 - Simulation Engineer Level)
```math
\text{Order Capture Latency} = \text{Baseline Cycle Time} \times \left(1 + \frac{\text{Pricing Exception Rate}}{\text{CPQ Automation Rate}}\right)
```
- **Primary Data Entity**: Sales Order Document (`SALES_ORDER_v1`).
- **Asset Load**: Interrogates Salesforce CPQ via `asset_crm_system` and persists to SAP S/4HANA via `asset_erp_system`.
