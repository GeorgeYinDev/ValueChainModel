# Enterprise Value Chain Modeling Engine

A composable, schema-driven framework for Enterprise Architects to model, validate, index, and simulate business process lifecycles, value streams, RACI operational execution, DACI decision authority, system asset hierarchies, and operational disruption scenarios.

Designed to adapt the multi-tiered detail engine from the **WorldBuild** architecture for enterprise architecture modeling (TOGAF / APQC / SCOR alignment).

---

## 📁 Repository Directory Structure

```
/mnt/ssd-data/AntigravityData/AG2/ValueChainModel/
├── README.md                           # Repository documentation & architecture guide
├── ROADMAP.md                          # Master implementation plan & strategic release roadmap
├── CHANGELOG.md                        # Versioned change history & release log
├── GEMINI.md                           # Agent instructions, LOD invariants & execution commands
├── docs/
│   ├── decisions/                      # Architecture Decision Records (ADRs 0001 - 0004)
│   ├── architecture/                   # Enterprise Architecture Deep Dives
│   │   ├── core-financial-triad.md     # Cross-lifecycle S2P ⟷ O2C ⟷ R2R integration
│   │   └── governance-raci-daci.md     # Dual RACI vs. DACI & Single Approver governance
│   ├── guides/                         # Practitioner & Authoring Guides
│   │   ├── authoring-elements-and-lifecycles.md # Modeling guide for EA architects
│   │   └── quantitative-scenario-simulation.md  # Queueing math & multi-shock modeling
│   └── reference/                      # Engine CLI Reference
│       └── cli-tooling-reference.md    # CLI syntax, arguments, flags & output schemas
├── schema/                             # JSON Schemas enforcing metadata & frontmatter validation
│   ├── value_chain_element.schema.json # Element frontmatter validation schema (RACI & DACI)
│   ├── lifecycle_manifest.schema.json  # Lifecycle blueprint validation schema
│   ├── asset_hierarchy.schema.json     # System asset node validation schema
│   └── scenario_simulation.schema.json # Scenario simulation payload schema
├── ontology/                           # EA taxonomies, RACI & DACI definitions, graph relation types
│   └── taxonomies.json
├── lifecycles/                         # Business Lifecycle Presets & Manifests
│   ├── source_to_pay.json              # Source-to-Pay (S2P) Lifecycle Manifest (8 milestones)
│   ├── order_to_cash.json              # Order-to-Cash (O2C) Lifecycle Manifest (5 milestones)
│   └── record_to_report.json           # Record-to-Report (R2R) Lifecycle Manifest (5 milestones)
├── templates/                          # Boilerplate templates for new elements
│   ├── element_template.md             # Process step / policy / stream template
│   ├── role_template.md                # Enterprise role definition template
│   ├── asset_template.md               # Enterprise IT system node template
│   ├── lifecycle_template.json         # Business lifecycle manifest JSON template
│   ├── scenario_template.json          # Operational scenario shock JSON template
│   └── visualizer_template.html        # Interactive visualizer dashboard template
├── elements/                           # Value Chain Core Elements (Markdown + YAML Frontmatter)
│   ├── process_steps/                  # Granular Process Milestones
│   │   ├── s2p_001 .. s2p_008          # S2P Strategic Sourcing & P2P steps
│   │   ├── o2c_001 .. o2c_005          # O2C Quote-to-Cash steps
│   │   └── r2r_001 .. r2r_005          # R2R Financial Accounting & Reporting steps
│   ├── value_streams/                  # End-to-End Value Streams
│   │   ├── strategic_sourcing_stream.md
│   │   ├── procure_to_pay_stream.md
│   │   ├── order_fulfillment_stream.md
│   │   └── financial_close_reporting_stream.md
│   └── control_policies/               # Governance, Internal Controls & Policies
│       ├── sod_spending_limits_policy.md
│       ├── credit_limit_risk_policy.md
│       └── sox_financial_reporting_controls_policy.md
├── roles/                              # Enterprise Role Definitions & RACI/DACI Maps
│   ├── role_category_manager.md
│   ├── role_procurement_specialist.md
│   ├── role_accounts_payable_clerk.md
│   ├── role_finance_controller.md
│   ├── role_supplier.md
│   ├── role_sales_ops_specialist.md
│   ├── role_credit_manager.md
│   ├── role_warehouse_supervisor.md
│   ├── role_billing_specialist.md
│   ├── role_customer.md
│   ├── role_general_ledger_accountant.md
│   ├── role_consolidation_specialist.md
│   └── role_internal_auditor.md
├── assets/                             # Object Hierarchies of Enterprise Assets & Infrastructure
│   ├── asset_erp_system.md             # Core Enterprise ERP (SAP S/4HANA)
│   ├── asset_eprocurement_portal.md    # Cloud Procurement Portal
│   ├── asset_payment_gateway.md        # Bank ISO 20022 Disbursement Gateway
│   ├── asset_crm_system.md             # Enterprise Cloud CRM & CPQ (Salesforce)
│   ├── asset_wms_system.md             # Warehouse Management & Dispatch System (SAP EWM)
│   └── asset_financial_consolidation_system.md # Consolidation & Reporting (SAP Group Reporting)
├── simulations/                        # Operational Scenario Simulation Definitions
│   ├── scenario_supplier_disruption.json
│   ├── scenario_invoice_bottleneck.json
│   ├── scenario_erp_outage.json
│   ├── scenario_credit_hold_surge.json
│   └── scenario_close_period_crunch.json
├── index/                              # Auto-generated Knowledge Graph, Diagrams & Dashboards
│   ├── knowledge_graph.json            # Compiled graph database of all entities & relations
│   ├── value_chain_visualizer.html     # Standalone interactive executive web visualizer
│   ├── diagrams_summary.md             # Consolidated GitHub-renderable Mermaid flowcharts
│   ├── diagram_raci_matrix.md          # 2D RACI grid with workload load metrics & SoD analysis
│   ├── diagram_daci_matrix.md          # 2D DACI grid with decision authority & approver verification
│   ├── diagram_process_flow_*.mmd      # Raw Mermaid process flowcharts (O2C, R2R, S2P, ALL)
│   ├── diagram_raci_swimlanes_*.mmd    # Raw Mermaid RACI swimlanes (O2C, R2R, S2P, ALL)
│   ├── diagram_system_architecture.mmd # Raw Mermaid IT systems & asset topology diagram
│   ├── llm_context_s2p.md              # Compiled prompt pack for S2P lifecycle
│   ├── llm_context_o2c.md              # Compiled prompt pack for O2C lifecycle
│   └── llm_context_r2r.md              # Compiled prompt pack for R2R lifecycle
└── tools/                              # Validation, Visualization & Simulation CLI Tooling
    ├── validate_and_build.py           # Model validator, graph linker & index compiler
    ├── export_diagram.py               # Multi-lifecycle Mermaid diagram & visualizer builder
    └── simulate_scenario.py            # Quantitative scenario simulation engine
```

---

## 📚 Documentation Index & Reading Guides

A comprehensive enterprise documentation suite is available in the [`docs/`](docs/) directory:

| Domain | Guide / Specification | Primary Focus & Target Audience |
| :--- | :--- | :--- |
| **Enterprise Architecture** | [Core Financial Triad](docs/architecture/core-financial-triad.md) | End-to-end integration of Source-to-Pay (S2P), Order-to-Cash (O2C), and Record-to-Report (R2R); subledger ingestion mechanics; double-entry balance constraints. |
| **Enterprise Architecture** | [Dual RACI & DACI Governance](docs/architecture/governance-raci-daci.md) | Operational task delivery vs. decision rights; Single Approver rule ($|A|=1$); Segregation of Duties (SoD) toxic combination detection algorithm. |
| **Practitioner Guide** | [Authoring Elements & Lifecycles](docs/guides/authoring-elements-and-lifecycles.md) | Step-by-step authoring manual for process milestones, control policies, value streams, roles, IT assets, and new lifecycle blueprints. |
| **Practitioner Guide** | [Quantitative Scenario Simulation](docs/guides/quantitative-scenario-simulation.md) | Disruption shock mechanics; Kingman queueing math & bottleneck shifts; multi-shock modifier modeling; interpreting sensitivity reports. |
| **Technical Reference** | [CLI Tooling & Engine Reference](docs/reference/cli-tooling-reference.md) | Exhaustive parameter, flag, and output schema reference for `validate_and_build.py`, `export_diagram.py`, and `simulate_scenario.py`. |
| **Strategic Roadmap** | [Master Implementation Plan](ROADMAP.md) | Multi-phase strategic roadmap from Core Financial Triad to H2R, P2P, REST API, and process mining telemetry. |
| **Decisions (ADRs)** | [Architecture Decision Records](docs/decisions/) | ADR-0001 (Framework), ADR-0002 (S2P), ADR-0003 (O2C), and ADR-0004 (R2R Financial Triad). |

---

## 🎯 Detail Tiers (Level of Detail - LOD)

Every process element implements 3 distinct tiers tailored for different enterprise stakeholders:

- **Tier 1 (Executive / Strategic)**: High-level capability overview, strategic alignment, business outcomes, and key enterprise risk drivers.
- **Tier 2 (Operational / Process Architect)**: Detailed workflow steps, RACI execution assignments, DACI decision governance, SLAs, inputs/outputs, and business rules.
- **Tier 3 (Systems & Simulation Engineer)**: IT asset bindings, queueing math, throughput constraints (TPS), cycle times, unit costs, error rates, automation rates, and simulation equations.

---

## 👥 Governance Models: RACI & DACI

The engine supports two complementary governance matrices across all lifecycles:

| Model | Dimensions | Enterprise Focus | Key Principle |
| :--- | :--- | :--- | :--- |
| **RACI** | **R**esponsible, **A**ccountable, **C**onsulted, **I**nformed | Operational Execution & Day-to-Day Task Delivery | Ensures clear operational ownership and delivery roles. |
| **DACI** | **D**river, **A**pprover, **C**ontributor, **I**nformed | Decision Authority & Governance Milestones | **Single Approver Rule**: Exactly one designated Approver (A) per decision to prevent consensus gridlock. |

> [!TIP]
> If an element's frontmatter omits explicit `daci:` keys, [`tools/validate_and_build.py`](tools/validate_and_build.py) automatically derives DACI roles from RACI assignments (`Responsible` $\rightarrow$ `Driver`, `Accountable` $\rightarrow$ `Approver`, `Consulted` $\rightarrow$ `Contributor`, `Informed` $\rightarrow$ `Informed`).

---

## 🔄 Supported Business Lifecycles

### 1. Source to Pay (S2P)
Covers end-to-end strategic procurement from spend analysis to bank disbursement:
- **Milestones**: `s2p_001` (Spend Analysis), `s2p_002` (Supplier Discovery), `s2p_003` (RFx Execution), `s2p_004` (Contracting), `s2p_005` (Requisition & PO), `s2p_006` (Goods Receipt), `s2p_007` (Invoice 3-Way Match), `s2p_008` (Payment Settlement).
- **Core Governance**: Segregation of Duties (SoD) & Spending Limits Policy ([`elements/control_policies/sod_spending_limits_policy.md`](elements/control_policies/sod_spending_limits_policy.md)).
- **Primary Systems**: SAP S/4HANA ERP, Cloud e-Procurement Portal, ISO 20022 Payment Gateway.

### 2. Order to Cash (O2C)
Covers the customer revenue and commercial fulfillment lifecycle from quote capture to cash reconciliation:
- **Milestones**: `o2c_001` (Quote & Order Capture), `o2c_002` (Credit Check & Risk Approval), `o2c_003` (Inventory Allocation & Dispatch), `o2c_004` (Customer Billing & Invoicing), `o2c_005` (Cash Collection & AR Reconciliation).
- **Core Governance**: Commercial Credit Limit & Customer Risk Exposure Policy ([`elements/control_policies/credit_limit_risk_policy.md`](elements/control_policies/credit_limit_risk_policy.md)).
- **Primary Systems**: Salesforce CRM & CPQ, SAP EWM Warehouse Management, SAP S/4HANA ERP, Corporate Payment Gateway.

### 3. Record to Report (R2R)
Covers the corporate general ledger accounting, intercompany matching, group consolidation, and statutory reporting lifecycle:
- **Milestones**: `r2r_001` (Subledger Ingestion & Journal Recording), `r2r_002` (Intercompany Matching & Elimination), `r2r_003` (Balance Sheet Account Substantiation), `r2r_004` (Financial Close & Group Consolidation), `r2r_005` (Statutory, Tax & Management Disclosures).
- **Core Governance**: SOX 404 Financial Reporting Internal Controls & Materiality Thresholds Policy ([`elements/control_policies/sox_financial_reporting_controls_policy.md`](elements/control_policies/sox_financial_reporting_controls_policy.md)).
- **Primary Systems**: SAP S/4HANA ERP, SAP Group Reporting / OneStream (`asset_financial_consolidation_system`).

---

## 📊 Interactive Standalone Executive Visualizer

The visualizer ([`index/value_chain_visualizer.html`](index/value_chain_visualizer.html)) is a **100% standalone, client-side Single-Page Application (SPA)** with zero server dependencies. All knowledge graph metadata, RACI/DACI assignments, operational parameters, and precomputed Mermaid diagrams are compiled directly into the file.

### How to Open
- **Direct Browser File Open**:
  ```bash
  # Linux desktop
  xdg-open index/value_chain_visualizer.html

  # Or open file:///mnt/ssd-data/AntigravityData/AG2/ValueChainModel/index/value_chain_visualizer.html
  ```
- **Local Web Server (Optional for Network Sharing)**:
  ```bash
  python3 -m http.server 8080 --directory index
  # Visit: http://localhost:8080/value_chain_visualizer.html
  ```

### Dashboard Capabilities
1. **Process Flow Pipeline Grid**: Filter by lifecycle (`S2P`, `O2C`, `R2R`, `ALL`), search by step ID or tag, and view SLAs, costs, and automation percentages.
2. **RACI / DACI Decision Matrix**: Interactive toggle between operational RACI and decision DACI grids, dynamically synchronized with the selected lifecycle scope.
3. **Enterprise IT Asset Map**: Visual topology of core applications, APIs, uptime SLAs, throughput limits, and bound process workloads.
4. **Scenario Stress-Testing**: Real-time simulation of operational disruptions (cost shocks, lead time delays, error rate spikes) with bottleneck identification.
5. **Live Mermaid Architecture**: Zero-error dynamic rendering of process flows, governance linkages, RACI swimlanes, and infrastructure topologies across all lifecycle scopes (`S2P`, `O2C`, `R2R`, `ALL`).

---

## 🚀 CLI Commands & Workflows

### 1. Validate Repository & Build Index
Execute the build engine whenever elements, roles, assets, or policies are modified:
```bash
uv run tools/validate_and_build.py --profile manufacturing
```
This automatically:
- Validates frontmatter schemas and cross-references.
- Verifies bi-directional graph relations, asset dependencies, and RACI/DACI roles.
- Compiles the unified knowledge graph (`index/knowledge_graph.json`).
- Compiles LLM prompt context packs (`index/llm_context_s2p.md`, `index/llm_context_o2c.md`, `index/llm_context_r2r.md`).
- Generates all Mermaid diagrams and updates `index/value_chain_visualizer.html`.

### 2. Export Diagrams Directly
Generate Mermaid flowcharts, markdown matrices, and the standalone dashboard for specific lifecycles:
```bash
# Export all formats for Record-to-Report (R2R)
uv run tools/export_diagram.py --lifecycle R2R --format all

# Export all formats for Order-to-Cash (O2C)
uv run tools/export_diagram.py --lifecycle O2C --format all

# Export all formats for Source-to-Pay (S2P)
uv run tools/export_diagram.py --lifecycle S2P --format all

# Export enterprise-wide consolidated views
uv run tools/export_diagram.py --lifecycle ALL --format all
```

### 3. Run Quantitative Operational Simulations
Simulate operational resilience and quantify cycle lead time and unit cost impacts:
```bash
# 1. Year-End Financial Close Crunch & Manual Adjustment Surge (R2R)
uv run tools/simulate_scenario.py simulations/scenario_close_period_crunch.json

# 2. Customer Credit Hold Surge Scenario (O2C)
uv run tools/simulate_scenario.py simulations/scenario_credit_hold_surge.json

# 3. Supplier Disruption Shock Scenario (S2P)
uv run tools/simulate_scenario.py simulations/scenario_supplier_disruption.json

# 4. Invoice Exception & Matching Bottleneck Scenario (S2P)
uv run tools/simulate_scenario.py simulations/scenario_invoice_bottleneck.json

# 5. Enterprise Core ERP Outage Scenario (Global)
uv run tools/simulate_scenario.py simulations/scenario_erp_outage.json
```

---

## 📄 Architecture Governance

Managed under Architecture Decision Records in `docs/decisions/`:
- **ADR-0001**: WorldBuild Architecture Adaptation for Enterprise Value Chains
- **ADR-0002**: Source-to-Pay (S2P) Lifecycle Taxonomy & Governance Design
- **ADR-0003**: Order-to-Cash (O2C) Lifecycle Taxonomy & CRM/WMS System Integration
- **ADR-0004**: Record-to-Report (R2R) Lifecycle Taxonomy, SOX 404 Controls & Consolidation Boundaries

All changes tracked in [`CHANGELOG.md`](CHANGELOG.md).
