#!/usr/bin/env python3
"""Validate a task set folder and keep its AGENTS.md table in sync.

Usage: python3 check_task_set.py <.tasks/NN_name> [--fix]
--fix rewrites AGENTS.md from templates/AGENTS.md. Exit 1 on any problem.
"""
import json
import re
import sys
from pathlib import Path

STATUSES = {"pending", "in_progress", "done", "failed", "skipped"}
FINISHED = {"done", "failed", "skipped"}
PLACEHOLDER = re.compile(r"\{\{[^{}]*\}\}|T0NN")
TEMPLATE = Path(__file__).resolve().parent.parent / "templates" / "AGENTS.md"


def rows(tasks):
    out = []
    for tid, t in tasks.items():
        out.append(f"| {tid} | | {t.get('title', '')} | {t.get('status', '')} |")
        for sid, s in t.get("subtasks", {}).items():
            out.append(f"| {tid} | {sid} | {s.get('title', '')} | {s.get('status', '')} |")
    return out


def render(data):
    text = TEMPLATE.read_text()
    meta = data["meta"]
    text = text.replace("{{NN_name}}", meta["task_set"]).replace("{{meta.goal}}", meta["goal"].rstrip("."))
    return text.replace("{{table rows: see reference/task-format.md}}", "\n".join(rows(data["tasks"])))


def check_item(path, item, errors, subtask):
    keys = ("title", "prompt", "expect") if subtask else ("title",)
    for k in keys:
        if not str(item.get(k, "")).strip():
            errors.append(f"{path}: missing {k}")
    if item.get("status") not in STATUSES:
        errors.append(f"{path}: bad status {item.get('status')!r}")
    if not isinstance(item.get("note"), str):
        errors.append(f"{path}: note must be a string")
    elif item.get("status") in FINISHED and not item["note"].strip():
        errors.append(f"{path}: status {item['status']} needs a note")


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) != 1:
        sys.exit(__doc__)
    folder = Path(args[0])
    errors = []
    if not re.fullmatch(r"\d{2}_[a-z0-9_]+", folder.name):
        errors.append(f"folder name {folder.name!r} must be NN_snake_case")
    try:
        raw = (folder / "00_tasks.json").read_text()
        data = json.loads(raw)
    except (OSError, ValueError) as e:
        sys.exit(f"cannot read 00_tasks.json: {e}")
    for m in PLACEHOLDER.finditer(raw):
        errors.append(f"placeholder left in file: {m.group(0)}")
    meta = data.get("meta", {})
    for k in ("task_set", "name", "goal", "generated_at"):
        if not str(meta.get(k, "")).strip():
            errors.append(f"meta.{k} missing")
    if meta.get("task_set") != folder.name:
        errors.append("meta.task_set must equal the folder name")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(meta.get("generated_at", ""))):
        errors.append("meta.generated_at must be YYYY-MM-DD")
    tasks = data.get("tasks", {})
    if not tasks:
        errors.append("no tasks")
    for n, (tid, t) in enumerate(tasks.items(), 1):
        if tid != f"T{n:03d}":
            errors.append(f"{tid}: expected T{n:03d} (contiguous ids)")
        check_item(tid, t, errors, False)
        subs = t.get("subtasks")
        own = "prompt" in t or "expect" in t
        if subs and own:
            errors.append(f"{tid}: has subtasks and its own prompt/expect; use one form")
        if not subs and not (t.get("prompt", "").strip() and t.get("expect", "").strip()):
            errors.append(f"{tid}: needs subtasks or its own prompt and expect")
        for k, (sid, s) in enumerate((subs or {}).items(), 1):
            if sid != f"{tid}.{k}":
                errors.append(f"{sid}: expected {tid}.{k}")
            check_item(sid, s, errors, True)
        if subs and t.get("status") == "done" and any(
            s.get("status") not in ("done", "skipped") for s in subs.values()
        ):
            errors.append(f"{tid}: done while a subtask is not done or skipped")
    if tasks and list(tasks.values())[-1].get("title", "").lower().find("verify") < 0:
        errors.append("last task must be the verify task (templates/tasks/verify.json)")
    if not errors:
        expected = render(data)
        agents = folder / "AGENTS.md"
        if "--fix" in sys.argv:
            agents.write_text(expected)
        elif not agents.exists() or agents.read_text() != expected:
            errors.append("AGENTS.md out of sync with 00_tasks.json (run with --fix)")
    for e in errors:
        print("FAIL", e)
    print("OK" if not errors else f"{len(errors)} problem(s)")
    sys.exit(1 if errors else 0)


main()
