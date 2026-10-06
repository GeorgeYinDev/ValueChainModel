# ADR 0007: Multi-Industry Profile Taxonomy Inheritance Architecture

## Status
Accepted

## Context
The Enterprise Value Chain Modeling Engine initially maintained a flat global repository of value chain elements, lifecycles, RACI roles, and IT assets. However, enterprise operating models vary significantly across industries:
- Discrete manufacturing organizations require Plan-to-Make (P2M), Order-to-Cash (O2C) for physical fulfillment, and systems like MES, WMS, and APS planners.
- Professional services and consulting organizations operate Lead-to-Cash (L2C) and Engagement-to-Cash (E2C), tracking billable hours, project margins, resource scheduling, and Professional Services Automation (PSA) tools.
- Yet both industries share enterprise back-office functions: Record-to-Report (R2R), Hire-to-Retire (H2R), Source-to-Pay (S2P), Segregation of Duties (SoD), SOX financial controls, Core ERP, and HCM platforms.

Duplicating shared elements across separate industry silos causes code drift, maintenance overhead, and breaks cross-industry EA benchmarks.

## Decision
We established a layered, composable profile inheritance architecture:
1. **Profiles Root Hierarchy (`profiles/`)**:
   - `profiles/core/`: Industry-agnostic foundation containing shared lifecycles (`S2P`, `R2R`, `H2R`), governance policies (SOX 404, SoD spending limits), core enterprise roles, and shared assets (ERP, HCM, Payment Gateway).
   - `profiles/manufacturing/`: Discrete manufacturing overlay extending `core` (`extends: ["core"]`), adding `P2M` and `O2C` lifecycles, manufacturing roles, plant systems (MES, WMS, APS), and supply-chain disruption simulations.
   - `profiles/professional_services/`: Services overlay extending `core` (`extends: ["core"]`), adding `L2C` and `E2C` lifecycles, consulting roles (Practice Director, Engagement Manager, Solution Architect), PSA systems, and project billing flows.
2. **Profile Manifests (`profile.json`)**:
   - Enforced by `schema/profile_manifest.schema.json`.
   - Declares `profile_id`, `name`, `industry`, `version`, `extends`, `lifecycles`, and `default_lifecycle`.
3. **Layer Resolution & Collision Rules (`tools/vcm_profiles.py`)**:
   - **Resolution Order**: Walks `extends` depth-first to produce an inheritance sequence (e.g. `["core", "manufacturing"]`). Cycles are rejected at compile time.
   - **Collision Prevention**: If a child profile introduces an element ID identical to an inherited element, build fails unless the child element explicitly declares `overrides: <layer_id>`.
   - **Non-Destructive Overlays via Patches (`patches/*.yaml`)**: Child profiles can append relationships (`graph_relations`), tags, and lifecycle bindings to inherited elements without copying or mutating the source files. Enforced by `schema/profile_patch.schema.json`.
   - **Isolation Guarantee**: The `core` profile must compile cleanly on its own (`--profile core`), proving zero leakage of industry-specific dependencies into shared architecture.
4. **Partitioned Build Artifacts**:
   - Compiles indexes, context packs, and visualizers into `index/<profile>/`.
   - Provides a root profile switcher dashboard at `index/index.html`.

## Consequences
- **Positive**: Zero duplication of common financial, HR, and procurement processes; complete isolation between manufacturing and services models; seamless support for future industry profiles (Healthcare, Retail, Banking).
- **Tooling Impact**: CLI commands now accept `--profile <name>` (defaulting to `manufacturing` or `VCM_PROFILE` environment variable) and `--profile ALL` for global compilation.
