---
id: credit_limit_risk_policy
type: control_policy
name: Commercial Credit Limit & Customer Risk Exposure Policy
version: 1.0.0
lifecycles: [O2C]
lod_support: [tier_1, tier_2, tier_3]
tags: [policy, credit, risk, compliance]

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
  baseline_cycle_time_hours: 0.0
  baseline_cost_per_unit: 0.0
  automation_rate: 1.0
  error_rate: 0.0
  sla_hours: 0.0

asset_dependencies:
  - asset_erp_system
  - asset_crm_system

---

# Control Policy: Commercial Credit Limit & Risk Exposure

## Executive Summary
Defines corporate governance standards for underwriting customer credit limits, monitoring rolling accounts receivable exposures, and enforcing automatic order holds to prevent bad debt default.

## 1. Governance Rules & Controls (Tier 1)
- **Rule 1 (Automatic Credit Hold)**: Orders exceeding a customer's approved credit limit or accounts with past-due balances >60 days are automatically placed on credit hold in `asset_erp_system`.
- **Rule 2 (Single Underwriter Limit)**: Orders under credit hold up to $250,000 USD can be released solely by `role_credit_manager`.
- **Rule 3 (Executive Exception Approval)**: Overrides exceeding $250,000 USD mandate formal sign-off from `role_finance_controller` with collateral or parent company guarantee.
