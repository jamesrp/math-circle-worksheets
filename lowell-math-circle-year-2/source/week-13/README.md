# Route packing and bottlenecks: Week 13 editable release — current editable source

**Problem files, October 23, 2026.** The student packets are stored as [problem files](../problem-files/README.md): `week.toml`, `figures.py` (the old builder's boards and page template, unchanged) and one file per problem in `problems/`, with each band's wording inside it. The old builder wrote flowing LaTeX with a fancyhdr header and footer; `figures.py` keeps that document through the canvas hooks (`page_preamble`, `page_prompt`, `page_text`, `PAGE_CLOSE`). The conversion changed no wording or board: the rebuilt LaTeX is byte-identical to the previous builder's, and the three print PDFs match in pages, extracted text and 100-dpi pixels. The previous builder (`build_packets.py`) and source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md); its exhaustive checks moved unchanged to `editable/src/student_checks.py`, which reads the boards from `figures.py`.

- **Student pages:** edit `problems/*.md` (boards in `figures.py`), then build every view:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-13 --out tmp/week-13-views --tex --publish lowell-math-circle-year-2/band-views/week-13
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-13-views lowell-math-circle-year-2/week-13 week-13
  ```

  The first-route and return packets, the one-page problem menu and the key arranged by problem are published in [band-views/week-13/](../../band-views/README.md#weeks-stored-as-problem-files).
- **Adult guide:** its source is still `editable/facilitator-src/build_guide.py` (ReportLab), built by the package. The problem files' `key` and `hints` sections repeat its answers for the key view; `python3 lowell-math-circle-year-2/source/week-13/check_guide_copy.py` checks that every key sentence and table row still appears in the guide. Change both together.
- **Portable package:** `editable/` is the package; `editable/src/regenerate.py` writes the student LaTeX from the problem files, and the package build runs it before compiling. The [portable source ZIP](route-packing-week13-editable-source.zip) holds the package plus the problem files and tools in `problem-files/`, written by `package.py`:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-13 --zip route-packing-week13-editable-source.zip --top route-packing-week13-editable-source
  ```

  Rebuild it after any change and check a clean rebuild from the extracted ZIP.

The [portable base source ZIP](route-packing-week13-editable-source.zip) and [complete extracted package](editable/README.md) contain the current **October 4, 2026 fresh-review revision**. Current print copies are in [../../week-13/](../../week-13/). References are exact duplicates of those print PDFs.

Read `editable/README.md` for dependencies and commands. Copy the complete package to a fresh folder under the project's `tmp/` before rebuilding; keep intermediates out of current print/source folders. `verify_revision.py` checks current pages and permits only specifically audited full-page alternate hashes for pre-existing font/hyphenation differences in unchanged student packets; the original strict verifier remains available. Every changed packet and guide reproduces exact 100-dpi pixels from the extracted ZIP.

The [corpus revision report](../../../plans/fresh-review-revision-2026-10-04/REPORT.md) records per-band decisions, independent mathematical/visual checks, all clean-ZIP rebuilds and physical-testing limits. Previous affected print PDFs and the complete previous source ZIP are separately archived in `archive-before-fresh-review-2026-10-04/` within their print/source folders; the builder replaced by problem files is in `archive-before-problem-files-2026-10-23/`. Bonus companions are separate; this base ZIP does not incorporate them. The theme remains **unpiloted** and can span several meetings.
