---
description: Save a settled decision, insight, or business rule into .physarum/agents/product_owner via the business-memory skill
argument-hint: <what to save, free text>
---

## User Input

```text
$ARGUMENTS
```

1. Resolve what to save, first match wins; state it in one line so the user can correct it:
   - the User Input text;
   - every decision, business rule, or lesson this session settled with the user and has not been saved yet (list them in the one line; save them as one package);
   - otherwise ask what to save.
2. Check the target. `.physarum/agents/product_owner/index.json` missing → STOP: say the memory is not initialised and offer to run the `business-memory` skill's `reference/init.md` first. Do not create it from this command.
3. Invoke `business-memory` and follow its `reference/save.md` with the resolved input. Unsettled input follows the skill's "Chốt hay chưa" and "Evidence" rules: never `accepted` without the owner's explicit choice.
   Ask once with the diff; the resolved-input line and the diff confirmation are the same stop.
4. STOP after the skill reports the files written and the updated `index.json`. Do not edit code or invoke another gate's skill.
