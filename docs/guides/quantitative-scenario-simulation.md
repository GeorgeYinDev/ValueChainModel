# Practitioner Guide: Quantitative Scenario Simulation & Resilience Modeling

The **Enterprise Value Chain Modeling Engine** includes a discrete-event quantitative simulation framework for stress-testing business processes against macroeconomic shocks, IT outages, volume surges, capacity shortages, and supplier disruptions.

---

## 1. Simulation Engine Architecture

Simulations can be executed through two complementary interfaces:
1. **Headless CLI Engine**: [`tools/simulate_scenario.py`](../../tools/simulate_scenario.py) generates structured Markdown executive reports in `index/<profile>/simulation_report_<scenario_id>.md`.
2. **Interactive Standalone Visualizer**: [`index/<profile>/value_chain_visualizer.html`](../../index) executes real-time parameter recalculation, dynamically highlighting bottleneck shifts and cost variances.

---

## 2. Core Operational Parameters

Each process element specifies baseline operational attributes in its YAML frontmatter:

| Attribute | Unit | Valid Range | Definition |
| :--- | :---: | :---: | :--- |
| `baseline_cycle_time_hours` | Hours | $\ge 0.0$ | Expected working hours to execute one unit of work under normal conditions. |
| `baseline_cost_per_unit` | USD ($) | $\ge 0.0$ | Direct operational labor and system processing cost per transaction unit. |
| `automation_rate` | Ratio | $[0.0, 1.0]$ | Proportion of throughput processed straight-through (STP) without human touch. |
| `error_rate` | Ratio | $[0.0, 1.0]$ | Frequency of exceptions, validation failures, or rework cycles. |
| `sla_hours` | Hours | $\ge 0.0$ | Contractual or policy-mandated maximum processing lead time. |
| `volume_per_period` | Count | $\ge 0$ | Standard transaction arrival volume per operating period. |
| `capacity_fte` | FTE | $\ge 0.0$ | Allocated operational staffing capacity assigned to this step. |

---

## 3. Disruption Shock Mechanics & Math

Scenarios apply attribute modifiers through a combination of multiplicative scalers ($M$) and additive deltas ($\Delta$):

### Cycle Time Expansion
$$T_{\text{shocked}} = (T_{\text{baseline}} \times M_{\text{time}}) + \Delta_{\text{time}}$$

### Unit Cost Inflation
$$C_{\text{shocked}} = (C_{\text{baseline}} \times M_{\text{cost}}) + \Delta_{\text{cost}}$$

### Automation Degradation
$$\alpha_{\text{shocked}} = \max\left(0.0, \, \min\left(1.0, \, (\alpha_{\text{baseline}} \times M_{\text{auto}}) + \Delta_{\text{auto}}\right)\right)$$

### Error Rate & Exception Surge
$$\epsilon_{\text{shocked}} = \max\left(0.0, \, \min\left(1.0, \, (\epsilon_{\text{baseline}} \times M_{\text{err}}) + \Delta_{\text{err}}\right)\right)$$

### Multi-Shock Modeling & Error Amplification
The simulator compounds operational degradation by adjusting effective lead time and unit cost by error rework cycles:
$$T_{\text{effective}} = T \times (1 + \epsilon)$$
$$C_{\text{effective}} = C \times (1 + \epsilon)$$

---

## 4. Queueing Theory & Bottleneck Amplification

When an operational disruption occurs, system throughput does not degrade linearly. According to Kingman's formula and $M/M/1$ queueing models, wait times grow asymptotically as system utilization ($\rho$) approaches capacity:

$$W_q \approx \left(\frac{\rho}{1 - \rho}\right) \times \left(\frac{C_a^2 + C_s^2}{2}\right) \times \frac{1}{\mu}$$

Where:
- $\lambda$: Inbound transaction arrival rate.
- $\mu$: Maximum processing throughput per human worker or system asset.
- $\rho = \frac{\lambda}{\mu \cdot \alpha}$: Effective operational utilization.

When error rates ($\epsilon$) surge or automation ($\alpha$) collapses during an outage, effective service capacity drops, driving $\rho \to 1.0$ and causing exponential backlog queues.

---

## 5. Authoring a Scenario Payload (`simulations/`)

Scenario files are stored as JSON payloads conforming to [`schema/scenario_simulation.schema.json`](../../schema/scenario_simulation.schema.json).

### Example: `profiles/professional_services/simulations/scenario_project_margin_slippage.json`
```json
{
  "$schema": "../../../schema/scenario_simulation.schema.json",
  "scenario_id": "scenario_project_margin_slippage",
  "name": "Project Scope Creep & Margin Slippage Disruption",
  "target_lifecycle": "E2C",
  "applicable_profiles": ["professional_services"],
  "description": "Simulates project scope creep and prolonged client acceptance rework loops, triggering consultant overtime costs and eroded gross margins.",
  "shocks": [
    {
      "target_element_id": "e2c_003_project_execution_delivery",
      "attribute_modifier": "baseline_cycle_time_hours",
      "multiplier": 1.35,
      "additive_delta": 0.0
    },
    {
      "target_element_id": "e2c_003_project_execution_delivery",
      "attribute_modifier": "baseline_cost_per_unit",
      "multiplier": 1.0,
      "additive_delta": 15000.0
    },
    {
      "target_element_id": "e2c_005_client_acceptance",
      "attribute_modifier": "baseline_cycle_time_hours",
      "multiplier": 1.5,
      "additive_delta": 12.0
    },
    {
      "target_element_id": "e2c_006_project_billing_invoicing",
      "attribute_modifier": "error_rate",
      "multiplier": 1.4,
      "additive_delta": 0.03
    }
  ]
}
```

---

## 6. Built-in Scenario Inventory

| Scenario ID | Target Profile | Target Lifecycle | Focus & Operational Risk |
| :--- | :---: | :---: | :--- |
| `scenario_close_period_crunch` | `core` | `R2R` | Controller overload and manual adjustments during fiscal period-end close. |
| `scenario_controller_absence_surge` | `core` | `R2R` | Single-approver bottleneck when Controller is absent during close crunch. |
| `scenario_erp_outage` | `core` / `ALL` | `S2P` | Core ERP platform outage forcing manual AP and purchasing workflows. |
| `scenario_supplier_disruption` | `core` | `S2P` | Global supply chain interruption impacting supplier lead times. |
| `scenario_invoice_bottleneck` | `core` | `S2P` | 3-way match invoice exception surge and AP approval delays. |
| `scenario_payroll_outage_surge` | `core` | `H2R` | HCM platform outage right before payroll cutoff date. |
| `scenario_credit_hold_surge` | `manufacturing` | `O2C` | Macroeconomic credit contraction causing customer fulfillment holds. |
| `scenario_raw_material_stockout` | `manufacturing` | `P2M` | Raw material stockout halting manufacturing line execution. |
| `scenario_project_margin_slippage` | `professional_services` | `E2C` | Scope creep and deliverable rework loops eroding project gross margins. |
| `scenario_consultant_bench_surge` | `professional_services` | `L2C` | Elongated presales cycles causing unassigned consultant bench spikes. |
| `scenario_psa_outage_billing_crunch` | `professional_services` | `E2C` | Cloud PSA outage at month-end billing cutoff forcing manual spreadsheets. |

---

## 7. Execution & Report Interpretation

### Running via CLI
```bash
# Run against Professional Services profile
uv run tools/simulate_scenario.py --profile professional_services scenario_project_margin_slippage

# Run against Manufacturing profile
uv run tools/simulate_scenario.py --profile manufacturing scenario_credit_hold_surge

# Run against Core Back-Office profile
uv run tools/simulate_scenario.py --profile core scenario_close_period_crunch
```

### Understanding the Generated Report
The engine writes an executive report to `index/<profile>/simulation_report_<scenario_id>.md`:
- **Macro Outcomes**: Total lifecycle lead time delta ($\Delta\%$) and total unit cost delta ($\Delta\%$).
- **Bottleneck Sensitivity Table**:
  - Highlights process steps exceeding baseline lead times with `🔥 +X%` badges.
  - Highlights steps experiencing unit cost inflation with `💸 +X%` badges.
  - Identifies which step becomes the critical-path bottleneck under shock conditions.
