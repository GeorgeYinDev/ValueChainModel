# Change Log

All notable changes to the Enterprise Value Chain Modeling Engine repository will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.8.0] - 2026-10-05

### Added
- **Multi-Industry Profile Inheritance Architecture (`profiles/`)**: Restructured the monolithic repository into a layered profile architecture with `profiles/core`, `profiles/manufacturing`, and `profiles/professional_services`.
- **Profile Loader Engine (`tools/vcm_profiles.py`)**: Resolves multi-layer profile inheritance, merges taxonomies, validates manifests and patches with schemas, and prevents accidental cross-layer ID collisions.
- **JSON Schemas for Profiles**: Added `schema/profile_manifest.schema.json` and `schema/profile_patch.schema.json`; updated `value_chain_element.schema.json` with `overrides:` and `lifecycle_manifest.schema.json` with data-driven `phases:`.
- **Profile Scaffolding CLI (`tools/new_profile.py`)**: Single-command generator for bootstrapping new industry overlays.
- **Global Build Mode & Switcher Dashboard (`index/index.html`)**: Added `--profile ALL` and an interactive profile switcher landing dashboard.
- **Professional Services Operating Model**: Initialized `L2C` (Lead-to-Cash) and `E2C` (Engagement-to-Cash) lifecycles, consulting roles, and `asset_psa_system`.
- **Architecture Governance Records**: Added ADR-0007 (Industry Profiles Architecture) and ADR-0008 (Professional Services Taxonomy).
- **Profile Test Suite**: Added `tests/test_profiles.py` and fixture profiles covering inheritance, cycle rejection, collision prevention, overrides, and isolation guarantees.

### Changed
- All CLI tools (`tools/validate_and_build.py`, `tools/simulate_scenario.py`, `tools/export_diagram.py`) accept `--profile <name>` (defaulting to `VCM_PROFILE` or `manufacturing`).
- Diagram exporter replaces hardcoded element prefixes with data-driven `phases` declared in lifecycle manifests.
- Output artifacts are cleanly isolated into `index/<profile>/`.

## [1.7.0] - 2026-10-04

### Added
- **Plan-to-Make (P2M) Lifecycle**: Full 6-milestone discrete manufacturing lifecycle (`p2m_001` through `p2m_006`) covering Demand Sensing, MRP Planning, Production Sequencing, Shop Floor Execution, Quality Release, and Finished Goods Put-Away.
- **Manufacturing Systems & Roles**: Added MES (`asset_mes_system`), APS (`asset_aps_planner`), and WMS (`asset_wms_system`), alongside roles for Demand Planner, Inventory Manager, Manufacturing Supervisor, Production Scheduler, and QA Engineer.
- **Manufacturing Disruption Scenarios**: Added Raw Material Stockout scenario (`simulations/scenario_raw_material_stockout.json`).
- **ADR-0006**: Plan-to-Make taxonomy design.

## [1.6.0] - 2026-10-04

### Added
- **Hire-to-Retire (H2R) Lifecycle**: Full 6-milestone HR operations model (`h2r_001` through `h2r_006`) from Job Requisition through Payroll Enrollment and Offboarding.
- **HCM & Payroll Integration**: Added `asset_hcm_platform` and `asset_payroll_engine` integrated into R2R general ledger recording.
- **ADR-0005**: Hire-to-Retire taxonomy design.
- **Payroll Outage Scenario**: Added `scenario_payroll_outage_surge.json`.

## [1.5.0] - 2026-10-04

### Added
- **Model Enrichment & Quantitative Calibration**: First-class KPI elements, data entity elements, and capacity fields for queueing theory modeling.
- **Approval Limit Enforcement**: Automated cross-validation between role approval limits and process step thresholds.

## [1.4.0] - 2026-10-03

### Fixed
- **Integrity Release**: Enforced JSON schema validation across all elements, assets, and lifecycles; single approver rule enforcement ($|A|=1$); eliminated simulation double-counting; fixed policy self-referencing loops; added automated pytest suite and CI workflow.

## [1.3.0] - 2026-10-03

### Added
- **Comprehensive Architecture Documentation Suite (`docs/architecture/`)**:
  - `docs/architecture/core-financial-triad.md`: Detailed architecture specification for the end-to-end Core Financial Triad (S2P $\longleftrightarrow$ O2C $\longleftrightarrow$ R2R).
  - `docs/architecture/governance-raci-daci.md`: Governance specification for dual RACI and DACI models, Single Approver rule enforcement, and SoD conflict detection.
- **Practitioner & Modeling Guides (`docs/guides/`)**:
  - `docs/guides/authoring-elements-and-lifecycles.md`: Step-by-step authoring manual.
  - `docs/guides/quantitative-scenario-simulation.md`: Mathematical modeling guide.
- **CLI Reference & Scaffolding Templates**:
  - `docs/reference/cli-tooling-reference.md`.
  - `templates/lifecycle_template.json` and `templates/scenario_template.json`.

## [1.2.0] - 2026-10-03

### Added
- **Record-to-Report (R2R) Business Lifecycle**: Full 5-milestone financial accounting and reporting model (`r2r_001` through `r2r_005`).
- **Core Financial Triad Integration**: Connected S2P payment settlement (`s2p_008`) and O2C cash reconciliation (`o2c_005`) into R2R (`r2r_001`).
- **Financial Governance**: SOX 404 Controls Policy (`sox_financial_reporting_controls_policy.md`).
- **Close Period Crunch Simulation**: `scenario_close_period_crunch.json`.
- **ADR-0004**: Record-to-Report taxonomy design.

## [1.1.0] - 2026-10-03

### Added
- **Order-to-Cash (O2C) Business Lifecycle**: Full 5-milestone commercial execution model (`o2c_001` through `o2c_005`).
- **DACI Decision Authority Matrix**: Integrated DACI governance alongside RACI with Single Approver verification.
- **Commercial Governance Policies**: Commercial Credit Limit Policy and Credit Hold Surge scenario.
- **Interactive Standalone Executive Dashboard**: Re-architected `index/value_chain_visualizer.html` as an SPA.
- **ADR-0003**: Order-to-Cash taxonomy design.

## [1.0.0] - 2026-08-08

### Added
- **Core Engine Architecture**: Schema-driven validation engine based on the WorldBuild composable model framework.
- **JSON Schemas**: Strict validation schemas for frontmatter elements, business lifecycle manifests, asset hierarchies, and scenario simulations (`schema/`).
- **Source to Pay (S2P) Lifecycle**: Complete 8-step lifecycle model (`s2p_001` through `s2p_008`).
- **Enterprise Roles & Assets**: Core procurement roles and enterprise ERP, e-Procurement Portal, and Banking Payment Gateway assets.
- **Scenario Simulation CLI**: Scenario evaluator (`tools/simulate_scenario.py`) for disruptions and outages.
- **ADR-0001 & ADR-0002**: Initial architecture decisions.
