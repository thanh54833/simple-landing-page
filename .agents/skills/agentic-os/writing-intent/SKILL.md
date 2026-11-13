---
name: writing-intent
description: Use when capturing a raw idea, ticket, or incident alert as an intent.md proto-spec before any design. Fires on requests to write intent.md, turn a ticket into intent, convert an incident alert into a new intent, capture a proto-spec through analyst questions without designing, or revise an unaccepted draft. NOT for writing spec.md, implementation plans, or code.
---

## Local Overrides (Notion hub ai-engineer)

- Agent đọc skill này khi user muốn ghi `intent.md` proto-spec trước design (source: idea, ticket, alert). Không dùng để viết spec, plan, code.
- Viết xong `intent.md` thì DỪNG. Không endpoint, file path, estimate, không gọi `writing-plans`. Accept là việc của product owner (merge hoặc đóng review).
- Skill này fire TRƯỚC `brainstorming`, không nhét vào plugin Superpowers, không copy vào thư mục Superpowers.
- Tiny/Quick (việc nhỏ trên flow có sẵn: typo, rename, comment, format, hằng số, flag, chỉnh một endpoint có sẵn mà giữ nguyên contract, sửa một file; 1–2 file, không cần tiêu chí chấp nhận mới) thì `intent.md` là tuỳ chọn: ngắn, mỗi mục một dòng, chỉ viết khi user muốn ghi lại. Lane `[/intent →] /implement` → `/verify` → `/ship`, không spec, không plan.
- Hotfix (production hỏng, mục tiêu khôi phục hành vi cũ) cũng khỏi `intent.md`: lane là `/debug` → `/verify` → `/ship`, bắt đầu thẳng từ `/debug`.
- Policy must-hold (PII, auth, path cấm) không nhét vào skill này. Skill là advisory; hook hoặc review ở stage sau.
- Nguồn Notion: Skill intent-md trước design (hub ai-engineer) — SKILL.md local thắng nếu lệch.

# Intent Capture (Before Design)

## Overview

An intent is a proto-spec in the originator's own words, written before any approach exists. Core principle: intent stops where design starts — problem, outcome, users, constraints, open questions, never how to build it.

## When to Use

- User asks to write an `intent.md`, capture an idea, or brainstorm a proto-spec without designing
- Turning a ticket into intent (keep a `Source ref` to the ticket)
- Turning an incident alert into a new intent file (never edit an old spec in place)
- Revising a draft that is not yet accepted

When NOT to use: writing `spec.md` from an accepted intent, running `writing-plans`, implementing from a `plan.md`, or a Tiny/Quick change the user does not want recorded.

## Hard Gate

Before any design or implementation action — including invoking `brainstorming`, `writing-plans`, writing product code, scaffolding, or shaping APIs — the accepted `intent.md` must exist. If the user asks for a spec in the same turn, still write `intent.md` first and say design is a separate gate. Approval of an idea does not approve a spec; approval of a spec does not approve a plan.

## Workflow

1. **Classify source** — `idea`, `ticket`, or `alert`. If missing, ask once.
2. **Ask analyst questions one at a time** — what cannot be done today, who is affected, what better looks like, what is out of scope. Multiple choice when real options exist.
3. **Keep the originator's words** in Problem and Proposed outcome. Unconfirmed assumptions go to Open questions, never Constraints.
4. **Classify** — fill `## Classification` from the Classification table below. Every row's predicate must be answered (yes / no / unknown) from the answers so far; ask the missing ones, one at a time. Unknown after asking → list it in Open questions and mark `Class` as `provisional`.
5. **Write from the template below.** Status stays `draft` unless the user explicitly accepts. Default path `docs/physarum/intents/YYYY-MM-DD-<slug>-intent.md` — same root and date-stem naming as Superpowers specs/plans; `<slug>` is kebab-case from the outcome (not the task name), date is creation date. Reuse the same date+topic stem for the later spec and plan so the chain sorts together.
6. **Hand the file to the originator for correction**, with the proposed Class and Lane stated in one line for them to confirm or change. Do not commit unless asked.
7. **On accept:** set `Status: accepted` plus `Accepted by` (name + date). Do not start design.

## Template

```markdown
# Intent: <outcome name, not task name>
- Status: draft
- Originator: <role or name>
- Source: idea
- Source ref: —
- Accepted by: —
## Problem
## Proposed outcome
## Affected users and systems
## Constraints
## Out of scope
## Open questions
## Classification
- Class: <T0 | T1 | T3> (proposed, or provisional)
- Lane: <gates in order, from the table>
- Signals: <predicates that matched, one line>
```

| Field | Write | Never write |
|---|---|---|
| Problem | Current pain, who, frequency if known | The fix |
| Proposed outcome | What the user sees or can do when done | How to build it |
| Affected users and systems | Roles and system names | File paths, endpoints |
| Constraints | Decided non-negotiables (PII, auth, format, SLA) | Guesses |
| Out of scope | Adjacent work excluded this time | Roadmap |
| Open questions | Unanswered analyst questions | Decided matters |

| Classification | Class, Lane, matched Signals | Approach, options, estimates |

Prose follows the user's language; labels stay English. Longer than one page means it is becoming a PRD — cut it.

## Classification

Source: the stage-gate reference §6 (the file was removed from the working tree; see git history). Codes rise with risk (T0 lowest, T3 highest). Evaluate in that order, highest code first (T3, T2, T1, then T0); the first predicate that is yes wins. The table below lists rows ascending, so read it from the bottom up.

| Class | Predicate (observable from the intent) | Lane after accept |
|---|---|---|
| T0 Tiny/Quick | None of T1–T3: a small change on an existing flow (typo, rename, comment, format, constant, flag, a tweak to an existing endpoint that keeps its contract, one-file fix) that touches 1–2 files and needs no new acceptance criteria; more files than that is not T0 (T1, or T3 when it spans modules) | `/implement` → `/verify` → `/ship`; an intent, if written, is optional and short, and with none `/implement` takes the request from chat |
| T1 Feature | Adds or changes behavior users see, so acceptance criteria are needed | `/spec` → `/plan` → `/implement` → `/verify` → `/ship` |
| T2 Hotfix/Debug | Production is broken now (an alert, an incident, a report from live); the goal restores existing behavior, no new behavior. An alert that calls for new behavior or a schema, auth, or contract change is not T2: it gets a new intent (T1 or T3) | No intent needed — say so, name `/debug` → `/verify` → `/ship`, and stop |
| T3 Architecture | Changes a data schema, auth model, public contract, event flow, or spans more than one module/system; or is hard to reverse | `/spec` → `/adr` → `/plan` → `/implement` → `/verify` → `/ship` |

- Classification states impact, never approach: "touches the orders schema" is a signal; "add a column" is design.
- A Tiny/Quick change that turns out to need new acceptance criteria or to touch more than 1–2 files is reclassified to T1 at `/implement`: stop and run the T1 lane.
- A T2 Hotfix/Debug whose fix turns out to need a schema, auth, or contract change is reclassified to T3 at `/debug`: stop and write an intent for the T3 lane.
- Scope grows after accept → reclassify upward, add the missing gates; never skip gates in the lane.

## Handoff

1. This skill writes `intent.md` and stops. PO accepts by merge.
2. Only then run the first command of the intent's `Lane`. For `/spec`: invoke Superpowers, point it at the intent file, run `brainstorming` architectural path. Spec and plan use Superpowers defaults — `docs/physarum/specs/YYYY-MM-DD-<topic>-design.md`, then `writing-plans` writes `docs/physarum/plans/YYYY-MM-DD-<feature-name>.md`. Keep the same date+topic stem across all three.
3. After spec approval, `writing-plans` writes the plan. Three gates, three folders (`intents/`, `specs/`, `plans/`), one stem. A hotfix has no intent, spec or plan: `/debug` writes one record in `hotfixes/` instead. A Tiny/Quick change has at most a short intent (or none): `/implement` takes the intent, or the request in chat, directly.

## Common Mistakes

- Designing approaches inside intent (2-3 options, architecture, data flow) — that is Stage 2, a separate gate
- File paths, endpoints, or estimates in any field
- Guesses filed under Constraints instead of Open questions
- Copying domain facts from a past example into a new intent
- Starting `brainstorming` or `writing-plans` before PO acceptance
