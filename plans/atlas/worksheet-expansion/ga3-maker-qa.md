# GA3 maker PDF quality record

Status: **CLOSED — maker QA and independent PDF review complete at v4; registered for assembly**. Date: 2026-09-26. Independent design approval is recorded in `review-ga3-design.md`; no design repair was requested. This note covers the isolated preview, not the final combined books.

## Current preview and hashes

Current immutable preview: `tmp/pdfs/atlas-remaining/ga3-preview-v4/`.

- student: 26 pages; SHA-256 `bccc9ee0ebeb73ebd5f7c414bf8ae9c13a3a0db20679e9cfa2fa68cca4c67ebc`. PDF: `tmp/pdfs/atlas-remaining/ga3-preview-v4/atlas-ga3-student-worksheets.pdf`.
- facilitator: 42 pages; SHA-256 `42a82b45dba9f2a13686e004149c68f97fce14096d5549263350a634dd9df357`. PDF: `tmp/pdfs/atlas-remaining/ga3-preview-v4/atlas-ga3-facilitator-guide.pdf`.

The student volume contains one contents page plus 25 staged bodies for GA-18,19,20,21,22,23,24,27. GA-23 uses four bodies; every other family uses three. The guide contains one contents page plus 41 guide bodies, including separate worked mirror, transport and flood figures. It preserves complete proofs, hints, extensions and source statements without a page cap.

Build command:

```sh
sh lowell-math-circle-year-2/source/atlas-remaining/build.sh --batch ga3 --output-dir tmp/pdfs/atlas-remaining/ga3-preview-v4
```

## What was inspected

Every student page 1–26 was inspected at full size. Initial pages 1–8 were read under the first preview; pages 9–26 were read under v2. A byte comparison confirmed the only first-preview-to-v2 student change was page 23 (the equal-scale circle/ellipse correction), which was inspected in v2. All five v2-to-v3 changed student pages — 14,16,20,24,25 — were reinspected at full size under the fresh v3 path. Thus every current student body has actual full-size coverage, with unchanged pages linked by byte identity rather than a claimed second visual pass.

All 42 current guide pages were inspected on the five v3 contact sheets. Full-size guide pages: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 21, 22, 23, 25, 26, 27, 28, 29, 30, 31, 33, 34, 35, 38, 39, 40, 41, 42. These 36 pages include every exact calculation/proof/extension, all worked diagrams, the contents, and dense source/gate pages. The remaining six pages contain lower-density setup, a single delayed hint, or source blocks and were covered on contacts. Full-size inspection checked the actual printed algebra, signs, endpoints, supplied assumptions and prompt/key alignment, not just whitespace.

## Repairs and fidelity

- The first guide build stopped on unsupported superscript T in an integral limit. The two occurrences of `∫₀ᵀ` in GA-20's guide extension now use explicit `∫[0,T]` notation. The limit and mathematics are unchanged; no shared font/helper was edited. The earlier progress message calling this a transpose symbol was mistaken: it was the integral's upper endpoint.
- The GA-24 circle/ellipse comparison now uses exactly 35 physical points per coordinate unit in both drawings, with radii 35 versus ellipse semiaxes 70 and 35. The small first-preview circle mismatch was repaired before v2.
- GA-22 Board II's C label was moved away from the y-axis label on student pages 14 and 16.
- The variable-longitude sphere caption explicitly says it is a schematic (student 20). The coordinate transport and exact angles remain in the supplied rule and proofs.
- Flood-grid y labels moved inside the upper-left side of the vertical axis, separating them from each level/title (students 24,25 and guide41).

The v2-to-v3 PNG comparison shows exactly students 14,16,20,24,25 and guide41 changed. All other 62 PNGs are byte-identical. Both preview directories are retained unchanged for independent comparison.

Diagram checks: GA-18 preserves the exact 2:1 horizontal width ratio and the open/closed step endpoints, with no optimal height drawn. GA-19 uses common fixed axes rather than individually magnified graphs. GA-20 marks only required endpoints and the explicitly added waypoint; no winning path appears in a launch. GA-21 has equal coordinate scales, accurate full/short mirror endpoints and a reflected guide-only witness. GA-22's coordinates are correct and no hulls/diagonals/contact witnesses are supplied prematurely. GA-23 uses an orthographic sphere schematic, correctly directed short arcs and a blank student return ledger; its worked basis arrows and frame signs agree with the independently reviewed proof. GA-24 distinguishes a solid joined center from separated circles, with no puncture-count cues. GA-27 uses square coordinate grids, keeps the zero-level touching point, and draws the correct closed, clipped wet regions only in the guide. Its forced-route witness stays in the square and passes through the marked (a,0).

Every workspace count follows a supplied input (the three losses, two basis arrows or three requested levels), rather than disclosing an undiscovered number of solutions. Later supplied facts and comparisons remain staged by page. Sufficient open proof space remains after the diagrams; extra paper is allowed by the contents. Some guide pages are intentionally short because complete question/hint/source blocks stay together.

## Mechanical and mathematical checks

Both final build reports list no blank pages, no out-of-page characters and no suspect glyphs. Every page rendered. I independently compared the full 50 recorded prompt strings with current data: each ID appears exactly once and every string matches. The build also checks assigned families, planned page counts and contents starts.

The complete author checker was rerun after the notation-only edit; all eight groups pass. Its current results include the current data hash. General proofs, hypotheses and all eight extensions were independently approved at design stage; finite enumeration is never represented as a universal proof. Root's separate PDF pass is still required before assembly.

No PDF operation marker was rerun. Original atlas cards, prior ten, closed batch sources, and shared helpers were preserved. The top-level data status now records independent design approval and delegates PDF status to the maker/reviewer/release records.

## Current source hashes

- `ga3-data.json`: `d4a460fe3b33b4a56d26bdcb71da87dff35793884fc3f039ee665bd222af2af0`
- `ga3-design.md`: `0d040d80f1409a2bf75983ca90ac9329fe492748eeba6b2d3edbb04377672d6f`
- `ga3-checks.py`: `219707049b628898f1a54d23527709e46e3b7aafcbf73916eca83007f12fe8ee`
- `ga3-checks-results.json`: `9689785a174e31d98c1bf29ea32672d3c1cc90946252d35919b5d8ac004a37bf`
- `review-ga3-design.md`: `820dde3e79b63235f214badecec091783508e0cf68753c177276aa6ea64e2865`
- `ga3.py`: `0a248725fd77da41c088a72b598c31180c8bc5994348dd861aa3f2da698449b2`

## Candid first-pilot assessment

GA-22's pegs and GA-24's removable-point tests are the most accessible first pilots. GA-18 and GA-21 are promising after their algebra/geometric gates; GA-20's finite schedule is accessible earlier than its calculus continuation. GA-19 is calculus throughout, GA-23 requires real spatial-vector readiness, and GA-27's final page explicitly needs partial derivatives/Hessians. Physical transport on a ball remains approximate and needs rehearsal; the exact frame proof is authoritative. None of these has been classroom-piloted. The checks establish mathematical/render fidelity, not actual timing or engagement.

## Independent review repair: v4

Root's independent review passed all 42 guide pages and requested one product-copy refinement on student23. Replaced the typesetting statement “Equal scale: 1 unit = 35 points” with “Both pictures use the same coordinate scale.” No diagram coordinates, tasks, keys or mathematical data changed.

Fresh current preview is **`tmp/pdfs/atlas-remaining/ga3-preview-v4/`** (26 student / 42 guide pages). I inspected repaired student23 at full size under this fresh path. A byte comparison confirms it alone changed among all 68 page PNGs; the other 67 are identical to v3. Mechanical checks again show no blank pages, out-of-page characters or suspect glyphs.

- Current student PDF SHA-256: `bccc9ee0ebeb73ebd5f7c414bf8ae9c13a3a0db20679e9cfa2fa68cca4c67ebc`.
- Current guide PDF SHA-256 (unchanged): `42a82b45dba9f2a13686e004149c68f97fce14096d5549263350a634dd9df357`.
- Current renderer SHA-256: `0a248725fd77da41c088a72b598c31180c8bc5994348dd861aa3f2da698449b2`.
All data/design/check hashes listed above remain current. Final independent PDF disposition belongs in `review-ga3-pdf.md`.

Independent closure: root inspected the fresh v4 student23, independently confirmed the other 67 PNGs unchanged, saved `review-ga3-pdf.md`, and registered GA3 in `reviewed-previews.json`. No findings remain. Data, renderer and preview directories are now frozen.
