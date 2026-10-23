# Week 69: Thin and fat road triangles — current editable source

One shared Grades 4–5 packet (4 student pages, GGT69-S-v2) and a 2-page theorem-first adult guide (GGT69-FAC-v2). Unpiloted; no physical rehearsal has been performed. The print PDFs are in [../../week-69/](../../week-69/).

**Problem files, October 23, 2026.** The student packet is stored as [problem files](../problem-files/README.md): `week.toml`, `template.tex` (the old `students.tex` preamble) and one file per problem in `problems/`. The conversion changed no wording or figure: the generated LaTeX differs from the old `students.tex` only by blank lines between sections, and rebuilt here the two give pixel-identical packets (the October 16 print PDF, made with another TeX installation, differs from both by at most 123 pixels a page with identical text). The hand-written `students.tex` and the previous source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

- **Student pages:** edit `problems/*.md`, then build and compare:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-69 --out tmp/week-69-views --tex
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-69-views lowell-math-circle-year-2/week-69 week-69
  ```

  Week 69 is a shared-packet week, so its one-page menu in [band-views/week-69/](../../band-views/README.md) is built from the page index `../band-views/indexes/week-69.toml` by `band_views.py build`; update the index when a problem moves to another page.
- **Adult guide:** `editable/guide/facilitator.tex`, built by the package. The problem files carry each problem's one-sentence idea (`kernel`), not its answers.
- **Portable package:** `editable/` is the package (`editable/README.md`, which keeps the week's earlier release notes); `editable/student/regenerate.py` writes `students.tex` from the problem files and the package build runs it first. The [portable source ZIP](../week-69-source.zip) holds the package plus the problem files and tools in `problem-files/`. Rebuild it with

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-69 --zip ../week-69-source.zip --top week-69
  ```

  and check a clean rebuild from the extracted ZIP with `python3 build.py --out output` in its `week-69/` folder. `editable/reference-pdfs/` holds copies of the print PDFs.

The review and research record is in [plans/ggt-prototypes-66-75/week-69/](../../../plans/ggt-prototypes-66-75/week-69/) and the review card in [plans/review/week-69.md](../../../plans/review/week-69.md).
