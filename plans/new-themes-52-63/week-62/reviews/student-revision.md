# Week 62 revision-stage record

Completed October 4, 2026 against `review.md`, `review-math.md`, and `math-audit.md`, using the direct combined-packet routing. Deliverable: `students.pdf`, nine US Letter pages; editable portable sources: `src/`. No facilitator guide, older packet, global index or remote copy was edited.

## Located revisions

- R1 / mathematics issue 1, p. 4: cycle requires at least three different circles and repeats only the start, at the end. The existing square input/partway/output visual remains.
- R2 / mathematics issue 3, p. 7: no moving applies during an ordered first-fit trial. After a finished order, moves are explicitly permitted with the goal of using fewer slots. Both blank trials remain; no ordering or repair method is supplied.
- R3 / mathematics issue 2, p. 6: both six-site boards now use a convex staggered layout. All six labels, five tree edges and the second edgeless graph remain. Every straight pairwise connection clears every nonendpoint 20 mm activity disk: minimum center distance is 13 mm, giving about 3 mm clearance outside the disk. All six minimal tree additions and all 20 minimal triangle sets are drawable under the usual straight-line convention.
- R4, pp. 1 and 7: textual circle-mark lists are replaced with the actual same-network marked-circle outputs, showing fixed activity letters above bold slot numbers. All working sites now put their letters in the upper portion, leaving matching number space below. Non-task input and meaningful intermediate placements remain.

All nine original investigations, 18 graph instances, arbitrary-network reasoning, clique-bound gap, order-dependent first-fit tree and named counting questions remain. Problems remain consecutively numbered 1–9. Grades 2–5 headers appear on pp. 1–3; Grades 4–5 headers appear on pp. 4–9. No K–1 coverage is claimed.

## Verification of this final packet

Rendered and personally inspected every final page; no overlaps, overflow, obscured graph endpoints or illegible labels found. All 104 full-size circles measure 20 mm. All 18 actual PDF graphs agree with their raw TikZ coordinates and edge lists; all printed edges avoid third-site disks. Page 6 checks cover every possible new connection, not only chosen answers. No regular polygon claim or side-count requirement applies to these graph drawings.

`src/verify.py` checks all graph minima/cliques, all 24 path orders and 40,320 eight-vertex tree orders, every minimal added-edge answer, all potential page 6 connection clearances, and the four named counts. `src/verify_pdf.py` adapts the independent reviewer extractor and checks actual PDF vectors and text; `pdf-verification.json` records the complete results. Counts remain: path first-fit 18 two-slot / 6 three-slot orders; tree 12,810 two-slot / 26,880 three-slot / 630 four-slot orders; path named assignments 24/108 and diamond 6/48. Minimum additions remain 1/3, with 6/20 complete optimal edge sets.

A fresh lean student-source ZIP was created only for the extraction/rebuild check under `qa/`, extracted into a new unique directory, and built from `/tmp`. Every source member hash was verified; the generated LaTeX/graph snapshots match the delivered source. `clean-rebuild-checks.json` confirms identical text, page dimensions and rendered pixels on all nine pages. `qa/source-rebuild-provenance.json` records the fresh extraction and hashes. Root will handle the final combined student/guide release ZIP.

Current build dependencies: Python 3 standard library; pdfTeX 1.40.27 / TeX Live 2025, with portable `geometry`, `fontenc`, `helvet`, TikZ `arrows.meta`, `fancyhdr`, and `array`. PDF QA used PyMuPDF 1.28.2 and Pillow 12.3.0 in `tmp/bonus-35-51-venv/bin/python`; PyMuPDF is a QA dependency, not a worksheet-build dependency. The README includes portable commands.

Physical kit handling, preparation time, rehearsal, classroom piloting and remote currency remain untested/unverified. These digital checks do not establish them.


Record note: this is the completed authored stage report. Stage-local render/build
evidence referenced under `tmp/` is historical and is not included in source ZIPs.
Current released-file hashes and actual ZIP-extraction text/dimension/pixel checks
are recorded in `../release-checks.json`; coordinator page coverage is recorded
in `../../final-visual-review.json`. Physical pretests and piloting remain unperformed.
