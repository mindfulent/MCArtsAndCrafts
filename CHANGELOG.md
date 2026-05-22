# Changelog

All notable changes to TBA will be documented in this file.


## [1.0.6] - 2026-05-22

### Updated
- **StreamCraft** 0.7.26 → 0.8.25 — major upgrade. The macOS/Linux native media stack was rewritten from scratch: JavaCV (FFmpeg/OpenCV/OpenBLAS) was dropped for purpose-built OS-native capture libraries, shrinking each per-platform JAR by 70–82%. Adds distance-based ("positional") screen-share audio on Display Blocks — volume fades with your distance from the screen, scaled to screen size. Wayland screen sharing now works on Linux. Also includes NeoForge view-angle culling fixes, macOS audio-sync fixes, and a refreshed "How It Works" screen. Sourced from CurseForge metadata across all four platforms (windows/linux/macos-arm64/macos-x86_64) — CurseForge approved the v0.8.25 files (project 1451729, file IDs 8124065/8124066/8124068/8124069), so this release goes straight to CF metadata with no Modrinth-override step.

### Notes
- **StreamCraft protocol version bumped 4 → 5.** Players still on TBA 1.0.5 (StreamCraft 0.7.26) will hit a StreamCraft protocol mismatch against a 1.0.6 server and lose webcam / screen-share / voice features — updating the modpack is required, not optional.
- Mod count: 194 total (unchanged from 1.0.5 — StreamCraft version swap only).


## [1.0.5] - 2026-04-26

### Fixed
- **Distant Horizons** — suppressed the "New update available!" prompt on first launch by setting `client.advanced.autoUpdater.enableAutoUpdater = false` in `config/DistantHorizons.toml`. DH is pinned to 2.4.5-b deliberately because 3.0.x breaks server-side mixins (Travelers Backpack LanguageMixin crash, see v1.0.3); players should never click "Update" — so we don't ask them.

### Updated
- **StreamCraft 0.7.26** — flipped from Modrinth URL mode back to CurseForge metadata across all four platforms (windows/linux/macos-arm64/macos-x86_64). CurseForge approved the v0.7.26 files (project 1451729, file IDs 7996534/7996556/7996538/7996545), so the platform JARs are now first-party CF dependencies in the `.zip` exports instead of bundled overrides — restoring CurseForge-First Policy compliance for the CurseForge App distribution. JAR contents are byte-identical (same SHA1s); only the source URL changes. The v1.0.5 `.zip` artifacts on CurseForge App reflect this; GitHub release `.mrpack` artifacts (Prism Launcher / server) were not rebuilt since they install correctly under either source.

### Removed
- **ShapeCraft** — removed `mods/shapecraft-0.4.18.jar`. ShapeCraft is not published to CurseForge or Modrinth, so it shipped as a raw override JAR in the CurseForge `.zip` export, which violates CurseForge-First Policy compliance for modpack submission. ShapeCraft was experimentally bundled in 1.0.0–1.0.4; with v1.0.5 it leaves the modpack until it has a public CurseForge or Modrinth listing. Players who placed ShapeCraft-generated blocks in those builds will see them turn to air on first load after this update.

### Notes
- Mod count: 194 total (-1 ShapeCraft removed vs 1.0.4).
- v1.0.4 was published with the multi-platform pipeline + StreamCraft 0.7.26 upgrade but missed the DH popup suppression. v1.0.5 supersedes it; v1.0.4 should be skipped.

## [1.0.4] - 2026-04-26

### Updated
- **StreamCraft** 0.6.2 → 0.7.26 — Adds platform-specific native bundles (LiveKit FFI / JNA / JavaCV / FFmpeg) so Mac and Linux clients now have working in-game webcam, screen share, and voice. Sourced temporarily from Modrinth (`cdn.modrinth.com`) while CurseForge approval of the v0.7.26 files is pending; will move back to CurseForge metadata once approved.

### Infrastructure
- **Multi-platform release artifacts** — every TBA release now ships 4 variants so StreamCraft's native libraries match the player's OS/CPU. Filenames: `TBA-X.Y.Z.{mrpack,zip}` (Windows, canonical), `TBA-X.Y.Z-linux.{mrpack,zip}`, `TBA-X.Y.Z-macos-arm64.{mrpack,zip}`, `TBA-X.Y.Z-macos-x86_64.{mrpack,zip}`.
- **`scripts/build-variants.py`** — new build helper that swaps `mods/streamcraft-live.pw.toml` per platform, runs `packwiz refresh && modrinth/curseforge export`, and writes named artifacts to `dist/`. Restores the original toml on exit. Supports both CurseForge metadata and Modrinth URL sources per platform via the StreamCraft file registry.
- **`.packwizignore`** — added `dist/` and `scripts/` so per-variant builds don't bundle each other or the build script.
- **`server-config.py update-pack`** now defaults to the Linux variant (the server runs on Linux and needs the Linux StreamCraft JAR). Override with `--variant <name>` if needed. Whitelisted `cdn.modrinth.com` so mrpack4server can fetch the Modrinth-sourced StreamCraft.
- **theblockacademy site** — new `/downloads` page with auto-detected platform pre-selection. Version + URL constants centralized in `src/config/downloads.ts`. `AVAILABLE_PLATFORMS` registry gates broken links per release.

### Notes
- Mod count: 195 total (unchanged from 1.0.3 — StreamCraft swap only).
- Validated end-to-end on LocalServer with the Windows variant: StreamCraft initialized cleanly, server boot in ~1.2s.


## [1.0.3] - 2026-04-19

### Reverted
- **Distant Horizons** 3.0.1-b → 2.4.5-b — DH 3.0.1-b (beta) bundles an outdated `fabric-resource-loader-v0 2.0.0` whose `server.LanguageMixin` fails `@Redirect` injection against MC 1.21.1's `Language` class. The failure surfaces on server startup when Travelers Backpack calls `Language.getString()` during `onInitialize`, which forces mixin transformation on `class_2477` and crashes the server. Client-only play didn't exercise the server-side LanguageMixin path, so the bug didn't appear during earlier testing. Reverting DH restores a stable server. Players will see DH's "New update available!" menu popup again — click "Not now" to dismiss.

### Notes
- Mod count: 195 total (unchanged from 1.0.2)

## [1.0.2] - 2026-04-19

### Added
- **ShapeCraft** 0.4.18 — Natural language block generation. Describe a custom block via `/shapecraft <description>` and ShapeCraft generates a valid block model, picks textures, and injects it as a placeable block in real time. Registers 64 pool blocks, 64 pool items, a pool block entity, and 9 network payloads. *(Note: ShapeCraft was silently bundled in the 1.0.0 and 1.0.1 exports but not documented in those changelogs. This entry formalizes it and git-tracks the jar to prevent it being dropped from a clean working-directory rebuild.)*

### Notes
- Mod count: 195 total (+1 ShapeCraft vs 0.9.100 — retroactively correct for 1.0.0 and 1.0.1, which stated 194)

## [1.0.1] - 2026-04-19

### Updated
- **Distant Horizons** 2.4.5-b → 3.0.1-b — Suppresses the "New update available!" menu prompt for fresh 1.0 installs. 3.0.0 adds MC 26 support (no impact on 1.21.1), a rendering API bump (5.1.0 → 6.0.0), progressive LOD quality loading, and framerate stability improvements; 3.0.1 fixes an underwater-grid bug. Both releases are still tagged beta. Major-version bumps for DH have historically reformatted LOD data — existing client and server DH SQLite databases may regenerate or migrate on first load.

### Notes
- Mod count: 194 total (unchanged from 1.0.0)

## [1.0.0] - 2026-04-19

**🎉 TBA 1.0 — out of beta.** After 100+ patch releases and a year-plus of curation on the Fabric 1.21.1 build, the modpack is stable, mature, and ready to drop the 0.9 prefix. No breaking changes vs 0.9.100 — this is a symbolic version bump paired with a routine StreamCraft update.

### Updated
- **StreamCraft Live** 0.5.1 → 0.6.2 — Adds Minecraft 26.1 ("Tiny Takeover") support (no impact on 1.21.1 users), fixes missing HUD overlays (LIVE indicator, viewer-name list, self-view preview) introduced in v0.6.0, and fixes held-item tooltip rendering `item.streamcraft-server.display_block` instead of "StreamCraft Block"

### Notes
- Mod count: 194 total (unchanged from 0.9.100)

## [0.9.100] - 2026-03-17

### Updated
- **StreamCraft Live** 0.3.4 → 0.5.1 — Multi-version support (MC 1.21.1 + 1.20.1), true 100% opacity on Display Blocks (no more world bleed-through), persistent Display Block settings across reconnects/chunk reloads, sticky defaults (configure one block, all future blocks inherit), auto-reconnect for bound Display Blocks when streamers rejoin, mid-session license activation, version gate enforcement, and improved activation feedback

### Notes
- Mod count: 194 total (unchanged from 0.9.99)

## [0.9.99] - 2026-03-02

### Added
- **Mighty Mail** 1.1.4 — In-game mailbox system for sending items and letters between players (+ Framework 0.13.11 library)
- **Cubes Without Borders** 3.0.0 — Borderless fullscreen windowed mode
- **Immersive Aircraft** 1.4.2 — Craftable biplanes, airships, and gyrodyne helicopters

### Updated
- **Connectible Chains** 2.5.5 → 2.5.7
- **StreamCraft Live** 0.3.3 → 0.3.4 — Fixed macOS crash when opening StreamCraft menu (Windows-only capture code now platform-gated; capture buttons greyed out on non-Windows with status message)

### Notes
- Mod count: 194 total (+4 from 0.9.98)

## [0.9.98] - 2026-02-16

### Updated
- **StreamCraft Live** 0.2.13 → 0.3.3 — Major rewrite: replaced MCEF (Chromium) with LiveKit Rust FFI via JNA. ~200MB → ~30MB download size, ~80% less RAM usage (~30MB vs ~150MB). Direct frame pipeline without JavaScript bridge. Also includes deferred LiveKit FFI initialization (zero startup overhead), webcam rendering/aspect ratio fixes, license handshake validation improvements, and redesigned trial expired screen.
- **SceneCraft Live** 0.1.27 → 0.1.29 — Block at checkbox when trial exhausted (prevents recording a full session only to discover export is unavailable on disconnect), persisted license state surviving client restarts, simplified trial exhausted screen.
- **SynthCraft Live** 0.1.15 → 0.1.17 — Fresh license validation on handshake (bypasses 24h throttle), simplified trial expired screen, redesigned upgrade messaging.
- **Core Curriculum** 0.1.23 → 0.1.24 — Splash screen progress bar now fades with the splash screen and uses vanilla's smoothed progress directly

### Notes
- Mod count: 190 total (unchanged from 0.9.97)

## [0.9.97] - 2026-02-16

### Updated
- **StreamCraft Live** 0.2.11 → 0.2.13 — Lazy-load MCEF browser: Chromium no longer spawns on game startup, deferred until player actually needs it (menu open, token received, or nearby streamer). Zero startup cost for non-users. Also fixes Display Block opacity being semi-transparent by default (now fully opaque unless explicitly lowered) and adds per-block opacity/brightness controls.
- **Core Curriculum** 0.1.22 → 0.1.23 — Added loading progress bar to custom TBA splash screen (smoothed fill animation with dark navy bar matching logo palette)

### Changed
- Unbound Iris "Disable Shaders" keybind (was F12, conflicted with SceneCraft recording)
- Added `join.theblock.academy` to the default server list — new installs start with The Block Academy pre-populated in Multiplayer

### Notes
- Mod count: 190 total (unchanged from 0.9.96)

## [0.9.96] - 2026-02-14

### Updated
- **SceneCraft Live** 0.1.16 → 0.1.27 — Major export quality improvements: eliminated camera jerk/twitch during export by removing packet lookahead and preloading all position data, fixed block pre-placement in exported video, smooth tick-boundary camera tracking (bypasses Minecraft's xo/x interpolation discontinuities), fixed chunks disappearing during export travel, fixed player skin not loading in replays, full-recording export option, client-side license recheck on disconnect, fixed frame gaps from chunk compilation, fixed mouse input corrupting rotation during export, centered license UI on review screen, fixed EXPIRED license re-validation and stale license state on clients

### Notes
- Mod count: 190 total (unchanged from 0.9.95)

## [0.9.95] - 2026-02-12

### Added
- **SceneCraft Live** 0.1.16 — Automatic cinematic highlight reels from your gameplay. Records your session in the background, detects highlights (combat, building, exploration, advancements), generates cinematic camera paths, and batch-renders MP4 clips. Press F12 to start recording, disconnect to review and export. 10 free export sessions.

### Updated
- **SynthCraft Live** 0.1.13 → 0.1.15 — Prompt templates (10 Minecraft-themed presets), duration quality warning for songs over 60s, bugfixes and security measures
- **Core Curriculum** 0.1.21 → 0.1.22 — Added SynthCraft and SceneCraft tips to welcome screen, new "Mod Shortcuts" section on commands page listing keybinds for all three mods

### Notes
- Mod count: 190 total (+1 from 0.9.94)

## [0.9.94] - 2026-02-09

### Added
- **SynthCraft Live** 0.1.13 — AI-powered music generation for Minecraft. Describe the genre, mood, and lyrics you want, and get a full original song in seconds. Listen privately or broadcast server-wide as a shared soundtrack replacing vanilla ambient music. Press `,` (comma) to open the menu.

### Notes
- Mod count: 189 total (+1 from 0.9.93)

## [0.9.93] - 2026-02-06

### Updated
- **StreamCraft Live** 0.2.9 → 0.2.11 — Fixed server deadlock: `DisplayBlockEntity.setLevel()` now uses `scheduleTick()` instead of `execute()` to safely defer streaming state reset after chunk loading (deadlocked with C2ME). Also adds desktop audio streaming for screen share (WASAPI loopback capture, toggle in menu, default ON), audio track receiving, and `setAudioVolume()` API.

### Fixed
- Suppressed Fetzi's Asian Decoration join message (bundled config override)

### Notes
- Mod count: 188 total (unchanged from 0.9.90)

## [0.9.91] - 2026-02-06

### Updated
- **StreamCraft Live** 0.2.9 → 0.2.10 — Desktop audio streaming for screen share (WASAPI loopback capture, toggle in menu, default ON), audio track receiving for subscribers, `setAudioVolume()` API for future proximity-based volume control. Fixed DisplayBlockEntity deadlock causing server freeze on chunk load.

### Notes
- Mod count: 188 total (unchanged from 0.9.90)

## [0.9.90] - 2026-02-04

### Updated
- **StreamCraft Live** 0.1.19 → 0.2.9 — Major update with unified single-JAR mod (replaces separate client/server jars):
  - Renamed "Display Block" to "StreamCraft Block" with configurable appearances (11 vanilla block disguises)
  - Dynamic stream illumination (active streams emit light level 12)
  - Fullbright webcam billboards (visible at night like name tags)
  - Horizontal offset control for screen projection
  - "Who can see me?" viewer list in HUD while streaming
  - "How It Works" info modal with privacy consent gate
  - Video quality improvements (1080p capture, 8 Mbps bitrate)
  - Fixed disconnect crash, mirrored webcam, and various stability issues

### Notes
- Mod count: 188 total (-1 from 0.9.89 — StreamCraft unified into single JAR)

## [0.9.89] - 2026-02-04

### Updated
- **StreamCraft Live** 0.1.16 → 0.1.19 — Fixed mirrored webcam billboard, fixed inverted billboard pitch, added FPS overlay toggle in Settings (hidden by default)
- **StreamCraft Live (Server)** 0.1.16 → 0.1.19 — Server-side updates matching client changes
- **Core Curriculum** 0.1.19 → 0.1.21 — Added player stats sync (reads stat files every 15min, syncs to backend, auto-allowlisting, excludes banned players)

### Fixed
- **StreamCraft server mod not deploying** — Changed `side` from "server" back to "both". mrpack4server only extracts from `overrides/`, not `server-overrides/`.
- **StreamCraft server mod CurseForge metadata** — Reinstalled server mod via CurseForge to use proper metadata instead of bare URL (prevents overrides in CF export)

### Notes
- Mod count: 189 total (unchanged)

## [0.9.88] - 2026-02-03

### Updated
- **StreamCraft Live** 0.1.15 → 0.1.16 — Added handshake diagnostics: state machine (NOT_SENT, PENDING, RECEIVED, TIMEOUT), 5-second timeout detection, detailed client/server logging. Menu now shows connection status. Fixed client version constant (was hardcoded to 0.1.0).
- **StreamCraft Live (Server)** 0.1.15 → 0.1.16 — Added detailed handshake logging (player name, UUID, versions, license state). Fixed server MOD_VERSION constant.

### Notes
- Mod count: 189 total (unchanged from 0.9.87)

## [0.9.87] - 2026-02-03

### Fixed
- **StreamCraft Live** 0.1.14 → 0.1.15 — Fixed crash when placing Display Block in hotbar. Both client and server must register Display Block for packet handling.
- **StreamCraft Live (Server)** 0.1.14 → 0.1.15 — Re-added Display Block registration for server-side packet decoding.

### Notes
- Mod count: 189 total (unchanged from 0.9.86)

## [0.9.86] - 2026-02-03

### Updated
- **StreamCraft Live** 0.1.12 → 0.1.14 — Display Block re-enabled. Block registration moved from server mod to client mod, resolving registry mismatch errors when connecting to servers. Client mod no longer depends on server mod.
- **StreamCraft Live (Server)** 0.1.10 → 0.1.14 — Server mod cleaned up; Display Block registration now handled by client.

### Notes
- Mod count: 189 total (unchanged from 0.9.85)

## [0.9.85] - 2026-02-03

### Fixed
- **StreamCraft server mod not installing** — Changed `side` from "server" to "both" so mrpack4server extracts it from `overrides/` instead of `server-overrides/` (which mrpack4server doesn't support)

### Notes
- Mod count: 189 total (unchanged from 0.9.84)

## [0.9.84] - 2026-02-03

### Fixed
- **StreamCraft Live** 0.1.11 → 0.1.12 — Fixed client crash on launch (payload types not registered with Fabric networking). Client now registers its own payload types so it works standalone.

### Notes
- Mod count: 189 total (unchanged from 0.9.83)

## [0.9.83] - 2026-02-03

### Fixed
- **StreamCraft Live** 0.1.10 → 0.1.11 — Fixed client crash on launch (`ClassNotFoundException: HandshakeC2S`). v0.1.10's optional server dependency fix was incomplete; payload classes now properly duplicated in client mod.

### Notes
- Mod count: 189 total (unchanged from 0.9.82)

## [0.9.82] - 2026-02-02

### Fixed
- Removed StreamCraft server mod from CurseForge zip overrides (flagged by CurseForge moderation as a CF-hosted project that should be in manifest). Server mod is now marked server-side only and excluded from client distribution.

### Notes
- Mod count: 189 total (unchanged from 0.9.81)

## [0.9.81] - 2026-02-02

### Added
- **StreamCraft Live** v0.1.10 — Real-time video conferencing in Minecraft (webcam, screen share, voice via LiveKit WebRTC). Client mod for players, server mod for proximity tracking and token brokering.

### Updated
- **Core Curriculum** 0.1.18 → 0.1.19:
  - Custom TBA splash screen replaces Mojang Studios branding during game loading
  - HUD now hidden during screenshot capture mode for cleaner submissions

### Notes
- Mod count: 189 total (+2 from 0.9.80)

## [0.9.80] - 2026-01-30

### Added
- **Fabric Seasons: Delight Compat** v1.0 — Adds Farmer's Delight compatibility for Fabric Seasons, suppresses the first-join nag message

### Updated
- **Core Curriculum** 0.1.17 → 0.1.18:
  - HUD auto-hides during screenshot capture mode (hotbar, crosshair removed for cleaner screenshots)
  - HUD state preserved — if already hidden via F1, stays hidden after submission
  - Welcome screen scrollbar no longer appears when content fits on screen

### Notes
- Mod count: 187 total (+1 from 0.9.79)

## [0.9.79] - 2026-01-30

### Fixed
- **LuckPerms Placeholders hook** — Replaced broken JAR (artifact was renamed upstream from `LuckPerms-Fabric-PlaceholderAPI-Hook.jar` to `LuckPerms-Fabric-Placeholders.jar`), fixing `%luckperms:prefix%` not resolving in chat
- **Core Curriculum** 0.1.16 → 0.1.17 — Title prefixes now use Simplified Text Format tags for Styled Chat compatibility

### Notes
- Mod count: 186 total (unchanged from 0.9.78)

## [0.9.78] - 2026-01-29

### Updated
- **Core Curriculum** 0.1.15 → 0.1.16 — Fixed `/link status`, `/submissions`, and other commands failing due to missing Accept header

### Notes
- Mod count: 186 total (unchanged from 0.9.77)

## [0.9.77] - 2026-01-28

### Fixed
- Switched C2ME, Sounds, and Leaf Me Alone from Modrinth to CurseForge metadata for CF export compliance
- Removed duplicate mod metadata files (c2me-fabric, leaf-me-alone)

### Notes
- Mod count: 186 total (unchanged from 0.9.76)
- CurseForge overrides reduced from 7 to 4 (VerdantVibes, ReFramed, Better Sleep, Fabricord)

## [0.9.76] - 2026-01-28

### Added
- **FallingTree** - Chop the bottom log and the whole tree falls

### Notes
- Mod count: 186 total (net +1 from 0.9.75)

## [0.9.75] - 2026-01-28

### Added — Performance
- **C2ME** - Multi-core chunk generation (Modrinth-only)
- **ImmediatelyFast** - Immediate mode rendering optimization
- **BadOptimizations** - Micro-optimizations for various game systems
- **Clumps** - Merges XP orbs to reduce entity lag
- **Enhanced Block Entities** - Faster block entity rendering (chests, signs, beds)

### Added — Building & Creative
- **Diagonal Fences** - Fences connect diagonally (completes diagonal set)
- **Easy Magic** - Enchanting table QoL (no bookshelves needed to see enchants)
- **Fast Item Frames** - Item frame rendering optimization
- **Trade Cycling** - Cycle villager trades without breaking/replacing workstation
- **Bridging Mod** - Bedrock-style reach-around block placement

### Added — Visual
- **Continuity** - Connected textures support (glass panes, bookshelves, etc.)
- **Blur+** - GUI background blur effect
- **Inventory Particles** - Item pickup particle effects
- **Smooth Swapping** - Animated item movement in inventories

### Added — Audio
- **Cool Rain** - Material-specific rain sounds (wood, stone, metal, etc.)
- **Sounds** - 170+ UI and interaction sounds (Modrinth-only)

### Added — Content
- **Do A Barrel Roll** - Enhanced elytra flight control with roll mechanics
- **Illager Invasion** - New illager types and boss encounters
- **Naturally Trimmed** - Mobs spawn wearing armor trims
- **Trimmable Tools** - Apply armor trims to tools

### Added — Quality of Life
- **Crash Assistant** - Helpful GUI after game crashes
- **Leaf Me Alone** - Ride through leaves on horses/boats (Modrinth-only)
- **Leaves Be Gone** - Quick leaf decay after tree chopping
- **Paginated Advancements** - Better advancement screen with pagination
- **Stack to Nearby Chests** - Terraria-style deposit items into nearby chests
- **Status Effect Bars** - Duration bars on status effect icons

### Changed
- **Mouse Wheelie** replaces **Mouse Tweaks** - Better inventory scrolling, sorting, and refilling

### Dependencies Added
- MidnightLib (for Blur+)
- MossyLib (for Inventory Particles)
- CICADA (for Do A Barrel Roll)
- M.R.U (for Sounds)

### Notes
- Mod count: 185 total (net +30 from 0.9.74, including 4 new library deps)
- Modrinth-only mods: C2ME, Sounds, Leaf Me Alone (bundled as overrides in CF export)

## [0.9.74] - 2026-01-28

### Added
- **Enchanted Vertical Slabs** - Place slabs vertically with enchantment support
- **VerdantVibes Unofficial Port** - Decorative plants and vegetation (Modrinth-only)

### Notes
- Mod count: 155 total (net +2 from 0.9.73)
- VerdantVibes is Modrinth-only and will be bundled as an override in CurseForge exports

## [0.9.73] - 2026-01-17

### Changed
- **Core Curriculum** v0.1.9 → v0.1.15 - New features and improvements:
  - **Welcome screen** - Multi-page onboarding for new players, auto-shows on first join, press `H` to reopen
  - **Gamemode time tracking** - Tracks time in Survival/Creative/Adventure for title progression
  - **Gamemode announcements** - Discord notifications when switching gamemodes with session time
  - **Title revoke** - OPs can now revoke titles with `/title revoke <player> <title>`
  - **Discord mentions** - Title grants now @mention recipient and granter in Discord
  - **UI polish** - Welcome screen with gradient backgrounds, progress dots, smooth animations
- **Auto HUD** - Now disabled by default (HUD stays visible). Players can re-enable dynamic hiding via Mod Menu settings.

### Notes
- Mod count: 153 total (unchanged from 0.9.72)

## [0.9.72] - 2026-01-17

### Changed
- **Core Curriculum** v0.1.3 → v0.1.9 - Major update with ownership verification and UI improvements:
  - **Ledger-based ownership verification** - Build submissions now include block ownership stats, allowing slashAI to detect if the submitter actually built what they're submitting
  - **Discord link required** - `/submit` and `/feedback` now require a linked Discord account for feedback delivery
  - **Submission management** - Delete submissions from history, improved success messaging
  - **UI polish** - Smaller thumbnails, location displayed in header, camera emoji placeholders
  - **OP commands** - `/title grant <player> <title>` for staff to grant titles directly
  - **New nomination categories** - teacher, student, builder, game-master

### Notes
- Mod count: 153 total (unchanged from 0.9.71)

## [0.9.71] - 2026-01-15

### Changed
- **Core Curriculum** v0.1.0 → v0.1.3 - Major update with new features:
  - `/submissions` - View submission history with status tracking
  - `/recognitions` - View peer nominations and title progress
  - `/nominate <player> <category> "reason"` - Recognize peers for mentoring, collaboration, or spirit
  - Session tracking for event attendance and teaching credits

### Notes
- Mod count: 153 total (unchanged from 0.9.70)

## [0.9.70] - 2026-01-15

### Changed
- **Axiom** - Skip first-time intro and tips for new installs via bundled config

### Notes
- Mod count: 153 total (unchanged from 0.9.69)

## [0.9.69] - 2026-01-14

### Added
- **Block Runner** v21.1.2 - Run faster on path blocks and other configurable surfaces

### Notes
- Mod count: 153 total (+1 from 0.9.68)

## [0.9.68] - 2026-01-14

### Changed
- **CoreCurriculum** - Renamed `/discord` command to `/link` to avoid conflicts with other mods
  - `/link` - Generate Discord linking code
  - `/link status` - Check if Discord is linked
  - `/link remove` - Unlink Discord account

## [0.9.67] - 2026-01-14

### Added - Core Curriculum Recognition System

**Recognition & Titles (3 new mods):**
- **CoreCurriculum** v0.1.0 - Recognition system for TBA with title management
  - `/titles` - Browse and activate earned titles by category
  - `/title set/clear` - Manage active displayed title
  - `/submit "Build Name"` - Submit builds for AI review
  - `/feedback "Build Name"` - Request WIP feedback
  - `/discord link` - Link Minecraft account to Discord
- **Styled Chat** v2.6.1 - Server-side chat formatting with prefix support
- **LuckPerms Placeholders** v5.4 - Enables title prefixes in chat via `%luckperms:prefix%`

### Notes
- Mod count: 152 total (+3 from 0.9.66)
- Titles appear as colored prefixes in chat (e.g., `[Apprentice Builder] PlayerName`)
- Build submissions are reviewed by slashAI with results posted to Discord

## [0.9.66] - 2026-01-11

### Added - Season 1 Content Update

**Visual & Audio (6 new mods):**
- **Visuality** v0.7.7 - Additional ambient particles (block breaking, hits, etc.)
- **3D Skin Layers** v1.10.1 - Renders skin layers with depth instead of flat
- **Particle Rain** v4.0.0 - Enhanced rain and snow particle effects
- **Presence Footsteps** v1.10.2 - Material-aware footstep sounds
- **Eating Animation** v1.9.72 - Visible eating and drinking actions
- **AutoHUD** v8.11 - Auto-hiding HUD for cleaner gameplay/recording

**Resource Packs (1):**
- **Gentler Weather Sounds** - Softer rain and thunder audio

**Building & Decoration (11 new mods):**
- **Macaw's Paintings** v1.0.5 - Additional painting variants
- **Macaw's Holidays** v1.1.2 - Seasonal decorations (Christmas, Halloween, etc.)
- **Macaw's Paths and Pavings** v1.1.1 - Path and road blocks
- **Sooty Chimneys** v1.3.2 - Chimneys with smoke particle effects
- **Diagonal Windows** v21.1.1 - Angled window placements
- **Beautify Refabricated** v1.3.0 - Decorative blocks (ropes, blinds, trellises)
- **Clutter** v0.6.5 - Small decorative objects
- **Fetzi's Asian Decoration** v1.7.2a - Asian-themed decor blocks
- **Dusty Decorations** v1.1 - Aged/weathered block variants
- **NiftyCarts** v21.1.1 - Decorative market and farm carts
- **Trinkets** v3.10.0 - Accessory slots (dependency for Let's Do mods)

**Let's Do Series (3 new mods):**
- **[Let's Do] Brewery** v2.1.5 - Brewing equipment and alcoholic drinks
- **[Let's Do] Meadow** v1.4.4 - Alpine cottage aesthetic and content
- **[Let's Do] Beach Party** v2.1.2 - Beach furniture and decorations

**Mobs & Creatures (1):**
- **Friends and Foes** v4.0.19 - Mob vote mobs (Copper Golem, Tuff Golem, Mooblooms, Glare, and more)

**Music & Instruments (1):**
- **Even More Instruments** v6.1.4 - Keyboard, violin, guitar, saxophone with MIDI support

### Changed
- **Keybind defaults** - Resolved conflicts between new mods and existing keybinds:
  - AutoHUD: Toggle HUD -> Unbound (auto-hides anyway)
  - Genshin/Even More Instruments: Transpose -> [ and ]
  - NiftyCarts: Attach/Detach -> G

### Notes
- Mod count: 149 total (+22 from 0.9.65)
- 8 mods from the original list excluded (not available for 1.21.1 or CurseForge)

## [0.9.65] - 2026-01-11

### Added
- **Essential Permissions** - Adds permission nodes to vanilla commands, enabling LuckPerms to control `/gamemode` and other vanilla commands

### Fixed
- **Gamemode switcher not working for non-OP players** - Gamemode Unrestrictor allowed the F3+F4 UI to appear, but switching failed because vanilla commands lack permission nodes. Essential Permissions bridges this gap.

### Notes
- Mod count: 127 total (+1)
- Server admins: Run `/lp group default permission set minecraft.command.gamemode true` to enable gamemode switching for all players

## [0.9.64] - 2026-01-10

### Fixed
- **Restored missing shaderpacks** - Added back Photon v1.2a and Solas Shader v3.1c
  - Root cause: These shaders existed locally but were never committed to git
  - When working directory was rebuilt during v0.9.62 rebrand, untracked files were lost
  - All 4 bundled shaders now properly tracked in git

### Included Shaderpacks
- BSL v10.0
- Complementary Reimagined r5.6.1
- Photon v1.2a
- Solas Shader v3.1c

### Notes
- Mod count: 126 total (unchanged)

## [0.9.63] - 2026-01-05

### Fixed
- **CurseForge compliance** - Switched AutoWhitelist from Modrinth to CurseForge source
  - Mods available on CurseForge must be referenced in manifest.json, not bundled
  - Thanks to CurseForge moderation team for the feedback

### Notes
- Mod count: 126 total (unchanged)

## [0.9.62] - 2026-01-05

### Changed
- **Rebrand from MCC to TBA** - Full rebrand from "Minecraft College" to "The Block Academy"
  - Updated pack name, assets, and all documentation
  - New banner and square logo images
  - Server address: `play.theblock.academy`

### Notes
- Mod count: 126 total (unchanged from 0.9.61)
- This release marks the official transition to The Block Academy branding

## [0.9.61] - 2026-01-03

### Fixed
- **Server-side mods not installing** - Fixed Advanced Backups, AutoWhitelist, Better Sleep, and Fabricord not being installed on the server. Root cause: mrpack4server doesn't support the `server-overrides` folder from mrpack format. Changed these mods from `side = "server"` to `side = "both"` so they're included in regular `overrides/` folder.

### Notes
- Mod count: 126 total (all mods now install correctly on both client and server)

## [0.9.60] - 2026-01-03

### Added
- **Accurate Block Placement Reborn** v1.3.9 - Place blocks in the direction you're facing
- **BetterF3** v11.0.3 - Enhanced F3 debug screen with customizable modules
- **Entity Culling** v1.9.5 - Performance: skip rendering off-screen entities
- **Genshin Instruments** v5.0.1 - Playable musical instruments (Lyre, Zither, etc.)
- **Ledger** v1.3.5 - Server-side block/entity logging for grief rollback (ops only)
- **VinURL** v2.2.1 - Play audio from URLs on note blocks (YouTube, SoundCloud, direct links)
- **owo-lib** v0.12.15.4 - Library dependency for VinURL

### Notes
- Mod count: 126 total (123 client, 3 server-only)

## [0.9.59] - 2026-01-03

### Removed
- **Creative Block Replacer** - Removed
- **Collective** - No longer needed (was Creative Block Replacer dependency)

### Notes
- Mod count: 119 total (116 client, 3 server-only)

## [0.9.58] - 2026-01-03

### Removed
- **Just Zoom** - Removed due to conflicts with other zoom utilities

### Changed
- **Keybinds**:
  - Camera Utils Zoom: Unbound → Z (replaces Just Zoom)
  - Toggle Cinematic Camera: Unbound → F8

### Notes
- Mod count: 121 total (118 client, 3 server-only)
- Camera keys: F5 (perspective), F6 (stable cam), F8 (cinematic), Z (zoom)

## [0.9.57] - 2026-01-03

### Changed
- **Audio Defaults** - Adjusted default sound levels for new players:
  - Weather: 100% → 50%
  - Hostile mobs: 100% → 0%
  - Friendly mobs: 100% → 0%
  - Ambient: 100% → 25%

### Notes
- Mod count: 122 total (119 client, 3 server-only)

## [0.9.56] - 2026-01-03

### Changed
- **Keybinds** - Resolved multiple keybind conflicts:
  - Create Waypoint (JourneyMap): B → K
  - JourneyMap fullscreen pan (N/S/E/W): Arrow keys → Unmapped
  - Disable Shaders (Iris): K → F12
  - Third Person Camera 1 (Camera Utils): F6 → Unmapped
  - Third Person Camera 2 (Camera Utils): F7 → Unmapped
  - Camera Utils Zoom: Z → Unmapped (duplicate of Just Zoom)
  - Toggle Firstperson (First-person Model): F6 → Unmapped
  - Open Backpack (Traveler's Backpack): Stays on B
  - Cycle Tool (Traveler's Backpack): Z → Unmapped

### Notes
- Mod count: 122 total (119 client, 3 server-only)
- Z: Just Zoom only
- F6: Stable Cam only
- F7: Disable Voice Chat only
- F11: Toggle Fullscreen (vanilla)
- F12: Disable Shaders (Iris)
- K: Create Waypoint (JourneyMap)

## [0.9.55] - 2026-01-03

### Changed
- **Keybinds** - Resolved M key conflict between minimap and Litematica:
  - Litematica main menu: M → L
  - Advancements: L → Unmapped

### Notes
- Mod count: 122 total (119 client, 3 server-only)

## [0.9.54] - 2026-01-01

### Removed
- **Universal Graves** - Removed to fix creative mode crash (DecoderException on set_creative_mode_slot packet when using Immersive Paintings items)

### Notes
- Mod count: 122 total (119 client, 3 server-only)
- Players' items now drop normally on death (vanilla behavior)

## [0.9.53] - 2026-01-01

### Fixed
- **Advanced Backups** - Fixed wrong JAR variant: was using Spigot version (non-functional on Fabric) instead of Fabric version. This may have caused item-related crashes including the Immersive Paintings hotbar crash.

### Notes
- Mod count: 123 total (120 client, 3 server-only)
- Critical fix: Backups now actually work on the server

## [0.9.52] - 2025-12-31

### Removed
- **VinURL** - Caused creative mode crash (same DecoderException as Fox Nap - known Fabric 1.21 server issue with custom item NBT serialization)
- **owo-lib** - No longer needed (was VinURL dependency)

### Notes
- Mod count: 123 total (120 client, 3 server-only)
- Photon shader remains bundled (4 shaders total)

## [0.9.51] - 2025-12-31

### Removed
- **Brewin' And Chewin'** - Removed (was Modrinth-only, causing CurseForge export issues)

### Notes
- Mod count: 125 total (122 client, 3 server-only)

## [0.9.50] - 2025-12-31

### Added
- **VinURL** v2.2.0 - Play audio from URLs on note blocks (YouTube, SoundCloud, direct links)
- **owo-lib** v0.12.15.4 - Library dependency for VinURL
- **Photon Shader** v1.2a - Gameplay-focused shader with semi-realistic style, colored lighting, detailed clouds

### Notes
- Mod count: 126 total (123 client, 3 server-only)
- Now includes 4 bundled shaders: BSL, Complementary Reimagined, Photon, Solas

## [0.9.49] - 2025-12-31

### Removed
- **Fox Nap** - Caused creative mode crash (DecoderException on set_creative_mode_slot packet when dragging items to inventory)

### Notes
- Mod count: 124 total (121 client, 3 server-only)

## [0.9.48] - 2025-12-31

### Added
- **Fox Nap** v0.2.0 - Custom music discs with a new "Maestro" villager profession (uses jukeboxes as job site). Trade tonewood and goat horns for discs.
- **Creative Block Replacer** v2.6 - Replace blocks in creative mode by clicking on them with the replacement block
- **Collective** v8.13 - Library dependency for Creative Block Replacer
- **Immersive Paintings** v0.7.4 - Upload custom images as paintings in any size

### Notes
- Mod count: 125 total (122 client, 3 server-only)

## [0.9.47] - 2025-12-31

### Added
- **Solas Shader v3.1c** - Fantasy stylized shaderpack with colored lighting (bundled in shaderpacks/)

### Notes
- Mod count: 121 total (unchanged)
- Now includes 3 bundled shaders: BSL, Complementary Reimagined, Solas

## [0.9.46] - 2025-12-31

### Added
- **AmbientSounds** v6.3.1 - Dynamic ambient soundscapes based on biome, weather, and time of day
- **Brewin' And Chewin'** v4.4.1 - Brewing addon for Farmer's Delight with kegs and alcoholic beverages (Modrinth-only: external Fabric port, not on CurseForge)
- **YetAnotherConfigLib** v3.8.1 - Config library dependency
- **playerAnimator** v2.0.4 - Animation library dependency
- **GeckoLib** v4.8.2 - Entity animation library dependency

### Removed
- **Mouse Wheelie** - Incompatible with 1.21.1 (mixin failure on RecipeBookWidget)

### Notes
- Mod count: 121 total
- Brewin' And Chewin' bundled as override in CurseForge exports (not available on CF)

## [0.9.45] - 2025-12-31

### Added
**Content & Gameplay (24 new mods, 117 total):**
- **More Delight** - Additional foods and recipes for Farmer's Delight
- **Traveler's Backpack** - Wearable backpacks with fluid storage and tool slots
- **Lootr** - Per-player loot in chests, barrels, and minecarts (no stealing!)
- **Carry On** - Pick up and carry blocks, chests, and entities
- **Sit** - Right-click stairs and slabs to sit
- **Better Climbing** - Enhanced ladder climbing mechanics
- **Actually Harvest** - Right-click crops to harvest and replant
- **Universal Bone Meal** - Bone meal works on more plants

**Building & Decoration:**
- **Diagonal Walls** - Walls connect diagonally
- **Falling Leaves** - Leaf particles fall from trees

**Audio & Immersion:**
- **Sound Physics Remastered** - Realistic reverb and sound occlusion
- **Voice Chat Interaction** - Nearby sounds play through voice chat proximity
- **Subtle Effects** - Ambient environmental particle effects

**Camera & Animation:**
- **First-person Model** - See your own body in first person
- **Not Enough Animations** - Player animations for eating, map holding, etc.
- **Camera Overhaul** - Tilting and swaying camera effects
- **Camera Utils** - Freecam, third-person distance, and camera controls

**QoL & UI:**
- **InvMove** - Move while inventory is open
- **Mod Menu** - Browse and configure mods from the title screen

**Server Administration:**
- **LuckPerms** - Advanced permissions system
- **Connectivity** - Improved connection stability and error handling

**Dependencies (auto-installed):**
- Cardinal Components API (for Traveler's Backpack)
- Fzzy Config (for Subtle Effects)
- Cupboard (for Connectivity)
- Entity Model Features + Entity Texture Features (OptiFine entity model/texture support)
- Text Placeholder API (for Mod Menu)

## [0.9.44] - 2025-12-31

### Changed
- **ReplayMod auto-recording disabled by default** - New players no longer have recording start automatically when joining. Recording can still be enabled in ReplayMod settings.

### Added
- Bundled `config/replaymod.json` with `autoStartRecording: false`

## [0.9.43] - 2025-12-28

### Fixed
- **CurseForge + ReplayMod compatibility** - Pinned versions now sourced from CurseForge
  - Moonlight Lib: 2.28.0 (CF file 7324529)
  - Supplementaries: 3.4.18 (CF file 7114488)
  - Amendments: 2.0.8 (CF file 7054320)

### Notes
- CurseForge export has only 1 override (ReFramed)
- ReplayMod playback works correctly with these pinned versions
- Best of both worlds: CF-clean submission + working cinematics

## [0.9.42] - 2025-12-28

### Fixed
- **CurseForge compatibility** - All mods now use CurseForge metadata

### Notes
- Superseded by v0.9.43 - newer CF versions broke ReplayMod playback

## [0.9.41] - 2025-12-28

### Added
- **Bundled options.txt** - Pre-resolved keybind configuration included in modpack. New players get conflict-free keybinds out of the box.

### Changed (Keybind Resolutions)
| Key | Function | Mod |
|-----|----------|-----|
| **C** | Mute Microphone | Voice Chat (moved from M) |
| **F7** | Disable Voice Chat | Voice Chat (moved from N) |
| **U** | Quiver | Supplementaries (moved from V) |
| **F4** | Toggle Replace Mode | Axiom (moved from R) |
| **F10** | Reload Shaders | Iris (moved from R) |
| **Right Alt** | Context Menu | Axiom (moved from Left Alt) |
| **Y** | Shader Selection | Iris (moved from O) |
| **]** | Undo | Effortless (moved from [) |
| **\\** | Redo | Effortless (moved from ]) |
| **'** | Minimap Preset | JourneyMap (moved from \\) |
| **.** | Chat Position | JourneyMap (moved from C) |
| **F9** | Play/Pause Replay | ReplayMod (moved from P) |

### Notes
- ReplayMod hotkeys mostly unbound (use in-game menus) to avoid conflicts during normal gameplay
- Use the Controlling mod (Options → Controls → Search) to find or remap any keybind
- Players with existing installations keep their settings; this only affects new installs

## [0.9.40] - 2025-12-28

### Fixed
- **ReplayMod compatibility** - Downgraded Supplementaries, Moonlight Lib, and Amendments to resolve "Received attachment change for unknown target" crash when playing back replays

### Changed
- **Supplementaries** 3.5.14 → 3.4.18
- **Moonlight Lib** 2.29.2 → 2.28.0
- **Amendments** 2.0.13 → 2.0.8

### Notes
- This is a compatibility fix release - no new features
- Players must update to avoid client/server mismatch errors

## [0.9.39] - 2025-12-28

### Added
- **ReplayMod** v2.6.23 - Timeline-based recording, keyframed cameras, and video export for cinematics and replays (client-side, requires FFmpeg for rendering)
- **Better Third Person** v1.9.0 - Independent camera rotation in third person, 360° orbit, 8-direction movement (client-side)
- **Stable Cam** v1.0.0 - Stable camera perspective mode for recording cinematics (client-side)

### Notes
- All 3 new mods are client-side only - players without them can still connect normally
- Mod count increased from 87 to 90

## [0.9.38] - 2025-12-28

### Fixed
- **CurseForge export** - Added CurseForge metadata to 9 mods that were incorrectly bundled as JARs in the CF export. All mods available on both platforms now properly reference CurseForge project/file IDs in manifest.json.

### Changed
- **MaLiLib** 0.21.9 → 0.21.0 - CurseForge version (masa's original, not Modrinth port)
- **Litematica** 0.19.59 → 0.19.50 - CurseForge version

### Notes
- Version downgrades were necessary because CurseForge has older versions for MaLiLib and Litematica compared to Modrinth
- The CurseForge export (`.zip`) now passes CurseForge moderation requirements
- Only ReFramed remains as an override JAR (Modrinth-only mod, not available on CurseForge)

## [0.9.37] - 2025-12-27

### Removed
- **Fairy Lights** - Removed for CurseForge compatibility (Modrinth-only mod)

### Changed
- Mod count reduced from 88 to 87

### Fixed
- CurseForge modpack export now works correctly (excluded server plugins folder, fixed Voice Chat duplication)

## [0.9.36] - 2025-12-26

### Changed
- **Replaced WorldEdit with Axiom** v5.2.1 - Modern building/editing tool with real-time previews, terraforming, sculpting, and 3D software-style controls (Right-Shift for Editor Mode)

### Notes
- Axiom requires both client and server installation for full functionality
- Free for non-commercial use (singleplayer, localhost, plot servers)

## [0.9.35] - 2025-12-25

### Fixed
- **Minescript** - Fixed Python path configuration for Windows users with standard Python installation (was pointing to Microsoft Store stub)

### Added
- Bundled Minescript config with portable Python path (`python="python"`)

## [0.9.34] - 2025-12-25

### Updated
- **Distant Horizons** 2.4.3-b → 2.4.5-b

## [0.9.33] - 2025-12-25

### Added
- **Minescript** v4.0 - Python scripting for Minecraft (run scripts from chat with `\scriptname`, requires Python 3 installed)

### Changed
- Mod count increased from 87 to 88

## [0.9.32] - 2025-12-24

### Added
- **Gamemode Unrestrictor** v1.0.2 - Allows using gamemode commands (F3+F4) even when LAN/server restricts cheats (client-side)

### Changed
- Mod count increased from 86 to 87

## [0.9.31] - 2025-12-24

### Added
- **WATERFrAMES** v2.1.22 - Display images and videos from URLs on in-game frames and projectors
- **WATERMeDIA** v2.1.37 (dependency) - Multimedia API for video/image handling
- **WATERViSION** v0.1.0-alpha (dependency) - Video player component
- **CreativeCore** v2.13.14 (dependency) - Library for creative features
- **WATERMeDIA Youtube Plugin** v2.1.1 (dependency) - Youtube support for WATERMeDIA

### Changed
- Mod count increased from 81 to 86

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
