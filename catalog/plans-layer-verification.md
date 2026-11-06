# Planned-weeks layer verification

Implemented from [the brief](../plans/briefs/planned-weeks-layer.md), based on fetched main `d48efee6b0c705a7673b4dc0d3446b9abd505da4`. Row-only claim: `6cf7022005eca187c2519455c5123c22e0fc4dd5`; implementation branch: `codex/planned-weeks-layer`.

## Records and boundaries

108 records, exactly Weeks 101–208, read against all 108 source plans. All have the three proposed band entries. There are 15 numbered strongest picks (close-behind mentions are not marked). No new concepts or mechanisms: the existing vocabulary covers the plan descriptions. Analysis's seven plans map to the existing `chance` area; counts are networks 14, games 12, chance 17, number 14, symmetry 13, shape 16, logic 15, counting 7. Dates preserve the status lines' month precision, `2026-11`; no day has been inferred from research dates.

Source titles, files, dates, fields and bands were checked for every record. Concepts, mechanisms, materials and related links were assigned after reading each plan. Mathematics is shortened from the plans, retaining assumptions and proved/checked/open/observed distinctions. Related links target only existing weekly themes; atlas families, other plans and prior-year handouts do not fit that field. Those references, detailed checks, app ideas, physical prerequisites, overlap recommendations and unresolved questions remain in each linked source. No plan was adopted or approved, and no mathematical source was changed.

Plan sources, week/draft/path records, collection/use-log data, concepts, student pages, guides and approval states are unchanged. Existing explorer week, draft, atlas, relation, collection and path payloads compare exactly with the baseline; existing concept and network positions and default dimensions also remain unchanged. Default activity count remains 113 (101 themes + 12 drafts); adding Plans gives 221, with 108 plans. With atlas also selected there are 311 entries.

## Validation and browser checks

- Catalog build, standalone path checker and standalone readiness report pass with Python 3.12. The standalone report matches the build output byte for byte; a second build changes no output.
- 68 scratch negative builds pass across 13 test methods: missing records and sources; missing required fields; duplicate ids, sources and related weeks; week/draft id collisions; non-plan status; unknown concept/mechanism/area/band/week/relation/field; invalid dates and types; empty/oversized/duplicate lists; filename/source-id mismatch; out-of-tree or wrong source; invalid pick; malformed related data; plan membership through collections' weeks, drafts or plans; and a plan on the path. Diagnostics are clear and contain no traceback. Promotion is also checked: keeping both plan and draft fails, replacing the plan with a valid draft succeeds.
- Chrome ran **505 assertions**, including every one of the **108 detail panels** and their exact warning, title, related-week count and GitHub source link. Default list and area/reasoning/concept counts, every rung and collection count, and path/strand content match the baseline.
- Checked plans-only view, search including deep field, area clear, band, concept, mechanism, rung/collection exclusion, ready-next exclusion, repeated map toggles, network relation toggles, independent plan/draft visibility, reset, related navigation, direct plan links and reload. Plans chip and both map controls share one state; reset restores Plans off. Path and strands exclude plans even with Plans on.
- Inspected screenshots of desktop default, plan detail, concept map, network and path, plus phone dark detail and default list (390 px). No viewport overflow, browser page errors or console errors. The plan network panel resets its scroll so the warning is visible on repeated selections.
- JavaScript syntax and `git diff --check` pass. Extraction scripts, scratch fixtures, browser harness and screenshots stay outside the commit.

The only readiness-report changes are the line **Draft plans with no pages: 108** under the headline and the **Draft plans** column in By area; all previous report text and values are preserved.

## Ten named source spot-checks

Each checks the exact title, all three bands and every selected related week against Nearest existing themes. This is a selection of source-grounding checks, not new mathematical verification.

| Week | Title | Related weeks |
|---|---|---|
| 101 | Bead machines and the odd triangle | 42, 44, 76 |
| 108 | Hailstone numbers | 92, 79, 80, 74 |
| 115 | Wallpaper patterns | 35, 1, 1e, 34, 37 |
| 124 | One straight cut | 28, 35, 37, 9, 21 |
| 138 | Tiny machines and the busy beaver | 17, 72, 91, 11 |
| 155 | Weird dice | 24, 55, 42 |
| 164 | Three rings that hold together | 40, 41, 75 |
| 177 | Pirates share the gold | 7, 87 |
| 190 | Follow the loop to find your card | 3, 63, 43 |
| 208 | Long runs | 24, 44 |

No implementation blocker remains. Claude reviews the result and handles any later claude.ai republication; no publication is part of this source integration. GitHub Pages is a separate unclaimed task. Historical draft PR #6 is unchanged.
