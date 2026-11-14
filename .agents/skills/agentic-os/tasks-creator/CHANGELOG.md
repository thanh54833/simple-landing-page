# Changelog — tasks-creator

Một file duy nhất cho `skills/agentic-os/tasks-creator/`, newest first. Heading đầu giữ cùng version với `../agentic-os-lock.json`. Prose tiếng Việt, thuật ngữ kỹ thuật giữ tiếng Anh.

## local-2026-11-14

- Viết lại cho repo này: task set `.tasks/NN_<name>/` gồm `00_tasks.json` (tasks → subtasks) và `AGENTS.md` derived. Bỏ waves, folder api/web/qa, `.meta/00_projects.json`, template migration và `01_status.json`.
- Thêm field `note` (mặc định rỗng) cho task và subtask; agent ghi kết quả vào đó khi done/failed/skipped.
- Thêm `templates/` (task-set, feature/bugfix/chore/verify, AGENTS.md; placeholder `{{...}}`) và `scripts/check_task_set.py` (validate + `--fix` sinh `AGENTS.md`) để mọi task set cùng chất lượng; quy trình thêm bước đọc code trước, verify task cuối bắt buộc, task có subtasks xor prompt/expect, bảng xếp theo task rồi subtasks của nó.
- Thay `reference/generation-rules.md` và `reference/agents-md-templates.md` bằng `reference/task-format.md`; viết lại `evals/`; `_template.json` chuyển thành `templates/task-set.json`.

## local-2026-10-12

- Initial self-built release (repo migration: waves, `01_status.json`); đã thay thế bởi bản local-2026-11-14.
