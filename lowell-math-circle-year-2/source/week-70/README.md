# Week 70: Four shields in a portal room — current editable source

One shared Grades 4–5 packet (4 student pages, GGT70-S-v1) and a 3-page theorem-first adult guide (GGT70-FAC-v1). Unpiloted; no physical rehearsal has been performed. The print PDFs are in [../../week-70/](../../week-70/).

**Problem files, October 23, 2026.** The student packet is stored as [problem files](../problem-files/README.md): `week.toml`, `template.tex` (the old `students.tex` preamble) and one file per problem in `problems/`. The conversion changed no wording or figure: the generated LaTeX differs from the old `students.tex` only by blank lines between sections, and the rebuilt packet matches the print PDF with identical text and no differing pixels. The hand-written `students.tex` and the previous source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

- **Student pages:** edit `problems/*.md`, then build and compare:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-70 --out tmp/week-70-views --tex
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-70-views lowell-math-circle-year-2/week-70 week-70
  ```

  Week 70 is a shared-packet week, so its one-page menu in [band-views/week-70/](../../band-views/README.md) is built from the page index `../band-views/indexes/week-70.toml` by `band_views.py build`; update the index when a problem moves to another page.
- **Adult guide:** `editable/guide/facilitator.tex`, built by the package. The problem files carry each problem's one-sentence idea (`kernel`), not its answers.
- **Portable package:** `editable/` is the package (`editable/README.md`, which keeps the week's earlier release notes); `editable/student/regenerate.py` writes `students.tex` from the problem files and the package build runs it first. The [portable source ZIP](../week-70-source.zip) holds the package plus the problem files and tools in `problem-files/`. Rebuild it with

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-70 --zip ../week-70-source.zip --top week-70
  ```

  and check a clean rebuild from the extracted ZIP with `python3 build.py --out output` in its `week-70/` folder. `editable/reference-pdfs/` holds copies of the print PDFs.

The review and research record is in [plans/ggt-prototypes-66-75/week-70/](../../../plans/ggt-prototypes-66-75/week-70/) and the review card in [plans/review/week-70.md](../../../plans/review/week-70.md).
