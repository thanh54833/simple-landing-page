# Guide for agents — skills root

Three packs, different domains. Pack-level rules live in each pack; this file routes.

## OVERVIEW
`.agents/skills/` holds `agentic-os/` (SDLC gate skills, factory-built), `rea/` (artifact/CI investigation skills, sourced from REA repo), and `react-best-practices/` (vendored Vercel performance rules).

## WHERE TO LOOK
| Task | Location | Notes |
|------|----------|-------|
| Pack policy (version, vendored, style) | `agentic-os/AGENTS.md` | applies to agentic-os pack |
| SDLC gates (intent/adr/update-spec/tasks/init-deep) | `agentic-os/<skill>/` | self-built, single SKILL.md |
| Frontend design system | `agentic-os/impeccable/` | vendored, don't touch upstream |
| New-page design skill | `agentic-os/hallmark/` | vendored, don't touch upstream; use for new builds, not existing designs |
| Co-authoring docs | `agentic-os/doc-coauthoring/` | minimal copy + Local Overrides |
| Release/CI/tooling/RE investigation | `rea/` | see `rea/AGENTS.md` |
| React/Next performance rules | `react-best-practices/` | vendored; `AGENTS.md` is build output of `rules/` — don't hand-edit, no build tooling shipped here |
| Add new skill | mimic sibling layout + trigger-only frontmatter | add lock pin if pack uses one |

## CONVENTIONS
- One `SKILL.md` per skill is source of truth; sibling `AGENTS.md` (where present) is the edit guide, never procedure.
- `rea/` skills were written for the REA repo — their `../../../docs/*` links dangle here; don't "fix" by copying docs in.
- `.claude/skills/` is a generated mirror of this whole tree (`make agents_sync`); never edit it there.

## ANTI-PATTERNS
- Don't mix domains: SDLC gate logic stays in `agentic-os/`, investigation tooling in `rea/`.
- Don't duplicate pack rules here that already live in `agentic-os/AGENTS.md`.
