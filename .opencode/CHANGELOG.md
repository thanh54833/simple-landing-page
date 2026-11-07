# Changelog — .opencode

File tổng cho toàn bộ `.opencode/` (gate routers + agent/model config), newest first.
Heading theo ngày (`## YYYY-MM-DD`) vì runtime copy không pin version trong lock như skill.
Chi tiết router → xem `command/CHANGELOG.md` (copy từ `.agents/.commands/CHANGELOG.md`). File này chỉ ghi thay đổi cấu trúc/config ảnh hưởng toàn cây.

## 2026-10-30

- Initial changelog: tổng hợp hiện trạng `command/` 11 routers + `CHANGELOG.md` (mirror byte-identical từ `.agents/.commands/`, gồm 7 gates `intent → spec → adr → plan → implement → verify → ship` + `debug`, `impeccable`, `retro`, `update-spec`).
- `oh-my-openagent.json`: `default_model: opencode-go/muse-spark-1.3-contributor`; 11 agents + 10 categories (mirror `.omo/omo.jsonc` — đổi luôn cả hai cùng lúc).
- `package.json`: `@opencode-ai/plugin` (gitignored cùng `node_modules/`).
- Quy ước: không sửa `command/` ở đây; sửa canonical `.agents/.commands/` rồi chạy `make agents_sync`. Cách update file này: thêm bullet newest-first dưới `## YYYY-MM-DD` khi `oh-my-openagent.json` đổi model/temperature/category/agent hoặc cấu trúc `command/` đổi ngoài sync (đổi do sync thường thì không ghi — đã có ở canonical log).

## Cách update changelog

- Khi đổi `oh-my-openagent.json`: 1 bullet (agent/category nào + giá trị mới + đã mirror `.omo/omo.jsonc` chưa).
- Khi cấu trúc `command/` đổi ngoài sync: 1 bullet tóm tắt, trỏ chi tiết về `command/CHANGELOG.md`.
- Không ghi thay đổi procedure/skill — ghi ở `.agents/skills/.../CHANGELOG.md`.
