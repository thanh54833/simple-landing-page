# Guide for agents — writing-intent

File này giải thích cách sửa `writing-intent` mà không gãy gate đầu SDLC.
Mẫu theo `blader/humanizer` `AGENTS.md`.

## What this skill contains

Skill single `SKILL.md`, không build step. Capture idea/ticket/alert thành `intent.md`
proto-spec bằng lời của originator, trước mọi design. Intent dừng ở chỗ design bắt đầu —
problem, outcome, users, constraints, open questions, không bao giờ viết how-to-build.
Viết xong thì DỪNG — không gọi `brainstorming`/`writing-plans`, không endpoint/file path/estimate.

## Key files

- `SKILL.md` — source of truth duy nhất: classify source, analyst questions, template, bảng Classification T2/T3/T4. Mọi sửa behavior bắt đầu ở đây.
- `AGENTS.md` (file này) — rule guide cho agent sửa skill; không chứa procedure chạy gate.
- `CHANGELOG.md` — release notes, newest first. Behavior change hoặc non-obvious fix phải có 1 note.
- `../agentic-os-lock.json` — pin `writing-intent` (`sourceType: local`, `version: local-YYYY-MM-DD`).
- `.opencode/command/intent.md` — router `$ARGUMENTS` (idea/ticket/alert) vào skill; giữ in sync, không chép procedure.
- Target runtime: `docs/superpowers/intents/YYYY-MM-DD-<slug>-intent.md` (cùng stem date+topic với spec/plan sau này).

## Rules for changes

- Giữ `SKILL.md` và `.opencode/command/intent.md` in sync. Command chỉ resolve input + classify + khai báo điểm DỪNG.
- **Hard gate:** không design/implement trước khi `intent.md` accepted (kể cả khi user đòi spec cùng turn — viết intent trước, design là gate riêng).
- **Template:** field nào viết/không viết theo bảng Field (Problem = pain hiện tại, không phải fix; Outcome = user thấy gì, không phải build sao). Intent > 1 trang là đang thành PRD — cắt. Đổi template → cập nhật bảng Field + `Common Mistakes`.
- **Classification:** evaluate top-down, row đầu match thắng (T4 Architecture → T3 Hotfix → T2 Feature → T0/T1 Bounded). Đổi predicate/Lane → cập nhật bảng + Handoff (`/spec`/`/plan` path, T3 không spec, T0/T1 khỏi intent). Scope phình sau accept → reclassify upward, không skip gate.
- **Bounded:** flag/endpoint nhỏ/one-file fix trên flow có sẵn thì khỏi `intent.md` — design trong chat là đủ.
- **Version:** giữ cùng version ở `../agentic-os-lock.json` và heading đầu `CHANGELOG.md`. Đổi skill → bump lock cùng commit.
- **Compatibility:** instructions trung lập runtime (Claude Code, OpenCode, Orca là ví dụ).
- **Description:** frontmatter chỉ nêu trigger (`Use when...`), không tóm tắt workflow.
- **Length:** mỗi từ trong `SKILL.md` bị đọc mỗi lần fire. Thêm chữ phải đáng giá.
- **History:** thêm note ngắn vào `CHANGELOG.md` cho mọi behavior change.
- **Checks:** đọc lại `SKILL.md`; verify frontmatter `name: writing-intent`; chạy tay 1 intent mỗi loại source (idea/ticket/alert) + 1 case Bounded từ chối.

## Writing style

Plain Language trong prompt, doc, validation message, progress report:

- Lead bằng main point. Common words, active voice. Câu/đoạn ngắn.
- Một term cho một item. Dùng `must` cho requirement.
- Headings, lists, tables khi giúp reader. Bỏ từ lặp/thừa.
- Tránh double negative. Giữ nguyên identifier, command, path, schema field, quotation.
- Giữ nguyên lời originator ở Problem/Proposed outcome; assumption chưa confirm → Open questions, không nhét vào Constraints.
- Prose tiếng Việt, thuật ngữ kỹ thuật giữ tiếng Anh; labels template giữ English.

## Editing the skill

- Giữ YAML metadata valid. Coi prompt dưới metadata là product.
- Ưu tiên instruction ngắn, rõ hơn là thêm exception hay giải thích lặp.
- Local rule mới → vào `Local Overrides` đầu `SKILL.md`; `SKILL.md` local thắng ref Notion/`00_sdlc_docs/` khi lệch.
