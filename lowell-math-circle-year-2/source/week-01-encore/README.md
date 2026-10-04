# Week 1 encore: Pattern blocks II

Concrete revision of October 3, 2026: F01E-K-v1 / F01E-M-v1 / F01E-U-v1, adult guide F01E-FAC-v1. **Unpiloted.** It follows the organizer's report on Weeks 1 and 2 ([forecast and pivot](../../../plans/fall-forecast-2026-10-03.md)): rules enforced by the materials or by the other player, partner play at fixed KK11 / 3333 / 445 tables, and deeper questions late in each packet.

- [K–1](../../week-01-encore/week-01-encore-k-1.pdf) — 7 pages.
- [Grades 2–3](../../week-01-encore/week-01-encore-grades-2-3.pdf) — 7 pages.
- [Grades 4–5](../../week-01-encore/week-01-encore-grades-4-5.pdf) — 10 pages.
- [Adult guide](../../week-01-encore/week-01-encore-facilitator.pdf) — 8 pages: materials and counts, launch, pairing, answers, hints, and what to record.

A second pattern-block session, written after the organizer reported that Week 1 went well and the children did not finish. Every table plays a two-player placement game with blue rhombi on triangle-grid boards (the copying strategy decides the winner on half-turn-symmetric boards). K–1 makes giant copies on the Upscale pieces and fills pictures with the fewest and most pieces. Grades 2–3 count two-up and two-down red trapezoids across different tilings and solve fewest-piece puzzles. Grades 4–5 turn rhombus tilings into cube stacks (a flip adds or removes one cube) and compare red-trapezoid tilings, where odd returns are possible.

Boards are printed at actual size (small triangle edge 1 inch); check one board against a green triangle. Upscale 2× and 3× pieces trivialize fewest-piece tasks, so those tasks say to use small pieces. The 4–5 table needs snap cubes and the inside corner of a small box. The unused problems of the [Week 1 packets](../week-01/README.md) remain available as well.

Print US Letter, single-sided, at 100% / Actual Size. Give one page at a time; the packets hold more than an hour, and stopping anywhere is fine.

The student pages were drafted with the [worksheet workflow](../../../worksheet-workflow/README.md) from the outline `worksheet-workflow/outlines/week-01e-pattern-blocks.md`: writer, adversarial review and independent math check, then revision. The run record (prompts, reviews, draft and final PDFs) is in `tmp/worksheet-runs/week-01e-pattern-blocks-v1/`. The adult guide was written separately from the final pages; its answers are recomputed by the scripts in `guide-src/`.

Rebuild from the repository root: `sh lowell-math-circle-year-2/source/week-01-encore/build.sh`. It builds in `tmp/pdfs/week-01-encore-build/` and copies the four PDFs into `lowell-math-circle-year-2/week-01-encore/`. Requires Python 3 and pdfLaTeX with TikZ and Source Sans Pro. `src/` holds the student pages with their generators and checks; `guide-src/` holds the adult guide and its answer checks, which read `../src`.
