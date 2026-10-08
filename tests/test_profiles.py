import sys
import pytest
import pathlib
import subprocess
import json

ROOT_DIR = pathlib.Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(ROOT_DIR))

from tools.vcm_profiles import resolve_profile, list_profiles
FIXTURES_PROFILES = ROOT_DIR / "tests" / "fixtures" / "profiles"
VALIDATOR_SCRIPT = ROOT_DIR / "tools" / "validate_and_build.py"

def test_profile_resolution_order():
    """Verify depth-first inheritance and layer ordering."""
    ep = resolve_profile(FIXTURES_PROFILES, "child", ROOT_DIR)
    assert ep.layers == ["base", "child"]
    assert "test_step_1" in ep.element_files
    assert "test_step_2" in ep.element_files
    assert ep.element_files["test_step_1"][1] == "base"
    assert ep.element_files["test_step_2"][1] == "child"

def test_profile_cycle_detection():
    """Verify circular profile inheritance is detected and rejected."""
    with pytest.raises(ValueError, match="Inheritance cycle detected"):
        resolve_profile(FIXTURES_PROFILES, "bad_cycle_a", ROOT_DIR)

def test_accidental_collision_rejected():
    """Verify accidental ID clash across layers fails without 'overrides'."""
    with pytest.raises(ValueError, match="Accidental ID collision"):
        resolve_profile(FIXTURES_PROFILES, "bad_collision", ROOT_DIR)

def test_authorized_override_succeeds():
    """Verify authorized override with 'overrides' succeeds."""
    ep = resolve_profile(FIXTURES_PROFILES, "child_override", ROOT_DIR)
    assert "test_step_1" in ep.element_files
    file_path, layer = ep.element_files["test_step_1"]
    assert layer == "child_override"

def test_patch_application():
    """Verify patches append tags/relations and build successfully."""
    import shutil
    try:
        res = subprocess.run(
            ["uv", "run", str(VALIDATOR_SCRIPT), "--profile", "child", "--profiles-root", "tests/fixtures/profiles"],
            cwd=ROOT_DIR,
            capture_output=True,
            text=True
        )
        assert res.returncode == 0, f"Validator failed on child profile: {res.stderr}\n{res.stdout}"
        
        kg_path = ROOT_DIR / "index" / "child" / "knowledge_graph.json"
        assert kg_path.exists()
        kg_data = json.loads(kg_path.read_text(encoding="utf-8"))
        step_1 = kg_data["elements"]["test_step_1"]
        assert "patched_by_child" in step_1.get("tags", [])
    finally:
        child_out = ROOT_DIR / "index" / "child"
        if child_out.exists():
            shutil.rmtree(child_out)

def test_bad_patch_fails():
    """Verify patch targeting non-existent element causes validator to fail."""
    import shutil
    try:
        res = subprocess.run(
            ["uv", "run", str(VALIDATOR_SCRIPT), "--profile", "bad_patch", "--profiles-root", "tests/fixtures/profiles"],
            cwd=ROOT_DIR,
            capture_output=True,
            text=True
        )
        assert res.returncode != 0
        assert "Patch target 'non_existent_step' not found" in res.stdout
    finally:
        bad_out = ROOT_DIR / "index" / "bad_patch"
        if bad_out.exists():
            shutil.rmtree(bad_out)

def test_profile_isolation_guarantee():
    """Verify that core builds cleanly and has zero industry-specific elements."""
    res = subprocess.run(
        ["uv", "run", str(VALIDATOR_SCRIPT), "--profile", "core"],
        cwd=ROOT_DIR,
        capture_output=True,
        text=True
    )
    assert res.returncode == 0, f"Core build failed: {res.stderr}\n{res.stdout}"
    
    kg_path = ROOT_DIR / "index" / "core" / "knowledge_graph.json"
    kg_data = json.loads(kg_path.read_text(encoding="utf-8"))
    
    # Ensure no manufacturing, professional services, or healthcare elements exist in core
    for eid in kg_data["elements"].keys():
        assert not eid.startswith("p2m_"), f"Unexpected manufacturing element '{eid}' in core graph"
        assert not eid.startswith("o2c_"), f"Unexpected manufacturing element '{eid}' in core graph"
        assert not eid.startswith("l2c_"), f"Unexpected professional services element '{eid}' in core graph"
        assert not eid.startswith("e2c_"), f"Unexpected professional services element '{eid}' in core graph"
        assert not eid.startswith("p2d_"), f"Unexpected healthcare element '{eid}' in core graph"
        assert not eid.startswith("rcm_"), f"Unexpected healthcare element '{eid}' in core graph"

def test_professional_services_isolation():
    """Verify professional services contains no discrete manufacturing or healthcare elements."""
    res = subprocess.run(
        ["uv", "run", str(VALIDATOR_SCRIPT), "--profile", "professional_services"],
        cwd=ROOT_DIR,
        capture_output=True,
        text=True
    )
    assert res.returncode == 0, f"Professional Services build failed: {res.stderr}\n{res.stdout}"
    
    kg_path = ROOT_DIR / "index" / "professional_services" / "knowledge_graph.json"
    kg_data = json.loads(kg_path.read_text(encoding="utf-8"))
    
    for eid in kg_data["elements"].keys():
        assert not eid.startswith("p2m_"), f"Unexpected manufacturing element '{eid}' in professional services graph"
        assert not eid.startswith("o2c_"), f"Unexpected manufacturing element '{eid}' in professional services graph"
        assert not eid.startswith("p2d_"), f"Unexpected healthcare element '{eid}' in professional services graph"
        assert not eid.startswith("rcm_"), f"Unexpected healthcare element '{eid}' in professional services graph"

def test_healthcare_profile_resolution():
    """Verify healthcare profile resolves with expected layers and elements."""
    ep = resolve_profile(ROOT_DIR / "profiles", "healthcare", ROOT_DIR)
    assert ep.layers == ["core", "healthcare"]
    assert "p2d_001_patient_registration_scheduling" in ep.element_files
    assert "rcm_001_charge_capture_coding" in ep.element_files
    assert "asset_ehr_system" in ep.asset_files
    assert "role_attending_physician" in ep.role_files

def test_healthcare_isolation():
    """Verify healthcare contains no discrete manufacturing or professional services elements."""
    res = subprocess.run(
        ["uv", "run", str(VALIDATOR_SCRIPT), "--profile", "healthcare"],
        cwd=ROOT_DIR,
        capture_output=True,
        text=True
    )
    assert res.returncode == 0, f"Healthcare build failed: {res.stderr}\n{res.stdout}"
    
    kg_path = ROOT_DIR / "index" / "healthcare" / "knowledge_graph.json"
    kg_data = json.loads(kg_path.read_text(encoding="utf-8"))
    
    for eid in kg_data["elements"].keys():
        assert not eid.startswith("p2m_"), f"Unexpected manufacturing element '{eid}' in healthcare graph"
        assert not eid.startswith("o2c_"), f"Unexpected manufacturing element '{eid}' in healthcare graph"
        assert not eid.startswith("l2c_"), f"Unexpected professional services element '{eid}' in healthcare graph"
        assert not eid.startswith("e2c_"), f"Unexpected professional services element '{eid}' in healthcare graph"

