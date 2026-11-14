# Guide for agents — github-issues

File này giải thích cách sửa `github-issues` mà không làm lệch upstream.
Mẫu theo `ai-image-generation` `AGENTS.md`.

## What this skill contains

Tạo, cập nhật, quản lý GitHub issues: labels, assignees, milestones, issue types, issue fields, sub-issues, dependencies, Projects V2. Đọc qua MCP `mcp__github__*`, ghi qua `gh api` (REST/GraphQL). `SKILL.md` vendored từ `github/awesome-copilot` (`skills/github-issues`), kèm `references/` theo từng capability.

## Key files

- `SKILL.md` — upstream nguyên văn (commit `8ecd5b1`): workflow, tạo/sửa issue, bảng Extended Capabilities.
- `references/*.md` — upstream: `templates`, `labels`, `milestones`, `sub-issues`, `dependencies`, `issue-types`, `issue-fields`, `projects`, `search`, `images`. Nạp khi cần.
- `AGENTS.md` (file này) — rule guide cho agent sửa skill.
- `CHANGELOG.md` — release notes, newest first.
- `evals/evals.json`, `evals/triggers.json` — evals do repo viết; upstream sync không được ghi đè.
- `../agentic-os-lock.json` — pin `github-issues` (`sourceType: github`, `source: github/awesome-copilot`, `version: main@<sha7>`).

## Rules for changes

- **Vendored:** nội dung upstream và `references/` giữ nguyên. Rule local (nếu cần) vào khối `Local Overrides` đầu `SKILL.md`; mỗi lần đổi có note trong `CHANGELOG.md`.
- **Upstream:** monorepo không có tag; pin commit sha. Sync upstream = thay `SKILL.md` và `references/`, giữ `Local Overrides`, `AGENTS.md`, `CHANGELOG.md`, `evals/`. Link trong `SKILL.md` tới `references/` phải resolve.
- **Version:** giữ cùng version ở `../agentic-os-lock.json` và heading đầu `CHANGELOG.md`. Sync upstream → bump cả hai cùng commit.
- **Outward-facing:** mọi write (`gh api -X POST/PATCH`) tạo hoặc sửa dữ liệu thật trên GitHub. Xác nhận repo và nội dung với user trước khi ghi; hỏi lại khi thiếu thông tin thay vì đoán.
- **zsh:** quote cả cặp `'labels[]=bug'` khi dùng `gh api`.
- **Overlap:** `gh-issue-sync` làm việc theo file local; skill này làm việc trực tiếp qua API. Không dùng cả hai trên cùng một thay đổi.
- **Compatibility:** instructions trung lập runtime.
- **Checks:** `python3 .agents/playbooks/002_skills/01_evals/check-evals.py .agents/skills/agentic-os/github-issues` in `0 error`; verify frontmatter `name: github-issues`; link `references/` resolve; `make agents_sync` rồi `make agents_sync-check`.

## Writing style

- Nội dung upstream giữ tiếng Anh như gốc; `AGENTS.md` và `CHANGELOG.md` viết tiếng Việt, thuật ngữ kỹ thuật giữ tiếng Anh.
- Lead bằng main point, câu ngắn. Giữ nguyên identifier, command, path.
