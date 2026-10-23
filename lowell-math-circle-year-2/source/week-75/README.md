# Week 75: Twists on a cylinder — current editable source

One shared Grades 4–5 packet (4 student pages, GGT75-S-v4) and a 3-page theorem-first adult guide (GGT75-FAC-v4). Unpiloted; the tape, yarn and paper sleeve have not been rehearsed. The print PDFs are in [../../week-75/](../../week-75/).

**Problem files, October 23, 2026.** The student packet is stored as [problem files](../problem-files/README.md): `week.toml`, `template.tex` (the old `students.tex` preamble) and one file per problem in `problems/`. The conversion changed no wording or figure: the generated LaTeX differs from the old `students.tex` only by blank lines between sections, and the rebuilt packet matches the print PDF in pages, extracted text and 100-dpi pixels. The hand-written `students.tex` and the previous source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

**Card fixes, October 23, 2026.** Made in the problem files after the conversion: Problems 6–7 say "strand crossings" (places where the two strands cross each other), and page 3 has a shrunk twist example and, under Problem 4, a strip with B copies −4 to 4 and quarter-height dotted lines for the twisted routes (the review card's two musts); Problem 6's rows are 0.8 in tall under a "Sketch" heading. Problem numbers and pages are unchanged; the guide matches (GGT75-S-v2, GGT75-FAC-v2). [editable/review/card-fixes-2026-10-23.md](editable/review/card-fixes-2026-10-23.md) lists what changed, what was deferred and how it was checked. The replaced print PDFs are in [../../week-75/archive-before-card-fixes-2026-10-23/](../../week-75/archive-before-card-fixes-2026-10-23/) and the conversion's ZIP in [../archive-before-card-fixes-2026-10-23/](../archive-before-card-fixes-2026-10-23/).

**Shoulds 4–7, later on October 23, 2026** (GGT75-S-v3, GGT75-FAC-v3). Page 1's rules leave taping and feeding to the launch, Problem 1 has two sketch boxes for its same-winding routes, Problem 2's partner lays each route with yarn, and Problem 3 ends "Explain the difference." Pages 3–4 changed only in the footer; the guide's launch now shows the taping. Version 2's PDFs and ZIP are in the two `archive-before-shoulds-2026-10-23/` folders.

**Minus signs, later on October 23, 2026** (GGT75-S-v4, GGT75-FAC-v4). After an independent critic's review, page 2's lift boards label the left dot "B, copy −1" with a true minus (from `\liftboard` in `template.tex`), as page 3's strip already did. The other pages changed only in the footer, and the guide only in its footer and review-status line; `editable/review/verify_minus_signs_2026_10_23.py` checks this against version 3, whose PDFs and ZIP are in the two `archive-before-minus-signs-2026-10-23/` folders.

- **Student pages:** edit `problems/*.md`, then build and compare:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-75 --out tmp/week-75-views --tex
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-75-views lowell-math-circle-year-2/week-75 week-75
  ```

  Week 75 is a shared-packet week, so its one-page menu in [band-views/week-75/](../../band-views/README.md) is built from the page index `../band-views/indexes/week-75.toml` by `band_views.py build`; update the index when a problem moves to another page.
- **Adult guide:** `editable/guide/facilitator.tex`, built by the package. The problem files carry each problem's one-sentence idea (`kernel`), not its answers.
- **Portable package:** `editable/` is the package (`editable/README.md`); `editable/student/regenerate.py` writes `students.tex` from the problem files and the package build runs it first. The [portable source ZIP](../week-75-source.zip) holds the package plus the problem files and tools in `problem-files/`. Rebuild it with

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-75 --zip ../week-75-source.zip --top week-75
  ```

  and check a clean rebuild from the extracted ZIP with `python3 build.py --out output` in its `week-75/` folder. The print copies in `../../week-75/` and `editable/reference-pdfs/` come from that package build.

The review and research record is in [plans/ggt-prototypes-66-75/week-75/](../../../plans/ggt-prototypes-66-75/week-75/) and the review card in [plans/review/week-75.md](../../../plans/review/week-75.md).
