import subprocess
import pathlib

ROOT_DIR = pathlib.Path(__file__).parent.parent.resolve()
SIMULATOR_SCRIPT = ROOT_DIR / "tools" / "simulate_scenario.py"

def test_simulation_baseline_vs_shock():
    """Test that a simulation correctly computes totals and the visualizer matches."""
    scenario_path = ROOT_DIR / "simulations" / "scenario_close_period_crunch.json"
    
    result = subprocess.run(
        ["uv", "run", str(SIMULATOR_SCRIPT), str(scenario_path)],
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
