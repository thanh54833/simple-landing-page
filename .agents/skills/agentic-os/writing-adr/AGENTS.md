# Guide for agents — writing-adr

File này giải thích cách sửa `writing-adr` mà không gãy gate G2+.
Mẫu theo `blader/humanizer` `AGENTS.md`.

## What this skill contains

Skill single `SKILL.md`, không build step. Chạy ở gate G2+, giữa spec đã approve và `writing-plans`.
Mặc định là "không cần ADR"; chỉ ghi ADR khi quyết định qua đủ 3 điều kiện filter.
Viết xong thì DỪNG ở `Status: accepted` — không gọi `writing-plans`, không sửa code.

## Key files

- `SKILL.md` — source of truth duy nhất: filter, template `NNNN-<slug>.md`, handoff. Mọi sửa behavior bắt đầu ở đây.
- `AGENTS.md` (file này) — rule guide cho agent sửa skill; không chứa procedure chạy gate.
- `CHANGELOG.md` — release notes, newest first. Behavior change hoặc non-obvious fix phải có 1 note.
- `../agentic-os-lock.json` — pin `writing-adr` (`sourceType: local`, `version: local-YYYY-MM-DD`).
- `.opencode/command/adr.md` — router `$ARGUMENTS` (spec path) vào skill; giữ in sync với skill, không chép procedure.
- Target runtime: `docs/superpowers/adr/NNNN-<slug>.md` + mục `## Decisions` trong spec (tạo lazy khi chạy `/adr` lần đầu).

## Rules for changes

- Giữ `SKILL.md` và `.opencode/command/adr.md` in sync. Command chỉ resolve spec + check approve + khai báo điểm DỪNG.
- **Filter:** candidate thành ADR chỉ khi cả 3 đúng: hard to reverse + surprising without context + real trade-off. Đổi filter → cập nhật Workflow §2 + `Common Mistakes` + ví dụ.
- **Template:** một ADR = một decision. `Status: proposed | accepted | superseded by NNNN | deprecated`. Đổi quyết định thì viết ADR mới + đánh `Supersedes`; ADR cũ chỉ đổi Status, không rewrite. Đổi template → cập nhật Self-check §6 (Binds/Prevents, rejected alternative).
- **Numbering:** tôn trọng scheme sẵn có trong `docs/superpowers/adr/` (location, extension, numbering, headings). Không có folder thì tạo lazy, bắt đầu `0001`, next = max + 1. Không introduce scheme thứ hai.
- **Load-bearing:** quyết định paradigm/stack/ranh giới lớn do user chọn (Coaching default, Fast với `[ASSUMPTION]`). Không bao giờ để agent tự quyết silently.
- **Version:** giữ cùng version ở `../agentic-os-lock.json` và heading đầu `CHANGELOG.md`. Đổi skill → bump lock cùng commit.
- **Compatibility:** instructions trung lập runtime (Claude Code, OpenCode, Orca là ví dụ).
- **Description:** frontmatter dùng câu đầu của trigger; chỉ nêu `Use when...`, không tóm tắt workflow.
- **Length:** mỗi từ trong `SKILL.md` bị đọc mỗi lần fire. Thêm chữ phải đáng giá.
- **History:** thêm note ngắn vào `CHANGELOG.md` cho mọi behavior change.
- **Checks:** đọc lại `SKILL.md`; verify frontmatter `name: writing-adr`; chạy tay `/adr` trên 1 spec mẫu (case cần ADR + case "No ADR needed").

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
- Local rule mới → vào `Local Overrides` đầu `SKILL.md`; `SKILL.md` local thắng `00_sdlc_docs/` khi lệch.
