# Week 63 fresh revision record

October 4, 2026. Revision stage only, following the independent student critic and mathematical review. Direct routing produces one combined nine-page student packet and one three-page material packet. Current local revision IDs are **W63-S-v2** and **W63-M-v2**; the reviewed draft remains separately in draft/. No guide, previous week, workflow prompt, repository instruction, global index, remote copy or Git operation was changed.

## Targeted repairs

**R1, student page 2, before Problem 2:** added a compact non-task visual using the page-1 VUWX placement. One 56 by 27 mm outcome-card frame contains the unchanged U/V/W/X homes, the whole V/U/W/X row and persistent VUWX ID. Two checks, “W in home W: yes” and “X in home X: yes,” connect to that single whole-outcome object. The output records VUWX in both W-home and X-home groups. Shared guidance explicitly defines one outcome card as one whole placement, simultaneous membership, and grouping on the tabletop. It neither gives the A-C answer nor supplies an add-back calculation or sorting layout. The 70 mm recording box remains, with three answer lines below it.

**R2, student page 9, Problem 9:** changed “any number of distinct cards” to “two or more distinct cards.” Children still find the counting rule and explain unique counting; the page does not print the recurrence or its method. Source notes state the adult limits n>=2, D0=1 and D1=0.

All other investigations and printed material contents are preserved. Footer versions advanced consistently. The source README now records revision status, record-box/tabletop geometry and unperformed physical/classroom status. It also records pooling the E-at-A branch from page 8 with E-at-B/C/D contributions from the three upper children or rotating roles; no child needs to list all 120 permutations.

## Actual-page coverage

All twelve final pages were freshly rendered at 144 dpi and individually viewed. Headers, footers, problem sequence, row labels, arrow directions, workspace and every material shape/card/catalog were checked.

| Actual student pages | Band and decision |
|---|---|
| 1-2 | Grades 2-5, supported entry. Page 1 already sufficient and preserved; page 2 has the new whole-outcome/simultaneous-membership convention before first use. |
| 3-5 | Grades 3-5, already sufficient and preserved. Complete four-card catalog, partial A/B avoidance and four-group inclusive overlaps remain substantial. |
| 6-8 | Grades 4-5, already sufficient and preserved. Five-group per-outcome cancellation, row-to-arrow example and both removal/reversal conventions remain available for later visits. |
| 9 | Grades 4-5, changed only in rule domain. Branch catalog and pooling task remain, with sixteen blank five-home rows. |
| Materials 1-3 | All contents already sufficient and preserved. Two decks/home strips, six A-C outcomes, five home-group labels, twelve blank A-E outcome records and all 24 A-D outcomes verified from the actual final PDF. |

There is no independent K-1 packet. Prerequisites, adult reading/recording support and readiness-dependent upper continuations remain in src/README.md.

## Mathematical and digital checks

The independent review's permutation and fixed-label row-deletion/insertion audit was adapted for final outputs and run freshly; it imports neither the author verifier nor a precomputed answer table. It verifies every row for n=0 through 5, every inclusive fixed-home intersection, every per-outcome alternating contribution, every distinguished-home branch and both inverses. It additionally extracts and verifies the new actual-page VUWX whole outcome, both markers, persistent ID and Problem 9 domain. The source's separate authored backtracking verifier was run as a secondary check.

Results preserve:

- Home-free counts 1,0,1,2,9,44 for n=0,1,2,3,4,5.
- Partial A/B avoidance counts 3 of 6 and 14 of 24.
- Four-card terms 24-24+12-4+1=9; five-card terms 120-120+60-20+5-1=44.
- Each specified k-home intersection has (n-k)! rows, including additional matches.
- Each unwanted row has alternating coefficient zero; each home-free row has coefficient one.
- Distinguished-home branches have one reciprocal plus two longer rows for four cards, and two reciprocal plus nine longer rows for five cards.
- The two-family recurrence applies for n>=2 with D0=1 and D1=0; removal/restoration retains original labels.

All pages are US Letter, 612 by 792 points, with consecutive Problems 1-9 and actual band headers. Material drawing-path measurements give ten 30 by 40 mm working cards, ten 35 by 45 mm home cells, 56 by 27 mm outcome frames and 9 by 10 mm internal record cells. Home labels lie in the top 5 mm clearance. Both triangles have three equal 12 mm sides; both squares and both rotated squares have four equal 12 mm sides. Both five-tip stars have ten equal boundary segments; circles are circular. Student record cells use equal scaling and are writing spaces, not full-size placement mats.

Clean copied-source and ZIP-extracted-source builds reproduce each final page's extracted text, dimensions and 144-dpi pixels exactly. Both rebuilt PDF files also match delivered bytes. The test ZIP contains exactly README.md, build.py, common.tex, materials.tex, students.tex and verify.py: no prompts, exemplars, books, borrowed assets, intermediate renders or reference PDFs. Source is free of build intermediates.

Page text, render paths, hashes, catalogs, intersections, reductions, geometry and page-by-page rebuild comparisons are in ../revision-evidence/results.json. Individual page inspection and draft-preservation checks are in ../revision-evidence/visual-and-preservation.json: only student pages 2 and 9 change body content; the other ten page bodies match the draft pixels exactly, with only footer version changes. Mathematical explanations and audit instructions are in ../revision-evidence/README.md; the clean ZIP test is in ../revision-rebuild/. The source builder takes an independent output directory without repository dependencies. Build logs contain no overfull/underfull boxes or LaTeX warnings/errors.

## Remaining limits

Physical cutting/card fit, grouping-ring and property-marker handling, bottom-edge placement, reversal procedures and classroom piloting remain **unperformed**. Digital dimensions and mathematics do not establish those. The 24 outcome cards require 36,288 mm² before gaps, exceeding the 173 by 95/97 mm student recording boxes, so grouping uses the tabletop. Source notes are not a separately authored/reviewed guide. This revision is ready for local review/guide work; no remote current-version or release approval is claimed.


Record note: this is the completed authored stage report. Stage-local render/build
evidence referenced under `tmp/` is historical and is not included in source ZIPs.
Current released-file hashes and actual ZIP-extraction text/dimension/pixel checks
are recorded in `../release-checks.json`; coordinator page coverage is recorded
in `../../final-visual-review.json`. Physical pretests and piloting remain unperformed.
