# Changelog — commands

Một file duy nhất cho toàn bộ `.agents/.commands/`, newest first. Heading theo ngày (`## YYYY-MM-DD`). Prose tiếng Việt, thuật ngữ kỹ thuật giữ tiếng Anh.

## 2026-11-13

- Thêm `/img` (standalone): gọi skill `ai-image-generation`, skill chuyển sang Cobra (`.physarum/ai-image-generate/cobra-agent/`) để tạo, duyệt hoặc cải tiến ảnh theo design system. Từ đầu tiên là verb của Cobra (`generate`, `approve`, `improve`…), còn lại là brief gán vào series/slot; thiếu `cobra-agent/AGENTS.md` thì STOP. Evals ở `evals/img/`.

## 2026-11-12

- `/implement` bước 1: làm rõ nhánh T0 khi User Input rỗng và session chưa có plan/intent/spec thì lấy chính câu chat gọi command làm request (đủ điều kiện Tiny/Quick thì chạy trực tiếp, việc lớn hơn thì STOP gợi ý `/intent`). Khớp với `writing-intent` đã ghi "không intent thì `/implement` nhận mô tả từ chat"; không đổi số bước, không sửa `impeccable.md` (router frontend standalone, không có gate intent/plan/spec).
- Thêm `/save` (standalone): gọi skill `business-memory` (`reference/save.md`) để lưu decision, insight hoặc business rule đã chốt vào `docs/physarum/business-memory/`. Input là text tự do hoặc điều session vừa chốt; chưa chốt thì ghi `proposed`. Memory chưa khởi tạo thì STOP và gợi ý `reference/init.md`. Cập nhật `business-memory` AGENTS.md: skill nay có command. Verify chéo skill/command/persona: chốt `/save` gom mọi mục chưa lưu thành một gói, rule chưa chốt vào `open_questions`, id decision/insight đánh theo số file. Subagent dry-run 5 tình huống tìm thêm 5 chỗ hở, đã sửa trong `reference/save.md`: ngưỡng "đã chốt" vs ý nghiêng, lời owner làm evidence, `supersedes` dùng id đầy đủ và đề xuất `writing-adr` khi decision cũ gốc từ ADR, một lần dừng cho resolve + diff, quy tắc đặt tên topic và `br-XXX`.

## 2026-11-11

- `/spec` bước 5: sau khi user approve spec, hỏi một lần chạy lệnh nào tiếp theo, đưa đúng hai lựa chọn `/adr` và `/plan`, lệnh khuyến nghị đứng trước và gắn `(Recommended)` kèm một dòng lý do dẫn quyết định của user. Chọn khuyến nghị theo thang luật, khớp luật đầu tiên thắng: (1) user đã nói bỏ ADR → `/plan`; (2) `## Decisions` đã có outcome cho `/plan` đi tiếp (ADR accepted, "No ADR needed", "Deferred", hoặc dòng `ADR skipped by user`) và không còn ADR nào chưa accepted → `/plan`; (3) intent T3, spec ghi đổi kiến trúc, hoặc còn ADR chưa accepted → `/adr`; (4) còn lại → `/plan`. Mỗi khi user chọn `/plan` trên intent T3 hoặc spec đổi kiến trúc mà `## Decisions` chưa có outcome (kể cả khi luật 1 là luật khớp), ghi đúng dòng `ADR skipped by user` vào `## Decisions`. `/plan` bước 3 coi đúng dòng đó là một quyết định đã có và đi tiếp, nói rõ một dòng rằng ADR được bỏ qua. Không đổi số bước, không router nào cần sửa tham chiếu; cập nhật dòng `spec.md` và `plan.md` trong `AGENTS.md`.

## 2026-11-10

- Đổi mã lane cho liên tục và tăng dần theo rủi ro: T0 Tiny/Quick, T1 Feature, T2 Hotfix/Debug, T3 Architecture (cũ: T2 Feature, T3 Hotfix, T4 Architecture; T1 bị bỏ khi gộp Tiny/Quick). Áp cho `writing-intent`, `writing-adr`, `/implement`, `/verify` và các dòng `Class:`/`Signals:` của intent, spec, plan đã có.
- Gộp lane Tiny và Quick: `[/intent →] /implement` → `/verify` → `/ship`, intent tuỳ chọn. `/intent` bước 3: việc Tiny/Quick hỏi/ghi intent ngắn nếu user muốn, không thì nêu lane và dừng. `/implement` nhận intent `Class: T0` hoặc mô tả việc từ chat (việc lớn hơn thì STOP, gợi ý `/intent`); cần tiêu chí chấp nhận mới hoặc chạm hơn 1–2 file thì reclassify T2. `/verify` nhận thêm trường hợp không có artifact: kiểm diff của session. (dùng mã cũ; xem dòng đổi mã ở đầu mục này)
- Tiny lane: `/intent` → `/implement` → `/verify` → `/ship`. `/intent` bước 3: Tiny vẫn có intent ngắn. `/implement` nhận intent `Class: T0` thay plan, chạy thẳng trong session (không plan, không subagent, TDD khi có test), đổi hành vi thì reclassify T2. `/verify` nhận intent Tiny: chạy bộ test, diff không được thêm/đổi hành vi. `writing-intent`: bảng Classification có row T0 Tiny, `Class` là T0/T2/T4. (dùng mã cũ; xem dòng đổi mã ở đầu mục này)
- Hotfix lane mới: `/debug` → `/verify` → `/ship`, không còn intent/spec/plan. `/debug` thêm bước ghi record `docs/physarum/hotfixes/YYYY-MM-DD-<slug>.md` (Symptom, Root cause, Regression test đỏ rồi xanh, Fix, Verify), fix cần đổi schema/auth/contract thì STOP và đi `/intent`. `/verify` nhận plan hoặc hotfix record (bỏ ADR check và design evidence cho hotfix). `/plan` bỏ nhánh T3 (argument-hint, step 1–5). `/intent` bước 3: hotfix thì nói không cần intent và nêu lane. `writing-intent`: row T3 thành "No intent needed", `Class` chỉ còn T2/T4. (dùng mã cũ; xem dòng đổi mã ở đầu mục này)

- Audit chéo các router/skill (reviewer đọc nguội) và vá: (1) `/spec` giữ bước review của brainstorming cho tới khi `## Design` được ghi vào file spec đã lưu; (2) lệch `## Design` → `/update-spec` giờ có nhánh patch `## Design` rồi quay lại `/implement`; (3) `/implement` ghi `Evidence:` dưới task trong plan, controller chạy vòng visual, `/verify` thêm bước đọc `Evidence:`; (4) `impeccable.md`: scope check lên đầu, intent/spec path đi thẳng vào Spec/Build stage, override rõ cho `craft-floor` ở Spec stage, `Experience` không có mode reference, chiều rộng desktop 1440px / mobile 390px; (5) trỏ theo tên thay vì số bước, bỏ `polish`/`quieter`/`typeset` (không có trong impeccable đã vendor) khỏi ví dụ; (6) base commit = HEAD ghi trước khi sửa, kiểm diff bằng hunk thay vì `--stat`; (7) `AGENTS.md` ghi ngoại lệ cho luật "không procedure trong router" khi skill phía sau là vendored.

- Thêm `/enhance`: router standalone thin tới `impeccable` để tăng cường MỘT element được gọi tên (khác `/redesign` thay cả layout/phân cấp). Scope cố định lên đầu (neighbors/page/tokens không đổi, `git diff --stat` chỉ gồm component + CSS + test của target), direction word → `reference/<name>.md` (mặc định `bolder.md`), một nước đi chính + phần xung quanh lùi lại, hành vi mới phải hỏi một lần trước khi build. Viết độc lập, không phụ thuộc `redesign.md`: tự chứa các bước parse/resolve, look, pin, verify, clean (cố ý trùng với `redesign.md`, sửa lỗi chung thì sửa cả hai). Update `.commands/AGENTS.md` (row + standalone list).

- `/redesign`: nhận thêm URL và DOM path làm target; sửa step 3 bắt load `reference/polish.md` (file không có trong impeccable đã vendor) thành `reference/layout.md` + luật reference thiếu của `impeccable.md`; coi spec có `## Design` là brief. Thêm bước nhìn trước khi sửa (app chạy ở `:3000`, screenshot 1440px + 390px mọi state, chọn pattern đã ship để mirror), bước pin behavior (grep test của target), verify gọn một lượt (`impeccable detect`, build, vitest, một vòng visual), và bước giữ tree sạch (`.playwright-mcp/` có file tracked: không xoá cả folder; revert `tsconfig.tsbuildinfo`). Kiểm tra phạm vi (backend-only → STOP) chuyển lên step 1; đánh số lại 6 → 8 bước; không có router nào khác trỏ số bước của `/redesign`.

- Design contract cho UI: `impeccable.md` định nghĩa một lần mục `## Design` (Mode, Mirrors, Structure, Tokens, States, Responsive, Copy, Interaction/a11y, Acceptance checks) kèm spec stage và build stage. `/spec` thêm bước UI check: spec có UI thì chạy `/impeccable` để có `## Design` trước khi user approve. `/plan` chép `Copy` + `Acceptance checks` vào Global Constraints và gắn `Design:` cho từng UI task. `/implement` build + verify UI task theo `## Design` (detect, build, test, screenshot desktop + 390px từng state); lệch design thì STOP và đi qua `/update-spec`. `impeccable.md` thêm luật: reference thiếu trong folder vendored thì nói rõ và đi tiếp, không tự dựng lại nội dung.

- `/implement`: luôn hỏi method và workspace trong cùng một lượt, đặt option khuyến nghị lên đầu (`subagent-driven (Recommended)`, `current branch (Recommended)`), vẫn để user chọn. Lựa chọn workspace được truyền cho skill để không hỏi lại; trên `main`/`master` thì nêu rõ là commit vào default branch.

## 2026-11-07

- Thêm `/redesign`: router thin tới skill `impeccable` cho target do user chỉ định (component, page, sheet, selector, route) — resolve target → files, refine trong DESIGN.md (không thêm token/hue), giữ behavior + test, build + vitest, STOP với report. Update `.commands/AGENTS.md` (row + standalone list).

## 2026-10-30

- Session default input cho `/spec`, `/adr`, `/plan`, `/implement`, `/verify`, `/update-spec`: thứ tự User Input path → artifact gate trước vừa accept/approve/tạo/sửa trong session (mới nhất thắng; dùng luôn, nêu path một dòng) → mới list và hỏi. Approval đã có trong session thì không hỏi lại "reviewed and approved?". `/implement` cũng lấy method đã chọn ở `/plan`.
- Update `.commands/AGENTS.md`: thêm 2 convention tương ứng (wording giống hệt giữa các router).

## 2026-10-26

- Thêm `/update-spec`: router thin (resolve spec trong `docs/physarum/specs/` + check approve → invoke skill `update-spec` → STOP); scope mọi file spec, gỡ di sản `openspec list --json`.
- Update `.commands/AGENTS.md`: thêm row `update-spec` + standalone list (gate chain không đổi).
- Thêm `/debug`: router tới Superpowers `systematic-debugging` (4 phases, no fixes before Phase 1), kèm layer check vite proxy → FastAPI `:8000` cho dev stack của repo.

## 2026-10-10

- Initial changelog: tổng hợp hiện trạng 7 gates `intent → spec → adr → plan → implement → verify → ship`.
- Thêm `## TẠO COMMAND MỚI` vào `AGENTS.md` (guide: naming, frontmatter 2 field, body `$ARGUMENTS` + steps, fallback skill local, sync mirror, verify) + file `CHANGELOG.md` chung này.
