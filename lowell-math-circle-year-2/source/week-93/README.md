# Week 93: Squaring a rectangle — current editable source

One shared student packet (5 pages, W93-S-v2: Grades 3–5 pages 1–4, a Grades 4–5 page 5 for children ready for general reasoning) and a 5-page theorem-first adult guide. Unpiloted; cutting, card fit and timing are unrehearsed. The print PDFs are in [../../week-93/](../../week-93/).

**Problem files, October 23, 2026.** The student packet is stored as [problem files](../problem-files/README.md): `week.toml`, `template.tex` (the old `students.tex` preamble) and one file per problem or shared rule in `problems/`, in the flow layout. The conversion changed no wording or figure: the generated LaTeX differs from the old `students.tex` only by blank lines between sections, and in this container it compiles to a PDF byte-identical to the old source's. Against the print copy, compiled with a newer pdfTeX (1.40.27), the old and new sources both differ by the same antialiased glyph pixels (at most 116 on a page at 100 dpi); pages and extracted text are identical. The hand-written `students.tex` and the previous source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

- **Student pages:** edit `problems/*.md`, then build and compare:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-93 --out tmp/week-93-views --tex
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-93-views lowell-math-circle-year-2/week-93 week-93
  ```

  Week 93 is a shared-packet week, so its Grades 2–3 slice and one-page menu in [band-views/week-93/](../../band-views/README.md) are built from the page index `../band-views/indexes/week-93.toml` by `band_views.py build`; update the index when a problem moves to another page.
- **Adult guide:** `editable/guide/facilitator.tex`, built by the package. The problem files carry each problem's one-sentence idea (`kernel`), not its answers.
- **Portable package:** `editable/` is the package (`editable/README.md`); `editable/student/regenerate.py` writes `students.tex` from the problem files and the package build runs it first, then the mathematical checker. The [portable source ZIP](../week-93-source.zip) holds the package plus the problem files and tools in `problem-files/`. Rebuild it with

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-93 --zip ../week-93-source.zip --top week-93
  ```

  and check a clean rebuild from the extracted ZIP with `python3 week-93/build.py --out rebuilt --work tmp/build`.

The production record is in [plans/new-families-92-97/](../../../plans/new-families-92-97/STATUS.md) and the review card in [plans/review/week-93.md](../../../plans/review/week-93.md).
