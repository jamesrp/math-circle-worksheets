# Week 55: Few sums and equal spacing — current editable source

One student packet (10 landscape pages, W55-S-v2, all headed Grades 3–5, Problems 1–10) and a 9-page theorem-first adult guide (W55-F-v1). Unpiloted; kit fit, handling and the launch are unrehearsed. The print PDFs are in [../../week-55/](../../week-55/).

**Problem files, October 23, 2026.** The student packet is stored as [problem files](../problem-files/README.md): `week.toml`, `figures.py` (the old `students.tex` preamble as the page template) and one file per problem or shared rule in `problems/`, in the canvas layout. Prompts are placed with `## prompt @y`, and the TikZ drawing code is copied as written. The conversion changed no wording or figure: in this container the rebuilt packet is byte-identical to the old `students.tex` compiled with the same TeX. Against the print copy, compiled with a newer pdfTeX (1.40.27, against 1.40.25 here), the old and new sources both differ by the same antialiased glyph pixels (at most 193 on a page at 100 dpi) and the same `pdftotext -layout` spacing; pages and the words on each page are identical. The hand-written `students.tex` and the October 4 source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

- **Student pages:** edit `problems/*.md`, then build and compare:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-55 --out tmp/week-55-views --tex
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-55-views lowell-math-circle-year-2/week-55 week-55
  ```

  The build also writes a first-route packet, a one-page problem menu and a key view into `tmp/`; they are not published. Week 55 is a shared-packet week, so its page menu in [band-views/week-55/](../../band-views/README.md) is built from the page index `../band-views/indexes/week-55.toml` by `band_views.py build`; update the index when a page's header range or problems change.
- **Adult guide:** `editable/guide/facilitator.tex`, built by the package. The problem files carry each problem's one-sentence idea (`kernel`), not its answers.
- **Portable package:** `editable/` is the package (`editable/README.md`); `editable/student/regenerate.py` writes `students.tex` from the problem files and the package `build.py` runs it first. `editable/reference-pdfs/` holds copies of the print PDFs. The [portable source ZIP](../week-55-source.zip) holds the package plus the problem files and tools in `problem-files/`. Rebuild it with

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-55 --zip ../week-55-source.zip --top week-55
  ```

  and check a clean rebuild from the extracted ZIP with `python3 week-55/build.py --out rebuilt`.

The research and review record is in [plans/new-themes-52-63/week-55/](../../../plans/new-themes-52-63/week-55/outline.md) and the review card in [plans/review/week-55.md](../../../plans/review/week-55.md).
