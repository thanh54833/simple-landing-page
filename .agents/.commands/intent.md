---
description: Capture an idea, ticket, or incident alert as a draft intent.md (proto-spec) before any design
argument-hint: <idea | ticket ref | alert text>
---

## User Input

```text
$ARGUMENTS
```

Invoke the `writing-intent` skill. If the runtime cannot find it, read `.agents/skills/agentic-os/writing-intent/SKILL.md` and follow it exactly.

1. Treat the User Input as source material. If it is empty, ask for the idea, ticket, or alert.
2. Classify the source (`idea` | `ticket` | `alert`); ask once if unclear. Ticket → keep its ID in `Source ref`.
3. If the request is a Tiny/Quick change (a small change on an existing flow: typo, rename, comment, format, constant, flag, a tweak to an existing endpoint that keeps its contract, one-file fix; 1–2 files, no new acceptance criteria) → an intent is optional: write a short one only if the user wants it recorded, otherwise say it is not needed, name `[/intent →] /implement` → `/verify` → `/ship`, and stop. If it is a hotfix (production is broken, the goal restores existing behavior) → say intent.md is not needed, name `/debug` → `/verify` → `/ship`, and stop.
4. Ask analyst questions one at a time, per the skill, until every Classification predicate is answered or parked in Open questions.
5. Write `docs/physarum/intents/YYYY-MM-DD-<outcome-slug>-intent.md` from the skill's template (including `## Classification`), `Status: draft`.
6. STOP. Hand the file path to the originator for correction and state the proposed `Class` + `Lane` plus the next command (the first step of the Lane) for them to confirm or change. Do not commit, do not invoke `brainstorming` or `writing-plans`, do not design.
