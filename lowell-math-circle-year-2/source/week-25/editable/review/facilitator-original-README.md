# Week 25 facilitator guide source

This portable bundle rebuilds the 18-page PDF `../facilitator-guide.pdf`. It does not modify or rebuild student packets. The guide is a draft and unpiloted, for an unscheduled library slot. It matches final student versions W25-K-v2 (7 pages), W25-23-v2 (6 pages), and W25-45-v2 (7 pages), including K-1 Problem 6 and the upper Problem 3 route continuation.

## Rebuild

Requirements: Python 3.9 or newer and ReportLab. The verified build used Python 3.12.14 and ReportLab 4.4.9. All fonts needed by the builder are bundled under `fonts/`, including their redistribution license. No LaTeX, network access, absolute repository path, or system font lookup is needed.

From this directory:

```sh
python3 -m pip install reportlab==4.4.9
python3 verify_math.py --output verification.json
python3 build_guide.py --output ../facilitator-guide.pdf
```

For an isolated environment, create and activate a Python virtual environment before installing. Both scripts accept `--help`. The builder uses deterministic PDF metadata (`invariant=1`) and explicit Letter-sized pagination. Changing `--output` permits a non-destructive comparison build.

## Editing

`build_guide.py` is the complete editable text and vector-diagram source. Each `g.new(...)` starts one guide page; the following paragraphs and board strings specify its content. Board strings use 1 for a counter, 0 for an empty cell, and `/` between rows from top to bottom. Labels and actual margins are drawn automatically. Dots denote occupied cells, not named or individually distinguishable pieces.

The builder asserts paragraph and diagram clearance; its `layout-checks.json` reports each page's last content cursor. A cursor includes trailing paragraph space, so it can be below the last printed baseline. It is not a substitute for visual inspection. After any edit, rebuild, rerun the independent checks, render every page, and inspect the images.

```sh
mkdir -p render
pdftoppm -r 100 -png ../facilitator-guide.pdf render/page
```

Poppler (`pdftoppm`) is optional for rebuilding but necessary for the same rendering workflow used here. The QA record reports the actual final inspection. Font files are Liberation Sans under their included license; embed them rather than relying on a PDF viewer's substitute Helvetica.

## Mathematical independence

`verify_math.py` is a separate standard-library program, not an import or replay of the student builder or its answer files. It reconstructs binary pictures by row-subset enumeration, builds every legal rectangle-switch edge, and uses breadth-first search for shortest distances. It checks all printed fixed margin cases, explicit route examples, all printed switch options, four-counter construction examples and full four-counter margin classes, uniqueness for all 4,864 binary boards of shapes 2x4, 2x6, and 3x3, and every same-margin two-row ordered pair against the distance, count, and diameter formulas.

`verification.json` contains the full fixed-case catalogs, exact switch results, shortest routes, counts, and student-PDF hashes. Hash collection is optional if only this source folder is copied elsewhere. It does not make the guide depend on the student files. General results are proved in the guide; finite checks are not represented as proofs of an infinite family.

## Navigation

- Pages 1-2: supplies, prerequisites, common launch, flexible hour, hint use
- Pages 3-7: all K-1 numbered tasks, including revised Problem 6
- Pages 8-11: all grades 2-3 numbered tasks
- Pages 12-15: all grades 4-5 numbered tasks and full two-row theorem
- Page 16: complete no-switch uniqueness proof
- Page 17: extensions and post-pilot observation plan
- Page 18: verified references, independent check scope, honest limits

## Source record

The guide was aligned with the repository's AGENTS.md, README.md, Week 25 PROMPT.md, review.md, review-math.md, and final PDFs/source. The final student texts were extracted and all 20 student pages were inspected in fresh renders. The broad source brief is not treated as a later instruction to change the student tasks.

Primary mathematics: H. J. Ryser, *Combinatorial Properties of Matrices of Zeros and Ones*, Canadian Journal of Mathematics 9 (1957), 371-377, section 3, Theorem 3.1, pp. 375-376. The Cambridge PDF definition and proof body were read on 2026-10-03. DOI verified against the publisher record: https://doi.org/10.4153/CJM-1957-044-3 . The guide's nested-row and exact two-row proofs are independently supplied arguments.

Pedagogy: Laura Givental, Maria Nemirovskaya, Ilya Zakharevich, *Math Circle by the Bay: Topics for Grades 1-5*, Preface vii-ix, especially ix, inspected in the repository's MSRI collection. The reference supports discussion of manipulatives, peer interaction, reserve tasks, pace, and explaining. The guide's launch, held hints, pacing menu, and observation plan are proposed adaptations, not claims of demonstrated classroom effectiveness.
