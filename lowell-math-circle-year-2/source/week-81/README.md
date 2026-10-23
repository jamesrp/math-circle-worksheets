# Week 81: Buckets of Fish — current editable source

One shared student packet (5 pages, W81-S-v2: Problems 1–3 for Grades 2–5 on pages 1–4, with the board on page 2 and the sorting cards on page 3; Problems 4–5 for Grades 4–5 on page 5) and a 4-page theorem-first adult guide. Unpiloted; the board, counters and cards have not been handled in a session. The print PDFs are in [../../week-81/](../../week-81/).

**Revised after the organizer's approval.** The organizer approved the 5-page packet (W81-S-draft-v1) on October 17, 2026. The October 23 revision (v2), from the review card's shoulds and coulds, post-dates that approval and has not been re-approved: Problem 5 now starts from two pictures, the two-bucket (0, 3) beside (1, 1, 1), and asks "If you think every game ends, however big the refills, explain why."; Problem 3's first start is (2, 0, 2) instead of Problem 1's (2, 2, 2); page 1's cap reads "add at most one counter to each bucket to the left of the one you took from"; the footer drops "draft". The guide corrects the repair move ("add 1 to each earlier odd bucket (0 to each earlier even one)"), gives a Grades 4–5 route (Problem 1 and some Problem 2 cards, then Problems 4–5, Problem 3 for a pair that finishes), adds a K–1 route on the nine small Problem 2 cards, shows the one-per-bucket cap in the launch, replaces the stale "count card" wording, keys (0, 3) and (2, 0, 2), adds a capped longest-game return visit, and is headed "Adult guide". `editable/check_card_fixes.py`, run by the package build, checks each changed key, start and wording. The approved PDFs are archived in [../../week-81/archive-before-card-fixes-2026-10-23/](../../week-81/archive-before-card-fixes-2026-10-23/README.md) and the source ZIP before the fixes in [archive-before-card-fixes-2026-10-23/](archive-before-card-fixes-2026-10-23/README.md); the game, its rules, the board and the sixteen cards are unchanged.

**Problem files, October 23, 2026.** The student packet is stored as [problem files](../problem-files/README.md): `week.toml`, `template.tex` (the old `students.tex` preamble) and one file per problem or material page in `problems/`, in the flow layout. The conversion, committed alone before the v2 revision, changed no wording or figure: the generated LaTeX differs from the old `students.tex` only by blank lines between sections, and the rebuilt packet matches the print copy in pages, extracted text and 100-dpi pixels. The hand-written `students.tex` and the previous source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

- **Student pages:** edit `problems/*.md`, then build and compare:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-81 --out tmp/week-81-views --tex
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-81-views lowell-math-circle-year-2/week-81 week-81
  ```

  Week 81 is a shared-packet week, so its band slices and one-page menu in [band-views/week-81/](../../band-views/README.md) are built from the page index `../band-views/indexes/week-81.toml` by `band_views.py build`; update the index when a problem moves to another page.
- **Adult guide:** `editable/guide/facilitator.tex`, built by the package. The problem files carry each problem's one-sentence idea (`kernel`), not its answers.
- **Portable package:** `editable/` is the package (`editable/README.md`); `editable/student/regenerate.py` writes `students.tex` from the problem files and the package build runs it first, then the mathematical checker. The [portable source ZIP](../week-81-source.zip) holds the package plus the problem files and tools in `problem-files/`. Rebuild it with

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-81 --zip ../week-81-source.zip --top week-81
  ```

  and check a clean rebuild from the extracted ZIP with `python3 week-81/build.py --out rebuilt --work tmp/build`.

The research and review record is in [plans/infinity-prototypes-79-84/](../../../plans/infinity-prototypes-79-84/README.md) and the review card in [plans/review/week-81.md](../../../plans/review/week-81.md).
