#!/usr/bin/env python3
"""
Enterprise Value Chain Custom Profile Overlay Importer
------------------------------------------------------
Unpacks a client-side Designer Studio bundle (.vcm.json) into a layered
profile directory (profiles/<custom_id>/) and runs validate_and_build.py.
"""

import argparse
import json
import pathlib
import subprocess
import sys
from typing import Any

import yaml


def _write_element_markdown(target_file: pathlib.Path, entry: dict[str, Any]) -> None:
    if "frontmatter" in entry and isinstance(entry["frontmatter"], dict):
        fm = dict(entry["frontmatter"])
        tiers = entry.get("tiers", {}) if isinstance(entry.get("tiers"), dict) else {}
    else:
        fm = dict(entry)
        tiers = fm.pop("tiers", {}) if isinstance(fm.get("tiers"), dict) else {}

    fm.pop("source_layer", None)
    elem_id = fm.get("id", target_file.stem)
    fm["id"] = elem_id
    fm.setdefault("type", "process_step")
    fm.setdefault("name", elem_id)
    fm.setdefault("version", "1.0.0")
    fm.setdefault("lifecycles", ["S2P"])
    fm.setdefault("lod_support", ["tier_1", "tier_2", "tier_3"])
    fm.setdefault("tags", ["custom"])

    tier1 = tiers.get("tier_1") or fm.get(
        "description", "Strategic capability aligned with enterprise governance."
    )
    tier2 = tiers.get("tier_2") or "Operational workflow with RACI and DACI authority controls."
    tier3 = tiers.get("tier_3") or "System transaction bindings and queueing parameters."

    yaml_str = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True).strip()
    md_content = f"""---
{yaml_str}
---

# {fm["name"]}

## Executive Summary
{tier1}

## 1. Strategic Intent & Outcome (Tier 1 - Executive Level)
{tier1}

## 2. Operational Workflow & RACI (Tier 2 - Process Architect Level)
{tier2}

## 3. Systems Math & Simulation Parameters (Tier 3 - Simulation Engineer Level)
{tier3}
"""
    target_file.write_text(md_content, encoding="utf-8")


def _write_role_markdown(target_file: pathlib.Path, role_data: dict[str, Any]) -> None:
    fm = dict(role_data)
    fm.pop("source_layer", None)
    role_id = fm.get("id", target_file.stem)
    fm["id"] = role_id
    fm.setdefault("type", "role")
    name = fm.setdefault("name", role_id.replace("role_", "").replace("_", " ").title())
    dept = fm.setdefault("department", "Enterprise Operations")
    limit = float(fm.setdefault("approval_limit_usd", 100000.0))
    desc = fm.pop("description", f"Operational and governance responsibilities for {name}.")

    yaml_str = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True).strip()
    md_content = f"""---
{yaml_str}
---
# Role Definition: {name}

- **Role ID**: `{role_id}`
- **Department**: {dept}
- **Approval Limit**: ${limit:,.2f} USD

## Key Responsibilities
- {desc}
"""
    target_file.write_text(md_content, encoding="utf-8")


def _write_asset_markdown(target_file: pathlib.Path, asset_data: dict[str, Any]) -> None:
    fm = dict(asset_data)
    fm.pop("source_layer", None)
    asset_id = fm.get("id", target_file.stem)
    fm["id"] = asset_id
    name = fm.setdefault("name", asset_id)
    fm.setdefault("asset_type", "it_application")
    fm.setdefault("version", "1.0.0")
    fm.setdefault("status", "operational")
    fm.setdefault("sla_uptime_percent", 99.9)
    fm.setdefault("capacity_max_tps", 500)
    fm.setdefault("parent_asset_id", None)
    desc = fm.pop("description", f"Enterprise IT asset node for {name}.")

    yaml_str = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True).strip()
    md_content = f"""---
{yaml_str}
---

# Enterprise Asset: {name}

{desc}
"""
    target_file.write_text(md_content, encoding="utf-8")


def import_bundle(
    bundle_path: pathlib.Path,
    profiles_root: pathlib.Path,
    output_dir: pathlib.Path,
    root: pathlib.Path,
    skip_build: bool = False,
) -> int:
    bundle = json.loads(bundle_path.read_text(encoding="utf-8"))
    prof_meta = dict(bundle.get("profile", {}))
    profile_id = prof_meta.get("profile_id")
    if not profile_id:
        print("❌ Bundle is missing 'profile.profile_id'")
        return 1

    prof_meta.setdefault("name", profile_id.replace("_", " ").title())
    prof_meta.setdefault("version", "1.0.0")
    prof_meta.setdefault("extends", ["manufacturing"])
    prof_meta.setdefault("lifecycles", ["S2P"])

    p_dir = profiles_root / profile_id
    for folder in [
        "elements",
        "roles",
        "assets",
        "lifecycles",
        "ontology",
        "simulations",
        "patches",
    ]:
        (p_dir / folder).mkdir(parents=True, exist_ok=True)

    (p_dir / "profile.json").write_text(json.dumps(prof_meta, indent=2), encoding="utf-8")

    # Prepare ontology/taxonomies.json
    tax = dict(bundle.get("taxonomy", {}))
    tax_lcs = list(tax.get("lifecycles", []))
    existing_lc_ids = {item.get("id") for item in tax_lcs if isinstance(item, dict)}
    for lc_id, lc_obj in bundle.get("lifecycles", {}).items():
        if lc_id not in existing_lc_ids:
            tax_lcs.append(
                {
                    "id": lc_id,
                    "name": lc_obj.get("name", lc_id),
                    "description": lc_obj.get("description", f"Lifecycle {lc_id}"),
                }
            )
    tax["lifecycles"] = tax_lcs
    tax.setdefault("raci_definitions", {})
    (p_dir / "ontology" / "taxonomies.json").write_text(
        json.dumps(tax, indent=2), encoding="utf-8"
    )

    # Write roles
    for role_id, role_obj in bundle.get("roles", {}).items():
        _write_role_markdown(p_dir / "roles" / f"{role_id}.md", role_obj)

    # Write assets
    for asset_id, asset_obj in bundle.get("assets", {}).items():
        _write_asset_markdown(p_dir / "assets" / f"{asset_id}.md", asset_obj)

    # Write elements
    for elem_id, elem_entry in bundle.get("elements", {}).items():
        _write_element_markdown(p_dir / "elements" / f"{elem_id}.md", elem_entry)

    # Write lifecycles
    for lc_id, lc_obj in bundle.get("lifecycles", {}).items():
        clean_lc = dict(lc_obj)
        clean_lc.pop("source_layer", None)
        clean_lc.setdefault("lifecycle_id", lc_id)
        clean_lc.setdefault("name", lc_id)
        clean_lc.setdefault("version", "1.0.0")
        clean_lc.setdefault("description", f"Customized {lc_id} lifecycle")
        clean_lc.setdefault("milestones", [])
        lc_file = p_dir / "lifecycles" / f"lifecycle_{lc_id.lower()}.json"
        lc_file.write_text(json.dumps(clean_lc, indent=2), encoding="utf-8")

    # Write patches
    for idx, patch_obj in enumerate(bundle.get("patches", [])):
        if isinstance(patch_obj, dict) and patch_obj.get("target"):
            target_name = patch_obj["target"]
            patch_file = p_dir / "patches" / f"patch_{idx + 1}_{target_name}.yaml"
            patch_file.write_text(
                yaml.safe_dump(patch_obj, sort_keys=False, allow_unicode=True),
                encoding="utf-8",
            )

    print(f"[+] Materialized custom profile overlay '{profile_id}' into {p_dir}")

    if skip_build:
        return 0

    val_script = root / "tools" / "validate_and_build.py"
    res = subprocess.run(
        [
            "uv",
            "run",
            str(val_script),
            "--profile",
            profile_id,
            "--profiles-root",
            str(profiles_root),
            "--output-dir",
            str(output_dir),
        ],
        check=False,
    )
    return res.returncode


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Import a Designer Studio .vcm.json bundle into profiles/<custom_id>/"
    )
    parser.add_argument("bundle_path", help="Path to exported .vcm.json bundle")
    parser.add_argument("--profiles-root", default="profiles", help="Path to profiles directory")
    parser.add_argument("--output-dir", default="index", help="Output directory path")
    parser.add_argument(
        "--skip-build", action="store_true", help="Only materialize files without running validator"
    )
    args = parser.parse_args()

    root = pathlib.Path(__file__).resolve().parent.parent
    bundle_path = pathlib.Path(args.bundle_path).resolve()
    if not bundle_path.exists():
        print(f"❌ Bundle file not found: {bundle_path}")
        sys.exit(1)

    profiles_root = pathlib.Path(args.profiles_root)
    if not profiles_root.is_absolute():
        profiles_root = root / profiles_root

    output_dir = pathlib.Path(args.output_dir)
    if not output_dir.is_absolute():
        output_dir = root / output_dir

    rc = import_bundle(bundle_path, profiles_root, output_dir, root, skip_build=args.skip_build)
    sys.exit(rc)


if __name__ == "__main__":
    main()
