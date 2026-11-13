# Guide for agents — ai-image-generation

File này giải thích cách sửa `ai-image-generation` mà không làm lệch upstream.
Mẫu theo `hallmark` `AGENTS.md`.

## What this skill contains

Sinh ảnh AI (text-to-image, image-to-image, inpainting, upscaling) qua `belt app run <app-id>` của inference.sh CLI, với bảng model (GPT-Image-2.5, FLUX, Gemini, Grok, Seedream, Reve…). `SKILL.md` vendored từ `inference-sh/skills` kèm khối `Local Overrides`; thêm local: tạo **superprompt JSON** (schema, validator, flatten), **reference image**, và **Cobra first** (trong repo có `.physarum/ai-image-generate/cobra-agent/`, mọi ảnh đi qua Cobra và lưu ở `drafts/`). `allowed-tools: Bash(belt *)`.

## Key files

- `SKILL.md` — upstream (commit `0cbf91c`) cộng khối `Local Overrides (factory-skills)` đầu file và 3 trigger local cuối `description`. Phần còn lại không sửa tay.
- `references/superprompt.md` — quy trình 6 bước, schema theo `prompt_type`, 7 nguyên tắc, flatten, tham số `width`/`height`. Phương pháp lấy từ `BluebagAI/skills` `superimage-generator`.
- `references/document.md` — quy trình viết/làm mới `AI-IMAGE-GENERATION.md` + `style-lock.json` (scan) và cải tiến Cobra từ ledger (improve), theo mẫu `document` của `impeccable`.
- `references/reference-images.md` — block `reference`, input `images`, giới hạn (logo/chữ nhỏ có thể lệch).
- `references/examples/physarum-cover.json` — ví dụ `product` + `vector` đã qua validator; đổi schema thì chạy lại.
- `scripts/validate-superprompt.mjs` — validator không dependency (upstream cần `zod`); exit 0 = VALID.
- `AGENTS.md` (file này) — rule guide cho agent sửa skill; không chứa danh sách model.
- `CHANGELOG.md` — release notes, newest first.
- `../agentic-os-lock.json` — pin `ai-image-generation` (`sourceType: github`, `source: inference-sh/skills`, `version: main@<sha7>`).

## Rules for changes

- **Vendored + local:** phần upstream của `SKILL.md` giữ nguyên. Chỉ `Local Overrides` và 3 trigger local (`superprompt`, `json prompt`, `reference image`) được sửa tay; local thắng upstream khi lệch, và mỗi lần đổi phải có note trong `CHANGELOG.md`. Rule hành vi (confirm, login, overwrite) vẫn ở `Local rules`, không nhét vào `SKILL.md`.
- **Cobra first:** điều kiện là file `.physarum/ai-image-generate/cobra-agent/AGENTS.md` tồn tại trong repo đang làm việc (skill được phân phối sang repo khác, nên không hardcode làm mặc định). Nội dung Cobra (style, ledger, thư mục ảnh) nằm ở `.physarum/`, không chép vào skill; skill chỉ trỏ tới và giữ quy trình trong `references/`.
- **Superprompt:** schema và danh sách enum trong `references/superprompt.md` và `scripts/validate-superprompt.mjs` phải khớp nhau; đổi một bên thì đổi bên kia và chạy lại ví dụ trong `references/examples/`.
- **Model table:** bảng App ID đổi theo upstream (thêm/bớt model). Cập nhật bằng sync, không sửa tay; `belt app list --category image` là nguồn thật.
- **Cost + data:** mọi lần `belt app run` tốn credit và gửi nội dung lên dịch vụ ngoài.
- **Upstream:** upstream không có tag; pin commit sha. Sync upstream = thay phần upstream của `SKILL.md`, giữ lại khối `Local Overrides` và 3 trigger local; `references/`, `scripts/` local không bị upstream ghi đè.
- **Version:** giữ cùng version ở `../agentic-os-lock.json` và heading đầu `CHANGELOG.md`. Sync upstream → bump lock cùng commit.
- **Compatibility:** instructions trung lập runtime (Claude Code, OpenCode, Orca là ví dụ).
- **Description:** frontmatter giữ upstream, chỉ thêm 3 trigger local ở cuối danh sách `Triggers`.
- **Checks:** đọc lại `SKILL.md`; verify frontmatter `name: ai-image-generation`; `node scripts/validate-superprompt.mjs --input references/examples/physarum-cover.json` ra `✓ VALID`; link tới `references/` resolve; chạy `make agents_sync` rồi `make agents_sync-check`.

## Local rules

Rule xác nhận trước khi chạy và model mặc định đã có một dòng trong `Local Overrides` của `SKILL.md` (để nhánh không có Cobra cũng xác nhận); các rule còn lại dưới đây không nằm trong `SKILL.md`, nên không tự nạp khi skill fire; evals kiểm hành vi tương ứng.

- Xác nhận model và prompt với user trước khi `belt app run` (tốn credit, gửi nội dung ra ngoài).
- Chưa có `belt`: hướng dẫn cài, không tự pipe script từ mạng vào shell; chưa đăng nhập: yêu cầu `belt login`.
- Không ghi đè file có sẵn trong repo; không tự chạy `npx skills add` trong mục Related Skills.

## Writing style

- Nội dung upstream giữ tiếng Anh như gốc; `AGENTS.md` và `CHANGELOG.md` viết tiếng Việt, thuật ngữ kỹ thuật giữ tiếng Anh.
- Lead bằng main point, câu ngắn, một term cho một item. Giữ nguyên identifier, command, app ID.
