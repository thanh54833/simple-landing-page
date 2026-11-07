# Changelog — settings

Một file duy nhất cho toàn bộ `settings/`, newest first. Heading theo ngày (`## YYYY-MM-DD`). Prose tiếng Việt, thuật ngữ kỹ thuật giữ tiếng Anh.

## 2026-10-26

- Initial changelog: tổng hợp hiện trạng 2 single source of truth (`models.json`, `mcp.json`), sync xuống runtime copies bằng `make agents_sync`.
- `models.json`: `defaultProvider: opencode-go`, `defaultModel: opencode-go/muse-spark-1.3-contributor`.
- `mcp.json`: 2 servers `websearch` (http `search.parallel.ai/mcp`) + `playwright` (`npx @playwright/mcp`, `--headless --isolated`).
