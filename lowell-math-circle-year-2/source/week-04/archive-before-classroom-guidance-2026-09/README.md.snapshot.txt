# Week 4: Round and round: shifts and perfect shuffles

Prepared September 19, 2026. Classify repeated fixed shifts, explain their cycle lengths, and discover the arithmetic of a perfect shuffle. Grade labels describe entry points, not age restrictions. The [redesign plan](../../../plans/week-04-redesign.md) gives mathematical rationale, source references, readiness, the hour, hints, proofs, and prior-use notes.

## Print packets

- [K–1: Hop around the ring](../../week-04/week-04-k-1.pdf) — 2 pages, F04-K-v2. One-, two-, and three-hop routes; infer and undo a fixed turn.
- [Grades 2–3: One clue controls the whole code](../../week-04/week-04-grades-2-3.pdf) — 2 pages, F04-M-v2. Consistent clues; ten-letter orbits under +2 and +3; reversibility versus visiting.
- [Grades 4–5: The twelve-place code](../../week-04/week-04-grades-4-5.pdf) — 3 pages, F04-U-v2. Shift orbits, a concrete return proof, optional adult-supported gcd formula, inverse and commuting rotations.
- [Extra, grades 6–7: A perfect shuffle has a clock](../../week-04/week-04-extra-grades-6-7.pdf) — 1 page, F04-X-v2. Eight-card out-shuffle; modular doubling and proof of first return time.
- [Facilitator guide](../../week-04/week-04-facilitator.pdf) — 4 pages: materials, prerequisites, 60-minute flow, hints, all checked solutions, research boundaries, and sources.

Print US Letter, single-sided, preferably Actual Size. These are counter/card activities and do not require the one-inch pattern-block calibration used in Week 1. Give one page at a time. For K,K,1 / 3,3,3 / 5, print 3 K–1, 3 middle, and 1 upper packet: **15 core student sheets**, plus one extra reserve sheet and one facilitator copy if wanted. Do not require all pages in one meeting.

**Materials:** Seven counters, pencils, scratch paper, eight card scraps numbered 0–7 (sixteen for the optional larger shuffle). Printed fixed rings are the manipulatives; no cut-out wheel or brad is needed.

The full twelve-row table is optional. The general proof additionally needs the [coprime divisibility scaffold](../../../plans/coprime-divisibility-scaffold.md); the finite-ring proof is a satisfying stopping point.

**Mathematical lineage:** Cyclic groups, modular arithmetic, gcd, permutation orbits, and Diaconis–Graham–Kantor’s perfect-shuffle research. The extra is a standalone one-page challenge with its solutions in the facilitator packet. Younger children can move to the next entry level; no separate lower-level extras are required.

## Build and verify

From the repository root, run `sh lowell-math-circle-year-2/source/week-04/build.sh`. Requires Python 3 (standard library only for verification), pdfLaTeX with TikZ, Source Sans Pro, microtype, extarticle, fancyhdr, geometry, tabularx, amsmath/amssymb, and hyperref. Editable sources are the five `week-04-*.tex` files and local `common.tex`. The build executes `verify.py`, compiles twice, and copies final files into `lowell-math-circle-year-2/week-04/`. Intermediate build files stay in `tmp/pdfs/week-04-build/`.

`python3 lowell-math-circle-year-2/source/week-04/verify.py` runs the mathematical checks alone. Every shift on rings of sizes 4,6,10,12,18 agrees with the gcd formula. All cipher examples and routes pass. Direct shuffle simulation verifies position formulas and first return times 4,3,4 for 6,8,16 cards, including every printed eight-card row.

After edits, rebuild and render every page with `pdftoppm`; review layout again. The [review record](REVIEW.md) records this batch's own visual and mathematical checks. Record actual use, including targets/keys/ring sizes and whether the extra was attempted, in the shared [use log](../../../plans/fall-k-5-year-a-use-log.md). These packets are prepared activities, not evidence that a child has encountered them.
