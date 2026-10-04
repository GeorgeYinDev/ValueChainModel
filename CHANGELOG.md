# Change Log

All notable changes to the Enterprise Value Chain Modeling Engine repository will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.3.0] - 2026-10-03

### Added
- **Comprehensive Architecture Documentation Suite (`docs/architecture/`)**:
  - `docs/architecture/core-financial-triad.md`: Detailed architecture specification for the end-to-end Core Financial Triad (S2P $\longleftrightarrow$ O2C $\longleftrightarrow$ R2R), subledger transaction ingestion mechanics, three-tier LOD mappings, and enterprise IT asset topology.
  - `docs/architecture/governance-raci-daci.md`: Governance specification for dual RACI (operational delivery) and DACI (decision authority) models, Single Approver rule enforcement ($|A|=1$), Segregation of Duties (SoD) toxic combination detection algorithm, and role workload balance analysis.
- **Practitioner & Modeling Guides (`docs/guides/`)**:
  - `docs/guides/authoring-elements-and-lifecycles.md`: Step-by-step authoring manual for process milestones, control policies, value streams, roles, IT assets, and new lifecycle manifests with troubleshooting for common schema validation errors.
  - `docs/guides/quantitative-scenario-simulation.md`: Mathematical modeling guide for discrete-event and shock disruption analysis, Kingman queueing latency, bottleneck shift formulas, and multi-shock modifier mechanics.
- **CLI Tooling & Engine Reference (`docs/reference/`)**:
  - `docs/reference/cli-tooling-reference.md`: Complete syntax, arguments, flags, output artifact schemas, and example commands for `validate_and_build.py`, `export_diagram.py`, and `simulate_scenario.py`.
- **Reusable EA Scaffolding Templates (`templates/`)**:
  - `templates/lifecycle_template.json`: Documented JSON manifest boilerplate conforming to `schema/lifecycle_manifest.schema.json`.
  - `templates/scenario_template.json`: Documented JSON disruption payload boilerplate conforming to `schema/scenario_simulation.schema.json`.
- **Strategic Product Roadmap (`ROADMAP.md`)**:
  - Authored multi-phase master implementation plan establishing completed milestones (Phases 1-4: S2P, O2C, R2R, Documentation) and future roadmap targets (Phase 5: Hire-to-Retire H2R, Phase 6: Plan-to-Produce P2P, Phase 7: REST API microservice, Phase 8: Process mining & ERP event telemetry).
- **Repository Navigator & Agent Rule Synchronization**:
  - Added Documentation Index & Reading Guides table to `README.md`.
  - Updated `GEMINI.md` system guidelines and directory layout to direct agents to the new `docs/` hierarchy and `ROADMAP.md`.

## [1.2.0] - 2026-10-03

### Added
- **Record-to-Report (R2R) Business Lifecycle**: Full 5-milestone financial accounting and reporting model (`r2r_001` through `r2r_005`) covering Subledger Ingestion, Intercompany Matching & Elimination, Balance Sheet Substantiation, Financial Close & Consolidation, and Statutory/Regulatory Disclosures (`lifecycles/record_to_report.json`).
- **Core Financial Triad Integration**: Bi-directionally connected S2P payment settlement (`s2p_008`) and O2C cash reconciliation (`o2c_005`) into R2R general ledger recording (`r2r_001`), completing the unified enterprise financial lifecycle graph.
- **Enterprise Roles Expansion**: Added role definitions for General Ledger Accountant (`roles/role_general_ledger_accountant.md`), Financial Consolidation Specialist (`roles/role_consolidation_specialist.md`), and Internal Auditor (`roles/role_internal_auditor.md`).
- **Enterprise Systems Expansion**: Added Financial Consolidation & Reporting System node (`assets/asset_financial_consolidation_system.md`, SAP Group Reporting / OneStream) as a child system of Core ERP.
- **Financial Governance & Controls**: Added SOX 404 Financial Reporting Internal Controls & Materiality Thresholds Policy (`elements/control_policies/sox_financial_reporting_controls_policy.md`).
- **Financial Close Value Stream**: Added Financial Close, Consolidation & Regulatory Reporting Stream (`elements/value_streams/financial_close_reporting_stream.md`).
- **Close Period Crunch Simulation**: Added Fiscal Year-End Financial Close Crunch stress-test scenario (`simulations/scenario_close_period_crunch.json`).
- **Multi-Shock Simulation Support**: Enhanced `tools/simulate_scenario.py` and `index/value_chain_visualizer.html` to support multiple concurrent shock modifiers on a single process element (e.g. cycle time, cost, error rate).
- **Architecture Governance**: Added Architecture Decision Record ADR-0004 for R2R lifecycle taxonomy, internal controls, and consolidation system boundaries (`docs/decisions/0004-r2r-lifecycle-taxonomy-design.md`).

## [1.1.0] - 2026-10-03

### Added
- **Order-to-Cash (O2C) Business Lifecycle**: Full 5-milestone commercial execution model (`o2c_001` through `o2c_005`) covering Quote-to-Order, Credit Assessment, Warehouse Dispatch, Billing, and AR Reconciliation (`lifecycles/order_to_cash.json`).
- **DACI Decision Authority Matrix**: Integrated DACI governance (Driver, Approver, Contributor, Informed) alongside RACI in schemas, taxonomies, and validation compiler with strict Single Approver rule verification.
- **Enterprise Roles Expansion**: Added role definitions for Sales Operations Specialist, Credit & Risk Manager, Warehouse Supervisor, Billing Specialist, and Customer (`roles/`).
- **Enterprise Systems Expansion**: Added asset object models for Enterprise Cloud CRM & CPQ (Salesforce) and Automated Warehouse Management & Dispatch System (SAP EWM) (`assets/`).
- **Commercial Governance Policies**: Added Commercial Credit Limit & Customer Risk Exposure Policy (`elements/control_policies/credit_limit_risk_policy.md`).
- **Operational Scenario Simulation**: Added Credit Hold Surge stress-test scenario (`simulations/scenario_credit_hold_surge.json`).
- **Interactive Standalone Executive Dashboard**: Re-architected `index/value_chain_visualizer.html` as a standalone client-side Single-Page Application (SPA) with multi-lifecycle scope selectors, RACI/DACI live toggles, and dynamic zero-error Mermaid diagram rendering.
- **Architecture Governance**: Added Architecture Decision Record ADR-0003 for O2C lifecycle taxonomy and CRM/WMS integration (`docs/decisions/0003-o2c-lifecycle-taxonomy-design.md`).

### Fixed
- **Mermaid 10 Layout Parser Conflict**: Resolved Mermaid syntax error in `index/value_chain_visualizer.html` by transitioning to deferred on-demand rendering, sanitizing special characters in labels (`&amp;`, `&quot;`), switching policy shapes to stadium brackets `(["..."])`, declaring value streams in dedicated subgraphs, and eliminating self-referencing relationship loops.

## [1.0.0] - 2026-08-08

### Added
- **Core Engine Architecture**: Schema-driven validation engine based on the WorldBuild composable model framework.
- **JSON Schemas**: Strict validation schemas for frontmatter elements, business lifecycle manifests, asset hierarchies, and scenario simulations (`schema/`).
- **Source to Pay (S2P) Lifecycle**: Complete 8-step lifecycle model (`s2p_001` through `s2p_008`) spanning Strategic Sourcing, Contracting, Procure-to-Pay, Invoice Processing, and Disbursement.
- **Enterprise Roles & RACI Definitions**: Structured role definitions (`roles/`) for Category Manager, Procurement Specialist, AP Clerk, Finance Controller, and Supplier.
- **Enterprise Asset Object Hierarchies**: Parent-child system trees (`assets/`) for Enterprise ERP, Cloud e-Procurement Portal, and Banking Payment Gateway.
- **Scenario Simulation Engine**: CLI tool (`tools/simulate_scenario.py`) for evaluating supplier disruptions, invoice bottlenecks, and system outages.
- **Knowledge Graph & LLM Prompt Indexing**: Validation CLI (`tools/validate_and_build.py`) for automated graph synthesis and context prompt pack compilation (`index/`).
- **Architecture Governance**: Initial Architecture Decision Records ADR-0001 and ADR-0002 (`docs/decisions/`).
