#!/usr/bin/env python3
"""Merge targeted re-check results (data/<prefix>_*.json) back into data/verified_*.json by
program name, then print verdict changes. Usage: python3 apply_recheck.py [prefix]
(default prefix: phd_recheck)."""
import glob
import json
import sys
from pathlib import Path

DATA = Path(__file__).resolve().parent / "data"
prefix = sys.argv[1] if len(sys.argv) > 1 else "phd_recheck"

updates = {}
for f in sorted(glob.glob(str(DATA / f"{prefix}_[0-9]*.json"))):
    for r in json.loads(Path(f).read_text()):
        updates[r["name"]] = r

changed, applied = [], set()
for f in sorted(glob.glob(str(DATA / "verified_*.json"))):
    rows = json.loads(Path(f).read_text())
    for i, r in enumerate(rows):
        u = updates.get(r["name"])
        if not u:
            continue
        if u.get("verdict") != r.get("verdict"):
            changed.append(f'{r["name"][:70]}: {r.get("verdict")} -> {u.get("verdict")}')
        u.pop("id", None)
        u.pop("source_scout", None)
        rows[i] = {**r, **u}
        applied.add(r["name"])
    Path(f).write_text(json.dumps(rows, indent=2, ensure_ascii=False))

print(f"applied {len(applied)}/{len(updates)} updates")
missing = set(updates) - applied
if missing:
    print("not matched:", *sorted(missing), sep="\n  ")
print(f"{len(changed)} verdict changes:", *changed, sep="\n  ")
