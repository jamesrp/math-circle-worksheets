# Week 49 Four towers and differences editable source — current editable source

**Problem files, October 23, 2026.** The student packets are stored as [problem files](../problem-files/README.md): `week.toml`, `figures.py` (the old builder's drawing code; the pages use the house canvas template) and one file per problem in `problems/`, with each band's wording inside it. The conversion changed no wording or figure: the three print PDFs match the rebuilt ones in pages, extracted text and 100-dpi pixels. The previous builder (`make.py`, `draw.py`) and the ZIP it came in are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

- **Student pages:** edit `problems/*.md` (figures in `figures.py`), then build every view:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-49 --out tmp/week-49-views --tex --publish lowell-math-circle-year-2/band-views/week-49
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-49-views lowell-math-circle-year-2/week-49 week-49
  ```

  The first-route and return packets, the one-page problem menu and the key of each problem's idea are published in [band-views/week-49/](../../band-views/README.md#weeks-stored-as-problem-files).
- **Adult guide:** its source is still `editable/facilitator-src/content.json` (ReportLab) with `route-note.json`, built by the package.
- **Portable package:** `editable/` is the package; `editable/src/regenerate.py` writes the student LaTeX from the problem files, and the package build runs it before compiling. The [portable source ZIP](four-tower-differences-week49-editable-source.zip) holds the package plus the problem files and tools in `problem-files/`. Rebuild it with `python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-49 --zip four-tower-differences-week49-editable-source.zip --top four-tower-differences-week49-source` and check a clean rebuild from the extracted ZIP (`python3 build.py`, then `python3 verify_revision.py`).

The [portable base source ZIP](four-tower-differences-week49-editable-source.zip) and [complete extracted package](editable/README.md) contain the current **October 4, 2026 fresh-review revision**. Current print copies are in [../../week-49/](../../week-49/). References are exact duplicates of those print PDFs.

Read `editable/README.md` for dependencies and commands. Copy the complete package to a fresh folder under the project's `tmp/` before rebuilding; keep intermediates out of current print/source folders. `verify_revision.py` checks current pages and permits only specifically audited full-page alternate hashes for pre-existing font/hyphenation differences in unchanged student packets; the original strict verifier remains available. Every changed packet and guide reproduces exact 100-dpi pixels from the extracted ZIP.

The [corpus revision report](../../../plans/fresh-review-revision-2026-10-04/REPORT.md) records per-band decisions, independent mathematical/visual checks, all clean-ZIP rebuilds and physical-testing limits. Previous affected print PDFs and the complete previous source ZIP are separately archived in `archive-before-fresh-review-2026-10-04/` within their print/source folders. Bonus companions are separate; this base ZIP does not incorporate them. The theme remains **unpiloted** and can span several meetings.
