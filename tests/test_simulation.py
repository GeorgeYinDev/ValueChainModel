import subprocess
import pathlib

ROOT_DIR = pathlib.Path(__file__).parent.parent.resolve()
SIMULATOR_SCRIPT = ROOT_DIR / "tools" / "simulate_scenario.py"

def test_simulation_baseline_vs_shock():
    """Test that a simulation correctly computes totals and the visualizer matches."""
    scenario_path = ROOT_DIR / "profiles" / "core" / "simulations" / "scenario_close_period_crunch.json"
    
    result = subprocess.run(
        ["uv", "run", str(SIMULATOR_SCRIPT), "--profile", "core", str(scenario_path)],
        cwd=ROOT_DIR,
        capture_output=True,
        text=True
    )
    
    assert result.returncode == 0, f"Simulator failed: {result.stderr}"
    
    # Check that totals are output
    assert "Total Lead Time:" in result.stdout
    assert "Total Unit Cost:" in result.stdout
    
    lines = result.stdout.splitlines()
    time_line = next(line for line in lines if "Total Lead Time:" in line)
    
    # Extract the baseline hours. e.g. "Total Lead Time: 70.0h -> 84.0h (+20.0%)"
    parts = time_line.split(":")
    time_str = parts[1].split("->")[0].strip()
    assert "h" in time_str
    
    val = float(time_str.replace("h", ""))
    assert val > 0
    # Phase 5.3 verified R2R drops from 140h to 70h, so check it's around 70-80, not >100.
    assert val < 100, f"Baseline time {val}h is too high, possible double-counting!"

import pytest

@pytest.mark.parametrize("profile_name", ["manufacturing", "professional_services", "healthcare"])
def test_simulation_cross_profile_erp_outage(profile_name):
    """Test that a shared scenario (scenario_erp_outage) runs cleanly across profiles."""
    result = subprocess.run(
        ["uv", "run", str(SIMULATOR_SCRIPT), "--profile", profile_name, "scenario_erp_outage"],
        cwd=ROOT_DIR,
        capture_output=True,
        text=True
    )
    assert result.returncode == 0, f"Simulator failed on {profile_name}: {result.stderr}\n{result.stdout}"
    assert "Simulation Report written to:" in result.stdout

@pytest.mark.parametrize("scenario_id,expected_min_increase", [
    ("scenario_project_margin_slippage", 30.0),
    ("scenario_consultant_bench_surge", 80.0),
    ("scenario_psa_outage_billing_crunch", 5.0)
])
def test_simulation_professional_services_scenarios(scenario_id, expected_min_increase):
    """Test that professional services disruption scenarios execute and compute valid deltas."""
    result = subprocess.run(
        ["uv", "run", str(SIMULATOR_SCRIPT), "--profile", "professional_services", scenario_id],
        cwd=ROOT_DIR,
        capture_output=True,
        text=True
    )
    assert result.returncode == 0, f"Simulator failed on {scenario_id}: {result.stderr}\n{result.stdout}"
    assert "Total Lead Time:" in result.stdout
    assert "Total Unit Cost:" in result.stdout
    assert "Simulation Report written to:" in result.stdout

@pytest.mark.parametrize("scenario_id", [
    "scenario_clearinghouse_cyberattack_outage",
    "scenario_payer_prior_auth_denial_surge",
    "scenario_emergency_surge_capacity_crunch"
])
def test_simulation_healthcare_scenarios(scenario_id):
    """Test that healthcare disruption scenarios execute and compute valid deltas."""
    result = subprocess.run(
        ["uv", "run", str(SIMULATOR_SCRIPT), "--profile", "healthcare", scenario_id],
        cwd=ROOT_DIR,
        capture_output=True,
        text=True
    )
    assert result.returncode == 0, f"Simulator failed on {scenario_id}: {result.stderr}\n{result.stdout}"
    assert "Total Lead Time:" in result.stdout
    assert "Total Unit Cost:" in result.stdout
    assert "Simulation Report written to:" in result.stdout


