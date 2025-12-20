# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Minecraft College 1.21.1 Fabric modpack built with Packwiz. This repository contains the modpack definition files and documentation for a college CMP server.

## Commands

```bash
# Add mod from Modrinth
./packwiz.exe mr install <mod-slug> -y

# Update all mods
./packwiz.exe update --all

# Update specific mod
./packwiz.exe update <mod-name>

# Refresh index after manual changes
./packwiz.exe refresh

# Export to .mrpack for Modrinth distribution
./packwiz.exe modrinth export

# Local test server (serves pack at localhost:8080)
./packwiz.exe serve
```

## Directory Structure

```
MCServer/
├── pack.toml                    # Main pack definition (name, version, MC version, loader)
├── index.toml                   # File index with hashes
├── mods/                        # Mod metadata files (.pw.toml)
├── packwiz.exe                  # Packwiz binary
├── Minecraft College Modpack-0.9.0.mrpack  # Exported modpack for distribution
└── docs/
    ├── server-plan.md           # Mod ecosystem research (1.21.1 Fabric vs NeoForge)
    └── minecraft-college-setup-guide.md  # Bloom.host server & player setup guide
```

## Modpack Composition (41 mods)

**Performance:** Sodium, Lithium, FerriteCore, ModernFix, Krypton, Iris (shaders)

**Content:** Farmer's Delight Refabricated, Chipped (11k+ block variants), Handcrafted, Storage Drawers, full Macaw's suite (Doors, Windows, Bridges, Roofs, Fences, Trapdoors, Furniture, Lights)

**QoL:** REI (recipes), JourneyMap, Jade (tooltips), AppleSkin, Inventory Profiles Next, Mouse Tweaks, Controlling

**Multiplayer:** Simple Voice Chat, Universal Graves, Flan (claims), Better Sleep, Spark, Chunky

## Side Configuration

Sides are auto-detected from Modrinth metadata:
- **Client-only:** Sodium, Iris, Effective, Controlling, Mouse Tweaks, IPN
- **Server-only:** Flan, Universal Graves
- **Both:** Most content mods, Voice Chat, REI, JourneyMap

## Deployment

1. **Modrinth:** Upload `Minecraft College-1.0.0.mrpack` to modrinth.com
2. **Bloom.host:** Use mrpack4server or manual mod extraction
3. **Players:** Import .mrpack via Prism Launcher

See `docs/minecraft-college-setup-guide.md` for detailed deployment steps.
