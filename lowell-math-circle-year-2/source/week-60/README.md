# Week 60: Take it or pass — current editable source

One shared student packet (8 pages, W60-S-v3: Grades K–5 pages 1, 2 and 6, Grades 3–5 pages 3 and 7, Grades 4–5 pages 4, 5 and 8) and an 8-page theorem-first adult guide (W60-FAC-v3). Unpiloted; rolling, counters, card scoring and the K–1 towers are physically unrehearsed. The print PDFs are in [../../week-60/](../../week-60/).

**Review-card fixes, October 23, 2026.** The [review card](../../../plans/review/week-60.md)'s seven shoulds and coulds 8 and 10–14: pages 1, 2 and 6 are headed Grades K–5, and the guide's KK11 paragraph becomes an adult-led K–1 route (two-offer rounds, then take and pass cube towers by first-offer row on pages 2 and 6) with a plain-words key; page 1 puts out one turn counter per offer; page 2's practice rule takes any first offer; each Problem 4 card has A and B lines, so the guide's erase step is gone; Problem 5 asks "Take or pass in each position? Explain with average scores." without the average blanks; Problem 7 continues on a new page with bag 0, 2, 6 (pass 0 and 2, take 6, total 34); the guide makes a blank die stickered 0, 0, 4, 4, 6, 6 the default draw, with tickets as the fallback, and page 1 now reads "Every offer is a fresh draw from the whole bag: roll the bag's die, or put the ticket back and mix."; Problem 2 names its competitors; the p. 8 tie sentence is corrected; Problem 7's repeated draw rules and Problem 8's "How should the first offer 5 be treated in each?" are cut; Problem 6 asks "Can any legal plan beat plan B from Problem 4 on the 27 cards? Explain."; cutting the cards is optional. Could 10 (purple chevrons) and the 3/3/1 roster sentence of could 14 went with the tiling paragraph. Could 9 (moving Problem 7 before Problem 5) is left. The replaced PDFs are in [../../week-60/archive-before-card-fixes-2026-10-23/](../../week-60/archive-before-card-fixes-2026-10-23/).

**Problem files, October 23, 2026.** The student packet is stored as [problem files](../problem-files/README.md): `week.toml`, `template.tex` (the head of the old `students.tex`, with its card and position macros) and one file per problem in `problems/`, in the flow layout. This is a shared-packet week: `week.toml` defines one band, `shared`, whose packet is `week-60-students.pdf`, and each page's header range is set by `\renewcommand{\band}` in the text that opens the page. The conversion changed no wording or figure: the generated LaTeX differs from the old `students.tex` only by blank lines between sections, and the rebuilt packet matches the old builder's in pages, extracted text and 100-dpi pixels. Against the print copy, compiled with a newer pdfTeX (1.40.27), the old and new builders both differ the same way: small glyph differences, and shorter rows in Problem 1's rounds table, whose `\arraystretch` the newer TeX Live applies differently. The hand-written `students.tex` and the October 4 source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

**Critic follow-up, October 23, 2026 (W60-FAC-v3).** An independent critic noted that the guide gave KK11 one kit (one die, four counters, 30 cubes) for two pairs who roll and build towers, while the first-6 row alone takes 28 cubes. The guide now prepares five kits, two for KK11 (one per pair), 30 linking cubes per KK11 pair, and a page 1 and pages 2 and 6 for each pair. The student packet is unchanged (W60-S-v3). The v2 guide is in [../../week-60/archive-before-critic-fixes-2026-10-23/](../../week-60/archive-before-critic-fixes-2026-10-23/) and the previous ZIP in [archive-before-critic-fixes-2026-10-23/](archive-before-critic-fixes-2026-10-23/README.md). Unpiloted.

- **Student pages:** edit `problems/*.md`, then build and compare:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-60 --out tmp/week-60-views --tex
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-60-views lowell-math-circle-year-2/week-60 week-60
  ```

  The build also writes a first-route and a return packet, a one-page problem menu and a key view into `tmp/`; they are not published. The published views of this week are its band slices and page menu in [band-views/week-60/](../../band-views/README.md), built from the page index `../band-views/indexes/week-60.toml` by `band_views.py build`; update the index when a page's header range or problems change.
- **Adult guide:** `editable/guide/facilitator.tex`, built by the package.
- **Portable package:** `editable/` is the package (`editable/README.md`); `editable/student/regenerate.py` writes `students.tex` from the problem files, and the package `build.py` runs it before compiling. `editable/reference-pdfs/` holds copies of the print PDFs. The [portable source ZIP](../week-60-source.zip) holds the package plus the problem files and tools in `problem-files/`. Rebuild it with

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-60 --zip ../week-60-source.zip --top week-60
  ```

  and check a clean rebuild from the extracted ZIP with `python3 week-60/build.py --out rebuilt`.

The research and review record is in [plans/new-themes-52-63/week-60/](../../../plans/new-themes-52-63/week-60/outline.md) and the review card in [plans/review/week-60.md](../../../plans/review/week-60.md).
