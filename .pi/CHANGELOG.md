# Changelog — .pi

File tổng cho toàn bộ `.pi/` (pi runtime: generated + manifest), newest first.
Heading theo ngày (`## YYYY-MM-DD`) vì runtime copy không pin version trong lock như skill.
`npm/` (~160 MB) + `git/` (11 MB) là install tree gitignored — không ghi ở đây.

## 2026-10-30

- Initial changelog: tổng hợp hiện trạng `mcp.json` (verbatim copy `.mcp/servers.json`: `websearch` + `playwright`) + `prompts/` 11 templates (`adr`, `debug`, `impeccable`, `implement`, `intent`, `plan`, `retro`, `ship`, `spec`, `update-spec`, `verify`, kèm generated marker) + `settings.json` (`defaultProvider: opencode-go`, `defaultModel: muse-spark-1.3-contributor`, `packages`: `npm:pi-subagents`, `npm:pi-lens`, `git:github.com/obra/superpowers@v7.0.0`, `subagents`: `defaultModel` + `agentOverrides.worker`).
- Provider `opencode-go` built-in (`OPENCODE_API_KEY` qua root `.env` + `make pi`); `pi auth check --provider opencode-go` xác thực. `settings.json#packages` do `pi install -l`/`pi remove -l` sở hữu; khối `subagents` hand-owned.
- Quy ước: không sửa `mcp.json`/`prompts/` ở đây; sửa canonical (`.mcp/servers.json` + `make mcp`, `.agents/.commands/` + `make agents_sync`). Cách update file này: thêm bullet newest-first dưới `## YYYY-MM-DD` khi `settings.json` đổi packages/model/provider (ghi lệnh `pi install -l` đã chạy + pin tag, vd `@v7.0.0`).

## Cách update changelog

- Thêm/bớt pi package: 1 bullet (tên + tag + lệnh đã chạy).
- Đổi `defaultModel`/`subagents`: 1 bullet (tên field + giá trị mới + lý do).
- Không ghi thay đổi do `make mcp`/`make agents_sync` sinh ra — đã có ở canonical log (`.mcp/CHANGELOG.md`, `.agents/CHANGELOG.md`).
