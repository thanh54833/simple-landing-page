# Guide for agents — tasks-creator

File này giải thích cách sửa `tasks-creator` mà không làm lệch task set của các group đang chạy.
Mẫu theo `blader/humanizer` `AGENTS.md`.

## What this skill contains

Skill `SKILL.md` + 2 file `reference/`, không build step. Không thuộc chuỗi gate `intent → ship`;
chạy tay khi cần tạo/cập nhật `02_target/<group>/.tasks/01_migration/{00_tasks.json, AGENTS.md, 01_status.json}`.
Điểm mạnh của skill: thêm app vào group đang có progress mà không đụng task đã `done`/`in_progress`.

Skill chạy trên repo migration (có `.meta/00_projects.json`, `00_migration/02_template/01_tasks/`),
không phải repo factory này. Path trong skill là path của repo đích — không remap, không chạy thử tại đây.

## Key files

- `SKILL.md` — source of truth: Core Procedure, "Adding an App Without Losing Progress", Quick Reference, Common Mistakes.
- `reference/generation-rules.md` — công thức cơ học: classify BE/FE, numbering folder, wave key, `source_dir`/`target_dir`, wave-table.
- `reference/agents-md-templates.md` — template literal cho `AGENTS.md` của task folder (central vs stub).
- `AGENTS.md` (file này) — rule guide cho agent sửa skill; không chứa procedure.
- `CHANGELOG.md` — release notes, newest first.
- `../agentic-os-lock.json` — pin `tasks-creator` (`sourceType: local`, `version: local-YYYY-MM-DD`).
- Chưa có command route trong `.opencode/command/` — skill gọi trực tiếp theo trigger `description`.

## Rules for changes

- **Một nguồn wording:** `skills`/`prompt`/`expect` chỉ đến từ 3 template của repo đích. Không chép wording vào skill này.
- **Giữ nguyên tắc incremental:** `00_tasks.json` và `01_status.json` không bao giờ rewrite cả file khi đã có progress; `AGENTS.md` task folder luôn derived, an toàn overwrite. Sửa rule nào chạm 2 điều này phải nêu rõ trong `CHANGELOG.md`.
- **SKILL ↔ reference in sync:** đổi công thức ở `generation-rules.md` → cập nhật điểm trỏ §-number trong `SKILL.md` (Core Procedure, Adding an App) và Common Mistakes nếu bị ảnh hưởng.
- **Script song song:** `.tmp/scripts/generate_task.py` (repo đích) sinh cùng output cho case from-scratch. Đổi rule ở đây → kiểm tra script có lệch không, ghi chú vào `CHANGELOG.md`.
- **Scope:** `02_target/.tasks/00_migration/*` (orchestration cấp root) nằm ngoài skill. Không mở rộng scope sang đó.
- **Reference files:** thêm file `reference/` mới chỉ khi nội dung >100 dòng hoặc dùng lại ở nhiều chỗ; link từ `SKILL.md`.
- **Version:** giữ cùng version ở `../agentic-os-lock.json` và heading đầu `CHANGELOG.md`. Đổi skill → bump lock cùng commit.
- **Compatibility:** instructions trung lập runtime (Claude Code, OpenCode, Orca là ví dụ).
- **Description:** frontmatter chỉ nêu `Use when...`, không tóm tắt workflow.
- **Length:** mỗi từ trong `SKILL.md` bị đọc mỗi lần fire. Thêm chữ phải đáng giá; công thức dài để ở `reference/`.
- **History:** thêm note ngắn vào `CHANGELOG.md` cho mọi behavior change.
- **Checks:** đọc lại `SKILL.md` + reference; verify frontmatter `name: tasks-creator`; kiểm link §-number còn đúng; dry-run tay trên 1 group mẫu (case group mới + case thêm app vào group có progress).

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
