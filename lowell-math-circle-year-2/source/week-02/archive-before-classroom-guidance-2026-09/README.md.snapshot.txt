# Week 2: Pair switches and cheapest repairs

Prepared September 19, 2026. Toggle two endpoint lamps at a time; prove what is reachable and find the cheapest move lists. Grade labels describe entry points, not age restrictions. The [redesign plan](../../../plans/week-02-redesign.md) gives mathematical rationale, source references, readiness, the hour, hints, proofs, and prior-use notes.

## Print packets

- [K–1: Two at a time](../../week-02/week-02-k-1.pdf) — 2 pages, F02-K-v2. Undoing, pair targets, and an impossible single lamp.
- [Grades 2–3: Which pictures are possible?](../../week-02/week-02-grades-2-3.pdf) — 2 pages, F02-M-v2. All eight reachable four-lamp states; parity and path cancellation.
- [Grades 4–5: The cheapest light show](../../week-02/week-02-grades-4-5.pdf) — 3 pages, F02-U-v2. Exactly two complementary solutions; shortest moves; a theorem for all targets.
- [Extra, grades 6–7: A theorem for any network](../../week-02/week-02-extra-grades-6-7.pdf) — 1 page, F02-X-v2. Component parity and the unique tree solution; T-join optimization.
- [Facilitator guide](../../week-02/week-02-facilitator.pdf) — 4 pages: materials, prerequisites, 60-minute flow, hints, all checked solutions, research boundaries, and sources.

Print US Letter, single-sided, preferably Actual Size. These are counter/card activities and do not require the one-inch pattern-block calibration used in Week 1. Give one page at a time. For K,K,1 / 3,3,3 / 5, print 3 K–1, 3 middle, and 1 upper packet: **15 core student sheets**, plus one extra reserve sheet and one facilitator copy if wanted. Do not require all pages in one meeting.

**Materials:** 29 two-sided counters plus 8 spares, pencils, and scratch paper. One counter at each printed lamp; flip faces without moving locations. Paper disks with one shaded side work. No electronic kit.

**Mathematical lineage:** Binary linear algebra, parity, graph paths/cycle spaces, and minimum T-joins (Edmonds–Johnson). The extra is a standalone one-page challenge with its solutions in the facilitator packet. Younger children can move to the next entry level; no separate lower-level extras are required.

## Build and verify

From the repository root, run `sh lowell-math-circle-year-2/source/week-02/build.sh`. Requires Python 3 (standard library only for verification), pdfLaTeX with TikZ, Source Sans Pro, microtype, extarticle, fancyhdr, geometry, tabularx, amsmath/amssymb, and hyperref. Editable sources are the five `week-02-*.tex` files and local `common.tex`. The build executes `verify.py`, compiles twice, and copies final files into `lowell-math-circle-year-2/week-02/`. Intermediate build files stay in `tmp/pdfs/week-02-build/`.

`python3 lowell-math-circle-year-2/source/week-02/verify.py` runs the mathematical checks alone. All edge subsets on cycles of sizes 4–7: respectively 8,16,32,64 even targets; exactly two complementary reduced solutions per target; maximum minimum floor(n/2). The two optimization targets, disconnected obstruction, and all 32 even targets on a six-vertex tree also pass.

After edits, rebuild and render every page with `pdftoppm`; review layout again. The [review record](REVIEW.md) records this batch's own visual and mathematical checks. Record actual use, including targets/keys/ring sizes and whether the extra was attempted, in the shared [use log](../../../plans/fall-k-5-year-a-use-log.md). These packets are prepared activities, not evidence that a child has encountered them.
