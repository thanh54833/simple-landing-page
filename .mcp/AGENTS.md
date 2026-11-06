# Guide for agents — MCP registry

## OVERVIEW
`.mcp/servers.json` is the only place MCP servers are declared. Every client file is generated from it.

## SERVER SHAPE
| Field | Meaning |
|-------|---------|
| `command` + `args` | stdio server |
| `url` (+ `headers`) | HTTP server |
| `env` | stdio env; values use `${VAR}` |
| `timeout`, `description`, `enabled` | passed through to the clients |
| no `command`, `url`, or `type` | pi-only override of a user-level server; skipped for opencode |

Servers today: `websearch` (HTTP, parallel.ai) and `playwright` (`npx @playwright/mcp`, `--headless --isolated`).

## WHERE TO LOOK
| Task | Location | Notes |
|------|----------|-------|
| Add/remove/change a server | `servers.json` here | then `make mcp` |
| Verify generated files | `make mcp-check` | exits 1 on drift |
| pi client config | `.pi/mcp.json` | `mcpServers` written verbatim |
| opencode client config | `opencode.json` → `mcp` block | rest of the file untouched |
| Browser QA output | `.playwright-mcp/` | console logs + aria snapshots |
| Track history | `CHANGELOG.md` | newest-first per date; update khi thêm/sửa/xóa server |

## CONVENTIONS
- `make mcp` rewrites `.pi/mcp.json` and the `opencode.json` `mcp` block from this one file, so both clients agree.
- Env syntax is translated: pi `${VAR}` → opencode `{env:VAR}`. Write the pi form in the registry.
- opencode needs an explicit `type`; the generator derives `local` from `command` and `remote` from `url`.
- One server name must match `^[A-Za-z0-9_-]+$` and carry exactly one of `command` / `url`.
- Cách update changelog: thêm bullet newest-first dưới `## YYYY-MM-DD` trong `CHANGELOG.md` khi đổi `servers.json`; chi tiết xem cuối file đó.

## ANTI-PATTERNS
- Don't hand-edit `.pi/mcp.json` or `opencode.json#mcp` — regenerated, and `make mcp-check` fails.
- Don't declare the same server in both client files.
