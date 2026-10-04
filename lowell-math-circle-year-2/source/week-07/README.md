# Week 7: Take-away games

Concrete revision of October 3, 2026: F07-K-v4 / F07-M-v4 / F07-U-v4, adult guide F07-FAC-v4. **Unpiloted.** It follows the organizer's report on Weeks 1 and 2 ([forecast and pivot](../../../plans/fall-forecast-2026-10-03.md)): rules enforced by the materials or by the other player, partner play at fixed KK11 / 3333 / 445 tables, and deeper questions late in each packet.

- [K–1](../../week-07/week-07-k-1.pdf) — 6 pages.
- [Grades 2–3](../../week-07/week-07-grades-2-3.pdf) — 5 pages.
- [Grades 4–5](../../week-07/week-07-grades-4-5.pdf) — 8 pages.
- [Adult guide](../../week-07/week-07-facilitator.pdf) — 9 pages: materials and counts, launch, pairing, answers, hints, and what to record.

Two-player take-away games with counters and with a token on a number track, where colouring the squares you want to leave for your opponent becomes the win/lose chart. K–1 plays 1-or-2 games and the grown-up; grades 2–3 classify piles for moves 1, 3, 4; grades 4–5 find and explain repeating patterns, change the rule, and try last-counter-loses and two-pile versions.

Track squares are about 0.68 inch: use a snap cube or small counter as the token. Adults should know the winning strategies so children can try to work out how the grown-up always wins.

Print US Letter, single-sided, at 100% / Actual Size. Give one page at a time; the packets hold more than an hour, and stopping anywhere is fine.

The student pages were drafted with the [worksheet workflow](../../../worksheet-workflow/README.md) from the outline `worksheet-workflow/outlines/week-07-take-away.md`: writer, adversarial review and independent math check, then revision. The run record (prompts, reviews, draft and final PDFs) is in `tmp/worksheet-runs/week-07-take-away-v1/`. The adult guide was written separately from the final pages; its answers are recomputed by the scripts in `guide-src/`.

Rebuild from the repository root: `sh lowell-math-circle-year-2/source/week-07/build.sh`. It builds in `tmp/pdfs/week-07-build/` and copies the four PDFs into `lowell-math-circle-year-2/week-07/`. Requires Python 3 and pdfLaTeX with TikZ and Source Sans Pro. `src/` holds the student pages with their generators and checks; `guide-src/` holds the adult guide and its answer checks, which read `../src`.

The previous version (F07-*-v3, with its optional grades 6–7 extra) is preserved in [archive/](archive/README.md) with its sources, and its PDFs are in `lowell-math-circle-year-2/week-07/archive/`. Older versions remain in the `archive-before-*` folders here and beside the PDFs.
