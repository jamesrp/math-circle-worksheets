# Week 5: Tower cities

Concrete revision of October 3, 2026: F05-K-v4 / F05-M-v4 / F05-U-v4, adult guide F05-FAC-v4. **Unpiloted.** It follows the organizer's report on Weeks 1 and 2 ([forecast and pivot](../../../plans/fall-forecast-2026-10-03.md)): rules enforced by the materials or by the other player, partner play at fixed KK11 / 3333 / 445 tables, and deeper questions late in each packet.

- [K–1](../../week-05/week-05-k-1.pdf) — 7 pages.
- [Grades 2–3](../../week-05/week-05-grades-2-3.pdf) — 9 pages.
- [Grades 4–5](../../week-05/week-05-grades-4-5.pdf) — 8 pages.
- [Adult guide](../../week-05/week-05-facilitator.pdf) — 9 pages: materials and counts, launch, pairing, answers, hints, and what to record.

Snap-cube towers viewed from the ends of a row at eye level, then Latin-square cities with outside clues. K–1 builds rows of three towers, finds every order and plays a hidden-row game behind a folder. Grades 2–3 build and solve 3-by-3 cities and make one-answer puzzles for a partner. Grades 4–5 solve a ladder of 4-by-4 puzzles and design puzzles with as few clues as possible; every printed puzzle was checked by computer.

Pre-building towers of each height saves a lot of time; the adult guide gives cube counts per table. File folders serve as screens. `src/exploration/` keeps the scripts used to search for puzzles; they are a record and not part of the build.

Print US Letter, single-sided, at 100% / Actual Size. Give one page at a time; the packets hold more than an hour, and stopping anywhere is fine.

The student pages were drafted with the [worksheet workflow](../../../worksheet-workflow/README.md) from the outline `worksheet-workflow/outlines/week-05-tower-cities.md`: writer, adversarial review and independent math check, then revision. The run record (prompts, reviews, draft and final PDFs) is in `tmp/worksheet-runs/week-05-tower-cities-v1/`. The adult guide was written separately from the final pages; its answers are recomputed by the scripts in `guide-src/`.

Rebuild from the repository root: `sh lowell-math-circle-year-2/source/week-05/build.sh`. It builds in `tmp/pdfs/week-05-build/` and copies the four PDFs into `lowell-math-circle-year-2/week-05/`. Requires Python 3 and pdfLaTeX with TikZ and Source Sans Pro. `src/` holds the student pages with their generators and checks; `guide-src/` holds the adult guide and its answer checks, which read `../src`.

The previous version (F05-*-v3, with its optional grades 6–7 extra) is preserved in [archive/](archive/README.md) with its sources, and its PDFs are in `lowell-math-circle-year-2/week-05/archive/`. Older versions remain in the `archive-before-*` folders here and beside the PDFs.
