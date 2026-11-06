---
description: Turn an accepted intent.md into a written design spec via Superpowers brainstorming
argument-hint: <path to accepted intent.md>
---

## User Input

```text
$ARGUMENTS
```

1. Resolve the intent file, first match wins:
   - the User Input path;
   - the intent this session accepted, else created or revised, else the user named as the subject of work (latest wins) — use it without asking, and state its path in one line so the user can correct it;
   - otherwise list `docs/superpowers/intents/*-intent.md` and ask which one.
2. Read it from disk (an accept in this session edits the file; never rely on memory of its `Status`). If `Status` is not `accepted` → STOP: say the PO must accept it first (run `/intent` to revise a draft). No intent file → STOP, suggest `/intent`.
3. Invoke the Superpowers `brainstorming` skill (Claude Code: `superpowers:brainstorming`) with the intent as the brief:
   - Take the architectural path; do not reclassify to bounded or spike.
   - Problem, Proposed outcome, Constraints, Out of scope come from the intent — do not re-ask them; only ask what is still in Open questions or needed for design.
4. Save the spec to `docs/superpowers/specs/YYYY-MM-DD-<topic>-design.md`, reusing the intent's date+topic stem.
5. STOP after the user approves the written spec. Suggest `/adr <spec path>` (G2+; may conclude "No ADR needed"), then `/plan`. Do not invoke `writing-plans` — planning is a separate gate.
