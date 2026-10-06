---
id: project_pricing_margin_policy
type: control_policy
name: Project Pricing & Target Gross Margin Governance Policy
version: 1.0.0
lifecycles: [L2C]
lod_support: [tier_1, tier_2, tier_3]
tags: [policy, pricing, margin, governance, professional_services]

raci:
  responsible: [role_solution_architect]
  accountable: [role_practice_director]
  consulted: [role_account_executive]
  informed: [role_engagement_manager]

daci:
  driver: [role_solution_architect]
  approver: [role_practice_director]
  contributor: [role_account_executive]
  informed: [role_engagement_manager]

attributes:
  baseline_cycle_time_hours: 0.0
  baseline_cost_per_unit: 0.0
  automation_rate: 1.0
  error_rate: 0.0
  sla_hours: 0.0
  approval_threshold_usd: 100000.0

asset_dependencies:
  - asset_crm_system
  - asset_psa_system

graph_relations: []
---

# Control Policy: Project Pricing & Target Gross Margin Governance

## Executive Summary
Defines corporate governance standards for pricing client engagements, validating rate card compliance, setting mandatory gross margin hurdle rates, and enforcing escalation workflows for non-standard commercial concessions.

## 1. Governance Rules & Controls (Tier 1)
- **Rule 1 (Minimum Margin Hurdle Rate)**: All proposed client engagements (fixed-fee and time-and-materials) must meet or exceed a baseline projected Gross Margin of 45.0%.
- **Rule 2 (Rate Card Discounting Limits)**:
  - Discounts <= 10.0% against standard master rate cards: Authorized by `role_account_executive`.
  - Discounts 10.1% to 20.0%: Mandates sign-off from `role_practice_director` (up to approval limit of $250,000 USD).
  - Discounts > 20.0%: Mandates executive exception sign-off from `role_finance_controller`.
- **Rule 3 (Fixed-Fee Scope Contingency Buffer)**: Fixed-price contracts must incorporate a mandatory 15.0% scope contingency risk buffer in effort estimation models before proposal delivery.
