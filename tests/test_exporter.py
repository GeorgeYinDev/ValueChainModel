import os
import subprocess
import pathlib

ROOT_DIR = pathlib.Path(__file__).parent.parent.resolve()
EXPORTER_SCRIPT = ROOT_DIR / "tools" / "export_diagram.py"
INDEX_DIR = ROOT_DIR / "index"

def test_exporter_creates_files():
    """Test that the exporter creates the expected diagrams and visualizer."""
    
    # We can clean up the index dir first, or just run it and check file existence
    # Note: validate_and_build already runs exporter. But we can run it standalone.
    
    result = subprocess.run(
        ["uv", "run", str(EXPORTER_SCRIPT), "--lifecycle", "ALL", "--format", "all"],
        cwd=ROOT_DIR,
        capture_output=True,
        text=True
    )
    
    assert result.returncode == 0, f"Exporter failed: {result.stderr}"
    
    expected_files = [
        "value_chain_visualizer.html",
        "diagram_process_flow_all.mmd",
        "diagram_raci_swimlanes_all.mmd",
        "diagram_system_architecture.mmd",
        "diagram_raci_matrix.md",
        "diagram_daci_matrix.md",
        "diagrams_summary.md"
    ]
    
    for f in expected_files:
        assert (INDEX_DIR / f).exists(), f"Expected artifact {f} was not generated."
        
    # Check that visualizer contains the offline node / filter logic
    html_content = (INDEX_DIR / "value_chain_visualizer.html").read_text(encoding="utf-8")
    assert "mermaid" in html_content.lower()
    assert "applyscenario" in html_content.lower()
