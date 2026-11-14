# Guide for agents — impeccable

File này giải thích cách sửa `impeccable` mà không làm lệch upstream hay gãy router.
Mẫu theo `writing-for-agents` `AGENTS.md`.

## What this skill contains

Skill thiết kế/review frontend (design, critique, audit, polish, harden, animate, adapt…) cho website, dashboard, component, form. Vendored nguyên project từ `pbakaus/impeccable`: `SKILL.md` route sang sub-command trong `reference/`, và launcher `scripts/impeccable` chạy engine `detect`/`live`. Là skill sau các router `/impeccable`, `/redesign`, `/enhance`, và sở hữu contract `## Design` mà `spec`, `plan`, `implement`, `verify` dùng.

## Key files

- `SKILL.md` — entry: `Local Overrides (factory-skills)` + routing sang `reference/<name>.md`. Mọi sửa local bắt đầu ở `Local Overrides`.
- `reference/` — một file mỗi sub-command (`audit`, `critique`, `bolder`, `layout`, `harden`, `live`…) cùng `craft*.md`, `mode-*.md`, `degraded/`. `SKILL.md` và router trỏ tới từng file; thiếu file thì nói rõ, không dựng lại từ trí nhớ.
- `scripts/` — launcher `impeccable` (và `impeccable.cmd` cho Windows), `command-metadata.json`, `live-browser-*.js`, `data/`, `VERSION` (version engine binary, không phải version skill). Lần chạy đầu tải engine binary về `~/.impeccable/bin/`; không cần Node.
- `agents/` — `openai.yaml` và các `impeccable_*.toml` (asset producer, documenter, manual edit applier); metadata subagent, không chứa nội dung skill.
- `AGENTS.md` (file này) — rule guide cho agent sửa skill; không chứa rule design.
- `CHANGELOG.md` — release notes, newest first.
- `../agentic-os-lock.json` — pin `impeccable` (`sourceType: github`, `source: pbakaus/impeccable`, `version: X.Y.Z`, `skillPath: impeccable/SKILL.md`).
- `.agents/.commands/spec.md` (cuối file: contract `## Design`), `redesign.md`, `enhance.md` — router; glue repo (contract `## Design`, resolve target) nằm ở đây vì skill vendored không sửa được.

## Rules for changes

- **Vendored:** không sửa `reference/`, `scripts/`, `agents/`. Cần đổi → sync từ upstream; chỉ `Local Overrides` trong `SKILL.md` được sửa tay, và phải có note trong `CHANGELOG.md`.
- **Path:** literal `.agents/skills/impeccable/...` trong `SKILL.md` và `reference/` đọc thành `.agents/skills/agentic-os/impeccable/...`; `<skill-base-dir>` = folder chứa `SKILL.md`.
- **Glue ở router:** logic riêng của repo (contract `## Design`, `redesign`, `enhance`) vào `.agents/.commands/`, không vào skill. Giữ ở mức skill còn thiếu.
- **Upstream:** `SKILL.md` local thắng upstream khi lệch. Sync upstream thì giữ lại khối `Local Overrides` và rà lại router khi tên sub-command đổi.
- **Version:** giữ cùng version ở `../agentic-os-lock.json` và heading đầu `CHANGELOG.md`. Sync upstream → bump lock cùng commit.
- **Compatibility:** instructions trung lập runtime (Claude Code, OpenCode, Orca là ví dụ).
- **Description:** frontmatter giữ nguyên upstream; là trigger, không tóm tắt workflow.
- **Length:** mỗi từ trong `SKILL.md` bị đọc mỗi lần fire.
- **History:** thêm note ngắn vào `CHANGELOG.md` cho mọi sync upstream hoặc đổi `Local Overrides`.
- **Checks:** đọc lại `SKILL.md`; verify frontmatter `name: impeccable`; verify các `reference/*.md` mà router nhắc còn tồn tại; chạy `make agents_sync` rồi `make agents_sync-check`.

## Writing style

Plain Language trong prompt, doc, validation message, progress report:

- Lead bằng main point. Common words, active voice. Câu/đoạn ngắn.
- Một term cho một item. Dùng `must` cho requirement.
- Headings, lists, tables khi giúp reader. Bỏ từ lặp/thừa.
- Tránh double negative. Giữ nguyên identifier, command, path, schema field, quotation.
- Nội dung upstream (`SKILL.md`, `reference/`) giữ tiếng Anh như gốc; `AGENTS.md` và `CHANGELOG.md` viết tiếng Việt, thuật ngữ kỹ thuật giữ tiếng Anh.

## Editing the skill

- Giữ YAML metadata valid. Coi prompt dưới metadata là product.
- Local rule mới → vào `Local Overrides` đầu `SKILL.md`; local thắng upstream khi lệch, và phải có note trong `CHANGELOG.md`.
