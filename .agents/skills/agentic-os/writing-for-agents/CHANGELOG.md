# Changelog — writing-for-agents

Một file duy nhất cho `skills/agentic-os/writing-for-agents/`, newest first. Heading đầu giữ cùng version với `../agentic-os-lock.json`. Prose tiếng Việt, thuật ngữ kỹ thuật giữ tiếng Anh.

## v1.3.1

- Vendored từ `mattpocock/skills` (`skills/productivity/writing-for-agents`), pin `sourceType: github` trong lock.
- `SKILL.md`: reference chung cho mọi document agent đọc (skill, `AGENTS.md`, `CLAUDE.md`) — context pointers, two loads, information hierarchy, completion criteria, when to split, leading words, pruning.
- `SKILL-MECHANICS.md`: nhánh riêng cho skill — invocation (model-invoked vs user-invoked), splitting by invocation, router skills.
- `agents/openai.yaml`: metadata cho runtime OpenAI.
- Thêm `AGENTS.md` rule guide + `CHANGELOG.md` theo mẫu `writing-adr`.
