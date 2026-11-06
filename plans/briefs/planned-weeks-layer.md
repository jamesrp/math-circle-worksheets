# Brief: a "planned" layer for the Weeks 101–208 plans

**For Codex.** Written by Claude on November 6, 2026. Work board line: "Catalog: planned layer for the Weeks 101–208 draft plans". Background: [plans/drafts/weeks-101-plus/README.md](../drafts/weeks-101-plus/README.md), [plans/corpus-plan.md](../corpus-plan.md), [catalog/README.md](../../catalog/README.md).

## Goal

James likes the explorer and asked whether Weeks 101–208 are on it. They aren't: the catalog has Weeks 1–100 (101 themes with 1e), 90 atlas families and 12 draft themes. The 108 plans in `plans/drafts/weeks-101-plus/` are markdown only, with no student pages, guide, review card or pilot. Put them in the catalog and the explorer as a third, clearly separate kind, **plan**, so a reader can browse the whole intended corpus without mistaking a plan for a worksheet. Change no plan, week, draft or path record.

## Steps

Work on a branch from fetched `origin/main`.

1. **Records.** One file per plan in `catalog/plans/week-1NN.toml`, 108 in all. Fields, all taken from the plan file (add no new claims; shorten, don't rewrite the mathematics):
   - `id` ("101"), `title`, `file` (the plan's path), `status = "plan"`, `date` (from the plan's status line);
   - `area` (the plan's strand, as a `concepts.toml` area id) and `field` (its deep-math field, free text);
   - `hook` (one sentence from "A kid-friendly way in"), `math` (two or three sentences from "The deep idea", keeping its proved / checked / open distinctions);
   - `concepts` and `mechanisms`, using existing ids from `concepts.toml` where they fit. Add a new concept only when no existing one is close, and list every concept you add in the report;
   - `bands` (the bands its "By band" section gives an entry for), `materials` (from the plan; empty list if none);
   - `related`: 0–6 links to existing weeks from "Nearest existing themes", with the usual relation kinds and a one-line note;
   - optional `pick = true` for the plans the README's index names as strongest picks.
   A small extraction script is fine for title, date, strand and file; fill concepts, mechanisms, bands and related by reading each plan. Keep any script in `catalog/` only if `build.py` needs it; otherwise leave it out of the commit.
2. **Validate in `catalog/build.py`.** Stop the build when: a plan file in `plans/drafts/weeks-101-plus/week-*.md` has no record, or a record's `file` is missing; ids repeat or collide with a week record; a required field is missing; `status` is not `plan`; or a concept, mechanism, area, band, week or relation kind is unknown. Plans never count toward any readiness rung, the six-year path or a collection; the build stops if a collection names one.
3. **Explorer.** Add "Plans" to the library chips, **off by default**, so the default view is unchanged. Give plans their own look (for example a dotted outline and a grey "plan" pill, distinct from the yellow draft style) and list them after drafts. Their detail panel opens with one line, in plain words: "Draft plan only: no pages, guide, review or pilot yet. Unproven with children." Then hook, mathematics, field, bands, materials, related weeks and a link to the plan file on GitHub. Plans may appear in the concept map and network when the Plans chip is on, never in the path. Rung and Collection filters exclude them. Keep the page one self-contained file.
4. **CATALOG.md and readiness.** Add a "Draft plans, Weeks 101–208" section after the drafts, with one compact table (week, title, area, bands, link) grouped by area. In `plans/readiness.md`, add one line under the headline table: "Draft plans with no pages: 108", and in the By area table one extra column "Draft plans". List these report changes in your report; nothing else in the report should change.
5. **Docs.** Add the plan record to `catalog/README.md` with a field table, as for draft themes, and say how a plan becomes a draft theme (pages drafted with the worksheet workflow, then a draft record replaces the plan record in the same change).

## Checks

- `python3 catalog/build.py`, `python3 catalog/check_path.py` and `python3 catalog/readiness.py --print` run clean, and a second build leaves no diff.
- Break each new rule once on a scratch copy and confirm a clear message; commit no broken data.
- In a browser: with Plans off, the list, filters and counts match today's build; with Plans on, 108 plans appear and each detail panel shows the "Draft plan only" line. Say whether you looked in a browser.
- Spot-check ten records against their plan files (title, bands, related weeks) and name them in the report.
- `git diff --stat` touches only `catalog/`, `explorer/index.html`, `CATALOG.md`, `plans/readiness.md` and the work board.

## Waits for Claude

Nothing before you start. Claude reviews the result and republishes the claude.ai explorer page; don't publish it.

## Report

Counts (records, new concepts added and why), the validation rules, anything in the plans that didn't fit the fields, the ten spot-checks, and whether you looked in a browser.
