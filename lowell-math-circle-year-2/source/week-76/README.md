# Week 76: Substitution strips — current editable source

One shared Grades 3–5 packet (4 student pages, F76-35-v1) and a 4-page theorem-first adult guide (F76-FAC-v1). Promoted after organizer review on October 15, 2026. Unpiloted; tile handling has not been rehearsed. The print PDFs are in [../../week-76/](../../week-76/).

**Problem files, October 23, 2026.** The student packet is stored as [problem files](../problem-files/README.md): `week.toml`, `template.tex` (the old `students.tex` preamble) and one file per problem in `problems/`. Each page is still one TikZ canvas: a problem's `text` sections are its drawing code and `\promptat{y}` places its numbered prompt. The conversion changed no wording or figure, and the rebuilt packet matches the print PDF in pages, extracted text and 100-dpi pixels. The hand-written `students.tex` and the previous source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

- **Student pages:** edit `problems/*.md`, then build and compare:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-76 --out tmp/week-76-views --tex
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-76-views lowell-math-circle-year-2/week-76 week-76
  ```

  Week 76 is a shared-packet week, so its one-page menu in [band-views/week-76/](../../band-views/README.md) is built from the page index `../band-views/indexes/week-76.toml` by `band_views.py build`; update the index when a problem moves to another page.
- **Adult guide:** `editable/guide/facilitator.tex`, built by the package. The problem files carry each problem's one-sentence idea (`kernel`), not its answers.
- **Portable package:** `editable/` is the package (`editable/README.md`); `editable/student/regenerate.py` writes `students.tex` from the problem files and the package build runs it first. The [portable source ZIP](../week-76-source.zip) holds the package plus the problem files and tools in `problem-files/`. Rebuild it with

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-76 --zip ../week-76-source.zip --top week-76
  ```

  and check a clean rebuild from the extracted ZIP with `python3 build.py --out output` in its `week-76/` folder. The print copies in `../../week-76/` and `editable/reference-pdfs/` come from that package build.

The review and research record is in [plans/frontier-prototypes-76-78/week-76/](../../../plans/frontier-prototypes-76-78/week-76/) and the review card in [plans/review/week-76.md](../../../plans/review/week-76.md).
