# Change Log

All notable changes to the Enterprise Value Chain Modeling Engine repository will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.10.0] - 2026-10-07

### Added
- **Healthcare Provider & Clinical Systems Domain Model Overlay (`profiles/healthcare/`)**:
  - **Operating Model Overlay**: Created healthcare industry profile inheriting shared back-office capabilities (`R2R`, `H2R`, `S2P`) from `profiles/core`.
  - **Patient Access & Care Delivery (P2D) Lifecycle**: Added 5-milestone clinical journey (`p2d_001` through `p2d_005`) covering Patient Scheduling/Registration, Insurance Clearance & Prior Authorization, Inpatient Admission & Triage, Acute Care Delivery (CPOE / eMAR), and Discharge Planning & Care Transition.
  - **Revenue Cycle Management (RCM) Lifecycle**: Added 6-milestone hospital revenue cycle (`rcm_001` through `rcm_006`) covering Charge Capture & ICD-10/CPT Medical Coding, EDI 837 Claim Scrubbing & Submission, Payer Adjudication & ERA 835 Remittance, Denial Management & Appeals, Patient Billing & Collections, and Cash Posting & Subledger Reconciliation.
  - **Healthcare Roles**: Added `role_attending_physician.md`, `role_triage_nurse.md`, `role_patient_access_specialist.md`, `role_medical_coder.md`, `role_rcm_director.md`, `role_compliance_officer.md`, and `role_patient.md` conforming to Phase 6.2 role frontmatter and financial approval limits.
  - **Clinical & Administrative IT Assets**: Added Electronic Health Record (`asset_ehr_system`), EDI Clearinghouse & Billing Platform (`asset_rcm_clearinghouse`), and Diagnostic PACS & LIS (`asset_pacs_lis_system`).
  - **Enterprise Value Stream Elements**: Added `clinical_patient_care_stream.md` (spanning P2D) and `hospital_revenue_cycle_stream.md` (spanning RCM).
  - **Governance & Control Policies**: Added `hipaa_phi_privacy_policy.md` (minimum necessary rule, audit trails, BAA compliance) and `clinical_prior_auth_medical_necessity_policy.md` (pre-service financial clearance and peer-to-peer review escalation).
  - **First-Class KPI Metric Elements**: Added `kpi_initial_denial_rate.md` (<= 5.0% target), `kpi_days_in_ar.md` (<= 38.0 days target), and `kpi_average_length_of_stay.md` (<= 4.2 days target).
  - **First-Class Data Entity Elements**: Added `data_electronic_health_record.md` (system of record: `asset_ehr_system`) and `data_837_claim_file.md` (system of record: `asset_rcm_clearinghouse`).
  - **Operational Disruption Scenarios**: Added `scenario_clearinghouse_cyberattack_outage.json` (nationwide EDI clearinghouse ransomware outage), `scenario_payer_prior_auth_denial_surge.json` (payer algorithmic claim denial shock), and `scenario_emergency_surge_capacity_crunch.json` (inpatient respiratory epidemic capacity crunch).
  - **Cross-Lifecycle Patch**: Added `s2p_006_goods_services_receipt.yaml` patching core goods receipt to care delivery order execution.
  - **Core Financial Triad Integration**: Integrated hospital cash posting (`rcm_006_cash_posting_reconciliation`) directly into general ledger journal voucher ingestion (`r2r_001_journal_entry_recording`).
  - **Architecture Governance Record**: Added [ADR-0009](docs/decisions/0009-healthcare-operating-model-taxonomy.md) establishing healthcare taxonomy design.
  - **Automated Test Coverage**: Expanded `tests/test_profiles.py` and `tests/test_simulation.py` with healthcare isolation, layer resolution, and simulation tests, reaching 26 automated tests passing.

## [1.9.0] - 2026-10-05

### Added
- **Professional Services Domain Model Expansion (`profiles/professional_services/`)**:
  - **Enterprise Value Stream Elements**: Added `client_engagement_delivery_stream.md` (spanning L2C and E2C) and `consulting_revenue_billing_stream.md` (covering timesheet capture, client acceptance, billing, and GL posting).
  - **Governance & Control Policies**: Added `project_pricing_margin_policy.md` (45% gross margin hurdle rate and rate card discounting limits) and `time_expense_compliance_policy.md` (weekly timesheet lock SLA and expense substantiation rules) linked to process steps via `governed_by`.
  - **First-Class KPI Metric Elements**: Added `kpi_billable_utilization.md` (>= 78.5% target), `kpi_project_gross_margin.md` (>= 45.0% target), and `kpi_deal_win_rate.md` (>= 35.0% target) linked via `impacted_by`.
  - **First-Class Data Entity Elements**: Added `data_statement_of_work.md` (system of record: `asset_crm_system`) and `data_consultant_timesheet.md` (system of record: `asset_psa_system`) linked via `produces_artifact`.
  - **Disruption Scenarios**: Added `scenario_project_margin_slippage.json` (E2C scope creep and margin slippage), `scenario_consultant_bench_surge.json` (L2C presales pipeline stagnation and unassigned bench surge), and `scenario_psa_outage_billing_crunch.json` (E2C PSA cloud outage and billing crunch).
  - **Financial Triad Integration**: Connected professional services billing (`e2c_006_project_billing_invoicing`) directly into core GL subledger ingestion (`r2r_001_journal_entry_recording`).
  - **Automated Simulation Test Suite**: Expanded `tests/test_simulation.py` to validate all three professional services disruption scenarios, bringing test suite to 20 automated tests.

### Changed
- Updated `profiles/professional_services/roles/` to conform to Phase 6.2 role frontmatter standard (`department`, `approval_limit_usd`).
- Enhanced `tools/validate_and_build.py` to robustly evaluate role financial approval limits across root and nested attributes.

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
