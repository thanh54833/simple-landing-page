# Guide for agents — gate routers

## OVERVIEW
Canonical slash-command routers: each names one skill plus its gate, never the procedure.

## STRUCTURE
Gate chain, in order: `intent` → `spec` → `adr` → `plan` → `implement` → `verify` → `ship`. Standalone (outside the chain): `debug`, `impeccable`, `redesign`, `retro`, `update-spec` (back-sync gate for drifted specs). Shared `CHANGELOG.md` (newest-first per date).

## WHERE TO LOOK
| Router | Backing skill | Notes |
|--------|---------------|-------|
| `intent.md` | `writing-intent` | draft intent.md; STOPs on Bounded work (no intent needed) |
| `spec.md` | Superpowers `brainstorming` | needs accepted intent |
| `adr.md` | `writing-adr` | G2+ gate; "no ADR needed" is a valid outcome |
| `plan.md` | Superpowers `writing-plans` | needs approved spec (+ accepted ADRs); T3 hotfix takes accepted intent |
| `implement.md` | `subagent-driven-development` / `executing-plans` | STOPS before branch finishing |
| `verify.md` | `verification-before-completion` + `requesting-code-review` | verdict `READY TO SHIP` / `NOT READY` |
| `ship.md` | `finishing-a-development-branch` | needs `/verify` verdict first |
| `debug.md` | Superpowers `systematic-debugging` | no fixes before Phase 1; includes the vite → `:8000` layer check |
| `impeccable.md` | `impeccable` | frontend-only; routes sub-commands in `reference/` |
| `redesign.md` | `impeccable` | frontend-only; resolves a component/page/sheet target to files, refines inside DESIGN.md (no new tokens), keeps behavior + tests |
| `retro.md` | `writing-for-agents` | needs session id/log; categories: nav, checks, standards, global, tools |
| `update-spec.md` | `update-spec` | back-sync drifted spec; STOP, suggest `/adr` (new number), `/verify`, or `/intent` |

## CONVENTIONS
- Frontmatter is exactly two fields: `description` (trigger-only) + `argument-hint`. Quote `argument-hint` when it starts with `[` (`retro`, `verify`), or YAML parses it as a list.
- Body is `## User Input` with a fenced `$ARGUMENTS` block, then numbered steps.
- Chain inputs strictly: accepted intent → `/spec`; approved spec → `/plan`; reviewed plan + method → `/implement`; verdict → `/ship`. Each router STOPS and names the next command instead of invoking the next skill.
- Session default input: `spec`, `adr`, `plan`, `implement`, `verify`, `update-spec` resolve their file by the same ladder — User Input path, else the artifact this session just produced at the previous gate (latest accepted/approved, else created/revised, else named by the user), else list and ask. A session default is used without asking and stated in one line; the user corrects it by passing a path. Keep the wording identical across routers. `/plan` T3 resolves an intent only when the User Input is an intent path or the session's latest accepted intent is `Class: T3`.
- Approval already given in the session counts: do not re-ask "reviewed and approved?" for an artifact the user approved earlier in the same session.
- `/verify` failure suggests fixing via `systematic-debugging` (same skill behind `/debug`).

## ANTI-PATTERNS
- Don't put procedure in a router — the skill owns it.
- Don't add a router without a backing skill (local `.agents/skills/` or a named Superpowers skill).
- Don't invent a second naming scheme — filename is the command name, one router per gate.
