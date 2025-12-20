# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

MCArtsAndCrafts - A Fabric 1.21.1 modpack for the Minecraft College CMP, built with Packwiz.

## Commands

```bash
# Add mod from Modrinth
./packwiz.exe mr install <mod-slug> -y

# Update all mods
./packwiz.exe update --all

# Update specific mod
./packwiz.exe update <mod-name>

# Remove a mod
./packwiz.exe remove <mod-name> -y

# Refresh index after manual changes
./packwiz.exe refresh

# Export to .mrpack for distribution
./packwiz.exe modrinth export

# Local test server (serves pack at localhost:8080)
./packwiz.exe serve
```

## Directory Structure

```
MCServer/
├── pack.toml                    # Pack definition (name, version, MC version, loader)
├── index.toml                   # File index with hashes
├── options.txt                  # Default game options (GUI scale, render distance, etc.)
├── mods/                        # Mod metadata files (.pw.toml) - 42 mods
├── config/                      # Mod configurations
│   ├── iris.properties          # BSL shader enabled by default
│   ├── xaerominimap.txt         # Minimap hidden
│   ├── xaeroworldmap.txt        # World map hidden
│   └── inventoryprofilesnext/   # IPN locked slots hidden
├── shaderpacks/                 # Bundled shaders
│   ├── BSL_v10.0.zip
│   └── ComplementaryReimagined_r5.6.1.zip
├── journeymap/                  # JourneyMap minimap hidden
├── packwiz.exe                  # Packwiz binary (gitignored)
├── MCArtsAndCrafts-0.9.0.mrpack # Exported modpack (gitignored)
└── docs/
    ├── server-plan.md           # Mod ecosystem research
    └── minecraft-college-setup-guide.md  # Bloom.host setup guide
```

## Modpack Composition (42 mods)

**Performance:** Sodium, Lithium, FerriteCore, ModernFix, Krypton, Iris

**Maps:** JourneyMap, Xaero's Minimap, Xaero's World Map

**Building:** Chipped (11k+ blocks), Handcrafted, full Macaw's suite (8 mods)

**Content:** Farmer's Delight Refabricated, Storage Drawers

**QoL:** REI, Jade, AppleSkin, IPN, Mouse Tweaks, Controlling

**Multiplayer:** Simple Voice Chat, Universal Graves, Flan, Better Sleep, Spark, Chunky

## Default Configurations

The modpack ships with these defaults configured:
- `options.txt`: GUI Scale 3x, max render/simulation distance, auto-jump off, dark loading screen
- `config/iris.properties`: BSL shader enabled
- `config/xaerominimap.txt`: Minimap hidden by default
- `config/xaeroworldmap.txt`: World map hidden by default
- `journeymap/config/`: JourneyMap minimap disabled
- `config/inventoryprofilesnext/`: Locked slot indicators hidden

## Side Configuration

Sides are auto-detected from Modrinth metadata:
- **Client-only:** Sodium, Iris, Controlling, Mouse Tweaks, IPN, Xaero's maps
- **Server-only:** Flan, Universal Graves
- **Both:** Most content mods, Voice Chat, REI, JourneyMap

## Known Issues

- **Effective mod:** Removed due to Veil/ImGui crash with REI's background caching

## Deployment

1. **GitHub Releases:** `.mrpack` attached to releases
2. **Bloom.host:** Use mrpack4server or manual mod extraction
3. **Players:** Import .mrpack via Prism Launcher

See `docs/minecraft-college-setup-guide.md` for detailed deployment steps.
