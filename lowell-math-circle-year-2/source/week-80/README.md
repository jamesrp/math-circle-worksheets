# Week 80: Midnight laboratory — current editable source

One shared student packet (6 pages, M80-D-v2: Problems 1–3 for Grades 2–5 on pages 1–3, Problems 4–6 for Grades 4–5 on pages 4–5, and a cut-out page) and a 4-page theorem-first adult guide (M80-FAC-v2). Unpiloted; folding, the counter and the card have not been handled in a session. The print PDFs are in [../../week-80/](../../week-80/).

**Critic follow-up, October 23, 2026 (M80-FAC-v2).** An independent critic found that Problem 3's key accepted "never flip" for the card but gave no ruling on a counter that stops moving, the likeliest child answer, and that the guide's footer carried no version id, so the approved guide (which keys the old numbering) and this one could not be told apart in print. The key now says a counter that stops has settled, like the card that never flips, so it does not answer the question; ask for a rule that keeps the counter moving at every mark but never settles. The footer reads M80-FAC-v2. The page index's `guide_routes` gives the band-view menu and a K–1 slice the K–1 route's pages 1 and 6. The student packet did not change. The previous guide is in `../../week-80/archive-before-critic-fixes-2026-10-23/` and the previous ZIP in [archive-before-critic-fixes-2026-10-23/](archive-before-critic-fixes-2026-10-23/README.md). Unpiloted.

**Revised after the organizer's approval.** The organizer approved the 5-page packet (M80-D-v1) on October 17, 2026. The October 23 revision (v2), from the review card's shoulds and coulds, post-dates that approval and has not been re-approved: a new Grades 2–5 Problem 3 asks for a card rule that settles and a counter rule that does not get closer and closer to one place (the guide's old encore); the old Problems 3–5 are now 4–6; Problem 2 asks "Does the counter get closer and closer to one place?"; Problem 4 drops its last sentence and its MIDNIGHT box now holds the card (80 × 58 mm); Problem 5 begins "The switches before midnight stay the same."; the guide adds Problem 3's key, Problem 4's answer, the "flip once more at midnight" obstacle, a K–1 route on the existing pages, a 15 mm counter, scissors and glue, one counter move in the launch, and the header "Adult guide", and drops its author-facing lines. `editable/check_card_fixes.py`, run by the package build, checks each changed key, size and wording. The approved PDFs are archived in [../../week-80/archive-before-card-fixes-2026-10-23/](../../week-80/archive-before-card-fixes-2026-10-23/README.md) and the source ZIP before the fixes in [archive-before-card-fixes-2026-10-23/](archive-before-card-fixes-2026-10-23/README.md); the story, the fold, the card, the counter and the endpoint questions are unchanged.

**Problem files, October 23, 2026.** The student packet is stored as [problem files](../problem-files/README.md): `week.toml`, `template.tex` (the old `students.tex` preamble) and one file per problem or material page in `problems/`, in the flow layout. The conversion, committed alone before the v2 revision, changed no wording or figure: the generated LaTeX differs from the old `students.tex` only by blank lines between sections, and the rebuilt packet matches the print copy in pages, extracted text and 100-dpi pixels. The hand-written `students.tex` and the previous source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

- **Student pages:** edit `problems/*.md`, then build and compare:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-80 --out tmp/week-80-views --tex
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-80-views lowell-math-circle-year-2/week-80 week-80
  ```

  Week 80 is a shared-packet week, so its band slices and one-page menu in [band-views/week-80/](../../band-views/README.md) are built from the page index `../band-views/indexes/week-80.toml` by `band_views.py build`; update the index when a problem moves to another page.
- **Adult guide:** `editable/guide/facilitator.tex`, built by the package. The problem files carry each problem's one-sentence idea (`kernel`), not its answers.
- **Portable package:** `editable/` is the package (`editable/README.md`); `editable/student/regenerate.py` writes `students.tex` from the problem files and the package build runs it first, then the mathematical checker. The [portable source ZIP](../week-80-source.zip) holds the package plus the problem files and tools in `problem-files/`. Rebuild it with

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-80 --zip ../week-80-source.zip --top week-80
  ```

  and check a clean rebuild from the extracted ZIP with `python3 week-80/build.py --out rebuilt --work tmp/build`.

The research and review record is in [plans/infinity-prototypes-79-84/](../../../plans/infinity-prototypes-79-84/README.md) and the review card in [plans/review/week-80.md](../../../plans/review/week-80.md).
