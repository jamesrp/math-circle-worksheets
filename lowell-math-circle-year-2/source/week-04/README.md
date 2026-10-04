# Week 4: Stars and secret wheels

Concrete revision of October 3, 2026: F04-K-v4 / F04-M-v4 / F04-U-v4, adult guide F04-FAC-v4. **Unpiloted.** It follows the organizer's report on Weeks 1 and 2 ([forecast and pivot](../../../plans/fall-forecast-2026-10-03.md)): rules enforced by the materials or by the other player, partner play at fixed KK11 / 3333 / 445 tables, and deeper questions late in each packet.

- [K–1](../../week-04/week-04-k-1.pdf) — 10 pages.
- [Grades 2–3](../../week-04/week-04-grades-2-3.pdf) — 9 pages.
- [Grades 4–5](../../week-04/week-04-grades-4-5.pdf) — 11 pages.
- [Adult guide](../../week-04/week-04-facilitator.pdf) — 10 pages: materials and counts, launch, pairing, answers, hints, and what to record.

Ring shifts made visible. Children hop counters and draw skip-stars on circles of dots; the number of separate pieces of a star is gcd(n, k). Grades 2–3 and 4–5 also cut out and assemble shift wheels to encode, decode and crack messages and to combine shifts. K–1 uses picture rings instead of letters.

Shift wheels are cut out from the last pages and joined with brass fasteners; older children can cut their own, and a few spare pre-cut wheels help. Check that counters fit on the K–1 dots.

Print US Letter, single-sided, at 100% / Actual Size. Give one page at a time; the packets hold more than an hour, and stopping anywhere is fine.

The student pages were drafted with the [worksheet workflow](../../../worksheet-workflow/README.md) from the outline `worksheet-workflow/outlines/week-04-stars-wheels.md`: writer, adversarial review and independent math check, then revision. The run record (prompts, reviews, draft and final PDFs) is in `tmp/worksheet-runs/week-04-stars-wheels-v1/`. The adult guide was written separately from the final pages; its answers are recomputed by the scripts in `guide-src/`.

Rebuild from the repository root: `sh lowell-math-circle-year-2/source/week-04/build.sh`. It builds in `tmp/pdfs/week-04-build/` and copies the four PDFs into `lowell-math-circle-year-2/week-04/`. Requires Python 3 and pdfLaTeX with TikZ and Source Sans Pro. `src/` holds the student pages with their generators and checks; `guide-src/` holds the adult guide and its answer checks, which read `../src`.

The previous version (F04-*-v3, with its optional grades 6–7 extra) is preserved in [archive/](archive/README.md) with its sources, and its PDFs are in `lowell-math-circle-year-2/week-04/archive/`. Older versions remain in the `archive-before-*` folders here and beside the PDFs.
