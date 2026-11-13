---
name: evals
description: Use when creating evals/evals.json or evals/triggers.json for a self-built skill, when a skill was just tuned and needs a regression eval, or when asked "tạo/thêm/audit evals".
---

# Playbook — Evals cho một skill (chuẩn Grok)

## Overview

Mỗi skill self-built có 2 file eval trong `evals/`: `evals.json` kiểm tra **hành vi**, `triggers.json` kiểm tra **kích hoạt**. Template: `evals.template.json`, `triggers.template.json`. Checker: `check-evals.py` (cùng folder). **Core rule:** assertion phải cụ thể và kiểm tra được; "works correctly" là eval giả.

## When to use

- Skill mới → tạo cả 2 file.
- Vừa **TUNE** `SKILL.md` → thêm đúng 1 regression test mới vào `evals.json`.
- Phát hiện trigger phrase mới hoặc câu bị over-trigger → thêm vào `triggers.json`.
- Skill vendored → **DỪNG**, xem Gate. Viết skill/changelog → playbook `001_changelog`, không phải playbook này.

## Gate

```bash
python3 -c "import json;d=json.load(open('.agents/skills/agentic-os/agentic-os-lock.json'))['skills'];print({k:v['source'] for k,v in d.items()})"
```

| Skill | Điều kiện | Hành động |
|---|---|---|
| `skills/agentic-os/<skill>` | `source == "local"` | Tiếp tục |
| `source` khác `"local"` (vendored) | — | **DỪNG**, báo user, không tạo file |

Danh sách vendored đổi theo lock; luôn đọc lock, không dựa vào trí nhớ.

Ngoại lệ: user yêu cầu rõ evals cho skill vendored → làm, chỉ thêm `evals/`; không đụng `SKILL.md`, không thêm `CHANGELOG.md` (vendored dùng `Local Overrides`), và báo user rằng lần sync upstream có thể ghi đè.

## Steps

1. Qua Gate. Đọc `SKILL.md` của skill; liệt kê **3-5 use case thật** (happy path + failure mode chính + mỗi điểm DỪNG/Hard Gate).
2. `mkdir -p <skill>/evals`, copy 2 template, thay `ten-skill`.
3. `evals.json`: mỗi use case = 1 test case. `name` snake_case, `input` là đúng câu user sẽ nói, `assertions` theo công thức bên dưới. Tối thiểu 3 case, mỗi case khác biệt rõ (không copy assertion giữa các case).
4. `triggers.json`: ≥3 trigger, mỗi nhánh của `description` ("Fires on…") 1 positive, và **≥2-3 negative** lấy từ phần "NOT for" + các skill/gate lân cận (spec, plan, debug, commit).
5. Mỗi `evals.json` có cả "PHẢI làm" và "KHÔNG ĐƯỢC làm"; assertion nêu tool/script/file cụ thể khi có.
6. Chạy `check-evals.py` (Quick reference), sửa tới 0 error.
7. Ghi 1 dòng vào `CHANGELOG.md` của skill (playbook `001_changelog`). Chỉ bump lock nếu `SKILL.md` đổi.
8. Báo kết quả kèm output của checker.

## Công thức assertion

`[Hành động cụ thể] + [Điều kiện] + [Kết quả kiểm tra được]`

| Tốt | Tệ (bị loại) |
|---|---|
| `Calls opencode_project_list before creating session` | `Works correctly` |
| `Does NOT create session until project is confirmed` | `Handles the request properly` |
| `Creates evals/evals.json with 3+ test cases` | `Creates the necessary files` |
| `Preserves existing task statuses` | `Does the right thing` |
| `Reads INDEX.md first, then follows relevant wikilinks only` | `Uses the knowledge graph` |

Model đầy đủ: `skills/agentic-os/writing-adr/evals/`.

## Audit sau session (7 câu hỏi)

Với mọi skill đã dùng hoặc lẽ ra phải dùng. Câu YES → hành động; phần eval là Q5, Q6.

| # | Câu hỏi | Nếu YES |
|---|---|---|
| 1 | Instructions dẫn sai hoặc thiếu bước? | **TUNE** `SKILL.md` (rewrite section, không append) **+ regression eval (Q6)** |
| 2 | Học được thứ chưa document? | **GROW** `references/what-i-learned.md` |
| 3 | Giải quyết được vấn đề đáng lưu? | **GROW** `examples/` (request + solution + gotcha) |
| 4 | Viết code sẽ dùng lại? | **GROW** `scripts/` (extract + parameterize) |
| 5 | Phát hiện trigger phrase mới? | **GROW** `evals/triggers.json` |
| 6 | Phát hiện failure mode cần test? | **GROW** `evals/evals.json` (regression) |
| 7 | Skill làm mọi thứ tệ hơn hoặc vô dụng? | **RETIRE** (chuyển vào `_retired/`) |

Change Plan bắt buộc trước khi sửa:

```markdown
| Skill | Q# | Action | File | Change |
|-------|----|--------|------|--------|
| xxx   | 1  | TUNE   | SKILL.md | Thêm bước kiểm tra branch |
| xxx   | 6  | GROW   | evals/evals.json | Test: phải đọc file trước khi sửa |
```

Dấu hiệu audit tốt: mistake score giảm dần, nhiều Q2-Q3 hơn Q1, skill mới được extract từ pattern lặp 3 lần. Dấu hiệu tệ: cùng skill bị TUNE lặp lại, eval là stub, chỉ append note cuối `SKILL.md`.

## Quick reference

| Kiểm tra | Cách |
|---|---|
| Checker pass | `python3 .agents/playbooks/002_skills/01_evals/check-evals.py .agents/skills/agentic-os/<skill>` → `0 error`, exit 0 |
| JSON hợp lệ | checker đã parse; lỗi parse hiện là error |
| Còn stub/TODO | checker báo; hoặc `grep -n 'TODO\|ten-skill\|câu positive' <skill>/evals/*.json` → rỗng |
| Mirror không drift | `make agents_sync-check` → exit 0 (evals nằm trong folder skill, được mirror) |

Checker kiểm: ≥3 test case, có assertion, không stub/TODO/placeholder, không assertion chung chung trong blacklist, ≥3 trigger với ≥1 negative, `skill` khớp tên folder.

## Common mistakes

| Sai | Đúng |
|---|---|
| Assertion chung chung | Viết lại: hành động cụ thể + phủ định |
| Chỉ có positive trigger | Thêm ≥2-3 negative → tránh over-trigger |
| TUNE `SKILL.md` mà không thêm eval | Mỗi TUNE = 1 regression eval mới |
| Copy-paste assertion giữa các case | Mỗi case một edge case khác |
| Chỉ test happy path | Thêm case cho Hard Gate / điểm DỪNG |
| Chạy `validate-skill.py` của Grok | Path đó không có ở repo này; dùng `check-evals.py` |

## Red flags — DỪNG

- "Assertion này đủ rõ rồi" (mà chứa `works`, `properly`, `correctly`, `necessary`)
- "Thêm eval sau khi TUNE xong"
- "Negative trigger không cần, skill đã có 'NOT for'"
- "Báo xong khi chưa chạy checker"

Tất cả nghĩa là: quay lại Steps 3-6 và dán output của checker.
