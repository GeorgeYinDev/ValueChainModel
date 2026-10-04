# Practitioner Guide: Authoring Value Chain Elements & Lifecycles

This guide provides step-by-step instructions for Enterprise Architects, Business Process Engineers, and Systems Analysts to model and introduce new business lifecycles, process steps, governance policies, enterprise roles, and IT assets into the **Enterprise Value Chain Modeling Engine**.

---

## 1. Directory Conventions & Element Types

All model entities reside in designated directories and must follow kebab_case or snake_case file naming:

```
elements/
├── process_steps/       # Granular business activities (e.g., s2p_001, o2c_001, r2r_001)
├── value_streams/       # End-to-end value delivery chains (e.g., procure_to_pay_stream)
└── control_policies/    # Governance rules & internal controls (e.g., sox_financial_reporting_controls_policy)
roles/                   # Enterprise human/organizational roles (e.g., role_finance_controller.md)
assets/                  # IT systems & infrastructure nodes (e.g., asset_erp_system.md)
lifecycles/              # Lifecycle blueprints and manifests (e.g., source_to_pay.json)
simulations/             # Scenario disruption shock definitions (e.g., scenario_close_period_crunch.json)
```

---

## 2. Authoring a Granular Process Step

Process steps are stored as Markdown documents with YAML frontmatter in `elements/process_steps/`.

### Step 1: Create the File
Copy from [`templates/element_template.md`](../../templates/element_template.md):
```bash
cp templates/element_template.md elements/process_steps/h2r_001_job_requisition_posting.md
```

### Step 2: Configure YAML Frontmatter
Ensure the frontmatter adheres to [`schema/value_chain_element.schema.json`](../../schema/value_chain_element.schema.json):

```yaml
---
id: h2r_001_job_requisition_posting
type: process_step
name: Job Requisition Approval & Portal Posting
version: 1.0.0
lifecycles: [H2R]
lod_support: [tier_1, tier_2, tier_3]
tags: [hr, recruiting, requisition, headcount]

raci:
  responsible: [role_talent_acquisition_specialist]
  accountable: [role_hiring_manager]
  consulted: [role_compensation_analyst]
  informed: [role_hr_business_partner]

daci:
  driver: [role_talent_acquisition_specialist]
  approver: [role_hiring_manager]
  contributor: [role_compensation_analyst]
  informed: [role_hr_business_partner]

attributes:
  baseline_cycle_time_hours: 24.0
  baseline_cost_per_unit: 150.00
  automation_rate: 0.70
  error_rate: 0.02
  sla_hours: 48.0

asset_dependencies:
  - asset_erp_system
  - asset_hcm_platform

graph_relations:
  - relation: feeds_into
    target: h2r_002_candidate_screening_interview
    weight: 1.0
  - relation: governed_by
    target: headcount_compensation_policy
    weight: 0.95
---
```

### Step 3: Author the Three-Tier Markdown Body
- **Tier 1 (Executive Summary & Strategic Outcome)**: Why this step exists, business value, and risk exposure.
- **Tier 2 (Operational Workflow & RACI)**: Numbered execution sequence, RACI roles, and SLA commitments.
- **Tier 3 (Systems Math & Simulation Parameters)**: Mathematical equations in LaTeX math blocks (`$$...$$`), primary data entities, and asset bottlenecks.

---

## 3. Defining Enterprise Roles (`roles/`)

Every role referenced in an element's `raci:` or `daci:` block **must exist** in `roles/`.

### File Template: `roles/role_<role_id>.md`
```markdown
# Role Definition: Talent Acquisition Specialist

- **Role ID**: `role_talent_acquisition_specialist`
- **Department**: Human Resources & Talent Sourcing
- **Reports To**: Head of Talent Acquisition
- **Internal / External**: Internal

## Key Responsibilities
- Partner with hiring managers to draft and publish job descriptions.
- Screen candidate resumes and manage applicant tracking workflows.

## Decision Rights & Financial Approval Limits
- **Job Board Posting Discretion**: Up to $5,000 USD per campaign.

## Required IT Systems Access
- `asset_hcm_platform` (Role: Recruiting Power User)
- `asset_erp_system` (Role: Position Management Viewer)
```

---

## 4. Defining IT Assets & Systems (`assets/`)

Every system referenced in `asset_dependencies:` must exist in `assets/` and adhere to [`schema/asset_hierarchy.schema.json`](../../schema/asset_hierarchy.schema.json).

### File Template: `assets/asset_<asset_id>.md`
```yaml
---
id: asset_hcm_platform
name: Enterprise Human Capital Management Platform (Workday)
asset_type: it_application
version: 4.1.0
parent_asset_id: asset_erp_system
status: operational
sla_uptime_percent: 99.95
capacity_max_tps: 800
---

# Enterprise Asset: Human Capital Management Platform

## Overview & Architecture
Central cloud repository for global employee records, position requisitions, payroll configuration, and organizational hierarchies.

## Parent & Child Dependencies
- **Parent Asset**: `asset_erp_system`
- **Child Sub-Assets**: None

## Operational SLAs & Capacity Limits
- **Uptime SLA**: 99.95%
- **Throughput Capacity**: 800 TPS
- **Recovery Time Objective (RTO)**: 2 hours
```

---

## 5. Blueprinting a New Lifecycle (`lifecycles/`)

Lifecycles define sequential milestone blueprints and key performance metrics. Store manifests in `lifecycles/<lifecycle_id>.json` conforming to [`schema/lifecycle_manifest.schema.json`](../../schema/lifecycle_manifest.schema.json):

```json
{
  "lifecycle_id": "H2R",
  "name": "Hire to Retire Lifecycle",
  "version": "1.0.0",
  "description": "End-to-end human capital lifecycle from talent acquisition and onboarding to performance, payroll, and separation.",
  "milestones": [
    { "step_id": "h2r_001_job_requisition_posting", "name": "Requisition Approval & Job Posting", "order": 1 },
    { "step_id": "h2r_002_candidate_screening_interview", "name": "Candidate Screening & Assessment", "order": 2 },
    { "step_id": "h2r_003_offer_letter_onboarding", "name": "Offer Extension & New Hire Onboarding", "order": 3 },
    { "step_id": "h2r_004_payroll_benefits_enrollment", "name": "Payroll Setup & Benefits Provisioning", "order": 4 },
    { "step_id": "h2r_005_offboarding_separation_settlement", "name": "Employee Separation & Final Settlement", "order": 5 }
  ],
  "key_performance_indicators": [
    "time_to_hire_days",
    "offer_acceptance_rate",
    "onboarding_satisfaction_score",
    "first_run_payroll_accuracy"
  ]
}
```

---

## 6. Build & Validation Rules

Always execute the automated build engine after adding or editing files:

```bash
python3 tools/validate_and_build.py
```

### Common Pitfalls & How to Fix Them

| Error Message | Root Cause | Resolution |
| :--- | :--- | :--- |
| `references undefined role 'role_xyz' in RACI.responsible` | The role ID does not match any file in `roles/role_xyz.md`. | Create `roles/role_xyz.md` or correct the typo. |
| `references undefined asset 'asset_xyz'` | The asset ID does not match any file in `assets/asset_xyz.md`. | Create `assets/asset_xyz.md` with required frontmatter. |
| `references non-existent target 'step_xyz'` | `graph_relations` target does not exist as an element or asset. | Verify the target ID spelling and verify the file exists. |
| `Missing 'id' in frontmatter` | The Markdown file lacks valid YAML frontmatter delimiter (`---`). | Add valid YAML frontmatter blocks at line 1. |
| `Split Approver Authority Detected` | Multiple roles listed in `daci.approver`. | Reduce to exactly one primary Approver role. |
