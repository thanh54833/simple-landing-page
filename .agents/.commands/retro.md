---
description: Retrospective on a coding session — suggest improvements to the agent's environment so future runs go better
argument-hint: "[session id or log path]"
---

## User Input

```text
$ARGUMENTS
```

1. Load the `writing-for-agents` skill (`.agents/skills/agentic-os/writing-for-agents/SKILL.md`) for the writing style guide.
2. Read the primary sources for the session: the User Input session id or log path, or if empty, the current session (session logs on this machine). Do not rely on memory of the session.
3. Identify improvement candidates in these categories:
   - **Navigation** — did the agent struggle to find files or information? Would a pointer in `AGENTS.md` or a reference doc have helped?
   - **Automated checks** — could lint, typecheck, tests or another check have caught the agent's errors? No guardrail at all (no pre-commit hook or CI job running lint/typecheck/test) is itself a finding.
   - **Coding standards** — should the reviewer agent get a new rule, or should an existing rule be removed or clarified? A mechanical rule belongs in a deterministic check; `CODING_STANDARDS.md` is for judgement calls only.
   - **Global `AGENTS.md`** — is steering that belongs in coding standards or automated checks sitting in the always-loaded file, especially when it is large?
   - **Tool economy** — were there expensive or token-inefficient tool calls that tooling could streamline?
   - **No-ops** — steering instructions that did not change the agent's behavior, especially in large steering files.
   - **Information access** — did the agent lack key information, such as dev server logs or read-only access to a third-party service?
4. Present the candidates to the user, ordered by severity. Each one: what happened (evidence from the session), the proposed change, and where it goes. STOP — do not apply changes until the user picks.

## Reference

- Implementation agents carry the most context pressure: they explore, write code and debug.
- Review agents receive a diff, need little exploration, and should enforce coding standards.
- `CLAUDE.md` / `AGENTS.md` load into every agent's context — use sparingly, mainly for navigation pointers.
- `CODING_STANDARDS.md` is read only during review. Past 1,000 lines, add navigation pointers to docs folders.
- Docs are reference files other files point to. Check for existing docs before writing new ones.
- Skills suit docs (their descriptions enter context) or user-invoked commands.
