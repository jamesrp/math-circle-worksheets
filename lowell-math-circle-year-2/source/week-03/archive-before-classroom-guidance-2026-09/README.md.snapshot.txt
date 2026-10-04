# Week 3: Code machines, loops, and long returns

Prepared September 19, 2026. Repeat reversible substitutions, classify their loops, and prove a maximum return time. Grade labels describe entry points, not age restrictions. The [redesign plan](../../../plans/week-03-redesign.md) gives mathematical rationale, source references, readiness, the hour, hints, proofs, and prior-use notes.

## Print packets

- [K–1: The changing-symbol machine](../../week-03/week-03-k-1.pdf) — 2 pages, F03-K-v2. Shape keys, inverse decoding, three-cycles, swaps, and information loss.
- [Grades 2–3: A code you can undo](../../week-03/week-03-grades-2-3.pdf) — 2 pages, F03-M-v2. Repeated-symbol patterns, repeated keys, all four-symbol cycle types.
- [Grades 4–5: How long until every letter returns?](../../week-03/week-03-grades-4-5.pdf) — 3 pages, F03-U-v2. Prove maximum order six on five symbols; overlapping swaps need not commute.
- [Extra, grades 6–7: The slowest eight-letter machine](../../week-03/week-03-extra-grades-6-7.pdf) — 1 page, F03-X-v2. Construct order fifteen and prove a complete upper bound; predict nine letters.
- [Facilitator guide](../../week-03/week-03-facilitator.pdf) — 4 pages: materials, prerequisites, 60-minute flow, hints, all checked solutions, research boundaries, and sources.

Print US Letter, single-sided, preferably Actual Size. These are counter/card activities and do not require the one-inch pattern-block calibration used in Week 1. Give one page at a time. For K,K,1 / 3,3,3 / 5, print 3 K–1, 3 middle, and 1 upper packet: **15 core student sheets**, plus one extra reserve sheet and one facilitator copy if wanted. Do not require all pages in one meeting.

**Materials:** 18 shape slips (two circle/triangle/square sets per youngest child), 12 A–D cards (one set per middle child), A–E plus F–H for upper/extra, 13 counters (three per K–1 child and one per older child), pencils, paper. Hand-lettered scraps suffice.

**Mathematical lineage:** Permutation groups, disjoint cycles, least common multiples, composition, and Landau’s maximal-order function. The extra is a standalone one-page challenge with its solutions in the facilitator packet. Younger children can move to the next entry level; no separate lower-level extras are required.

## Build and verify

From the repository root, run `sh lowell-math-circle-year-2/source/week-03/build.sh`. Requires Python 3 (standard library only for verification), pdfLaTeX with TikZ, Source Sans Pro, microtype, extarticle, fancyhdr, geometry, tabularx, amsmath/amssymb, and hyperref. Editable sources are the five `week-03-*.tex` files and local `common.tex`. The build executes `verify.py`, compiles twice, and copies final files into `lowell-math-circle-year-2/week-03/`. Intermediate build files stay in `tmp/pdfs/week-03-build/`.

`python3 lowell-math-circle-year-2/source/week-03/verify.py` runs the mathematical checks alone. Every permutation for n=4,5,6,8,9 was enumerated; maxima are 4,6,6,15,20. The script checks every printed message trace and both composition orders. The guide supplies independent loop-decomposition and partition upper-bound proofs.

After edits, rebuild and render every page with `pdftoppm`; review layout again. The [review record](REVIEW.md) records this batch's own visual and mathematical checks. Record actual use, including targets/keys/ring sizes and whether the extra was attempted, in the shared [use log](../../../plans/fall-k-5-year-a-use-log.md). These packets are prepared activities, not evidence that a child has encountered them.
