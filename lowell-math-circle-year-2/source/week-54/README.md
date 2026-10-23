# Week 54: Partitions and rebuilding — current editable source

One shared student packet (9 pages, W54-S-v1: Grades 2–5 pages 1–5, Problems 1–5; Grades 4–5 pages 6–9, Problems 6–9) and an 8-page theorem-first adult guide (W54-FAC-v1). Unpiloted; the cube pretests on guide p. 2 have not been run. The print PDFs are in [../../week-54/](../../week-54/).

**Problem files, October 23, 2026.** The student packet is stored as [problem files](../problem-files/README.md): `week.toml`, `figures.py` (the old `students.tex` preamble as the page template) and one file per problem or shared rule in `problems/`, in the canvas layout. Each page's first text section opens the page with `\beginpage{2--5}` or `\beginpage{4--5}`, which draws that page's header; prompts are placed with `## prompt @y`, and the TikZ drawing code is copied as written. The conversion changed no wording or figure: the rebuilt packet's page content streams are identical to the old `students.tex` compiled with the same TeX, and against the print copy, compiled with a newer pdfTeX (1.40.27, against 1.40.25 here), the old and new sources both differ by the same antialiased glyph pixels (at most 113 on a page at 100 dpi); pages and extracted text are identical. The hand-written `students.tex` and the October 4 source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

- **Student pages:** edit `problems/*.md`, then build and compare:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-54 --out tmp/week-54-views --tex
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-54-views lowell-math-circle-year-2/week-54 week-54
  ```

  The build also writes a first-route packet, a one-page problem menu and a key view into `tmp/`; they are not published. Week 54 is a shared-packet week, so its band slices and page menu in [band-views/week-54/](../../band-views/README.md) are built from the page index `../band-views/indexes/week-54.toml` by `band_views.py build`; update the index when a page's header range or problems change.
- **Adult guide:** `editable/guide/facilitator.tex`, built by the package. The problem files carry each problem's one-sentence idea (`kernel`), not its answers.
- **Portable package:** `editable/` is the package (`editable/README.md`); `editable/student/regenerate.py` writes `students.tex` from the problem files and the package `build.py` runs it first. `editable/reference-pdfs/` holds copies of the print PDFs. The [portable source ZIP](../week-54-source.zip) holds the package plus the problem files and tools in `problem-files/`. Rebuild it with

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-54 --zip ../week-54-source.zip --top week-54
  ```

  and check a clean rebuild from the extracted ZIP with `python3 week-54/build.py --out rebuilt`.

The research and review record is in [plans/new-themes-52-63/week-54/](../../../plans/new-themes-52-63/week-54/outline.md) and the review card in [plans/review/week-54.md](../../../plans/review/week-54.md).
