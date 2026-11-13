---
name: writing-command
description: Use when creating a new slash command, or changing, renaming or fixing an existing one, in `.agents/.commands/`. Fires on requests to add a command, add a step to a router, or sync a command across runtimes.
---

## Local Overrides (hub agentic-os-core)

- Canonical chỉ ở `.agents/.commands/`. `.claude/commands/`, `.opencode/command/`, `.pi/prompts/` do `make agents_sync` sinh ra: không sửa tay.
- Quy ước của router nằm ở `.agents/.commands/AGENTS.md`; file đó thắng khi lệch skill này.
- Prose tiếng Việt cho `CHANGELOG.md`; thân command viết tiếng Anh như các router hiện có.

# Writing Commands

## Overview

Command là router mỏng: resolve input → check gate → gọi một skill → STOP và nêu command kế tiếp. Procedure nằm trong skill, không nằm trong router.

## When to Use

- Thêm command mới, thêm hoặc đổi bước của command cũ, đổi tên, sửa drift giữa các runtime.

When NOT to use: viết hay sửa `SKILL.md` → `writing-for-agents`; command không có skill phía sau → viết skill trước.

## Workflow

1. **Classify.** Mới hay sửa; gate router (trong chuỗi `intent → ship`) hay standalone. Gọi tên skill backing (local `.agents/skills/` hoặc Superpowers). Chưa có skill → STOP, tạo skill trước.
2. **Place each rule.** Router giữ bốn thứ: resolve input, check gate, skill nào, điểm STOP + command kế tiếp. Luật về cách làm việc thuộc skill (`Local Overrides`); skill phía sau là vendored (không sửa được) thì phần glue của repo nằm ngắn ở router. Luật nhiều router dùng chung được định nghĩa một lần ở router sở hữu và các router khác trỏ tới bằng tên.
3. **Reuse before writing.** `grep` `.agents/.commands/` tìm router đã có cùng bước (resolve target ở `redesign.md`, ladder session-default ở `spec`/`adr`/`plan`/`implement`/`verify`/`update-spec`). Gate router dùng đúng nguyên văn ladder của router hàng xóm; standalone router trỏ tới bước đã có thay vì chép lại. User yêu cầu router độc lập thì chép các bước cần dùng và ghi ở `.commands/AGENTS.md` rằng chúng cố ý trùng.
4. **Write from the template** dưới đây. Mỗi bước kết thúc bằng điều kiện kiểm được; bước cuối là STOP.
5. **Improve an existing router.** Trước khi sửa, `grep -rn "step [0-9]\|steps [0-9]" .agents/` để tìm mọi chỗ trỏ tới số bước của nó. Router trỏ theo tên stage hoặc tên bước (vd "Spec stage", "the look step") thì grep chính tên đó. Đánh số lại hoặc đổi tên xong thì sửa từng chỗ trỏ. Bước không đổi giữ nguyên chữ.
6. **Register.** `.agents/.commands/AGENTS.md`: dòng trong `WHERE TO LOOK` + danh sách chain/standalone; thêm convention chỉ khi có luật chéo router mới. `.agents/.commands/CHANGELOG.md`: một bullet tiếng Việt dưới heading ngày hôm nay.
7. **Sync and check.** `make agents_sync`, rồi `make agents_sync-check`, rồi `diff .agents/.commands/<name>.md .claude/commands/<name>.md`. File mirror lạ do sync sinh ra thì báo user, không tự thêm.
8. **Dry-run.** Đọc router như agent: với input rỗng, input là path, input ngoài phạm vi, mỗi nhánh phải kết thúc bằng một hành động hoặc STOP. Báo kết quả từng nhánh.

## Template

```markdown
---
description: <one line, trigger-only>
argument-hint: <path or free text>   # quote it when it starts with `[`
---

## User Input

(copy this block verbatim from an existing router such as `spec.md`: a `text` fence holding the arguments token)

1. Resolve the input, first match wins; state the resolved target in one line. Nothing resolves → ask.
2. Check the gate (approval, prerequisite artifact). Not met → STOP and name the missing step.
3. Invoke `<skill>` (Claude Code: `<plugin:skill>`) with the input.
4. STOP at <the point>. Suggest `/<next command>`. Do not invoke the next gate's skill.
```

## Common Mistakes

- Chép bước resolve-target hoặc ladder từ router khác thay vì dùng lại.
- Nhét procedure hoặc rule "cách làm" vào router; đáng ra vào skill.
- Đổi số bước mà quên các chỗ khác đang trỏ "step N".
- Sửa `.claude/commands/` hay `.pi/prompts/` trực tiếp, hoặc quên `agents_sync-check`.
- Frontmatter có field thứ ba, hoặc `argument-hint` bắt đầu bằng `[` mà không quote.
