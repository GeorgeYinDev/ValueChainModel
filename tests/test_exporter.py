import pathlib
import shutil
import subprocess

ROOT_DIR = pathlib.Path(__file__).parent.parent.resolve()
EXPORTER_SCRIPT = ROOT_DIR / "tools" / "export_diagram.py"
SOURCE_KG = ROOT_DIR / "index" / "manufacturing" / "knowledge_graph.json"


def test_exporter_creates_files(tmp_path):
    """Test that the exporter creates the expected diagrams and visualizer."""
    out_base = tmp_path / "index"
    out_dir = out_base / "manufacturing"
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(SOURCE_KG, out_dir / "knowledge_graph.json")

    result = subprocess.run(
        [
            "uv", "run", str(EXPORTER_SCRIPT),
            "--profile", "manufacturing",
            "--lifecycle", "ALL",
            "--format", "all",
            "--output-dir", str(out_base),
        ],
        cwd=ROOT_DIR,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, f"Exporter failed: {result.stderr}"

    expected_files = [
        "value_chain_visualizer.html",
        "diagram_process_flow_all.mmd",
        "diagram_raci_swimlanes_all.mmd",
        "diagram_system_architecture.mmd",
        "diagram_raci_matrix.md",
        "diagram_daci_matrix.md",
        "diagrams_summary.md",
    ]

    for f in expected_files:
        assert (out_dir / f).exists(), f"Expected artifact {f} was not generated."

    # Check that visualizer contains the offline node / filter logic
    html_content = (out_dir / "value_chain_visualizer.html").read_text(encoding="utf-8")
    assert "mermaid" in html_content.lower()
    assert "applyscenario" in html_content.lower()

