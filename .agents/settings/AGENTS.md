# Guide for agents — settings

## OVERVIEW
Single source of truth for model + MCP servers; `make agents_sync` fans out to every runtime copy.

## WHERE TO LOOK
| Task | Location | Notes |
|------|----------|-------|
| Change default model/provider | `models.json` | `{defaultModel, defaultProvider}`; patches `model`/`default_model` downstream, keeps temperature/reasoning untouched |
| Add/remove MCP server | `mcp.json` | `{mcpServers: {<name>: {command/args/env \| url/headers}}}` in pi entry shape |
| Track settings history | `CHANGELOG.md` | newest-first per date, one file for whole dir |
| Sync logic | `scripts/sync-agents.mjs` | `MODEL_SOURCE` + `MCP_SOURCE` sections; `--check` fails on drift |

## CONVENTIONS
- `models.json`: `defaultModel` is `provider/model`; sync derives `shortModel` (after `/`) for `.pi/settings.json` and full ref for `.omo/` + `.opencode/`.
- `mcp.json`: name must match `^[A-Za-z0-9_-]+$`; each entry needs exactly one of `command` or `url`, never both.
- Env interpolation differs per runtime: pi reads `${VAR}`, opencode reads `{env:VAR}` — write `${VAR}`, the script converts.
- Pi-only entries (only `exposure`/`toolExposure`, no `command`/`url`) are skipped in the opencode `mcp` block.
- `make agents_sync` writes `.mcp/servers.json` (verbatim), `.pi/mcp.json` (verbatim), and the `mcp` block in `opencode.json` (converted, rest untouched).

## ANTI-PATTERNS
- Don't hand-edit `.mcp/servers.json`, `.pi/mcp.json`, `opencode.json` `mcp` block, `.pi/settings.json`, `.omo/`, `.opencode/oh-my-openagent.json` — regenerated silently.
- Don't put secrets in `mcp.json`; reference env vars via `${VAR}`.
- Don't set both `command` and `url` on one server, or neither (pi-only excepted).
