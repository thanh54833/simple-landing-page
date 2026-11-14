# Guide for agents — command evals

## OVERVIEW
Behavior and trigger evals for the gate routers in `../*.md`, one folder per command. Not routers: `make agents_sync` copies only top-level `.md` files of `.commands/`, so nothing here is mirrored or listed as a command.

## STRUCTURE
```
evals/
├── AGENTS.md              # this file
└── <command>/             # same name as ../<command>.md
    ├── evals.json         # behavior: input + assertions
    └── triggers.json      # activation: phrase + should_trigger
```
One folder per router today: `intent`, `spec`, `adr`, `plan`, `implement`, `verify`, `ship`, `debug`, `backsync`, `save`, `retro`, `impeccable`, `redesign`, `enhance`, `img`.

## WHERE TO LOOK
| Task | Location | Notes |
|------|----------|-------|
| Add evals for a new router | copy `intent/` shape, `skill` = router filename without `.md` | method: `.agents/playbooks/002_skills/01_evals/evals.md` |
| Check a folder | `python3 .agents/playbooks/002_skills/01_evals/check-evals.py .agents/.commands/evals/<command>` | flat layout is auto-detected; must print `0 error` |
| Skill evals (not commands) | `.agents/skills/agentic-os/<skill>/evals/` | different layout: `evals/` inside the skill folder |

## CONVENTIONS
- Folder name = router filename without `.md`; `"skill"` in both JSON files must equal it (checker enforces).
- One test case per router step or gate branch: resolve input, each STOP condition, skill invoked, final STOP + next command. Inputs start with `/<command>`; a parenthesized note states session state the router reads.
- Assertions use the formula action + condition + checkable result. Pair each "must" with a `Does NOT` where the router forbids something (no next-gate skill, no commit, no code edit).
- `triggers.json`: ≥1 negative, drawn from neighboring gates (spec vs plan vs adr, redesign vs enhance, debug vs verify).
- No assertion text repeated inside one `evals.json`; reword per case.
- Changing a router's steps or STOP point → add or edit the matching case in the same commit. Renumbering steps changes nothing here: cases cite behavior, not step numbers.

## ANTI-PATTERNS
- Don't put a router, CHANGELOG, or any `.md` other than this guide directly in `evals/`: sync would treat top-level `.md` files as commands.
- Don't restate router procedure in an assertion beyond what makes it checkable; the router stays the single source.
- Don't write generic assertions (`works correctly`, `handles properly`): the checker rejects them.
