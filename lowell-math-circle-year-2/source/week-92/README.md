# Week 92: Fold-and-stretch predictions — current editable source

One shared student packet (7 pages, W92-S-v2: Grades 2–3 pages 1–3, Grades 4–5 pages 4–7) and a 5-page theorem-first adult guide. Unpiloted; physical rehearsal untested. The print PDFs are in [../../week-92/](../../week-92/).

**Problem files, October 23, 2026.** The student packet is stored as [problem files](../problem-files/README.md): `week.toml`, `figures.py` (the old `students.tex` preamble and drawing macros, as its page template) and one file per problem or shared rule in `problems/`, in the canvas layout: each page is one TikZ picture, each prompt and text sits at the height its heading gives, and each figure is the old TikZ code verbatim. `band(...)` at the top of a page sets the grade range its header prints. The conversion changed no wording or figure: the rebuilt packet is byte-identical to the old source's build in this container. Against the print copy, compiled with a newer pdfTeX (1.40.27), the old and new sources both differ by the same antialiased glyph pixels (at most 76 on a page at 100 dpi); pages and extracted text are identical. The hand-written `students.tex` and the previous source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

- **Student pages:** edit `problems/*.md`, then build and compare:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-92 --out tmp/week-92-views --tex
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-92-views lowell-math-circle-year-2/week-92 week-92
  ```

  Week 92 is a shared-packet week, so its band slices and one-page menu in [band-views/week-92/](../../band-views/README.md) are built from the page index `../band-views/indexes/week-92.toml` by `band_views.py build`; update the index when a problem moves to another page or a page's grade range changes.
- **Adult guide:** `editable/guide/facilitator.tex`, built by the package. The problem files carry each problem's one-sentence idea (`kernel`), not its answers.
- **Portable package:** `editable/` is the package (`editable/README.md`); `editable/student/regenerate.py` writes `students.tex` from the problem files and the package build runs it first, then the mathematical checker. The [portable source ZIP](../week-92-source.zip) holds the package plus the problem files and tools in `problem-files/`. Rebuild it with

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-92 --zip ../week-92-source.zip --top week-92
  ```

  and check a clean rebuild from the extracted ZIP with `python3 week-92/build.py --out rebuilt --work tmp/build`.

The production record is in [plans/new-families-92-97/](../../../plans/new-families-92-97/STATUS.md) and the review card in [plans/review/week-92.md](../../../plans/review/week-92.md).
