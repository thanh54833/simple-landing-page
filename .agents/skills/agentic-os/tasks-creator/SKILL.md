---
name: tasks-creator
description: Use when creating or updating a task set under `.tasks/` (00_tasks.json + AGENTS.md) by hand — a new task set, adding a task or subtask to a set that already has progress, or recording a finished task's result in its note.
---

# tasks-creator

`<skill dir>` below = the folder that holds this `SKILL.md`; run scripts as `python3 <skill dir>/scripts/...`.

## Overview

A task set is one folder `.tasks/NN_<name>/` holding `00_tasks.json` (tasks → subtasks) and a derived
`AGENTS.md`. There are no waves, no per-app folders and no status file: progress lives in each
task's and subtask's `status` and `note`. Schema, status values and table format:
[`reference/task-format.md`](reference/task-format.md). Every set is built from the files in
`templates/`, so every set has the same shape:

| File | Use |
|---|---|
| `templates/task-set.json` | Frame of `00_tasks.json` (`meta` + `tasks`) |
| `templates/tasks/feature.json` | Task: new behavior, test first |
| `templates/tasks/bugfix.json` | Task: reproduce, root cause, regression test |
| `templates/tasks/chore.json` | Task: setup, config, refactor, docs |
| `templates/tasks/verify.json` | Last task of every set |
| `templates/AGENTS.md` | Folder `AGENTS.md` |
| `scripts/check_task_set.py` | Validator; `--fix` regenerates `AGENTS.md` |

## When to Use

- Creating a new task set under `.tasks/`.
- Adding a task or subtask to a set that already has `done`/`in_progress` work.
- Running a task: set `in_progress`, do it, then set the final status and write the result in `note`.

## Core Procedure

1. **Pick the folder**: run `ls .tasks`; `NN` = next free two-digit number, `<name>` English snake_case. The folder name must match `NN_snake_case` even when the set is written outside `.tasks/`.
   Never renumber or delete an existing folder. Get the date from `date +%F`.
2. **Read the code the tasks touch** (`ls`/`grep`). Every path in a `prompt` must exist, or be a new
   file marked "create" whose parent folder exists; every command must be one you checked. If the code
   shows the goal is already met or the bug is already fixed, stop and tell the user instead of
   writing the set.
3. **Build `00_tasks.json`** from `templates/task-set.json`: for each unit of work copy the matching
   block from `templates/tasks/`, renumber `T0NN`, and replace every `{{...}}` with real values.
   Add or drop subtasks as the work needs (2–5 per task, one checkable outcome each); keep the
   `skills` value from the block. Finish with the `verify.json` block as the last task; add to its `prompt` the command that covers the changed area if `make test` does not.
4. **Generate `AGENTS.md` (never by hand) and validate: `python3 <skill dir>/scripts/check_task_set.py .tasks/NN_<name> --fix`,
   then run it again without `--fix`.** It must print `OK`.
5. If `00_tasks.json` already exists, add or edit only the task or subtask asked for; insert new
   work before the verify task, renumber only that verify task's id.

## Running and Updating Tasks

1. Set the task or subtask `in_progress` before starting.
2. Check the result against `expect`.
3. Set `done` and write the result in `note` (what was done, numbers or evidence, hints for the next
   task). On `failed` or `skipped`, write the reason in `note`.
4. When every subtask is `done` or `skipped`, set the task `done` and summarize in its `note`.
5. Edit only the task or subtask in hand, then run `python3 <skill dir>/scripts/check_task_set.py .tasks/NN_<name> --fix`.

## Quick Reference

| Question | Answer |
|---|---|
| Waves, `01_status.json`, per-app folders? | Not used — do not create them |
| Add to a set with progress? | Add only the new task or subtask; leave the rest byte-for-byte |
| Where does a result go? | The `note` of the task or subtask that produced it |
| A task has no subtasks? | Allowed for a single-step task (the verify block): `prompt`/`expect` on the task itself, never together with subtasks |
| Which `skills` value? | Keep the one in the template block; do not invent or combine |

## Common Mistakes

- Rewriting a whole `00_tasks.json` to add one item — wipes status and notes on the rest.
- Hand-editing `AGENTS.md` outside regeneration — the table drifts from `00_tasks.json`.
- Setting `done` without writing `note`, or without checking `expect`.
- Leaving a `{{placeholder}}` or `T0NN` in the file, or a path in a `prompt` that was neither checked nor marked "create".
- Skipping the validator.
- Using a status outside `pending / in_progress / done / failed / skipped`.
- Setting a task `done` while a subtask is not `done` or `skipped`.
