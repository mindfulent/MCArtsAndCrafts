<p align="center">
  <img src="logo.png" alt="MCArtsAndCrafts Logo" width="400">
</p>

# MCArtsAndCrafts v0.9.27

A curated Fabric 1.21.1 modpack for the Minecraft College CMP, built with [Packwiz](https://packwiz.infra.link/) for easy version control and distribution.

## Features

### Performance Optimizations
- **Sodium** - Modern rendering engine (significant FPS boost)
- **Lithium** - Game logic optimizations (~50% tick improvement)
- **FerriteCore** - Memory usage reduction (~45% RAM savings)
- **ModernFix** - Faster loading, dynamic resource management
- **Krypton** - Network stack optimization
- **Iris Shaders** - OptiFine shader compatibility
- **Distant Horizons** - LOD rendering for extended view distances

### Building Tools
- **Litematica** - Schematic mod for displaying build guides/holograms
- **Effortless Structure** - Mirrors, arrays, build modes, block randomizer

### Building & Decoration
- **Chipped** - 11,000+ decorative block variants with connected textures
- **Handcrafted** - 250+ furniture pieces (fantasy, steampunk, medieval styles)
- **Macaw's Suite** - Doors, Windows, Bridges, Roofs, Fences, Trapdoors, Furniture, Lights
- **Excessive Building** - 100+ vanilla-style blocks (mosaic wood, vertical stairs), hammer/wrench tools
- **Adorn** - Furniture (chairs, sofas, tables, shelves, kitchen blocks)
- **Supplementaries** - Jars, signs, clocks, pulleys, cages, and 100+ decorative/utility items
- **Amendments** - Supplementaries companion (wall lanterns, skull candles, ceiling pots)
- **Connectible Chains** - Decorative chain links between fences and walls
- **Underlay** - Place carpets and blocks under chests, beds, stairs
- **Arts & Crafts** - Dyeable decorated pots, chalk, terracotta shingles, soapstone
- **ReFramed** - Copy any block's appearance onto stairs, slabs, fences, and more
- **Armor Statues** - Pose and customize armor stands with a book interface
- **Fairy Lights** - Decorative string lights for buildings and events
- **Little Joys** - Small ambient details (clovers, rocks, fallen leaves, butterflies)

### Content
- **Farmer's Delight Refabricated** - Cooking and farming expansion
- **Storage Drawers** - Compact item storage system
- **Universal Sawmill** - Sawmill workstation with Carpenter villager
- **[Let's Do] Bakery** - Pastries, cakes, and baking stations (includes Farm & Charm)
- **[Let's Do] Vinery** - Vineyard and wine themed content
- **Fabric Seasons** - Four seasons with visual and gameplay changes (currently locked to Winter)
- **Joy of Painting** - Paint custom pictures on canvases and display them like vanilla paintings
- **Camerapture** - Take in-game photos and hang them as pictures

### Web Map
- **BlueMap** - Live 3D web map of the server world (port 8100)

### Quality of Life
- **Roughly Enough Items (REI)** - Recipe viewer and item browser
- **JourneyMap** - Full-featured world map with browser viewing and waypoints
- **WTHIT** - Block/entity tooltips (what am I looking at?)
- **AppleSkin** - Food/hunger visualization
- **Mouse Tweaks** - Enhanced inventory controls
- **Controlling** - Searchable keybinds with conflict detection
- **Just Zoom** - Configurable camera zoom (C key by default)
- **ItemSwapper** - Quick item palette for swapping similar blocks

### Multiplayer
- **Simple Voice Chat** - Proximity-based voice communication
- **Universal Graves** - Death item protection (server-side, vanilla client compatible)
- **Flan** - Land claiming and protection
- **Better Sleep** - Sleep voting for multiplayer nights
- **WorldEdit** - In-game map editor for terrain and building (server-side)
- **Advanced Backups** - Automated world backups with scheduling and retention policies (server-side)

### Discord Integration
- **Simple Discord RPC** - Shows Minecraft activity in your Discord status (client-side)
- **Fabricord** - Bridges server chat with Discord channel (server-side)

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
2. Get the latest `.mrpack` from [Releases](https://github.com/mindfulent/MCArtsAndCrafts/releases)
3. In Prism: **Add Instance** → **Import** → Select the `.mrpack`
4. Allocate 4-6GB RAM (Edit Instance → Settings → Memory)
5. Connect to the server!

### Pre-Generated LOD Data (Optional)

We provide pre-generated Distant Horizons LOD data for the server. This gives you beautiful distant terrain rendering without waiting for your client to generate it.

**Download:** [DistantHorizons.sqlite](https://drive.google.com/YOUR_LINK_HERE)

Place the downloaded `DistantHorizons.sqlite` file in your Prism Launcher instance's minecraft folder:

**Windows** (Win+R, paste, replace `{username}` with your Windows username):
```
C:\Users\{username}\AppData\Roaming\PrismLauncher\instances\MCArtsAndCrafts-0.9.27\minecraft
```

**macOS** (Finder → Go → Go to Folder, replace `{username}`):
```
/Users/{username}/Library/Application Support/PrismLauncher/instances/MCArtsAndCrafts-0.9.27/minecraft
```

**Alternative:** In Prism Launcher, right-click the instance → "Folder" → drop the file there.

### For Development

```bash
# Clone the repository
git clone https://github.com/mindfulent/MCArtsAndCrafts.git
cd MCArtsAndCrafts

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
MCArtsAndCrafts/
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
    ├── CREDITS.md            # Mod creators and donation links
    ├── server-plan.md        # Mod ecosystem research
    └── minecraft-college-setup-guide.md  # Deployment guide
```

## Server Deployment

The server uses **mrpack4server** which downloads modpacks from GitHub releases. Updates are managed via `server-config.py`.

### Quick Deploy (for maintainers)

```bash
# After making changes:
./packwiz.exe modrinth export
git add -A && git commit -m "v0.9.X - description" && git push
gh release create v0.9.X MCArtsAndCrafts-0.9.X.mrpack --title "v0.9.X"
python server-config.py update-pack 0.9.X
python server-config.py restart
```

### Initial Setup

1. Upload `mrpack4server-0.5.0.jar` to server root
2. Create `modpack-info.json` pointing to GitHub release
3. Set server jar to `mrpack4server-0.5.0.jar` in Bloom.host panel
4. Start server - mods auto-download from GitHub

See [docs/DEPLOYMENT_GUIDE.md](docs/DEPLOYMENT_GUIDE.md) for complete documentation.

### Fabricord Discord Setup

After first server start, configure Discord integration:

1. **Create a Discord Bot:**
   - Go to [Discord Developer Portal](https://discord.com/developers/applications/)
   - Create a new application → Bot → Copy the token
   - Enable "Message Content Intent" under Bot settings
   - Invite bot to your server with Send Messages + Read Message History permissions

2. **Get Channel IDs:**
   - Enable Developer Mode in Discord (Settings → App Settings → Advanced)
   - Right-click your chat channel → Copy ID
   - (Optional) Right-click a console channel → Copy ID

3. **Edit server config:**
   - Location: `home/fabricord/config.yml` (in server root)
   - Set your bot token and channel IDs in the YAML config

4. **Restart the server**

## Mod Compatibility

### Client/Server Sides

| Side | Mods |
|------|------|
| **Client-only** | Sodium, Iris, Controlling, Mouse Tweaks |
| **Server-only** | Flan, Universal Graves, Fabricord, WorldEdit |
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

This modpack configuration is open source. Individual mods retain their respective licenses. See [docs/CREDITS.md](docs/CREDITS.md) for a complete list of mod creators and donation links.

## Links

- [Prism Launcher](https://prismlauncher.org/) - Recommended launcher
- [Packwiz Documentation](https://packwiz.infra.link/) - Modpack tooling
- [Modrinth](https://modrinth.com/) - Mod hosting platform
- [BSL Shaders](https://modrinth.com/shader/bsl-shaders) - Default shader
- [Complementary Shaders](https://modrinth.com/shader/complementary-reimagined) - Alternative shader
