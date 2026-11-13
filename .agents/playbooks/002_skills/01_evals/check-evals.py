#!/usr/bin/env python3
"""Check evals/ of a skill folder. Usage: check-evals.py <skill-dir>"""
import json, re, sys
from pathlib import Path

GENERIC = re.compile(
    r"^(works?|handles?|does)\b.*\b(correctly|properly|right thing)\b|creates the necessary|uses the \w+ graph",
    re.I,
)
STUB = re.compile(r"TODO|TBD|ten-skill|ten_test_ro_rang|câu positive|đúng câu user", re.I)

def main(skill_dir):
    root = Path(skill_dir)
    errs = []
    # Flat layout (e.g. .commands/evals/<cmd>/) keeps the files beside each other.
    evdir = root if (root / "evals.json").exists() else root / "evals"

    def load(name):
        p = evdir / name
        if not p.exists():
            errs.append(f"{name}: missing")
            return None
        try:
            d = json.loads(p.read_text())
        except Exception as e:
            errs.append(f"{name}: invalid JSON ({e})")
            return None
        if d.get("skill") != root.name:
            errs.append(f"{name}: skill '{d.get('skill')}' != folder '{root.name}'")
        if STUB.search(p.read_text()):
            errs.append(f"{name}: stub/TODO/placeholder text found")
        return d.get("test_cases", [])

    ev = load("evals.json")
    if ev is not None:
        if len(ev) < 3:
            errs.append(f"evals.json: {len(ev)} test cases (<3)")
        seen = set()
        for c in ev:
            n = c.get("name", "?")
            if not c.get("input"):
                errs.append(f"evals.json[{n}]: empty input")
            a = c.get("assertions") or []
            if not a:
                errs.append(f"evals.json[{n}]: no assertions")
            for s in a:
                if GENERIC.search(s.strip()):
                    errs.append(f"evals.json[{n}]: generic assertion: {s!r}")
                if s in seen:
                    errs.append(f"evals.json[{n}]: duplicate assertion across cases: {s!r}")
                seen.add(s)

    tr = load("triggers.json")
    if tr is not None:
        if len(tr) < 3:
            errs.append(f"triggers.json: {len(tr)} triggers (<3)")
        if not any(t.get("should_trigger") is False for t in tr):
            errs.append("triggers.json: no negative (should_trigger: false)")
        if not any(t.get("should_trigger") is True for t in tr):
            errs.append("triggers.json: no positive")

    for e in errs:
        print("ERROR", e)
    print(f"{len(errs)} error")
    return 1 if errs else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1]) if len(sys.argv) > 1 else 2)
