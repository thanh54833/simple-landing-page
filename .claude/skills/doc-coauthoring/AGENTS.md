# Guide for agents — doc-coauthoring

File này giải thích cách sửa `doc-coauthoring` mà không làm lệch upstream.
Mẫu theo `writing-for-agents` `AGENTS.md`.

## What this skill contains

Skill workflow 3 stage (Context Gathering → Refinement & Structure → Reader Testing), không build step. Chạy khi user muốn viết doc có cấu trúc (PRD, spec, RFC, decision doc). Không dùng để sửa code.
Copy tay từ `anthropics/skills`, chỉ thêm khối `Local Overrides` ở đầu `SKILL.md`.

## Key files

- `SKILL.md` — source of truth duy nhất: `Local Overrides` (Notion hub ai-engineer) + workflow upstream. Mọi sửa behavior bắt đầu ở `Local Overrides`.
- `AGENTS.md` (file này) — rule guide cho agent sửa skill; không chứa procedure.
- `CHANGELOG.md` — release notes, newest first. Behavior change hoặc non-obvious fix phải có 1 note.
- `../agentic-os-lock.json` — pin `doc-coauthoring` (`sourceType: local`, `version: local-YYYY-MM-DD`, `repository` trỏ upstream).
- `.agents/.commands/AGENTS.md` — liệt kê skill này là vendored; chưa có command riêng.

## Rules for changes

- **Upstream:** nguồn là `anthropics/skills/skills/doc-coauthoring/SKILL.md`. Không sửa phần thân upstream; local rule mới chỉ vào `Local Overrides`. `SKILL.md` local thắng upstream khi lệch.
- **Stage 1 stop:** đọc xong phải dừng ở Context Gathering, không draft cả tài liệu. Đổi rule này → ghi `CHANGELOG.md`.
- **Freeform:** user từ chối workflow thì viết freeform; không ép 3 stage.
- **Scope edit:** user sửa một section thì chỉ sửa section đó, trừ khi họ nói viết lại hết.
- **Version:** giữ cùng version ở `../agentic-os-lock.json` và heading đầu `CHANGELOG.md`. Đổi skill → bump lock cùng commit.
- **Compatibility:** instructions trung lập runtime (Claude Code, OpenCode, Orca là ví dụ).
- **Description:** frontmatter giữ nguyên upstream; không tóm tắt thêm workflow.
- **Length:** mỗi từ trong `SKILL.md` bị đọc mỗi lần fire. Thêm chữ phải đáng giá.
- **History:** thêm note ngắn vào `CHANGELOG.md` cho mọi behavior change.
- **Checks:** đọc lại `SKILL.md`; verify frontmatter `name: doc-coauthoring`; chạy `make agents_sync` rồi `make agents_sync-check`.

## Writing style

Plain Language trong prompt, doc, validation message, progress report:

- Lead bằng main point. Common words, active voice. Câu/đoạn ngắn.
- Một term cho một item. Dùng `must` cho requirement.
- Headings, lists, tables khi giúp reader. Bỏ từ lặp/thừa.
- Tránh double negative. Giữ nguyên identifier, command, path, schema field, quotation.
- Nội dung upstream (`SKILL.md`, `reference/`) giữ tiếng Anh như gốc; `AGENTS.md` và `CHANGELOG.md` viết tiếng Việt, thuật ngữ kỹ thuật giữ tiếng Anh.

## Editing the skill

- Giữ YAML metadata valid. Coi prompt dưới metadata là product.
- Ưu tiên instruction ngắn, rõ hơn là thêm exception hay giải thích lặp.
- Local rule mới → vào `Local Overrides` đầu `SKILL.md`; local thắng upstream khi lệch, và phải có note trong `CHANGELOG.md`.
