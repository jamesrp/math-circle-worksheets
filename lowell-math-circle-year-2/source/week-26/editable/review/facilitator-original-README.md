# Week 26 facilitator source

Status: draft / unpiloted. Unscheduled library slot. Created 2026-10-03.

## Rebuild from any directory

The source folder is self-contained: editable prose and layout are in `build_guide.py`, mathematical example coordinates and independent verification are in `check_math.py`, and the two embedded font files and their license are in `fonts/`. No absolute repository path, original student builder, TeX format, network access, or external artwork is needed to build.

Requirements: Python 3.10+ and ReportLab 4.x. Install ReportLab in your chosen environment if necessary: `python3 -m pip install reportlab`. The mathematical checker uses only the Python standard library. PDF QA additionally uses `pdfplumber`; rendering uses Poppler's `pdftoppm`.

Run:

1. `python3 check_math.py`
2. `python3 build_guide.py` (writes `../facilitator-guide.pdf`)
3. Or use an explicit output: `python3 build_guide.py /path/to/facilitator-guide.pdf`
4. Render: `pdftoppm -r 110 -png ../facilitator-guide.pdf /your/qa-folder/guide`
5. Inspect every rendered page after edits. The builder raises an error if a content block crosses the reserved footer area.

The optional `check_pdf.py` audits page count, embedded source labels, basic text geometry and coverage: `python3 check_pdf.py ../facilitator-guide.pdf`.

## Coverage

The guide gives full solutions, diagrams, held hints and prerequisite gates for all six numbered problems in each of the three final student packets, with a concrete launch, practical materials, flexible hour menu, complete general proofs, extensions, source locators and limitations.

Guide pages 4-7: K-1 Problems 1-6.
Guide pages 8-12: Grades 2-3 Problems 1-6.
Guide pages 13-17: Grades 4-5 Problems 1-6.
Pages 1-3: practical session support and reusable proofs. Page 18: extensions, source evidence and verification limits.

The final K-1 Problem 6 asks for one best relocation result for each start. Its minima are 14, 10 and 12. Only the latter two starts can be shortened. The old request to find every move is not retained.

The Grades 4-5 Problem 2 hole answer is intentionally yes: the guide gives a connected 12-tile, 11-shared-side, perimeter-26 example that encloses an empty cell via incidental corner contact. A 2-by-2 block is impossible in a maximizer. The guide does not confuse these facts or impose a no-corner-contact rule.

## What the checks establish

`check_math.py` was written independently of the student builder. It counts perimeter by directly testing each tile's four neighbor positions, not by using 4n - 2e. It then compares that direct count with a separate shared-side count. It checks every solution illustration and the fewest-starting-tile constructions, exhausts all legal one-tile relocations of the three K-1 starts, and independently grows all fixed connected polyominoes through 8 tiles before identifying turns/flips. It also checks the balanced dimension-pair lower bound and explicit attaining construction for every n from 1 to 200. `checks.json` is its full machine-readable output.

Finite enumeration is not a proof for arbitrary n. The guide supplies the independent counting, connectivity, row/column and balancing arguments for the general claims. No claim of classroom success or real-world timing validation is made.

`qa.json` records inspection and a self-contained rebuild comparison. `page-map.json` records the guide's page-level contents. Student PDF SHA-256 checks before and after authoring confirm they were not changed.
