# Polyomino perimeter and shared edges: Week 26 editable release — current editable source

**Problem files, October 23, 2026.** The student packets are stored as [problem files](../problem-files/README.md): `week.toml`, `figures.py` (the old builder's drawing code and page template) and one file per problem in `problems/`, with each band's wording inside it. The conversion changed no wording or figure. The three print PDFs rebuild with the same pages, extracted text and 100-dpi pixels, and the rebuilt LaTeX matches the old builder's byte for byte once the header and footer macros are expanded. The previous builder (`build_packets.py`) and the ZIP it replaced are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

- **Student pages:** edit `problems/*.md` (figures and the page template in `figures.py`), then build every view:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-26 --out tmp/week-26-views --tex
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-26-views lowell-math-circle-year-2/week-26 week-26
  ```

  The print copies in [../../week-26/](../../week-26/) and `editable/reference-pdfs/` come from the package build below, whose student pages are these same packets.
- **Adult guide:** its source is still `editable/facilitator-src/build_guide.py` (ReportLab) with `overview-content.json`, built by the package. Each problem file's `key` repeats the main answer from the guide page it names, and `guide/overview.tex` repeats the guide's overview; `python3 lowell-math-circle-year-2/source/week-26/check_guide_copy.py` checks that every copied sentence is still in the guide source. Change both together.
- **Portable package:** `editable/` is the package. `editable/src/regenerate.py` writes the student LaTeX from the problem files and `editable/src/check_shapes.py` checks the shapes they print; the package's `build.sh` runs both before compiling. The [portable source ZIP](polyomino-perimeter-week26-editable-source.zip) holds the package plus the problem files and tools in `problem-files/`, written by `package.py` (see the problem-files README). Rebuild it after any change and check a clean rebuild from the extracted ZIP with its `build.sh` and `verify_revision.py`.

The package contains the **October 4, 2026 fresh-review revision** with the **October 23, 2026 guide corrections** from the review card (`editable/review/card-fixes-2026-10-23.md`). Current print copies are in [../../week-26/](../../week-26/). References are exact duplicates of those print PDFs.

Read `editable/README.md` for dependencies and commands. Copy the complete package to a fresh folder under the project's `tmp/` before rebuilding; keep intermediates out of current print/source folders. `verify_revision.py` checks current pages and permits only specifically audited full-page alternate hashes for pre-existing font/hyphenation differences in unchanged student packets; the original strict verifier remains available. Every changed packet and guide reproduces exact 100-dpi pixels from the extracted ZIP.

The [corpus revision report](../../../plans/fresh-review-revision-2026-10-04/REPORT.md) records per-band decisions, independent mathematical/visual checks, all clean-ZIP rebuilds and physical-testing limits. Previous affected print PDFs and the complete previous source ZIP are separately archived in `archive-before-fresh-review-2026-10-04/` within their print/source folders; the guide and ZIP replaced on October 23 are in `archive-before-card-fixes-2026-10-23/`. Bonus companions are separate; this base ZIP does not incorporate them. The theme remains **unpiloted** and can span several meetings.
