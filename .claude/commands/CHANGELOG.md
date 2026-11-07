# Changelog — commands

Một file duy nhất cho toàn bộ `.agents/commands/`, newest first.
Heading theo ngày (`## YYYY-MM-DD`) vì command không pin version trong lock như skill.
Mẫu: `blader/humanizer` `CHANGELOG.md`.

## 2026-11-07

- Thêm `/redesign`: router thin tới skill `impeccable` cho target do user chỉ định (component, page, sheet, selector, route) — resolve target → files, refine trong DESIGN.md (không thêm token/hue), giữ behavior + test, build + vitest, STOP với report. Update `.commands/AGENTS.md` (row + standalone list).

## 2026-10-30

- Session default input cho `/spec`, `/adr`, `/plan`, `/implement`, `/verify`, `/update-spec`: thứ tự User Input path → artifact gate trước vừa accept/approve/tạo/sửa trong session (mới nhất thắng; dùng luôn, nêu path một dòng) → mới list và hỏi. Approval đã có trong session thì không hỏi lại "reviewed and approved?". `/implement` cũng lấy method đã chọn ở `/plan`.
- Update `.commands/AGENTS.md`: thêm 2 convention tương ứng (wording giống hệt giữa các router).

## 2026-10-26

- Thêm `/update-spec`: router thin (resolve spec trong `docs/superpowers/specs/` + check approve → invoke skill `update-spec` → STOP); scope mọi file spec, gỡ di sản `openspec list --json`.
- Update `.commands/AGENTS.md`: thêm row `update-spec` + standalone list (gate chain không đổi).
- Thêm `/debug`: router tới Superpowers `systematic-debugging` (4 phases, no fixes before Phase 1), kèm layer check vite proxy → FastAPI `:8000` cho dev stack của repo.

## 2026-10-10

- Initial changelog: tổng hợp hiện trạng 7 gates `intent → spec → adr → plan → implement → verify → ship`.
- Thêm `## TẠO COMMAND MỚI` vào `AGENTS.md` (guide: naming, frontmatter 2 field, body `$ARGUMENTS` + steps, fallback skill local, sync mirror, verify) + file `CHANGELOG.md` chung này.
