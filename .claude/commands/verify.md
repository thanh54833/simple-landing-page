---
description: Verify an implemented branch with evidence and code review before shipping, via Superpowers
argument-hint: "[plan path | hotfix record path | Tiny/Quick intent path]"
---

## User Input

```text
$ARGUMENTS
```

1. Resolve the plan, the hotfix record `/debug` wrote, an accepted Tiny/Quick intent, or (Tiny/Quick with no artifact) this session's diff, first match wins:
   - the User Input path;
   - the plan, hotfix record, or Tiny/Quick work this session implemented, else reviewed, created, or revised, else the user named as the subject of work (latest wins) — use it without asking, and state its path in one line so the user can correct it;
   - otherwise list `.physarum/docs/plans/*.md`, `.physarum/docs/hotfixes/*.md` and `.physarum/docs/intents/*-intent.md` (accepted, `Class: T0`) and ask. None of them and the work is Tiny/Quick → verify the branch diff itself.
2. ADR check: open the plan's spec, read `## Decisions`. Any linked ADR whose `Status` is not `accepted` → STOP with `NOT READY` and the ADR path as reason. A hotfix record or Tiny/Quick work (no plan, no spec) → skip steps 2 and 4.
3. Invoke the Superpowers `verification-before-completion` skill (Claude Code: `superpowers:verification-before-completion`). Run every test/verify command in the plan (hotfix record: its `Verify` commands and its regression test; Tiny/Quick: no plan commands, only the project's test suite, and the diff must stay a small change on an existing flow with no new acceptance criteria) plus the project's test suite; report real output. Failure → STOP with `NOT READY`, suggest fixing via `systematic-debugging`.
4. Design evidence. When the spec opened in step 2 has `## Design`, every item under its `Acceptance checks` has an entry in the `Evidence:` list of at least one UI task in the plan (written by `/implement`), and every UI task that touches a checked state has its own entry, and every UI task has a `detect:` entry equal to `[]` (any finding left in it counts as missing). A missing entry, or a bare "done", → STOP with `NOT READY`, listing the items. No `## Design` → skip this step.
5. Invoke the Superpowers `requesting-code-review` skill (Claude Code: `superpowers:requesting-code-review`) on the branch diff vs base. Fix Critical/Important findings and re-record the `Evidence:` entries a fix affects, then re-run steps 3 and 4.
6. STOP with a verdict: `READY TO SHIP` or `NOT READY` + reasons. Do not merge or push. On `READY TO SHIP`, suggest `/ship`.
