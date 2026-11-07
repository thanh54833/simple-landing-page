# Changelog — update-spec

Một file duy nhất cho `skills/agentic-os/update-spec/`, newest first. Heading đầu giữ cùng version với `../agentic-os-lock.json`. Prose tiếng Việt, thuật ngữ kỹ thuật giữ tiếng Anh.

## local-2026-10-26

- Initial self-built release: unified back-sync drift + record delta, thay raw copy `openspec-update-change` (ý tưởng hunk MODIFIED/ADDED/REMOVED port từ `.templates/spec/OpenSpec`, adapt hub: patch tại chỗ `docs/superpowers/specs/`, không openspec CLI).
- TDD theo `writing-skills`: RED lộ silent load-bearing decision + scope creep vào code/tests/`DESIGN.md` + rewrite pinned test (đã revert sạch); GREEN đúc guardrails + rationalization table + red flags vào skill.
- Confirm-then-write, một spec một lần; DỪNG sau patch, suggest `/verify` (T4 → `/adr` số mới).
