# Guide for agents — pack rea

## OVERVIEW
Investigation skills for shipped artifacts and CI/tooling, sourced from the REA repo (`morluto/rea`): changelog prep, CI audit, tool design, reverse engineering.

## WHERE TO LOOK
| Task | Location | Notes |
|------|----------|-------|
| Release notes + contributor thanks | `rea-changelog-update/` | pins history via release-please manifest; prepares only, never publishes |
| CI/test-suite audit | `rea-ci-tests-audit/` | evidence-backed; notes go to /tmp, not tree |
| Tool/contract design | `rea-tool-design/` | boundary + Evidence semantics proposal |
| Binary/firmware/package analysis | `reverse-engineer-anything/` | needs REA MCP/providers; skip for plain source analysis |
| Shared REA references | `reverse-engineer-anything/references/`, `rea-ci-tests-audit/references/` | connection/recovery, evidence workflows |

## CONVENTIONS
- Written against REA repo paths (`../../../docs/*`, `scripts/release-notes.mjs`, `morluto/rea`) — resolve those against the target repo under investigation, not this factory.
- Investigation alone never authorizes edits/push/merge; keep the scope the user gave.

## ANTI-PATTERNS
- Don't run REA readiness/setup on ordinary source repos — normal repo tools suffice.
- Don't guess contributor identities in changelogs; preserve unknowns (`user: null`).
- Don't rerun full suites after doc-only edits; don't rebuild unchanged complete suites.
