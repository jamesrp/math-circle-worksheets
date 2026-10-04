# Week 10: Bridges and one-stroke drawings

Concrete revision of October 3, 2026: F10-K-v4 / F10-M-v4 / F10-U-v4, adult guide F10-FAC-v4. **Unpiloted.** It follows the organizer's report on Weeks 1 and 2 ([forecast and pivot](../../../plans/fall-forecast-2026-10-03.md)): rules enforced by the materials or by the other player, partner play at fixed KK11 / 3333 / 445 tables, and deeper questions late in each packet.

- [K–1](../../week-10/week-10-k-1.pdf) — 12 pages.
- [Grades 2–3](../../week-10/week-10-grades-2-3.pdf) — 12 pages.
- [Grades 4–5](../../week-10/week-10-grades-4-5.pdf) — 12 pages.
- [Adult guide](../../week-10/week-10-facilitator.pdf) — 8 pages: materials and counts, launch, pairing, answers, hints, and what to record.

Walks that cross every bridge once. A counter sits on every bridge and is picked up when the bridge is crossed, so no bridge can be reused. K–1 walks towns, tries one-stroke drawings and builds towns from hexagons and craft sticks for a partner; grades 2–3 find where walks start and end, count bridges at each island and repair towns; grades 4–5 explain the odd-island rule, join loops, decide Königsberg and find the fewest repeated bridges for delivery routes.

The towns were sized for counters about 1 inch across; check that yours fit. Craft sticks and yellow hexagons for children's own towns; masking tape for an optional floor town.

Print US Letter, single-sided, at 100% / Actual Size. Give one page at a time; the packets hold more than an hour, and stopping anywhere is fine.

The student pages were drafted with the [worksheet workflow](../../../worksheet-workflow/README.md) from the outline `worksheet-workflow/outlines/week-10-bridges.md`: writer, adversarial review and independent math check, then revision. The run record (prompts, reviews, draft and final PDFs) is in `tmp/worksheet-runs/week-10-bridges-v1/`. The adult guide was written separately from the final pages; its answers are recomputed by the scripts in `guide-src/`.

Rebuild from the repository root: `sh lowell-math-circle-year-2/source/week-10/build.sh`. It builds in `tmp/pdfs/week-10-build/` and copies the four PDFs into `lowell-math-circle-year-2/week-10/`. Requires Python 3 and pdfLaTeX with TikZ and Source Sans Pro. `src/` holds the student pages with their generators and checks; `guide-src/` holds the adult guide and its answer checks, which read `../src`.

The previous version (F10-*-v3, with its optional grades 6–7 extra) is preserved in [archive/](archive/README.md) with its sources, and its PDFs are in `lowell-math-circle-year-2/week-10/archive/`. Older versions remain in the `archive-before-*` folders here and beside the PDFs.
