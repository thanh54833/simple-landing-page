# Guide for agents — canonical skills + gate routers

## OVERVIEW
`agentic-os-core` ships skill packs here, not app code: `skills/agentic-os/` (SDLC gates, self-built + 3 vendored), `skills/rea/` (REA investigation), and `skills/react-best-practices/` (vendored Vercel rules). `.commands/` holds the gate routers. Both trees are canonical — every runtime copy is generated from here by `make agents_sync`.

## STRUCTURE
```
.agents/
├── .commands/                 # gate routers: 11 + CHANGELOG.md (thin: route + gate, no procedure)
├── settings/
│   ├── models.json            # single source of truth for model (synced down by `make agents_sync`)
│   └── mcp.json               # single source of truth for MCP servers (synced down by `make agents_sync`)
├── skills/
│   ├── AGENTS.md              # pack router
│   ├── agentic-os/            # intent, adr, update-spec, tasks-creator, init-deep, doc-coauthoring, impeccable, writing-for-agents
│   ├── rea/                   # 4 artifact/CI investigation skills
│   └── react-best-practices/  # vendored; AGENTS.md is generated
└── AGENTS.md                  # this file
```

Fan-out written by `scripts/sync-agents.mjs` (`make agents_sync`, short `make asc`, alias `make acs`):

| Target | Contents |
|---|---|
| `.claude/commands/` | every router, byte-identical |
| `.opencode/command/` | every router, byte-identical |
| `.pi/prompts/` | routers only, plus a generated marker inside the frontmatter |
| `.claude/skills/` | mirror of the whole `skills/` tree |
| `.omo/omo.jsonc`, `.opencode/oh-my-openagent.json`, `.pi/settings.json` | model fields patched from `settings/models.json` |
| `.mcp/servers.json`, `.pi/mcp.json`, `opencode.json` (`mcp` block) | MCP servers from `settings/mcp.json` |

## WHERE TO LOOK
| Task | Location | Notes |
|------|----------|-------|
| Edit a gate router | `.commands/<name>.md` | canonical; run `make agents_sync` after |
| Sync the runtime copies | `scripts/sync-agents.mjs` | `--check` writes nothing, exits 1 on drift |
| Pack rules | `skills/AGENTS.md` | start here, then the pack's own `AGENTS.md` |
| Write/revise an intent | `skills/agentic-os/writing-intent/SKILL.md` | source of truth for `/intent` |
| Record an ADR | `skills/agentic-os/writing-adr/SKILL.md` | gate G2+; writes `docs/superpowers/adr/` |
| Back-sync a drifted spec | `skills/agentic-os/update-spec/SKILL.md` | hunk-labeled patch, confirm-then-write |
| Gate task sets | `skills/agentic-os/tasks-creator/` | outside the gate chain, no command |
| Hierarchy `AGENTS.md` | `skills/agentic-os/init-deep/SKILL.md` | generator for this file |
| Release/CI/RE work | `skills/rea/AGENTS.md` | REA paths resolve against the target repo |
| Frontend design | `skills/agentic-os/impeccable/SKILL.md` | vendored; follow its `Local Overrides` |
| Write skills/AGENTS.md | `skills/agentic-os/writing-for-agents/SKILL.md` | vendored reference: pointers, hierarchy, pruning |

## CONVENTIONS
- Edit only here. `.claude/commands/`, `.claude/skills/`, `.opencode/command/`, `.pi/prompts/` are generated mirrors — `make agents_sync` writes them, `make agents_sync-check` fails when they drift.
- Routers stay thin: they name the skill and the gate, never the procedure. The skill holds the procedure.
- Self-built skill = single `SKILL.md` + sibling `AGENTS.md` (edit guide) + `CHANGELOG.md`; vendored = upstream layout untouched, local rules under `Local Overrides`.
- Frontmatter `description` is trigger-only (`Use when...`); the workflow lives in the body.
- Every word in `SKILL.md` is read on each fire — cut before adding.

## ANTI-PATTERNS
- Don't hand-edit a generated mirror (`make agents_sync` overwrites it silently); don't author routers or skills anywhere but `.agents/`.
- Don't add a copy directory without adding it to `ROUTER_TARGETS` (or the skills mirror) in `scripts/sync-agents.mjs` — an unlisted copy is drift nobody checks.
- Don't mix domains: SDLC gates in `agentic-os/`, investigation tooling in `rea/`.
- Don't hand-edit `react-best-practices/AGENTS.md` — it is generated from `rules/`.
- Don't copy REA docs in to fix dangling `../../../docs/*` links; they resolve in the repo under investigation.
