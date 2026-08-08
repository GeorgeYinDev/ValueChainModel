# Change Log

All notable changes to the Enterprise Value Chain Modeling Engine repository will be documented in this file.

The format is based on [Keep a Changelog](https.keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
