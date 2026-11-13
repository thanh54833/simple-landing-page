# Generation Rules — exact formulas

Precise mechanical rules for hand-building a group's `.tasks/01_migration/` files. Wording
(`skills`/`prompt`/`expect`) always comes from the 3 template files under
`00_migration/02_template/01_tasks/` — never invent wording here.

## 1. Inputs

- `.meta/00_projects.json` → `root.01_origin[]`, find the entry whose `name == <GROUP>`. Its
  `projects[]` is the list to classify.
- Each project has: `name`, `type` (`api` / `worker` / `web` / other, e.g. `database` — ignore
  other types entirely, no task, no warning), `path` (origin-repo-relative path), and
  `metadata.origin.platform` (may be absent).
- 3 mandatory templates: `00_tasks_api.json`, `00_tasks_web.json` (each a flat
  `{"T001": {skills, prompt, expect}, "T002": {...}, "T003": {...}}`), `00_tasks_qa.json` (two
  variants, `"default"` and `"worker"`, each shaped like the above). If any file is missing, or
  any is missing a T001–T003 key or a `skills`/`prompt`/`expect` field, stop — don't guess
  content. That directory also holds a 4th file, `00_tasks_aie.json` — a legacy leftover from the
  dropped `/init-deep` + documentation phase; it is **not** one of the 3 mandatory templates and
  must be ignored.

## 2. Classify apps (per group)

A project is **known** (eligible for a task) if:
- `type` is `api`/`worker`/`web`, AND
- `metadata.origin.platform` is present and not `"Unknown"`, **or** it's exactly `"Unknown"` but
  a local folder already exists at `01_origin/<GROUP>/<path>` or `02_target/<GROUP>/apps/<name>`.

Split known projects into:
- **BE** = `type` in (`api`, `worker`)
- **FE** = `type == "web"`

Any `api`/`worker`/`web` project that fails the known check → skip, no task generated (optionally
note why: no platform info at all, vs. platform `"Unknown"` with no local folder yet).

## 3. Plan folders (contiguous, only categories present, fixed order api → web → qa)

```
n = 0
if BE not empty:  folder "{n:02d}_tasks_api" ; n += 1
if FE not empty:  folder "{n:02d}_tasks_web" ; n += 1
if BE or FE:      folder "{n:02d}_tasks_qa"  ; n += 1
```
Never renumber a folder that already exists on disk just because the category composition
changed — only assign numbers when creating folders that don't exist yet.

**Edge case — first app of a brand-new category for an already-existing group**: this happens
whenever a group currently has, say, only `00_tasks_api` + `01_tasks_qa`, and its first FE app is
added. Pure api→web→qa order says the new `web` folder should be `01` — but `01` is already
`tasks_qa` on disk. Do **not** renumber `tasks_qa` to make room, and do **not** invent an ad-hoc
number (e.g. skipping to `02`, or reusing `01` alongside `qa`) — this skill has no default for
that collision. Stop and ask the user how they want it resolved.

## 4. Wave keys

`SUFFIX(name)` = uppercase `name`, every run of non-alphanumeric characters collapsed to a single
`_`, leading/trailing `_` trimmed. E.g. `alphagen-admin-api` → `ALPHAGEN_ADMIN_API`.

- `NN_tasks_api` / `NN_tasks_web`: exactly 1 project in that category → unsuffixed
  `WAVE_01_BE` / `WAVE_01_FE`. More than 1 → `WAVE_{i:02d}_{BE|FE}_{SUFFIX(name)}`, `i` = 1..N in
  the project's list order.
- `NN_tasks_qa`: **always** suffixed, even with exactly 1 app: `WAVE_QA_01_{SUFFIX(name)}`. With
  multiple apps, number sequentially **across BE and FE combined, BE apps first then FE apps, in
  list order** — QA numbering does not restart per category. `is_worker` = true only for
  `type == "worker"` BE apps (FE apps are always the `"default"` QA variant).

  "List order" everywhere above means: the order the *known* apps of that category appear in
  `.meta/00_projects.json`'s `projects[]` for this group, after the §2 filter — never re-sort
  alphabetically, by `name`, or by `path`. For QA, that means BE's own `projects[]` order first
  (all BE apps), then FE's own `projects[]` order (all FE apps) — the two halves are concatenated,
  not interleaved.

## 5. Per-task fields (`skills`, `monorepo`, `source_dir`, `target_dir`, `prompt`, `expect`, `status`)

`<app-name>` is always the project entry's **`name`** field (e.g. `alphagen-admin-api`) — never
its `path` field. `path` is the origin-repo-relative path (e.g. `apps/cci.api.alphagen-admin`) and
is used *only* for the local-folder-exists fallback check in §2; the actual `apps/` folder under
`02_target/<GROUP>/` is always named after `name`.

Let `d = 02_target/<GROUP>/apps/<app-name>` and `app_path = apps/<app-name>`. Placeholders
`{group}`, `{app}`, `{app_path}` are substituted into the template's `prompt`/`expect` text via
plain string `.format()` (fail loudly if a template uses an unsupported placeholder — don't
silently leave literal `{...}` in the output).

**api / web waves** — `source_dir` is `d` for all 3 tasks; only `target_dir` changes:

| Task | source_dir | target_dir |
|---|---|---|
| T001 | `d` | `d` |
| T002 | `d` | `d/tests` |
| T003 | `d` | `02_target/<GROUP>/.tasks/01_migration/<THIS_FOLDER>/01_status.json` |

**qa waves** — T001's `source_dir` is still per-app (`d`, same app the wave is for); everything
downstream of that is a **group-level shared** dir, not per-app — every QA wave in the folder
writes T001's plan into, and reads T002's input from, the *same* `tests/plan` and `tests` dirs
(apps are differentiated by content/filenames written there, not by a per-app path):

| Task | source_dir | target_dir |
|---|---|---|
| T001 | `d` (per-app) | `02_target/<GROUP>/tests/plan` (shared) |
| T002 | `02_target/<GROUP>/tests/plan` (shared) | `02_target/<GROUP>/tests` (shared) |
| T003 | `02_target/<GROUP>/tests` (shared) | `02_target/<GROUP>/.tasks/01_migration/<THIS_FOLDER>/01_status.json` |

`monorepo` = `<GROUP>` on every task. `status` = `"pending"` on every newly-added task — never set
anything but `"pending"` for a task you are creating fresh, even if you believe the work is
already done elsewhere.

**Unknown-platform note**: if `metadata.origin.platform == "Unknown"` for that app, prepend this
exact text to T001's rendered prompt (before the rest of the prompt, same paragraph break):

```
⚠️ CHƯA XÁC ĐỊNH ĐƯỢC PLATFORM (metadata.origin.platform = "Unknown"): kiểm tra lại
source_dir bên dưới TRƯỚC KHI làm bất cứ điều gì — nhiều khả năng source_dir chỉ có file
scaffold (README/.gitignore) chứ chưa có code thật, hoặc code nằm ở branch/repo khác. Nếu
source_dir thực sự trống, DỪNG LẠI và báo cáo cho người phụ trách repo nguồn thay vì tiếp
tục migrate.

```

## 6. `01_status.json`

If the file doesn't already exist for a folder, create it as a literal **empty file** (0 bytes) —
not `{}`. Never overwrite one that already has content.

## 7. `AGENTS.md` — central vs. stub, and when to refresh

- **Central folder** = whichever folder name sorts alphabetically first among all folders that
  currently have a `00_tasks.json` for this group (i.e. the lowest `NN`). It gets the full
  operating doc (see `agents-md-templates.md`, central template) with a **Current State** section
  built by concatenating, for each folder in name-sorted order: a `### <folder_name>` heading,
  one blank line, then that folder's wave table (see below) — no other text in between.
- Every other folder gets the stub template (same reference file) with only its own wave table.
- Whenever **any** folder's `00_tasks.json` changes (task added, status updated, whole new folder
  created), regenerate `AGENTS.md` for **every** folder in that group from whatever is currently on
  disk — `AGENTS.md` is a derived doc, always safe to fully rewrite, unlike `00_tasks.json` /
  `01_status.json` which hold real progress and must never be blindly regenerated.
- A folder found on disk that no longer matches the current project list (e.g. an app was removed
  from `.meta/00_projects.json`) is never auto-deleted — leave it, still refresh its `AGENTS.md`.

### Wave table (used inside both templates)

Columns: `Wave | Module | Tasks | Status`.

- **Module** = basename of T001's `source_dir` for that wave (in every real case this is the app
  name, e.g. `alphagen-admin-api`).
- **Tasks** = comma-joined `T00N (label)`, in task-id order, where `label` is picked from the
  task's `skills` string (case-insensitive substring match, first match wins):
  `verify-complete`→`verify`, `api-planning`→`plan`, `qa-implement`→`implement`,
  `testing`→`tests`, `dotnet-migration`→`migrate`, `db-docs`→`docs`, else `task`.
- **Status** = aggregate of that wave's task statuses (`done`/`completed` both count as done),
  checked in this order:
  1. any task `failed` → `❌ failed (needs attention)` — takes priority over every other case, so
     a wave stuck waiting on a user decision never gets mistaken for one still progressing
     normally.
  2. else all tasks `done`/`completed`/`skipped` → `✅ done`.
  3. else all `pending` → `⏳ pending`.
  4. else → `🔄 in progress (X/Y done)` where X = count done (`done`/`completed`/`skipped`),
     Y = total tasks.
