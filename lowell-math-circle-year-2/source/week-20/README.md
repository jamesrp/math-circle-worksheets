# Averaging and the maximum principle: Week 20 editable release — current editable source

**Problem files, October 23, 2026.** The student packets are stored as [problem files](../problem-files/README.md): `week.toml`, `figures.py` (the old builder's drawing code and page template) and one file per problem in `problems/`, with the shared rules in `problems/00-rules.md`. The conversion changed no wording or figure: the rebuilt LaTeX matches the old builder's line for line (only the file's final newline differs), and it compiles to the same pages, extracted text and 100-dpi pixels as the old builder's LaTeX compiled with the same TeX. Against the October 4 print PDFs, which were compiled with another TeX installation, the text is identical and up to 160 pixels per page differ in glyph rendering, exactly as for the old LaTeX compiled here. The previous builder (`build_packets.py`) and the ZIP it replaced are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

- **Student pages:** edit `problems/*.md` (figures and the page template in `figures.py`), then build every view:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-20 --out tmp/week-20-views --tex --publish lowell-math-circle-year-2/band-views/week-20
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-20-views lowell-math-circle-year-2/week-20 week-20
  ```

  The first-route and return packets (from the guide's table routes), the one-page problem menu and the key arranged by problem are published in [band-views/week-20/](../../band-views/README.md#weeks-stored-as-problem-files).
- **Adult guide:** its source is still `editable/facilitator-src/` (`content.py`, `graphs.py`, `mathematical-overview.json`, `route-note.json`), built by the package.
- **Portable package:** `editable/` is the package. `editable/src/regenerate.py` writes the student LaTeX from the problem files and solves every board with fixed values exactly (`src/answer_checks.py`, written to `src/checked-values.txt` as before; the old builder used sympy, which is no longer needed); `build.sh` runs it and compiles. The [portable source ZIP](averaging-maximum-principle-week20-editable-source.zip) holds the package plus the problem files and tools in `problem-files/`, written by `package.py`:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-20 --zip averaging-maximum-principle-week20-editable-source.zip --top averaging-maximum-principle-week20-editable-source
  ```

  Check a clean rebuild from the extracted ZIP with `bash build.sh` and `python3 verify_revision.py`.

The [portable base source ZIP](averaging-maximum-principle-week20-editable-source.zip) and [complete extracted package](editable/README.md) contain the current **October 4, 2026 fresh-review revision**. Current print copies are in [../../week-20/](../../week-20/). References are exact duplicates of those print PDFs.

Read `editable/README.md` for dependencies and commands. Copy the complete package to a fresh folder under the project's `tmp/` before rebuilding; keep intermediates out of current print/source folders. `verify_revision.py` checks current pages and permits only specifically audited full-page alternate hashes for pre-existing font/hyphenation differences in unchanged student packets; the original strict verifier remains available. Every changed packet and guide reproduces exact 100-dpi pixels from the extracted ZIP.

The [corpus revision report](../../../plans/fresh-review-revision-2026-10-04/REPORT.md) records per-band decisions, independent mathematical/visual checks, all clean-ZIP rebuilds and physical-testing limits. Previous affected print PDFs and the complete previous source ZIP are separately archived in `archive-before-fresh-review-2026-10-04/` within their print/source folders. Bonus companions are separate; this base ZIP does not incorporate them. The theme remains **unpiloted** and can span several meetings.
