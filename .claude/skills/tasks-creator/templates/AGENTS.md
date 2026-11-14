# Task set: {{NN_name}}

{{meta.goal}}. Source of truth: `00_tasks.json` (tasks -> subtasks).

## How to run

1. Pick the first task or subtask that is `pending`; set it to `in_progress`.
2. Do it, check the result against its `expect`.
3. Set `status` to `done` (or `failed` / `skipped` with the reason) and write the result into `note`.
4. When all subtasks of a task are `done`, set the task `done` and summarize in its `note`.
5. Edit only the task you are working on; refresh the table below.

## Current State

| Task | Subtask | Title | Status |
|------|---------|-------|--------|
{{table rows: see reference/task-format.md}}

## Rules

- Edit only the item you are working on; never rewrite other tasks.
- Status values: pending, in_progress, done, failed, skipped.
