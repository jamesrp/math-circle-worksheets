# Week 37 Mirror twins editable source — current editable source

**Problem files, October 23, 2026.** The student packets are stored as [problem files](../problem-files/README.md): `week.toml`, `figures.py` (the old builder's drawing code and page template, unchanged) and one file per problem in `problems/`, with each band's wording inside it. The conversion changed no wording or figure. The rebuilt LaTeX is byte-identical to the previous builder's (the page header, footer and number come from `page_open` and `page_close` in `figures.py`), and the three print PDFs match in pages, extracted text and 100-dpi pixels. The previous builder (`build_packets.py`) and source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md); its arithmetic checks moved unchanged to `editable/src/student_checks.py`.

**Card fixes, October 23, 2026.** Made in the problem files after the conversion, from the review card's student-page items: grades 2–3 Problem 3 now asks which model of the Problem 2 pair a newly labelled model matches and whether one can match neither; grades 4–5 Problems 1, 2 and 6 and grades 2–3 Problem 4 are tightened; the pages say "model" instead of "frame". No problem is renumbered. The guide keys follow, and footer ids are now v3. Every page of the three packets and guide pages 1–5 changed. [editable/review/card-fixes-2026-10-23.md](editable/review/card-fixes-2026-10-23.md) lists what changed, what was deferred and how it was checked. The ZIP from the conversion is in [archive-before-student-page-fixes-2026-10-23/](archive-before-student-page-fixes-2026-10-23/README.md), and the replaced print PDFs are beside the current ones. Later the same day the guide's route update (p. 6) said how the grades 2–3 pairs share the table's four models in Problem 3, with a pointer on p. 2; no other page changed.

- **Student pages:** edit `problems/*.md` (figures in `figures.py`), then build every view:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-37 --out tmp/week-37-views --tex --publish lowell-math-circle-year-2/band-views/week-37
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-37-views lowell-math-circle-year-2/week-37 week-37
  ```

  The first-route and return packets, the one-page problem menu and the key arranged by problem are published in [band-views/week-37/](../../band-views/README.md#weeks-stored-as-problem-files).
- **Adult guide:** its source is still `editable/facilitator-src/guide.md`, built by the package. The problem files' `key` sections repeat its answers for the key view; `python3 lowell-math-circle-year-2/source/week-37/check_guide_copy.py` checks that every key sentence and table row still appears in the guide. Change both together.
- **Portable package:** `editable/` is the package; `editable/src/regenerate.py` writes the student LaTeX from the problem files, and the package build runs it before compiling. The [portable source ZIP](mirror-twins-week37-editable-source.zip) holds the package plus the problem files and tools in `problem-files/`, written by `package.py`:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-37 --zip mirror-twins-week37-editable-source.zip --top mirror-twins-week37-source
  ```

  Rebuild it after any change and check a clean rebuild from the extracted ZIP.

The [portable base source ZIP](mirror-twins-week37-editable-source.zip) and [complete extracted package](editable/README.md) contain the current **October 4, 2026 fresh-review revision** with the **October 23, 2026 guide corrections and printable kit** from the review card (`editable/review/card-fixes-2026-10-23.md`): the guide accepts a complete check of the three turns about A as a proof, and `week-37-materials.pdf` gives a 90 mm card tetrahedron net, letter caps and a pose mat, digitally checked and physically unrehearsed. Current print copies are in [../../week-37/](../../week-37/). References are exact duplicates of those print PDFs.

Read `editable/README.md` for dependencies and commands. Copy the complete package to a fresh folder under the project's `tmp/` before rebuilding; keep intermediates out of current print/source folders. `verify_revision.py` checks current pages and permits only specifically audited full-page alternate hashes for pre-existing font/hyphenation differences in unchanged student packets; the original strict verifier remains available. Every changed packet and guide reproduces exact 100-dpi pixels from the extracted ZIP.

The [corpus revision report](../../../plans/fresh-review-revision-2026-10-04/REPORT.md) records per-band decisions, independent mathematical/visual checks, all clean-ZIP rebuilds and physical-testing limits. Previous affected print PDFs and the complete previous source ZIP are separately archived in `archive-before-fresh-review-2026-10-04/` within their print/source folders; the guide and ZIP replaced by the October 23 kit are in `archive-before-card-fixes-2026-10-23/`, the builder replaced by problem files in `archive-before-problem-files-2026-10-23/`, and the PDFs and ZIP replaced by the student-page fixes in `archive-before-student-page-fixes-2026-10-23/`. Bonus companions are separate; this base ZIP does not incorporate them. The theme remains **unpiloted** and can span several meetings.
