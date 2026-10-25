# Make the printable materials for "{TOPIC}"

The student pages for this theme are final drafts, but some objects they ask children to use are printed nowhere, so a parent volunteer would have to hand-make them. Your job is one materials file that supplies them. Work only inside `{RUN}`: sources in `{RUN}/src/`, output `{RUN}/materials.pdf`. Do not edit the student pages, the guide or anything else in the repository.

## Read first

1. `/home/claude/math-circle-worksheets/AGENTS.md`, especially "Make activities usable", "Size diagrams for their use" and "Review age fit operationally".
2. The final student pages and their sources: `{DRAFT}/k-1.pdf`, `{DRAFT}/grades-2-3.pdf`, `{DRAFT}/grades-4-5.pdf`{EXTRA}, and `{DRAFT}/src/`. Render every page and read it. List every physical object a problem asks children to build on, cut, move, lay out or play on, and whether a packet already prints it at usable size.
3. The outline `{OUTLINE}`, especially its materials and their physical constraints (piece sizes, counter widths, board spacing).
4. The draft facilitator guide `{GUIDE}` (source in the same run's `draft/src/`): its materials and preparation sections may describe hand-made workarounds. Known gaps it reported: {GAPS}
5. Model materials files from the library: `/home/claude/math-circle-worksheets/lowell-math-circle-year-2/week-91/week-91-materials.pdf` and `/home/claude/math-circle-worksheets/lowell-math-circle-year-2/week-87/week-87-materials.pdf` (sources under `lowell-math-circle-year-2/source/week-91/` and `source/week-87/`), and this theme family's one existing mat, `/home/claude/math-circle-worksheets/plans/topic-scouting/drafts/train-yard-sorting/track-mat.pdf`.

## What to make

- Every object the pages use that no packet prints at a size children can work on, and nothing the packets already supply. Boards and mats at playing size for the stated counters or pieces; strips, cards, tiles or templates on cut lines. Use each object's name exactly as the pages use it (for example "the 3 by 5 board"), so a child or adult can match it to the problem.
- Objects that cannot be printed (cubes, counters, coins, scissors) stay in the guide's list; do not draw substitutes for them unless paper versions are clearly better and the outline allows it.
- US Letter, pdfLaTeX, printed single-sided at 100%. Header `Week NN / {TOPIC} / Materials`; footer `Bellingham Math Circle / Week NN / {PREFIX}-M-v1` with the page number. Match the look of the model materials files. Short object labels only; no instructions, encouragement or teaching notes on the sheets (those belong in the guide). Keep 12 mm or more from every paper edge.
- Few pages. Group objects so a volunteer can print one set per pair or per table with minimal cutting, and put objects only one band uses on their own page where that saves printing.
- Sizes are the point of this file. Draw squares and regular shapes with equal scaling on both axes, size cells and spaces from the outline's constraints, and keep labels clear of pieces.

## Checks before you finish

- Compile with no errors or overfull boxes. Render every page and look at it.
- Measure the delivered PDF, not the source: write `src/check_materials.py` to confirm the key dimensions (cell sizes, card sizes, spacing) by reading the PDF's drawn paths or by rendering at a known DPI and measuring pixels, within 0.5 mm. Confirm every board's shape matches the problem that uses it (for example the same rows and columns, the same printed marks).
- Confirm nothing on these pages gives away an answer that a problem asks children to find.

Report back in a few sentences: the page count; each page's objects and which problems use them; how many copies to print per pair or per table; the measured sizes; and anything still needing hand preparation.
