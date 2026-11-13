---
description: Design, critique, audit, polish or improve a frontend interface via the impeccable skill
argument-hint: <sub-command and/or target, e.g. "critique apps/web" | "layout checkout form">
---

## User Input

```text
$ARGUMENTS
```

1. Backend-only or non-UI input → say so and STOP before anything else. Otherwise read `.agents/skills/agentic-os/impeccable/SKILL.md` in full. It is the source of truth; follow its `Local Overrides` (every `.agents/skills/impeccable/...` path reads as `.agents/skills/agentic-os/impeccable/...`; `<skill-base-dir>` = that folder).
2. Route the User Input per the skill:
   - First word matches a sub-command (`reference/<name>.md`, e.g. `adapt`, `animate`, `clarify`, `delight`, `layout`, `optimize`, `init`, `doctor`) → load that reference file and apply it to the rest of the input as the target.
   - An intent path or a spec path goes to the Spec stage or Build stage below, not to the design-brief branch.
   - Otherwise treat the whole input as the design brief and let the skill choose the reference files.
   - Empty input → list the available sub-commands from `reference/` and ask which one.
3. Run the launcher on Windows as `scripts/impeccable.cmd` (not the `sh` script). Do not edit anything under `impeccable/` — vendored. Repo rules for it live in this router (the skill cannot hold them); short skill-level overrides go in its `Local Overrides`.
4. **Missing reference.** If a `reference/<name>.md` that the skill or the User Input names is missing from the vendored folder, say so in one line and continue from `SKILL.md` plus the references that exist. Do not reconstruct its content from memory.
5. **Design contract** — the one definition `/spec`, `/plan`, `/implement` and `/verify` share; they point here by name and do not restate it. A UI spec carries a `## Design` section with exactly these slots, each holding a concrete value:
   - **Mode:** `Persuade`, `Operate`, `Read` or `Experience`, plus one line on why.
   - **Mirrors:** the shipped screen or `DESIGN.md` component this surface is built from, as a route or component name; or `none` with the reason no existing pattern fits.
   - **Structure:** the regions in reading order, each naming the `DESIGN.md` component it reuses. A component that does not exist yet is marked `new`, and `/impeccable extract` is suggested afterward.
   - **Tokens:** the roles used, by `DESIGN.md` token name (color, type step, radius, spacing), ending with the line "no new hue, token or shadow".
   - **States:** for every region, the empty, loading, error, long-content and edge-content appearance, one line each (edge content = the longest, shortest and odd-character values the data can hold).
   - **Responsive:** what changes at 1024px and up, 1023px and down, 767px and down, and 390px.
   - **Copy:** every user-visible string, verbatim.
   - **Interaction and a11y:** keyboard path, focus target, touch size, reduced-motion behavior.
   - **Acceptance checks:** observable assertions, each checkable in a screenshot, in computed style or in a test (for example "list row height 32px", "current row = wash + line + 2px gold rail").
6. **Spec stage** (input is an accepted intent or a spec path with no `## Design`): load PRODUCT.md and DESIGN.md through the skill's context step, screenshot the `Mirrors` screen in the running app when one exists, set the spatial thesis with `layout` and the mode reference (`mode-operate`, `mode-read` or `mode-persuade`; `Experience` has none, so use `layout` alone), then fill every slot. Read `craft-floor.md` here even though no code is edited (this stage overrides the skill's planning-only exemption) and redraw any region whose slot needs a pattern on its Refuse list. Write the result into the saved spec file as `## Design`. Do not edit product code at this stage.
7. **Build stage** (input is a spec or task that carries `## Design`): build exactly what it says — strings verbatim, components and tokens as named. Then verify once, batched: run `impeccable detect` on the changed UI files, run the project build and the target's tests, take desktop (1440px) and mobile (390px) screenshots of every state listed under `States`, and record each acceptance check with its evidence (a computed value, a test name, or a screenshot path) as an `Evidence:` list under the task in the plan file. A deviation is not made in code: STOP and run `/update-spec`, which patches `## Design`, then resume the build.
