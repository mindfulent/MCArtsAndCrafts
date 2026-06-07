# TBA Deployment Guide

This guide documents the complete workflow for updating the modpack and deploying changes to the Bloom.host server.

## Architecture Overview

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  Local Dev      │────►│  GitHub Release  │────►│  Bloom.host     │
│  (packwiz)      │     │  (.mrpack)       │     │  (mrpack4server)│
└─────────────────┘     └──────────────────┘     └─────────────────┘
```

**Key Components:**
- **Packwiz**: Local tool for managing mods and exporting .mrpack files
- **GitHub Releases**: Hosts versioned .mrpack files for distribution
- **mrpack4server**: Server-side tool that downloads and installs modpacks
- **modpack-info.json**: Server config pointing to the GitHub release URL

## How mrpack4server Works

mrpack4server looks for modpack configuration in this priority order:
1. `modpack-info.json` embedded in the jar (for modpack makers)
2. `modpack-info.json` in server root directory ← **We use this**
3. `local.mrpack` in server root directory

**Important**: If `modpack-info.json` exists, it takes precedence over `local.mrpack`. This is why we use the GitHub release workflow.

### modpack-info.json Structure

```json
{
  "project_id": "tba",
  "version_id": "0.9.19",
  "display_name": "TBA",
  "display_version": "0.9.19",
  "url": "https://github.com/slashdaemon/TBA/releases/download/v0.9.19/TBA-0.9.19.mrpack",
  "size": 1567913,
  "sha512": "66043d9cbe0c0a719a6b1c672cac29d6...",
  "whitelisted_domains": ["github.com", "objects.githubusercontent.com"],
  "non_overwritable_paths": ["world", "server.properties", "ops.json", ...]
}
```

## Complete Deployment Workflow

### Step 1: Make Changes Locally

```bash
# Add a new mod
./packwiz.exe mr install <mod-slug> -y

# Update all mods
./packwiz.exe update --all

# Remove a mod
./packwiz.exe remove <mod-name> -y
```

### Step 2: Bump Version

Edit `pack.toml` and increment the version:
```toml
version = "0.9.20"  # Increment from previous
```

### Step 3: Export the Modpack

For single-variant releases (StreamCraft pinned to one platform — historical, pre-0.7.26):
```bash
./packwiz.exe modrinth export
./packwiz.exe curseforge export
# Creates: TBA-0.9.20.mrpack and TBA-0.9.20.zip in the repo root
```

For multi-platform releases (StreamCraft 0.7.26+, with file IDs registered in `scripts/build-variants.py`):
```bash
python scripts/build-variants.py
# Builds 8 artifacts in dist/:
#   TBA-0.9.20.{mrpack,zip}                  Windows (canonical)
#   TBA-0.9.20-linux.{mrpack,zip}            Linux (also what the server uses)
#   TBA-0.9.20-macos-arm64.{mrpack,zip}      Apple Silicon
#   TBA-0.9.20-macos-x86_64.{mrpack,zip}     Intel Mac
```

The script swaps `mods/streamcraft-live.pw.toml` per platform, exports, renames, and restores the original toml at the end. Build a single platform with `--platform <name>`.

### Step 4: Commit and Push

```bash
git add -A
git commit -m "v0.9.20 - Add new mods"
git push
```

### Step 5: Create GitHub Release

Single variant:
```bash
gh release create v0.9.20 TBA-0.9.20.mrpack TBA-0.9.20.zip --title "v0.9.20" --notes "Release notes here"
```

Multi-platform (all 8 artifacts):
```bash
gh release create v0.9.20 dist/TBA-0.9.20*.{mrpack,zip} --title "v0.9.20" --notes "Release notes here"
```

Then upload all 4 `.zip` files to the CurseForge modpack page (Windows = primary release, others = additional release files). CurseForge reviews each file independently, so Mac/Linux variants ship in waves.

### Step 6: Update Server Configuration

```bash
python server-config.py update-pack 0.9.20
```

This command:
- Reads the local `dist/TBA-0.9.20-linux.mrpack` (or repo root `TBA-0.9.20.mrpack` for legacy single-variant releases)
- Calculates SHA512 hash and file size
- Updates `modpack-info.json` on the server via SFTP

The server runs on Linux, so `update-pack` defaults to `--variant linux`. The Linux variant bundles the Linux StreamCraft JAR; using any other variant on the server would crash StreamCraft on startup.

### Step 7: Restart Server

```bash
python server-config.py restart
```

The server will:
1. Detect the new version in modpack-info.json
2. Download the .mrpack from GitHub
3. Validate the SHA512 hash
4. Extract and install new mods
5. Start the Minecraft server

## Quick Reference

```bash
# Full deployment (after making changes)
./packwiz.exe modrinth export
git add -A && git commit -m "v0.9.X - description" && git push
gh release create v0.9.X TBA-0.9.X.mrpack --title "v0.9.X"
python server-config.py update-pack 0.9.X
python server-config.py restart
```

## Troubleshooting

### Server shows wrong version

Check `modpack-info.json` on the server:
```bash
python server-config.py list
# Then inspect the file via Bloom.host panel
```

The `version_id` should match your release.

### Hash mismatch error

```
Couldn't validate file! Expected hash: X, got: Y
```

This means the file on GitHub doesn't match the hash in modpack-info.json.

**Causes:**
- GitHub CDN caching (wait a few minutes and retry)
- Wrong .mrpack file uploaded to release
- modpack-info.json has stale hash

**Fix:**
```bash
# Re-run update-pack to recalculate hash from local file
python server-config.py update-pack 0.9.X

# Ensure GitHub release has the correct file
gh release view v0.9.X --json assets
```

### Mods not updating

mrpack4server caches downloaded mods. To force a clean install:

1. Stop the server
2. Delete `/mods` folder via Bloom.host panel or SFTP
3. Delete `/.mrpack4server` folder
4. Start the server

### .mrpack file too large

Check `.packwizignore` to ensure build artifacts aren't included:
```
*.mrpack
backup_*/
*.jar
.env
__pycache__/
```

Expected size: ~1-3 MB (mods are downloaded, not bundled)

## Server Management Commands

```bash
python server-config.py status        # Check server status
python server-config.py start         # Start server
python server-config.py stop          # Stop server
python server-config.py restart       # Restart server
python server-config.py cmd "say hi"  # Send console command
python server-config.py list          # List server files
```

## Version History

Versions follow semantic versioning: `0.MAJOR.MINOR`
- **MAJOR**: Significant content additions or breaking changes
- **MINOR**: Bug fixes, small additions, config changes

See [CHANGELOG.md](../CHANGELOG.md) for detailed version history.
