# Changelog

All notable changes to MCArtsAndCrafts will be documented in this file.

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
