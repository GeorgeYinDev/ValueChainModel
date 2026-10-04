---
id: o2c_002_credit_check_approval
type: process_step
name: Customer Credit Assessment & Exposure Check
version: 1.0.0
lifecycles: [O2C]
lod_support: [tier_1, tier_2, tier_3]
tags: [credit, risk, underwriting, compliance]

raci:
  responsible: [role_credit_manager]
  accountable: [role_finance_controller]
  consulted: [role_sales_ops_specialist]
  informed: [role_customer]

daci:
  driver: [role_credit_manager]
  approver: [role_finance_controller]
  contributor: [role_sales_ops_specialist]
  informed: [role_customer]

attributes:
  baseline_cycle_time_hours: 4.0
  baseline_cost_per_unit: 15.00
  automation_rate: 0.90
  error_rate: 0.01
  sla_hours: 8.0

asset_dependencies:
  - asset_erp_system
  - asset_crm_system

graph_relations:
  - relation: feeds_into
    target: o2c_003_inventory_allocation_fulfillment
    weight: 1.0
  - relation: governed_by
    target: credit_limit_risk_policy
    weight: 1.0
---

# Process Step: Customer Credit Assessment & Exposure Check

## Executive Summary
Evaluates customer commercial creditworthiness, computes rolling accounts receivable exposures, and adjudicates automated or manual credit holds prior to physical inventory commitment.

## 1. Strategic Intent & Outcome (Tier 1 - Executive Level)
- **Business Value**: Safeguards corporate balance sheet liquidity, prevents bad debt write-offs, and enforces disciplined working capital management.
- **Strategic Alignment**: Directly supports risk governance, SOX financial reporting controls, and corporate cash conversion cycle targets.
- **Risk Exposure**: Insolvent buyer default, uncollectible revenue, or commercial sales friction due to unwarranted credit holds.

## 2. Operational Workflow & RACI (Tier 2 - Process Architect Level)
- **Workflow Sequence**:
  1. Sales order creation triggers automated credit check evaluating total exposure (Open AR + Unbilled Deliveries + Current Order).
  2. If total exposure is within approved credit line and no invoices are >60 days past due, order is automatically released.
  3. If credit limit is breached, an automated credit hold lock is applied in `asset_erp_system`.
  4. Credit Underwriter reviews financial statements, payment history, and either requests payment or secures controller override.
- **RACI Assignment Matrix**:
  - **Responsible**: `role_credit_manager`
  - **Accountable**: `role_finance_controller`
  - **Consulted**: `role_sales_ops_specialist`
  - **Informed**: `role_customer`
- **Service Level Agreement (SLA)**: 8.0 Hours.

## 3. Systems Math & Simulation Parameters (Tier 3 - Simulation Engineer Level)
```math
\text{Total Exposure} = \text{Open AR Balance} + \sum \text{Unbilled Shipments} + \text{Order Value}
```
```math
\text{Credit Verification Delay} = \text{Baseline Cycle Time} \times \left(1 + \frac{\text{Credit Exception Ratio}}{\text{Auto-Approval Rate}}\right)
```
- **Primary Data Entity**: Credit Decision Record (`CREDIT_DECISION_v1`).
- **Asset Load**: ERP Credit Management module in `asset_erp_system` with credit score feed from `asset_crm_system`.
