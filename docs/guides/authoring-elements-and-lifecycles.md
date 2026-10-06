# Practitioner Guide: Authoring Value Chain Elements & Lifecycles

This guide provides step-by-step instructions for Enterprise Architects, Business Process Engineers, and Systems Analysts to model and introduce new business lifecycles, process steps, governance policies, enterprise roles, and IT assets into the **Enterprise Value Chain Modeling Engine**.

---

## 1. Multi-Industry Profile Architecture & Conventions

All model entities reside within designated industry profiles under `profiles/<profile_id>/`:
- `profiles/core/`: Cross-industry horizontal capabilities (S2P, R2R, H2R).
- `profiles/manufacturing/`: Discrete manufacturing overlay (P2M, O2C, MES, APS, WMS).
- `profiles/professional_services/`: Consulting & services overlay (L2C, E2C, PSA).
- `profiles/<custom>/`: Bespoke industry overlays created via `tools/new_profile.py`.

Inside each profile directory, entities are organized into standard subfolders:

```
profiles/<profile_id>/
├── elements/            # Process steps, value streams, control policies, KPIs, data entities
│   ├── process_steps/   # Granular business activities (e.g., s2p_001, l2c_001, e2c_001)
│   ├── value_streams/   # End-to-end value delivery chains (e.g., client_engagement_delivery_stream)
│   ├── control_policies/# Governance rules & controls (e.g., project_pricing_margin_policy)
│   ├── kpi_metrics/     # Quantitative performance metrics (e.g., kpi_billable_utilization)
│   └── data_entities/   # Transactional records and artifacts (e.g., data_statement_of_work)
├── roles/               # Enterprise roles with approval limits (e.g., role_practice_director.md)
├── assets/              # IT applications & systems nodes (e.g., asset_psa_system.md)
├── lifecycles/          # Lifecycle manifests with phases & milestones (e.g., lead_to_cash.json)
├── simulations/         # Disruption scenario definitions (e.g., scenario_project_margin_slippage.json)
└── patches/             # YAML patches modifying inherited elements (e.g., s2p_006_goods_services_receipt.yaml)
```

---

## 2. Authoring a Granular Process Step

Process steps are stored as Markdown documents with YAML frontmatter in `elements/process_steps/`.

### Step 1: Create the File
Copy from [`templates/element_template.md`](../../templates/element_template.md):
```bash
cp templates/element_template.md profiles/professional_services/elements/process_steps/e2c_001_project_kickoff.md
```

### Step 2: Configure YAML Frontmatter
Ensure the frontmatter adheres to [`schema/value_chain_element.schema.json`](../../schema/value_chain_element.schema.json):

```yaml
---
id: e2c_001_project_kickoff
type: process_step
name: Project Kickoff & Resource Allocation
version: 1.0.0
lifecycles: [E2C]
lod_support: [tier_1, tier_2, tier_3]
tags: [delivery, staffing, kickoff]

raci:
  responsible: [role_engagement_manager]
  accountable: [role_practice_director]
  consulted: [role_consultant]
  informed: [role_customer]

daci:
  driver: [role_engagement_manager]
  approver: [role_practice_director]
  contributor: [role_consultant]
  informed: [role_customer]

attributes:
  baseline_cycle_time_hours: 16.0
  baseline_cost_per_unit: 500.00
  automation_rate: 0.20
  error_rate: 0.02
  sla_hours: 24.0
  volume_per_period: 40
  capacity_fte: 2.0
  approval_threshold_usd: 50000.0

apqc_pcf_id: "3.5.1.1"

asset_dependencies:
  - asset_psa_system

graph_relations:
  - relation: feeds_into
    target: e2c_002_resource_scheduling
    weight: 1.0
  - relation: governed_by
    target: project_pricing_margin_policy
    weight: 1.0
---
```

### Step 3: Author the Three-Tier Markdown Body
- **Tier 1 (Executive Summary & Strategic Outcome)**: Why this step exists, business value, and risk exposure.
- **Tier 2 (Operational Workflow & RACI)**: Numbered execution sequence, RACI roles, and SLA commitments.
- **Tier 3 (Systems Math & Simulation Parameters)**: Mathematical equations in LaTeX math blocks (`$$...$$`), primary data entities, and asset bottlenecks.

---

## 3. Defining Enterprise Roles (`roles/`)

Every role referenced in an element's `raci:` or `daci:` block **must exist** in the resolved role registry. Roles declare explicit departmental affiliations and financial delegation authority:

```markdown
---
id: role_practice_director
type: role
name: "Practice Director"
department: "Practice Leadership"
approval_limit_usd: 250000.0
---

# Role Definition: Practice Director

- **Role ID**: `role_practice_director`
- **Department**: Practice Leadership
- **Reports To**: Managing Director / VP Professional Services
- **Internal / External**: Internal

## Key Responsibilities
- Accountable for practice P&L, consultant billable utilization, and strategic portfolio growth.
- Approving pricing rate card exceptions and commercial engagements up to $250,000 USD.

## Required IT Systems Access
- `asset_psa_system` (Role: Practice Director Superuser)
- `asset_crm_system` (Role: Sales Practice Approver)
```

---

## 4. Defining IT Assets & Systems (`assets/`)

Every system referenced in `asset_dependencies:` must exist in `assets/` and adhere to [`schema/asset_hierarchy.schema.json`](../../schema/asset_hierarchy.schema.json).

```yaml
---
id: asset_psa_system
name: Professional Services Automation Platform (Certinia/Kantata)
asset_type: it_application
version: 2026.2
parent_asset_id: asset_erp_system
status: operational
sla_uptime_percent: 99.9
capacity_max_tps: 500
---

# Enterprise Asset: Professional Services Automation Platform

## Overview & Architecture
Cloud-native PSA engine managing consultant skills, staffing rosters, project WBS structures, billable time capture, and milestone revenue recognition.

## Parent & Child Dependencies
- **Parent Asset**: `asset_erp_system`
- **Child Sub-Assets**: None

## Operational SLAs & Capacity Limits
- **Uptime SLA**: 99.9%
- **Throughput Capacity**: 500 TPS
- **Recovery Time Objective (RTO)**: 4 hours
```

---

## 5. Blueprinting a New Lifecycle (`lifecycles/`)

Lifecycles define sequential milestone blueprints, data-driven visualization phases, and key performance indicators conforming to [`schema/lifecycle_manifest.schema.json`](../../schema/lifecycle_manifest.schema.json):

```json
{
  "$schema": "../../schema/lifecycle_manifest.schema.json",
  "lifecycle_id": "L2C",
  "name": "Lead to Cash",
  "version": "1.1.0",
  "description": "Sales pipeline generation, proposal development, and contract closure.",
  "milestones": [
    { "order": 1, "step_id": "l2c_001_lead_qualification", "name": "Lead Qualification" },
    { "order": 2, "step_id": "l2c_002_proposal_development", "name": "Proposal Development" },
    { "order": 3, "step_id": "l2c_003_contract_negotiation", "name": "Contract Negotiation" },
    { "order": 4, "step_id": "l2c_004_deal_closure_handover", "name": "Deal Closure" }
  ],
  "phases": [
    {
      "phase_id": "pipeline_proposal",
      "name": "Pipeline & Proposal Phase",
      "milestones": ["l2c_001_lead_qualification", "l2c_002_proposal_development"]
    },
    {
      "phase_id": "negotiation_closing",
      "name": "Negotiation & Deal Closure Phase",
      "milestones": ["l2c_003_contract_negotiation", "l2c_004_deal_closure_handover"]
    }
  ],
  "key_performance_indicators": [
    "Win Rate",
    "Time to Close",
    "Pipeline Velocity"
  ]
}
```

---

## 6. Authoring Value Streams, Policies, KPIs & Data Entities

The engine provides first-class support for specialized architectural primitives:

| Element Type | Primary Purpose | Required Fields | Typical Graph Relations |
| :--- | :--- | :--- | :--- |
| `value_stream` | Multi-step macro workflow delivery | `id`, `name`, `lifecycles`, `raci` | `governed_by`, `feeds_into` |
| `control_policy` | Internal controls, SLAs, risk limits | `approval_threshold_usd` | Target of `governed_by` |
| `kpi_metric` | Formal business metric definition | `formula`, `target`, `owner`, `unit` | `impacted_by` |
| `data_entity` | System of record data artifact | `system_of_record`, `owner` | Target of `produces_artifact`, `triggers` |

---

## 7. Build & Validation Rules

Always execute the automated build engine after adding or editing files:

```bash
# Validate your target profile
uv run tools/validate_and_build.py --profile professional_services

# Validate all profiles globally
uv run tools/validate_and_build.py --profile ALL
```

### Common Pitfalls & How to Fix Them

| Error Message | Root Cause | Resolution |
| :--- | :--- | :--- |
| `references undefined role 'role_xyz' in RACI.responsible` | The role ID does not exist in the current profile or inherited base layers. | Create `roles/role_xyz.md` in your profile or check the role spelling. |
| `references undefined asset 'asset_xyz'` | The asset ID does not exist in the profile or base layers. | Create `assets/asset_xyz.md` with required frontmatter. |
| `references non-existent target 'step_xyz'` | `graph_relations` target does not exist as an element or asset. | Verify the target ID and confirm the element is loaded. |
| `Split Approver Authority Detected` | Multiple roles listed in `daci.approver` or `raci.accountable`. | Reduce to exactly one Approver role ($|A|=1$). |
| `Approval Threshold Exceeds Role Limit` | A step or policy's `approval_threshold_usd` exceeds the Accountable role's `approval_limit_usd`. | Increase the role limit in its frontmatter, or assign a role with sufficient authority. |
| `SoD Conflict: Role cannot be both Responsible and Accountable` | The same role is assigned to `responsible` and `accountable` in the RACI matrix. | Declare a valid `compensating_control: "..."` string in the frontmatter. |
| `Accidental ID collision in elements` | An overlay element reuses an ID from an inherited parent layer without declaring an override. | Add `overrides: <parent_layer>` to the element frontmatter if replacing intentionally. |
