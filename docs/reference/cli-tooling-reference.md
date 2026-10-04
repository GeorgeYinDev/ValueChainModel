# CLI Tooling & Engine Reference Manual

This document provides a comprehensive technical reference for the command-line interface (CLI) tools in the `tools/` directory.

---

## 1. Model Validator & Knowledge Graph Builder (`validate_and_build.py`)

### Synopsis
```bash
python3 tools/validate_and_build.py
```

### Purpose
The primary validation and build orchestrator for the repository. It ingests all Markdown elements, roles, assets, and lifecycle manifests, performs schema and relational integrity checks (verifying all targets exist), compiles the unified graph database, generates LLM context prompt packs, and triggers diagram exports.

### Execution Sequence & Checks
1. **Role Ingestion**: Scans `roles/*.md` and compiles the enterprise role registry.
2. **Asset Ingestion**: Scans `assets/*.md` and verifies parent-child hierarchy linkages.
3. **Element Ingestion**: Parses YAML frontmatter across `elements/**/*.md`.
4. **Relational & Integrity Validation**:
   - Verifies that every role in `raci:` and `daci:` exists in `roles/`.
   - Auto-derives DACI roles if omitted from frontmatter.
   - Verifies that all `asset_dependencies:` exist in `assets/`.
   - Validates that `graph_relations:` targets exist and are reachable.
5. **Knowledge Graph Compilation**: Writes consolidated JSON database to `index/knowledge_graph.json`.
6. **LLM Prompt Pack Generation**: Compiles standalone context packs per lifecycle into `index/llm_context_<lifecycle_id>.md`.
7. **Downstream Pipeline Trigger**: Automatically invokes `tools/export_diagram.py --lifecycle ALL --format all`.

### Exit Codes
- `0`: Validation and build succeeded with zero defects.
- `1`: Validation failed due to missing roles, invalid asset links, or malformed YAML.

---

## 2. Diagram & Interactive Visualizer Exporter (`export_diagram.py`)

### Synopsis
```bash
python3 tools/export_diagram.py [--lifecycle LIFECYCLE_ID] [--format FORMAT] [--output-dir DIR]
```

### CLI Arguments

| Argument | Type | Default | Description |
| :--- | :---: | :---: | :--- |
| `--lifecycle` | string | `S2P` | Target lifecycle scope to filter. Options: `S2P`, `O2C`, `R2R`, `ALL`. |
| `--format` | string | `all` | Output artifact format. Choices: `mermaid`, `markdown`, `html`, `all`. |
| `--output-dir` | string | `index` | Target directory where generated artifacts will be saved. |

### Output Files Generated

| Output Artifact | Format | Description |
| :--- | :---: | :--- |
| `index/diagram_process_flow_<id>.mmd` | Mermaid | Subgraph-partitioned flowchart with cycle times, costs, and auto rates. |
| `index/diagram_raci_swimlanes_<id>.mmd` | Mermaid | Cross-functional swimlane diagram highlighting Responsible (R) handoffs. |
| `index/diagram_system_architecture.mmd` | Mermaid | Enterprise IT systems topology and parent-child integration links. |
| `index/diagram_raci_matrix.md` | Markdown | 2D operational execution matrix with Segregation of Duties (SoD) analysis. |
| `index/diagram_daci_matrix.md` | Markdown | 2D decision authority matrix with Single Approver rule verification. |
| `index/diagrams_summary.md` | Markdown | Consolidated GitHub-renderable Mermaid pack containing all views. |
| `index/value_chain_visualizer.html` | HTML | Standalone interactive executive Single-Page Application (SPA). Note: Requires active internet connection to load Mermaid.js via CDN. |

### Example Commands
```bash
# Export only Mermaid diagrams for R2R
python3 tools/export_diagram.py --lifecycle R2R --format mermaid

# Export markdown RACI and DACI governance tables
python3 tools/export_diagram.py --lifecycle ALL --format markdown

# Compile the standalone interactive dashboard
python3 tools/export_diagram.py --lifecycle ALL --format html
```

---

## 3. Quantitative Scenario Simulator (`simulate_scenario.py`)

### Synopsis
```bash
python3 tools/simulate_scenario.py <path_to_scenario.json>
```

### Purpose
Calculates the operational impact of disruption shocks on process lead times, unit costs, automation levels, and error rates, pinpointing critical-path bottlenecks.

### Positional Arguments
- `<path_to_scenario.json>`: Path to a valid scenario payload conforming to [`schema/scenario_simulation.schema.json`](../../schema/scenario_simulation.schema.json).

### Execution Behavior
1. Loads `index/knowledge_graph.json` (auto-builds if missing).
2. Filters process elements matching the scenario's `target_lifecycle`.
3. Evaluates all shocks targeting each element, applying multiplicative scalers ($M$) and additive deltas ($\Delta$).
4. Computes baseline vs. shocked lead time (hours) and unit cost ($).
5. Compiles executive Markdown report to `index/simulation_report_<scenario_id>.md`.

### Example Commands
```bash
# Simulate Month-End Close Crunch (R2R)
python3 tools/simulate_scenario.py simulations/scenario_close_period_crunch.json

# Simulate Customer Credit Hold Contraction (O2C)
python3 tools/simulate_scenario.py simulations/scenario_credit_hold_surge.json

# Simulate Supplier Disruption (S2P)
python3 tools/simulate_scenario.py simulations/scenario_supplier_disruption.json
```
