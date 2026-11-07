# Changelog — tasks-creator

Một file duy nhất cho `skills/agentic-os/tasks-creator/`, newest first. Heading đầu giữ cùng version với `../agentic-os-lock.json`. Prose tiếng Việt, thuật ngữ kỹ thuật giữ tiếng Anh.

## local-2026-10-12

- Initial self-built release: tạo/cập nhật tay `.tasks/01_migration/` của một group (`00_tasks.json`, `AGENTS.md`, `01_status.json`), ngoài chuỗi gate SDLC.
- Rule chính: classify BE/FE từ `.meta/00_projects.json`, numbering contiguous `api → web → qa`, wave key `SUFFIX(name)`; wording chỉ lấy từ 3 template (`reference/generation-rules.md`).
- Incremental: thêm app vào group có progress chỉ thêm wave mới, không rewrite `00_tasks.json`/`01_status.json`; `AGENTS.md` task folder luôn derived (`reference/agents-md-templates.md`).
- DỪNG sau khi ghi 3 file của group; không chạy `generate_task.py`, không sửa template.
- Thêm `AGENTS.md` rule guide + `CHANGELOG.md` theo mẫu `blader/humanizer`.
