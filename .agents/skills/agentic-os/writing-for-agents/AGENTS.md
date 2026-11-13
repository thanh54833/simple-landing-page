# Guide for agents — writing-for-agents

File này giải thích cách sửa `writing-for-agents` mà không làm lệch upstream.
Mẫu theo `writing-adr` `AGENTS.md`.

## What this skill contains

Skill reference, không build step. Dùng khi tạo/sửa skill, `AGENTS.md`, `CLAUDE.md`.
`SKILL.md` là phần universal; `SKILL-MECHANICS.md` chỉ đọc khi document đang viết là skill.
Skill này vendored từ upstream, nên sửa local phải tối thiểu và có ghi chú.

## Key files

- `SKILL.md` — source of truth: context pointers, two loads, information hierarchy, completion criteria, when to split, leading words, pruning.
- `SKILL-MECHANICS.md` — nhánh skill-specific: frontmatter, invocation choice, router skills. `SKILL.md` trỏ tới file này; giữ link hai chiều còn đúng.
- `agents/openai.yaml` — metadata runtime OpenAI; không chứa nội dung skill.
- `AGENTS.md` (file này) — rule guide cho agent sửa skill; không chứa nội dung reference.
- `CHANGELOG.md` — release notes, newest first. Behavior change hoặc non-obvious fix phải có 1 note.
- `../agentic-os-lock.json` — pin `writing-for-agents` (`sourceType: github`, `source: mattpocock/skills`, `version: vX.Y.Z`).

## Rules for changes

- **Single source of truth:** mỗi meaning nằm đúng một nơi. Universal → `SKILL.md`; skill-specific → `SKILL-MECHANICS.md`. Không chép giữa hai file.
- **Upstream:** nguồn là `mattpocock/skills`. Ưu tiên sync từ upstream hơn sửa tay; sửa local thì ghi rõ trong `CHANGELOG.md` để lần sync sau không ghi đè mất.
- **Pointers:** link `SKILL.md` ↔ `SKILL-MECHANICS.md` phải resolve. Đổi tên file → sửa mọi pointer cùng commit.
- **Dogfood:** skill này tự áp dụng chính nó — không duplication, không no-op, ưu tiên positive phrasing, leading word thay cho câu dài. Thêm câu mới phải qua test "có đổi behavior so với default không".
- **Version:** giữ cùng version ở `../agentic-os-lock.json` và heading đầu `CHANGELOG.md`. Đổi skill → bump lock cùng commit.
- **Compatibility:** instructions trung lập runtime (Claude Code, OpenCode, Orca là ví dụ).
- **Description:** frontmatter `description` là context pointer luôn nằm trong context; giữ ngắn, front-load trigger. Không tóm tắt nội dung.
- **Length:** mỗi từ trong `SKILL.md` bị đọc mỗi lần fire. Thêm chữ phải đáng giá.
- **History:** thêm note ngắn vào `CHANGELOG.md` cho mọi behavior change.
- **Checks:** đọc lại `SKILL.md` và `SKILL-MECHANICS.md`; verify frontmatter `name: writing-for-agents`; verify các link tương đối resolve; chạy `make agents_sync` rồi `make agents_sync-check`.

## Writing style

Plain Language trong prompt, doc, validation message, progress report:

- Lead bằng main point. Common words, active voice. Câu/đoạn ngắn.
- Một term cho một item. Dùng `must` cho requirement.
- Headings, lists, tables khi giúp reader. Bỏ từ lặp/thừa.
- Tránh double negative. Giữ nguyên identifier, command, path, schema field, quotation.
- `SKILL.md` và `SKILL-MECHANICS.md` giữ tiếng Anh như upstream; `AGENTS.md` và `CHANGELOG.md` viết tiếng Việt, thuật ngữ kỹ thuật giữ tiếng Anh.

## Editing the skill

- Giữ YAML metadata valid. Coi prompt dưới metadata là product.
- Ưu tiên instruction ngắn, rõ hơn là thêm exception hay giải thích lặp.
- Local rule mới → ghi vào `AGENTS.md` này hoặc `Local Overrides` đầu `SKILL.md`; local thắng upstream khi lệch, và phải có note trong `CHANGELOG.md`.
