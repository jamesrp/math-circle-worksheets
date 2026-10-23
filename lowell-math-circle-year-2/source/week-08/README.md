# Week 8: Rook race and Nim

Concrete revision of October 3, 2026: F08-K-v4 / F08-M-v4 / F08-U-v4, adult guide F08-FAC-v4. **Unpiloted.** It follows the organizer's report on Weeks 1 and 2 (the October 3 forecast and pivot, a private record: see [LOCAL-RESOURCES.md](../../../LOCAL-RESOURCES.md#private-records)): rules enforced by the materials or by the other player, partner play at fixed KK11 / 3333 / 445 tables, and deeper questions late in each packet.

- [K–1](../../week-08/week-08-k-1.pdf) — 7 pages.
- [Grades 2–3](../../week-08/week-08-grades-2-3.pdf) — 5 pages.
- [Grades 4–5](../../week-08/week-08-grades-4-5.pdf) — 7 pages.
- [Game boards](../../week-08/week-08-materials.pdf) — 4 sheets: the separate 8-by-8 and 5-by-5 boards with 1-inch squares, and the 8-by-8 in two halves for a printer that cuts an edge. Each sheet says how many copies to print and has a 10 cm check line. **Physically unrehearsed:** not yet printed and measured.
- [Adult guide](../../week-08/week-08-facilitator.pdf) — 9 pages: materials and counts, launch, pairing, answers, hints, and what to record.

October 23, 2026: the separate game boards the guide asks for are now a printable PDF built from `materials/` (F08-MAT-v1), and the guide points to them; a checkerboard with a star sticker still works. Guide corrections from the [review card](../../../plans/review/week-08.md): section 1 now states Bouton's rule with its limits and the queen pairs, and separates play, conjecture and explanation; 4–5 starts with pages 1–3, since page 4 prints five of Problem 4's answers; page 5's squares are 1.05 inch; the launch shows what children circle; the K–1 notes match Problems 6–7 (the partner goes first, then the adult); and the 4–5 Problem 9 picture has its star. Student packets are unchanged; the previous guide is in `week-08/archive-before-card-fixes-2026-10-23/`.

A token races to the star corner of a board, moving straight toward it; the diagonal squares are the ones to move to, which is two-pile Nim with the copying strategy. Grades 2–3 map the board and move to piles; grades 4–5 play three-pile Nim, find balanced positions and binary bundles, and try the queen game (Wythoff) later in the packet.

One token per pair on 1-inch squares (a green triangle or a counter). The opponent checks that every move is legal. Print the game boards at 100% and check the 10 cm line on one sheet before printing the rest.

Print US Letter, single-sided, at 100% / Actual Size. Give one page at a time; the packets hold more than an hour, and stopping anywhere is fine.

The student pages were drafted with the [worksheet workflow](../../../worksheet-workflow/README.md) from the outline `worksheet-workflow/outlines/week-08-rooks-nim.md`: writer, adversarial review and independent math check, then revision. The run record (prompts, reviews, draft and final PDFs) is in `tmp/worksheet-runs/week-08-rooks-nim-v1/`. The adult guide was written separately from the final pages; its answers are recomputed by the scripts in `guide-src/`.

Rebuild from the repository root: `sh lowell-math-circle-year-2/source/week-08/build.sh`. It builds in `tmp/pdfs/week-08-build/` and copies the five PDFs into `lowell-math-circle-year-2/week-08/`. Requires Python 3 and XeLaTeX (student pages) and pdfLaTeX (guide) with TikZ, fontspec and TeX Gyre Heros and Source Sans Pro. `src/` holds the student pages with their generators and checks; `materials/` holds the game-board builder (`materials.py`, which writes `materials.tex`) and `check_materials.py`, which measures the squares and the scale line in the PDF (it needs PyMuPDF and is skipped without it); `guide-src/` holds the adult guide and its answer checks, which read `../src`.

The previous version (F08-*-v3, with its optional grades 6–7 extra) is preserved in [archive/](archive/README.md) with its sources, and its PDFs are in `lowell-math-circle-year-2/week-08/archive/`. Older versions remain in the `archive-before-*` folders here and beside the PDFs.
