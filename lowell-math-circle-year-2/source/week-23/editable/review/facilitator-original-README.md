# Week 23 facilitator guide source

Draft and unpiloted. Unscheduled library slot. No student packet was edited.

## Rebuild

Requires Python 3 and ReportLab (`python3 -m pip install reportlab`). From this directory:

1. `python3 checks.py` regenerates the independent exact audit `checks.json`.
2. `python3 build.py` writes `../facilitator-guide.pdf` using only files in this directory.
3. `pdftoppm -r 90 -png ../facilitator-guide.pdf render/final` renders all pages for visual review (Poppler).

Expected: 12 US Letter pages. The builder embeds the bundled Liberation Sans fonts (license included), so there are no external font or image dependencies. `layout.py` contains the drawing and typography helpers. Every numbered student problem has a keyed solution, held hints and readiness/stopping guidance. Canonical network diagrams and complete small certificates are included.

## Verified 2026-10-03

Read final v2 sources and all three final student PDFs, the prompt, both reviews, repository guidance and relevant teaching-source pages. The checks are separately implemented rather than imported from the student's builder. Verified the changed K-1 selective-binary task, neighbor-only six-bar optimum and exact swap histories. Freshly rendered all 12 guide pages and visually inspected each for legibility, overlap, missing symbols, diagrams and footers. The final source attribution was corrected against the book's title page, and the final page rerendered and rechecked. Student source and PDF hashes are in `student-input-sha256.txt`; no student modifications were made.

The script gives finite checks; the PDF supplies complete human arguments and explicitly limits source and classroom-evidence claims. Before teaching, treat timing and readiness judgments as proposals to adjust after observation.
