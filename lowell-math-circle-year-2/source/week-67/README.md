# Week 67: Meeting on shortest roads

One shared Grades 3–5 prototype: 5 student pages and a separate 3-page theorem-first adult guide. Independently reviewed and digitally checked, awaiting organizer review. Unpiloted; physical preparation and handling have not been rehearsed. The week number is a library identifier, not an adopted schedule.

**Problem files, October 23, 2026.** The student packet is stored as [problem files](../problem-files/README.md) in this folder: `week.toml`, `template.tex` (the old `students.tex` preamble) and one file per problem in `problems/`, in the flow layout. The conversion changed no wording or figure: the generated `student/students.tex` differs from the old hand-written file only by blank lines between sections, and the packet rebuilds with the same pages, text and pixels. The old `students.tex` and the October 6 source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

**Card fixes, October 23, 2026 (v2).** After the conversion, the review card's shoulds and coulds were made in the problem files and the guide: Problem 5 moved to its own page with two blank cube maps; Problem 4's right-hand homes are 000, 001 and 111 (meeting label 001, not next to 111); the p. 1 example is drawn at the boards' spacing; p. 4's label sentence and Problem 2's "Keep a drawing" are gone. The guide adds an adult-led K–1 route with a plain-words key, median graphs and the majority-as-middle remark, two extra maps for Problem 3, the six-dot launch remark and a 1.2 cm counter size. Footers GGT67-S-v2 and GGT67-FAC-v2. `review/verify_card_fixes_2026_10_23.py` checks every changed claim, and `review/card-fixes-2026-10-23.md` records each card item. The replaced PDFs are in [../../week-67/archive-before-card-fixes-2026-10-23/](../../week-67/archive-before-card-fixes-2026-10-23/README.md) and the replaced ZIP in [archive-before-card-fixes-2026-10-23/](archive-before-card-fixes-2026-10-23/README.md).

- **Student pages:** edit `problems/*.md` (the page preamble and macros are in `template.tex`), then build and compare:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-67 --out tmp/week-67-views --tex
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-67-views lowell-math-circle-year-2/week-67 week-67
  ```

  Week 67 is a shared-packet week, so its one-page menu in [band-views/week-67/](../../band-views/README.md) is built from `../band-views/indexes/week-67.toml` by `band_views.py build`; update the index when a problem moves to another page.
- **Print copies:** `build.py` (below) first runs `student/regenerate.py`, which writes `student/students.tex` from the problem files, then compiles the packet and the guide. The print copies in [../../week-67/](../../week-67/) come from this build.
- **Portable ZIP:** [../week-67-source.zip](../week-67-source.zip) holds this folder with the problem-file tools in `tools/`, written by `python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-67 --flat --zip week-67-source.zip --top week-67`.

## Build from this portable package

Use Python 3 and a normal TeX Live/MacTeX installation with pdfLaTeX, TikZ/PGF, AMS fonts, geometry, fancyhdr and Latin Modern (the guides may additionally use enumitem and hyperref). No network, repository files, private references, external artwork or custom Python packages are needed.

    python3 build.py --out output
    python3 build.py --verify-only

The first command reconstructs both named PDFs; the second runs the independent, student and adult mathematical checks without TeX. Builders run in an isolated temporary directory. Edit the student pages in `problems/*.md` and `template.tex` (never only the generated `student/students.tex`), and the adult guide in `guide/facilitator.tex`. All required authored input is here.

## Readiness and use

Print single-sided US Letter at 100% / Actual Size. The grade band is approximate and not a readiness guarantee. Read `student/README.md` for the particular reading, arithmetic, spatial and representational prerequisites, and the adult guide for materials, preparation, a manageable first route, hints and stopping points. No K–1 route is implied. Page completion is not the goal.

The mathematical destination is distinct from the familiar props: For three vertices of a rectangular unit grid with Manhattan distance, the unique vertex belonging to some shortest route for each pair is (median x, median y).

`MATHEMATICS.md` records assumptions and general arguments. `SOURCES.md` gives verified primary-source locations and attribution limits. Independent adversarial review and revision decisions are preserved in the repository's `plans/ggt-prototypes-66-75/week-67/` record. The actual ZIP extraction/rebuild comparison is recorded there as `release-checks.json`; a source/PDF build does not establish physical readiness.

The package excludes stage prompts, borrowed exemplars, downloaded references, cached fonts, generated render images, build logs, old versions and private classroom information.
