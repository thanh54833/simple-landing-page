# Guide for agents — gh-issue-sync

File này giải thích cách sửa `gh-issue-sync` mà không làm lệch upstream.
Mẫu theo `ai-image-generation` `AGENTS.md`.

## What this skill contains

Đồng bộ GitHub issues về file Markdown local (`.issues/open/`, `.issues/closed/`) qua CLI `gh-issue-sync` (`init`, `pull`, `push`, `list`, `new`, `close`, `reopen`, `status`, `diff`). Single `SKILL.md` vendored từ `mitsuhiko/gh-issue-sync` (thư mục `skill/`). Upstream còn `embed.go` (code Go của repo gốc), không lấy.

## Key files

- `SKILL.md` — upstream nguyên văn (commit `955fe4c`). Không sửa tay trừ khi thêm khối `Local Overrides`.
- `AGENTS.md` (file này) — rule guide cho agent sửa skill.
- `CHANGELOG.md` — release notes, newest first.
- `evals/evals.json`, `evals/triggers.json` — evals do repo viết; upstream sync không được ghi đè.
- `../agentic-os-lock.json` — pin `gh-issue-sync` (`sourceType: github`, `source: mitsuhiko/gh-issue-sync`, `version: main@<sha7>`).

## Rules for changes

- **Vendored:** nội dung upstream giữ nguyên. Rule local (nếu cần) vào khối `Local Overrides` đầu `SKILL.md`; mỗi lần đổi có note trong `CHANGELOG.md`.
- **Upstream:** không có tag; pin commit sha. Sync upstream = thay `SKILL.md`, giữ `Local Overrides`, `AGENTS.md`, `CHANGELOG.md`, `evals/`.
- **Version:** giữ cùng version ở `../agentic-os-lock.json` và heading đầu `CHANGELOG.md`. Sync upstream → bump cả hai cùng commit.
- **Push is outward-facing:** `push` tạo/sửa/đóng issue và post comment trên GitHub. Chạy `push --dry-run` và xác nhận với user trước `push`.
- **Pull:** `pull` bỏ qua conflict; chỉ dùng `--force` khi user đồng ý ghi đè file local.
- **Overlap:** `github-issues` làm việc trực tiếp qua API (labels, types, dependencies, projects); skill này làm việc theo file local. Chọn theo cách user muốn làm việc, không dùng cả hai trên cùng một thay đổi.
- **Compatibility:** instructions trung lập runtime.
- **Checks:** `python3 .agents/playbooks/002_skills/01_evals/check-evals.py .agents/skills/agentic-os/gh-issue-sync` in `0 error`; verify frontmatter `name: gh-issue-sync`; `make agents_sync` rồi `make agents_sync-check`.

## Writing style

- Nội dung upstream giữ tiếng Anh như gốc; `AGENTS.md` và `CHANGELOG.md` viết tiếng Việt, thuật ngữ kỹ thuật giữ tiếng Anh.
- Lead bằng main point, câu ngắn. Giữ nguyên identifier, command, path.
