# Changelog — impeccable

Một file duy nhất cho `skills/agentic-os/impeccable/`, newest first. Heading đầu giữ cùng version với `../agentic-os-lock.json`. Prose tiếng Việt, thuật ngữ kỹ thuật giữ tiếng Anh.

## 4.5.2

- Vendored từ `pbakaus/impeccable` (`.agents/skills/impeccable`), pin `sourceType: github` trong lock, `skillPath: impeccable/SKILL.md`.
- Layout upstream giữ nguyên: `SKILL.md`, `reference/` (sub-command + `degraded/`), `scripts/` (launcher, `command-metadata.json`, `live-browser-*.js`, `data/`, `VERSION`), `agents/`.
- Thêm `Local Overrides (factory-skills)`: canonical path `.agents/skills/agentic-os/impeccable/`, đọc literal path upstream theo path này, launcher tải engine về `~/.impeccable/bin/`.
- Router `/impeccable`, `/redesign`, `/enhance` giữ glue riêng của repo (contract `## Design`).
- Thêm `AGENTS.md` rule guide + `CHANGELOG.md` theo mẫu `writing-for-agents`.
