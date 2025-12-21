# Changelog

All notable changes to MCArtsAndCrafts will be documented in this file.

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
