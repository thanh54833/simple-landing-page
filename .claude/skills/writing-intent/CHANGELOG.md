# Changelog — writing-intent

Một file duy nhất cho `skills/agentic-os/writing-intent/`, newest first. Heading đầu giữ cùng version với `../agentic-os-lock.json`. Prose tiếng Việt, thuật ngữ kỹ thuật giữ tiếng Anh.

## local-2026-11-10

- Thêm `evals/evals.json` (9 test case) và `evals/triggers.json` (10 trigger, 5 negative).
- Đổi mã lane cho liên tục và tăng dần theo rủi ro: T0 Tiny/Quick, T1 Feature, T2 Hotfix/Debug, T3 Architecture (cũ: T2 Feature, T3 Hotfix, T4 Architecture; T1 bị bỏ khi gộp Tiny/Quick). Áp cho `writing-intent`, `writing-adr`, `/implement`, `/verify` và các dòng `Class:`/`Signals:` của intent, spec, plan đã có.
- Gộp Tiny và Quick thành một lane T0 Tiny/Quick: `[/intent →] /implement` → `/verify` → `/ship`. `intent.md` chỉ còn là tuỳ chọn (ngắn); không có intent thì `/implement` nhận mô tả từ chat. Bảng Classification chỉ còn một row T0 (bỏ T1); cần tiêu chí chấp nhận mới hoặc chạm hơn 1–2 file thì reclassify T2.
- Thêm lane T0 Tiny: có `intent.md` ngắn rồi `/implement <intent>` → `/verify` → `/ship`, không spec/plan. Bảng Classification tách T0 Tiny (không đổi hành vi, 1–2 file) khỏi T1 Quick/Bounded (vẫn không cần intent); Tiny hóa ra đổi hành vi thì reclassify T2 ở `/implement`.
- Hotfix (T3) bỏ intent: lane là `/debug` → `/verify` → `/ship`, `/debug` ghi record vào `docs/physarum/hotfixes/`. Row T3 trong bảng Classification giờ là "No intent needed" (như T0/T1); `Class` chỉ còn T2/T4; T3 cần đổi schema/auth/contract thì reclassify T4 ở `/debug`.

## local-2026-10-09

- Initial self-built release: capture idea/ticket/alert thành `intent.md` trước design.
- Analyst questions one-at-a-time + bảng Classification T2/T3/T4 (nguồn `00_sdlc_docs/07_*` §6).
- Template `YYYY-MM-DD-<slug>-intent.md` (Problem, Outcome, Users, Constraints, Out of scope, Open questions, Classification); DỪNG ở `Status: draft`, không design.
- Bounded fix (flag, endpoint nhỏ, one-file fix) thì khỏi intent.
- Thêm `AGENTS.md` rule guide + `CHANGELOG.md` theo mẫu `blader/humanizer`.
