# CLI Tooling & Engine Reference Manual

This document provides a comprehensive technical reference for the command-line interface (CLI) tools in the `tools/` directory.

---

## 1. Model Validator & Knowledge Graph Builder (`validate_and_build.py`)

### Synopsis
```bash
# Validate and build a specific industry profile (default: manufacturing)
uv run tools/validate_and_build.py [--profile PROFILE_ID]

# Validate and build ALL industry profiles and generate multi-profile switcher dashboard
uv run tools/validate_and_build.py --profile ALL
```

### Purpose
The primary validation and build orchestrator for the repository. It resolves profile inheritance via `tools/vcm_profiles.py`, ingests all Markdown elements, roles, assets, and lifecycle manifests across the inheritance tree, enforces schema compliance and relational integrity, compiles unified graph databases, produces LLM prompt context packs, and exports interactive visualizers.

### CLI Arguments

| Argument | Type | Default | Description |
| :--- | :---: | :---: | :--- |
| `--profile` | string | `manufacturing` | Profile ID to validate and build (`core`, `manufacturing`, `professional_services`), or `ALL` to build all discovered profiles sequentially. |

### Execution Sequence & Checks
1. **Profile Resolution**: Loads `profile.json` manifests via depth-first inheritance traversal, validates schemas (`profile_manifest.schema.json`), and applies profile patches (`patches/*.yaml`).
2. **Role Ingestion**: Scans `roles/*.md` across inherited layers, parses `department` and `approval_limit_usd` frontmatter, and registers roles.
3. **Asset Ingestion**: Scans `assets/*.md` and verifies parent-child hierarchy linkages.
4. **Element Ingestion**: Parses YAML frontmatter across `elements/**/*.md` (Process Steps, Value Streams, Control Policies, KPI Metrics, Data Entities).
5. **Relational & Governance Integrity Validation**:
   - Verifies that every role in `raci:` and `daci:` exists in the resolved role registry.
   - Validates Segregation of Duties (SoD): Accountable and Responsible roles cannot be identical unless `compensating_control` is declared.
   - Enforces Approval Limits: Verifies `approval_threshold_usd` does not exceed the Accountable role's limit.
   - Verifies that all `asset_dependencies:` exist in the asset registry.
   - Validates that `graph_relations:` targets exist, have valid relation types, and avoid self-referencing loops.
   - Prevents accidental cross-layer ID collisions unless marked with `overrides:`.
6. **Knowledge Graph Compilation**: Writes consolidated JSON database to `index/<profile>/knowledge_graph.json`.
7. **LLM Prompt Pack Generation**: Compiles standalone context packs per lifecycle into `index/<profile>/llm_context_<lifecycle_id>.md`.
8. **Downstream Diagram & Visualizer Build**: Invokes `tools/export_diagram.py --profile <profile> --lifecycle ALL --format all`.
9. **Multi-Profile Landing Dashboard**: When `--profile ALL` is passed, compiles `index/index.html` with an interactive profile switcher.

### Exit Codes
- `0`: Validation and build succeeded with zero defects.
- `1`: Validation failed due to schema violations, missing targets, SoD conflicts, or threshold errors.

---

## 2. Diagram & Interactive Visualizer Exporter (`export_diagram.py`)

### Synopsis
```bash
uv run tools/export_diagram.py [--profile PROFILE_ID] [--lifecycle LIFECYCLE_ID] [--format FORMAT] [--output-dir DIR]
```

### CLI Arguments

| Argument | Type | Default | Description |
| :--- | :---: | :---: | :--- |
| `--profile` | string | `manufacturing` | Target profile whose knowledge graph and lifecycles to render. |
| `--lifecycle` | string | `ALL` | Target lifecycle scope to filter (`S2P`, `O2C`, `R2R`, `H2R`, `P2M`, `L2C`, `E2C`, or `ALL`). |
| `--format` | string | `all` | Output artifact format. Choices: `mermaid`, `markdown`, `html`, `all`. |
| `--output-dir` | string | `index/<profile>` | Target output directory where generated artifacts will be saved. |

### Output Files Generated

| Output Artifact | Format | Description |
| :--- | :---: | :--- |
| `index/<profile>/diagram_process_flow_<id>.mmd` | Mermaid | Phase-partitioned flowchart with cycle times, costs, and auto rates. |
| `index/<profile>/diagram_raci_swimlanes_<id>.mmd` | Mermaid | Cross-functional swimlane diagram highlighting Responsible (R) handoffs. |
| `index/<profile>/diagram_system_architecture.mmd` | Mermaid | IT systems topology and parent-child integration links. |
| `index/<profile>/diagram_raci_matrix.md` | Markdown | 2D operational execution matrix with Segregation of Duties (SoD) analysis. |
| `index/<profile>/diagram_daci_matrix.md` | Markdown | 2D decision authority matrix with Single Approver rule verification. |
| `index/<profile>/diagrams_summary.md` | Markdown | Consolidated GitHub-renderable Mermaid pack containing all views. |
| `index/<profile>/value_chain_visualizer.html` | HTML | Standalone interactive executive Single-Page Application (SPA). |

---

## 3. Quantitative Scenario Simulator (`simulate_scenario.py`)

### Synopsis
```bash
uv run tools/simulate_scenario.py [--profile PROFILE_ID] <path_or_id_of_scenario>
```

### Purpose
Calculates the operational impact of disruption shocks on process lead times, unit costs, automation levels, and error rates, pinpointing critical-path bottlenecks under specific industry profile contexts.

### CLI Arguments & Options
- `--profile PROFILE_ID`: Target industry profile (default: `manufacturing`).
- `<path_or_id_of_scenario>`: Path or identifier of a scenario JSON file (e.g. `scenario_project_margin_slippage` or `profiles/professional_services/simulations/scenario_project_margin_slippage.json`).

### Execution Behavior
1. Loads `index/<profile>/knowledge_graph.json` (auto-builds if missing).
2. Filters process elements matching the scenario's `target_lifecycle` that belong to the active profile.
3. Evaluates all shocks targeting each element, applying multiplicative scalers ($M$) and additive deltas ($\Delta$).
4. Computes baseline vs. shocked lead time (hours) and unit cost ($), incorporating error-rework multipliers.
5. Writes an executive Markdown report to `index/<profile>/simulation_report_<scenario_id>.md`.

### Example Commands
```bash
# Discrete Manufacturing Scenarios:
uv run tools/simulate_scenario.py --profile manufacturing scenario_credit_hold_surge
uv run tools/simulate_scenario.py --profile manufacturing scenario_raw_material_stockout

# Professional Services Scenarios:
uv run tools/simulate_scenario.py --profile professional_services scenario_project_margin_slippage
uv run tools/simulate_scenario.py --profile professional_services scenario_consultant_bench_surge
uv run tools/simulate_scenario.py --profile professional_services scenario_psa_outage_billing_crunch

# Core Back-Office Scenarios:
uv run tools/simulate_scenario.py --profile core scenario_close_period_crunch
uv run tools/simulate_scenario.py --profile core scenario_supplier_disruption
uv run tools/simulate_scenario.py --profile core scenario_invoice_bottleneck
uv run tools/simulate_scenario.py --profile core scenario_erp_outage
uv run tools/simulate_scenario.py --profile core scenario_controller_absence_surge
uv run tools/simulate_scenario.py --profile core scenario_payroll_outage_surge
```

---

## 4. Industry Profile Scaffolding CLI (`new_profile.py`)

### Synopsis
```bash
uv run tools/new_profile.py <profile_id> [--extends PARENT_PROFILE] [--name DISPLAY_NAME]
```

### Purpose
Automates the creation of directory trees, boilerplate configuration, and manifest files for a new industry overlay.

### Generated Structure
```
profiles/<profile_id>/
├── profile.json               # Profile manifest declaring extends, lifecycles, and industry
├── ontology/taxonomies.json   # Industry lifecycle and RACI definitions
├── elements/                  # Process steps, streams, policies, KPIs, data entities
├── roles/                     # Industry-specific role definitions
├── assets/                    # Industry-specific system nodes
├── lifecycles/                # JSON lifecycle manifests
├── simulations/               # Disruption scenario JSON definitions
└── patches/                   # Base element patches (*.yaml)
```

### Example
```bash
uv run tools/new_profile.py aerospace --extends manufacturing --name "Aerospace & Defense"
```
