# Save — lưu logic phục vụ quyết định sau này

Mục tiêu: ghi lại **vì sao** để quyết định tương lai không phải đoán. Ba loại ghi: Decision, Insight, Domain update.

## Điều kiện

- Chưa có `docs/physarum/business-memory/index.json` → DỪNG, báo owner memory chưa khởi tạo và hỏi có chạy `reference/init.md` không. Không tự khởi tạo.

## Chọn loại

| Tình huống | Loại | Status |
|---|---|---|
| Owner đã chốt lựa chọn | Decision | `accepted` |
| Agent hoặc owner đề xuất, chưa chốt | Decision | `proposed` |
| Quan sát từ vận hành, chưa chốt hành động | Insight | n/a |
| Business rule, flow, scope, constraint đã chốt đổi | Domain update | n/a |
| Rule hoặc điều kiện chưa chốt / chưa có nguồn | Không ghi vào rule; thêm vào `open_questions` | n/a |

**Chốt hay chưa:** chỉ coi là chốt khi owner nói rõ đã chọn ("chốt", "quyết định", "dùng X"). Ý nghiêng về một hướng ("hình như", "có thể nên") chưa phải chốt: nếu đã nêu được `reasons` và `alternatives_rejected` thì ghi decision `proposed`, nếu chưa thì ghi vào `open_questions`; không bịa lý do để đủ trường.

**Evidence:** lời owner trong phiên đủ làm `source` cho decision và rule (ghi `source: "phiên với owner YYYY-MM-DD"`). Insight cần dữ kiện về vận hành (số liệu, ticket, log); thông tin owner kể lại từ người khác chỉ ghi được với `confidence: low` và `observation` nói rõ là kể lại, nếu không thì vào `open_questions` kèm nguồn.

Insight không được đóng vai decision. Một lần chốt thường chạm nhiều loại (decision + domain); trình bày gộp thành một gói.

## Bước chung

1. **Recall trước.** Đọc `index.json`, mở decision/insight/rule cùng topic. Tìm: decision đang `accepted` mâu thuẫn hoặc bị thay thế, phương án trùng `alternatives_rejected`, `open_question` được trả lời.
2. **Thu thập trường bắt buộc** từ cuộc trao đổi. Thiếu trường nào → hỏi owner, không điền bừa.
3. **Trình bày gói thay đổi** (một lần dừng duy nhất: câu "đã resolve" của command và diff gộp chung vào đây, owner trả lời một lần): file tạo/sửa + diff từng file (gồm `index.json`). Chờ owner xác nhận.
4. **Ghi**, cập nhật `index.json`, kiểm tra JSON parse.
5. Báo lại: id vừa tạo, decision bị `superseded` (nếu có), `open_question` đã đóng.

## Decision

File: `decisions/dec-XXX-<slug>.json`. `XXX` = số file trong `decisions/` + 1 (tính cả `superseded`; `decision_count` phải bằng số này), 3 chữ số. `slug` kebab-case ngắn.

```json
{
  "id": "dec-007-slug",
  "status": "accepted",
  "date": "YYYY-MM-DD",
  "title": "",
  "context": "Vấn đề và ràng buộc lúc quyết định",
  "decision": "Chọn gì",
  "reasons": [],
  "alternatives_rejected": [{ "option": "", "why_not": "" }],
  "consequences": [],
  "reversible": "easy | medium | hard",
  "related_flows": [],
  "related_entities": [],
  "keywords": [],
  "supersedes": null,
  "constraints": [],
  "files": [],
  "source": "ADR / PRODUCT.md / phiên với owner",
  "author": ""
}
```

**Bắt buộc có nội dung:** `context`, `decision`, `reasons`, `alternatives_rejected` (mỗi mục đủ `option` và `why_not`), `consequences`, `reversible`, `keywords`, `source`. Cách đã thử và fail ghi vào `alternatives_rejected`. `author` là tên owner nêu trong phiên, hoặc `git config user.name`; không có thì hỏi.

**Chất lượng `reasons`:** nêu thứ có thể kiểm chứng (số liệu, ràng buộc, deadline), không dùng tính từ chung chung ("tốt hơn", "đơn giản hơn").

**Đổi ý:**
1. Tạo decision mới với `supersedes: "<id đầy đủ của decision cũ>"` (vd `dec-001-session-in-memory-cookie`, không dùng dạng rút gọn `dec-001`).
2. Ở file cũ chỉ đổi `status` thành `superseded`. Không sửa trường khác.
3. Nếu rule trong `domain.json` đổi, làm Domain update trong cùng gói.
4. Nếu decision cũ có `source` là ADR, đề xuất owner chạy `writing-adr` để ADR mới supersede ADR đó; không sửa ADR từ skill này.

**ADR liên quan:** nếu quyết định là kiến trúc khó đảo ngược, đề xuất owner chạy `writing-adr`; decision ở đây trỏ `source` về ADR đó, không chép lại toàn văn.

## Insight

File: `insights/ins-XXX-<slug>.json`. `XXX` = số file `ins-*.json` + 1, 3 chữ số.

```json
{
  "id": "ins-001-slug",
  "date": "YYYY-MM-DD",
  "title": "",
  "observation": "Điều quan sát được, kèm số liệu hoặc nguồn",
  "implication": "Ý nghĩa với nghiệp vụ",
  "suggested_decision": "",
  "linked_decision": null,
  "keywords": [],
  "confidence": "low | medium | high"
}
```

`observation` phải có evidence (ticket, số liệu, log vận hành, lời owner). Không có evidence thì không ghi insight.

## Domain update

Sửa `domain.json` có chủ đích:

- Thêm/đổi `business_rules` (id `br-XXX` = số lớn nhất hiện có + 1, kể cả khi id có khoảng trống), `constraints`, `core_flows`, `entities`, `scope`.
- Đóng `open_questions` đã được trả lời (xoá khỏi danh sách, và kết luận phải nằm ở decision hoặc rule tương ứng).
- Thêm `open_questions` mới cho điều chưa biết phát sinh khi lưu.
- Cập nhật `updated_at`.
- Rule nghiệp vụ chỉ nằm ở `domain.json`; decision trỏ `br-XXX`, không chép nội dung.

## Cập nhật `index.json`

- `decision_count`, `updated_at`, `recent_decisions` (3 mới nhất, mới nhất trước).
- Thêm id vào đúng `topics[]`. Tạo topic mới khi không topic nào khớp `keywords`; tên topic là danh từ ngắn theo nghiệp vụ (vd "Refund"), không đặt theo tên file.
- Đồng bộ `open_questions_from_domain` với `domain.json`.

## Không lưu

Design token UI, lỗi CI thuần kỹ thuật, preference máy local, log chat, điều không có nguồn.
