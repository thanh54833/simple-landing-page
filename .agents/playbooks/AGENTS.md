# Guide for agents — playbooks

## OVERVIEW
Step-by-step procedures for maintenance chores on `.agents/` itself, one numbered folder per chore. Not skills, not gate routers: nothing fires from a trigger. An agent reads a playbook only when pointed at it (`.agents/AGENTS.md` WHERE TO LOOK, or the user), so discoverability is part of authoring.

## STRUCTURE
```
playbooks/
├── AGENTS.md                  # this file
└── 001_changelog/
    ├── changelog.md           # the playbook
    └── CHANGELOG.template.md  # asset the playbook copies from
```

## WHERE TO LOOK
| Task | Location | Notes |
|------|----------|-------|
| Create/extend a `CHANGELOG.md` | `001_changelog/changelog.md` | model playbook: copy its shape |
| Write a new playbook | "ADD A PLAYBOOK" below | start from the skeleton, not from scratch |
| Deep method for wording and testing | `superpowers:writing-skills` | same discipline; playbooks are skills minus auto-trigger |

## CONVENTIONS
- One chore = one folder `NNN_<topic>/` (zero-padded, next free number, never renumber). Folder = playbook + every asset it copies from; they reference each other by bare filename, so move them together.
- Not mirrored: `scripts/sync-agents.mjs` copies only `.commands/` and `skills/`, so `make agents_sync` never reads this tree.
- Prose Vietnamese, technical terms in English. Frontmatter `description` is triggers only ("Use when…"), never the steps: a description that summarizes the workflow gets followed instead of the body.
- Each line is read on every use: cut before adding. Link instead of copying; one source per fact.

## ADD A PLAYBOOK
1. **Worth it?** Needs a judgment call or an easy-to-miss order of steps → playbook. Fully mechanical → script or `make` target. Applies to one skill only → that skill's `AGENTS.md`.
2. **Observe the failure first.** Run the chore once with an agent that has no playbook (dry run, no writes). Write down verbatim where it goes wrong. No observed failure = nothing to write.
3. **Pick the form that matches the failure.** Skips a rule under pressure → Gate + Red flags. Wrong output shape → state what the output IS (parts, in order), not a "don't" list. Forgets an element → put it in the template as a required slot. Depends on a condition → conditional on an observable predicate.
4. **Copy this skeleton**, in this order:
   ```
   ---
   name: <topic>
   description: Use when <symptoms/triggers>
   ---
   # Playbook — <title>
   ## Overview        (1-2 lines + the one core rule)
   ## When to use     (also when NOT, and which other playbook/skill)
   ## Gate            (go/stop by a command or file check, never by a remembered list)
   ## Steps           (numbered, one action each)
   ## Quick reference (verify commands + expected result)
   ## Common mistakes (wrong | right)
   ## Red flags       (the agent's own excuses, from step 2)
   ```
5. **Gate on facts.** Any list that changes over time (vendored skills, supported scopes) is read from its source file by a command in the Gate. Hard-coded lists rot.
6. **Verify block pastes output.** Each check names a command and its passing result; "done" without output is not done.
7. **Re-run step 2 with the playbook.** Agent complies → ship. New excuse → add it to Red flags, re-run.
8. **Wire it up.** Add a row to this file's WHERE TO LOOK and, if broadly useful, to `.agents/AGENTS.md`. No link = nobody finds it.

## ANTI-PATTERNS
- Don't put a playbook under `skills/` or `.commands/`: those get mirrored and fire from triggers.
- Don't copy a template's contents into the playbook; reference it.
- Don't reuse or renumber `NNN_` after deleting a folder.
- Don't write Red flags from imagination when step 2 is possible; invented excuses miss the real ones.
- Don't append "unless it matters" clauses to a rule; state the exception as its own conditional.
- Don't ship a playbook whose paths you did not run: a wrong path (like a lock file at the wrong root) fails silently.
