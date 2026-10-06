#!/usr/bin/env python3
import argparse
import pathlib
import json

def main():
    parser = argparse.ArgumentParser(description="Create a new industry profile")
    parser.add_argument("profile_id", help="ID of the new profile (e.g. healthcare)")
    parser.add_argument("--extends", default="core", help="Parent profile ID")
    parser.add_argument("--name", default="", help="Display name")
    args = parser.parse_args()

    root = pathlib.Path(__file__).parent.parent.resolve()
    p_dir = root / "profiles" / args.profile_id
    if p_dir.exists():
        print(f"[-] Profile '{args.profile_id}' already exists!")
        return

    for folder in ["elements", "roles", "assets", "lifecycles", "ontology", "simulations", "patches"]:
        (p_dir / folder).mkdir(parents=True, exist_ok=True)

    manifest = {
        "profile_id": args.profile_id,
        "name": args.name or args.profile_id.title(),
        "industry": args.profile_id,
        "version": "1.0.0",
        "extends": [args.extends],
        "lifecycles": ["S2P", "R2R", "H2R"],
        "default_lifecycle": "R2R"
    }
    
    (p_dir / "profile.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    
    tax = {
        "lifecycles": [],
        "raci_definitions": {}
    }
    (p_dir / "ontology" / "taxonomies.json").write_text(json.dumps(tax, indent=2), encoding="utf-8")

    print(f"[+] Created new profile '{args.profile_id}' at {p_dir.relative_to(root)}")

if __name__ == "__main__":
    main()
