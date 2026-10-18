import json
import pathlib
import re
import shutil
import subprocess

ROOT_DIR = pathlib.Path(__file__).parent.parent.resolve()
EXPORTER_SCRIPT = ROOT_DIR / "tools" / "export_diagram.py"
IMPORTER_SCRIPT = ROOT_DIR / "tools" / "import_custom_profile.py"
SOURCE_KG = ROOT_DIR / "index" / "manufacturing" / "knowledge_graph.json"


def test_visualizer_hydration_and_studio_ui(tmp_path):
    """Verify visualizer HTML has hydrated lifecycles, scenarios, roles, roleTitles, and Studio UI."""
    out_base = tmp_path / "index"
    out_dir = out_base / "manufacturing"
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(SOURCE_KG, out_dir / "knowledge_graph.json")

    result = subprocess.run(
        [
            "uv",
            "run",
            str(EXPORTER_SCRIPT),
            "--profile",
            "manufacturing",
            "--lifecycle",
            "ALL",
            "--format",
            "html",
            "--output-dir",
            str(out_base),
        ],
        cwd=ROOT_DIR,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, f"Exporter failed: {result.stderr}"

    html = (out_dir / "value_chain_visualizer.html").read_text(encoding="utf-8")

    # Verify Designer Studio functions are present
    for fn_name in [
        "saveOverlayStep",
        "validateStudioGovernance",
        "exportValidatedOverlayBundle",
        "buildMermaidFlowClient",
    ]:
        assert fn_name in html, f"Missing Studio function {fn_name} in visualizer HTML"

    # Extract injected JSON payloads and verify non-empty hydration
    lf_match = re.search(r"const lifecycles = (\{.*?\});\n", html)
    assert lf_match, "lifecycles payload not found"
    lifecycles_data = json.loads(lf_match.group(1))
    assert "S2P" in lifecycles_data and "O2C" in lifecycles_data

    sc_match = re.search(r"const scenarios = (\[.*?\]);\n", html)
    assert sc_match, "scenarios payload not found"
    scenarios_data = json.loads(sc_match.group(1))
    assert len(scenarios_data) >= 3

    roles_match = re.search(r"const roles = (\{.*?\});\n", html)
    assert roles_match, "roles dictionary payload not found"
    roles_data = json.loads(roles_match.group(1))
    assert "role_procurement_specialist" in roles_data

    rt_match = re.search(r"const roleTitles = (\{.*?\});\n", html)
    assert rt_match, "roleTitles payload not found"
    role_titles_data = json.loads(rt_match.group(1))
    assert role_titles_data.get("role_procurement_specialist") == "Procurement Specialist"


def test_round_trip_custom_overlay_import_and_build(tmp_path):
    """Test importing a custom .vcm.json overlay bundle and building its knowledge graph & visualizer."""
    profiles_root = tmp_path / "profiles"
    shutil.copytree(ROOT_DIR / "profiles" / "core", profiles_root / "core")
    shutil.copytree(ROOT_DIR / "profiles" / "manufacturing", profiles_root / "manufacturing")
    out_base = tmp_path / "index"

    base_kg = json.loads(SOURCE_KG.read_text(encoding="utf-8"))
    orig_o2c = base_kg["lifecycles"]["O2C"]
    o2c_step1 = base_kg["elements"]["o2c_001_customer_quote_order_entry"]
    resp_roles = o2c_step1["raci"]["responsible"]
    cons_roles = o2c_step1["raci"].get("consulted", [])
    inf_roles = o2c_step1["raci"].get("informed", [])

    custom_milestones = list(orig_o2c["milestones"]) + [
        {
            "step_id": "o2c_006_deal_desk_review",
            "name": "Custom Deal Desk Review",
            "order": len(orig_o2c["milestones"]) + 1,
        }
    ]
    custom_o2c = dict(orig_o2c)
    custom_o2c["overrides"] = "manufacturing"
    custom_o2c["milestones"] = custom_milestones

    bundle = {
        "bundle_version": "1.0.0",
        "validated": True,
        "profile": {
            "profile_id": "acme_custom",
            "name": "Acme Custom Manufacturing Overlay",
            "industry": "manufacturing",
            "version": "1.0.0",
            "description": "Custom overlay profile created via Designer Studio",
            "extends": ["manufacturing"],
            "lifecycles": ["S2P", "O2C", "R2R", "H2R", "P2M"],
            "default_lifecycle": "O2C",
        },
        "roles": {
            "role_custom_deal_desk": {
                "id": "role_custom_deal_desk",
                "type": "role",
                "name": "Deal Desk Director",
                "department": "Commercial Operations",
                "approval_limit_usd": 250000.0,
            }
        },
        "assets": {
            "asset_custom_cpq_engine": {
                "id": "asset_custom_cpq_engine",
                "name": "Enterprise CPQ Pricing Engine",
                "asset_type": "it_application",
                "version": "1.0.0",
                "status": "operational",
                "sla_uptime_percent": 99.95,
                "capacity_max_tps": 800,
                "parent_asset_id": "asset_erp_system",
            }
        },
        "elements": {
            "o2c_006_deal_desk_review": {
                "frontmatter": {
                    "id": "o2c_006_deal_desk_review",
                    "type": "process_step",
                    "name": "Custom Deal Desk Review",
                    "version": "1.0.0",
                    "lifecycles": ["O2C"],
                    "lod_support": ["tier_1", "tier_2", "tier_3"],
                    "tags": ["commercial", "deal_desk", "custom"],
                    "raci": {
                        "responsible": resp_roles,
                        "accountable": ["role_custom_deal_desk"],
                        "consulted": cons_roles,
                        "informed": inf_roles,
                    },
                    "daci": {
                        "driver": resp_roles,
                        "approver": ["role_custom_deal_desk"],
                        "contributor": cons_roles,
                        "informed": inf_roles,
                    },
                    "attributes": {
                        "baseline_cycle_time_hours": 4.0,
                        "baseline_cost_per_unit": 18.0,
                        "automation_rate": 0.85,
                        "error_rate": 0.01,
                        "sla_hours": 12.0,
                        "approval_threshold_usd": 100000.0,
                    },
                    "asset_dependencies": ["asset_custom_cpq_engine", "asset_erp_system"],
                    "graph_relations": [
                        {
                            "relation": "feeds_into",
                            "target": "o2c_001_customer_quote_order_entry",
                            "weight": 1.0,
                        }
                    ],
                },
                "tiers": {
                    "tier_1": "Ensure non-standard commercial quotes meet margin thresholds.",
                    "tier_2": "Deal Desk reviews pricing structure prior to order capture.",
                    "tier_3": "Automated CPQ pricing validation rules.",
                },
            }
        },
        "lifecycles": {"O2C": custom_o2c},
    }

    bundle_file = tmp_path / "acme_custom.vcm.json"
    bundle_file.write_text(json.dumps(bundle, indent=2), encoding="utf-8")

    res = subprocess.run(
        [
            "uv",
            "run",
            str(IMPORTER_SCRIPT),
            str(bundle_file),
            "--profiles-root",
            str(profiles_root),
            "--output-dir",
            str(out_base),
        ],
        cwd=ROOT_DIR,
        capture_output=True,
        text=True,
    )
    assert res.returncode == 0, f"Importer failed:\nSTDOUT:\n{res.stdout}\nSTDERR:\n{res.stderr}"

    kg_path = out_base / "acme_custom" / "knowledge_graph.json"
    assert kg_path.exists()
    kg = json.loads(kg_path.read_text(encoding="utf-8"))
    assert "o2c_006_deal_desk_review" in kg["elements"]
    assert "role_custom_deal_desk" in kg["roles"]
    assert "asset_custom_cpq_engine" in kg["assets"]
    assert (out_base / "acme_custom" / "value_chain_visualizer.html").exists()


def test_imported_bundle_governance_enforcement(tmp_path):
    """Verify that bundles with unresolved SoD conflicts are rejected by the validator."""
    profiles_root = tmp_path / "profiles"
    shutil.copytree(ROOT_DIR / "profiles" / "core", profiles_root / "core")
    shutil.copytree(ROOT_DIR / "profiles" / "manufacturing", profiles_root / "manufacturing")
    out_base = tmp_path / "index"

    bad_bundle = {
        "bundle_version": "1.0.0",
        "validated": False,
        "profile": {
            "profile_id": "bad_sod_custom",
            "name": "Invalid SoD Overlay",
            "version": "1.0.0",
            "extends": ["manufacturing"],
            "lifecycles": ["S2P", "O2C", "R2R", "H2R", "P2M"],
        },
        "elements": {
            "o2c_099_invalid_sod_step": {
                "id": "o2c_099_invalid_sod_step",
                "type": "process_step",
                "name": "Unresolved SoD Step",
                "version": "1.0.0",
                "lifecycles": ["O2C"],
                "lod_support": ["tier_1", "tier_2", "tier_3"],
                "tags": ["invalid"],
                "raci": {
                    # Same role is Responsible and Accountable with no compensating_control!
                    "responsible": ["role_order_management_specialist"],
                    "accountable": ["role_order_management_specialist"],
                    "consulted": [],
                    "informed": [],
                },
            }
        },
    }

    bundle_file = tmp_path / "bad_sod_custom.vcm.json"
    bundle_file.write_text(json.dumps(bad_bundle, indent=2), encoding="utf-8")

    res = subprocess.run(
        [
            "uv",
            "run",
            str(IMPORTER_SCRIPT),
            str(bundle_file),
            "--profiles-root",
            str(profiles_root),
            "--output-dir",
            str(out_base),
        ],
        cwd=ROOT_DIR,
        capture_output=True,
        text=True,
    )
    assert res.returncode != 0
    assert "SoD Conflict" in res.stdout
