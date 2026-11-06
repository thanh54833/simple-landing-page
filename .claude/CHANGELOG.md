# Changelog — .claude

File tổng cho toàn bộ `.claude/` (mirror + plugin switch), newest first.
Heading theo ngày (`## YYYY-MM-DD`) vì runtime copy không pin version trong lock như skill.
Chi tiết router → xem `commands/CHANGELOG.md` (copy từ `.agents/.commands/CHANGELOG.md`); chi tiết từng skill → xem `skills/agentic-os/<skill>/CHANGELOG.md`. File này chỉ ghi thay đổi cấu trúc/settings/plugin ảnh hưởng toàn cây.

## 2026-10-30

- Initial changelog: tổng hợp hiện trạng `commands/` 11 routers + `CHANGELOG.md` (mirror byte-identical từ `.agents/.commands/`, gồm 7 gates `intent → spec → adr → plan → implement → verify → ship` + `debug`, `impeccable`, `retro`, `update-spec`), `skills/` mirror đầy đủ `.agents/skills` (3 packs, `react-best-practices/` included, 79 files).
- `settings.json`: `enabledPlugins: superpowers@claude-plugins-official` — `/implement`, `/verify`, `/ship` gọi skill Superpowers.
- Quy ước: không sửa gì ở đây; sửa canonical `.agents/` rồi chạy `make agents_sync`. Cách update file này: thêm bullet newest-first dưới `## YYYY-MM-DD` khi `settings.json` đổi plugin hoặc cấu trúc `commands/`/`skills/` đổi ngoài sync (đổi do sync thường thì không ghi — đã có ở canonical log).

## Cách update changelog

- Khi đổi `settings.json` (thêm/bớt plugin): thêm 1 bullet ở heading ngày hiện tại.
- Khi `make agents_sync` thêm/xóa router hoặc đổi cấu trúc `skills/`: 1 bullet tóm tắt, trỏ chi tiết về canonical log.
- Không ghi thay đổi procedure/skill — ghi ở `.agents/skills/.../CHANGELOG.md`.
