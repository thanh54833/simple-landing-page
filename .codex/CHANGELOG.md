# Changelog — .codex

File tổng cho toàn bộ `.codex/` (Codex MCP client config), newest first.
Heading theo ngày (`## YYYY-MM-DD`) vì runtime copy không pin version trong lock như skill.
File sinh ra (`config.toml`) không ghi ở đây ngoài initial — xem `make mcp-check`.

## 2026-11-07

- Initial changelog: tổng hợp hiện trạng `config.toml` 2 tables — `mcp_servers.websearch` (HTTP `https://search.parallel.ai/mcp`, `tool_timeout_sec: 120`) + `mcp_servers.playwright` (`command: npx -y @playwright/mcp@latest --headless --isolated`, `tool_timeout_sec: 120`).
- Canonical: `.agents/settings/mcp.json` (pi entry shape) → `config.toml` qua `scripts/codex-toml.mjs#renderCodexToml` (dùng chung bởi `sync-mcp.mjs` + `sync-agents.mjs`); Codex đọc `.agents/skills/` natively, không mirror skill/command ở đây.
- Quy ước: không sửa `config.toml` ở đây; sửa canonical rồi chạy `make mcp` (hoặc `make agents_sync`). Cách update file này: thêm bullet newest-first dưới `## YYYY-MM-DD` khi server đổi ngoài sync (đổi do sync thường thì không ghi — đã có ở canonical log).

## Cách update changelog

- Thêm server: 1 bullet (tên + `command`/`url` + `tool_timeout_sec` vắn tắt).
- Sửa/xóa server: 1 bullet (tên + cái gì đổi + client nào chịu ảnh hưởng).
- Không ghi nội dung sync sinh ra — `make mcp-check` là nguồn xác thực drift.
