# Init — khởi tạo business memory cho project

Mục tiêu: dựng `.physarum/agents/product_owner/` từ evidence có sẵn, để agent hiểu nghiệp vụ trước khi ra quyết định.

## Điều kiện

- Nếu thư mục đã có `domain.json` hoặc `index.json`: DỪNG, báo owner, chuyển sang `reference/save.md`. Không ghi đè.

## Bước

1. **Đọc nguồn** (chỉ những gì tồn tại): `PRODUCT.md`, `README*`, `AGENTS.md` gốc, `.physarum/docs/{intents,specs,adr}/`, `package.json`/`pyproject.toml` để biết stack, cấu trúc `apps/`/`src/`.
2. **Lập bản nháp `domain.json`** theo schema dưới. Mỗi mục có nguồn; mục không có nguồn bỏ vào `open_questions`.
3. **Lập decision nháp từ ADR** đã `accepted`: mỗi ADR → một `dec-XXX` (`source` trỏ ADR, `alternatives_rejected` lấy từ phần "Alternatives considered"). Quyết định ghi ở `PRODUCT.md` hoặc owner nói trong phiên cũng được, nêu rõ `source`. ADR còn `proposed` thì decision là `proposed`.
4. **Hỏi owner tối đa 3 câu** cho chỗ evidence không trả lời được (users chính, non-goals, rule quan trọng nhất). Câu nào chưa trả lời → `open_questions`.
5. **Trình bày toàn bộ file sẽ tạo** (tên + tóm tắt từng file). Chờ owner xác nhận.
6. **Ghi file**, rồi kiểm tra JSON parse.
7. **Sao chép `reference/memory-agents-template.md`** thành `AGENTS.md` trong thư mục memory nếu chưa có (xem Template cuối file).
8. Báo owner: số decision đã tạo, `open_questions`, và mục nào còn dựa trên suy luận cần xác nhận.

## Layout tạo ra

```
.physarum/agents/product_owner/
├── AGENTS.md        # persona + quy trình recall/save
├── index.json
├── domain.json
├── decisions/dec-001-<slug>.json
└── insights/.gitkeep
```

Không tạo insight lúc init: insight chỉ đến từ quan sát vận hành thật.

## `domain.json` schema

```json
{
  "version": 1,
  "updated_at": "YYYY-MM-DD",
  "system": { "name": "", "one_liner": "", "users": [], "jobs_to_be_done": [] },
  "scope": { "in": [], "out": [] },
  "core_flows": [{ "id": "", "name": "", "steps": [], "actors": [], "rules": [] }],
  "entities": [{ "name": "", "meaning": "", "key_fields": [], "states": [] }],
  "business_rules": [{ "id": "br-001", "rule": "", "reason": "" }],
  "constraints": [],
  "open_questions": []
}
```

- `business_rules[].reason` trỏ `dec-XXX` hoặc nguồn khi có.
- `constraints` chỉ chứa ràng buộc có thật (stack cố định, giới hạn nền tảng, quyết định brand).

## `index.json` schema

```json
{
  "version": 1,
  "updated_at": "YYYY-MM-DD",
  "domain_summary": "",
  "decision_count": 0,
  "topics": [{ "name": "", "keywords": [], "decisions": [], "insights": [], "flows": [] }],
  "recent_decisions": [],
  "open_questions_from_domain": []
}
```

Gom decision theo topic (3–6 topic); `keywords` là từ agent sẽ tìm.

## `decision` schema

Xem `reference/save.md` mục Decision.

## Template `AGENTS.md`

`reference/memory-agents-template.md` là persona + quy trình recall/save. Sao chép nguyên văn vào `.physarum/agents/product_owner/AGENTS.md`; chỉ đổi tên product/đường dẫn nếu project khác repo này.
