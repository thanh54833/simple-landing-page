# Guide for agents — Claude Code surface

## OVERVIEW
Claude Code integration: a generated command mirror, a generated skills mirror, and the plugin switch. None of it is the source of truth.

## STRUCTURE
```
.claude/
├── CHANGELOG.md   # root log: structure/settings changes, newest-first per date
├── commands/      # generated from .agents/.commands (11 routers + CHANGELOG.md)
├── skills/        # generated mirror of .agents/skills (all three packs)
└── settings.json  # enabledPlugins: superpowers@claude-plugins-official
```

## WHERE TO LOOK
| Task | Location | Notes |
|------|----------|-------|
| Canonical router text | `.agents/.commands/<name>.md` | edit there, then `make agents_sync` |
| Canonical skill text | `.agents/skills/` | this tree is a copy |
| Gate steps | `.agents/.commands/` + `.agents/skills/agentic-os/` | routers route, skills hold procedure |
| Superpowers plugin | `settings.json` | `/implement`, `/verify`, `/ship` invoke its skills |
| Track history | `CHANGELOG.md` | newest-first per date; update khi đổi `settings.json`/cấu trúc (sync thường không ghi) |

## CONVENTIONS
- Both trees are generated: `make agents_sync` writes them, `make agents_sync-check` exits 1 on drift or a stale copy.
- `commands/` gets every router byte-identically; the `.pi/prompts/` copy is the one that carries the generated marker.
- `skills/` is a complete mirror, `react-best-practices/` included.
- Cách update changelog: thêm bullet newest-first dưới `## YYYY-MM-DD` trong `CHANGELOG.md` khi đổi `settings.json` hoặc cấu trúc; chi tiết xem cuối file đó.

## ANTI-PATTERNS
- Don't author skills or routers here — an edit here is overwritten by the next `make agents_sync`.
- Don't add plugin/config entries here that another runtime needs; those belong to root configs.
