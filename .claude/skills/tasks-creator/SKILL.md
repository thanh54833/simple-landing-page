---
name: tasks-creator
description: Use when creating or updating a group's `.tasks/01_migration/` task set (00_tasks.json, AGENTS.md, 01_status.json) by hand — creating tasks for a new group, adding an app to a group that already has in-progress tasks, changing task prompt/skill wording shared across all groups, or unsure why folder numbering or a wave key looks the way it does.
---

# tasks-creator

## Overview

Builds `02_target/<group>/.tasks/01_migration/{00_tasks.json, AGENTS.md, 01_status.json}`
directly, by following the exact rules in this skill — reading `.meta/00_projects.json` plus the
template files, then writing the files yourself. This is the sole mechanism for **incremental**
changes that must preserve existing progress (new group from scratch, or adding one app to a
group that already has `done`/`in_progress` tasks) — it does not require running
`.tmp/scripts/generate_task.py` or `make target_generate_task` for that. A separate script
(see Quick Reference) covers from-scratch/full-`--all` regeneration instead; it is never safe to
run on a folder with real progress, so this skill is still the only safe path once any task has
moved past `pending`.
Never write `00_tasks.json`/`AGENTS.md` by copying another group's — it drifts from the rules and
loses the fields that don't apply to the new group.

## When to Use

- Creating the initial task set for a group that has apps under `apps/` + an entry in
  `.meta/00_projects.json` but no `.tasks/` yet.
- A group already has `.tasks/01_migration/` with `done`/`in_progress` tasks and a new app was
  added — you must add its wave without touching any existing task.
- Changing task wording/skills that should apply to every group, not just one.
- Out of scope: `02_target/.tasks/00_migration/*` — the root-level, hand-authored orchestration
  folders that sit one level up from any single group (e.g. `00_tasks_aie_init_agent/`,
  `01_tasks_aie_sync_docs/`, `03_task_fix_swagger/`, `04_tasks_run_group_waves/`). They look
  similar on the surface (`00_tasks.json` + `AGENTS.md` + `01_status.json`) but are keyed
  differently (by wave or by group, not derived from a single group's `apps/`) and are not built
  from `.meta/00_projects.json` + the 3 templates below — no rule in this skill covers producing
  or editing them.

## Core Procedure

1. **Read inputs**: the group's entry (`projects[]`) in `.meta/00_projects.json`, and all 3
   mandatory templates under `00_migration/02_template/01_tasks/`
   (`00_tasks_api.json`, `00_tasks_web.json`, `00_tasks_qa.json`). These templates are the only
   source of `skills`/`prompt`/`expect` wording — edit them (never a per-group file) to change
   wording for every group going forward; a per-group `00_tasks.json` edit never propagates back.
2. **Classify apps into BE / FE**, decide which of `NN_tasks_api` / `NN_tasks_web` / `NN_tasks_qa`
   apply, and number them contiguously. Exact classify + numbering rules:
   see [`reference/generation-rules.md`](reference/generation-rules.md) §2–3.
3. **Build each wave**: wave-key naming (incl. the `SUFFIX(name)` formula and the QA
   always-suffixed / combined-numbering rule) and the exact `source_dir`/`target_dir` per task —
   see [`reference/generation-rules.md`](reference/generation-rules.md) §4–5. Every newly-added
   task starts `"status": "pending"`.
4. **Write `00_tasks.json`** for any folder that doesn't already have one. If a folder already has
   a `00_tasks.json`, never rewrite the whole file — only add/edit the specific wave(s) you were
   asked to change (see "Adding an app" below). Ensure `01_status.json` exists (create as a
   literal **empty file**, not `{}`, if missing) — see §6.
5. **(Re)write every folder's `AGENTS.md` in the group**, whenever any folder's `00_tasks.json`
   changed — `AGENTS.md` is always fully derived and safe to overwrite, unlike `00_tasks.json` /
   `01_status.json`. Use the literal templates in
   [`reference/agents-md-templates.md`](reference/agents-md-templates.md): the lowest-numbered
   folder gets the central (full) doc, every other folder gets the stub. Wave-table rendering
   rules (module/label/status columns) are in `generation-rules.md` §7.

## Adding an App Without Losing Progress

The whole point of doing this by hand instead of a bulk regenerate: you touch only what changed.

1. Add the app to `.meta/00_projects.json` → that group's `projects[]` (keeps this document
   accurate for future edits).
2. Add **one new wave key** to the relevant `{folder}/00_tasks.json` (api or web) and to
   `NN_tasks_qa/00_tasks.json` — `skills` copied verbatim from the matching template, but
   `prompt`/`expect` rendered per §5 (placeholder substitution, plus the Unknown-platform note on
   T001 if that app's platform is `"Unknown"` — don't paste raw `{app}`/`{group}` placeholders
   into the file), `source_dir`/`target_dir` per §5, `"status": "pending"`. Leave every other wave
   in the file untouched, byte-for-byte. If the app is the first of a category that has no folder
   yet for this group, you're creating a new folder, not just a new wave — see the numbering
   edge case in `generation-rules.md` §3 before assigning it a number.
3. Refresh `AGENTS.md` for every folder in the group (step 5 above) so the Current State tables
   catch up — this never touches `00_tasks.json`/`01_status.json` content.

## Quick Reference

| Question | Answer |
|---|---|
| Hand-write `00_tasks.json` for a new group? | Yes — follow the Core Procedure; that's what this skill is for |
| Change one group's task wording only? | Not cleanly — templates are shared; editing `00_migration/02_template/01_tasks/*.json` changes future generation for every group, not just one |
| `00_tasks_aie/` folder? | Not covered by this skill (dropped from the pipeline along with `/init-deep` and the documentation phase) — don't create one |
| Templates folder shows 4 files, not 3? | `00_migration/02_template/01_tasks/` also has a leftover `00_tasks_aie.json` from before the aie phase was dropped — it's not one of the 3 mandatory templates; ignore it |
| `01_status.json` empty vs `{}`? | Starts as a literal empty file; only gets JSON once a wave's tasks are all `done` and verified |
| A folder on disk no longer matches `.meta/00_projects.json` | Never delete it — leave it, still refresh its `AGENTS.md` |
| `.tmp/scripts/generate_task.py` / `make target_generate_task` | A script exists that automates this same output for a from-scratch group or a full `--all` regen. It always fully (re)writes a folder's `00_tasks.json` from scratch or no-ops if one exists, and `--force` resets every task in that file to `pending` — never use it on a folder that has real progress; use the Core Procedure by hand instead |

## Common Mistakes

- Copying another group's `00_tasks.json` by hand as a starting point — re-derive from the
  templates + rules instead, field by field.
- Rewriting a whole folder's `00_tasks.json` to "add one app" — wipes status on every other wave.
- Hand-editing a folder's `AGENTS.md` content outside the Current State table — it's meant to be
  fully derived; any manual edit gets lost the next time it's refreshed.
- Editing a per-group `00_tasks.json` expecting it to change wording repo-wide — only
  `00_migration/02_template/01_tasks/*.json` is shared source.
- Treating every QA field as per-app — only T001's `source_dir` is per-app; its `target_dir` and
  all of T002's `source_dir`/`target_dir` are the *same* group-level `tests/plan` / `tests` dirs
  across every QA wave in the folder, not a per-app subfolder.
