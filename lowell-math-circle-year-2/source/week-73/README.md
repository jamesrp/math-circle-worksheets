# Week 73: The gentlest stretch — current editable source

One shared Grades 4–5 packet (4 student pages, GGT73-S-v1) and a 3-page theorem-first adult guide (GGT73-FAC-v1). Unpiloted; dot placement, strip comparison and midpoint measurement at print scale have not been rehearsed. The print PDFs are in [../../week-73/](../../week-73/).

**Problem files, October 23, 2026.** The student packet is stored as [problem files](../problem-files/README.md): `week.toml`, `template.tex` (the old `students.tex` preamble) and one file per problem in `problems/`. The conversion changed no wording or figure: the rebuilt packet matches the print PDF in pages, extracted text and 100-dpi pixels. The hand-written `students.tex` and the previous source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

- **Student pages:** edit `problems/*.md`, then build and compare:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-73 --out tmp/week-73-views --tex
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-73-views lowell-math-circle-year-2/week-73 week-73
  ```

  Week 73 is a shared-packet week, so its one-page menu in [band-views/week-73/](../../band-views/README.md) is built from the page index `../band-views/indexes/week-73.toml` by `band_views.py build`; update the index when a problem moves to another page or the footer changes.
- **Adult guide:** `editable/guide/facilitator.tex`, built by the package. The problem files carry each problem's one-sentence idea (`kernel`), not its answers.
- **Portable package:** `editable/` is the package (`editable/README.md`); `editable/student/regenerate.py` writes `students.tex` from the problem files and the package build runs it first. The [portable source ZIP](../week-73-source.zip) holds the package plus the problem files and tools in `problem-files/`. Rebuild it with

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-73 --zip ../week-73-source.zip --top week-73
  ```

  and check a clean rebuild from the extracted ZIP with `python3 build.py --out output` in its `week-73/` folder. The print copies in `../../week-73/` and `editable/reference-pdfs/` come from that package build.

The review and research record is in [plans/ggt-prototypes-66-75/week-73/](../../../plans/ggt-prototypes-66-75/week-73/) and the review card in [plans/review/week-73.md](../../../plans/review/week-73.md).
