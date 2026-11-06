# Changelog — init-deep

Newest first. Heading đầu giữ cùng version với `../agentic-os-lock.json`.

## local-2026-10-12

- Initial self-built release: sinh hierarchy `AGENTS.md` (Root 50-150 dòng + subdirs 30-80 dòng theo complexity score), ngoài chuỗi gate SDLC.
- Discovery concurrent: explore background (dynamic spawning theo scale) + bash structure + LSP/codegraph code map + đọc `AGENTS.md` sẵn có; modes `--create-new` / `--max-depth`.
- Scoring matrix 8 factors + Decision Rules (Root ALWAYS, `>15` create, `8-15` distinct domain, `<8` skip); File Writing Rule Edit-vs-Write; Review dedup + Final Report.
- DỪNG ở Final Report (files, dirs analyzed, hierarchy); không design/implement tiếp.
- Thêm `AGENTS.md` rule guide + `CHANGELOG.md` theo mẫu `blader/humanizer`.
