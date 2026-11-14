# Guide for agents — tasks-creator

File này giải thích cách sửa `tasks-creator` mà không làm lệch task set của các group đang chạy.
Mẫu theo `blader/humanizer` `AGENTS.md`.

## What this skill contains

Skill `SKILL.md` + `reference/task-format.md` + `templates/` + `scripts/check_task_set.py`. Không thuộc chuỗi gate
`intent → ship`; chạy tay khi cần tạo/cập nhật một task set `.tasks/NN_<name>/{00_tasks.json, AGENTS.md}`
của repo này. Cấu trúc: tasks → subtasks, không waves, không status file; kết quả ghi vào `note`.

## Key files

- `SKILL.md` — source of truth cho quy trình: Core Procedure, Running and Updating Tasks, Quick Reference, Common Mistakes.
- `reference/task-format.md` — source of truth cho schema, status, granularity, format bảng.
- `templates/` — khung cố định để mọi task set cùng chất lượng: `task-set.json`, `tasks/{feature,bugfix,chore,verify}.json`, `AGENTS.md`. Placeholder là `{{...}}` và `T0NN`.
- `scripts/check_task_set.py` — validator + `--fix` sinh `AGENTS.md`; mọi rule máy kiểm được nằm ở đây, không lặp lại thành văn bản dài.
- `evals/` — test case và trigger.
- `AGENTS.md` (file này) — rule guide cho agent sửa skill; không chứa procedure.
- `CHANGELOG.md` — release notes, newest first.
- `../agentic-os-lock.json` — pin `tasks-creator` (`sourceType: local`, `version: local-YYYY-MM-DD`).
- Chưa có command route trong `.opencode/command/` — skill gọi trực tiếp theo trigger `description`.

## Rules for changes

- **Một nguồn cho mỗi thứ:** schema/status/granularity → `reference/task-format.md`; wording task → `templates/tasks/*.json`; khung `AGENTS.md` → `templates/AGENTS.md`; rule máy kiểm được → `scripts/check_task_set.py`. `SKILL.md` chỉ trỏ tới, không chép lại.
- **Giữ nguyên tắc incremental:** `00_tasks.json` không bao giờ rewrite cả file khi đã có progress; `AGENTS.md` task folder luôn derived (qua script), an toàn overwrite. Sửa rule nào chạm 2 điều này phải nêu rõ trong `CHANGELOG.md`.
- **Đổi schema/template/script:** cập nhật đồng thời `reference/task-format.md`, `templates/`, `scripts/check_task_set.py`, `evals/`; rồi chạy validator trên mọi `.tasks/*/` hiện có và sửa cho `OK`.
- **Reference files:** thêm file `reference/` mới chỉ khi nội dung >100 dòng hoặc dùng lại ở nhiều chỗ; link từ `SKILL.md`.
- **Version:** giữ cùng version ở `../agentic-os-lock.json` và heading đầu `CHANGELOG.md`. Đổi skill → bump lock cùng commit.
- **Compatibility:** instructions trung lập runtime (Claude Code, OpenCode, Orca là ví dụ).
- **Description:** frontmatter chỉ nêu `Use when...`, không tóm tắt workflow.
- **Length:** mỗi từ trong `SKILL.md` bị đọc mỗi lần fire. Thêm chữ phải đáng giá; chi tiết dài để ở `reference/`.
- **History:** thêm note ngắn vào `CHANGELOG.md` cho mọi behavior change.
- **Checks:** `python3 scripts/check_task_set.py` trên mọi set hiện có in `OK`; grep không còn tên file đã xoá; dry-run bằng subagent: tạo task set mới từ một goal mẫu rồi validate.

## Writing style

Plain Language trong prompt, doc, validation message, progress report:

- Lead bằng main point. Common words, active voice. Câu/đoạn ngắn.
- Một term cho một item. Dùng `must` cho requirement.
- Headings, lists, tables khi giúp reader. Bỏ từ lặp/thừa.
- Tránh double negative. Giữ nguyên identifier, command, path, schema field, quotation.
- Prose tiếng Việt, thuật ngữ kỹ thuật giữ tiếng Anh; labels template giữ English.

## Editing the skill

- Giữ YAML metadata valid. Coi prompt dưới metadata là product.
- Ưu tiên instruction ngắn, rõ hơn là thêm exception hay giải thích lặp.
- Local rule mới → `Local Overrides` đầu `SKILL.md` nếu có; local thắng `00_sdlc_docs/` khi lệch.
- Không tạo copy dưới `.claude/skills/` — sửa duy nhất ở `.agents/`.
