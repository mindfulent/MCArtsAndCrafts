# Changelog

All notable changes to MCC will be documented in this file.

## [0.9.31] - 2025-12-24

### Added
- **WATERFrAMES** v2.1.22 - Display images and videos from URLs on in-game frames and projectors
- **WATERMeDIA** v3.0.0-alpha.3 (dependency) - Multimedia API for video/image handling
- **WATERViSION** v0.1.0-alpha (dependency) - Video player component
- **CreativeCore** v2.13.14 (dependency) - Library for creative features

### Changed
- Mod count increased from 81 to 85

### Notes
- Requires VLC installed on Linux/Mac for video playback

## [0.9.30] - 2025-12-24

### Added
- **WindChime Unofficial Continued** v1.3.7 - Decorative wind chimes (bamboo, glass, amethyst, copper, iron, gold, diamond, netherite, echo) placeable on ceilings or walls

### Changed
- Mod count increased from 80 to 81

## [0.9.29] - 2025-12-24

### Added
- **AutoWhitelist** v1.3.2 - Discord-based whitelist management (server-side)
- **Fabric Language Kotlin** v1.13.8 (dependency)

### Features
- Players use `/register <username>` in Discord to whitelist themselves
- Auto-removes whitelist when player leaves Discord server
- Tied to Discord membership via `@everyone` role

### Changed
- Mod count increased from 78 to 80

## [0.9.28] - 2025-12-23

### Changed
- **Project renamed** from MCArtsAndCrafts to MCC (MinecraftCollege.com)
- All documentation, scripts, and GitHub repository updated with new naming
- Release packages now named `MCC-X.Y.Z.mrpack` instead of `MCArtsAndCrafts-X.Y.Z.mrpack`

### Notes
- No mod changes in this release
- Existing player instances will continue to work
- GitHub redirects old MCArtsAndCrafts URLs to MCC automatically

## [0.9.27] - 2025-12-23

### Added
- **Amendments** v2.0.13 - Supplementaries companion mod (wall lanterns, skull candles, ceiling pots, ceiling banners, skull piles)

### Changed
- Mod count increased from 77 to 78

## [0.9.26] - 2025-12-23

### Fixed
- Server crash on startup - Reintegrated Arts & Crafts requires base Arts & Crafts mod

### Added
- **Arts & Crafts** v1.5.3 - Dyeable decorated pots, chalk, terracotta shingles, soapstone
- **JinxedLib** v1.0.4 (dependency)

### Changed
- Mod count increased from 75 to 77

## [0.9.25] - 2025-12-23

### Removed
- **Immersive Aircraft** - Caused creative mode crash (DecoderException on set_creative_mode_slot packet)

### Changed
- Mod count reduced from 76 to 75

## [0.9.24] - 2025-12-23

### Added
- **Immersive Aircraft** v1.4.1 - Flyable planes, airships, and helicopters with custom models
- **Reintegrated: Arts and Crafts** v1.0.1 - Dyeable copper blocks from 1.21 snapshot (bulk tinting with copper ingots)
- **Just Zoom** v2.1.0 - Configurable camera zoom (C key by default)
- **Camerapture** v1.10.8 - Take in-game photos and hang them as pictures
- **Supplementaries** v3.5.14 - Jars, signs, clocks, pulleys, cages, and 100+ decorative/utility items
- **Little Joys** v21.1.9 - Small ambient details (clovers, rocks, fallen leaves, butterflies)
- **Armor Statues** v21.1.0 - Pose and customize armor stands with a book interface
- **ItemSwapper** v0.8.5 - Quick item palette for swapping similar blocks (hold your key, pick variant)
- **Fairy Lights** v1.1.0 - Decorative string lights for buildings and events
- **ReFramed** v1.6.6 - Copy any block's appearance onto stairs, slabs, fences, and more

### Dependencies Added
- Lithostitched v1.5.4 (Arts and Crafts)
- Konkrete v1.9.9 (Just Zoom)
- Balm v21.0.55 (Little Joys)
- Puzzles Lib v21.1.39 (Armor Statues)

### Changed
- Mod count increased from 62 to 76

## [0.9.23] - 2025-12-23

### Added
- **Advanced Backups** v3.7.1 - Automated world backups with configurable scheduling (uptime or real-time based), incremental/differential backup support, and automatic purging policies (server-side)

### Changed
- Mod count increased from 61 to 62

## [0.9.22] - 2025-12-22

### Added
- **Joy of Painting** v1.0.1 - Paint your own pictures on canvases (1×1, 1×2, 2×1, 2×2) and hang them like vanilla paintings

### Changed
- Mod count increased from 60 to 61

## [0.9.21] - 2025-12-22

### Changed
- **Jade** replaced with **WTHIT** v12.8.3 - MIT licensed (was CC BY-NC-SA 4.0)
- Added **Bad Packets** v0.8.2 - WTHIT dependency

### Added
- **docs/LICENSES.md** - Complete license audit for all 59 mods

### Notes
- This change enables potential server monetization by removing the only non-commercial license restriction

## [0.9.20] - 2025-12-22

### Added
- **Litematica** v0.19.59 - Schematic mod for displaying build guides/holograms
- **MaLiLib** v0.21.9 - Library for Litematica
- **Effortless Structure** v3.4.0 - Mirrors, arrays, build modes, block randomizer
- **Excessive Building** v3.3.10 - 100+ vanilla-style blocks (mosaic wood, vertical stairs), hammer/wrench tools
- **[Let's Do] Vinery** v1.5.2 - Vineyard and wine themed content
- **Adorn** v6.1.2 - Furniture (chairs, sofas, tables, shelves, kitchen blocks)
- **Forge Config API Port** v21.1.6 - Dependency for Excessive Building

### Changed
- Mod count increased from 52 to 59

## [0.9.19] - 2025-12-22

### Added
- **Connectible Chains** v2.5.5 - Decorative chain links between fences and walls
- **Universal Sawmill** v1.7.2 - Sawmill workstation with Carpenter villager
- **Underlay** v0.9.9 - Place carpets/blocks under chests, beds, stairs
- **[Let's Do] Bakery** v2.1.2 - Pastries, cakes, and baking stations
- **[Let's Do] Farm & Charm** v1.1.14 - Crops and cooking (Bakery dependency)
- **Moonlight Lib** v2.28.3 - Library for Sawmill

### Added (Infrastructure)
- **`.packwizignore`** - Excludes build artifacts from .mrpack export
- **`update-pack` command** - New server-config.py command for deployment
- **`docs/DEPLOYMENT_GUIDE.md`** - Complete deployment documentation

### Fixed
- **Modpack export bloat** - .mrpack was 32MB due to including backup folders and stray jars, now ~1.5MB
- **BlueMap not loading** - Server wasn't receiving BlueMap due to mrpack4server using stale modpack-info.json

### Changed
- Mod count increased from 46 to 52
- Deployment workflow now uses GitHub releases with modpack-info.json pointing to release URLs
- Server-side mrpack4server downloads from GitHub instead of using local.mrpack uploads

### Known Issues
- **Underlay + Jade** - Server logs harmless error about client-only Jade plugin

## [0.9.18] - 2025-12-21

### Changed
- **Fabric Seasons** - Locked to Winter indefinitely (disabled real-time sync)

## [0.9.17] - 2025-12-21

### Changed
- **Pause on Lost Focus** - Disabled by default (game no longer pauses when alt-tabbing)

## [0.9.16] - 2025-12-20

### Fixed
- **BlueMap** - Downgraded to v5.6 for stability (v5.7 had issues)

## [0.9.15] - 2025-12-20

### Added
- **BlueMap** - 3D interactive web map viewable in browser (server-side, access at port 8100)

### Removed
- **JourneyMap Web Map** - Replaced by BlueMap for proper server-hosted web maps

## [0.9.14] - 2025-12-20

### Fixed
- **Server shutdown hang** - Distant Horizons now client-only (was causing SQLite connection hang on server restart)

## [0.9.13] - 2025-12-20

### Added
- **JourneyMap Web Map** - Browser-based map viewer for JourneyMap (access at localhost while in-game)

### Changed
- Mod count increased from 45 to 46

## [0.9.12] - 2025-12-20

### Added
- **Fabric Seasons** - Four seasons (Spring, Summer, Fall, Winter) with visual and gameplay changes
- **Fabric Seasons: Extras** - Additional seasonal features and integrations
- **server.properties** - Bundled server defaults (creative mode, max view distance)

### Changed
- Default gamemode set to creative
- Seasons sync with real-world calendar (Northern Hemisphere)
- View/simulation distance maxed at 32
- Mod count increased from 43 to 45

## [0.9.11] - 2025-12-20

### Added
- **WorldEdit** - In-game map editor for building and terrain manipulation (server-side)

### Changed
- Mod count increased from 42 to 43

## [0.9.10] - 2025-12-20

### Added
- **Fabricord** - Discord chat bridge for Fabric servers (replaces Discord-MC-Chat)

### Changed
- Mod count increased from 41 to 42

## [0.9.9] - 2025-12-20

### Removed
- **Discord-MC-Chat** - Incompatible with 1.21.1 (no version between 1.20.4 and 1.21.4)

### Fixed
- **Athena** - Changed from client-only to both sides (required by Chipped on server)
- Removed duplicate mod entries from partial CurseForge migration

### Changed
- Mod count reduced from 42 to 41

## [0.9.8] - 2025-12-20

### Added
- **Simple Discord RPC** - Shows Minecraft activity in Discord status (client-side)
- **CraterLib** - Dependency for Simple Discord RPC
- **Discord-MC-Chat** - Bridges server chat with Discord channel (server-side)

### Changed
- Mod count increased from 39 to 42

## [0.9.7] - 2025-12-20

### Fixed
- **Default settings restored** - Render distance, simulation distance, and dark loading screen were accidentally reset in previous versions
  - Render Distance: 32 (was 12)
  - Simulation Distance: 32 (was 12)
  - Dark Loading Screen: On (was off)

## [0.9.6] - 2025-12-20

### Added
- **Distant Horizons** - LOD rendering for extended view distances without performance loss

### Changed
- Mod count increased from 38 to 39

## [0.9.5] - 2025-12-20

### Fixed
- **JourneyMap minimaps** - Both minimap presets now properly disabled by default
- **Keybinds** - Copied all keybind settings from working game instance
- **Options** - Full options.txt with all game settings from tested instance

## [0.9.4] - 2025-12-20

### Fixed
- **Keybind conflict on M** - Disabled alternate map toggle keybinds to prevent conflicts
- Added explicit keybind settings: J for fullscreen map, disabled minimap toggles

## [0.9.3] - 2025-12-20

### Removed
- **Xaero's Minimap** - Replaced by JourneyMap (has browser-based map viewer)
- **Xaero's World Map** - Replaced by JourneyMap

### Changed
- Mod count reduced from 40 to 38
- JourneyMap is now the only map mod (minimap hidden by default, press J for full map)

## [0.9.2] - 2025-12-20

### Fixed
- **Xaero's Minimap** - Fixed config format (`minimap:false` instead of `minimapShown:false`)
- **Xaero's World Map** - Fixed config format (`displayMapOnLoad:false`)
- **JourneyMap** - Fixed config path and format for v6.0 (`journeymap/config/6.0/journeymap.minimap.config`)

Both minimaps should now be properly hidden by default on first launch.

## [0.9.1] - 2025-12-20

### Removed
- **Inventory Profiles Next (IPN)** - Not needed for creative-focused play
- **libIPN** - Dependency of IPN

### Changed
- Mod count reduced from 42 to 40

## [0.9.0] - 2025-12-20

### Added
- Initial release with 42 mods for Fabric 1.21.1

#### Performance
- Sodium, Lithium, FerriteCore, ModernFix, Krypton, Iris, Spark, Chunky

#### Building & Decoration
- Chipped, Handcrafted
- Macaw's Suite: Doors, Windows, Bridges, Roofs, Fences, Trapdoors, Furniture, Lights

#### Content
- Farmer's Delight Refabricated, Storage Drawers

#### Quality of Life
- REI, JourneyMap, Xaero's Minimap & World Map, Jade, AppleSkin
- Inventory Profiles Next, Mouse Tweaks, Controlling

#### Multiplayer
- Simple Voice Chat, Universal Graves, Flan, Better Sleep

#### Shaders
- BSL v10.0 (enabled by default)
- Complementary Reimagined r5.6.1

### Default Settings
- GUI Scale: 3x
- Render Distance: 32 (max)
- Simulation Distance: 32 (max)
- Auto-Jump: Off
- Dark Loading Screen: On
- Shaders: BSL v10.0 enabled
- Minimaps: Hidden by default

### Removed
- **Effective** - Caused crash with REI due to Veil/ImGui conflict
