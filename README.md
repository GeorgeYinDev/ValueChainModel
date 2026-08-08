# Enterprise Value Chain Modeling Engine

A composable, schema-driven framework for Enterprise Architects to model, validate, index, and simulate business process lifecycles, value streams, RACI role assignments, asset object hierarchies, and operational scenario simulations.

Designed to adapt the multi-tiered detail engine from the **WorldBuild** architecture for enterprise architecture modeling (TOGAF / APQC / SCOR alignment).

---

## 📁 Repository Directory Structure

```
/mnt/ssd-data/AntigravityData/AG2/ValueChainModel/
├── README.md                           # Repository documentation & architecture guide
├── CHANGELOG.md                        # Versioned change history & release log
├── docs/
│   └── decisions/                      # Architecture Decision Records (ADRs)
│       ├── 0001-worldbuild-architecture-adaptation.md
│       └── 0002-s2p-lifecycle-taxonomy-design.md
├── schema/                             # JSON Schemas enforcing metadata & frontmatter validation
│   ├── value_chain_element.schema.json # Element frontmatter validation schema
│   ├── lifecycle_manifest.schema.json  # Lifecycle blueprint validation schema
│   ├── asset_hierarchy.schema.json     # System asset node validation schema
│   └── scenario_simulation.schema.json # Scenario simulation payload schema
├── ontology/                           # EA taxonomies, RACI matrices, & relation graph types
│   └── taxonomies.json
├── lifecycles/                         # Business Lifecycle Presets & Manifests
│   ├── source_to_pay.json              # Source-to-Pay (S2P) Lifecycle Manifest
│   └── order_to_cash.json              # Order-to-Cash (O2C) Lifecycle Manifest
├── templates/                          # Boilerplate templates for new elements
│   ├── element_template.md
│   ├── role_template.md
│   └── asset_template.md
├── elements/                           # Value Chain Core Elements
│   ├── process_steps/                  # S2P Process Steps (s2p_001 .. s2p_008)
│   ├── value_streams/                  # Strategic Sourcing & P2P Stream definitions
│   └── control_policies/               # Segregation of Duties & Spending Limit rules
├── roles/                              # Enterprise Role Definitions & RACI Maps
│   ├── role_category_manager.md
│   ├── role_procurement_specialist.md
│   ├── role_accounts_payable_clerk.md
│   ├── role_finance_controller.md
│   └── role_supplier.md
├── assets/                             # Object Hierarchies of Enterprise Assets
│   ├── asset_erp_system.md             # Core Enterprise ERP node
│   ├── asset_eprocurement_portal.md    # Cloud Procurement Portal node
│   └── asset_payment_gateway.md        # Bank Disbursement Gateway node
├── simulations/                        # Operational Scenario Simulation Definitions
│   ├── scenario_supplier_disruption.json
│   ├── scenario_invoice_bottleneck.json
│   └── scenario_erp_outage.json
├── index/                              # Auto-generated Knowledge Graph & LLM Prompt Packs
│   ├── knowledge_graph.json
│   └── llm_context_source_to_pay.md
└── tools/                              # Validation & Simulation CLI Tooling
    ├── validate_and_build.py           # Model validator, graph linker & index compiler
    └── simulate_scenario.py            # Quantitative scenario simulation engine
```

---

## 🎯 Detail Tiers (Level of Detail - LOD)

Every process element supports 3 levels of detail tailored for different stakeholders:

- **Tier 1 (Executive / Strategic)**: High-level capability overview, strategic alignment, business outcomes, key risk drivers.
- **Tier 2 (Operational / Process Architect)**: Detailed workflow steps, RACI matrices (Responsible, Accountable, Consulted, Informed), SLAs, inputs/outputs, business rules.
- **Tier 3 (Systems & Simulation Engineer)**: Asset bindings, queueing math, throughput constraints, error rates, scenario differential equations.

---

## 🚀 How to Run Validation & Simulations

### 1. Validate Repository & Build LLM Prompt Packs
Run the validator anytime elements, roles, or manifests are created or updated:
```bash
python3 tools/validate_and_build.py
```
This tool:
- Validates frontmatter against `schema/value_chain_element.schema.json`.
- Verifies bi-directional graph linkages and RACI role existence.
- Compiles unified knowledge graph index (`index/knowledge_graph.json`).
- Auto-generates prompt context packs (`index/llm_context_source_to_pay.md`).

### 2. Run Operational Scenario Simulations
Execute what-if scenario simulations to evaluate operational resilience, cost deltas, and bottleneck shifts:
```bash
# Run Supplier Disruption Shock Scenario
python3 tools/simulate_scenario.py simulations/scenario_supplier_disruption.json

# Run Invoice Exception & Approval Bottleneck Scenario
python3 tools/simulate_scenario.py simulations/scenario_invoice_bottleneck.json

# Run ERP Outage Scenario
python3 tools/simulate_scenario.py simulations/scenario_erp_outage.json
```

---

## 📄 License & Governance

Managed under Architecture Decision Records in `docs/decisions/`. All changes tracked in `CHANGELOG.md`.
