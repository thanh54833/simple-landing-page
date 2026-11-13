# Guide for agents — gate routers

## OVERVIEW
Canonical slash-command routers: each names one skill plus its gate, never the procedure.

## STRUCTURE
Gate chain, in order: `intent` → `spec` → `adr` → `plan` → `implement` → `verify` → `ship`. Hotfix lane (no intent, spec or plan): `debug` → `verify` → `ship`. Tiny/Quick lane (intent optional): [`intent` →] `implement` → `verify` → `ship`. Standalone (outside the chain): `debug`, `enhance`, `impeccable`, `img` (images via Cobra), `redesign`, `retro`, `save` (business memory), `update-spec` (back-sync gate for drifted specs). Shared `CHANGELOG.md` (newest-first per date). `evals/<command>/` holds the evals for each router (not routers; sync ignores the folder).

## WHERE TO LOOK
| Router | Backing skill | Notes |
|--------|---------------|-------|
| `intent.md` | `writing-intent` | draft intent.md; STOPs on hotfix work (no intent needed); a Tiny/Quick change may get a short intent, optional |
| `spec.md` | Superpowers `brainstorming` | needs accepted intent; UI spec also gets `## Design` via `impeccable`; ends by offering `/adr` or `/plan`, recommended one first (first matching rule: user said skip ADR, or `## Decisions` has an outcome and no pending ADR → `/plan`; T3, architecture change or pending ADR → `/adr`; else `/plan`); picking `/plan` on T3 or an architecture change with no outcome writes the line `ADR skipped by user` to `## Decisions` |
| `adr.md` | `writing-adr` | G2+ gate; "no ADR needed" is a valid outcome |
| `plan.md` | Superpowers `writing-plans` | needs approved spec (+ accepted ADRs, or the `ADR skipped by user` line); carries `## Design` checks into the plan |
| `implement.md` | `subagent-driven-development` / `executing-plans`; Tiny/Quick (intent or request) runs directly with TDD | STOPS before branch finishing; UI tasks built to the spec's `## Design` |
| `verify.md` | `verification-before-completion` + `requesting-code-review` | takes a plan, a hotfix record, or Tiny/Quick work; verdict `READY TO SHIP` / `NOT READY`; a spec with `## Design` also needs an `Evidence:` entry per `Acceptance checks` item |
| `ship.md` | `finishing-a-development-branch` | needs `/verify` verdict first |
| `debug.md` | Superpowers `systematic-debugging` | no fixes before Phase 1; includes the vite → `:8000` layer check; a production fix starts the hotfix lane and writes a `docs/physarum/hotfixes/` record for `/verify` |
| `impeccable.md` | `impeccable` | frontend-only; routes sub-commands in `reference/`; owns the `## Design` contract used by `spec`, `plan`, `implement`, `verify` |
| `redesign.md` | `impeccable` | frontend-only; resolves a component/page/sheet/URL/DOM-path target to files, looks first (screenshots + shipped pattern to mirror), refines inside DESIGN.md (no new tokens), keeps behavior + tests, verifies once (detect, build, tests, one visual round) |
| `enhance.md` | `impeccable` | frontend-only; raises ONE named element (scope sovereign, diff hunks limited to it), no new behavior without asking; self-contained on purpose — its parse/resolve/look/pin/verify/clean steps duplicate `redesign.md`, so fix a shared bug in both |
| `img.md` | `ai-image-generation` (Cobra agent in `.physarum/ai-image-generate/cobra-agent/`) | standalone; first word a Cobra verb (`recall`, `new-series`, `add-slot`, `generate`, `approve`, `check`, `improve`, `document`) else the text is a brief mapped to a series/slot; STOPS when Cobra's `AGENTS.md` is missing; Cobra owns the procedure, the agreement before `belt app run` and the `drafts/` → `final/` flow, so the router holds none of it |
| `retro.md` | `writing-for-agents` | needs session id/log; categories: nav, checks, standards, global, tools |
| `save.md` | `business-memory` | standalone; saves a settled decision/insight/rule to `docs/physarum/business-memory/` (writes `proposed` when unsettled); STOPS if memory is not initialised, offering `reference/init.md` |
| `update-spec.md` | `update-spec` | back-sync drifted spec; STOP, suggest `/adr` (new number), `/verify`, or `/intent` |
| `evals/<command>/` | — | `evals.json` + `triggers.json` per router; rules in `evals/AGENTS.md`, method in `playbooks/002_skills/01_evals/evals.md` |

## CONVENTIONS
- Frontmatter is exactly two fields: `description` (trigger-only) + `argument-hint`. Quote `argument-hint` when it starts with `[` (`retro`, `verify`), or YAML parses it as a list.
- Body is `## User Input` with a fenced `$ARGUMENTS` block, then numbered steps.
- Chain inputs strictly: accepted intent → `/spec`; approved spec → `/plan`; reviewed plan + method → `/implement`; verdict → `/ship`. Each router STOPS and names the next command instead of invoking the next skill.
- Session default input: `spec`, `adr`, `plan`, `implement`, `verify`, `update-spec` resolve their file by the same ladder — User Input path, else the artifact this session just produced at the previous gate (latest accepted/approved, else created/revised, else named by the user), else list and ask. A session default is used without asking and stated in one line; the user corrects it by passing a path. Keep the wording identical across routers.
- Approval already given in the session counts: do not re-ask "reviewed and approved?" for an artifact the user approved earlier in the same session.
- `/verify` failure suggests fixing via `systematic-debugging` (same skill behind `/debug`).
- The `## Design` contract (slots, Spec stage, Build stage, Missing reference) is defined once in `impeccable.md`. `spec`, `plan`, `implement` and `verify` point there by name and never restate the slots.

## ANTI-PATTERNS
- Don't put procedure in a router — the skill owns it. Exception: a vendored skill (`impeccable`, `doc-coauthoring`, `writing-for-agents`) cannot be edited, so the repo glue for it (the design contract, `redesign`, `enhance`) lives in its router; keep that to what the skill lacks.
- Don't add a router without a backing skill (local `.agents/skills/` or a named Superpowers skill).
- Don't add any `.md` directly under `evals/`, and don't change a router's steps or STOP point without updating its `evals/<command>/` case: sync copies top-level `.md` files only, and a stale eval tests behavior the router no longer has.
- Don't invent a second naming scheme — filename is the command name, one router per gate.
