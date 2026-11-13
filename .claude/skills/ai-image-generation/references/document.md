# Document the image system, and improve Cobra

Write or refresh `AI-IMAGE-GENERATION.md` and its sidecar `style-lock.json` in a repo's Cobra agent, the way impeccable's `document` writes `DESIGN.md` and `design.json`. Run it in two cases: **scan** (the document is missing or the design system changed) and **improve** (the ledger holds new notes).

Locations (relative to the repo root): `.physarum/ai-image-generate/cobra-agent/` holds `AI-IMAGE-GENERATION.md`, `style-lock.json`, `ledger/index.json`, `series/`, `scripts/check.mjs`. The design system source is `DESIGN.md`; product truth is `PRODUCT.md`.

## Roles

| File | Role | Wins on conflict |
|---|---|---|
| `DESIGN.md` | UI design system | over both |
| `AI-IMAGE-GENERATION.md` | normative image rules, named rules, Known failures; frontmatter lists token **names** only | over the sidecar |
| `style-lock.json` | sidecar the scripts read: hex values, locked blocks, `negative_prompt_base` | - |

Hex values live in `style-lock.json` only; the document never repeats them.

## Scan

1. **Read** `DESIGN.md` (front matter colors, Overview, Elevation & Depth, Shapes, Typography, Do's and Don'ts) and `PRODUCT.md` (Evidence on Hand, Product Principles). Done when you can name the two hues, the depth rule, the bloom rule, the mark rules and the evidence constraints.
2. **Diff the sidecar.** For each palette token in `style-lock.json`, find its value in `DESIGN.md`. Done when every token is classed `same`, `changed` (new value), `new` or `removed`.
3. **Show the owner the diff** (palette changes, new or removed rules) and ask: refresh, overwrite or merge. An existing `AI-IMAGE-GENERATION.md` is never overwritten silently.
4. **Write** both files after the owner agrees. Keep the document's eight sections in this order: Overview, Palette, Type in images, Composition, Depth & Atmosphere, Shapes & Marks, Series & Consistency, Do's and Don'ts; then Known failures and Improvement loop. Omit a section only when `DESIGN.md` has nothing for it. Frontmatter `palette` equals the sidecar's palette keys.
5. **Verify** with `node .physarum/ai-image-generate/cobra-agent/scripts/check.mjs` until `✓ OK`. A palette change makes existing superprompts fail the hex check; list those superprompts for the owner instead of editing them silently.

Carry into the document only what constrains images: an Overview voice taken from `DESIGN.md`, the rules that bind marks, depth and evidence. Page layout and UI components do not belong.

## Improve

1. **Collect** — read every ledger entry whose `notes` defect no `fail-` row cites yet. An owner remark that is not in the ledger is first recorded, with the owner's agreement, as a review entry (`rev-NNN-<gen-id>`, fields `of`, `date`, `notes`). Done when every defect names a `gen-…` or `rev-…` entry.
2. **Merge** — a defect that matches a `Known failures` row adds its entry to that row's `Seen in`; a new defect becomes a row `fail-NNN` with Status `open`. Done when each defect has a row.
3. **Propose** — for each `open` row, state the smallest system change: one `negative_prompt_base` entry, one sentence in a series `layout`, one rule line in the document. List the superprompts that must change with it (a new base negative reaches every superprompt). Set Status `proposed` and show the diff. Done when the owner can read each change next to its evidence.
4. **Apply** — only after the owner agrees: edit the files (system files and the superprompts listed in step 3), set Status `applied`, run `check.mjs` to `✓ OK`. Never edit ledger entries or approved images.
5. **Verify** — after the next generation that exercises the change, set Status `verified` and write `verified by gen-…` in the row's System change cell. That generation follows Cobra's normal procedure (`cobra.generate`: anchor rules, estimate, the owner's agreement); improve never starts a run by itself. Until then `applied` means the change exists, not that it works.

A rule earns a place only from evidence in the ledger or from `DESIGN.md`/`PRODUCT.md`; a guess does not become a rule.

## Common mistakes

| Mistake | Fix |
|---|---|
| Hex values copied into the document | Names only in frontmatter; values in the sidecar |
| Document and sidecar disagree on palette | `check.mjs` reports it; fix the sidecar from `DESIGN.md` |
| A rule added with no ledger entry behind it | Cite a `gen-…` or `rev-…` entry, or `DESIGN.md#section`, or leave it out |
| Status `applied` read as "verified" | `applied` means the change exists; `verified` needs a generation that confirms it |
