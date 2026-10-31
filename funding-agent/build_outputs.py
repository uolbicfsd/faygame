#!/usr/bin/env python3
"""Merge scout JSON files into a de-duplicated master list, then build
   output/funding_opportunities.xlsx and output/funding_explorer.html.

Usage:  python3 funding-agent/build_outputs.py
"""
import glob
import json
import re
from datetime import date
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.table import Table, TableStyleInfo

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
OUT = ROOT / "output"
OUT.mkdir(exist_ok=True)

CATEGORIES = [
    "Seed/Small Research Grant",
    "Industry Research Award",
    "Compute/Cloud Credits",
    "Travel Grant",
    "Visiting/Mobility Grant",
]
FIELDS = [
    ("id", "#", 5), ("name", "Program", 34), ("funder", "Funder", 26),
    ("funder_country", "Funder country", 14), ("category", "Category", 22),
    ("amount", "Amount", 28), ("duration", "Duration", 16),
    ("deadline", "Next / typical deadline", 22), ("status", "Status", 11),
    ("pakistan_eligible", "Pakistan eligible?", 12), ("eligibility", "Eligibility", 40),
    ("eligibility_note", "Nationality rule (verified)", 44), ("ai_fit", "CS/AI fit", 9),
    ("how_to_apply_tip", "Beginner tip", 44), ("url", "Official link", 40),
    ("verified_on", "Verified on", 12), ("source_scout", "Found by", 12),
]


def norm(s):
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


def canon_category(c):
    c = (c or "").lower()
    if "compute" in c or "cloud" in c or "credit" in c:
        return "Compute/Cloud Credits"
    if "industry" in c:
        return "Industry Research Award"
    if "travel" in c:
        return "Travel Grant"
    if "visit" in c or "mobility" in c or "exchange" in c:
        return "Visiting/Mobility Grant"
    return "Seed/Small Research Grant"


def deadline_key(d):
    m = re.search(r"(\d{4})-(\d{2})-(\d{2})", d or "")
    if m:
        return (0, m.group(0))
    if "rolling" in (d or "").lower():
        return (1, "")
    return (2, d or "")


def load():
    items, seen = [], {}
    for f in sorted(glob.glob(str(DATA / "raw_*.json"))):
        scout = Path(f).stem.replace("raw_", "")
        try:
            rows = json.loads(Path(f).read_text())
        except json.JSONDecodeError as e:
            print(f"!! skipping {f}: {e}")
            continue
        for r in rows:
            r = {k: (str(v).strip() if v is not None else "") for k, v in r.items()}
            r["category"] = canon_category(r.get("category"))
            r["source_scout"] = scout
            if r.get("pakistan_eligible") not in ("Yes", "Likely", "Check"):
                r["pakistan_eligible"] = "Check"
            keys = {norm(r.get("name")), norm(r.get("url")).rstrip("/")}
            keys.discard("")
            dup = next((seen[k] for k in keys if k in seen), None)
            if dup is not None:  # keep the richer record
                if len(json.dumps(r)) > len(json.dumps(items[dup])):
                    items[dup] = r
                continue
            for k in keys:
                seen[k] = len(items)
            items.append(r)
    items.sort(key=lambda r: (CATEGORIES.index(r["category"]), deadline_key(r.get("deadline")), r.get("name", "")))
    for i, r in enumerate(items, 1):
        r["id"] = i
    return items


def build_xlsx(items, path):
    wb = Workbook()
    base = Font(name="Arial", size=10)
    head = Font(name="Arial", size=10, bold=True, color="FFFFFF")
    fill = PatternFill("solid", fgColor="0B5D4B")

    ws = wb.active
    ws.title = "Opportunities"
    for c, (_, label, width) in enumerate(FIELDS, 1):
        cell = ws.cell(row=1, column=c, value=label)
        cell.font, cell.fill = head, fill
        cell.alignment = Alignment(wrap_text=True, vertical="center")
        ws.column_dimensions[get_column_letter(c)].width = width
    elig_fill = {"Yes": "D8F0E3", "Likely": "FFF1C7", "Check": "F9D9D3"}
    for r_i, r in enumerate(items, 2):
        for c, (key, _, _) in enumerate(FIELDS, 1):
            cell = ws.cell(row=r_i, column=c, value=r.get(key, ""))
            cell.font = base
            cell.alignment = Alignment(wrap_text=True, vertical="top")
            if key == "url" and r.get("url", "").startswith("http"):
                cell.hyperlink = r["url"]
                cell.font = Font(name="Arial", size=10, color="0563C1", underline="single")
            if key == "pakistan_eligible":
                cell.fill = PatternFill("solid", fgColor=elig_fill[r[key]])
    last = len(items) + 1
    tbl = Table(displayName="Opportunities", ref=f"A1:{get_column_letter(len(FIELDS))}{last}")
    tbl.tableStyleInfo = TableStyleInfo(name="TableStyleLight1", showRowStripes=True)
    ws.add_table(tbl)
    ws.freeze_panes = "C2"

    s = wb.create_sheet("Summary", 0)
    s["A1"] = "Research funding opportunities: CS/AI early-career postdoc, Pakistani national"
    s["A1"].font = Font(name="Arial", size=13, bold=True)
    s["A2"] = f"Generated {date.today().isoformat()} by the funding-scout research agent. Counts below are live formulas over the Opportunities sheet."
    s["A2"].font = Font(name="Arial", size=9, italic=True)
    hdr = ["Category", "Total", "Pakistan: Yes", "Likely", "Check"]
    for c, h in enumerate(hdr, 1):
        cell = s.cell(row=4, column=c, value=h)
        cell.font, cell.fill = head, fill
    cat_col, el_col = "E", "J"
    rng = lambda col: f"Opportunities!${col}$2:${col}${last}"
    for i, cat in enumerate(CATEGORIES, 5):
        s.cell(row=i, column=1, value=cat)
        s.cell(row=i, column=2, value=f'=COUNTIF({rng(cat_col)},A{i})')
        for j, lvl in enumerate(["Yes", "Likely", "Check"], 3):
            s.cell(row=i, column=j, value=f'=COUNTIFS({rng(cat_col)},$A{i},{rng(el_col)},"{lvl}")')
    t = 5 + len(CATEGORIES)
    s.cell(row=t, column=1, value="Total")
    for c in range(2, 6):
        L = get_column_letter(c)
        s.cell(row=t, column=c, value=f"=SUM({L}5:{L}{t-1})")
    for row in s.iter_rows(min_row=5, max_row=t):
        for cell in row:
            cell.font = Font(name="Arial", size=10, bold=(cell.row == t))
    notes = [
        "How to read 'Pakistan eligible?':",
        "Yes = official page explicitly allows Pakistani nationals (named, 'all countries', or a developing-country list that includes Pakistan).",
        "Likely = open-call wording with no nationality restriction found, but not stated explicitly.",
        "Check = eligibility depends on host/partner country or was unclear; confirm with the funder before applying.",
        "Deadlines change every cycle. Always confirm the date on the official link before planning.",
    ]
    for k, n in enumerate(notes, t + 2):
        s.cell(row=k, column=1, value=n).font = Font(name="Arial", size=9, bold=(k == t + 2))
    s.column_dimensions["A"].width = 30
    for L in "BCDE":
        s.column_dimensions[L].width = 13
    wb.save(path)


def build_html(items, path):
    tpl = (ROOT / "explorer_template.html").read_text()
    payload = json.dumps(items, ensure_ascii=False).replace("</", "<\\/")
    html = tpl.replace("__DATA__", payload).replace("__DATE__", date.today().isoformat())
    Path(path).write_text(html)


if __name__ == "__main__":
    items = load()
    build_xlsx(items, OUT / "funding_opportunities.xlsx")
    build_html(items, OUT / "funding_explorer.html")
    (DATA / "master.json").write_text(json.dumps(items, indent=2, ensure_ascii=False))
    by = {c: sum(r["category"] == c for r in items) for c in CATEGORIES}
    print(f"{len(items)} unique opportunities -> {OUT}")
    for c, n in by.items():
        print(f"  {c}: {n}")
