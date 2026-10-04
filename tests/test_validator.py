import os
import subprocess
import tempfile
import pathlib
import pytest

ROOT_DIR = pathlib.Path(__file__).parent.parent.resolve()
VALIDATOR_SCRIPT = ROOT_DIR / "tools" / "validate_and_build.py"

def test_validator_success():
    """Test that the existing models validate successfully."""
    # Run the validator using uv
    result = subprocess.run(
        ["uv", "run", str(VALIDATOR_SCRIPT)],
        cwd=ROOT_DIR,
        capture_output=True,
        text=True
    )
    assert result.returncode == 0, f"Validator failed unexpectedly:\n{result.stderr}\n{result.stdout}"
    assert "✅ Validation & Build Successful!" in result.stdout

def test_validator_negative_case_sod(tmp_path):
    """Test that a Segregation of Duties violation fails the build."""
    # Create a temporary invalid element in the elements/process_steps directory
    invalid_element = ROOT_DIR / "elements" / "process_steps" / "test_invalid_sod.md"
    invalid_element.write_text("""---
id: test_invalid_sod
type: process_step
name: Test Invalid SoD
version: 1.0.0
lifecycles: [S2P]
lod_support: [tier_1]
tags: [test]
raci:
  responsible: [role_finance_controller]
  accountable: [role_finance_controller]
---
# Invalid SoD test element
""", encoding="utf-8")
    
    try:
        result = subprocess.run(
            ["uv", "run", str(VALIDATOR_SCRIPT)],
            cwd=ROOT_DIR,
            capture_output=True,
            text=True
        )
        assert result.returncode == 1, "Validator should have failed due to SoD conflict."
        assert "SoD Conflict in 'test_invalid_sod'" in result.stdout
    finally:
        # Clean up
        if invalid_element.exists():
            invalid_element.unlink()

def test_validator_negative_case_schema(tmp_path):
    """Test that a missing required property fails schema validation."""
    invalid_element = ROOT_DIR / "elements" / "process_steps" / "test_invalid_schema.md"
    invalid_element.write_text("""---
id: test_invalid_schema
# type is required but missing
name: Test Invalid Schema
version: 1.0.0
---
# Invalid Schema test element
""", encoding="utf-8")
    
    try:
        result = subprocess.run(
            ["uv", "run", str(VALIDATOR_SCRIPT)],
            cwd=ROOT_DIR,
            capture_output=True,
            text=True
        )
        assert result.returncode == 1, "Validator should have failed due to schema violation."
        assert "is not valid under any of the given schemas" in result.stdout or "Schema violation" in result.stdout or "'type' is a required property" in result.stdout
    finally:
        if invalid_element.exists():
            invalid_element.unlink()
