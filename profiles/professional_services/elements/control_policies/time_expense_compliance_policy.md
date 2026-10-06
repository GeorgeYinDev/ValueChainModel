---
id: time_expense_compliance_policy
type: control_policy
name: Consultant Time & Expense Submission Compliance Policy
version: 1.0.0
lifecycles: [E2C]
lod_support: [tier_1, tier_2, tier_3]
tags: [policy, compliance, timesheets, expenses, governance]

raci:
  responsible: [role_consultant]
  accountable: [role_engagement_manager]
  consulted: [role_billing_specialist]
  informed: [role_practice_director]

daci:
  driver: [role_consultant]
  approver: [role_engagement_manager]
  contributor: [role_billing_specialist]
  informed: [role_practice_director]

attributes:
  baseline_cycle_time_hours: 0.0
  baseline_cost_per_unit: 0.0
  automation_rate: 1.0
  error_rate: 0.0
  sla_hours: 0.0
  approval_threshold_usd: 50000.0

asset_dependencies:
  - asset_psa_system

graph_relations: []
---

# Control Policy: Consultant Time & Expense Submission Compliance

## Executive Summary
Establishes operating rules and governance controls for logging, substantiating, and approving billable and non-billable hours and project-related reimbursable expenses in the PSA platform.

## 1. Governance Rules & Controls (Tier 1)
- **Rule 1 (Weekly Submission Cutoff SLA)**: All consultants must submit complete weekly timesheets and expense records in `asset_psa_system` by 10:00 AM local time each Monday.
- **Rule 2 (Itemized Expense Substantiation)**: All single-item expense claims exceeding $25.00 USD require an attached, legible electronic receipt and documented business purpose.
- **Rule 3 (Manager Approval SLA)**: Engagement Managers must review and sign off or reject timesheets within 24 hours of submission to prevent month-end billing crunch delays.
