# Changelog — update-spec

Một file duy nhất cho `skills/agentic-os/update-spec/`, newest first. Heading đầu giữ cùng version với `../agentic-os-lock.json`. Prose tiếng Việt, thuật ngữ kỹ thuật giữ tiếng Anh.

## local-2026-11-10

- Thêm `evals/evals.json` (8 test case) và `evals/triggers.json` (10 trigger, 5 negative).
- Thêm nhánh `## Design`: lệch design do `/implement` chặn được patch vào `## Design` (hunk `MODIFIED`, không cần diff `apps/`) rồi quay lại `/implement`. Trước đó skill loại mọi drift copy/layout nên `/implement` → `/update-spec` không có lối ra.

## local-2026-10-26

- Initial self-built release: unified back-sync drift + record delta, thay raw copy `openspec-update-change` (ý tưởng hunk MODIFIED/ADDED/REMOVED port từ `.templates/spec/OpenSpec`, adapt hub: patch tại chỗ `docs/physarum/specs/`, không openspec CLI).
- TDD theo `writing-skills`: RED lộ silent load-bearing decision + scope creep vào code/tests/`DESIGN.md` + rewrite pinned test (đã revert sạch); GREEN đúc guardrails + rationalization table + red flags vào skill.
- Confirm-then-write, một spec một lần; DỪNG sau patch, suggest `/verify` (T4 → `/adr` số mới).
