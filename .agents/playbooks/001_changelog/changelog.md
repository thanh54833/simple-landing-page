---
name: changelog
description: Use when creating a CHANGELOG.md for a `.agents/` scope, when a self-built skill or the root/.commands/settings tree changed behavior and has no changelog entry, or when asked "tạo/thêm/cập nhật changelog".
---

# Playbook — CHANGELOG.md cho một scope trong `.agents/`

## Overview

Changelog nội bộ của factory: một file `CHANGELOG.md` mỗi scope, newest first, mỗi note một dòng. Template: `CHANGELOG.template.md` (cùng folder). **Làm sai ý định = làm sai luôn cả chữ:** đi đúng từng bước, kể cả khi scope "trông hiển nhiên".

## When to use

- Scope là skill self-built, hoặc file tổng của `.agents/`, `.commands/`, `settings/` → dùng playbook.
- Scope là vendored → **DỪNG**, xem Gate bên dưới.
- Phát hành package (release notes) → không phải playbook này, đó là việc của `rea-changelog-update`.

## Gate — chạy trước mọi thứ

```bash
python3 -c "import json;d=json.load(open('.agents/skills/agentic-os/agentic-os-lock.json'))['skills'];print({k:v['source'] for k,v in d.items()})"
```

| Scope | Điều kiện | Hành động |
|---|---|---|
| `skills/agentic-os/<skill>` | `source == "local"` (self-built) | Tiếp tục |
| `skills/agentic-os/<skill>` | `source` khác `"local"` (vendored, vd `impeccable`, `hallmark`, `doc-coauthoring`, `writing-for-agents`) hoặc `skills/react-best-practices`, `skills/rea/*` | **DỪNG**, báo user, không tạo file |
| `.agents`, `.commands`, `settings` (file tổng) | — | Tiếp tục |

Danh sách vendored thay đổi theo lock; luôn đọc lock, không dựa vào trí nhớ.

## Steps

1. Chốt `<scope>` (tên hiển thị) và `<scope-path>` (vd `skills/agentic-os/writing-intent`, `.commands`, `settings`). Qua Gate.
2. `<scope-path>/CHANGELOG.md` đã tồn tại → **thêm entry mới lên đầu** bằng Edit, bỏ qua bước 3-4. Chưa có → copy template (`cp`), thay `<scope>` và `<scope-path>`.
3. Chọn `<version-heading>`:
   - Skill self-built → `local-YYYY-MM-DD`, **bằng đúng** `version` của skill trong lock.
   - File tổng của dir/root → `YYYY-MM-DD`.
4. Viết entry `Initial ... release`: scope 1 dòng + rule chính + điểm DỪNG của scope.
5. Entry sau: 1 dòng 1 note, chỉ ghi behavior change, non-obvious fix, hoặc thay đổi ảnh hưởng toàn cây. Chi tiết đã có ở file con → link tới file đó, không chép lại.
6. Skill self-built đổi nội dung → bump `version` trong lock **cùng commit** với changelog, heading phải khớp.
7. Xóa khung `Quy ước` của template khỏi file vừa tạo.
8. Verify (xem Quick reference), rồi báo kết quả kèm output.

## Quick reference

| Kiểm tra | Cách |
|---|---|
| Heading khớp lock | `grep '"<skill>"' -A3 .agents/skills/agentic-os/agentic-os-lock.json` so với `## local-…` đầu file |
| Còn sót placeholder | `grep -n '<scope\|<version-heading\|Quy ước' <scope-path>/CHANGELOG.md` → phải rỗng |
| Mirror không drift | `make agents_sync-check` → exit 0. Drift thì `make agents_sync`, không sửa tay `.claude/` |
| Ngôn ngữ | Prose tiếng Việt, thuật ngữ kỹ thuật giữ tiếng Anh |

## Common mistakes

| Sai | Đúng |
|---|---|
| Tạo changelog cho skill vendored vì "cho đồng bộ" | Gate chặn. Vendored có `Local Overrides` trong SKILL.md thay cho changelog |
| Ghi đè `CHANGELOG.md` đang có bằng template | Edit, thêm entry mới lên đầu |
| Đoán version heading từ ngày hôm nay | Lấy từ lock; chỉ file tổng mới dùng `YYYY-MM-DD` |
| Đổi skill mà quên bump lock | Bump cùng commit, heading phải khớp |
| Sửa `.claude/skills/.../CHANGELOG.md` | Sửa ở `.agents/`, chạy `make agents_sync` |
| Chép lại nội dung file con vào changelog | Link tới file con |

## Red flags — DỪNG

- "Skill này vendored nhưng thêm changelog cũng vô hại"
- "Lock không ghi, chắc là self-built"
- "Bỏ `agents_sync-check`, chỉ là file markdown"
- "Verify sau", hoặc báo xong khi chưa chạy lệnh nào

Tất cả nghĩa là: quay lại Gate, rồi chạy Verify và dán output.
