# Week 32 Squares inside rectangles editable source — current editable source

**Problem files, October 23, 2026.** The student packets are stored as [problem files](../problem-files/README.md): `week.toml`, `figures.py` (the old builder's drawing code and page template, unchanged) and one file per problem in `problems/`, with each band's wording inside it. The conversion changed no wording or figure: the rebuilt LaTeX is byte-identical to the previous builder's, and `compare.py` finds the same text and no differing pixel at 100 dpi against the print copies. The previous builder (`make_packets.py`, `draw.py`) and the October 4 source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

- **Student pages:** edit `problems/*.md` (figures in `figures.py`), then build and compare:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-32 --out tmp/week-32-views --tex
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-32-views lowell-math-circle-year-2/week-32 week-32
  ```

- **Adult guide:** its source is still `editable/facilitator-src/guide.json` with `route-note.json`, built by the package. The problem files carry each problem's one-sentence idea (`kernel`), not its answers.
- **Portable package:** `editable/` is the package; `editable/student-src/regenerate.py` writes the student LaTeX from the problem files, and the package build runs it before compiling. The portable source ZIP holds the package plus the problem files and tools in `problem-files/`, written by `package.py`:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-32 --zip squares-inside-rectangles-week32-editable-source.zip --top squares-inside-rectangles-week32-source
  ```

The [portable base source ZIP](squares-inside-rectangles-week32-editable-source.zip) and [complete extracted package](editable/README.md) contain the current **October 4, 2026 fresh-review revision**. Current print copies are in [../../week-32/](../../week-32/). References are exact duplicates of those print PDFs.

Read `editable/README.md` for dependencies and commands. Copy the complete package to a fresh folder under the project's `tmp/` before rebuilding; keep intermediates out of current print/source folders. `verify_revision.py` checks current pages and permits only specifically audited full-page alternate hashes for pre-existing font/hyphenation differences in unchanged student packets; the original strict verifier remains available. Every changed packet and guide reproduces exact 100-dpi pixels from the extracted ZIP.

The [corpus revision report](../../../plans/fresh-review-revision-2026-10-04/REPORT.md) records per-band decisions, independent mathematical/visual checks, all clean-ZIP rebuilds and physical-testing limits. Previous affected print PDFs and the complete previous source ZIP are separately archived in `archive-before-fresh-review-2026-10-04/` within their print/source folders. Bonus companions are separate; this base ZIP does not incorporate them. The theme remains **unpiloted** and can span several meetings.
