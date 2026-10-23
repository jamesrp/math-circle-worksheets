# Week 68: How many ways out — current editable source

One shared Grades 3–5 packet (4 student pages, GGT68-S-v2) and a 3-page theorem-first adult guide (GGT68-FAC-v2). Unpiloted; placing blockers on the printed dots has not been rehearsed. The print PDFs are in [../../week-68/](../../week-68/).

**Problem files, October 23, 2026.** The student packet is stored as [problem files](../problem-files/README.md): `week.toml`, `template.tex` (the old `students.tex` preamble) and one file per problem in `problems/`. The conversion changed no wording or figure: the generated LaTeX differs from the old `students.tex` only by blank lines between sections, and the rebuilt packet matches the print PDF in pages, extracted text and 100-dpi pixels. The hand-written `students.tex` and the previous source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

**Card shoulds, October 23, 2026** (GGT68-S-v2, GGT68-FAC-v2), made in the problem files after the conversion. Page 1 calls the counters blockers throughout and marks X only on a placement worth keeping; Problem 3 asks how few blocked dots can split the ladder into two forever pieces, with a split on one ladder and a two-dot placement that does not split on the other; Problem 5's right-hand wall is the whole printed X column (seven dots), so P to Q must leave the window (12 steps), and both grids are 12 mm. The guide's Problem 3 key adds the diagonal splits (25 two-dot splits: 9 rungs, 16 diagonals), and it gains a one-minute ray demonstration at the launch, a first route from the line through the ladder to the tree, an adult-led K–1 route on Problems 1 and 7 with a plain-words key, the Problem 5 edge-dot note and the 12-step route. `editable/guide/check_math.py` checks each changed claim and the printed wording. Problem numbers and pages are unchanged; the guide grew to 3 pages. The previous PDFs are in [../../week-68/archive-before-card-fixes-2026-10-23/](../../week-68/archive-before-card-fixes-2026-10-23/) and the conversion's ZIP in [../archive-before-card-fixes-2026-10-23/](../archive-before-card-fixes-2026-10-23/). Unpiloted; the blockers on the 12 mm grids are unrehearsed.

- **Student pages:** edit `problems/*.md`, then build and compare:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-68 --out tmp/week-68-views --tex
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-68-views lowell-math-circle-year-2/week-68 week-68
  ```

  Week 68 is a shared-packet week, so its one-page menu in [band-views/week-68/](../../band-views/README.md) is built from the page index `../band-views/indexes/week-68.toml` by `band_views.py build`; update the index when a problem moves to another page.
- **Adult guide:** `editable/guide/facilitator.tex`, built by the package. The problem files carry each problem's one-sentence idea (`kernel`), not its answers.
- **Portable package:** `editable/` is the package (`editable/README.md`); `editable/student/regenerate.py` writes `students.tex` from the problem files and the package build runs it first. The [portable source ZIP](../week-68-source.zip) holds the package plus the problem files and tools in `problem-files/`. Rebuild it with

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-68 --zip ../week-68-source.zip --top week-68
  ```

  and check a clean rebuild from the extracted ZIP with `python3 build.py --out output` in its `week-68/` folder. The print copies in `../../week-68/` and `editable/reference-pdfs/` come from that package build.

The review and research record is in [plans/ggt-prototypes-66-75/week-68/](../../../plans/ggt-prototypes-66-75/week-68/) and the review card in [plans/review/week-68.md](../../../plans/review/week-68.md).
