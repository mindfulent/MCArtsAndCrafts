# v1.0.7 — Discord bridge moves out of the modpack

Removed two mods. The Discord ↔ server chat bridge, join/leave/advancement announcements, and `/register <username>` whitelist all still work — they now run through the slashAI Discord bot and the theblockacademy backend instead of in-process mods.

### Removed
- **Fabricord** (4.2.1) — Discord chat bridge. Replaced by the new `@DeanBot` client inside slashAI, which parses the Pterodactyl console WebSocket and writes back over RCON.
- **AutoWhitelist** (1.3.3+1.21) — `/register` slash command. Now lives on the slashAI side and calls the backend's `/mc/whitelist` endpoint (validates the Discord ↔ MC link, then runs `whitelist add` over RCON). Auto-revoke on Discord leave is preserved via the backend's `mc_audit` table.

### Notes
- Mod count: 192 (was 194).
- No functional change for players — same commands, same announcements, just served from a different process.
