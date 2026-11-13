# Changelog — writing-command

Một file duy nhất cho `skills/agentic-os/writing-command/`, newest first. Heading đầu giữ cùng version với `../agentic-os-lock.json`. Prose tiếng Việt, thuật ngữ kỹ thuật giữ tiếng Anh.

## local-2026-11-10

- Thêm `evals/evals.json` (8 test case) và `evals/triggers.json` (10 trigger, 5 negative).
- Initial self-built release: tạo hoặc sửa command trong `.agents/.commands/` (gate router và standalone), 8 bước Workflow + template router.
- Baseline theo `writing-skills` (subagent không có skill, dry-run tạo `/critique-ui` + sửa `/verify`): agent tự đọc `.commands/AGENTS.md` nên đúng phần lớn (chỉ sửa `.agents/`, sync, CHANGELOG, dòng bảng). Lỗi thật đưa vào skill: chép bước resolve-target từ `redesign.md` thay vì tái dùng; bước mới trong router dài như procedure; không kiểm cross-reference "step N" khi đánh số lại; không có check frontmatter/dry-run từng nhánh.
- Ngoại lệ cho luật tái dùng: user yêu cầu router standalone độc lập thì được chép các bước cần dùng, kèm ghi chú cố ý trùng ở `.commands/AGENTS.md` (từ `/enhance`).
- Step 2: skill phía sau là vendored thì glue của repo nằm ở router (khớp ngoại lệ mới trong `.commands/AGENTS.md`).
