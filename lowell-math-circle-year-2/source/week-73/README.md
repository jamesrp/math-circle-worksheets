# Week 73: The gentlest stretch — current editable source

One shared Grades 4–5 packet (4 student pages, GGT73-S-v2) and a 3-page theorem-first adult guide (GGT73-FAC-v2). Unpiloted; dot placement, strip comparison and midpoint measurement at print scale have not been rehearsed. The print PDFs are in [../../week-73/](../../week-73/).

**Problem files, October 23, 2026.** The student packet is stored as [problem files](../problem-files/README.md): `week.toml`, `template.tex` (the old `students.tex` preamble) and one file per problem in `problems/`. The conversion changed no wording or figure: the rebuilt packet matches the print PDF in pages, extracted text and 100-dpi pixels. The hand-written `students.tex` and the previous source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

**Card fixes, October 23, 2026** (GGT73-S-v2, GGT73-FAC-v2). Made in the problem files after the conversion, from the review card's should-fixes and clear coulds: Problem 5's second target is now 8 by 1, drawn under its 4 by 1 at the same 0.6 in scale, so width decides one target and height the other, and its wording says the partner tests the rule and asks for "a pair that every legal rule stretches at least that much"; the first page 4 arrow is shorter; the inner "right" and "left" labels on pages 1–3 sit nearer their own sheets; page 2 drops the example's caption. The guide's launch adds a doubling strip for "more than twice?", demonstrated on A–D; the Problem 1 key names A–D as Problem 4's lower bound for every legal rule; Problem 3 gains a hint that the centered fan is (x/2, 2y); the Problem 5 key covers 8 by 1; and the guide's sections now run on without a forced page break, keeping 3 pages. The package checks and MATHEMATICS.md use 8 by 1. Could 9 (a Grades 2–3 entry) is left for the organizer. Checked by `plans/review/checks/week-73/check_card_fixes.py`. The replaced PDFs are in [../../week-73/archive-before-card-fixes-2026-10-23/](../../week-73/archive-before-card-fixes-2026-10-23/README.md) and the conversion's ZIP in `../archive-before-card-fixes-2026-10-23/week-73-source.zip` (SHA-256 `29d597dac74ebbfed7df6bb830cdfa4236a460ab47ca98378977a052e4e8f8d9`).

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
