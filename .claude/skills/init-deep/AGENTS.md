# Guide for agents — init-deep

File này giải thích cách sửa `init-deep` mà không gãy scoring hay hierarchy `AGENTS.md`.
Mẫu theo `blader/humanizer` `AGENTS.md`.

## What this skill contains

Skill single `SKILL.md`, không build step. Sinh hierarchy `AGENTS.md` cho bất kỳ repo nào:
Root (full treatment, 50-150 dòng) + subdirs theo complexity score (30-80 dòng mỗi file).
Chạy standalone bằng `/init-deep` (không thuộc chuỗi gate `intent → ship`);
target là `AGENTS.md` của repo đích — không remap, không chạy thử tại factory này.

Điểm mạnh của skill: Discovery concurrent (explore background + bash + LSP/codegraph +
đọc `AGENTS.md` sẵn có) rồi mới Score & Decide, nên vị trí file bám cấu trúc thật,
không bám convention đoán mò.

## Key files

- `SKILL.md` — source of truth duy nhất: Discovery concurrent, Scoring matrix, Decision Rules, template Root/Subdir, Review & Final Report. Mọi sửa behavior bắt đầu ở đây.
- `AGENTS.md` (file này) — rule guide cho agent sửa skill; không chứa procedure chạy.
- `CHANGELOG.md` — release notes, newest first. Behavior change hoặc non-obvious fix phải có 1 note.
- `../agentic-os-lock.json` — pin `init-deep` (`sourceType: local`, `version: local-YYYY-MM-DD`).
- Chưa có command route trong `.opencode/command/` — skill gọi trực tiếp theo trigger `description` (như `tasks-creator`).
- Target runtime: `./AGENTS.md` (root, ALWAYS create) + `./<scored-dir>/AGENTS.md` của repo đích.

## Rules for changes

- **Scoring:** matrix 8 factors (File count 3x, Subdir 2x, Code ratio 2x, Unique patterns 1x, Module boundary 2x, Symbol density 2x, Export count 2x, Reference centrality 3x). Đổi weight/threshold → cập nhật bảng Phase 2 + Decision Rules trong `SKILL.md`.
- **Decision Rules:** Root ALWAYS create; `>15` create; `8-15` create nếu distinct domain; `<8` skip (parent covers). Đổi rule → cập nhật Review (dedup/trim) vì coverage đổi theo.
- **Template:** Root đủ `OVERVIEW → STRUCTURE → WHERE TO LOOK → CODE MAP → CONVENTIONS → ANTI-PATTERNS → UNIQUE STYLES → COMMANDS → NOTES`; subdir chỉ `OVERVIEW (1 dòng)` + `STRUCTURE (nếu >5 subdirs)` + `WHERE TO LOOK` + `CONVENTIONS (nếu khác parent)` + `ANTI-PATTERNS`, NEVER repeat parent. Đổi template → cập nhật Quality gates (Root 50-150, subdir 30-80) + Review checklist.
- **File Writing Rule:** `AGENTS.md` đã tồn tại → `Edit`; chưa tồn tại → `Write`; NEVER overwrite existing bằng `Write`. Không đổi rule này.
- **Concurrency:** explore background + bash + LSP/codegraph chạy concurrent; Root trước, subdirs parallel sau. Không serialize thành tuần tự.
- **Dynamic spawning:** agent count theo scale (files, lines, depth, monorepo, languages). Đổi threshold → cập nhật bảng Phase 1.
- **Version:** giữ cùng version ở `../agentic-os-lock.json` và heading đầu `CHANGELOG.md`. Đổi skill → bump lock cùng commit.
- **Compatibility:** instructions trung lập runtime (Claude Code, OpenCode, Orca là ví dụ).
- **Description:** frontmatter chỉ nêu trigger (`Initialize hierarchical AGENTS.md...`), không tóm tắt workflow.
- **Length:** mỗi từ trong `SKILL.md` bị đọc mỗi lần fire. Thêm chữ phải đáng giá; công thức dài tách ra `reference/` chỉ khi >100 dòng hoặc dùng lại nhiều chỗ.
- **History:** thêm note ngắn vào `CHANGELOG.md` cho mọi behavior change.
- **Checks:** đọc lại `SKILL.md`; verify frontmatter `name: init-deep`; chạy tay 1 repo mẫu (case update + case `--create-new`).

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
- Sửa duy nhất ở `.agents/`; `.claude/skills/` là mirror tracked, re-sync sau khi sửa (không sửa tay).
