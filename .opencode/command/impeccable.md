---
description: Design, critique, audit, polish or improve a frontend interface via the impeccable skill
argument-hint: <sub-command and/or target, e.g. "critique apps/web" | "polish checkout form">
---

## User Input

```text
$ARGUMENTS
```

1. Read `.agents/skills/agentic-os/impeccable/SKILL.md` in full. It is the source of truth; follow its `Local Overrides` (every `.agents/skills/impeccable/...` path reads as `.agents/skills/agentic-os/impeccable/...`; `<skill-base-dir>` = that folder).
2. Route the User Input per the skill:
   - First word matches a sub-command (`reference/<name>.md`, e.g. `adapt`, `animate`, `clarify`, `delight`, `layout`, `optimize`, `init`, `doctor`) → load that reference file and apply it to the rest of the input as the target.
   - Otherwise treat the whole input as the design brief and let the skill choose the reference files.
   - Empty input → list the available sub-commands from `reference/` and ask which one.
3. Run the launcher on Windows as `scripts/impeccable.cmd` (not the `sh` script). Do not edit anything under `impeccable/` — vendored; local rules go in `Local Overrides` only.
4. Not for backend-only or non-UI tasks — say so and STOP.
