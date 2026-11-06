---
description: Record architecture decisions from an approved design spec as ADRs (G2+ gate) before planning
argument-hint: <path to approved spec>
---

## User Input

```text
$ARGUMENTS
```

1. Resolve the spec, first match wins:
   - the User Input path;
   - the spec this session approved, else created or revised, else the user named as the subject of work (latest wins) — use it without asking, and state its path in one line so the user can correct it;
   - otherwise list `docs/superpowers/specs/*-design.md` and ask which one.
   No spec → STOP, suggest `/spec`.
2. Confirm the spec is approved: ask once "Has this spec been reviewed and approved?" unless the user already approved it in this session or said so. Not approved → STOP.
3. Invoke the `writing-adr` skill. If the runtime cannot find it, read `.agents/skills/agentic-os/writing-adr/SKILL.md` and follow it exactly.
   - Input is the spec; the skill decides whether any ADR is needed. "No ADR needed" is a valid outcome.
4. ADRs go to `docs/superpowers/adr/NNNN-<slug>.md`; the spec gets a `## Decisions` section listing each outcome.
5. STOP once the user has accepted every ADR (or the "No ADR needed" line). Report the ADR paths, suggest `/plan <spec path>`. Do not invoke `writing-plans` — planning is a separate gate.
