# Guide for agents — pack agentic-os

File này giải thích cách sửa pack `agentic-os` mà không gãy gate hay `install.sh`.
Mẫu theo `blader/humanizer` `AGENTS.md`: Key files + Rules + Writing style + Editing.

## What this pack contains

Pack skill 2 tầng (`agentic-os/<skill>/`); factory này consume tại chỗ, không có `install.sh`.
`SKILL.md` là prompt agent đọc. Pack không có build step.

| Skill | Nguồn | Hình thái |
|---|---|---|
| `writing-intent/` | self-built (`local`) | Single `SKILL.md`: capture `intent.md` proto-spec trước design |
| `writing-adr/` | self-built (`local`) | Single `SKILL.md`: gate G2+, lọc ADR, ghi `docs/superpowers/adr/` |
| `update-spec/` | self-built (`local`) | Single `SKILL.md`: back-sync spec đã approve với code drift, hunk dán nhãn |
| `tasks-creator/` | self-built (`local`) | `SKILL.md` + `reference/`: tạo tay `.tasks/01_migration/` của group, ngoài chuỗi gate, chưa có command |
| `init-deep/` | self-built (`local`) | Single `SKILL.md`: sinh hierarchy `AGENTS.md` (Root + subdirs theo complexity score), standalone, chưa có command |
| `doc-coauthoring/` | copy tay từ upstream | Single `SKILL.md` minimal + `Local Overrides` |
| `writing-for-agents/` | `mattpocock/skills@v1.3.1` | Vendored nguyên layout upstream: `SKILL.md` + `SKILL-MECHANICS.md` + `agents/openai.yaml` |
| `impeccable/` | `pbakaus/impeccable@4.5.2` | Full vendored project (`reference/` `scripts/` `agents/`) |
| `hallmark/` | `Nutlope/hallmark@2.0.0` | Full vendored project (`references/` `scripts/` `agents/`, `LICENSE`); design skill for new pages |

Chỉ sửa 5 skill self-built tại chỗ. Vendored giữ nguyên layout upstream.

## Key files

- `writing-intent/SKILL.md` — source of truth cho `/intent`; template `intent.md` + bảng Classification T2/T3/T4.
- `writing-adr/SKILL.md` — source of truth cho `/adr` (G2+); filter 3 điều kiện + template `NNNN-<slug>.md`.
- `tasks-creator/SKILL.md` — source of truth tạo `.tasks/01_migration/`; công thức ở `tasks-creator/reference/`.
- `init-deep/SKILL.md` — source of truth sinh hierarchy `AGENTS.md`; Scoring matrix + Decision Rules + template Root/Subdir.
- `<self-built>/AGENTS.md` — rule guide riêng từng skill (`writing-*`, `update-spec`, `tasks-creator`, `init-deep`; file này không chép lại internals của chúng).
- `<self-built>/CHANGELOG.md` — release notes từng skill, newest first. Chỉ skill self-built mới có.
- `agentic-os-lock.json` — pin version pack (`local-YYYY-MM-DD` cho skill tự build, tag upstream cho vendored).
- `.opencode/command/{intent,spec,adr,plan,implement,verify,ship,update-spec}.md` — router `$ARGUMENTS` vào skill (canonical); `.pi/prompts/` + `.claude/commands/` là bản copy; procedure nằm trong skill.
- `install.sh` (repo root) — copy pack + skeleton `docs/superpowers/` vào target, idempotent. Vắng tại factory này; setup theo runtime nằm trong `.pi/INSTALL.md`, `.opencode/INSTALL.md`, `.claude/INSTALL.md`.

## Rules for changes

- Giữ `SKILL.md` và command route nó (`intent.md`/`adr.md`) in sync. Command chỉ route + gate, không chép procedure. `tasks-creator` và `init-deep` chưa có command.
- `SKILL.md` local thắng mọi ref trong `00_sdlc_docs/` khi lệch. Local rule nằm ở `Local Overrides` đầu file.
- Single-file skill: mọi local rule vào `Local Overrides`, không tách file mới trừ khi >100 dòng reference (`tasks-creator/reference/` là trường hợp đã tách).
- Vendored (`impeccable/`, `doc-coauthoring/`, `writing-for-agents/`): không sửa nội dung upstream, chỉ thêm `Local Overrides` remap path lồng.
- **Version:** `agentic-os-lock.json` + heading đầu `CHANGELOG.md` giữ cùng một version. Self-built dùng `local-YYYY-MM-DD`; đổi skill → bump lock cùng commit.
- **Compatibility:** install và use instructions trung lập runtime (Orca, OpenCode, Claude Code là ví dụ, không phải giới hạn).
- **Description:** frontmatter `description` chỉ nêu trigger (`Use when...`), không tóm tắt workflow — agent phải đọc thân skill.
- **Length:** mỗi từ trong `SKILL.md` đều bị đọc mỗi lần fire. Thêm chữ phải đáng giá; cắt trước khi thêm.
- **History:** behavior change hoặc non-obvious fix → thêm 1 note ngắn vào `CHANGELOG.md` của skill đó.
- **Checks:** đọc lại `SKILL.md` sau sửa; verify frontmatter `name`/`description`; chạy tay gate liên quan (`/intent`, `/adr`, hoặc `/init-deep` trên 1 repo mẫu).

## Writing style

Plain Language trong comment, prompt, doc, validation message, progress report:

- Lead bằng main point. Common words, active voice.
- Câu và đoạn ngắn. Một term cho một item.
- Dùng `must` cho requirement. Headings, lists, tables khi giúp reader.
- Bỏ từ lặp/thừa. Hạn chế acronym, giải thích technical term.
- Không double negative.
- Giữ nguyên identifier, command, path, schema field, quotation, behavior-bearing example.
- Prose tiếng Việt, thuật ngữ kỹ thuật giữ tiếng Anh; labels trong template giữ English.

## Editing skills

- Giữ YAML frontmatter valid. Coi prompt dưới metadata là product.
- Ưu tiên instruction ngắn, rõ hơn là thêm exception hay giải thích lặp.
- Sửa duy nhất ở `.agents/`. `.claude/skills/` là bản mirror tracked: không sửa tay, re-sync sau mỗi thay đổi `.agents/`.
- Không lôi internals vendored project ra doc pack-level này.
