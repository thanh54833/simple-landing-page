---
description: Redesign a named component, page, or sheet inside the existing design system via the impeccable skill
argument-hint: <target and optional direction, e.g. "sync-panel" | "repo-head layout" | "/repository/1 header">
---

## User Input

```text
$ARGUMENTS
```

1. Treat the User Input as `<target> [direction]`. A URL in it names the route (its path, no host); a DOM path (`#root > … > div.skills-panel`) names the element inside that route's page, by its last class. Backend-only or non-UI input → say so and STOP. Empty → ask which component, page, or sheet, and what feels wrong about it.
2. Resolve the target to source files, first match wins, and state the files in one line so the user can correct them:
   - a file path;
   - a CSS selector or class (`aside.sync-panel`, `.repo-head`) → grep `apps/web/src` for the class, take the component that renders it plus its rules in `index.css`;
   - a route (`/repository/1`) → the page component that route renders; then the single element the user named, not the whole page;
   - a component or sheet name → its file in `apps/web/src`.
   Nothing resolves → list the nearest candidates and ask.
3. Read `.agents/skills/agentic-os/impeccable/SKILL.md` in full and follow its `Local Overrides`; run its context step with `--target <file>`. Treat this as a refinement inside the committed world: `PRODUCT.md` Brand Commitments and `DESIGN.md` are binding, so reuse existing tokens and component grammar; add no hue, token, shadow, or second decorative system. A redesign keeps behavior, copy, accessible names, and the tests that pin them; it replaces layout, hierarchy, and treatment. A spec in `docs/physarum/specs/` that names this target and has `## Design` is the brief and the redesign builds it (Build stage of `impeccable.md`); a change that departs from it goes through `/update-spec` first. Route a leftover direction word (`bolder`, `layout`, `clarify`, `adapt`…) to its `reference/<name>.md`; otherwise load `reference/layout.md`. A reference that is missing from the vendored folder follows the Missing-reference rule of `impeccable.md`.
4. Look before editing. The app must answer on `http://localhost:3000` (start `make dev` when it does not; on macOS free a busy `:3000` by hand first). Screenshot the target at 1440px and 390px wide in every state it can reach (empty, loading, error, long content), then name the shipped pattern in `DESIGN.md` or `index.css` that the result will mirror, and reuse its classes and tokens. Record `git rev-parse HEAD` and `git status --short` before editing: files already modified are not yours, and "the base commit" below is that HEAD.
5. Pin behavior. Grep `apps/web/tests` for the target's names and list the roles, accessible names, and text the tests assert; the redesign leaves them intact.
6. Build in one pass, then verify once, batched:
   - `impeccable detect --json <changed files>` must return no findings;
   - `cd apps/web && npm run build`, the target's vitest file, then the full web suite once (Node 22 if the default Node fails on `undici`);
   - one visual round at 1440px and 390px over every state named in the `Look before editing` step, all fixes in one batch, at most one confirming round.
   Report failures as they are; a failure that also occurs without your diff is pre-existing, so run the same test at the base commit before saying so.
7. Keep the tree clean. Save screenshots with viewport shots under `.playwright-mcp/` (an element-targeted shot clicks the page). `.playwright-mcp/` holds tracked files: delete only files you created, never the folder. Revert `apps/web/tsconfig.tsbuildinfo` when the build dirtied it.
8. STOP with a short report: what changed, files touched, build/test result, and what was not visually checked. A new reusable pattern → suggest `/impeccable document`.
