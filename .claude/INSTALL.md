# Cài đặt pi cho project

Hướng dẫn dựng môi trường pi trên máy mới. Nguồn cấu hình: `.pi/settings.json`.

## Yêu cầu
- Node.js >= 20 (đã kiểm tra trên v22) và `npm`
- `git` (package Superpowers clone qua git; máy map `https://github.com/` → SSH nên cần SSH key GitHub)

## 1. Cài pi CLI (global)
```bash
npm install -g @mariozechner/pi-coding-agent
pi --version        # 0.73.1 khi viết tài liệu này
```

## 2. Cài package của project
Chạy từ root repo. `-l` = project scope, ghi vào `.pi/settings.json`.
```bash
pi install -l npm:pi-subagents
pi install -l npm:pi-lens
pi install -l git:github.com/obra/superpowers@v7.0.0
pi list             # mục "Project packages" phải có đủ 3 package
```
`settings.json` đã khai báo sẵn các package này, nên lệnh chỉ dựng lại `.pi/npm/` và `.pi/git/` (cả hai gitignored, ~170 MB).

## 3. Sinh file derived
```bash
make mcp && make commands
make mcp-check && make commands-check   # phải exit 0
```

## 4. Dùng
- Package của project chỉ nạp sau khi **trust project**; `pi -a` duyệt cho một lần chạy.
- Sau `pi install`, mở **session mới** để có tool `subagent`, `lens_*`.
- Model subagent đặt tay trong `settings.json` → `subagents` (hiện `opencode-go/deepseek-v4.1-flash`); cần đăng nhập provider `opencode-go` trong pi.

## Gỡ / cập nhật
```bash
pi remove -l npm:<pkg>      # gỡ package project, prune checkout
pi list
```
Superpowers chỉ khai báo **một lần, project scope**; nếu có bản user-level thì `pi remove git:github.com/obra/superpowers` (không `-l`) để tránh nạp đôi.

Xem thêm `.pi/AGENTS.md`.
