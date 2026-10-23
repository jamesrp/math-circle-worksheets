# Week 52: Hinged frames and braces — current editable source

One shared student packet (12 pages, F52-S-v2: pages headed K–1, Grades 2–3, Grades 3–5 and Grades 4–5) and a 10-page theorem-first adult guide (F52-FAC-v2). Unpiloted; the bar-and-pin kits have not been built or handled in a session. The print PDFs are in [../../week-52/](../../week-52/).

**Problem files, October 23, 2026.** The student packet is stored as [problem files](../problem-files/README.md): `week.toml`, `template.tex` (the old `students.tex` preamble) and one file per problem in `problems/`, in the flow layout. Each page's first file opens with the `\band{...}` line that names that page's grade range. The conversion changed no wording or figure: the generated LaTeX differs from the old `students.tex` only by blank lines between sections. The rebuilt packet matches the old source's build in pages, extracted text and 100-dpi pixels; the print copy, compiled with TeX Live 2025 (pdfTeX 1.40.27), differs from both builds by the same few glyph pixels (at most 166 on a page at 100 dpi). The hand-written `students.tex` and the October 4 ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

- **Student pages:** edit `problems/*.md`, then build and compare:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-52 --out tmp/week-52-views --tex
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-52-views lowell-math-circle-year-2/week-52 week-52
  ```

  Week 52 is a shared-packet week, so its band slices and one-page menu in [band-views/week-52/](../../band-views/README.md) are built from the page index `../band-views/indexes/week-52.toml` by `band_views.py build`; update the index when a page's grade range or problems change.
- **Adult guide:** `editable/guide/facilitator.tex`, built by the package. The problem files carry each problem's one-sentence idea (`kernel`), not its answers.
- **Portable package:** `editable/` is the package (`editable/README.md`); `editable/student/regenerate.py` writes `students.tex` from the problem files and the package build runs it first. The [portable source ZIP](../week-52-source.zip) holds the package plus the problem files and tools in `problem-files/`. Rebuild it with

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-52 --zip ../week-52-source.zip --top week-52
  ```

  and check a clean rebuild from the extracted ZIP with `python3 week-52/build.py --out rebuilt`.

The research and review record is in [plans/new-themes-52-63/week-52/](../../../plans/new-themes-52-63/week-52/) and the review card in [plans/review/week-52.md](../../../plans/review/week-52.md).
