# Guide for agents — update-spec

File này giải thích cách sửa `update-spec` mà không gãy gate back-sync.
Mẫu theo `blader/humanizer` `AGENTS.md`.

## What this skill contains

Skill single `SKILL.md`, không build step. Chạy sau implement khi code drift khỏi spec đã approve (hotfix đổi logic, fix bug đổi behavior), hoặc khi change nhỏ đã chốt cần ghi vào spec. Patch spec tại chỗ trong `docs/superpowers/specs/`, hunk dán nhãn, confirm-then-write. Viết xong thì DỪNG — không gọi `writing-plans`, không sửa code.

## Key files

- `SKILL.md` — source of truth duy nhất: hai đường (back-sync drift / record delta), hunk MODIFIED/ADDED/REMOVED, confirm-then-write. Mọi sửa behavior bắt đầu ở đây.
- `AGENTS.md` (file này) — rule guide cho agent sửa skill; không chứa procedure chạy gate.
- `CHANGELOG.md` — release notes, newest first. Behavior change hoặc non-obvious fix phải có 1 note.
- `../agentic-os-lock.json` — pin `update-spec` (`sourceType: local`, `version: local-YYYY-MM-DD`).
- `.agents/.commands/update-spec.md` — router `$ARGUMENTS` (spec path) vào skill; giữ in sync, không chép procedure.
- Target runtime: mọi file trong `docs/superpowers/specs/` (patch tại chỗ) + ghi chú artifact liên quan khi cần.

## Rules for changes

- Giữ `SKILL.md` và `.agents/.commands/update-spec.md` in sync. Command chỉ resolve input + check approve + khai báo điểm DỪNG.
- **Drift:** base = commit lúc spec approved (`git log -- <spec-path>`), diff `base..HEAD -- apps/`. Behavior vào spec; UI-only loại + ghi lý do.
- **Reconcile:** draft trong conversation trước, check 2 chiều spec <-> intent/plan/ADR. `MODIFIED` giữ scenario cũ không bị đụng. Đọc lại file sau patch, quét note mới vs text cũ.
- **Confirm:** một spec một lần, show hunk + why, confirm mới ghi. Reject thì bỏ. Load-bearing (delete vs implement vs defer) → present options, không tự quyết.
- **Gate:** approved spec mới chạy. Chưa approve → `/spec`. Feature/kiến trúc mới → `/intent` mới. Đổi architecture → `/adr` số mới, không rewrite ADR cũ.
- **Scope:** planning artifacts only — không code, tests, `DESIGN.md`, `PRODUCT.md`, config. Không rewrite test đang pin để khớp quyết định của mình.
- **Version:** giữ cùng version ở `../agentic-os-lock.json` và heading đầu `CHANGELOG.md`. Đổi skill → bump lock cùng commit.
- **Compatibility:** instructions trung lập runtime (Claude Code, OpenCode, Orca là ví dụ).
- **Description:** frontmatter chỉ nêu trigger (`Use when...`), không tóm tắt workflow.
- **Length:** mỗi từ trong `SKILL.md` bị đọc mỗi lần fire. Thêm chữ phải đáng giá.
- **History:** thêm note ngắn vào `CHANGELOG.md` cho mọi behavior change.
- **Checks:** đọc lại `SKILL.md`; verify frontmatter `name: update-spec`; chạy tay 1 case back-sync drift + 1 case quyết định load-bearing (phải present options, không tự ghi).

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
- Local rule mới → vào `Local Overrides` đầu `SKILL.md`; `SKILL.md` local thắng `.templates/spec/OpenSpec/` khi lệch.
