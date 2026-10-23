# Week 89: Growing shapes and totals — current editable source

One shared Grades K–5 student packet (11 pages, W89-S-v2, Problems 1–20), a 2-page materials packet and an 8-page theorem-first adult guide. Unpiloted; tile fit, copying totals, zero turns, shells and piles are physically unrehearsed. The print PDFs are in [../../week-89/](../../week-89/).

**Problem files, October 23, 2026.** The student packet is stored as [problem files](../problem-files/README.md): `week.toml`, `template.tex` (the old `students.tex` preamble) and one file per problem in `problems/`, in the flow layout. The conversion changed no wording or figure: the generated LaTeX differs from the old `students.tex` only by blank lines between sections, and in this container it compiles to a PDF byte-identical to the old source's. Against the print copy, compiled with a newer pdfTeX, the old and new sources both differ by the same antialiased glyph pixels (at most 153 on a page at 100 dpi); pages and extracted text are identical. The hand-written `students.tex` and the previous source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

- **Student pages:** edit `problems/*.md`, then build and compare:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-89 --out tmp/week-89-views --tex
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-89-views lowell-math-circle-year-2/week-89 week-89
  ```

  Week 89 is a shared-packet week, so its one-page menu in [band-views/week-89/](../../band-views/README.md) is built from the page index `../band-views/indexes/week-89.toml` by `band_views.py build`; update the index when a problem moves to another page.
- **Adult guide and materials:** `editable/guide/facilitator.tex` and `editable/student/materials.tex`, built by the package. The problem files carry each problem's one-sentence idea (`kernel`), not its answers.
- **Portable package:** `editable/` is the package (`editable/README.md`); `editable/student/regenerate.py` writes `students.tex` from the problem files and the package build runs it first. The [portable source ZIP](../week-89-source.zip) holds the package plus the problem files and tools in `problem-files/`. Rebuild it with

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-89 --zip ../week-89-source.zip --top week-89
  ```

  and check a clean rebuild from the extracted ZIP with `python3 week-89/build.py --out rebuilt --work tmp/build`.

The production record is in [plans/seven-families-85-91/](../../../plans/seven-families-85-91/README.md) and the review card in [plans/review/week-89.md](../../../plans/review/week-89.md).
