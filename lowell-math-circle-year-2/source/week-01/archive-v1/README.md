# Week 1: pattern-block worksheets

LaTeX/TikZ building mats for all six K–5 grades, using the three entry bands in the [fall activity guide](../../../../plans/fall-k-5-year-a-activities.md#week-1-block-trades). Grade bands indicate prerequisites, not fixed placement. Give one page at a time and allow sustained play; the pages are not a completion checklist.

## Print

- [K–1: The block exchange shop](../../../week-01/archive-v1/week-01-k-1.pdf): 2 pages, F01-K. Blue/red trades, then two pennant fillings.
- [Grades 2–3: Two teams, no shared colors](../../../week-01/archive-v1/week-01-grades-2-3.pdf): 3 pages, F01-M. P1, P2, then P2 without yellow.
- [Grades 4–5: The fewest pieces](../../../week-01/archive-v1/week-01-grades-4-5.pdf): 3 pages, F01-U. The same three investigations with construction and minimum-piece arguments.
- [Facilitator guide and solutions](../../../week-01/archive-v1/week-01-facilitator.pdf): 3 pages. Preparation, prerequisites, flexible hour, hints, solution diagrams, proofs, and source references.

Print **US Letter, single-sided, 100% / Actual Size**. Disable Fit/Shrink. Outlines use a **1-inch (25.4 mm) block edge**. Compare the check line on the first page with a green triangle's edge before printing the full set. A different block size requires adjusting `\blockside` in `common.tex` and rebuilding, with a fresh layout check, or tracing around actual blocks. Do not scale the PDF blindly; larger blocks may require larger paper.

The current K, K, 1 / 3, 3, 3 / 5 roster needs 3 K–1 packets, 3 middle packets, and 1 upper packet: 18 student sheets. Keep the adult guide separate. Worksheets require physical pattern blocks (or accurate paper substitutes); the supplied miniatures in the answer key are not cut-out pieces.

## Build from LaTeX

Run `sh lowell-math-circle-year-2/source/week-01/archive-v1/build.sh` from the repository root. Requires pdfLaTeX with TikZ, Source Sans Pro, microtype, fancyhdr, geometry, tabularx, hyperref, and extarticle (available in TeX Live/MacTeX). Editable `.tex` files live here; final PDFs go to `lowell-math-circle-year-2/week-01/archive-v1/`, and compilation intermediates go to `tmp/pdfs/week-01-archive-v1-build/`.

Geometry is shared in `common.tex`: P1 is one regular hexagon plus an equilateral triangle attached outside a complete edge; P2 is two regular hexagons joined at a complete edge. Student mats omit internal joins. The adult key supplies checked tilings at reduced scale. No external images or color printing are needed.

## Sources and use history

The local activity guide's F01-K/M/U sequences govern these worksheets. Relevant originals are JRMF *Changing Colors*, regular and beginner guides, PDF pp. 3–6; Lowell Handout 3, problem 3.4, Handout 4, problems 4.3–4.5, and *Pattern Block Exercises*, problems 2–4 (PDF pp. 1–2); and *Math Circle by the Bay*, preface printed pp. ix–x (PDF pp. 10–11). Exact adaptations and teaching-source limits are described in the facilitator guide.

Do not mark these activities as taught merely because PDFs were prepared. After the meeting, record the exact instances and participants in [the session use log](../../../../plans/fall-k-5-year-a-use-log.md).
