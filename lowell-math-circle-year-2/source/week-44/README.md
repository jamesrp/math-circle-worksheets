# Week 44 The bag that copies editable source — current editable source

**Problem files, October 23, 2026.** The student packets are stored as [problem files](../problem-files/README.md): `week.toml`, `figures.py` (the old builder's drawing code and page template, unchanged) and one file per problem in `problems/`, with each band's wording inside it. The conversion changed no wording or figure: the rebuilt LaTeX is byte-identical to the previous builder's, and all three packets match that builder's output in this TeX runtime in exact 100-dpi pixels. (Grades 4–5 page 1 of the October 4 print copy breaks one line differently in this runtime, a pre-existing difference that the October 4 ZIP's own `verify_revision.py` also reports here.) The previous builder (`write.py`) and the October 4 source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md). The bonus companion (`../week-44-bonus/`) is not converted.

- **Student pages:** edit `problems/*.md` (figures in `figures.py`), then build every view:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-44 --out tmp/week-44-views --tex --publish lowell-math-circle-year-2/band-views/week-44
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-44-views lowell-math-circle-year-2/week-44 week-44
  ```

  The first-route and return packets, the one-page problem menu and the key arranged by problem are published in [band-views/week-44/](../../band-views/README.md#weeks-stored-as-problem-files). The routes are read from the guide's route update: K–1 first P1–2, Grades 2–3 first P1–2, Grades 4–5 first P1–3.
- **Adult guide:** its source is still `editable/facilitator-src/guide.json` with `route-note.json`, built by the package. The problem files' `key` sections repeat its answer keys for the key view; `python3 lowell-math-circle-year-2/source/week-44/check_guide_copy.py` checks that every key sentence is still in the guide source. Change both together.
- **Portable package:** `editable/` is the package; `editable/src/regenerate.py` writes the student LaTeX from the problem files, and the package build runs it before compiling. The [portable source ZIP](copying-bag-week44-editable-source.zip) holds the package plus the problem files and tools in `problem-files/`, written by `package.py` (see the problem-files README).

The [portable base source ZIP](copying-bag-week44-editable-source.zip) and [complete extracted package](editable/README.md) contain the current **October 4, 2026 fresh-review revision**, with the problem files. Current print copies are in [../../week-44/](../../week-44/). References are exact duplicates of those print PDFs.

Read `editable/README.md` for dependencies and commands. Copy the complete package to a fresh folder under the project's `tmp/` before rebuilding; keep intermediates out of current print/source folders. `verify_revision.py` checks current pages and permits only specifically audited full-page alternate hashes for pre-existing font/hyphenation differences in unchanged student packets; the original strict verifier remains available. Every changed packet and guide reproduces exact 100-dpi pixels from the extracted ZIP.

The [corpus revision report](../../../plans/fresh-review-revision-2026-10-04/REPORT.md) records per-band decisions, independent mathematical/visual checks, all clean-ZIP rebuilds and physical-testing limits. Previous affected print PDFs and the complete previous source ZIP are separately archived in `archive-before-fresh-review-2026-10-04/` within their print/source folders. Bonus companions are separate; this base ZIP does not incorporate them. The theme remains **unpiloted** and can span several meetings.
