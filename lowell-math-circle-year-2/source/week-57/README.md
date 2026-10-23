# Week 57: Area from dots — current editable source

One shared student packet (10 pages, N57-S-final-v2: Grades 3–5 pages 1–6, Problems 1–6; Grades 4–5 pages 7–10, Problems 7–10) and a 10-page theorem-first adult guide (W57-FAC-v1). Unpiloted; the real-material rehearsal on guide p. 2 is unperformed. The print PDFs are in [../../week-57/](../../week-57/).

**Problem files, October 23, 2026.** The student packet is stored as [problem files](../problem-files/README.md): `week.toml`, `template.tex` (the old `students.tex` preamble), `figures.py` and one file per problem or shared rule in `problems/`, in the flow layout. The figures are TikZ macros drawn from `editable/student/assets/polygons.json` by `editable/student/generate_figures.py`; `figures.py` puts their definitions in the first setup file's figure section, where the old `students.tex` loaded `figures.tex`. Problem 7's file sets the Grades 4--5 header. The conversion changed no wording or figure: the rebuilt packet's page content streams are identical to the old source's build here, and against the print copy, compiled with a newer pdfTeX (1.40.27, against 1.40.25 here), the old and new sources both differ by the same antialiased glyph pixels (at most 78 on a page at 100 dpi); pages and extracted text are identical. The hand-written `students.tex` and the October 4 source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

- **Student pages:** edit `problems/*.md` (and `editable/student/assets/polygons.json` for a figure), then build and compare:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-57 --out tmp/week-57-views --tex
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-57-views lowell-math-circle-year-2/week-57 week-57
  ```

  The build also writes a first-route packet, a one-page problem menu and a key view into `tmp/`; they are not published. Week 57 is a shared-packet week, so its band slices and page menu in [band-views/week-57/](../../band-views/README.md) are built from the page index `../band-views/indexes/week-57.toml` by `band_views.py build`; update the index when a page's header range or problems change.
- **Adult guide:** `editable/guide/facilitator.tex`, built by the package. The problem files carry each problem's one-sentence idea (`kernel`), not its answers.
- **Portable package:** `editable/` is the package (`editable/README.md`); `editable/student/regenerate.py` writes `students.tex` from the problem files and the package `build.py` runs it first. `editable/reference-pdfs/` holds copies of the print PDFs. The [portable source ZIP](../week-57-source.zip) holds the package plus the problem files and tools in `problem-files/`. Rebuild it with

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-57 --zip ../week-57-source.zip --top week-57
  ```

  and check a clean rebuild from the extracted ZIP with `python3 week-57/build.py --out rebuilt`.

The research and review record is in [plans/new-themes-52-63/week-57/](../../../plans/new-themes-52-63/week-57/outline.md) and the review card in [plans/review/week-57.md](../../../plans/review/week-57.md).
