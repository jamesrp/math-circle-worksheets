# Week 56 revision evidence

Fresh revision stage, October 4, 2026. Read AGENTS.md, README.md, REPUBLISHING.md, the direct stage routing, PROMPT.md and REVISE.md, both reviews, all editable sources, the actual nine-page draft student PDF and four-page preparation PDF, and the independent mathematical solutions/checks. Only the assigned Week 56 student/preparation revision is delivered here. No guide, other week, global index, workflow prompt or remote copy was edited by this stage.

The direct stage routing supersedes the generic three-packet destinations: the results are **students.pdf, 9 pages**, and **materials.pdf, 4 pages**, both US Letter. The main packet honestly serves Grades 2–5 on pages 1–6 and Grades 4–5 on pages 7–9. A possible younger physical fan entry remains adult read and recorded; there is no independent K–1 packet. Student footer ID is **N56-S-v2**; the unchanged preparation sheets retain **N56-M-v1**.

## Issue trace

| Review issue | Final change and evidence |
|---|---|
| Critic R1; independent math issue 1: open flat fans versus fans that close flat, and convexity before the test | Student page 3, Problem 3 now asks “Which groups can close into a pointed corner with no inward dents? Which close flat with no gap?” The shared fan rules and complete input/intermediate/output example remain before use. All six groups and their recording circles remain. Actual final text, rendered page 3 and `qa/independent-math/audit-results.json` verify the wording. |
| Critic R2: contrasting models must test the Euler count before generalization | Student page 6, Problem 6 now begins “Compare V−E+F for all four models in Problem 1.” This precedes the cube redrawings, using the existing Problem 1 inventories and workspace. All three independent redrawings, their table and the zero-gap question remain. Actual final text, rendered page 6 and the audit's wording contract verify this bridge. |
| Critic R3; independent math issue 3: polygonal domain in universal claims | Problems 7, 8 and 9, on actual student pages 7–9, now explicitly say closed convex solids “with polygon faces.” The connected opened drawing, tree reduction, polygon-angle explanation and both reverse problems remain. Actual final text/rendered pages and the audit's wording contract verify all three. |
| Critic R4: unnecessary angle measuring | Deleted “Measure the flat face corners” from page 4. The supplied 60°/90°/360° definitions and complete two-triangle calculation example remain before Problem 4. Actual final text, rendered page 4 and the audit verify deletion. No protractor was added. |
| Independent math issue 2: region deletion may merge with outside | Root had already corrected `plans/new-themes-52-63/week-56/research-notes.md`. The portable source README gives the correct reduction: delete a cycle edge, preserving connectivity, and merge two regions, possibly including the unbounded outside region; E and bounded F each decrease by one. The final bounded region can merge with outside, reaching a tree. No plan-note edit was needed for this revision. |

## Preserved mathematical work

The closed-model inventories are cube (8,12,6), tetrahedron (4,6,4), right equilateral triangular prism (6,9,5), octahedron (6,12,8), and square pyramid (5,8,5). Edge incidence and printed seam/vertex identities are reconstructed independently from the net TeX coordinates, rather than accepted from the writer's geometry JSON. Each supplied net admits a rigid placement into its intended closed convex solid; all five have total defect 720°.

The six fans, in printed order, have gaps 180°,120°,60°,0°,90°,0°. All can lie flat as open fans. The four positive-gap groups can close into convex pointed corners; the two zero-gap groups close flat with no gap. The independent audit also retains a concrete nonconvex pointed six-triangle cone, confirming why “no inward dents” matters.

Problem 5 still uses unequal gaps: apex 120° and four base gaps 150°. Problem 6 retains the original cube (8,12,6), one diagonal (8,13,7), one face center plus four segments (9,16,9), and one inserted edge vertex (9,13,6). Each alternating count is 2; face-center and edge-subdivision points have zero gap; total gap stays 720°.

Problem 7 retains the opened tetrahedron-to-tree worked visual, the opened cube and extra workspace. The actual cube PDF graph has 8 vertices, 12 edges and 5 bounded quadrilateral regions. The independent script enumerates 384 cube spanning trees and 16 tetrahedron spanning trees, verifies that the erased-edge count is F−1, and preserves the connected-tree reduction. Problem 8 retains the five-sided face → three triangles → 540° example and the general cancellation argument. Problem 9 retains five regular triangles per vertex and three regular pentagons per vertex, giving (V,E,F)=(12,30,20) and (20,30,12), respectively. Independent convex hull constructions establish existence for those two specific cases; a positive local fan gap alone is not advertised as whole-solid existence.

## Final-page visual coverage

Every final PDF page was rendered at scale 1.3 with PyMuPDF, then individually inspected using its full-page PNG, not only a contact sheet. Images/text are under `qa/render/`. No overflow, clipping, missing glyphs, text/diagram collision, header/footer inconsistency or changed polygon side count was found.

| Actual final page | Inspection result |
|---|---|
| Students 1 | Grades 2–5; shared-incidence visual precedes counting; all four closed-model rows legible. |
| Students 2 | Grades 2–5; separate/joined visual, all four inventory rows and workspace intact. |
| Students 3 | Grades 2–5; both revised closure tests fit in two lines; six records and first-use visual intact. |
| Students 4 | Grades 2–5; unneeded measuring sentence absent; worked angle example, four models and workspace intact. |
| Students 5 | Grades 2–5; top/base distinction, square plus four triangle faces, unequal-gap table intact. |
| Students 6 | Grades 2–5; four-model comparison appears before the three redrawings; table and workspace clear. |
| Students 7 | Grades 4–5; polygon-face scope visible; opened tetrahedron/tree bridge and both cube drawings clear. |
| Students 8 | Grades 4–5; polygon-face scope visible; both regular five-sided faces and triangulation clear. |
| Students 9 | Grades 4–5; polygon-face scope visible; five triangular and three pentagonal fan faces remain regular and legible. |
| Materials 1 | Cube/tetrahedron nets, seam pairs, assembled vertex numbers, face numbers, separate tabs and scale bar clear. |
| Materials 2 | Octahedron/right prism nets, seam/corner labels, all closing faces and separate tabs clear. |
| Materials 3 | Square pyramid net and eight separate marked equilateral fan pieces clear. |
| Materials 4 | Eight marked square fan pieces and two full-turn circles clear, with cutting separation. |

## Actual-PDF geometry audit

`qa/independent-math/audit-results.json` records all independent calculations and actual PDF path measurements. The measured 28 net faces have edge lengths 30.000214–30.000238 mm. The 16 fan cutouts (8 triangles, 8 squares) have edges 30.000217–30.000236 mm. The regular material polygons have 60° or 90° face angles within the audit tolerance. Both circle widths/heights are 80.000597–80.000608 mm. The 30 mm scale bar passes. These tiny deviations are vector rounding, within the stated 0.001 mm edge and 0.002 mm circle tolerances.

Actual gray tab paths were checked by convex polygon clipping, separately from source-coordinate geometry: 10 tabs on material page 1, 10 on page 2, and 4 on page 3. Across actual PDF face/face, face/tab and tab/tab pairs, positive-area overlaps above 0.001 mm² are absent; all reported maximum overlap areas are zero. The 28 actual blue face paths also match their authored source net polygons after a single translation and PDF y-reflection. Twenty-three intended regular triangle/pentagon paths on the student pages pass equal-side/equal-angle checks. Perspective solid thumbnails are not treated as regular plane faces.

The material TeX/net assets were not altered. All four final material pages have equal text and rendered pixels to the draft, independently compared at scale 1.3. Digital checks establish dimension/incidence/flat-layout correctness, not physical tab handling.

## Portable-source and clean-build evidence

`src/` contains only the original authored student/material TeX, five editable net TeX assets, standard-library geometry builder, geometry data, verifiers, build script and README. The separate independent audit is now portable as `audit_math.py OUTPUT_DIR QA_DIR`. The README preserves exact prerequisites, three stable adult tables, three five-solid sets, five fan sets, preparation dimensions, independent resetting of cube redrawings, source citations and provenance, later-visit pacing, and the distinction between experiments, conjectures and explanations. No prompts, borrowed exemplars/books, duplicate reference PDFs, render images, TeX intermediates or generated PDFs are inside `src/`.

Commands actually run:

```sh
sh final/src/build.sh final
../../bonus-35-51-venv/bin/python final/src/verify.py final final/qa/render
../../bonus-35-51-venv/bin/python final/src/audit_math.py final final/qa/independent-math
../../bonus-35-51-venv/bin/python final/src/clean_rebuild.py final final/qa/clean-rebuild
```

The commands above are shown relative to this Week 56 run folder; the repository-relative interpreter path is `tmp/bonus-35-51-venv/bin/python`. The verifier checks all Problems 1–9, page/header/text contracts, dimensions, final material sizes and renders all thirteen pages. The independent audit checks incidence, labels, seams, convex target geometry, fan feasibility, subdivisions, spanning trees, reverse solids, final wording and actual PDF paths.

`qa/clean-rebuild/clean-rebuild-check.json` confirms that a clean copied-source directory and a separately extracted lean ZIP each rebuild **both PDFs**, with identical extracted text, Letter dimensions and every rendered pixel at scale 1.3 on all 13 pages. The source ZIP contains 14 authored files. The extracted verifiers were also run successfully against the extracted-source rebuilt PDFs; evidence is under `qa/clean-rebuild/extracted-verify/` and `extracted-independent/`. The temporary verification ZIP is under QA; root owns final release packaging/indexing.

## Remaining limits

Cutting, folding, tape flexibility, 6 mm tab handling, 30 mm model handling, circle placement, marker use, preparation duration and classroom timing have not been physically rehearsed. The square fan's far corners extending slightly beyond the 80 mm circle remains a handling pretest; the circle marks angular gap, not piece containment. All investigations are unpiloted. These limits are stated in the source README. No remote upload/publication, classroom-readiness or piloting claim is made. No digital blocker remains.


Record note: this is the completed authored stage report. Stage-local render/build
evidence referenced under `tmp/` is historical and is not included in source ZIPs.
Current released-file hashes and actual ZIP-extraction text/dimension/pixel checks
are recorded in `../release-checks.json`; coordinator page coverage is recorded
in `../../final-visual-review.json`. Physical pretests and piloting remain unperformed.
