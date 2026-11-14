# Task set: 01_init_project

Initialize agentic-os-core on a fresh machine: toolchain, generated agent/MCP config, dependencies, green tests, and a running dev stack. Source of truth: `00_tasks.json` (tasks -> subtasks).

## How to run

1. Pick the first task or subtask that is `pending`; set it to `in_progress`.
2. Do it, check the result against its `expect`.
3. Set `status` to `done` (or `failed` / `skipped` with the reason) and write the result into `note`.
4. When all subtasks of a task are `done`, set the task `done` and summarize in its `note`.
5. Edit only the task you are working on; refresh the table below.

## Current State

| Task | Subtask | Title | Status |
|------|---------|-------|--------|
| T001 | | Environment and generated config | pending |
| T001 | T001.1 | Read project docs and check toolchain | pending |
| T001 | T001.2 | Create .env | pending |
| T001 | T001.3 | Generate agent and MCP config | pending |
| T002 | | Dependencies, tests and build | pending |
| T002 | T002.1 | Install api and web dependencies | pending |
| T002 | T002.2 | Run tests | pending |
| T002 | T002.3 | Lint and build | pending |
| T003 | | Verify the dev stack | pending |
| T003 | T003.1 | Start the stack | pending |
| T003 | T003.2 | Check the web app | pending |
| T003 | T003.3 | Stop the stack | pending |

## Rules

- Edit only the item you are working on; never rewrite other tasks.
- Status values: pending, in_progress, done, failed, skipped.
