# Week 4: Stars and secret wheels

**Problem files, October 23, 2026.** The student packets are stored as [problem files](../problem-files/README.md): `week.toml`, `template.tex` (the old builder's preamble), and one file per problem in `problems/`, with each band's wording inside it; the hop rule and the two cut-out wheels are shared by Grades 2–3 and 4–5. The figures are Python expressions evaluated in `figures.py`, which carries over the old builder's drawing code (`src/gen.py`, with `src/tikzlib.py`); `src/check.py` still checks the pieces, codes and cracking. The conversion changed no wording or figure: the rebuilt packets match the previous PDFs in pages, extracted text and 100-dpi pixels (`compare.py`). The previous builder, its generated LaTeX and the week's build script are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md). The build also publishes each band's first-route packet (the guide's core problems) and return packet, a one-page problem menu and a problem list to [band-views/week-04/](../../band-views/README.md#weeks-stored-as-problem-files); the answers stay in the adult guide.

Concrete revision of October 3, 2026: F04-K-v4 / F04-M-v4 / F04-U-v4, adult guide F04-FAC-v4. **Unpiloted.** It follows the organizer's report on Weeks 1 and 2 (the October 3 forecast and pivot, a private record: see [LOCAL-RESOURCES.md](../../../LOCAL-RESOURCES.md#private-records)): rules enforced by the materials or by the other player, partner play at fixed KK11 / 3333 / 445 tables, and deeper questions late in each packet.

- [K–1](../../week-04/week-04-k-1.pdf) — 10 pages.
- [Grades 2–3](../../week-04/week-04-grades-2-3.pdf) — 9 pages.
- [Grades 4–5](../../week-04/week-04-grades-4-5.pdf) — 11 pages.
- [Adult guide](../../week-04/week-04-facilitator.pdf) — 10 pages: materials and counts, launch, pairing, answers, hints, and what to record.

October 23, 2026: guide-only corrections from the [review card](../../../plans/review/week-04.md). The 4–5 Problem 12 answer and section 5 now say that the times-table curves touch the circle at the fixed dots and put the dents inside: a third of the radius from the centre toward dot 12 for ×2, half the radius toward dots 6 and 18 for ×3. The guide also notes that K–1 Problem 5's six-pointed star and three lines need the restart, prints a second copy of 2–3 p. 6 for trying hops, adds a 2–3 pacing note, and corrects "every other dot" and the MROOB dictionary words. `guide-src/check_answers.py` checks the new statements. Student packets are unchanged; the previous guide is in `week-04/archive-before-card-fixes-2026-10-23/`.

Ring shifts made visible. Children hop counters and draw skip-stars on circles of dots; the number of separate pieces of a star is gcd(n, k). Grades 2–3 and 4–5 also cut out and assemble shift wheels to encode, decode and crack messages and to combine shifts. K–1 uses picture rings instead of letters.

Shift wheels are cut out from the last pages and joined with brass fasteners; older children can cut their own, and a few spare pre-cut wheels help. Check that counters fit on the K–1 dots.

Print US Letter, single-sided, at 100% / Actual Size. Give one page at a time; the packets hold more than an hour, and stopping anywhere is fine.

The student pages were drafted with the [worksheet workflow](../../../worksheet-workflow/README.md) from the outline `worksheet-workflow/outlines/week-04-stars-wheels.md`: writer, adversarial review and independent math check, then revision. The run record (prompts, reviews, draft and final PDFs) is in `tmp/worksheet-runs/week-04-stars-wheels-v1/`. The adult guide was written separately from the final pages; its answers are recomputed by the scripts in `guide-src/`.

Rebuild from the repository root: `sh lowell-math-circle-year-2/source/week-04/build.sh`. It runs `src/check.py`, builds the packets from the problem files with `../problem-files/build.py`, then the adult guide, in `tmp/pdfs/week-04-build/`, copies the four PDFs into `lowell-math-circle-year-2/week-04/` and publishes the route packets, menu and problem list. Requires Python 3.11 and pdfLaTeX with TikZ, Source Sans Pro and Inconsolata, and the problem-file tools' requirements. `problems/` holds the student wording and `figures.py` the figure helpers; `src/` holds `tikzlib.py` and the answer checks; `guide-src/` holds the adult guide and its answer checks, which read the packets' LaTeX as built.

The previous version (F04-*-v3, with its optional grades 6–7 extra) is preserved in [archive/](archive/README.md) with its sources, and its PDFs are in `lowell-math-circle-year-2/week-04/archive/`. Older versions remain in the `archive-before-*` folders here and beside the PDFs.
