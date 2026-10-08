# Enterprise Value Chain Modeling Engine

A composable, schema-driven framework for Enterprise Architects to model, validate, index, and simulate business process lifecycles, value streams, RACI operational execution, DACI decision authority, system asset hierarchies, and operational disruption scenarios across multiple industry domains.

Designed to adapt the multi-tiered detail engine from the **WorldBuild** architecture for enterprise architecture modeling (TOGAF / APQC PCF / SCOR alignment).

---

## 📁 Repository Directory Structure

```
/mnt/ssd-data/AntigravityData/AG2/ValueChainModel/
├── README.md                           # Repository overview & architectural guide
├── ROADMAP.md                          # Master implementation plan & strategic release roadmap
├── CHANGELOG.md                        # Versioned change history & release log
├── GEMINI.md                           # Agent instructions, LOD invariants & execution commands
├── docs/
│   ├── decisions/                      # Architecture Decision Records (ADRs 0001 - 0009)
│   │   ├── 0001-worldbuild-architecture-adaptation.md
│   │   ├── 0002-s2p-lifecycle-taxonomy-design.md
│   │   ├── 0003-o2c-lifecycle-taxonomy-design.md
│   │   ├── 0004-r2r-lifecycle-taxonomy-design.md
│   │   ├── 0005-h2r-taxonomy.md
│   │   ├── 0006-p2m-taxonomy.md
│   │   ├── 0007-industry-profiles-architecture.md
│   │   ├── 0008-professional-services-taxonomy.md
│   │   └── 0009-healthcare-operating-model-taxonomy.md
│   ├── architecture/                   # Enterprise Architecture Deep Dives
│   │   ├── enterprise-value-chain-architecture.md # End-to-end integration across all 9 lifecycles
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
│   ├── scenario_simulation.schema.json # Scenario simulation payload schema
│   ├── profile_manifest.schema.json    # Industry profile definition schema
│   └── profile_patch.schema.json       # Cross-layer profile patch schema
├── profiles/                           # Layered Industry Taxonomy Overlays
│   ├── core/                           # Base back-office capabilities (S2P, R2R, H2R)
│   │   ├── elements/                   # Core process steps, streams, policies, data entities
│   │   ├── roles/                      # Core enterprise roles with approval limits
│   │   ├── assets/                     # Core IT applications (ERP, HCM, Portal, Gateway)
│   │   ├── lifecycles/                 # Core lifecycle manifests
│   │   ├── ontology/taxonomies.json    # Core enterprise taxonomy definitions
│   │   └── simulations/                # Core disruption scenario payloads
│   ├── manufacturing/                  # Discrete Manufacturing overlay (P2M, O2C, MES, WMS)
│   │   ├── elements/                   # Manufacturing process steps, KPIs, policies
│   │   ├── roles/                      # Plant manager, QA, schedulers, warehouse supervisors
│   │   ├── assets/                     # MES, APS planner, WMS systems
│   │   ├── lifecycles/                 # Plan-to-Make and Order-to-Cash manifests
│   │   ├── patches/                    # YAML patches linking core S2P to P2M
│   │   └── simulations/                # Stockout and credit hold disruption scenarios
│   ├── professional_services/          # Consulting & Services overlay (L2C, E2C, PSA)
│   │   ├── elements/                   # L2C and E2C steps, streams, policies, KPIs, data entities
│   │   ├── roles/                      # Practice director, engagement manager, consultant
│   │   ├── assets/                     # PSA platform (Certinia / Kantata)
│   │   ├── lifecycles/                 # Lead-to-Cash and Engagement-to-Cash manifests
│   │   └── simulations/                # Margin slippage, bench surge, and PSA outage scenarios
│   └── healthcare/                     # Healthcare Provider overlay (P2D, RCM, EHR, Clearinghouse)
│       ├── elements/                   # P2D and RCM steps, streams, policies, KPIs, data entities
│       ├── roles/                      # Physician, triage nurse, patient access, coder, RCM director
│       ├── assets/                     # EHR platform, EDI clearinghouse, PACS/LIS
│       ├── lifecycles/                 # Patient-to-Discharge and Revenue Cycle manifests
│       ├── patches/                    # Patch linking core S2P receipt to care delivery
│       └── simulations/                # Clearinghouse cyberattack, prior auth surge, emergency surge
├── templates/                          # Boilerplate templates for new model entities
│   ├── element_template.md             # Process step / policy / stream template
│   ├── role_template.md                # Enterprise role definition template
│   ├── asset_template.md               # Enterprise IT system node template
│   ├── lifecycle_template.json         # Business lifecycle manifest JSON template
│   └── scenario_template.json          # Operational scenario shock JSON template
├── index/                              # Generated Knowledge Graphs, Dashboards & Visualizers
│   ├── index.html                      # Multi-profile landing dashboard and switcher
│   ├── core/                           # Compiled artifacts for Core Back-Office profile
│   ├── manufacturing/                  # Compiled artifacts for Manufacturing profile
│   ├── professional_services/          # Compiled artifacts for Professional Services profile
│   └── healthcare/                     # Compiled artifacts for Healthcare profile
└── tools/                              # Validation, Visualization & Simulation CLI Tooling
    ├── vcm_profiles.py                 # Profile inheritance, patch merging & collision loader
    ├── validate_and_build.py           # Model validator, graph linker & multi-profile compiler
    ├── export_diagram.py               # Data-driven Mermaid diagram & visualizer builder
    ├── simulate_scenario.py            # Quantitative scenario simulation engine
    └── new_profile.py                  # Scaffolding generator for new industry overlays
```

---

## 📚 Documentation Index & Reading Guides

A comprehensive enterprise documentation suite is available in the [`docs/`](docs/) directory:

| Domain | Guide / Specification | Primary Focus & Target Audience |
| :--- | :--- | :--- |
| **Enterprise Architecture** | [The Enterprise Value Chain](docs/architecture/enterprise-value-chain-architecture.md) | End-to-end structural spine unifying all 7 lifecycles, operational material flows, subledger feeds, and IT topology. |
| **Enterprise Architecture** | [Dual RACI & DACI Governance](docs/architecture/governance-raci-daci.md) | Operational task delivery vs. decision rights; Single Approver rule ($|A|=1$); Segregation of Duties (SoD) toxic combination detection algorithm. |
| **Practitioner Guide** | [Authoring Elements & Lifecycles](docs/guides/authoring-elements-and-lifecycles.md) | Step-by-step authoring manual for process milestones, control policies, value streams, roles, IT assets, and new lifecycle blueprints. |
| **Practitioner Guide** | [Quantitative Scenario Simulation](docs/guides/quantitative-scenario-simulation.md) | Disruption shock mechanics; Kingman queueing math & bottleneck shifts; multi-shock modifier modeling; interpreting sensitivity reports. |
| **Technical Reference** | [CLI Tooling & Engine Reference](docs/reference/cli-tooling-reference.md) | Exhaustive parameter, flag, and output schema reference for `validate_and_build.py`, `export_diagram.py`, `simulate_scenario.py`, and `new_profile.py`. |
| **Strategic Roadmap** | [Master Implementation Plan](ROADMAP.md) | Multi-phase strategic roadmap from Core Financial Triad to H2R, P2M, Multi-Industry Profiles, and Professional Services. |
| **Decisions (ADRs)** | [Architecture Decision Records](docs/decisions/) | ADR-0001 through ADR-0008 documenting all lifecycle, framework, and profile governance decisions. |

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
| **DACI** | **D**river, **A**pprover, **C**ontributor, **I**nformed | Decision Authority & Governance Milestones | **Single Approver Rule**: Exactly one designated Approver ($|A|=1$) per decision to prevent consensus gridlock. |

> [!TIP]
> If an element's frontmatter omits explicit `daci:` keys, [`tools/validate_and_build.py`](tools/validate_and_build.py) automatically derives DACI roles from RACI assignments (`Responsible` $\rightarrow$ `Driver`, `Accountable` $\rightarrow$ `Approver`, `Consulted` $\rightarrow$ `Contributor`, `Informed` $\rightarrow$ `Informed`).

---

## 🔄 Supported Business Lifecycles

The engine models 7 enterprise lifecycles across horizontal and industry-specific profiles:

### 1. Source to Pay (S2P) — Core Back-Office
Covers end-to-end strategic procurement from spend analysis to bank disbursement:
- **Milestones**: `s2p_001` (Spend Analysis), `s2p_002` (Supplier Discovery), `s2p_003` (RFx Execution), `s2p_004` (Contracting), `s2p_005` (Requisition & PO), `s2p_006` (Goods Receipt), `s2p_007` (Invoice 3-Way Match), `s2p_008` (Payment Settlement).
- **Core Governance**: Segregation of Duties (SoD) & Spending Limits Policy.
- **Primary Systems**: SAP S/4HANA ERP, Cloud e-Procurement Portal, ISO 20022 Payment Gateway.

### 2. Order to Cash (O2C) — Manufacturing Profile
Covers the customer revenue and commercial fulfillment lifecycle from quote capture to cash reconciliation:
- **Milestones**: `o2c_001` (Quote & Order Capture), `o2c_002` (Credit Check & Risk Approval), `o2c_003` (Inventory Allocation & Dispatch), `o2c_004` (Customer Billing & Invoicing), `o2c_005` (Cash Collection & AR Reconciliation).
- **Core Governance**: Commercial Credit Limit & Customer Risk Exposure Policy.
- **Primary Systems**: Salesforce CRM & CPQ, SAP EWM Warehouse Management, SAP S/4HANA ERP.

### 3. Record to Report (R2R) — Core Back-Office
Covers corporate general ledger accounting, intercompany matching, group consolidation, and statutory reporting:
- **Milestones**: `r2r_001` (Subledger Ingestion & Journal Recording), `r2r_002` (Intercompany Matching & Elimination), `r2r_003` (Balance Sheet Account Substantiation), `r2r_004` (Financial Close & Group Consolidation), `r2r_005` (Statutory Disclosures).
- **Core Governance**: SOX 404 Financial Reporting Internal Controls & Materiality Thresholds Policy.
- **Primary Systems**: SAP S/4HANA ERP, SAP Group Reporting / OneStream (`asset_financial_consolidation_system`).

### 4. Hire to Retire (H2R) — Core Back-Office
Covers human capital management, talent onboarding, payroll processing, and separation settlement:
- **Milestones**: `h2r_001` (Job Requisition), `h2r_002` (Candidate Screening), `h2r_003` (Offer Letter & Onboarding), `h2r_004` (Payroll & Benefits Enrollment), `h2r_005` (Performance & Compensation Review), `h2r_006` (Separation & Offboarding Settlement).
- **Integrations**: Feeds payroll expenses and tax liabilities into `r2r_001`.
- **Primary Systems**: Workday HCM (`asset_hcm_platform`), ADP Payroll Engine (`asset_payroll_engine`).

### 5. Plan to Make (P2M) — Manufacturing Profile
Covers manufacturing operations from demand forecasting through shop-floor execution to warehouse put-away:
- **Milestones**: `p2m_001` (Demand Sensing), `p2m_002` (MRP Planning), `p2m_003` (Production Order Release), `p2m_004` (Manufacturing Execution), `p2m_005` (Quality Inspection Release), `p2m_006` (Finished Goods Put-away).
- **Integrations**: Ingests raw materials from S2P (`s2p_006`), supplies Available-to-Promise (ATP) inventory to O2C (`o2c_003`).
- **Primary Systems**: MES (`asset_mes_system`), APS Planner (`asset_aps_planner`), WMS (`asset_wms_system`).

### 6. Lead to Cash (L2C) — Professional Services Profile
Covers commercial pipeline development, technical scoping, rate card application, and SOW contracting:
- **Milestones**: `l2c_001` (Lead Qualification), `l2c_002` (Proposal Development & Scoping), `l2c_003` (Contract Negotiation & Legal Review), `l2c_004` (Deal Closure & Handover).
- **Core Governance**: Project Pricing & Target Gross Margin Governance Policy (45% GM hurdle).
- **Primary Systems**: Salesforce CRM (`asset_crm_system`), Professional Services Automation (`asset_psa_system`).

### 7. Engagement to Cash (E2C) — Professional Services Profile
Covers service fulfillment, consultant time/expense tracking, client acceptance, and project invoicing:
- **Milestones**: `e2c_001` (Project Kickoff), `e2c_002` (Resource Scheduling), `e2c_003` (Project Execution & Delivery), `e2c_004` (Time & Expense Logging), `e2c_005` (Client Review & Acceptance), `e2c_006` (Project Billing & Invoicing), `e2c_007` (Project Closure & Lessons Learned).
- **Core Governance**: Consultant Time & Expense Submission Compliance Policy (Monday 10 AM cutoff).
- **Integrations**: Connects directly to `r2r_001` for General Ledger subledger ingestion and revenue recognition.
- **Primary Systems**: PSA Platform (`asset_psa_system`), Core ERP (`asset_erp_system`).

### 8. Patient to Discharge (P2D) — Healthcare Profile
Covers acute inpatient and ambulatory clinical care delivery, patient access, and transition of care:
- **Milestones**: `p2d_001` (Registration & Scheduling), `p2d_002` (Insurance Verification & Prior Auth), `p2d_003` (Clinical Admission & Triage), `p2d_004` (Care Delivery & Order Execution), `p2d_005` (Discharge Planning & Transition).
- **Core Governance**: HIPAA Security, Privacy & PHI Governance Policy; Medical Necessity & Prior Auth Policy.
- **Integrations**: Ingests medical supplies from S2P (`s2p_006`); triggers encounter charge capture in RCM (`rcm_001`).
- **Primary Systems**: Epic / Cerner EHR (`asset_ehr_system`), Diagnostic PACS/LIS (`asset_pacs_lis_system`).

### 9. Revenue Cycle Management (RCM) — Healthcare Profile
Covers healthcare clinical-financial translation, electronic claim clearinghouse scrubbing, denial recovery, and cash posting:
- **Milestones**: `rcm_001` (Charge Capture & Coding), `rcm_002` (Claim Scrubbing & Submission), `rcm_003` (Payer Adjudication & Remittance), `rcm_004` (Denial Management & Appeals), `rcm_005` (Patient Billing & Collections), `rcm_006` (Cash Posting & Reconciliation).
- **Core Governance**: Medical Necessity & Prior Authorization Governance Policy.
- **Integrations**: Cash posting (`rcm_006`) feeds directly into General Ledger journal recording (`r2r_001`).
- **Primary Systems**: EDI Clearinghouse & Billing Platform (`asset_rcm_clearinghouse`), EHR Platform (`asset_ehr_system`), ERP GL (`asset_erp_system`).

---

## 📊 Interactive Standalone Executive Visualizers

Each profile compiles an independent, **100% standalone Single-Page Application (SPA)** with zero server dependencies:

- **Global Profile Switcher Dashboard**: [`index/index.html`](index/index.html)
- **Healthcare Visualizer**: [`index/healthcare/value_chain_visualizer.html`](index/healthcare/value_chain_visualizer.html)
- **Professional Services Visualizer**: [`index/professional_services/value_chain_visualizer.html`](index/professional_services/value_chain_visualizer.html)
- **Manufacturing Visualizer**: [`index/manufacturing/value_chain_visualizer.html`](index/manufacturing/value_chain_visualizer.html)
- **Core Back-Office Visualizer**: [`index/core/value_chain_visualizer.html`](index/core/value_chain_visualizer.html)

### How to Open
```bash
# Open global dashboard in default Linux browser
xdg-open index/index.html

# Or serve locally:
python3 -m http.server 8080 --directory index
# Visit: http://localhost:8080
```

---

## 🚀 CLI Commands & Workflows

### 1. Validate Repository & Build Index
Execute the build engine whenever elements, roles, assets, or policies are modified:
```bash
# Validate and build all profiles and update landing dashboard:
uv run tools/validate_and_build.py --profile ALL

# Or target a specific profile:
uv run tools/validate_and_build.py --profile professional_services
uv run tools/validate_and_build.py --profile manufacturing
uv run tools/validate_and_build.py --profile core
```

### 2. Export Diagrams
Generate Mermaid flowcharts, markdown matrices, and dashboards for specific lifecycles:
```bash
# Export all diagrams for professional services
uv run tools/export_diagram.py --profile professional_services --lifecycle ALL --format all

# Export only Mermaid process flow for Manufacturing Plan-to-Make
uv run tools/export_diagram.py --profile manufacturing --lifecycle P2M --format mermaid
```

### 3. Run Quantitative Operational Simulations
Simulate operational disruptions and quantify lead time and unit cost impacts:
```bash
# Professional Services Scenarios:
uv run tools/simulate_scenario.py --profile professional_services scenario_project_margin_slippage
uv run tools/simulate_scenario.py --profile professional_services scenario_consultant_bench_surge
uv run tools/simulate_scenario.py --profile professional_services scenario_psa_outage_billing_crunch

# Discrete Manufacturing Scenarios:
uv run tools/simulate_scenario.py --profile manufacturing scenario_credit_hold_surge
uv run tools/simulate_scenario.py --profile manufacturing scenario_raw_material_stockout

# Core Financial & Back-Office Scenarios:
uv run tools/simulate_scenario.py --profile core scenario_close_period_crunch
uv run tools/simulate_scenario.py --profile core scenario_supplier_disruption
uv run tools/simulate_scenario.py --profile core scenario_invoice_bottleneck
uv run tools/simulate_scenario.py --profile core scenario_controller_absence_surge
uv run tools/simulate_scenario.py --profile core scenario_payroll_outage_surge

# Cross-Profile Shared Scenarios:
uv run tools/simulate_scenario.py --profile manufacturing scenario_erp_outage
uv run tools/simulate_scenario.py --profile professional_services scenario_erp_outage
```

### 4. Scaffold New Industry Overlays
Generate folder structures and manifests for a new industry domain:
```bash
uv run tools/new_profile.py aerospace --extends manufacturing --name "Aerospace & Defense"
```

---

## 📄 Architecture Governance

Managed under Architecture Decision Records in `docs/decisions/`:
- **ADR-0001**: WorldBuild Architecture Adaptation for Enterprise Value Chains
- **ADR-0002**: Source-to-Pay (S2P) Lifecycle Taxonomy & Governance Design
- **ADR-0003**: Order-to-Cash (O2C) Lifecycle Taxonomy & CRM/WMS System Integration
- **ADR-0004**: Record-to-Report (R2R) Lifecycle Taxonomy, SOX 404 Controls & Consolidation Boundaries
- **ADR-0005**: Hire-to-Retire (H2R) Lifecycle Taxonomy & Human Capital Management
- **ADR-0006**: Plan-to-Make (P2M) Lifecycle Taxonomy & Manufacturing Operations
- **ADR-0007**: Multi-Industry Profiles & Layered Inheritance Architecture
- **ADR-0008**: Professional Services (L2C / E2C) Operating Model & PSA Integration

All releases and historical changes are tracked in [`CHANGELOG.md`](CHANGELOG.md).
