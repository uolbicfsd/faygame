# Research Funding Agent

A reusable multi-agent deep-research tool that finds research funding for one researcher
profile and builds a sortable spreadsheet plus an interactive web page.

## What's here
| Path | Purpose |
|---|---|
| `profile.md` | Your profile (field, stage, citizenship, funding types). Edit to retarget. |
| `../.claude/agents/funding-scout.md` | The research sub-agent: searches, opens official pages, verifies nationality eligibility, writes JSON. |
| `../.claude/skills/find-research-funding/SKILL.md` | Orchestrator: runs 5 scouts in parallel, merges, builds outputs. |
| `data/raw_*.json` | One file per scout (travel, visiting, seed_intl, industry, pakistan). |
| `data/master.json` | De-duplicated, sorted master list. |
| `build_outputs.py` | Merge + build `output/funding_opportunities.xlsx` and `output/funding_explorer.html`. |
| `explorer_template.html` | Web page template (data injected at build time). |

## Re-run it
In Claude Code, in this repo: **`/find-research-funding`** (or "refresh my funding list").
To rebuild outputs only after hand-editing the JSON: `python3 funding-agent/build_outputs.py`.

## Last run: 2026-10-31
88 unique opportunities (44 confirmed open to Pakistani nationals, 25 likely, 19 to check):
Seed grants 25 · Industry awards 4 · Compute credits 13 · Travel grants 19 · Visiting/mobility 27.

Removed after verification: PSF Travel Grant (suspended June 2026), TWAS Research Grants (no 2026 call),
NVIDIA Academic Grants (paused), Microsoft AFMR (ended), Pak-Turk Mobility (suspended), Sony Research
Award (Pakistan not eligible), TWAS-DFG visits (Africa/MENA only), JSPS short-term postdoc (region-restricted).

Seed leads used per scout are in the orchestrator prompts; add new funders you hear about to
the relevant scout's lead list when you re-run.
