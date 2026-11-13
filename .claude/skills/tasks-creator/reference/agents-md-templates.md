# AGENTS.md templates — literal text

Two templates: the **central** doc (full operating instructions, written into the lowest-numbered
folder) and the **stub** doc (written into every other folder of the group). Substitute
`<GROUP>`, `<CENTRAL_FOLDER>`, `<FOLDER_NAME>` literally; build `<CURRENT_STATE_SECTION>` /
`<WAVE_TABLE>` per the wave-table rules in `generation-rules.md` §7. Everything else is copied
verbatim. This mirrors what `generate_task.py` itself would render, field for field (schema,
status convention, wave/status-tracking rules, anti-patterns) — the one deliberate difference is
the provenance paragraph in the central template's Overview, which points at this skill instead of
claiming the script as the one true source (see below), since this skill is now the primary,
self-sufficient way to build these files.

## Central template (write to `<CENTRAL_FOLDER>/AGENTS.md`)

````markdown
# Migration Tasks — AGENTS.md

## Overview

`.tasks/01_migration/` chứa toàn bộ định nghĩa + trạng thái task migration của group **<GROUP>**
(`02_target/<GROUP>/`). File này là **nguồn hướng dẫn duy nhất** để chạy task — không có
slash-command hay skill riêng nào cả; khi được yêu cầu chạy/tiếp tục migration task cho group này,
đọc trực tiếp file này + `{folder}/00_tasks.json` rồi tự thực hiện theo các bước bên dưới.

Mỗi folder có `00_tasks.json` riêng, xây theo đúng cấu trúc + quy tắc của skill `tasks-creator`
(`.agents/skills/tasks-creator/SKILL.md`), dựa trên `.meta/00_projects.json` + 3 file template
dùng chung `00_migration/02_template/01_tasks/00_tasks_{api,web,qa}.json`. Một script tự động
tương đương cũng tồn tại (`make target_generate_task mono=<GROUP>` →
`.tmp/scripts/generate_task.py`) cho trường hợp sinh mới toàn bộ group hoặc `--all` — KHÔNG chạy
script đó (nhất là cờ `--force`) trên 1 folder đang có tiến độ thật, sẽ reset toàn bộ status về
`pending`; xem tiến độ thật thì thêm/sửa trực tiếp `00_tasks.json` theo đúng skill.
**Không sửa 3 file template dùng chung để hack dữ liệu riêng 1 group** — chỉ đọc/ghi
`02_target/<GROUP>/.tasks/01_migration/{folder}/00_tasks.json` của đúng folder đang thao tác.

## Directory Structure

```text
02_target/<GROUP>/.tasks/01_migration/
├── NN_tasks_api/    # 1 wave / app BE: T001 dotnet-migrate + T002 testing + T003 verify + T004 docs 00_db (db-docs) — chỉ có nếu group có app BE
├── NN_tasks_web/    # tương tự, cho app FE — chỉ có nếu group có app FE
└── NN_tasks_qa/     # 1 wave / app BE+FE: T001 qa-api-planning + T002 qa-implement + T003 qa-verify-complete — chỉ có nếu group có ít nhất 1 app BE hoặc FE
```

Số `NN` đánh liên tục không nhảy số, theo đúng thứ tự category **cố định api → web → qa**, chỉ
tính category thực có mặt: `api` (nếu có BE) lấy `00`, rồi `web` (nếu có FE) lấy số kế tiếp còn
trống, rồi `qa` (nếu có BE hoặc FE) lấy số kế tiếp — vd group chỉ có FE (không BE) thì web là
`00_tasks_web` và qa là `01_tasks_qa`, không phải `01_`/`02_`. Folder có số nhỏ nhất
(**<CENTRAL_FOLDER>** ở group này) giữ `AGENTS.md` đầy đủ (file này); các folder còn lại chỉ là
stub trỏ lại đây.

Không còn task `/init-deep`, không còn task documentation (phase 02), không còn task database
(DB-prepare/mssql→postgresql). Task db-docs giờ là **T004 docs 00_db** trong mỗi wave
BE (skill `aie-skills/db-docs`) — 1 task duy nhất, chạy sau T003 verify. Ngoài ra chỉ
còn testing + dotnet-migrate + verify (1 verify duy nhất/wave, skill tuỳ BE=`api-skills/be-verify-complete`
hay FE=`web-skills/fe-verify-complete`)
cộng với 1 wave QA riêng cho mỗi app (planning + implement + verify, skill tuỳ app có REST API
hay chỉ là worker).

## 00_tasks.json — cấu trúc

Root object của mỗi `00_tasks.json` là **flat**, KHÔNG bọc trong key tên phase. Mỗi entry là 1
wave, bên trong chứa 3 task con, mỗi task có các field: `skills`, `monorepo`, `source_dir`,
`target_dir`, `prompt`, `expect`, `status`.

- `NN_tasks_api` / `NN_tasks_web`: wave tên dạng `WAVE_0N_{BE|FE}[_SUFFIX]`, 3 task con là
  `T001` dotnet-migrate + `T002` testing + `T003` verify-complete + `T004` docs 00_db
  (db-docs) (1 verify duy nhất/wave, khác với cấu trúc cũ có 2 verify/wave).
- `NN_tasks_qa`: wave tên dạng `WAVE_QA_0N_<SUFFIX>` (1 wave / app BE **và** FE), 3 task con là
  `T001` qa-api-planning + `T002` qa-implement + `T003` qa-verify-complete.

## 1. Xác định phạm vi chạy

Không có cú pháp lệnh cố định — hiểu yêu cầu của user theo ngôn ngữ tự nhiên rồi map vào 1 trong các
dạng phạm vi sau (group luôn là group hiện tại, tự suy từ thư mục làm việc):

- Không nêu rõ, hoặc "chạy hết"/"chạy toàn bộ"/"all" → chạy toàn bộ mọi folder, theo thứ tự số;
  trong mỗi folder chạy lần lượt từng wave theo thứ tự xuất hiện, mỗi wave chạy T001 → T003.
- Nêu `<folder>` (vd "chạy 00_tasks_api") → toàn bộ folder đó (mọi wave).
- Nêu `<folder> <wave>` (vd "chạy 00_tasks_api WAVE_01_BE_...") → toàn bộ task trong đúng wave
  đó, theo thứ tự T001 → T003.
- Nêu `<folder> <wave> <task_id>` → chỉ chạy đúng task đó trong đúng wave.
- Bỏ qua task đã `"status": "done"` (hoặc giá trị legacy `"completed"`) / `"skipped"`; chỉ chạy
  task còn `"pending"`.

## 2. Với mỗi task cần chạy

1. Đọc lại nguyên task object từ `{folder}/00_tasks.json` (đúng folder đang thao tác): `skills`,
   `monorepo`, `source_dir`, `target_dir`, `prompt`, `expect`.
2. **Trước khi implement**: cập nhật ngay `"status"` của đúng task đó thành `"in_progress"` trong
   `{folder}/00_tasks.json` (sửa đúng 1 task, không đụng task/wave khác) — đánh dấu đang thực
   hiện để lần chạy sau hoặc người khác biết task này không còn `"pending"`.
3. Nạp hướng dẫn thực thi theo field `skills` (dạng path, vd `00_migration/api-skills/be-testing`)
   → đọc `.agents/skills/<path>/SKILL.md` và làm theo hướng dẫn trong đó; nếu `skills` rỗng →
   thực hiện trực tiếp theo `prompt`/`expect` của task, nếu không rõ cách làm thì dừng lại hỏi
   user thay vì tự đoán skill.
4. Thực thi task: đọc từ `source_dir`, ghi kết quả vào `target_dir`, trong phạm vi thư mục của
   group này.
5. Đối chiếu kết quả với `expect` (nếu có). Task loại verify-complete phải ghi kết quả vào đúng
   `target_dir` chỉ định — với các task này, `target_dir` đã trỏ đúng `{folder}/01_status.json`
   của folder đang xử lý (xem schema + rule chi tiết ở mục
   [Wave/Folder Status Tracking](#wavefolder-status-tracking-01_statusjson) bên dưới).
6. **Sau khi hoàn thành**: cập nhật `"status"` của đúng task đó từ `"in_progress"` → `"done"` (sửa
   đúng 1 task, không đụng task/wave khác).
7. Báo cáo ngắn gọn: task nào (kèm wave/folder) vừa xong, kết quả thế nào, trước khi sang task kế
   tiếp.

## 3. Khi chạy nhiều task ("all", cả folder, hoặc cả wave)

- Trong cùng 1 wave: chạy tuần tự T001 → T002 → T003 (verify) — T003 là task cuối mỗi wave,
  phụ thuộc T001 (dotnet-migrate) và T002 (testing) đã xong trước đó.
- Giữa các wave khác nhau trong cùng 1 folder: các wave thường độc lập (mỗi wave là 1 app riêng,
  `source_dir`/`target_dir` không giao nhau) — mặc định vẫn chạy tuần tự theo thứ tự xuất hiện
  trong file, trừ khi user yêu cầu song song.
- Giữa các folder: luôn tuần tự theo số thứ tự — folder sau không phụ thuộc cứng folder trước
  nhưng giữ thứ tự cho nhất quán, trừ khi user yêu cầu khác.
- Task thất bại / không đạt `expect` → dừng lại, báo lỗi, cập nhật `"status"` của đúng task đó
  thành `"failed"` (KHÔNG để lại `"in_progress"` và KHÔNG tự set `"done"`), hỏi user trước khi
  tiếp tục.
- Task có `skills` rỗng mà không tự suy ra được cách làm → dừng lại, hỏi user nên dùng skill nào;
  nếu đã lỡ set `"in_progress"` trước khi phát hiện, trả lại `"pending"`.
- Khi bắt đầu 1 lượt chạy "all"/cả folder/cả wave, nếu gặp task đang `"status": "in_progress"` từ
  lần chạy trước (bị ngắt giữa chừng) → coi như chưa xong, chạy lại từ đầu task đó.

## Status Convention

`pending` → `in_progress` → `done` (hoặc `failed` / `skipped`).

- `pending` → `in_progress`: set NGAY trước khi implement, sửa đúng 1 task (không đụng task/wave
  khác).
- `in_progress` → `done`: chỉ sau khi đối chiếu kết quả với `expect`.
- `in_progress` → `failed`: khi không đạt `expect` — KHÔNG để lại `in_progress`, KHÔNG tự set
  `done`; dừng lại hỏi user trước khi tiếp tục.
- `pending` → `skipped`: chủ động bỏ qua, phải có lý do rõ ràng.
- Giá trị legacy `"completed"` còn sót lại trong `00_tasks.json` (sinh trước khi convention đổi
  tên) coi tương đương `done` — không sửa lại thành `done` chỉ vì đổi tên, nhưng không tạo mới giá
  trị `"completed"` khi update task khác.

## Wave/Folder Status Tracking (01_status.json)

`{folder}/01_status.json` ghi kết quả verify sau khi **tất cả** task của 1 wave trong
`{folder}/00_tasks.json` đã `done`.

### Relationship với 00_tasks.json

| File | Purpose |
|------|---------|
| `{folder}/00_tasks.json` | Định nghĩa tất cả wave của folder đó. Mỗi task có `status: pending / in_progress / done`. |
| `{folder}/01_status.json` | Kết quả verify sau khi wave hoàn thành. Chỉ ghi khi wave đó đã done. |

**Luồng:**

1. Agent đọc `{folder}/00_tasks.json` → biết wave nào có task gì.
2. Chạy task → update `{folder}/00_tasks.json` (set `"status": "done"`).
3. Sau khi tất cả task của wave trong folder đó done → verify.
4. Nếu verify OK → ghi vào `{folder}/01_status.json`.

### 01_status.json Schema

```json
{
  "phase": "{folder}",
  "monorepo": "<GROUP>",
  "updated": "YYYY-MM-DD",
  "waves": {
    "WAVE_XX_{KIND}": {
      "status": "completed",
      "tasks": {
        "T001": {
          "name": "Task name",
          "status": "completed",
          "result": "Mô tả kết quả"
        }
      },
      "verified_at": "YYYY-MM-DD"
    }
  }
}
```

### Rules

**Rule 1 — Chỉ ghi wave vào `01_status.json` khi TẤT CẢ task của wave đó đã `done`.**
Không ghi wave đang làm dở (một vài task pending). Nếu chưa hoàn thành thì để `01_status.json`
không có wave đó (hoặc rỗng nếu chưa wave nào xong).

**Rule 2 — Mỗi task record phải có `name`, `status`, `result`.**
- `name`: tên ngắn gọn (vd "Test scripts", "Dotnet migrate")
- `status`: `completed` (chỉ ghi khi done)
- `result`: mô tả kết quả cụ thể, có số liệu (vd "245 tests, 100% passing")

**Rule 3 — Phải verify trước khi ghi status.**
Không ghi status từ assumption. Phải chạy `dotnet build` + `dotnet test` + kiểm tra file tồn tại
trước.

**Rule 4 — `updated` và `verified_at` phải khớp ngày thực tế.**
Format: `YYYY-MM-DD`. Dùng `date +%Y-%m-%d` nếu cần.

## Current State

<CURRENT_STATE_SECTION>

## Anti-Patterns

- ❌ Đọc/ghi trực tiếp vào các file template `00_migration/02_template/01_tasks/00_tasks_{api,web,qa,aie}.json`
  — đó là nguồn sinh dùng chung cho mọi group, không phải `00_tasks.json` thực tế của group này.
- ❌ Tự đoán skill khi field `skills` rỗng mà không suy ra được cách làm — dừng lại hỏi user; nếu
  đã lỡ set `in_progress` trước khi phát hiện, trả lại `pending`.
- ❌ Chạy "all" / khối lượng migrate lớn (vd toàn bộ .NET migration nhiều app cùng lúc) mà không
  xác nhận phạm vi với user trước.
- ❌ Current State (bảng trong AGENTS.md) lệch so với `{folder}/00_tasks.json` thực tế (vd: task
  đã done nhưng bảng vẫn ghi pending) — bảng này phải refresh mỗi khi `00_tasks.json` đổi, không
  tự sửa tay riêng bảng.
- ❌ Dùng giá trị status tuỳ tiện ngoài `pending/in_progress/done/failed/skipped`.
- ❌ Sửa nhầm task/wave khác khi cập nhật status của 1 task.
- ❌ Tìm/gọi slash-command hay skill riêng để biết cách chạy task — không có, mọi hướng dẫn đã nằm
  sẵn trong file này.
- ❌ Ghi status vào `01_status.json` trước khi verify — phải chạy build/test trước.
- ❌ Ghi wave chưa hoàn thành vào `01_status.json` — chỉ ghi khi tất cả task của wave đã done.
- ❌ Copy-paste result từ wave/folder khác — mỗi wave/folder có kết quả riêng.
- ❌ Để `01_status.json` trống khi có wave đã hoàn thành — phải update ngay.
- ❌ Quên update `{folder}/00_tasks.json` — phải set task status trước khi ghi status.
````

## Stub template (write to every non-central `<FOLDER_NAME>/AGENTS.md`)

````markdown
# <FOLDER_NAME> — AGENTS.md

## Overview

Rules vận hành đầy đủ (cách đọc/chạy task, quy ước status, schema `01_status.json`,
anti-patterns) nằm ở [`../<CENTRAL_FOLDER>/AGENTS.md`](../<CENTRAL_FOLDER>/AGENTS.md) — nguồn
hướng dẫn duy nhất cho toàn bộ group **<GROUP>**, áp dụng cho mọi folder task. File này chỉ mô
tả riêng `<FOLDER_NAME>`.

## Files

- `00_tasks.json` — định nghĩa task của `<FOLDER_NAME>`.
- `01_status.json` — kết quả verify sau khi wave của `<FOLDER_NAME>` hoàn thành (rỗng nếu chưa có).

## Current State

<WAVE_TABLE>
````
