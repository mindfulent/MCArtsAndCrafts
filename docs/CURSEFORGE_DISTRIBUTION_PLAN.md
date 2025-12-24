# CurseForge Distribution Plan

This document outlines everything required to publish MCC on CurseForge as a secondary distribution channel alongside Modrinth.

**Current Status:** Not pursued (as of v0.9.29)
**Effort Estimate:** Medium-High initial setup, ongoing maintenance overhead
**Decision:** Documented for future reference if wider distribution becomes a priority

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Prerequisites](#prerequisites)
3. [Technical Migration Process](#technical-migration-process)
4. [Mod Availability Audit](#mod-availability-audit)
5. [Submission Process](#submission-process)
6. [Ongoing Maintenance](#ongoing-maintenance)
7. [Decision Framework](#decision-framework)

---

## Executive Summary

### Why CurseForge?

- Larger established user base
- CurseForge app and Overwolf integration
- Better discoverability for public modpacks
- Some users prefer/only use CurseForge

### Why It's Complex

- All 80 mods currently have Modrinth metadata
- CurseForge requires mods on their platform to be referenced by project ID (not bundled)
- Maintaining two metadata sources doubles update work
- Different export formats (.mrpack vs .zip with manifest.json)

### Current Architecture

```
MCC/
├── mods/*.pw.toml          # All have Modrinth metadata (update.modrinth section)
├── pack.toml               # References Modrinth as primary
└── Exports to .mrpack      # Modrinth format
```

### Target Architecture for Dual Distribution

```
MCC/
├── mods/*.pw.toml          # Would need BOTH modrinth AND curseforge metadata
├── pack.toml               # No changes needed
├── Exports to .mrpack      # For Modrinth
└── Exports to .zip         # For CurseForge (manifest.json format)
```

---

## Prerequisites

### 1. CurseForge Account Setup

1. Create account at [curseforge.com](https://www.curseforge.com)
2. Apply for author status (required to upload projects)
3. Wait for approval (typically 1-3 days)
4. Set up project: Minecraft → Modpacks → Create Project

### 2. Project Configuration

Required information for CurseForge project:
- **Project name:** MCC
- **Summary:** Fabric 1.21.1 modpack for building, decoration, and multiplayer
- **Description:** Full markdown description with mod list, features, requirements
- **Categories:** Fabric, Multiplayer, Building, Decoration
- **License:** CC BY 4.0 (for pack configuration)
- **Source URL:** GitHub repository link
- **Issues URL:** GitHub issues link

### 3. Required Tools

```bash
# Packwiz (already installed)
./packwiz.exe --version

# GitHub CLI (for release automation)
gh --version
```

---

## Technical Migration Process

### Phase 1: Audit Mod Availability

Before migrating, verify each mod exists on CurseForge:

```bash
# For each mod, check CurseForge availability
./packwiz.exe cf install <mod-name> --dry-run  # If this existed

# Manual process: Search curseforge.com/minecraft/mc-mods/<mod-name>
```

See [Mod Availability Audit](#mod-availability-audit) section for the full list.

### Phase 2: Add CurseForge Metadata to Mods

Packwiz supports dual metadata. For each mod that exists on both platforms:

**Option A: Re-add from CurseForge (replaces Modrinth metadata)**
```bash
./packwiz.exe remove <mod-name>
./packwiz.exe cf install <mod-name>
```
⚠️ This loses Modrinth metadata - not recommended for dual distribution.

**Option B: Manually add CurseForge metadata (preserves both)**

Edit each `.pw.toml` file to include both update sections:

```toml
# Example: mods/sodium.pw.toml
name = "Sodium"
filename = "sodium-fabric-0.6.13+mc1.21.1.jar"
side = "client"

[download]
url = "..."
hash-format = "sha512"
hash = "..."

[update.modrinth]
mod-id = "AANobbMI"
version = "mc1.21.1-0.6.13-fabric"

[update.curseforge]
file-id = 12345678
project-id = 394468
```

This is labor-intensive but allows both export formats to work.

**Option C: Maintain separate branches (not recommended)**
- `main` branch with Modrinth metadata
- `curseforge` branch with CurseForge metadata
- High maintenance burden, version drift risk

### Phase 3: Handle Modrinth-Exclusive Mods

For mods NOT on CurseForge, you have three options:

1. **Bundle as override** - Include JAR in `overrides/mods/` (must be on CurseForge's Approved Non-CurseForge Mods list)
2. **Find alternative** - Replace with CurseForge-available equivalent
3. **Remove from CurseForge version** - Ship reduced feature set

### Phase 4: Export and Test

```bash
# Export CurseForge format
./packwiz.exe cf export
# Creates MCC-0.9.21.zip

# Verify manifest.json has project IDs (not bundled JARs)
unzip -p MCC-0.9.21.zip manifest.json | head -50

# Test import in CurseForge app or compatible launcher
```

### Phase 5: Upload to CurseForge

1. Go to your CurseForge project
2. Upload the .zip file
3. Select Minecraft version (1.21.1)
4. Select modloader (Fabric)
5. Set release type (Release/Beta/Alpha)
6. Add changelog
7. Submit for review

---

## Mod Availability Audit

### Mods to Verify (60 total)

| Mod | Modrinth | CurseForge | Notes |
|-----|----------|------------|-------|
| adorn | ✅ | ⬜ Check | |
| appleskin | ✅ | ⬜ Check | |
| architectury-api | ✅ | ⬜ Check | |
| athena-ctm | ✅ | ⬜ Check | |
| badpackets | ✅ | ⬜ Check | |
| better-sleep | ✅ | ⬜ Check | |
| bluemap | ✅ | ⬜ Check | |
| chipped | ✅ | ⬜ Check | |
| chunky | ✅ | ⬜ Check | |
| cloth-config | ✅ | ⬜ Check | |
| connectiblechains | ✅ | ⬜ Check | |
| controlling | ✅ | ⬜ Check | |
| craterlib | ✅ | ⬜ Check | |
| distanthorizons | ✅ | ⬜ Check | |
| effortless | ✅ | ⬜ Check | |
| excessive-building | ✅ | ⬜ Check | |
| fabric-api | ✅ | ⬜ Check | Core mod, definitely on CF |
| fabric-language-kotlin | ✅ | ⬜ Check | |
| fabricord | ✅ | ⬜ Check | |
| fabric-seasons | ✅ | ⬜ Check | |
| fabric-seasons-extras | ✅ | ⬜ Check | |
| farmers-delight-refabricated | ✅ | ⬜ Check | |
| ferrite-core | ✅ | ⬜ Check | |
| flan | ✅ | ⬜ Check | |
| forge-config-api-port | ✅ | ⬜ Check | |
| handcrafted | ✅ | ⬜ Check | |
| iris | ✅ | ⬜ Check | |
| journeymap | ✅ | ⬜ Check | Definitely on CF |
| krypton | ✅ | ⬜ Check | |
| lets-do-bakery-farmcharm-compat | ✅ | ⬜ Check | |
| lets-do-farm-charm | ✅ | ⬜ Check | |
| lets-do-vinery | ✅ | ⬜ Check | |
| litematica | ✅ | ⬜ Check | |
| lithium | ✅ | ⬜ Check | |
| macaws-bridges | ✅ | ⬜ Check | Macaw's mods likely on CF |
| macaws-doors | ✅ | ⬜ Check | |
| macaws-fences-and-walls | ✅ | ⬜ Check | |
| macaws-furniture | ✅ | ⬜ Check | |
| macaws-lights-and-lamps | ✅ | ⬜ Check | |
| macaws-roofs | ✅ | ⬜ Check | |
| macaws-trapdoors | ✅ | ⬜ Check | |
| macaws-windows | ✅ | ⬜ Check | |
| malilib | ✅ | ⬜ Check | |
| modernfix | ✅ | ⬜ Check | |
| moonlight | ✅ | ⬜ Check | |
| mouse-tweaks | ✅ | ⬜ Check | |
| polymer | ✅ | ⬜ Check | |
| rei | ✅ | ⬜ Check | |
| resourceful-lib | ✅ | ⬜ Check | |
| searchables | ✅ | ⬜ Check | |
| simple-discord-rpc | ✅ | ⬜ Check | |
| simple-voice-chat | ✅ | ⬜ Check | |
| sodium | ✅ | ⬜ Check | |
| spark | ✅ | ⬜ Check | |
| storagedrawers | ✅ | ⬜ Check | |
| underlay | ✅ | ⬜ Check | |
| universal-graves | ✅ | ⬜ Check | |
| universal-sawmill | ✅ | ⬜ Check | |
| worldedit | ✅ | ⬜ Check | Definitely on CF |
| wthit | ✅ | ⬜ Check | |

### How to Complete the Audit

```bash
# Quick manual check for each mod:
# 1. Go to curseforge.com/minecraft/mc-mods
# 2. Search for mod name
# 3. Verify Fabric 1.21.1 version exists
# 4. Note the project ID for later use
```

### Expected Results

Based on common mod distribution patterns:
- **~80-90% likely on both platforms** (Sodium, Lithium, JourneyMap, Macaw's mods, etc.)
- **~5-10% potentially Modrinth-exclusive** (newer mods, developer preference)
- **~5% may have different names** (e.g., "Farmer's Delight Refabricated" vs "Farmer's Delight [Fabric]")

---

## Submission Process

### First-Time Submission

1. **Prepare project page**
   - Write compelling description
   - Add screenshots (in-game builds, mod features)
   - List key features and included mods
   - Specify requirements (Fabric, Java version)

2. **Upload modpack**
   - Upload .zip file
   - Fill in version details
   - Write changelog

3. **Review process**
   - CurseForge staff reviews for policy compliance
   - Typically 1-3 days for new projects
   - May request changes if issues found

4. **Approval**
   - Project goes live
   - Appears in search results
   - Users can download via CurseForge app

### Subsequent Updates

```bash
# 1. Update mods as needed
./packwiz.exe cf update --all  # If using CF metadata

# 2. Bump version in pack.toml
# version = "0.9.22"

# 3. Export
./packwiz.exe cf export

# 4. Upload new version to CurseForge project
# 5. Add changelog
```

---

## Ongoing Maintenance

### Dual Distribution Workflow

If maintaining both Modrinth and CurseForge:

```bash
# Adding a new mod (need to add to both)
./packwiz.exe mr install <mod> -y
# Then manually add [update.curseforge] section to .pw.toml

# Updating mods
./packwiz.exe update --all
# May need to verify CF file IDs match

# Releasing
./packwiz.exe modrinth export  # For Modrinth/GitHub
./packwiz.exe cf export        # For CurseForge
# Upload to both platforms
```

### Maintenance Burden

| Task | Modrinth Only | Dual Distribution |
|------|---------------|-------------------|
| Add new mod | 1 command | 1 command + manual CF metadata |
| Update mods | 1 command | 1 command (if metadata synced) |
| Release | Export + GitHub release | Export x2 + GitHub + CF upload |
| Version sync | Automatic | Manual verification needed |

### Potential Issues

1. **Version mismatch** - Same mod version may have different file IDs on each platform
2. **Release timing** - Mod authors may release on one platform before the other
3. **Metadata drift** - Over time, manual edits may cause inconsistencies
4. **Exclusive mods** - If you add a Modrinth-exclusive mod, CF version needs alternative

---

## Decision Framework

### When CurseForge Makes Sense

✅ **Pursue CurseForge if:**
- You want maximum public reach
- Your target audience uses CurseForge app
- You have time for ongoing dual maintenance
- The pack is mature and update frequency is low

### When Modrinth-Only Makes Sense

✅ **Stay Modrinth-only if:**
- Primary audience is a known community (Minecraft College)
- Users are comfortable with Prism Launcher / ATLauncher
- You want minimal maintenance overhead
- Rapid iteration is more important than reach

### Current Recommendation

For MCC serving the Minecraft College community:

**Modrinth + GitHub releases is sufficient** because:
- Community members can be directed to specific download methods
- Server deployment via mrpack4server works well
- Lower maintenance burden allows focus on content
- CurseForge can be added later if demand emerges

### Revisit Triggers

Consider pursuing CurseForge if:
- Multiple users request CurseForge availability
- Pack reaches stability where updates are infrequent (quarterly)
- Community grows beyond direct communication channels
- You want to contribute to broader Minecraft modding ecosystem

---

## Quick Reference

### Commands

```bash
# Current workflow (Modrinth)
./packwiz.exe mr install <mod> -y
./packwiz.exe modrinth export

# CurseForge workflow (if implemented)
./packwiz.exe cf install <mod> -y
./packwiz.exe cf export
```

### Key Links

- CurseForge Author Portal: https://authors.curseforge.com
- CurseForge Modpack Policies: https://support.curseforge.com/en/support/solutions/articles/9000197913
- Approved Non-CurseForge Mods: https://support.curseforge.com/en/support/solutions/articles/9000197912
- Packwiz CurseForge Docs: https://packwiz.infra.link/tutorials/creating/curseforge/

---

## Appendix: Migration Script (Future Reference)

If you decide to proceed, this script could help automate the audit:

```python
#!/usr/bin/env python3
"""
Audit mod availability on CurseForge.
Requires: requests library
"""

import os
import tomllib
import requests

MODS_DIR = "mods"
CF_API = "https://api.curseforge.com/v1"
# Note: CurseForge API requires an API key

def get_mod_list():
    mods = []
    for f in os.listdir(MODS_DIR):
        if f.endswith(".pw.toml"):
            with open(os.path.join(MODS_DIR, f), "rb") as file:
                data = tomllib.load(file)
                mods.append({
                    "file": f,
                    "name": data.get("name", f),
                    "modrinth_id": data.get("update", {}).get("modrinth", {}).get("mod-id")
                })
    return mods

def check_curseforge(mod_name):
    # Would need CF API key and proper search implementation
    pass

if __name__ == "__main__":
    mods = get_mod_list()
    print(f"Found {len(mods)} mods to audit")
    for mod in mods:
        print(f"  - {mod['name']}")
```

---

*Document created: December 2024*
*Last updated: v0.9.21*
