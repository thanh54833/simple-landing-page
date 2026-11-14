# Task format

## `00_tasks.json`

```json
{
  "meta": { "task_set": "NN_name", "name": "name", "goal": "...", "generated_at": "YYYY-MM-DD", "note": "..." },
  "tasks": {
    "T001": {
      "title": "...",
      "skills": "superpowers:verification-before-completion",
      "status": "pending",
      "note": "",
      "subtasks": {
        "T001.1": { "title": "...", "prompt": "...", "expect": "...", "status": "pending", "note": "" }
      }
    }
  }
}
```

- **Ids**: tasks `T001`, `T002`…; subtasks `T001.1`, `T001.2`… (prefix = parent id). Contiguous, never reused.
- **Task**: `title`, `skills` (skill names to load; empty string = follow `prompt`/`expect` directly),
  `status`, `note`, `subtasks`.
- **Subtask**: `title`, `prompt` (what to do), `expect` (definition of done, checkable), `status`, `note`.
- **Single-step task**: omits `subtasks` and carries `prompt` and `expect` itself. A task has subtasks or its own `prompt`/`expect`, never both.
- **Granularity**: 2–5 subtasks per task; each has one outcome that `expect` can check with a command or a file state.
- **`expect`**: names a command and its pass condition, or a file state. No "works correctly".
- **Last task**: the verify block (`templates/tasks/verify.json`), title contains "Verify".
- **`note`**: `""` when created. The agent fills it when the item finishes: result, evidence, hints
  for later tasks. `failed`/`skipped` must say why.
- Template placeholders are `{{...}}` and `T0NN`; none may remain in the file. A path in a `prompt` exists, or is a new file marked "create" whose parent folder exists.

## Status

`pending` → `in_progress` → `done` (or `failed` / `skipped`).

- `in_progress` → `done`: only after checking `expect`.
- `in_progress` → `failed`: `expect` not met; never leave `in_progress`, never set `done`; stop and ask the user.
- `pending` → `skipped`: deliberate, with a reason in `note`.
- A task is `done` only when all its subtasks are `done` (or `skipped`).
- An interrupted `in_progress` item counts as not finished: rerun it from the start.

## `AGENTS.md` table

In file order, each task row (Subtask column empty) is followed directly by its subtask rows. Never group all tasks first. `scripts/check_task_set.py --fix` renders it from `templates/AGENTS.md`; do not write it by hand.

The folder `AGENTS.md` is `templates/AGENTS.md` with the title, goal and table filled in by the script.
