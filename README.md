# MCArtsAndCrafts v0.9.3

A curated Fabric 1.21.1 modpack for the Minecraft College CMP, built with [Packwiz](https://packwiz.infra.link/) for easy version control and distribution.

## Features

### Performance Optimizations
- **Sodium** - Modern rendering engine (significant FPS boost)
- **Lithium** - Game logic optimizations (~50% tick improvement)
- **FerriteCore** - Memory usage reduction (~45% RAM savings)
- **ModernFix** - Faster loading, dynamic resource management
- **Krypton** - Network stack optimization
- **Iris Shaders** - OptiFine shader compatibility

### Building & Decoration
- **Chipped** - 11,000+ decorative block variants with connected textures
- **Handcrafted** - 250+ furniture pieces (fantasy, steampunk, medieval styles)
- **Macaw's Suite** - Doors, Windows, Bridges, Roofs, Fences, Trapdoors, Furniture, Lights

### Content
- **Farmer's Delight Refabricated** - Cooking and farming expansion
- **Storage Drawers** - Compact item storage system

### Quality of Life
- **Roughly Enough Items (REI)** - Recipe viewer and item browser
- **JourneyMap** - Full-featured world map with browser viewing and waypoints
- **Jade** - Block/entity tooltips (what am I looking at?)
- **AppleSkin** - Food/hunger visualization
- **Mouse Tweaks** - Enhanced inventory controls
- **Controlling** - Searchable keybinds with conflict detection

### Multiplayer
- **Simple Voice Chat** - Proximity-based voice communication
- **Universal Graves** - Death item protection (server-side, vanilla client compatible)
- **Flan** - Land claiming and protection
- **Better Sleep** - Sleep voting for multiplayer nights

### Bundled Shaders
- **BSL v10.0** - High visual quality (enabled by default)
- **Complementary Reimagined r5.6.1** - Vanilla-enhanced aesthetic with "Potato" to "Ultra" presets

### Default Settings
The modpack comes pre-configured with sensible defaults:
- GUI Scale: 3x
- Render Distance: 32 (max)
- Simulation Distance: 32 (max)
- Auto-Jump: Off
- Dark Loading Screen: On
- Shaders: BSL v10.0 enabled
- JourneyMap minimap: Hidden by default (press J to open full map)

## Quick Start

### For Players

1. Download [Prism Launcher](https://prismlauncher.org/)
2. Get the latest `.mrpack` from [Releases](https://github.com/mindfulent/MCServer/releases)
3. In Prism: **Add Instance** → **Import** → Select the `.mrpack`
4. Allocate 4-6GB RAM (Edit Instance → Settings → Memory)
5. Connect to the server!

### For Development

```bash
# Clone the repository
git clone https://github.com/mindfulent/MCServer.git
cd MCServer

# Download Packwiz (Windows)
# Get from: https://github.com/packwiz/packwiz/releases
# Or via nightly: https://nightly.link/packwiz/packwiz/workflows/go/main/Windows%2064-bit.zip

# Add a mod
./packwiz.exe mr install <mod-slug> -y

# Update all mods
./packwiz.exe update --all

# Export for distribution
./packwiz.exe modrinth export
```

## Packwiz Commands

| Command | Description |
|---------|-------------|
| `packwiz mr install <slug>` | Add mod from Modrinth |
| `packwiz cf install <slug>` | Add mod from CurseForge |
| `packwiz update --all` | Update all mods to latest versions |
| `packwiz update <name>` | Update specific mod |
| `packwiz remove <name>` | Remove a mod |
| `packwiz list` | List all installed mods |
| `packwiz refresh` | Refresh index after manual changes |
| `packwiz modrinth export` | Export to `.mrpack` format |
| `packwiz serve` | Local test server at `localhost:8080` |

## Project Structure

```
MCServer/
├── pack.toml                 # Pack metadata (name, version, MC version, loader)
├── index.toml                # File index with hashes
├── options.txt               # Default game options
├── mods/                     # Mod metadata files (.pw.toml)
├── config/                   # Mod configurations
│   └── iris.properties       # Shader settings (BSL enabled)
├── shaderpacks/              # Bundled shaders
│   ├── BSL_v10.0.zip
│   └── ComplementaryReimagined_r5.6.1.zip
├── journeymap/config/6.0/    # JourneyMap config (minimap hidden)
└── docs/
    ├── server-plan.md        # Mod ecosystem research
    └── minecraft-college-setup-guide.md  # Deployment guide
```

## Server Deployment

### Option 1: mrpack4server (Recommended)

1. Upload `mrpack4server.jar` to server root
2. Create `modpack-info.json`:
   ```json
   {
     "project_id": "mcartsandcrafts",
     "version_id": "0.9.3"
   }
   ```
3. Set server jar to `mrpack4server.jar`
4. Start server - mods auto-download

### Option 2: Manual Installation

1. Export: `./packwiz.exe modrinth export`
2. Extract server-side mods from `.mrpack`
3. Upload to server `/mods` folder

See [minecraft-college-setup-guide.md](docs/minecraft-college-setup-guide.md) for detailed Bloom.host instructions.

## Mod Compatibility

### Client/Server Sides

| Side | Mods |
|------|------|
| **Client-only** | Sodium, Iris, Controlling, Mouse Tweaks |
| **Server-only** | Flan, Universal Graves |
| **Both** | Most content mods, Voice Chat, REI, JourneyMap |

### Not Available for 1.21.1
- **Create** - NeoForge only (no Fabric port)
- **Iron Chests** - Not yet updated
- **Decorative Blocks** - Stuck at 1.20.4
- **Effective** - Removed due to crash with REI (Veil/ImGui conflict)

## Requirements

- **Minecraft:** 1.21.1
- **Mod Loader:** Fabric 0.18.3+
- **Java:** 21 (required for 1.20.5+)
- **RAM:** 4GB minimum, 6GB recommended, 8GB for shaders

## Contributing

1. Fork the repository
2. Add/update mods using Packwiz commands
3. Test locally with `packwiz serve`
4. Submit a pull request

## License

This modpack configuration is open source. Individual mods retain their respective licenses.

## Links

- [Prism Launcher](https://prismlauncher.org/) - Recommended launcher
- [Packwiz Documentation](https://packwiz.infra.link/) - Modpack tooling
- [Modrinth](https://modrinth.com/) - Mod hosting platform
- [BSL Shaders](https://modrinth.com/shader/bsl-shaders) - Default shader
- [Complementary Shaders](https://modrinth.com/shader/complementary-reimagined) - Alternative shader
