# Enterprise Value Chain Modeling Engine — Quick Start Guide

Welcome! If you are an **Enterprise Architect (EA)**, **Process Architect**, or **Systems Engineer** who just cloned this repository, this guide shows what you can do out of the box and how to model, audit, visualize, and stress-test your own enterprise processes and IT systems in minutes.

Instead of maintaining static Visio/Lucidchart diagrams and disconnected Excel RACI spreadsheets that drift out of sync, you define (or customize) your operating model once—and the engine validates and compiles **6 distinct families of architecture artifacts**.

---

## 1. Explore What Exists Out of the Box

The repository ships with **5 composable industry profiles** spanning **11 end-to-end business lifecycles** in [`profiles/`](profiles/):

| Profile ID | Extends | Included Business Lifecycles | Primary Domain |
| :--- | :--- | :--- | :--- |
| **`core`** | *(Base)* | `S2P` (Source-to-Pay), `R2R` (Record-to-Report), `H2R` (Hire-to-Retire) | Cross-Industry Back-Office Foundation |
| **`manufacturing`** | `core` | `P2M` (Plan-to-Make), `O2C` (Order-to-Cash) + `core` | Discrete Manufacturing, MES, WMS & Supply Chain |
| **`professional_services`** | `core` | `L2C` (Lead-to-Cash), `E2C` (Engagement-to-Cash) + `core` | Consulting, Billable Delivery & PSA Platforms |
| **`healthcare`** | `core` | `P2D` (Patient-to-Discharge), `RCM` (Revenue Cycle Mgmt) + `core` | Clinical Inpatient Care, EHR & EDI Clearinghouse |
| **`financial_services`** | `core` | `C2A` (Client-to-Account KYC/AML), `L2S` (Loan-to-Settlement) + `core` | Commercial/Retail Banking, Core Subledger & LOS |

### Instant Verification & Dashboard Launch
```bash
# 1. List all available profiles and their lifecycles
uv run tools/validate_and_build.py --list-profiles

# 2. Validate and compile all profiles + the global profile switcher
uv run tools/validate_and_build.py --profile ALL

# 3. Open the interactive multi-profile dashboard in your browser
xdg-open index/index.html
# Or serve locally:
python3 -m http.server 8080 --directory index
```

---

## 2. The 6 Artifacts Generated for Your Enterprise

Whenever you run [`tools/validate_and_build.py`](tools/validate_and_build.py) and [`tools/simulate_scenario.py`](tools/simulate_scenario.py) for a profile (`index/<profile>/`), the engine compiles:

1. **Standalone Interactive Executive SPA (`value_chain_visualizer.html`)**
   - A zero-dependency, offline-capable single HTML file you can email to stakeholders or attach to an Architecture Review Board (ARB) ticket. Includes interactive process flows, RACI swimlanes, IT asset topology graphs, a live scenario simulator, and the **`🎨 Designer Studio`**.
2. **Governance & Audit Matrices (`diagram_raci_matrix.md` & `diagram_daci_matrix.md`)**
   - Full 2D role-by-step grids, role touchpoint/workload distribution, **Key-Person Risk (Concentrated Approver)** flags ($\ge 5$ approvals), **Single Approver Rule** verification ($|A|=1$), and **Segregation of Duties (SoD)** conflict audits.
3. **Architecture & Swimlane Mermaid Diagrams (`*.mmd` & `diagrams_summary.md`)**
   - Data-driven Mermaid flowcharts (`diagram_process_flow_<lc>.mmd`, `diagram_raci_swimlanes_<lc>.mmd`, `diagram_system_architecture.mmd`) ready to paste into GitHub PRs, Confluence, Notion, or Backstage.
4. **Validated Enterprise Knowledge Graph (`knowledge_graph.json`)**
   - A single machine-readable JSON index of all resolved elements (across inherited layers and patches), roles, approval limits, IT assets, and graph edges.
5. **Lifecycle LLM Context Blueprints (`llm_context_<lifecycle>.md`)**
   - Ready-to-use system prompts per lifecycle combining milestone sequences, KPIs, RACI assignments, asset bindings, and Tier 1–3 specifications so you can feed your company's operating model into an LLM for SOP generation, control gap analysis, or onboarding Q&A.
6. **Quantitative Disruption Sensitivity Reports (`simulation_report_<scenario>.md`)**
   - Step-by-step baseline vs. shocked lead time (hours) and unit cost ($) tables quantifying the impact of system outages, vendor delays, or regulatory surges.

---

## 3. Five Hands-On Examples Using Your Own Processes & Systems

### Example 1: Create a Company-Specific Hybrid Profile ("Acme MedTech")
**Goal**: Model a medical device manufacturer that inherits discrete manufacturing (`P2M`, `O2C` from `manufacturing`), but enforces FDA 21 CFR Part 820 Quality System Regulations before finished goods can be released.

1. **Scaffold the new profile extending `manufacturing`**:
   ```bash
   uv run tools/new_profile.py acme_medtech --extends manufacturing --name "Acme MedTech"
   ```
2. **Add your custom IT system & regulatory role**:
   - Create `profiles/acme_medtech/assets/asset_veeva_qms.md` (`asset_type: it_application`).
   - Create `profiles/acme_medtech/roles/role_vp_regulatory_affairs.md` with `approval_limit_usd: 1000000.0`.
3. **Override the inherited Quality Inspection step**:
   - Create `profiles/acme_medtech/elements/process_steps/p2m_005_quality_inspection_release.md` with `overrides: manufacturing` in its YAML frontmatter, bind `asset_veeva_qms`, set `approval_threshold_usd: 500000.0`, and assign `role_vp_regulatory_affairs` as `accountable`.
4. **Build and verify**:
   ```bash
   uv run tools/validate_and_build.py --profile acme_medtech
   ```

---

### Example 2: Catch & Remediate a SOX / Internal Audit Violation Before Production
**Goal**: Audit an "as-is" workflow where a single role both executes and approves a step, or where an approver lacks sufficient dollar authority, and prove compliance to Internal Audit.

- **Segregation of Duties (SoD) Gate**: If you assign `role_procurement_specialist` as both `responsible` (`R`) and `accountable` (`A`) on a step without declaring a `compensating_control:`, [`tools/validate_and_build.py`](tools/validate_and_build.py) fails the build:
  > `SoD Conflict in '<step_id>': Role(s) ['role_procurement_specialist'] cannot be both Responsible and Accountable without a 'compensating_control' declared.`
- **Approval Limit Gate**: If a process step declares `approval_threshold_usd: 250000.0` but the Accountable role only has `approval_limit_usd: 50000.0`, the validator fails the build:
  > `Threshold Violation in '<step_id>': Accountable role '<role_id>' has limit $50000.0 which is below the step threshold of $250000.0`
- **Single Approver Rule**: JSON Schema validation (`maxItems: 1` on `raci.accountable` and `daci.approver`) prevents split accountability across multiple roles.
- **Key-Person Concentration Audit**: Inspect `index/<profile>/diagram_daci_matrix.md` to see automatic flagging of any role holding $\ge 5$ Approver assignments (`🚨 Key-Person Risk (Concentrated Approver)`).

---

### Example 3: Zero-Code Process Re-Engineering in the Browser Designer Studio
**Goal**: During a live workshop with business stakeholders, insert a new compliance milestone into an existing lifecycle, re-sequence steps, and export the operating model without writing YAML or JSON by hand.

1. Open any compiled visualizer (e.g., [`index/financial_services/value_chain_visualizer.html`](index/financial_services/value_chain_visualizer.html)) and click the **`🎨 Designer Studio`** tab.
2. Use the four interactive authoring panels:
   - **IT System Assets Manager**: Add a new system (e.g., `asset_chainalysis_kyt` — Blockchain KYT Screening).
   - **Enterprise Roles Manager**: Add or adjust role approval limits.
   - **Process Step Editor**: Create a new step (`c2a_003b_crypto_onchain_provenance`) or override an existing step across Tier 1/2/3 descriptions, cycle time, unit cost, RACI/DACI roles, asset dependencies, and `feeds_into` links.
   - **Lifecycle Milestone Sequencer**: Insert the new step into the `C2A` milestone order.
3. Verify zero errors in the **Live Governance Guardrail Engine** banner and watch the Process Flow, RACI Swimlanes, and Asset Topology diagrams re-render live in the browser.
4. Click **Export `.vcm.json` Overlay Bundle**, then materialize it into a first-class repository profile:
   ```bash
   uv run tools/import_custom_profile.py path/to/acme_crypto_bank.vcm.json
   ```

---

### Example 4: IT System Outage Blast-Radius & Business Case Justification
**Goal**: Justify a high-availability investment for a critical system (e.g., Core ERP, WMS, EDI Clearinghouse, or Core Banking Platform) by quantifying what happens to lead times and unit costs when it degrades or goes offline.

1. Inspect `index/<profile>/diagram_system_architecture.mmd` to see every process workload connected via `-. runs on .->` to the target asset.
2. Create a scenario JSON in `profiles/<profile>/simulations/scenario_my_system_outage.json`:
   ```json
   {
     "$schema": "../../../schema/scenario_simulation.schema.json",
     "scenario_id": "scenario_my_system_outage",
     "name": "Legacy Middleware 24-Hour Outage",
     "target_lifecycle": "L2S",
     "applicable_profiles": ["financial_services"],
     "description": "Quantifies manual fallback delays and rework costs during a 24h middleware outage.",
     "shocks": [
       {
         "target_element_id": "l2s_004_loan_booking_funding_disbursement",
         "attribute_modifier": "automation_rate",
         "multiplier": 0.2,
         "additive_delta": 0.0
       },
       {
         "target_element_id": "l2s_004_loan_booking_funding_disbursement",
         "attribute_modifier": "baseline_cycle_time_hours",
         "multiplier": 3.5,
         "additive_delta": 16.0
       },
       {
         "target_element_id": "l2s_004_loan_booking_funding_disbursement",
         "attribute_modifier": "error_rate",
         "multiplier": 2.5,
         "additive_delta": 0.05
       }
     ]
   }
   ```
3. Run the simulator to generate a Markdown sensitivity report (`index/<profile>/simulation_report_scenario_my_system_outage.md`) where effective time and cost compound error rework via $T_{\text{eff}} = T \times (1 + \epsilon)$ and $C_{\text{eff}} = C \times (1 + \epsilon)$:
   ```bash
   uv run tools/simulate_scenario.py --profile financial_services scenario_my_system_outage
   ```

---

### Example 5: Non-Destructive Cross-Department Wiring via YAML Patches
**Goal**: Connect a shared corporate process in `core` (such as `s2p_006_goods_services_receipt` or `s2p_004_contracting_sla_negotiation`) into your industry-specific workflow without copying or mutating any files in `profiles/core/`.

1. Add a YAML patch file in `profiles/<your_profile>/patches/` (validated by [`schema/profile_patch.schema.json`](schema/profile_patch.schema.json)), for example [`profiles/healthcare/patches/s2p_006_goods_services_receipt.yaml`](profiles/healthcare/patches/s2p_006_goods_services_receipt.yaml):
   ```yaml
   target: s2p_006_goods_services_receipt
   append:
     graph_relations:
       - relation: feeds_into
         target: p2d_004_care_delivery_order_execution
         weight: 1.0
   ```
2. When you compile `--profile healthcare`, `s2p_006` automatically links into `p2d_004`, while `--profile core` remains 100% isolated and free of healthcare dependencies.

---

## 4. Where to Go Next

- **Step-by-Step Authoring Manual**: [`docs/guides/authoring-elements-and-lifecycles.md`](docs/guides/authoring-elements-and-lifecycles.md)
- **Simulation Math & Queueing Guide**: [`docs/guides/quantitative-scenario-simulation.md`](docs/guides/quantitative-scenario-simulation.md)
- **Dual RACI & DACI Governance Spec**: [`docs/architecture/governance-raci-daci.md`](docs/architecture/governance-raci-daci.md)
- **CLI Reference**: [`docs/reference/cli-tooling-reference.md`](docs/reference/cli-tooling-reference.md)
