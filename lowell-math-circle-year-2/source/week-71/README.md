# Week 71: Can you hear the room? — current editable source

One shared Grades 4–5 packet (5 student pages, GGT71-S-v1) and a 3-page theorem-first adult guide (GGT71-FAC-v1). Unpiloted; mirror handling and print-scale tracing have not been rehearsed. The print PDFs are in [../../week-71/](../../week-71/).

**Problem files, October 23, 2026.** The student packet is stored as [problem files](../problem-files/README.md): `week.toml`, `template.tex` (the old `students.tex` preamble), `figures.py` (which calls the package's window generator, `editable/student/make_diagrams.py`) and one file per problem in `problems/`. The conversion changed no wording or figure: the rebuilt packet matches the print PDF in pages, extracted text and 100-dpi pixels. The hand-written `students.tex`, its `windows.tex` and the previous source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

- **Student pages:** edit `problems/*.md`, then build and compare:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-71 --out tmp/week-71-views --tex
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-71-views lowell-math-circle-year-2/week-71 week-71
  ```

  Week 71 is a shared-packet week, so its one-page menu in [band-views/week-71/](../../band-views/README.md) is built from the page index `../band-views/indexes/week-71.toml` by `band_views.py build`; update the index when a problem moves to another page or the footer changes.
- **Adult guide:** `editable/guide/facilitator.tex`, built by the package. The problem files carry each problem's one-sentence idea (`kernel`), not its answers.
- **Portable package:** `editable/` is the package (`editable/README.md`); `editable/student/regenerate.py` writes `students.tex` from the problem files and the package build runs it first. The [portable source ZIP](../week-71-source.zip) holds the package plus the problem files and tools in `problem-files/`. Rebuild it with

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-71 --zip ../week-71-source.zip --top week-71
  ```

  and check a clean rebuild from the extracted ZIP with `python3 build.py --out output` in its `week-71/` folder. The print copies in `../../week-71/` and `editable/reference-pdfs/` come from that package build.

The review and research record is in [plans/ggt-prototypes-66-75/week-71/](../../../plans/ggt-prototypes-66-75/week-71/) and the review card in [plans/review/week-71.md](../../../plans/review/week-71.md).
