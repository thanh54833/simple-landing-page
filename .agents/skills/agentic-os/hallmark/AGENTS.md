# Guide for agents — hallmark

File này giải thích cách sửa `hallmark` mà không làm lệch upstream.
Mẫu theo `writing-for-agents` `AGENTS.md`.

## What this skill contains

Design skill cho website và page mới ("look designed, not generated"): `The Floor` (rule bất khả thương lượng), direction được chia theo lượt, một idea mỗi screen. Vendored nguyên layout upstream từ `Nutlope/hallmark`, có script lint/capture/theme chạy bằng Node. Không dùng trên design đã có trừ khi user gọi tên Hallmark (`/hallmark redesign <path>`).

## Key files

- `SKILL.md` — entry: `Local Overrides (factory-skills)` + `The Floor` + routing sang `references/`. Mọi sửa local bắt đầu ở `Local Overrides`.
- `references/` — rule theo chủ đề (`gates.md`, `direction.md`, `layout.md`, `fonts.md`, `redesign.md`, `review-finish.md`…) cùng `genres/`, `macrostructures/`, `themes/`. `SKILL.md` trỏ tới từng file.
- `scripts/` — `sloplint.mjs`, `refcheck.mjs`, `capture.mjs`, `theme.mjs`, `install*.mjs`, `imagegen.mjs`, `photos.json`, `fixtures/`.
- `agents/openai.yaml` — metadata runtime OpenAI; không chứa nội dung skill.
- `LICENSE` — license upstream; giữ nguyên.
- `AGENTS.md` (file này) — rule guide cho agent sửa skill; không chứa rule design.
- `CHANGELOG.md` — release notes, newest first.
- `../agentic-os-lock.json` — pin `hallmark` (`sourceType: github`, `source: Nutlope/hallmark`, `version: X.Y.Z`).

## Rules for changes

- **Vendored:** không sửa `references/`, `scripts/`, `agents/`, `LICENSE`. Cần đổi → sync từ upstream; chỉ `Local Overrides` trong `SKILL.md` được sửa tay, và phải có note trong `CHANGELOG.md`.
- **Install path:** literal `~/.claude/skills/hallmark`, `~/.agents/skills/hallmark` trong `references/` đọc thành install path của runtime đang dùng; `<skill-dir>` = folder chứa `SKILL.md`.
- **Scope:** page mới. Cải tiến UI đã có trong repo → router `/impeccable`, `/redesign`, `/enhance` (skill `impeccable`), không gọi Hallmark trừ khi user nêu tên.
- **Upstream:** `SKILL.md` local thắng upstream khi lệch. Sync upstream thì giữ lại khối `Local Overrides`.
- **Version:** giữ cùng version ở `../agentic-os-lock.json` và heading đầu `CHANGELOG.md`. Sync upstream → bump lock cùng commit.
- **Compatibility:** instructions trung lập runtime (Claude Code, OpenCode, Orca là ví dụ).
- **Description:** frontmatter giữ nguyên upstream; là trigger, không tóm tắt workflow.
- **Length:** mỗi từ trong `SKILL.md` bị đọc mỗi lần fire.
- **History:** thêm note ngắn vào `CHANGELOG.md` cho mọi sync upstream hoặc đổi `Local Overrides`.
- **Checks:** đọc lại `SKILL.md`; verify frontmatter `name: hallmark`; verify link tới `references/` resolve; chạy `make agents_sync` rồi `make agents_sync-check`.

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
