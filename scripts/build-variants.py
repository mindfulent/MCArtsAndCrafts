#!/usr/bin/env python3
"""
Build per-platform TBA modpack variants.

StreamCraft ships platform-specific JARs (Windows, Linux, macOS-arm64,
macOS-x86_64) because of native LiveKit FFI / JavaCV / JNA dependencies.
Packwiz pins one CurseForge file ID per mod, so each platform needs its
own modpack export with the matching StreamCraft JAR.

Usage:
    python scripts/build-variants.py                       # build all platforms
    python scripts/build-variants.py --platform windows    # one platform
    python scripts/build-variants.py --version 1.0.4       # override pack.toml
    python scripts/build-variants.py --streamcraft 0.7.26+mc1.21.1

Output: dist/TBA-<version>[-<platform>].{mrpack,zip}
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PACKWIZ = REPO_ROOT / "packwiz.exe"
STREAMCRAFT_TOML = REPO_ROOT / "mods" / "streamcraft-live.pw.toml"
PACK_TOML = REPO_ROOT / "pack.toml"
DIST = REPO_ROOT / "dist"

# Windows is canonical (no classifier in filename); other platforms get a suffix.
PLATFORMS = ["windows", "linux", "macos-arm64", "macos-x86_64"]


@dataclass(frozen=True)
class StreamCraftFile:
    """A registered StreamCraft artifact. Exactly one of cf_file_id / mr_url
    must be set — selects CurseForge metadata mode vs direct URL mode."""
    filename: str
    sha1: str
    cf_file_id: int | None = None
    mr_url: str | None = None

    def __post_init__(self) -> None:
        if (self.cf_file_id is None) == (self.mr_url is None):
            raise ValueError(
                f"StreamCraftFile {self.filename}: exactly one of cf_file_id or mr_url must be set"
            )


# Registry of StreamCraft files per version + platform.
#
# CurseForge mode (preferred — CurseForge-First Policy):
#   StreamCraftFile(filename=..., sha1=..., cf_file_id=NNNNNNN)
#
# Modrinth URL mode (fallback when CF approval is pending or unavailable):
#   StreamCraftFile(filename=..., sha1=..., mr_url="https://cdn.modrinth.com/...")
#   When using mr_url, mrpack4server needs `cdn.modrinth.com` in
#   whitelisted_domains (server-config.py update_modpack_info handles this).
#
# When CurseForge later approves a Modrinth-pinned version, swap the entry to
# cf_file_id mode so we're back on CF for downstream CurseForge App users.
STREAMCRAFT_REGISTRY: dict[str, dict[str, StreamCraftFile]] = {
    "0.6.2+mc1.21.1": {
        "windows": StreamCraftFile(
            filename="streamcraft-0.6.2+mc1.21.1.jar",
            sha1="681de053207181b5672da0cba78696fa71f58390",
            cf_file_id=7952947,
        ),
    },
    "0.7.26+mc1.21.1": {
        "windows": StreamCraftFile(
            filename="streamcraft-0.7.26+mc1.21.1.jar",
            sha1="69c5de6703750e88e0fffee9d74e0ad6cad141df",
            cf_file_id=7996534,
        ),
        "linux": StreamCraftFile(
            filename="streamcraft-0.7.26+mc1.21.1-linux.jar",
            sha1="e0b4e084263b54cdcffe49a6b7867a66f9746d72",
            cf_file_id=7996556,
        ),
        "macos-arm64": StreamCraftFile(
            filename="streamcraft-0.7.26+mc1.21.1-macos-arm64.jar",
            sha1="bdaae7d1b1097488326bbdb7ffda8dc409ffaa27",
            cf_file_id=7996538,
        ),
        "macos-x86_64": StreamCraftFile(
            filename="streamcraft-0.7.26+mc1.21.1-macos-x86_64.jar",
            sha1="3a85e944b38260ff573f7bef8da55f6229a5b65e",
            cf_file_id=7996545,
        ),
    },
    "0.8.25+mc1.21.1": {
        "windows": StreamCraftFile(
            filename="streamcraft-0.8.25+mc1.21.1.jar",
            sha1="b9dd7d132508566c2b3d1b0b1c42185941134b11",
            cf_file_id=8124065,
        ),
        "linux": StreamCraftFile(
            filename="streamcraft-0.8.25+mc1.21.1-linux.jar",
            sha1="701dc95e1d2080f5c48bd31841a8f4ae316bffcc",
            cf_file_id=8124066,
        ),
        "macos-arm64": StreamCraftFile(
            filename="streamcraft-0.8.25+mc1.21.1-macos-arm64.jar",
            sha1="92a93cb03065ab2af25e773d2257fde7832aa86d",
            cf_file_id=8124068,
        ),
        "macos-x86_64": StreamCraftFile(
            filename="streamcraft-0.8.25+mc1.21.1-macos-x86_64.jar",
            sha1="2fd599a4c75dd012ec8865c8d0543c5ee8d1b816",
            cf_file_id=8124069,
        ),
    },
}


def read_pack_version() -> str:
    for line in PACK_TOML.read_text(encoding="utf-8").splitlines():
        if line.startswith("version"):
            return line.split("=", 1)[1].strip().strip('"')
    raise RuntimeError("Could not parse version from pack.toml")


def read_current_streamcraft_version() -> str:
    """Infer the StreamCraft version currently pinned in mods/streamcraft-live.pw.toml.

    Returns the registry key (e.g., '0.6.2+mc1.21.1') by matching the filename.
    """
    text = STREAMCRAFT_TOML.read_text(encoding="utf-8")
    for line in text.splitlines():
        if line.startswith("filename"):
            filename = line.split("=", 1)[1].strip().strip('"')
            for key, variants in STREAMCRAFT_REGISTRY.items():
                for v in variants.values():
                    if v.filename == filename:
                        return key
    raise RuntimeError(
        f"Cannot infer StreamCraft version from {STREAMCRAFT_TOML}. "
        "Pass --streamcraft <version> explicitly."
    )


def write_streamcraft_toml(file: StreamCraftFile) -> None:
    if file.cf_file_id is not None:
        body = f'''name = "StreamCraft Live"
filename = "{file.filename}"
side = "both"

[download]
hash-format = "sha1"
hash = "{file.sha1}"
mode = "metadata:curseforge"

[update]
[update.curseforge]
file-id = {file.cf_file_id}
project-id = 1451729
'''
    else:
        body = f'''name = "StreamCraft Live"
filename = "{file.filename}"
side = "both"

[download]
hash-format = "sha1"
hash = "{file.sha1}"
url = "{file.mr_url}"
'''
    STREAMCRAFT_TOML.write_text(body, encoding="utf-8")


def run(cmd: list[str]) -> None:
    print(f"  $ {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=REPO_ROOT, capture_output=True, text=True)
    if result.returncode != 0:
        sys.stderr.write(result.stdout)
        sys.stderr.write(result.stderr)
        raise RuntimeError(f"Command failed: {' '.join(cmd)}")


def build_one(platform: str, pack_version: str, sc_version: str) -> None:
    if platform not in STREAMCRAFT_REGISTRY[sc_version]:
        raise RuntimeError(
            f"StreamCraft {sc_version} has no '{platform}' variant in the registry. "
            f"Available: {sorted(STREAMCRAFT_REGISTRY[sc_version])}"
        )

    suffix = "" if platform == "windows" else f"-{platform}"
    sc_file = STREAMCRAFT_REGISTRY[sc_version][platform]

    print(f"\n=== Building {platform} (StreamCraft {sc_file.filename}) ===")
    write_streamcraft_toml(sc_file)
    run([str(PACKWIZ), "refresh"])
    run([str(PACKWIZ), "modrinth", "export"])
    run([str(PACKWIZ), "curseforge", "export"])

    # Packwiz writes <pack-name>-<version>.{mrpack,zip} to repo root.
    src_mrpack = REPO_ROOT / f"TBA-{pack_version}.mrpack"
    src_zip = REPO_ROOT / f"TBA-{pack_version}.zip"
    dst_mrpack = DIST / f"TBA-{pack_version}{suffix}.mrpack"
    dst_zip = DIST / f"TBA-{pack_version}{suffix}.zip"

    DIST.mkdir(exist_ok=True)
    shutil.move(str(src_mrpack), str(dst_mrpack))
    shutil.move(str(src_zip), str(dst_zip))
    print(f"  -> {dst_mrpack.name}")
    print(f"  -> {dst_zip.name}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "--platform",
        choices=PLATFORMS,
        help="Build only this platform (default: all four).",
    )
    parser.add_argument(
        "--version",
        help="Override pack version (default: read from pack.toml).",
    )
    parser.add_argument(
        "--streamcraft",
        help="StreamCraft registry key (e.g., '0.7.26+mc1.21.1'). "
             "Default: infer from current mods/streamcraft-live.pw.toml.",
    )
    args = parser.parse_args()

    if not PACKWIZ.exists():
        print(f"error: {PACKWIZ} not found", file=sys.stderr)
        return 1

    pack_version = args.version or read_pack_version()
    sc_version = args.streamcraft or read_current_streamcraft_version()

    if sc_version not in STREAMCRAFT_REGISTRY:
        print(
            f"error: StreamCraft '{sc_version}' not in registry. "
            f"Known: {sorted(STREAMCRAFT_REGISTRY)}",
            file=sys.stderr,
        )
        return 1

    platforms = [args.platform] if args.platform else PLATFORMS
    # Skip platforms missing from this StreamCraft version's registry, with a warning.
    available = []
    for p in platforms:
        if p in STREAMCRAFT_REGISTRY[sc_version]:
            available.append(p)
        else:
            print(f"warn: skipping {p} (no StreamCraft {sc_version} file registered)")
    if not available:
        print("error: no platforms to build", file=sys.stderr)
        return 1

    print(f"Pack version:       {pack_version}")
    print(f"StreamCraft:        {sc_version}")
    print(f"Platforms to build: {', '.join(available)}")

    original_toml = STREAMCRAFT_TOML.read_text(encoding="utf-8")
    try:
        for platform in available:
            build_one(platform, pack_version, sc_version)
    finally:
        STREAMCRAFT_TOML.write_text(original_toml, encoding="utf-8")
        run([str(PACKWIZ), "refresh"])
        print(f"\nRestored {STREAMCRAFT_TOML.name} to original.")

    print(f"\nDone. Artifacts in {DIST}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
