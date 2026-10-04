# Week 9: Bouncing paths

Concrete revision of October 3, 2026: F09-K-v4 / F09-M-v4 / F09-U-v4, adult guide F09-FAC-v4. **Unpiloted.** It follows the organizer's report on Weeks 1 and 2 ([forecast and pivot](../../../plans/fall-forecast-2026-10-03.md)): rules enforced by the materials or by the other player, partner play at fixed KK11 / 3333 / 445 tables, and deeper questions late in each packet.

- [K–1](../../week-09/week-09-k-1.pdf) — 8 pages.
- [Grades 2–3](../../week-09/week-09-grades-2-3.pdf) — 8 pages.
- [Grades 4–5](../../week-09/week-09-grades-4-5.pdf) — 8 pages.
- [Adult guide](../../week-09/week-09-facilitator.pdf) — 10 pages: materials and counts, launch, pairing, answers, hints, and what to record.

A ball leaves the bottom-left corner of a grid table at 45 degrees and bounces until it reaches a corner. K–1 starts with a floor walk on a taped grid and traces small tables; grades 2–3 predict corners and bounces and design tables for a partner; grades 4–5 explain the corner and bounce rule with lcm and unfolding into mirror copies.

Set up a taped floor grid of about 3 by 5 large squares (or use floor tiles) for the K–1 walk. Rulers, coloured pencils, scissors and tape for the folding problems.

Print US Letter, single-sided, at 100% / Actual Size. Give one page at a time; the packets hold more than an hour, and stopping anywhere is fine.

The student pages were drafted with the [worksheet workflow](../../../worksheet-workflow/README.md) from the outline `worksheet-workflow/outlines/week-09-billiards.md`: writer, adversarial review and independent math check, then revision. The run record (prompts, reviews, draft and final PDFs) is in `tmp/worksheet-runs/week-09-billiards-v1/`. The adult guide was written separately from the final pages; its answers are recomputed by the scripts in `guide-src/`.

Rebuild from the repository root: `sh lowell-math-circle-year-2/source/week-09/build.sh`. It builds in `tmp/pdfs/week-09-build/` and copies the four PDFs into `lowell-math-circle-year-2/week-09/`. Requires Python 3 and pdfLaTeX with TikZ and Source Sans Pro. `src/` holds the student pages with their generators and checks; `guide-src/` holds the adult guide and its answer checks, which read `../src`.

The previous version (F09-*-v3, with its optional grades 6–7 extra) is preserved in [archive/](archive/README.md) with its sources, and its PDFs are in `lowell-math-circle-year-2/week-09/archive/`. Older versions remain in the `archive-before-*` folders here and beside the PDFs.
