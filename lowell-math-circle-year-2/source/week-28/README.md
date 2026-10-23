# Single-vertex flat folding: Week 28 editable release — current editable source

**Problem files, October 23, 2026.** The student packets are stored as [problem files](../problem-files/README.md): `week.toml`, `figures.py` (the old builder's drawing code and page template, unchanged) and one file per problem in `problems/`, with each band's wording inside it. The conversion changed no wording or figure. The rebuilt LaTeX is byte-identical to the previous builder's (the page header, footer and number come from `page_open` and `page_close` in `figures.py`), and the three print PDFs match in pages, extracted text and 100-dpi pixels. The previous builder (`build_packets.py`) and source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md); its arithmetic checks moved unchanged to `editable/src/student_checks.py`.

**Card fixes, October 23, 2026.** Made in the problem files after the conversion, from the review card's student-page items: K–1 Problem 3 prints four marked disks and two blank ones as extra workspace; grades 2–3 Problems 2 and 3 are swapped, so children try to close the disks before measuring them, with Problem 4 reworded; grades 4–5 Problem 6 has 16 recording strips for its 12 answers; three rule or explanation sentences are cut. The guide and kit follow the new grades 2–3 numbering. Footer ids are now v3. Every page of the three packets and the changed guide and kit pages changed. [editable/review/card-fixes-2026-10-23.md](editable/review/card-fixes-2026-10-23.md) lists what changed, what was deferred and how it was checked. The ZIP from the conversion is in [archive-before-student-page-fixes-2026-10-23/](archive-before-student-page-fixes-2026-10-23/README.md), and the replaced print PDFs are beside the current ones.

- **Student pages:** edit `problems/*.md` (figures in `figures.py`), then build every view:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-28 --out tmp/week-28-views --tex --publish lowell-math-circle-year-2/band-views/week-28
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-28-views lowell-math-circle-year-2/week-28 week-28
  ```

  The first-route and return packets, the one-page problem menu and the key arranged by problem are published in [band-views/week-28/](../../band-views/README.md#weeks-stored-as-problem-files).
- **Adult guide:** its source is still `editable/facilitator-src/build_guide.py (ReportLab)`, built by the package. The problem files' `key` sections repeat its answers for the key view; `python3 lowell-math-circle-year-2/source/week-28/check_guide_copy.py` checks that every key sentence and table row still appears in the guide. Change both together.
- **Portable package:** `editable/` is the package; `editable/src/regenerate.py` writes the student LaTeX from the problem files, and the package build runs it before compiling. The [portable source ZIP](single-vertex-flat-folding-week28-editable-source.zip) holds the package plus the problem files and tools in `problem-files/`, written by `package.py`:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-28 --zip single-vertex-flat-folding-week28-editable-source.zip --top single-vertex-flat-folding-week28-editable-source
  ```

  Rebuild it after any change and check a clean rebuild from the extracted ZIP.

The [portable base source ZIP](single-vertex-flat-folding-week28-editable-source.zip) and [complete extracted package](editable/README.md) contain the current **October 4, 2026 fresh-review revision** with the **October 23, 2026 printable kit** from the review card (`editable/review/card-fixes-2026-10-23.md`): `week-28-materials.pdf`, 15 pages of 18 cm folding disks, wedge sets, K–1 tabs and route cards, digitally checked and physically unrehearsed, and guide pages 1–2 pointing to it. Current print copies are in [../../week-28/](../../week-28/). References are exact duplicates of those print PDFs.

Read `editable/README.md` for dependencies and commands. Copy the complete package to a fresh folder under the project's `tmp/` before rebuilding; keep intermediates out of current print/source folders. `verify_revision.py` checks current pages and permits only specifically audited full-page alternate hashes for pre-existing font/hyphenation differences in unchanged student packets; the original strict verifier remains available. Every changed packet and guide reproduces exact 100-dpi pixels from the extracted ZIP.

The [corpus revision report](../../../plans/fresh-review-revision-2026-10-04/REPORT.md) records per-band decisions, independent mathematical/visual checks, all clean-ZIP rebuilds and physical-testing limits. Previous affected print PDFs and the complete previous source ZIP are separately archived in `archive-before-fresh-review-2026-10-04/` within their print/source folders; the guide and ZIP replaced by the October 23 kit are in `archive-before-card-fixes-2026-10-23/`, the builder replaced by problem files in `archive-before-problem-files-2026-10-23/`, and the PDFs and ZIP replaced by the student-page fixes in `archive-before-student-page-fixes-2026-10-23/`. Bonus companions are separate; this base ZIP does not incorporate them. The theme remains **unpiloted** and can span several meetings.
