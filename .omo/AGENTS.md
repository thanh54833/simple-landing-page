# Guide for agents — oh-my-openagent state

## OVERVIEW
Runtime state and model config for the OMO runner. Read the config if you must; do not reason from the history.

## WHAT IS WHAT
| Path | Role | Touch? |
|------|------|--------|
| `omo.jsonc` | model/category map; mirrors `.opencode/oh-my-openagent.json` and adds an `[opencode]` overlay + `_migrations` | yes, both files together |
| `omo.jsonc.bak.*` | timestamped backups from earlier edits | no |
| `migration-backup-*/` | previous `oh-my-openagent.json` before migration | no |
| `run-continuation/*.json` | per-session continuation transcripts (one per session; new ones arrive untracked) | no |
| `CHANGELOG.md` | root log: model/category/agent changes, newest-first per date | yes, khi đổi `omo.jsonc` |

## CONVENTIONS
- Everything is pinned to `opencode-go/deepseek-v4.1-flash`; `reasoning: high` where temperature ≤ 0.3, otherwise `medium`.
- Categories (`quick`, `deep-high`, `writing`, `architect`, …) and agents (`sisyphus`, `explore`, `librarian`, …) are the runner's routing vocabulary — reuse the existing names.
- Cách update changelog: thêm bullet newest-first dưới `## YYYY-MM-DD` trong `CHANGELOG.md` khi đổi model/reasoning/category/agent; chi tiết xem cuối file đó.

## ANTI-PATTERNS
- Don't grep `run-continuation/` for project facts — it is conversation history, not documentation.
- Don't delete backups or transcripts to "clean up" without asking.
- Don't put project rules here; they belong in `AGENTS.md` files.
