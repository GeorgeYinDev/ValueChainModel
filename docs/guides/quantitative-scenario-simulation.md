# Practitioner Guide: Quantitative Scenario Simulation & Resilience Modeling

The **Enterprise Value Chain Modeling Engine** includes a discrete-event quantitative simulation framework for stress-testing business processes against macroeconomic shocks, IT outages, volume surges, and supplier disruptions.

---

## 1. Simulation Engine Architecture

Simulations can be executed through two complementary interfaces:
1. **Headless CLI Engine**: [`tools/simulate_scenario.py`](../../tools/simulate_scenario.py) generates structured Markdown executive reports in `index/simulation_report_<scenario_id>.md`.
2. **Interactive Standalone Visualizer**: [`index/value_chain_visualizer.html`](../../index/value_chain_visualizer.html) executes real-time client-side parameter recalculation, dynamically highlighting bottleneck shifts and cost variances.

---

## 2. Core Operational Parameters

Each process element specifies five baseline operational attributes in its YAML frontmatter:

| Attribute | Unit | Valid Range | Definition |
| :--- | :---: | :---: | :--- |
| `baseline_cycle_time_hours` | Hours | $\ge 0.0$ | Expected working hours to execute one unit of work under normal conditions. |
| `baseline_cost_per_unit` | USD ($) | $\ge 0.0$ | Direct operational labor and system processing cost per transaction unit. |
| `automation_rate` | Ratio | $[0.0, 1.0]$ | Proportion of throughput processed straight-through (STP) without human touch. |
| `error_rate` | Ratio | $[0.0, 1.0]$ | Frequency of exceptions, validation failures, or rework cycles. |
| `sla_hours` | Hours | $\ge 0.0$ | Contractual or policy-mandated maximum processing lead time. |

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

### Multi-Shock Modeling
The simulation engine supports multiple simultaneous shocks on a single process milestone. For example, an intercompany dispute surge can simultaneously expand cycle time by 2.8x while increasing unit legal/accounting costs by $25/unit.

---

## 4. Queueing Theory & Bottleneck Amplification

> **Note:** The mathematical implementation of Kingman's formula and non-linear $M/M/1$ queueing behavior is scheduled for Phase 6 (Discrete Event Simulation Engine). Current calculations (Phase 5) use simplified linear multipliers.

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

### Example: `simulations/scenario_freight_rate_surge.json`
```json
{
  "scenario_id": "scenario_freight_rate_surge",
  "name": "Global Maritime Freight Rate & Port Congestion Shock",
  "target_lifecycle": "O2C",
  "description": "Simulates a geopolitical disruption to global shipping lanes, causing a 300% spike in fulfillment delays and increased warehouse staging costs.",
  "shocks": [
    {
      "target_element_id": "o2c_003_inventory_allocation_fulfillment",
      "attribute_modifier": "baseline_cycle_time_hours",
      "multiplier": 3.0,
      "additive_delta": 48.0
    },
    {
      "target_element_id": "o2c_003_inventory_allocation_fulfillment",
      "attribute_modifier": "baseline_cost_per_unit",
      "multiplier": 2.5,
      "additive_delta": 60.0
    },
    {
      "target_element_id": "o2c_004_billing_invoice_generation",
      "attribute_modifier": "error_rate",
      "multiplier": 2.0,
      "additive_delta": 0.05
    }
  ]
}
```

### Available Built-in Scenarios
The repository ships with several pre-calibrated baseline scenarios modeling real-world systemic risks:
- `scenario_controller_absence_surge.json`: Models key-person risk (Controller absence) during month-end close (R2R).
- `scenario_payroll_outage_surge.json`: Simulates an IT outage in the `asset_payroll_engine` right before cutoff (H2R).
- `scenario_raw_material_stockout.json`: A Tier-1 supplier failure cascading into a factory line stoppage (P2M).
- `scenario_credit_hold_surge.json`: A macroeconomic shock triggering a massive spike in customer credit holds (O2C).

---

## 6. Execution & Report Interpretation

### Running via CLI
```bash
uv run tools/simulate_scenario.py simulations/scenario_freight_rate_surge.json
```

### Understanding the Generated Report
The engine writes an executive report to `index/simulation_report_<scenario_id>.md`:
- **Macro Outcomes**: Total lifecycle lead time delta ($\Delta\%$) and total unit cost delta ($\Delta\%$).
- **Bottleneck Sensitivity Table**:
  - Highlights process steps exceeding SLA tolerances with `🔥 +X%` badges.
  - Highlights steps experiencing unit cost inflation with `💸 +X%` badges.
  - Identifies which step becomes the new critical-path constraint for the enterprise.
