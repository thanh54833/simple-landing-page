# Changelog — .agents

Một file duy nhất cho toàn bộ `.agents/` (routers + skills + settings), newest first. Heading theo ngày (`## YYYY-MM-DD`). Prose tiếng Việt, thuật ngữ kỹ thuật giữ tiếng Anh.
Chi tiết gate → xem `.commands/CHANGELOG.md`; chi tiết từng skill self-built → xem `skills/agentic-os/<skill>/CHANGELOG.md`. File này chỉ ghi thay đổi cấu trúc/sync/settings ảnh hưởng toàn cây.

## 2026-10-26

- Thêm skill self-built `update-spec` (TDD theo `writing-skills`: RED 2 probes, GREEN, verify comply) + router `/update-spec`; xóa raw copy `openspec-update-change`.
- Init-deep pass: vá doc drift `update-spec` ở 4 `AGENTS.md` (root count 10→11, pack table 7→8 skills, router table + skills router row).
- Initial changelog: tổng hợp hiện trạng `.commands/` 11 routers (7 gates `intent → spec → adr → plan → implement → verify → ship` + `debug`, `impeccable`, `retro`, `update-spec`), `skills/agentic-os/` 8 skills (5 self-built: `writing-intent`, `writing-adr`, `tasks-creator`, `init-deep`, `update-spec` + 3 vendored: `doc-coauthoring`, `writing-for-agents`, `impeccable`), `skills/rea/` 4 skills, `skills/react-best-practices/` vendored.
- Quy ước: sửa duy nhất ở `.agents/` canonical, runtime copies (`.claude/`, `.opencode/`, `.pi/`) do `make agents_sync` sinh ra.
