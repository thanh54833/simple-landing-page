# Guide for agents — Codex CLI surface

## OVERVIEW
Codex MCP client config only: a single generated TOML. Codex reads `.agents/skills/` natively and has no project-level commands, so only MCP needs a copy here.

## STRUCTURE
```
.codex/
├── AGENTS.md     # this file: what lives here, what is generated
├── CHANGELOG.md  # root log: config changes, newest-first per date
└── config.toml   # `[mcp_servers.*]` tables (GENERATED)
```

## WHERE TO LOOK
| Need | Go to |
|------|-------|
| Canonical server list | `.agents/settings/mcp.json` (pi entry shape) — edit there, then `make mcp` |
| TOML rendering | `scripts/codex-toml.mjs` (`renderCodexToml`, shared by `sync-mcp.mjs` + `sync-agents.mjs`) |
| Other client copies | `.mcp/servers.json` (verbatim compat), `.pi/mcp.json` (verbatim), `opencode.json` `mcp` block (converted) |
| Canonical skill text | `.agents/skills/` — Codex reads it directly, no mirror needed |
| Verify in sync | `make mcp-check` — exits 1 on drift (`make agents_sync` syncs the same MCP targets) |
| Track history | `CHANGELOG.md` | newest-first per date; update khi `config.toml` đổi ngoài sync (sync thường không ghi) |

## CONVENTIONS
- `config.toml` tables are `[mcp_servers.<name>]`: stdio = `command` + `args`, HTTP = `url`; `tool_timeout_sec` from `timeout`, `enabled = false` only when disabled.
- Env translation: literal `${VAR}` values stay in `env`/`http_headers`; whole-value `${VAR}` becomes `env_vars` (stdio) or `env_http_headers` (HTTP); `Authorization: Bearer ${VAR}` becomes `bearer_token_env_var`.
- Pi-only entries (no `command`/`url`, only pi switches) are skipped — they cannot be expressed in Codex, same as opencode.
- Servers today: `websearch` (HTTP, parallel.ai) and `playwright` (`npx @playwright/mcp`, `--headless --isolated`).
- The file header names `sync-agents.mjs`; both sync scripts render identical output via `renderCodexToml` — run either `make mcp` or `make agents_sync`.
- Cách update changelog: thêm bullet newest-first dưới `## YYYY-MM-DD` trong `CHANGELOG.md` khi server đổi ngoài sync; chi tiết xem cuối file đó.

## ANTI-PATTERNS
- Don't hand-edit `config.toml` — regenerated, and `make mcp-check` fails.
- Don't add a Codex-only server here; declare it in `.agents/settings/mcp.json` so all clients agree.
- Don't mirror skills or commands into `.codex/` — Codex needs neither.
