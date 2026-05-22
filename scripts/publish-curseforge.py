#!/usr/bin/env python3
"""
Publish all 4 platform variants of TBA to CurseForge as a single modpack version.

Reads .zip files from dist/ produced by scripts/build-variants.py and uploads them
to the TBA modpack project (1414683): the windows variant as the primary file,
then linux / macos-arm64 / macos-x86_64 linked as additional files via
parentFileID — mirroring the per-platform layout publish-modrinth.py uses on
Modrinth, and matching the manual upload convention prior releases followed.

Usage:
    # Dry-run to inspect metadata before publishing
    python scripts/publish-curseforge.py --version 1.0.6 \\
        --changelog-file docs/release-notes-v1.0.6.md --dry-run

    # Publish for real
    python scripts/publish-curseforge.py --version 1.0.6 \\
        --changelog-file docs/release-notes-v1.0.6.md

    # Recovery: a real run uploaded the windows primary then failed partway —
    # reuse that fileID instead of double-uploading the primary.
    python scripts/publish-curseforge.py --version 1.0.6 \\
        --changelog-file docs/release-notes-v1.0.6.md --primary-file-id 8131234

Auth via CURSEFORGE_TOKEN — looked up in the environment, then TBA's .env, then
../StreamCraft/.env (where the token actually lives — the same fallback
publish-modrinth.py uses for MODRINTH_TOKEN). Generate a token at
https://authors-old.curseforge.com/account/api-tokens — needs upload permission.

The script fetches /api/game/versions once and resolves friendly names ("1.21.1",
"Fabric", "Java 21") to CurseForge integer IDs. Misses print a warning.

Idempotency: CurseForge's API has no "find existing version" lookup, so a real
re-run double-uploads. If a run fails after the primary lands, note the printed
primary fileID and resume with --primary-file-id.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path

try:
    import requests
except ImportError:
    print("ERR: requests not installed. Install with: pip install requests")
    sys.exit(1)

try:
    import markdown as _markdown
except ImportError:
    _markdown = None  # falls back to text mode if package not installed


CURSEFORGE_API = "https://minecraft.curseforge.com/api"

# TBA's CurseForge modpack project — https://www.curseforge.com/minecraft/modpacks/theblockacademy
DEFAULT_PROJECT_ID = 1414683

# TBA targets MC 1.21.1 / Fabric. CurseForge wants every compatible MC point
# release advertised; the 1.21 line is "1.21" + "1.21.1". Note: unlike a mod
# project, a modpack project rejects the "Java NN" game-version tag (CF error
# 1009) — only MC versions + the modloader are valid here.
MC_VERSIONS = ["1.21", "1.21.1"]
LOADER_NAME = "Fabric"

# Windows is canonical (no classifier in filename); other platforms get a suffix.
PLATFORMS = ["windows", "linux", "macos-arm64", "macos-x86_64"]
PLATFORM_LABEL = {
    "windows":      "Windows",
    "linux":        "Linux",
    "macos-arm64":  "macOS (Apple Silicon)",
    "macos-x86_64": "macOS (Intel)",
}


def filename_for(version: str, platform: str) -> str:
    suffix = "" if platform == "windows" else f"-{platform}"
    return f"TBA-{version}{suffix}.zip"


def load_dotenv(path: Path) -> None:
    """Minimal .env loader: KEY=VALUE per line, no quoting/expansion."""
    if not path.exists():
        return
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key, value = key.strip(), value.strip()
        if key and value and key not in os.environ:
            os.environ[key] = value


def render_changelog(markdown_text: str, fmt: str) -> tuple[str, str]:
    """
    Returns (rendered, changelogType) for upload. CurseForge's "markdown"
    changelogType doesn't render reliably (raw markup leaks through), so by
    default we convert to HTML client-side and send changelogType="html".
    """
    if fmt == "html":
        if _markdown is None:
            print("WARN python-markdown not installed; install via 'pip install markdown'. "
                  "Falling back to changelogType=text.")
            return markdown_text, "text"
        return _markdown.markdown(markdown_text), "html"
    if fmt == "markdown":
        return markdown_text, "markdown"
    return markdown_text, "text"


def fetch_game_versions(token: str) -> dict[tuple[int, str], int]:
    """Fetch the CurseForge game-version catalog as a (typeId, name)->id map."""
    r = requests.get(
        f"{CURSEFORGE_API}/game/versions",
        headers={"X-Api-Token": token},
        timeout=30,
    )
    r.raise_for_status()
    return {(v["gameVersionTypeID"], v["name"]): v["id"] for v in r.json()}


def fetch_version_type_ids(token: str) -> dict[str, int]:
    """Return slug->typeId map for /api/game/version-types."""
    r = requests.get(
        f"{CURSEFORGE_API}/game/version-types",
        headers={"X-Api-Token": token},
        timeout=30,
    )
    r.raise_for_status()
    return {t["slug"]: t["id"] for t in r.json()}


def expected_type_slug(name: str) -> str | None:
    """
    Derive the version-type slug an upload-bound name must live under.
    "1.21.1"  -> "minecraft-1-21"
    "Fabric"  -> "modloader"
    "Java 21" -> "java"
    """
    if name in ("Fabric", "NeoForge"):
        return "modloader"
    if name.startswith("Java "):
        return "java"
    m = re.match(r"^(\d+)\.(\d+)(?:\.\d+)?$", name)
    if m:
        return f"minecraft-{m.group(1)}-{m.group(2)}"
    return None


def resolve_game_version_ids(
    catalog: dict[tuple[int, str], int],
    type_ids: dict[str, int],
) -> list[int]:
    """Build the gameVersions int-ID array CurseForge expects, filtered by the
    right version-type bucket per name (CF lists "1.21.1" under several types)."""
    ids: list[int] = []
    missing: list[str] = []
    for name in [*MC_VERSIONS, LOADER_NAME]:
        slug = expected_type_slug(name)
        type_id = type_ids.get(slug) if slug else None
        cf_id = catalog.get((type_id, name)) if type_id else None
        if cf_id is None:
            missing.append(f"{name} (slug={slug})")
        else:
            ids.append(cf_id)
    if missing:
        print(f"  WARN CF catalog missing {missing}; "
              f"those entries will not appear on the file's version list")
    return ids


def upload_file(project_id: int, zip_path: Path, metadata: dict, token: str) -> int:
    """POST one file. Returns the integer fileID assigned by CurseForge."""
    url = f"{CURSEFORGE_API}/projects/{project_id}/upload-file"
    size_mb = zip_path.stat().st_size / 1_000_000
    print(f"  POST {url} ({size_mb:.1f} MB, {zip_path.name}) ...")
    with zip_path.open("rb") as fh:
        files = {
            "metadata": (None, json.dumps(metadata), "application/json"),
            "file":     (zip_path.name, fh, "application/zip"),
        }
        r = requests.post(url, headers={"X-Api-Token": token}, files=files, timeout=600)
    if r.status_code >= 400:
        raise RuntimeError(f"CurseForge {r.status_code}: {r.text}")
    data = r.json()
    file_id = data.get("id")
    if not isinstance(file_id, int):
        raise RuntimeError(f"CurseForge returned no file id: {data}")
    print(f"    OK fileID={file_id}")
    return file_id


def main() -> int:
    p = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    p.add_argument("--version", required=True, help="TBA pack version (e.g. 1.0.6)")
    p.add_argument("--changelog-file", required=True,
                   help="Markdown file with the release notes (used verbatim)")
    p.add_argument("--project-id", type=int, default=DEFAULT_PROJECT_ID,
                   help=f"CurseForge modpack project ID (default: {DEFAULT_PROJECT_ID})")
    p.add_argument("--type", default="release", choices=["release", "beta", "alpha"])
    p.add_argument("--dist-dir", default="dist",
                   help="Directory containing the 4 .zip files")
    p.add_argument("--changelog-format", default="html",
                   choices=["html", "markdown", "text"],
                   help="changelogType to send. Default 'html' — CurseForge's "
                        "'markdown' type renders raw markup unreliably.")
    p.add_argument("--primary-file-id", type=int, default=None,
                   help="Recovery: reuse an existing windows fileID as the parent "
                        "for the 3 additional files (skips the primary upload).")
    p.add_argument("--dry-run", action="store_true",
                   help="Print metadata without uploading")
    args = p.parse_args()

    project_root = Path(__file__).resolve().parent.parent
    # Try TBA's .env first, then StreamCraft's (where CURSEFORGE_TOKEN lives).
    load_dotenv(project_root / ".env")
    load_dotenv(project_root.parent / "StreamCraft" / ".env")

    token = os.environ.get("CURSEFORGE_TOKEN", "")
    if not token and not args.dry_run:
        print("ERR CURSEFORGE_TOKEN not set (env var, TBA/.env, or StreamCraft/.env)")
        return 1

    dist = (project_root / args.dist_dir).resolve()
    if not dist.is_dir():
        print(f"ERR dist dir not found: {dist}")
        return 1

    # Verify all 4 files exist before doing anything.
    files: list[tuple[str, Path]] = []
    missing: list[str] = []
    for plat in PLATFORMS:
        path = dist / filename_for(args.version, plat)
        if path.exists():
            files.append((plat, path))
        else:
            missing.append(path.name)
    if missing:
        print(f"ERR missing artifacts in {dist}:")
        for m in missing:
            print(f"  - {m}")
        print("Run: python scripts/build-variants.py")
        return 1

    changelog_path = (project_root / args.changelog_file).resolve()
    if not changelog_path.exists():
        print(f"ERR changelog file not found: {changelog_path}")
        return 1
    raw_changelog = changelog_path.read_text(encoding="utf-8").strip()
    changelog, changelog_type = render_changelog(raw_changelog, args.changelog_format)

    primary_filename = filename_for(args.version, "windows")

    print(f"Project ID:     {args.project_id}")
    print(f"Version:        v{args.version} ({args.type})")
    print(f"MC versions:    {MC_VERSIONS} | {LOADER_NAME}")
    print(f"Files ({len(files)}):")
    total_mb = 0.0
    for plat, path in files:
        size_mb = path.stat().st_size / 1_000_000
        total_mb += size_mb
        marker = "  [primary]" if path.name == primary_filename else ""
        print(f"  {plat:14s} {path.name}  ({size_mb:.1f} MB){marker}")
    print(f"Total:          {total_mb:.1f} MB")
    print(f"Changelog:      {changelog_path.name} "
          f"({len(changelog)} chars, type={changelog_type})")

    # Resolve gameVersion integer IDs (CF wants ints, not strings). Runs in
    # dry-run too when a token is present — surfaces catalog drift early.
    game_version_ids: list[int] = []
    if token:
        try:
            type_ids = fetch_version_type_ids(token)
            catalog = fetch_game_versions(token)
            print(f"Loaded {len(catalog)} CF game-version entries "
                  f"across {len(type_ids)} version-types")
            game_version_ids = resolve_game_version_ids(catalog, type_ids)
        except Exception as e:
            print(f"ERR could not fetch CF game-version catalog: {e}")
            if not args.dry_run:
                return 1
            game_version_ids = [-1]
    else:
        game_version_ids = [-1]  # dry-run without a token
    print(f"gameVersion IDs: {game_version_ids}")

    primary_meta = {
        "changelog": changelog,
        "changelogType": changelog_type,
        "displayName": primary_filename,
        "gameVersions": game_version_ids,
        "releaseType": args.type,
    }

    # Additional-file metadata: CF rejects `gameVersions` on children (error
    # 1013) — they inherit version metadata from the parent via parentFileID.
    def extra_metadata(plat: str, parent_fid: int) -> dict:
        return {
            "changelog": changelog,
            "changelogType": changelog_type,
            "displayName": filename_for(args.version, plat),
            "releaseType": args.type,
            "parentFileID": parent_fid,
        }

    additional = [(plat, path) for plat, path in files if plat != "windows"]

    if args.dry_run:
        print("\nDRY-RUN — metadata that would be uploaded:")
        print(f"\nPRIMARY ({primary_filename}):")
        print(json.dumps(primary_meta, indent=2))
        for plat, path in additional:
            print(f"\nADDITIONAL ({path.name}, {PLATFORM_LABEL[plat]}):")
            print(json.dumps(extra_metadata(plat, "<primary fileID resolved at upload>"), indent=2))
        return 0

    # Real upload: windows primary first (or reuse --primary-file-id), then the
    # 3 additional files referencing the primary's fileID via parentFileID.
    print(f"\nStep 1/{1 + len(additional)}: primary file ...")
    if args.primary_file_id is not None:
        primary_id = args.primary_file_id
        print(f"  REUSE primary fileID={primary_id} (skipping windows upload)")
    else:
        windows_path = next(path for plat, path in files if plat == "windows")
        primary_id = upload_file(args.project_id, windows_path, primary_meta, token)

    for i, (plat, path) in enumerate(additional, start=2):
        print(f"\nStep {i}/{1 + len(additional)}: additional file ({PLATFORM_LABEL[plat]}) ...")
        try:
            upload_file(args.project_id, path, extra_metadata(plat, primary_id), token)
        except Exception as e:
            print(f"  FAILED ({plat}): {e}")
            print(f"  Primary landed as fileID={primary_id}. Resume the rest with:")
            print(f"    python scripts/publish-curseforge.py --version {args.version} "
                  f"--changelog-file {args.changelog_file} --primary-file-id {primary_id}")
            return 1
        time.sleep(1.5)  # stagger — CF flakes with 500s on rapid successive calls

    print(f"\nAll {len(files)} files uploaded (primary fileID={primary_id}).")
    print("Files enter CurseForge's moderation queue before going live.")
    print(f"URL: https://www.curseforge.com/minecraft/modpacks/theblockacademy/files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
