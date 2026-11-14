# Guide for agents — humanizer

File này giải thích cách dùng và sửa `humanizer` mà không làm lệch upstream.
Mẫu theo `hallmark` `AGENTS.md`.

## What this skill contains

Skill viết lại văn bản nghe như AI để đọc như người viết, giữ nguyên nội dung. Gồm 26 pattern chia sáu nhóm (A–F): staging, rhythm by rule, inflation, formatting by rule, leftovers, wrong reader. Pattern §1–§5 đủ để sửa ngay khi gặp một lần; pattern ghi `weak alone` cần thêm tell khác trong cùng đoạn. Có ba chế độ trả kết quả: pasted text, file mode, embedded mode. Nguồn pattern: Wikipedia "Signs of AI writing". Single `SKILL.md`, không build step.

Skill này **đã fetch từ upstream** (`blader/humanizer`, `version: 4.0.0` trong frontmatter), không phải self-built.

## Key files

- `SKILL.md` — entry duy nhất: quy trình (mark, draft, check, final), 26 pattern kèm ví dụ before/after, mục `When not to act`. Nội dung upstream, giữ tiếng Anh.
- `AGENTS.md` (file này) — rule guide cho agent sửa skill; không chứa rule viết lại văn bản.
- `CHANGELOG.md` — release notes, newest first.
- `../agentic-os-lock.json` — chưa có mục `humanizer`. Thêm khi chốt nguồn (`sourceType: github`, `source: blader/humanizer`, `version: 4.0.0`).

## Rules for changes

- **Fetched:** không sửa nội dung `SKILL.md` sau khi fetch về: không viết lại câu cho dễ đọc, không đổi pattern, ví dụ hay watch list. Cần cập nhật → sync lại từ upstream.
- **Local rule:** nếu cần thêm hướng dẫn riêng cho repo, thêm khối `Local Overrides (factory-skills)` ở đầu `SKILL.md` (sau frontmatter), giống `impeccable` và `hallmark`. Local thắng upstream khi lệch, và phải có note trong `CHANGELOG.md`.
- **Sync upstream:** giữ lại khối `Local Overrides`; bump `version` trong lock và heading đầu `CHANGELOG.md` cùng commit.
- **Description:** frontmatter giữ nguyên upstream; là trigger, không tóm tắt workflow.
- **File mode:** chỉ đổi prose; giữ code block, inline code, command, path, YAML metadata, data, link target. Áp dụng cả khi dùng skill lên tài liệu của repo (`.docs/`, `.physarum/docs/`).
- **Voice:** có mẫu viết của user thì mẫu thắng các pattern, kể cả luật dash §8. Prose tiếng Việt của repo: giữ thuật ngữ kỹ thuật tiếng Anh, không "dịch" pattern English máy móc sang tiếng Việt.
- **Compatibility:** instructions trung lập runtime (Claude Code, OpenCode, Pi, Codex là ví dụ).
- **Length:** mỗi từ trong `SKILL.md` bị đọc mỗi lần fire.
- **History:** thêm note ngắn vào `CHANGELOG.md` cho mọi sync upstream hoặc đổi `Local Overrides`.
- **Checks:** đọc lại `SKILL.md`; verify frontmatter `name: humanizer`; chạy `make agents_sync` rồi `make agents_sync-check`.

## Writing style

Plain Language trong prompt, doc, validation message, progress report:

- Lead bằng main point. Common words, active voice. Câu/đoạn ngắn.
- Một term cho một item. Dùng `must` cho requirement.
- Headings, lists, tables khi giúp reader. Bỏ từ lặp/thừa.
- Tránh double negative. Giữ nguyên identifier, command, path, schema field, quotation.
- `SKILL.md` giữ tiếng Anh như upstream; `AGENTS.md` và `CHANGELOG.md` viết tiếng Việt, thuật ngữ kỹ thuật giữ tiếng Anh.

## Editing the skill

- Giữ YAML metadata valid. Coi prompt dưới metadata là product.
- Local rule mới → vào `Local Overrides` đầu `SKILL.md`; không đụng phần upstream bên dưới.
