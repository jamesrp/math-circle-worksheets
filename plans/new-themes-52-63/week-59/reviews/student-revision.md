# Week 59 fresh revision record

Revised 4 October 2026, revision stage only. Read AGENTS.md, README.md,
REPUBLISHING.md (preserved), direct stage routing, PROMPT.md, REVISE.md, both
complete review reports, the independent mathematical derivation and code,
and all nine draft source files. Rendered and inspected the actual six-page
draft student packet and three-page materials packet before editing. The direct
combined-packet routing overrides the generated three-band filenames/quotas.
No facilitator guide, subagent, prior-week edit, index edit or remote write was
made. The packet remains unpiloted and has not been promoted to the library.

## Required revisions completed

**R1 / M1:** Student p.1 now begins “To measure width,” explicitly limiting
adjustable parallel, whole-body, two-contact supports to width measurement.
Problem 2 says “Keep the parallel edges fixed 60 mm apart while the piece turns
and slides.” Both classification questions and all five controls remain. Thus
an oval/straight-triangle position narrower than 60 mm is a legal fitting
position despite a gap at an edge. Nominal outcomes remain: disk and curved
triangle fit through a full turn and retain both contacts; oval and straight
triangle fit through a full turn but lose simultaneous contact; square cannot
fit through a full turn. Free translation is retained, with no fixed center pin.

**R2 / M2:** Before Problem 5, a three-panel non-task visual shows a marked
rectangle, one enclosing touching edge with an O-to-line perpendicular and
right-angle mark, then the same diagram with a matching “32 mm” record. The
nominal rectangle is 44×28 mm, O=(12,9), and its right support is x=44. Its
point-to-support distance is 44−12=32 mm; the two-edge width is 44 mm. O is
off center in both coordinates. At common display scale 0.6, the rectangle is
26.4×16.8 mm and the measured segment is 19.2 mm. The support touches the right
side and encloses the whole rectangle. The 32 mm example supplies neither
target's extrema and describes O as a marked point. Children still choose
orientations, search for extrema and investigate the relationship to width.
The two record rows remain 48 mm high, with 45 mm additional drawing space.

All six distinct problems remain, including two-size construction, the
all-direction support-sector explanation, the marked-point comparison and the
exact three-arc perimeter argument. The mathematical destination and
whole-body/sector-coverage proof remain in mathematical-notes.md. Original
geometry.py, materials.tex and build.py are byte-identical to the draft; the
output-directory build CLI and all existing assets are retained. Student footer
is W59-S-v2. Materials remains W59-M-v1 and is byte-identical to the reviewed
draft, with all six pieces, grid and both template sizes.

## Actual final page inspection

All nine final pages were freshly rendered at 108 dpi and individually viewed.
All are 612×792 pt US Letter. No clipped or overlapping text, diagrams, table
lines or labels were found. Headers and footers are legible, problems remain
consecutively numbered 1–6, and there are no Name/Date fields, extra task titles,
adult hints, timing or compulsory directed proof substeps on student pages.

| Final page / actual band | Coverage and visual result |
|---|---|
| Students 1 / Grades 2–5 | Changed shared scope. The three-panel 46 mm width convention remains clear; five contrasting controls, extrema columns and substantial sketch space remain. Square has four equal sides; straight triangle has three equal sides; curved triangle has the intended three arcs. |
| Students 2 / Grades 2–5 | Changed fixed-gap rule. Both fitting/contact questions, all five controls and deciding-position cells fit clearly. Sliding remains explicit. A deciding sketch supplies a possible obstruction; it alone does not prove an all-turn affirmative claim. |
| Students 3 / Grades 3–5 | Already sufficient. Non-task D/E/F compass input → opening DE at D → 90° EF arc appears before construction; both 60 and 40 mm records and workspace remain. |
| Students 4 / Grades 3–5 | Already sufficient. Circle/contact/right-angle convention precedes the serious proof task. All three Reuleaux orientations (7°,37°,83°), A/B/C labels, dashed equilateral skeletons and workspace are intact. The text requires turns between drawings. |
| Students 5 / Grades 3–5 | Changed first-use convention and spacing. All three new panels and both “32 mm” labels are legible before Problem 5. One support, off-center O, perpendicular segment and right-angle mark are visible. The marked disk and centroid-marked curved triangle remain distinct, with roomy extrema cells and additional drawing space. |
| Students 6 / Grades 4–5 | Already sufficient. Radius-30 disk, three-arc curved triangle, radius-60 generating circle, six equally spaced dots and matching highlighted 60° arcs remain clear. Exact boundary-length question and large workspace remain. |
| Materials 1 | Unchanged and freshly inspected. Six separated full-size pieces: marked disk, 60×40 oval, 60 mm-side square, 60 mm-side equilateral triangle, unmarked and centroid-marked width-60 Reuleaux triangles. Outside captions do not cross cuts; separate 100 mm bar is clear. |
| Materials 2 | Unchanged and freshly inspected. 200×200 mm grid with 21 horizontal and 21 vertical lines (400 squares), separate 100 mm bar and material instructions fit on Letter. Digital fit does not certify a printer's margins. |
| Materials 3 | Unchanged and freshly inspected. Two 60 mm-side and two 40 mm-side three-sided equilateral templates, A/B/C labels, outward-arc room and 100 mm bar remain clear. Three copies supply six templates of each size. |

## Mathematics and portable rebuild evidence

The modified verifier imports no geometry authoring functions. It checks all
30 nominal arcs, all 21 polygons including frames/nonregular examples, all nine
compiled pages and every existing control, cutout and template. New checks
independently validate the non-task rectangle, off-center mark, whole-body
support, perpendicular segment and matching record in both nominal geometry
and compiled PDF paths. It checks R1's actual final text and R2's placement
before Problem 5.

The independent math review's separate disk-intersection/vector checker was
rerun against the final PDFs in revision-evidence/final_independent_audit.py,
without importing the authoring geometry or verifier. It confirms all task
answers over 7,200 nominal directions, nine actual Reuleaux paths, all ten
regular polygons, all 30 nominal arcs, both marked locations, six boundary dots,
every 100 mm bar and the 200 mm grid. Universal claims rest on the retained
whole-body and complete angular-sector proof, not these finite samples.
The nominal curved triangle has width 60; the centroid's support-distance
extrema are 60−60/√3≈25.358984 and 60/√3≈34.641016 mm. Three radius-60, 60°
arcs have the same total boundary length 60π mm as the radius-30 disk.

PDF circles/arcs are cubic approximations. The nominal 60 mm disk's sampled
compiled widths are 60.000456–60.016920 mm. The greatest observed Reuleaux width
error in 3,600 directions is 0.001631 mm. These are finite digital samples,
not exact circular curves, certified uniform numerical bounds, or evidence of
successful physical fitting/contact.

The lean portable final/src contains exactly nine original source/notes files.
It excludes prompts, exemplars, downloaded books, reference PDFs, renders and
intermediates. The unchanged build CLI accepts an output directory and keeps
intermediates in OUTPUT/.build. Clean copied-source and ZIP-extracted-source
builds both pass; every copied/extracted source file matches the final source
bytes. All nine rebuilt pages exactly match final text, page dimensions and
rendered pixels at 108 dpi. A separate independent ZIP-extracted rebuild also
matched all nine final pages. The check ZIPs are QA intermediates, not release
packages; root handles final source packaging and promotion.

Evidence:

- final/qa/math-verification.json: final nominal, task, compiled-vector and new
  marked-point checks.
- final/qa/rebuild-checks/rebuild-verification.json: current source hashes and
  both clean source-copy/ZIP rebuild comparisons.
- revision-evidence/independent-math-checks.json: independent mathematical,
  full vector, construction/template/grid and extracted rebuild checks.
- revision-evidence/final-output-receipt.json and final-renders/: final hashes,
  per-page text, dimensions, pixel hashes and the individually inspected renders.

Final SHA-256: students.pdf
`1670487888991d29f36667a7ab4756d0100ee9fb4316da12f11482fe373515ba`;
materials.pdf
`4f1f572fdf9fdba649adaafe92bf0055cc54200d2e0a47f10dcf9d9c0c10454d`.
Draft PDF hashes were rechecked and remain the reviewed inputs.

## Remaining operational limits

Physical printer scale/margins, thirty stiff-card cutouts across five kits,
cutting smoothness/contact, 300 mm rail clearance on the 200 mm mats, movable
right-angle guides/parallelism, fixed-60 mm gap handling, O-to-line measurement,
compass-radius stability, preparation time, actual staffing, timing and classroom
piloting remain unperformed. No physical tolerance is established. The material
counts, construction controls, practical prerequisites and readiness gates stay
in the source notes. No rolling, axle, platform or exact-square-hole success is
claimed. There is no digital blocker to parent final review; physical readiness
and piloting still need actual evidence.


Record note: this is the completed authored stage report. Stage-local render/build
evidence referenced under `tmp/` is historical and is not included in source ZIPs.
Current released-file hashes and actual ZIP-extraction text/dimension/pixel checks
are recorded in `../release-checks.json`; coordinator page coverage is recorded
in `../../final-visual-review.json`. Physical pretests and piloting remain unperformed.
