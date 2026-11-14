# Changelog — ai-image-generation

Một file duy nhất cho `skills/agentic-os/ai-image-generation/`, newest first. Prose tiếng Việt, thuật ngữ kỹ thuật giữ tiếng Anh.

## main@0cbf91c

- Local: `Local Overrides` thêm **Confirm first** (xác nhận model và prompt trước `belt app run`) và model mặc định Flare, vì nhánh không có Cobra không xác nhận và Quick Start (FLUX) lệch bảng model; ảnh yêu cầu trong repo coi là của repo, trừ khi user nói không ([SKILL.md](SKILL.md)).
- Local: **Cobra first**: có `.physarum/agents/ai-image-generate/cobra-agent/AGENTS.md` thì mọi ảnh đi qua Cobra và lưu ở `drafts/<series>/`; không có thì dùng Quick Start. Baseline: agent thấy `.physarum/` nhưng bỏ qua vì skill không trỏ tới.
- Local: thêm [references/document.md](references/document.md) (viết/làm mới `AI-IMAGE-GENERATION.md` và `style-lock.json`, cải tiến Cobra từ ledger); [references/superprompt.md](references/superprompt.md) bước 4 và 6 trỏ vào đường dẫn và ledger của Cobra.
- Local: thêm 9 eval case và 4 trigger case cho các nhánh superprompt, reference image, Cobra first, improve và document ([evals/](evals/)).
- Local: thêm **superprompt JSON** và **reference image**: [references/superprompt.md](references/superprompt.md), [references/reference-images.md](references/reference-images.md), `scripts/validate-superprompt.mjs` (không dependency, port từ `BluebagAI/skills` `superimage-generator`), ví dụ `references/examples/physarum-cover.json`; `description` thêm trigger `superprompt, json prompt, reference image`. Baseline: agent tự bịa field, validate bằng `json.tool`, ghi `16:9` trong prompt thay vì `width`/`height`.
- Local: `SKILL.md` từng đặt lại nguyên văn upstream và chuyển rule local sang [AGENTS.md](AGENTS.md) mục `Local rules`; khối `Local Overrides` đã quay lại ở các mục trên.
- Initial release: vendored từ `inference-sh/skills` (commit `0cbf91c`, pin trong `../agentic-os-lock.json`), sinh ảnh AI qua `belt app run` với bảng App ID ở [SKILL.md](SKILL.md); rule chính: xác nhận model và prompt trước khi chạy (tốn credit); DỪNG khi chưa có `belt` hoặc chưa `belt login`, không ghi đè file có sẵn ([AGENTS.md](AGENTS.md)).
