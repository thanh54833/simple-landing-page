---
description: Execute an approved implementation plan task-by-task via Superpowers, stopping before branch finishing
argument-hint: <plan path | Tiny/Quick intent path | request> [subagent-driven | inline]
---

## User Input

```text
$ARGUMENTS
```

1. Resolve the plan (or a Tiny/Quick intent or request), first match wins:
   - the User Input path;
   - the plan this session reviewed, else created or revised, else the user named as the subject of work (latest wins) — use it without asking, and state its path in one line so the user can correct it;
   - otherwise list `.physarum/docs/plans/*.md` and ask which one.
   No plan → STOP, suggest `/plan`. Exception: an intent path with `Status: accepted` and `Class: T0` is valid input in place of a plan, and so is a Tiny/Quick request with no artifact (a small change on an existing flow, 1–2 files, no new acceptance criteria) stated in the User Input or this session; when User Input is empty and this session produced no plan, intent, or spec, the chat message that invoked this command is the request; either is the single task. A larger change with no plan → STOP, suggest `/intent`.
2. Resolve two choices, the execution method and the workspace. For each, first match wins; ask only for what is still unresolved, in one question round:
   - Method: the User Input, else the method chosen at `/plan` in this session, else ask. A Tiny/Quick change has no method: it runs directly in this session.
   - Workspace: the User Input or a workspace the user already stated in this session, else ask.
   When asking, never pick silently. List the recommended option first, labeled `(Recommended)`:
   - Method: `subagent-driven (Recommended)`, then `inline`.
   - Workspace: `current branch (Recommended)` (work in place on the checked-out branch, no worktree), then `new worktree` (isolated worktree and branch).
   When the checked-out branch is `main` or `master`, the `current branch` description must say it commits to the default branch. The user's answer is the consent `using-git-worktrees` requires.
3. A Tiny/Quick change (intent or request): implement it directly in this session — no plan, no subagents — with `superpowers:test-driven-development` when a test applies; the workspace choice still applies. A change that turns out to need new acceptance criteria or to touch more than 1–2 files → STOP and reclassify T1: write an intent if none is accepted, then `/spec`; when a spec for this intent already exists (same date+topic stem), suggest `/plan <spec path>` instead. Otherwise invoke the matching Superpowers skill with the plan:
   - `subagent-driven` → `subagent-driven-development` (Claude Code: `superpowers:subagent-driven-development`)
   - `inline` → `executing-plans` (Claude Code: `superpowers:executing-plans`)
   The skill owns TDD and per-task review — follow it as written. Pass the workspace choice from step 2 so the skill does not ask again: for `current branch`, skip worktree creation; for `new worktree`, follow its worktree setup.
4. UI tasks. When the plan's spec has `## Design`, every task that touches UI follows the Build stage of the Design contract in `.agents/.commands/spec.md` before its task review. The dispatch for a UI task names the spec's `## Design` section and tells the implementer to read `craft-floor.md` before editing. The implementer builds and runs the build and tests; the controller (the session with browser tools and the dev server) runs the visual round, runs `impeccable detect` on the changed UI files, and records the `Evidence:` list (including its `detect:` entry) under the task in the plan file. The reviewer receives `Acceptance checks` and `Copy` as constraints. A deviation from `## Design` stops the task and goes through `/backsync` (it patches `## Design`) before the task resumes; it is never made silently in code.
5. STOP at the point where the skill would invoke `finishing-a-development-branch`. Do not merge, push, open a PR, or discard. Report: branch/worktree, tasks completed, anything left open. Suggest `/verify <plan path>`.
