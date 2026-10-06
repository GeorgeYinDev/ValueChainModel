import os
import sys
import json
import yaml
from pathlib import Path
from dataclasses import dataclass
from typing import Dict, Any, List, Tuple, Optional

try:
    import jsonschema
except ImportError:
    jsonschema = None

@dataclass
class EffectiveProfile:
    profile_id: str
    manifest: Dict[str, Any]
    layers: List[str]
    taxonomy: Dict[str, Any]
    element_files: Dict[str, Tuple[Path, str]]
    role_files: Dict[str, Tuple[Path, str]]
    asset_files: Dict[str, Tuple[Path, str]]
    lifecycle_files: Dict[str, Tuple[Path, str]]
    scenario_files: Dict[str, Tuple[Path, str]]
    patches: List[Dict[str, Any]]
    output_dir: Path

def default_profile() -> str:
    return os.environ.get("VCM_PROFILE", "manufacturing")

def list_profiles(profiles_root: Path) -> List[Dict[str, Any]]:
    profiles = []
    if profiles_root.exists():
        for p_dir in sorted(profiles_root.iterdir()):
            if p_dir.is_dir() and (p_dir / "profile.json").exists():
                try:
                    manifest = json.loads((p_dir / "profile.json").read_text(encoding="utf-8"))
                    profiles.append(manifest)
                except Exception:
                    pass
    return profiles

def _resolve_layers(profiles_root: Path, profile_id: str, path: Optional[List[str]] = None) -> List[str]:
    if path is None:
        path = []
    if profile_id in path:
        cycle_str = " -> ".join(path + [profile_id])
        raise ValueError(f"Inheritance cycle detected: {cycle_str}")
    
    manifest_path = profiles_root / profile_id / "profile.json"
    if not manifest_path.exists():
        raise ValueError(f"Profile '{profile_id}' not found at {manifest_path}")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    
    current_path = path + [profile_id]
    layers = []
    for parent in manifest.get("extends", []):
        layers.extend(_resolve_layers(profiles_root, parent, current_path))
    
    unique_layers = []
    for layer in layers:
        if layer in unique_layers:
            unique_layers.remove(layer)
        unique_layers.append(layer)
        
    unique_layers.append(profile_id)
    return unique_layers

def parse_frontmatter(file_path: Path) -> Tuple[Dict[str, Any], str]:
    """Extract YAML frontmatter and body from Markdown file."""
    content = file_path.read_text(encoding="utf-8")
    frontmatter = {}
    body = content
    
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            try:
                frontmatter = yaml.safe_load(parts[1]) or {}
                body = parts[2].strip()
            except yaml.YAMLError as e:
                print(f"[-] YAML Parsing Error in {file_path}: {e}")
                sys.exit(1)
            
    return frontmatter, body

def _collect_files(directory: Path, file_dict: Dict[str, Tuple[Path, str]], layer: str, file_type: str = "element"):
    if not directory.exists():
        return
    for f in sorted(directory.rglob("*.*")):
        if f.suffix in [".md", ".json"]:
            identifier = f.stem
            override_layer = None
            if f.suffix == ".md":
                fm, _ = parse_frontmatter(f)
                identifier = fm.get("id", f.stem)
                override_layer = fm.get("overrides")
            elif f.suffix == ".json":
                try:
                    data = json.loads(f.read_text(encoding="utf-8"))
                    identifier = data.get("id", data.get("lifecycle_id", data.get("scenario_id", f.stem)))
                    override_layer = data.get("overrides")
                except Exception:
                    identifier = f.stem

            if identifier in file_dict:
                existing_file, existing_layer = file_dict[identifier]
                if existing_layer != layer:
                    if override_layer:
                        file_dict[identifier] = (f, layer)
                    else:
                        raise ValueError(
                            f"Accidental ID collision in {file_type}s: '{identifier}' in layer '{layer}' clashes with inherited '{identifier}' from layer '{existing_layer}'. Use 'overrides: {existing_layer}' to replace intentionally."
                        )
                else:
                    file_dict[identifier] = (f, layer)
            else:
                file_dict[identifier] = (f, layer)

def resolve_profile(profiles_root: Path, profile_id: str, repo_root: Path) -> EffectiveProfile:
    layers = _resolve_layers(profiles_root, profile_id)
    
    schema_dir = repo_root / "schema"
    profile_schema = None
    patch_schema = None
    if jsonschema and schema_dir.exists():
        p_schema_file = schema_dir / "profile_manifest.schema.json"
        if p_schema_file.exists():
            profile_schema = json.loads(p_schema_file.read_text(encoding="utf-8"))
        patch_schema_file = schema_dir / "profile_patch.schema.json"
        if patch_schema_file.exists():
            patch_schema = json.loads(patch_schema_file.read_text(encoding="utf-8"))

    taxonomy = {
        "lifecycles": [],
        "element_types": [],
        "relation_types": [],
        "raci_definitions": {},
        "daci_definitions": {},
        "lod_tiers": []
    }
    
    element_files: Dict[str, Tuple[Path, str]] = {}
    role_files: Dict[str, Tuple[Path, str]] = {}
    asset_files: Dict[str, Tuple[Path, str]] = {}
    lifecycle_files: Dict[str, Tuple[Path, str]] = {}
    scenario_files: Dict[str, Tuple[Path, str]] = {}
    patches: List[Dict[str, Any]] = []
    target_manifest: Dict[str, Any] = {}
    
    for layer in layers:
        layer_dir = profiles_root / layer
        manifest_path = layer_dir / "profile.json"
        if manifest_path.exists():
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            if layer == profile_id:
                target_manifest = manifest
            if jsonschema and profile_schema:
                try:
                    jsonschema.validate(instance=manifest, schema=profile_schema)
                except jsonschema.exceptions.ValidationError as e:
                    raise ValueError(f"Profile schema validation error in {manifest_path}: {e.message}")
        
        # Merge taxonomy
        tax_path = layer_dir / "ontology" / "taxonomies.json"
        if tax_path.exists():
            tax_data = json.loads(tax_path.read_text(encoding="utf-8"))
            for lc in tax_data.get("lifecycles", []):
                existing = [x for x in taxonomy["lifecycles"] if x["id"] == lc["id"]]
                if existing:
                    taxonomy["lifecycles"].remove(existing[0])
                taxonomy["lifecycles"].append(lc)
            
            for k in ["element_types", "relation_types"]:
                for t in tax_data.get(k, []):
                    if t not in taxonomy[k]:
                        taxonomy[k].append(t)
                        
            taxonomy["raci_definitions"].update(tax_data.get("raci_definitions", {}))
            taxonomy["daci_definitions"].update(tax_data.get("daci_definitions", {}))
            
            for lod in tax_data.get("lod_tiers", []):
                existing = [x for x in taxonomy["lod_tiers"] if x["id"] == lod["id"]]
                if existing:
                    taxonomy["lod_tiers"].remove(existing[0])
                taxonomy["lod_tiers"].append(lod)
                
        # Resolve files with collision checks
        _collect_files(layer_dir / "elements", element_files, layer, "element")
        _collect_files(layer_dir / "roles", role_files, layer, "role")
        _collect_files(layer_dir / "assets", asset_files, layer, "asset")
        _collect_files(layer_dir / "lifecycles", lifecycle_files, layer, "lifecycle")
        _collect_files(layer_dir / "simulations", scenario_files, layer, "scenario")
        
        # Patches
        patch_dir = layer_dir / "patches"
        if patch_dir.exists():
            for p in sorted(patch_dir.glob("*.yaml")):
                with p.open("r", encoding="utf-8") as f:
                    patch_content = yaml.safe_load(f)
                    if patch_content:
                        if jsonschema and patch_schema:
                            try:
                                jsonschema.validate(instance=patch_content, schema=patch_schema)
                            except jsonschema.exceptions.ValidationError as e:
                                raise ValueError(f"Patch schema validation error in {p}: {e.message}")
                        patches.append(patch_content)
                    
    return EffectiveProfile(
        profile_id=profile_id,
        manifest=target_manifest,
        layers=layers,
        taxonomy=taxonomy,
        element_files=element_files,
        role_files=role_files,
        asset_files=asset_files,
        lifecycle_files=lifecycle_files,
        scenario_files=scenario_files,
        patches=patches,
        output_dir=repo_root / "index" / profile_id
    )
