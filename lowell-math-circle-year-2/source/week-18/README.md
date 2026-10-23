# Error-correcting codebooks: Week 18 editable release — current editable source

**Problem files, October 23, 2026.** The student packets are stored as [problem files](../problem-files/README.md): `week.toml`, `figures.py` (the old builder's pictures, counter strips and page template) and one file per problem in `problems/`, with each band's wording inside it; problems that the bands share in different words (which keys work, the shortest key for two pictures, four pictures in five counters, three pictures in a short key) are one file each. The conversion changed no wording or figure: the rebuilt LaTeX is byte-identical to the old builder's, and the three print PDFs rebuild with the same pages and extracted text. Their 100-dpi pixels differ by at most 157 pixels a page because the print copies were made with pdfTeX 1.40.27 and this rebuild with 1.40.25; for the same reason `verify_revision.py` reports those pages as unreviewed with TeX Live 2023, before and after the conversion. The old builder (`build_packets.py`, `examples.py`) and the ZIP it replaced are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

- **Student pages:** edit `problems/*.md` (drawings and the page template in `figures.py`), then build every view:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-18 --out tmp/week-18-views --tex --publish lowell-math-circle-year-2/band-views/week-18
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-18-views lowell-math-circle-year-2/week-18 week-18
  ```

  The print copies in [../../week-18/](../../week-18/) and `editable/reference-pdfs/` come from the package build below, whose student pages are these same packets. The first-route and return packets, the one-page problem menu and a key view are published in [band-views/week-18/](../../band-views/README.md#weeks-stored-as-problem-files).
- **Adult guide:** its source is still `editable/facilitator-src/guide.json` with `route-note.json`, built by the package.
- **Portable package:** `editable/` is the package. `editable/src/regenerate.py` writes the student LaTeX from the problem files, and the package's `build.sh` runs it before compiling. The [portable source ZIP](error-correcting-codebooks-week18-editable-source.zip) holds the package plus the problem files and tools in `problem-files/`, written by `package.py` (see the problem-files README). Rebuild it after any change and check a clean rebuild from the extracted ZIP with its `build.sh` and `verify_revision.py`.

The [portable base source ZIP](error-correcting-codebooks-week18-editable-source.zip) and [complete extracted package](editable/README.md) contain the current **October 4, 2026 fresh-review revision**. Current print copies are in [../../week-18/](../../week-18/). References are exact duplicates of those print PDFs.

Read `editable/README.md` for dependencies and commands. Copy the complete package to a fresh folder under the project's `tmp/` before rebuilding; keep intermediates out of current print/source folders. `verify_revision.py` checks current pages and permits only specifically audited full-page alternate hashes for pre-existing font/hyphenation differences in unchanged student packets; the original strict verifier remains available. Every changed packet and guide reproduces exact 100-dpi pixels from the extracted ZIP.

The [corpus revision report](../../../plans/fresh-review-revision-2026-10-04/REPORT.md) records per-band decisions, independent mathematical/visual checks, all clean-ZIP rebuilds and physical-testing limits. Previous affected print PDFs and the complete previous source ZIP are separately archived in `archive-before-fresh-review-2026-10-04/` within their print/source folders. Bonus companions are separate; this base ZIP does not incorporate them. The theme remains **unpiloted** and can span several meetings.
