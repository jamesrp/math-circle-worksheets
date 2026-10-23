# Chip firing with a sink: Week 11 editable release — current editable source

**Problem files, October 23, 2026.** The student packets are stored as [problem files](../problem-files/README.md): `week.toml`, `figures.py` (the old builder's drawing code and page template, unchanged) and one file per problem in `problems/`, with each band's wording inside it. The conversion changed no wording or figure. The rebuilt LaTeX is byte-identical to the previous builder's (the page header, footer and number come from `page_open` and `page_close` in `figures.py`), and the three print PDFs match in pages and extracted text; grades 2–3 and 4–5 match in 100-dpi pixels, and K–1 page 6 differs by 100 pixels of glyph antialiasing that the previous builder's LaTeX shows too when compiled in the same TeX installation (TeX Live 2023, pdfTeX 1.40.25; the October 4 references were made with pdfTeX 1.40.27). For the same reason a clean rebuild of the unchanged guide here matches its LaTeX source but not its reference pixels. The previous builder (`build_packets.py`) and source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md); its numerical and order checks moved unchanged to `editable/src/student_checks.py`.

- **Student pages:** edit `problems/*.md` (figures in `figures.py`), then build every view:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-11 --out tmp/week-11-views --tex --publish lowell-math-circle-year-2/band-views/week-11
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-11-views lowell-math-circle-year-2/week-11 week-11
  ```

  The first-route and return packets, the one-page problem menu and the key arranged by problem are published in [band-views/week-11/](../../band-views/README.md#weeks-stored-as-problem-files).
- **Adult guide:** its source is still `editable/facilitator-src/build_guide.py` (with `mathematical-overview.tex`), which writes `facilitator-guide.tex`; the package builds it. The problem files' `key` and `hints` sections repeat its answers for the key view; `python3 lowell-math-circle-year-2/source/week-11/check_guide_copy.py` checks that every key sentence and table row still appears in the guide. Change both together.
- **Portable package:** `editable/` is the package; `editable/src/regenerate.py` writes the student LaTeX from the problem files, and the package build runs it before compiling. The [portable source ZIP](chip-firing-week11-editable-source.zip) holds the package plus the problem files and tools in `problem-files/`, written by `package.py`:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-11 --zip chip-firing-week11-editable-source.zip --top chip-firing-week11-editable-source
  ```

  Rebuild it after any change and check a clean rebuild from the extracted ZIP.

The [portable base source ZIP](chip-firing-week11-editable-source.zip) and [complete extracted package](editable/README.md) contain the current **October 4, 2026 fresh-review revision**. Current print copies are in [../../week-11/](../../week-11/). References are exact duplicates of those print PDFs.

Read `editable/README.md` for dependencies and commands. Copy the complete package to a fresh folder under the project's `tmp/` before rebuilding; keep intermediates out of current print/source folders. `verify_revision.py` checks current pages and permits only specifically audited full-page alternate hashes for pre-existing font/hyphenation differences in unchanged student packets; the original strict verifier remains available. Every changed packet and guide reproduces exact 100-dpi pixels from the extracted ZIP.

The [corpus revision report](../../../plans/fresh-review-revision-2026-10-04/REPORT.md) records per-band decisions, independent mathematical/visual checks, all clean-ZIP rebuilds and physical-testing limits. Previous affected print PDFs and the complete previous source ZIP are separately archived in `archive-before-fresh-review-2026-10-04/` within their print/source folders; the builder replaced by problem files is in `archive-before-problem-files-2026-10-23/`. Bonus companions are separate; this base ZIP does not incorporate them. The theme remains **unpiloted** and can span several meetings.
