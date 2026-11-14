# Guide for agents — writing-command

File này giải thích cách sửa `writing-command` mà không gãy quy ước router.
Mẫu theo `update-spec/AGENTS.md`.

## What this skill contains

Skill single `SKILL.md`, không build step. Chạy khi tạo hoặc sửa command trong `.agents/.commands/`: phân loại gate/standalone, đặt rule đúng chỗ (router vs skill), tái dùng bước đã có, kiểm cross-reference số bước, đăng ký `AGENTS.md` + `CHANGELOG.md`, sync, dry-run, converge (kiểm mâu thuẫn/mơ hồ đến khi 0 lỗi). Chưa có command riêng (như `tasks-creator`, `init-deep`).

## Key files

- `SKILL.md` — source of truth duy nhất: 9 bước Workflow + template router.
- `AGENTS.md` (file này) — rule guide cho agent sửa skill; không chứa procedure.
- `CHANGELOG.md` — release notes, newest first.
- `../agentic-os-lock.json` — pin `writing-command` (`sourceType: local`, `version: local-YYYY-MM-DD`).
- `.agents/.commands/AGENTS.md` — quy ước router mà skill này bám theo; thắng skill khi lệch.

## Rules for changes

- Skill chỉ nói về router. Procedure của skill khác thuộc `writing-for-agents`; không chép vào đây.
- Template phải khớp router thực tế trong `.agents/.commands/` (frontmatter đúng hai field, `## User Input`, bước cuối STOP). Đổi quy ước ở `.commands/AGENTS.md` → cập nhật template cùng commit.
- **Version:** giữ cùng version ở `../agentic-os-lock.json` và heading đầu `CHANGELOG.md`. Đổi skill → bump lock cùng commit.
- **Description:** frontmatter chỉ nêu trigger (`Use when...`), không tóm tắt workflow.
- **Length:** mỗi từ trong `SKILL.md` bị đọc mỗi lần fire. Cắt trước khi thêm.
- **History:** thêm note ngắn vào `CHANGELOG.md` cho mọi behavior change.
- **Checks:** đọc lại `SKILL.md`; verify frontmatter `name: writing-command`; chạy tay 1 case tạo command mới + 1 case sửa command có đổi số bước (phải tìm ra các chỗ trỏ số bước).

## Writing style

Plain Language: lead bằng main point, câu ngắn, một term cho một item, `must` cho requirement. Giữ nguyên identifier, command, path. Prose tiếng Việt, thuật ngữ kỹ thuật giữ tiếng Anh; labels template giữ English.

## Editing the skill

- Giữ YAML metadata valid. Local rule mới → `Local Overrides` đầu `SKILL.md`.
- Sửa duy nhất ở `.agents/`; `.claude/skills/` là mirror, re-sync sau mỗi thay đổi.
