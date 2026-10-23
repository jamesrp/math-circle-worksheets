# Week 60: Take it or pass — current editable source

One shared student packet (7 pages, W60-S-v2: Grades 3–5 pages 1–3 and 6, Grades 4–5 pages 4, 5 and 7) and an 8-page theorem-first adult guide (W60-FAC-v1). Unpiloted; drawing, mixing, counters and card scoring are physically unrehearsed. The print PDFs are in [../../week-60/](../../week-60/).

**Problem files, October 23, 2026.** The student packet is stored as [problem files](../problem-files/README.md): `week.toml`, `template.tex` (the head of the old `students.tex`, with its card and position macros) and one file per problem in `problems/`, in the flow layout. This is a shared-packet week: `week.toml` defines one band, `shared`, whose packet is `week-60-students.pdf`, and each page's header range is set by `\renewcommand{\band}` in the text that opens the page. The conversion changed no wording or figure: the generated LaTeX differs from the old `students.tex` only by blank lines between sections, and the rebuilt packet matches the old builder's in pages, extracted text and 100-dpi pixels. Against the print copy, compiled with a newer pdfTeX (1.40.27), the old and new builders both differ the same way: small glyph differences, and shorter rows in Problem 1's rounds table, whose `\arraystretch` the newer TeX Live applies differently. The hand-written `students.tex` and the October 4 source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

- **Student pages:** edit `problems/*.md`, then build and compare:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-60 --out tmp/week-60-views --tex
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-60-views lowell-math-circle-year-2/week-60 week-60
  ```

  The build also writes a first-route and a return packet, a one-page problem menu and a key view into `tmp/`; they are not published. The published views of this week are its band slices and page menu in [band-views/week-60/](../../band-views/README.md), built from the page index `../band-views/indexes/week-60.toml` by `band_views.py build`; update the index when a page's header range or problems change.
- **Adult guide:** `editable/guide/facilitator.tex`, built by the package.
- **Portable package:** `editable/` is the package (`editable/README.md`); `editable/student/regenerate.py` writes `students.tex` from the problem files, and the package `build.py` runs it before compiling. `editable/reference-pdfs/` holds copies of the print PDFs. The [portable source ZIP](../week-60-source.zip) holds the package plus the problem files and tools in `problem-files/`. Rebuild it with

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-60 --zip ../week-60-source.zip --top week-60
  ```

  and check a clean rebuild from the extracted ZIP with `python3 week-60/build.py --out rebuilt`.

The research and review record is in [plans/new-themes-52-63/week-60/](../../../plans/new-themes-52-63/week-60/outline.md) and the review card in [plans/review/week-60.md](../../../plans/review/week-60.md).
