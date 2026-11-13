---
name: business-memory
description: Use when a project needs its business memory created (domain map, decision log) or when a decision, business rule, or operational lesson was just settled and must be saved so later decisions can rely on it. Fires on requests to init business memory, remember or record a decision, save an insight, or capture domain rules for decision support.
---

## Local Overrides

- Memory nằm ở `docs/physarum/business-memory/` (owner chọn; không dùng `.physarum/memory/`). Policy kỹ thuật vẫn ở `AGENTS.md` gốc, không chép vào memory.
- Skill chỉ ghi memory. Không sửa code, không sinh spec/ADR/plan. ADR kỹ thuật vẫn đi qua `writing-adr`; decision ở đây tóm tắt và trỏ `source` về ADR.

# Business Memory

## Overview

Memory nghiệp vụ trong repo gồm: **domain map** (hiểu hệ thống), **decisions** (đã chốt + lý do + phương án bị loại), **insights** (quan sát vận hành), **index** (mục lục). Nguyên tắc: chỉ ghi điều có evidence, owner chốt thì mới `accepted`, không bao giờ xoá lịch sử.

## When to Use

- Project chưa có `docs/physarum/business-memory/` → **init**
- Owner vừa chốt một quyết định, đổi business rule, hoặc rút ra bài học nghiệp vụ → **save**

NOT for: design token UI, lỗi CI thuần kỹ thuật, preference máy local, ghi log chat, đọc/recall (đọc theo `AGENTS.md` trong thư mục memory).

## Route

| Việc | Đọc |
|---|---|
| Khởi tạo memory cho project | `reference/init.md` |
| Lưu decision / insight / đổi domain | `reference/save.md` |

Đọc đúng file reference của việc đang làm, rồi làm theo. Không đọc cả hai nếu không cần.

## Hard Rules

- **Evidence trước.** Mỗi mục lấy từ file repo, ADR, `PRODUCT.md`, hoặc lời owner trong phiên này. Không có nguồn thì hỏi owner hoặc để vào `open_questions`; không điền bừa.
- **Owner chốt mới `accepted`.** Đề xuất của agent là `proposed`. Ở `init`, ADR `accepted` và quyết định ghi trong `PRODUCT.md` đã là chốt của owner; owner xác nhận gói file ở bước 5 là đủ.
- **Append-only.** Không xoá hoặc sửa nội dung decision đã `accepted`. Đổi ý = decision mới có `supersedes`, cái cũ thành `superseded`.
- **Nêu diff trước khi ghi** và chờ owner xác nhận.
- **Index đồng bộ.** Mọi lần ghi cập nhật `index.json`.
- Sau khi ghi, kiểm tra mọi JSON parse được: `python3 -c "import json;json.load(open('<file>'))"`.

Violating the letter of these rules is violating the spirit.

## Rationalizations

| Excuse | Reality |
|---|---|
| "Rõ ràng owner sẽ chọn vậy, ghi `accepted` luôn" | Owner chưa nói thì là `proposed` |
| "Thiếu `alternatives_rejected`, điền tạm cho đủ" | Điền bừa làm hỏng quyết định sau; hỏi owner |
| "Decision cũ sai rồi, sửa thẳng tại chỗ" | Tạo decision mới + `supersedes` |
| "Rule này cũng hay, ghi luôn vào domain" | Không có nguồn thì vào `open_questions` |
| "Lưu cả đoạn chat cho đủ ngữ cảnh" | Ghi kết luận có cấu trúc, không ghi log chat |

## Red Flags: STOP

- Sắp ghi file mà owner chưa thấy diff
- Một trường nội dung không truy được nguồn
- Sắp xoá hoặc ghi đè decision `accepted`
- Sắp chép business rule vào decision thay vì trỏ `br-XXX`
