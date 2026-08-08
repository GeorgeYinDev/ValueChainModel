# ADR 0001: Adaptation of WorldBuild Architecture for Enterprise Value Chain Modeling

- **Status**: Approved
- **Date**: 2026-08-08
- **Authors**: Enterprise Architecture Team / Antigravity AI

## Context
Enterprise Business Process Lifecycles (such as Source-to-Pay, Order-to-Cash, and Hire-to-Retire) require multi-dimensional modeling across strategic business outcomes, operational RACI assignments, IT system asset dependencies, and quantitative risk/scenario simulations.

Existing enterprise tools often separate process diagrams (BPMN), system architecture (ArchiMate), and financial/simulation math into disparate silos.

The **WorldBuild** repository architecture provides an extensible, composable, markdown-first framework with:
1. Standardized YAML frontmatter for meta-properties and graph linkages.
2. 3-Tier Level of Detail (LOD) section structure.
3. JSON Schema validation for automated integrity checks.
4. Auto-generated Knowledge Graphs and LLM context prompt packs.

## Decision
We adapt the core engine patterns from WorldBuild to build the **Enterprise Value Chain Modeling Engine**:
1. Map **World Types** to **Business Lifecycles** (`S2P`, `O2C`, `R2R`, `H2R`).
2. Map **World Elements** to **Value Chain Elements** (`process_step`, `value_stream`, `control_policy`).
3. Introduce explicit **Role Assignment Objects** with RACI matrices (`roles/`).
4. Introduce **Asset Hierarchy Objects** with parent-child system trees (`assets/`).
5. Map **Simulation Math (Tier 3)** to a Python scenario execution engine (`tools/simulate_scenario.py`) for enterprise what-if stress testing.

## Consequences
- **Positive**: Single source of truth in human-readable Markdown with strict machine-validatable JSON Schemas.
- **Positive**: Enables LLM RAG prompt generation directly from validated enterprise models.
- **Positive**: Provides quantitative scenario simulations directly from process parameters.
- **Negative**: Requires discipline in maintaining bi-directional graph links when adding new elements.
