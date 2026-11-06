# Changelog — writing-adr

Newest first. Heading đầu giữ cùng version với `../agentic-os-lock.json`.

## local-2026-10-14

- ADR dir chuyển từ `docs/adr/` sang `docs/superpowers/adr/` theo owner override (gom vào gate working area); command `/adr` và spec `## Decisions` đồng bộ theo.

## local-2026-10-09

- Initial self-built release: gate G2+ giữa spec approved và `writing-plans`.
- Filter 3 điều kiện (hard to reverse, surprising without context, real trade-off) + invariant test.
- Template `docs/adr/NNNN-<slug>.md` (Status, Binds, Prevents, Context, Decision, Alternatives, Consequences).
- `## Decisions` trong spec (`ADR:` / `Deferred:` / `No ADR needed`); DỪNG ở `Status: accepted`.
- Thêm `AGENTS.md` rule guide + `CHANGELOG.md` theo mẫu `blader/humanizer`.
