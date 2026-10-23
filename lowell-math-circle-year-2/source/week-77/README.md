# Week 77: Persistent holes — current editable source

One shared Grades 4–5 packet (6 student pages, F77-45-v2) and a 4-page theorem-first adult guide (F77-FAC-v2). A prototype awaiting organizer review; unpiloted, and tile, token and edge-strip handling has not been rehearsed. The print PDFs are in [../../week-77/](../../week-77/). The October 15 revision added the introductory page (`editable/README.md`).

**Problem files, October 23, 2026.** The student packet is stored as [problem files](../problem-files/README.md): `week.toml`, `template.tex` (the old `students.tex` preamble) and one file per problem in `problems/`. Each page is still one TikZ canvas: a problem's `text` sections are its drawing code and `\promptat{y}` places its numbered prompt. The conversion changed no wording or figure, and the rebuilt packet matches the print PDF in pages, extracted text and 100-dpi pixels. The hand-written `students.tex` and the previous source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

- **Student pages:** edit `problems/*.md`, then build and compare:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-77 --out tmp/week-77-views --tex
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-77-views lowell-math-circle-year-2/week-77 week-77
  ```

  Week 77 is a shared-packet week, so its one-page menu in [band-views/week-77/](../../band-views/README.md) is built from the page index `../band-views/indexes/week-77.toml` by `band_views.py build`; update the index when a problem moves to another page. The package's `checks/independent_check.py` also reads the regenerated `students.tex` and asserts its task wording and diagram coordinates, so change it with any student-page change.
- **Adult guide:** `editable/guide/facilitator.tex`, built by the package. The problem files carry each problem's one-sentence idea (`kernel`), not its answers.
- **Portable package:** `editable/` is the package (`editable/README.md`); `editable/student/regenerate.py` writes `students.tex` from the problem files and the package build runs it first. The [portable source ZIP](../week-77-source.zip) holds the package plus the problem files and tools in `problem-files/`. Rebuild it with

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-77 --zip ../week-77-source.zip --top week-77
  ```

  and check a clean rebuild from the extracted ZIP with `python3 build.py --out output` in its `week-77/` folder. The print copies in `../../week-77/` and `editable/reference-pdfs/` come from that package build.

The review and research record is in [plans/frontier-prototypes-76-78/week-77/](../../../plans/frontier-prototypes-76-78/week-77/) and the review card in [plans/review/week-77.md](../../../plans/review/week-77.md).
