---
name: find-research-funding
description: Run a deep, multi-agent web search for research funding (seed/small grants, industry research awards, compute credits, travel grants, visiting/mobility grants) matched to the researcher profile in funding-agent/profile.md, then build a sortable Excel file and an interactive web page. Use when the user asks to find, refresh, or update research funding / grant opportunities.
---

# Find research funding (orchestrator)

1. **Profile.** Read `funding-agent/profile.md`. If the user gives new details (field, stage,
   citizenship, funding types), update that file first. Ask only if citizenship or field is unknown.
2. **Clear old raw data** you are about to replace: `funding-agent/data/raw_*.json`.
3. **Spawn scouts in parallel** — one `funding-scout` agent (definition:
   `.claude/agents/funding-scout.md`; if that type isn't registered, use `general-purpose` and tell
   it to read that file) per category below. Give each: the profile path, today's date, the
   category, 15–25 seed leads, a minimum count (12–15), and its output path
   `funding-agent/data/raw_<slug>.json`.
   | slug | category |
   |---|---|
   | travel | Conference / workshop / summer-school travel grants |
   | visiting | Short-term visiting, exchange and mobility grants |
   | seed_intl | Seed grants from international foundations, development & philanthropic funders |
   | industry | Industry research awards + compute/cloud credits |
   | pakistan | Home-country national + bilateral programs (adapt to the profile's country) |
   Seed leads for the last run are in `funding-agent/README.md`.
4. **Merge & build.** When all scouts finish: `python3 funding-agent/build_outputs.py`
   (dedupes, sorts, writes `funding-agent/output/funding_opportunities.xlsx`,
   `funding-agent/output/funding_explorer.html`, `funding-agent/data/master.json`).
   If fewer than 50 unique items result, send the weakest-category scout back for more.
5. **Recalculate** the workbook formulas (xlsx skill `scripts/recalc.py`), then publish the HTML
   with the Artifact tool (reuse the existing artifact URL if one exists) and report:
   total count, per-category counts, the 5 nearest deadlines, and any "Check" items.
