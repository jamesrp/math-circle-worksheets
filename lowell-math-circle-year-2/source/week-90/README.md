# Week 90: Sliding number arrays — current editable source

One shared Grades 2–5 student packet (8 pages, W90-students-v1, Problems 1–9), an 11-page materials packet and a 9-page theorem-first adult guide. Unpiloted; handling, masks, resets and timing are physically unrehearsed. The print PDFs are in [../../week-90/](../../week-90/).

**Problem files, October 23, 2026.** The student packet is stored as [problem files](../problem-files/README.md): `week.toml`, `template.tex` (the old `students.tex` preamble, with each page's header, rule and footer as the macros `\pageopen` and `\pageclose`) and one file per problem in `problems/`, in the flow layout; each page is one TikZ overlay, and a problem's `text` sections are its page's drawing code, as in Week 98. The conversion changed no wording or figure: in this container the generated LaTeX compiles to a PDF byte-identical to the old source's. Against the print copy, compiled with a newer pdfTeX, the old and new sources both differ by the same antialiased glyph pixels (at most 61 on a page at 100 dpi); pages and extracted text are identical. The hand-written `students.tex` and the previous source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

**Card fixes, October 23, 2026.** Made in the problem files after the conversion: page 1's teaser line is gone, Problem 2 ends "Explain how you know.", Problem 5's follow-up asks whether a start could be missing from the sixteen cards, Problem 6 refers to the finished B arrangements from Problem 5 and its targets are drawn alike, and two repeated sentences on pages 3 and 7 are cut. The guide has a K–1 route, what children are meant to discover, the upper trio's same-visit continuation, the pooled B record, the exit-only undo and the D table's reading direction. Student pages 1–3 and 5–7 and guide pages 1–4, 6 and 7 changed; the materials packet did not. [editable/review/card-fixes-2026-10-23.md](editable/review/card-fixes-2026-10-23.md) lists what changed and how it was checked. The ZIP from the conversion is in [archive-before-card-fixes-2026-10-23/](archive-before-card-fixes-2026-10-23/README.md), and the replaced print PDFs are beside the current ones.

- **Student pages:** edit `problems/*.md`, then build and compare:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-90 --out tmp/week-90-views --tex
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-90-views lowell-math-circle-year-2/week-90 week-90
  ```

  Week 90 is a shared-packet week, so its one-page menu in [band-views/week-90/](../../band-views/README.md) is built from the page index `../band-views/indexes/week-90.toml` by `band_views.py build`; update the index when a problem moves to another page.
- **Adult guide and materials:** `editable/guide/facilitator.tex` and `editable/student/materials.tex`, built by the package. The problem files carry each problem's one-sentence idea (`kernel`), not its answers.
- **Portable package:** `editable/` is the package (`editable/README.md`); `editable/student/regenerate.py` writes `students.tex` from the problem files and the package build runs it first. The [portable source ZIP](../week-90-source.zip) holds the package plus the problem files and tools in `problem-files/`. Rebuild it with

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-90 --zip ../week-90-source.zip --top week-90
  ```

  and check a clean rebuild from the extracted ZIP with `python3 week-90/build.py --out rebuilt --work tmp/build`.

The production record is in [plans/seven-families-85-91/](../../../plans/seven-families-85-91/README.md) and the review card in [plans/review/week-90.md](../../../plans/review/week-90.md).
