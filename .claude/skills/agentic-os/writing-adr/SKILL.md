---
name: writing-adr
description: Use when an approved design spec may contain architecture decisions that are hard to reverse, surprising without context, and the result of a real trade-off, and they must be recorded as ADRs before planning. Fires on requests to write an ADR, record an architecture decision, run the G2+ gate, or check whether a spec needs an ADR. NOT for writing specs, implementation plans, README/changelog/API docs, or code comments.
---

## Local Overrides (Notion hub ai-engineer)

- Agent đọc skill này ở gate G2+, giữa spec đã approve và `writing-plans`. Mặc định là "không cần ADR"; chỉ viết ADR khi quyết định qua bộ lọc bên dưới.
- Viết xong ADR thì DỪNG ở `Status: accepted` (user accept). Không gọi `writing-plans`, không sửa code.
- ADR là record vĩnh viễn: dùng chung toàn repo ở `docs/superpowers/adr/`, không gắn thư mục theo feature. Không xóa ADR cũ; quyết định đổi thì viết ADR mới và đánh dấu supersede.
- Quyết định load-bearing (paradigm, stack, ranh giới lớn) do user chọn; agent chỉ trình bày phương án và đề xuất, không tự quyết.
- Nguồn tham chiếu: agent-skills `documentation-and-adrs`, mattpocock `domain-modeling/ADR-FORMAT.md`, BMAD `bmad-architecture` (read-only trong `00_sdlc_docs/`). SKILL.md local thắng nếu lệch.

# Writing ADRs (G2+ gate)

## Overview

An ADR records *why* a significant technical decision was made: the context, the alternatives, the consequences. Code shows what was built; the ADR keeps the reasoning so no future human or agent re-decides it blindly. Core principle: most specs need no ADR — write one only when the decision earns it.

## When to Use

- A spec was approved and `/adr` (G2+) is the next gate
- User asks to record an architecture decision, or asks whether a spec needs an ADR
- Reclassification discovered architecture-level change mid-task (T4)

When NOT to use: writing the spec itself, implementation plans, README/changelog/API docs, comments in code, throwaway prototypes.

## Hard Gate

An approved spec must exist. No spec, or spec not approved → STOP and point to `/spec`. Do not write an ADR from a bare idea. Do not invoke `writing-plans` — planning is a separate gate.

## Workflow

1. **Scan.** Read the spec. List candidate decisions: technology with lock-in, data model/schema, auth/integration pattern, boundary and ownership rules, deliberate deviations from the obvious path, constraints invisible in code (compliance, SLA, partner contract).
2. **Filter.** A candidate becomes an ADR only if ALL THREE hold:
   1. **Hard to reverse** — changing your mind later costs meaningfully.
   2. **Surprising without context** — a future reader would wonder "why on earth this way?"
   3. **A real trade-off** — genuine alternatives existed and one was picked for specific reasons.

   Also apply the invariant test: if two units built independently could choose incompatibly here, and the call is non-obvious, it belongs in an ADR. Candidates that fail go under `Deferred` in the spec, not in an ADR.
3. **Match convention.** Inspect `docs/superpowers/adr/` (and any `.adr-dir`, project instructions) before writing. An existing scheme wins: location, extension, numbering, filename pattern, headings. If evidence conflicts, surface the conflict to the user — never introduce a second scheme. If no `docs/superpowers/adr/` exists, create it lazily and start at `0001`. Next number = highest existing + 1.
4. **Choose mode.** Coaching (default for T4): lay out 2–3 realistic alternatives with a recommendation and let the user choose each load-bearing call. Fast: draft the ADR with `[ASSUMPTION]` tags and let the user correct. Never silently decide a load-bearing call.
5. **Write** each ADR to `docs/superpowers/adr/NNNN-<slug>.md` from the template below. `<slug>` is kebab-case from the decision.
6. **Self-check** before asking for accept: no placeholders or `[ASSUMPTION]` left; at least one rejected alternative with a reason; no contradiction with the spec or earlier ADRs; `Binds` and `Prevents` filled.
7. **Record in the spec.** Append or update a `## Decisions` section in the spec, one line per outcome:
   - `- ADR: docs/superpowers/adr/NNNN-slug.md (accepted)`
   - `- Deferred: <decision> — <revisit condition>`
   - `- No ADR needed: <one-line reason>` (when nothing passed the filter)
8. **Ask the user to accept.** On accept set `Status: accepted` in each ADR. Then STOP.

## Template

```markdown
# NNNN: <short decision>

- Status: proposed
- Date: YYYY-MM-DD
- Spec: <stem YYYY-MM-DD-slug>
- Binds: <which units/areas this constrains>
- Prevents: <which divergence this stops>

## Context
<forces and constraints, 2-5 sentences>

## Decision
<what we chose, one paragraph>

## Alternatives considered
### <option>
- Rejected: <reason>

## Consequences
<downstream effects, including non-obvious ones>
```

`Status` values: `proposed | accepted | superseded by NNNN | deprecated`. A decision that changes gets a NEW ADR with `Supersedes: NNNN`; the old ADR is updated only to `Status: superseded by NNNN` and otherwise left intact.

Prose follows the user's language; labels stay English. One ADR is one decision — split if it records two.

## Handoff

1. This skill writes ADR(s) + the spec's `## Decisions` section and stops. The user accepts.
2. Only then `/plan <spec>` runs `writing-plans`. `/plan` STOPS if the spec links an ADR that is not `accepted`; `/verify` returns `NOT READY` for the same reason.

## Common Mistakes

- Writing an ADR for an easy-to-reverse or obvious choice — it just becomes noise
- Recording only the decision, not the rejected alternatives
- Introducing a new numbering/format scheme next to an existing one
- Deleting or rewriting an old ADR instead of superseding it
- Deciding a load-bearing call without showing the user the alternatives
- Starting `writing-plans` before the ADRs are accepted
