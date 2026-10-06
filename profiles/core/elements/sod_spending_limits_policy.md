---
id: sod_spending_limits_policy
type: control_policy
name: Segregation of Duties & Financial Authority Policy
version: 1.0.0
lifecycles: [S2P]
lod_support: [tier_1, tier_2, tier_3]
tags: [policy, governance, sod, compliance]

raci:
  responsible: [role_finance_controller]
  accountable: [role_finance_controller]
  consulted: [role_category_manager]
  informed: [role_procurement_specialist, role_accounts_payable_clerk]

attributes:
  baseline_cycle_time_hours: 0.0
  baseline_cost_per_unit: 0.0
  automation_rate: 1.0
  error_rate: 0.0
  sla_hours: 0.0

asset_dependencies:
  - asset_erp_system
compensating_control: "Policy configuration changes require dual authorization in GRC tool."
---

# Control Policy: Segregation of Duties (SoD) & Spending Limits

## Executive Summary
Establishes enterprise internal control policies mandating that no single individual can initiate a purchase, approve the purchase order, verify goods receipt, and execute payment disbursement.

## 1. Governance Rules & Controls (Tier 1)
- **Rule 1 (SoD Incompatibility)**: A single user cannot hold both `role_procurement_specialist` (PO creation) and `role_accounts_payable_clerk` (Invoice voucher creation).
- **Rule 2 (Dual Disbursement Signoff)**: Payments exceeding $100,000 USD require dual approval from `role_finance_controller`.
- **Rule 3 (Spending Threshold Hierarchy)**:
  - Buyer: up to $50,000 USD.
  - Category Manager: up to $500,000 USD.
  - Finance Controller: unlimited.
