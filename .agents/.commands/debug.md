---
description: Debug a bug, test failure, or unexpected behavior via systematic root-cause investigation
argument-hint: <symptom, error message, or failing test>
---

## User Input

```text
$ARGUMENTS
```

1. Treat the User Input as the symptom. If it is empty, ask what is broken: the error message, failing test, or unexpected behavior, plus the exact repro steps.
2. Invoke the Superpowers `systematic-debugging` skill (Claude Code: `superpowers:systematic-debugging`) with the symptom as input. It owns the four phases (root cause → pattern → hypothesis → implementation) — follow it as written. No fixes before Phase 1 completes.
3. For this repo's dev stack (vite proxy → FastAPI on `:8000`), check the layer first: is anything listening on `:8000`, and does the API answer directly, before touching code.
4. STOP with a report: root cause, the single fix applied, and verify output. 3+ failed fixes → question the architecture per the skill, do not attempt fix #4. Suggest `/verify` when the fix touches a planned implementation.
