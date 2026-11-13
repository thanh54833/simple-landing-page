---
description: Turn an approved design spec into an implementation plan ready to execute, via Superpowers writing-plans
argument-hint: <path to approved spec>
---

## User Input

```text
$ARGUMENTS
```

1. Resolve the spec, first match wins:
   - the User Input path;
   - the spec this session approved, else created or revised, else the user named as the subject of work (latest wins) — use it without asking, and state its path in one line so the user can correct it;
   - otherwise list `docs/physarum/specs/*-design.md` and ask which one.
   No spec → STOP, suggest `/spec`. A hotfix does not come here: its lane is `/debug` → `/verify` → `/ship`.
2. Confirm the spec is approved: ask once "Has this spec been reviewed and approved?" unless the user already approved it in this session or said so. Not approved → STOP.
3. ADR gate: read the spec's `## Decisions` section. Any linked ADR whose `Status` is not `accepted` → STOP, suggest `/adr <spec path>`. No `## Decisions` section and the spec records an architecture change (new subsystem, schema, auth, contract) → STOP, suggest `/adr`. A `## Decisions` line `ADR skipped by user` counts as a decision: continue and say in one line that the ADR was waived. Otherwise continue.
4. Invoke the Superpowers `writing-plans` skill (Claude Code: `superpowers:writing-plans`) with the spec as input, and hold its Execution Handoff until step 6.
5. Save to `docs/physarum/plans/YYYY-MM-DD-<topic>.md`, reusing the spec's date+topic stem. When the spec has `## Design`, the plan copies its `Copy` and `Acceptance checks` into Global Constraints and gives every UI task a `Design:` line naming the spec section, because implementers and reviewers see only their task brief and the Global Constraints.
6. Run the skill's Execution Handoff: ask the user to review the plan and choose an execution method (subagent-driven or inline).
7. STOP once the plan is reviewed and the method is chosen. Report the plan path and chosen method, suggest `/implement <plan path> <method>`. Do not invoke `subagent-driven-development` or `executing-plans` — implementation is a separate gate.
