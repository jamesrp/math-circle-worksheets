# Week 36 Making threes editable source — current editable source

**Problem files, October 23, 2026.** The student packets are stored as [problem files](../problem-files/README.md): `week.toml`, `figures.py` (the old builder's drawing code and page template, unchanged) and one file per problem in `problems/`, with each band's wording inside it. The conversion changed no wording or figure. The rebuilt LaTeX is byte-identical to the previous builder's, and the three print PDFs match in pages, extracted text and 100-dpi pixels. The previous builder (`build_packets.py`) and source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md); its exact checks moved unchanged to `editable/src/student_checks.py`.

**Review-card fixes, October 23, 2026 (v3).** After the conversion, the card's shoulds and clear coulds were made: Grades 4-5 Problem 1 asks openly whether a pair can have two completing tiles or none, Grades 4-5 Problem 4 has six record boards, Grades 2-3 Problem 3 asks "How do you know you cannot keep more?", and the guide prints the tiles from K-1 p. 3, states the record-board facts, gives a shapes-only fallback and an hour-shaped timetable. The bonus guide's Problem 3 extension is corrected. [editable/review/card-shoulds-2026-10-23.md](editable/review/card-shoulds-2026-10-23.md) lists every change and check; the replaced PDFs are in `../../week-36/archive-before-card-fixes-2026-10-23/` and the replaced ZIPs in [archive-before-card-fixes-2026-10-23/](archive-before-card-fixes-2026-10-23/README.md).

- **Student pages:** edit `problems/*.md` (figures in `figures.py`), then build and compare:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-36 --out tmp/week-36-views --tex
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-36-views lowell-math-circle-year-2/week-36 week-36
  ```
- **Adult guide:** its source is still `editable/facilitator-src/guide.md`, built by the package. The problem files carry each problem's one-sentence idea (`kernel`), not its answers.
- **Portable package:** `editable/` is the package; `editable/src/regenerate.py` writes the student LaTeX from the problem files, and the package build runs it before compiling. The [portable source ZIP](nine-point-world-week36-editable-source.zip) holds the package plus the problem files and tools in `problem-files/`, written by `package.py`:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-36 --zip nine-point-world-week36-editable-source.zip --top nine-point-world-week36-source
  ```

  Rebuild it after any change and check a clean rebuild from the extracted ZIP (`python3 build.py` in the extracted folder, then compare its PDFs).


The [portable base source ZIP](nine-point-world-week36-editable-source.zip) and [complete extracted package](editable/README.md) contain the current **October 4, 2026 fresh-review revision** with the **October 23, 2026 review-card fixes (v3)**. Current print copies are in [../../week-36/](../../week-36/). References are exact duplicates of those print PDFs.

Read `editable/README.md` for dependencies and commands. Copy the complete package to a fresh folder under the project's `tmp/` before rebuilding; keep intermediates out of current print/source folders. `verify_revision.py` checks current pages and permits only specifically audited full-page alternate hashes for pre-existing font/hyphenation differences in unchanged student packets; the original strict verifier remains available. Every changed packet and guide reproduces exact 100-dpi pixels from the extracted ZIP.

The [corpus revision report](../../../plans/fresh-review-revision-2026-10-04/REPORT.md) records per-band decisions, independent mathematical/visual checks, all clean-ZIP rebuilds and physical-testing limits. Previous affected print PDFs and the complete previous source ZIP are separately archived in `archive-before-fresh-review-2026-10-04/` within their print/source folders. Bonus companions are separate; this base ZIP does not incorporate them. The theme remains **unpiloted** and can span several meetings.
