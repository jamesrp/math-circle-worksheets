# Week 82: Endless class lines — current editable source

One Grades 3–5 student packet (6 pages, W82-S-v2: Problems 1–4 on pages 1–4, kid cards on page 5, stars and panels on page 6) and a 4-page theorem-first adult guide (W82-FAC-v2). Unpiloted; the cards, yarn and panels have not been handled in a session. The print PDFs are in [../../week-82/](../../week-82/).

**Critic follow-up, October 23, 2026 (W82-FAC-v2).** An independent critic found that the guide's footer carried no version id, so the approved guide, which keys the old "one or two rows" Problem 4, and this one could not be told apart in print; it now reads W82-FAC-v2. Page 1 now says the K–1 route on Problem 1 is on the next page, not "(page 2)", which read as a student page. The page index's `guide_routes` gives the band-view menu and a K–1 slice pages 1 and 5 (Problem 1 and the kid cards). The student packet did not change, and v2 has not been re-approved. The previous guide is in `../../week-82/archive-before-critic-fixes-2026-10-23/` and the previous ZIP in [archive-before-critic-fixes-2026-10-23/](archive-before-critic-fixes-2026-10-23/README.md). Unpiloted.

**Revised after the organizer's approval.** The organizer approved the 6-page packet (W82-Q-draft-v1) on October 17, 2026. The October 23 revision (v2), from the review card's shoulds and coulds, post-dates that approval and has not been re-approved: Problems 1–3 say "complete match", since the opening shows a match that leaves a kid out; Problem 4 asks for two endless rows, so it is no longer answered by Problem 2's lines; Problem 3 drops "There is no last red kid." and Problem 1 "Use cards and yarn to test your matches."; answer lines are 1 cm apart; page 6 has a third "This kid comes after EVERY kid" panel; the footer is W82-S-v2 (no "draft", and S for the old Q). The guide adds a launch demonstration of a rule on a non-task pair, a K–1 route on Problem 1's cards and yarn, Problem 4's key with the six-shape table (including the surprise that a star between two rows joins the second), clearer hint and right-edge wording, and the header "Adult guide". `editable/check_card_fixes.py`, run by the package build, checks each changed key, count and wording. The approved PDFs are archived in [../../week-82/archive-before-card-fixes-2026-10-23/](../../week-82/archive-before-card-fixes-2026-10-23/README.md) and the source ZIP before the fixes in [archive-before-card-fixes-2026-10-23/](archive-before-card-fixes-2026-10-23/README.md); the opening, the class lines of Problems 1–3 and the cards are unchanged.

**Problem files, October 23, 2026.** The student packet is stored as [problem files](../problem-files/README.md): `week.toml`, `template.tex` (the old `students.tex` preamble) and one file per problem or material page in `problems/`, in the flow layout. The conversion, committed alone before the v2 revision, changed no wording or figure: the generated LaTeX differs from the old `students.tex` only by blank lines between sections, and the rebuilt packet matches the old `students.tex` built the same way in pages, extracted text and 100-dpi pixels. Against the print copy, compiled with a newer pdfTeX (1.40.27), the old and new sources both differ by the same glyph pixels on pages 1–4 (at most 116), and the unchanged guide by at most 220. The hand-written `students.tex` and the previous source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

- **Student pages:** edit `problems/*.md`, then build and compare:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-82 --out tmp/week-82-views --tex
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-82-views lowell-math-circle-year-2/week-82 week-82
  ```

  Week 82 is a shared-packet week, so its band slices and one-page menu in [band-views/week-82/](../../band-views/README.md) are built from the page index `../band-views/indexes/week-82.toml` by `band_views.py build`; update the index when a problem moves to another page.
- **Adult guide:** `editable/guide/facilitator.tex`, built by the package. The problem files carry each problem's one-sentence idea (`kernel`), not its answers.
- **Portable package:** `editable/` is the package (`editable/README.md`); `editable/student/regenerate.py` writes `students.tex` from the problem files and the package build runs it first, then the mathematical checker. The [portable source ZIP](../week-82-source.zip) holds the package plus the problem files and tools in `problem-files/`. Rebuild it with

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-82 --zip ../week-82-source.zip --top week-82
  ```

  and check a clean rebuild from the extracted ZIP with `python3 week-82/build.py --out rebuilt --work tmp/build`.

The research and review record is in [plans/infinity-prototypes-79-84/](../../../plans/infinity-prototypes-79-84/README.md) and the review card in [plans/review/week-82.md](../../../plans/review/week-82.md).
