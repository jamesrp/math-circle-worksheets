# Week 24 facilitator guide source

Draft and unpiloted. Unscheduled library slot. No student source or PDF was edited.

## Rebuild

Requires Python 3 and ReportLab (`python3 -m pip install reportlab`). From this directory:

1. `python3 checks.py` regenerates the independent exact audit `checks.json`.
2. `python3 build.py` writes `../facilitator-guide.pdf` using only files in this directory.
3. `mkdir -p render && pdftoppm -r 90 -png ../facilitator-guide.pdf render/final` renders all pages for visual review (Poppler).

Expected: 13 US Letter pages. `layout.py` contains the typography helpers. Bundled Liberation Sans fonts are embedded under Helvetica aliases to avoid renderer-dependent base-font substitution; the font license is included. No external image files are needed. The render directory is QA evidence and may be omitted from a source distribution.

## Verified 2026-10-03

Read repository guidance, final v2 sources and all 22 final student PDF pages, the prompt, both reviews, the mathematical reference and the relevant teaching-source pages. Independently implemented all mathematical checks, without importing the student builder/checker. The final middle Problem 6 has exact totals 15,18,21; the old draft solutions do not satisfy it. The single verified construction is A=(3,5,7), B=(2,4,12), C=(1,9,11), with directed wins 5,5,6 out of 9. The final six-round game and winner-only hidden-bag task were checked against replacement and positive-probability arguments.

All 13 final PDF pages were freshly rendered with Poppler at 90 dpi and visually inspected. Tables, matrix labels, complete case coverage, text, final page references and footers were checked. The guide includes every numbered problem, held hints and prerequisite/stopping guidance. Sources explicitly separate source claims, independent deductions and untested classroom proposals.

checks.json retains all nine swap outcomes, all replacements, the 90 fixed-maximum cases, repeated-value two-card checks, all 1,680 labeled 1-9 partitions, the revised exact-total construction search and exact short-game probabilities. The PDF gives complete human arguments in addition to the computational error checks. student-input-sha256.txt identifies the student inputs; none were modified.
