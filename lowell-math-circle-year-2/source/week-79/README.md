# Week 79: Numbered-ball detectives — current editable source

One shared student packet (6 pages, 79-ST-v2: Problems 1–3 for Grades 2–5 on pages 1–2, Problem 4 for Grades 2–5 on page 3, Problem 5 for Grades 4–5 on page 4, a 24-card sheet and an A/B mat) and a 4-page theorem-first adult guide. Unpiloted; the cards and mat have not been handled in a session. The print PDFs are in [../../week-79/](../../week-79/).

**Revised after the organizer's approval.** The organizer approved the 5-page packet (79-ST-v1) on October 15, 2026. The October 23 revision (v2), from the review card's shoulds and coulds, post-dates that approval and has not been re-approved: Problem 2 asks for each card's entry day as well as its move day; a new Problem 4 lets children choose the moves and asks which of three six-card sets B can hold (verified by exhaustive search in `editable/check_math.py`); the old Problem 4 is Problem 5 and says "card" for "label"; the guide adds Problem 5's changed-rule finite-day answer, Problem 4's answers, both rules side by side in Problem 3 (one extra card sheet and mat per table), a K–1 route, a corrected band map, the Ross–Littlewood name and the header "Adult guide". The approved PDFs are archived in [../../week-79/archive-organizer-approved-2026-10-15/](../../week-79/archive-organizer-approved-2026-10-15/README.md); the activity, rule, cards and mat are unchanged.

**Problem files, October 23, 2026.** The student packet is stored as [problem files](../problem-files/README.md): `week.toml`, `template.tex` (the old `students.tex` preamble) and one file per problem, card sheet or mat in `problems/`, in the flow layout. The conversion, committed alone before the v2 revision, changed no wording or figure: the generated LaTeX differs from the old `students.tex` only by blank lines between sections. The rebuilt packet matches the old builder's in pages, extracted text and 100-dpi pixels; against the then-current print copy, compiled with a newer pdfTeX (1.40.27), the old and new builders both differed by the same glyph pixels on pages 1–3 (at most 82). The hand-written `students.tex` and the previous source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

- **Student pages:** edit `problems/*.md`, then build and compare:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-79 --out tmp/week-79-views --tex
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-79-views lowell-math-circle-year-2/week-79 week-79
  ```

  Week 79 is a shared-packet week, so its band slices and one-page menu in [band-views/week-79/](../../band-views/README.md) are built from the page index `../band-views/indexes/week-79.toml` by `band_views.py build`; update the index when a problem moves to another page.
- **Adult guide:** `editable/guide/facilitator.tex`, built by the package. The problem files carry each problem's one-sentence idea (`kernel`), not its answers.
- **Portable package:** `editable/` is the package (`editable/README.md`); `editable/student/regenerate.py` writes `students.tex` from the problem files and the package build runs it first, then the mathematical checker. The [portable source ZIP](../week-79-source.zip) holds the package plus the problem files and tools in `problem-files/`. Rebuild it with

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-79 --zip ../week-79-source.zip --top week-79
  ```

  and check a clean rebuild from the extracted ZIP with `python3 week-79/build.py --out rebuilt --work tmp/build`.

The research and review record is in [plans/infinity-prototypes-79-84/](../../../plans/infinity-prototypes-79-84/README.md) and the review card in [plans/review/week-79.md](../../../plans/review/week-79.md).
