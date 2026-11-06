# Changelog — .omo

File tổng cho toàn bộ `.omo/` (oh-my-openagent state + model config), newest first.
Heading theo ngày (`## YYYY-MM-DD`) vì config không pin version trong lock như skill.
`run-continuation/` là lịch sử hội thoại — không ghi ở đây.

## 2026-10-30

- Initial changelog: tổng hợp hiện trạng `omo.jsonc` — `categories` (10: `quick`, `unspecified-low/high`, `ultrabrain`, `visual-engineering`, `artistry`, `writing`, `deep-low/high`, `architect`) + `agents` (`explore`, `librarian`, `plan-consultant`, `plan-reviewer`) + `[opencode]` overlay (11 agents incl. `sisyphus`, `oracle`, `metis`, `momus`) + `_migrations` (`2026-08-reasoning-unification`, `2026-07-opencode-config-unification`).
- Mọi model pinned `opencode-go/muse-spark-1.3-contributor`; `reasoning: high` khi temperature ≤ 0.3, còn lại `medium`. Mirror `categories`/`agents` với `.opencode/oh-my-openagent.json` — đổi luôn cả hai cùng lúc.
- `omo.jsonc.bak.*` + `migration-backup-*/` là backup, `run-continuation/*.json` là transcript untracked — không sửa, không xóa khi chưa hỏi.
- Quy ước: không suy project fact từ `run-continuation/`. Cách update file này: thêm bullet newest-first dưới `## YYYY-MM-DD` khi đổi model/reasoning/thêm category/agent (ghi tên + giá trị mới + lý do).

## Cách update changelog

- Đổi model/reasoning: 1 bullet (category/agent nào + giá trị mới).
- Thêm/xóa category/agent: 1 bullet (tên + mirror `.opencode/oh-my-openagent.json` đã đổi kèm chưa).
- Không ghi backup/transcript mới đến — đó là state, không phải thay đổi có chủ ý.
