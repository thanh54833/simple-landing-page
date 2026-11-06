# Changelog — .mcp

File tổng cho toàn bộ `.mcp/` (MCP registry), newest first.
Heading theo ngày (`## YYYY-MM-DD`) vì registry không pin version trong lock như skill.
File sinh ra (` .pi/mcp.json`, `opencode.json#mcp`) không ghi ở đây — xem `make mcp-check`.

## 2026-10-30

- Initial changelog: tổng hợp hiện trạng `servers.json` 2 servers — `websearch` (HTTP `https://search.parallel.ai/mcp`, `timeout: 120`) + `playwright` (`npx -y @playwright/mcp@latest --headless --isolated`, `timeout: 120`).
- Quy ước shape: stdio = `command` + `args` (+ `env` với `${VAR}`); HTTP = `url` (+ `headers`); mỗi server đúng 1 trong 2 `command`/`url`; entry không có cả hai là pi-only override, bị skip ở opencode.
- Cách update file này: thêm bullet newest-first dưới `## YYYY-MM-DD` khi thêm/sửa/xóa server trong `servers.json` (ghi tên server + shape đổi + lý do), rồi chạy `make mcp`.

## Cách update changelog

- Thêm server: 1 bullet (tên + `command`/`url` + `timeout`/`description` vắn tắt).
- Sửa/xóa server: 1 bullet (tên + cái gì đổi + client nào chịu ảnh hưởng).
- Không ghi nội dung client sinh ra — `make mcp-check` là nguồn xác thực drift.
