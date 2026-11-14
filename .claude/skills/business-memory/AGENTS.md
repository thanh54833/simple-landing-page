# Guide for agents — business-memory

File này giải thích cách sửa `business-memory` mà không gãy schema của memory đã tạo.

## What this skill contains

Skill self-built (`local`): `SKILL.md` (route + hard rules) và `reference/` (`init.md`, `save.md`). Không build step.
Ghi vào `.physarum/agents/product_owner/` của project đích. Command `/save` (`.agents/.commands/save.md`) route vào `reference/save.md`; chưa có command cho `init`.

## Key files

- `SKILL.md` — route, hard rules, rationalization table. Giữ ngắn; chi tiết thủ tục ở `reference/`.
- `reference/init.md` — khởi tạo; chứa schema `domain.json` và `index.json`.
- `reference/save.md` — lưu decision/insight/domain; chứa schema decision và insight.
- `CHANGELOG.md` — release notes, newest first.
- `../agentic-os-lock.json` — pin `business-memory` (`sourceType: local`).

## Rules for changes

- Đổi schema ở `reference/` phải kèm: (1) ghi chú migration trong `CHANGELOG.md`, (2) cập nhật file mẫu trong `.physarum/agents/product_owner/` của repo này nếu có.
- `.physarum/agents/product_owner/AGENTS.md` (persona recall) và skill này phải khớp: verbs, trường decision bắt buộc, quy tắc append-only.
- Không thêm quy tắc xoá hoặc sửa decision `accepted`.
- Version: lock và heading đầu `CHANGELOG.md` cùng `local-YYYY-MM-DD`; đổi skill thì bump cùng commit.
- Sau khi sửa: chạy `make agents_sync` (sinh `.claude/skills/`), không sửa bản sinh tay.
- Description chỉ nêu trigger, không tóm tắt workflow.
