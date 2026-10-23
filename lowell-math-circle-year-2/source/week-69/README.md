# Week 69: Thin and fat road triangles — current editable source

One shared Grades 4–5 packet (4 student pages, GGT69-S-v3) and a 3-page theorem-first adult guide (GGT69-FAC-v4). Unpiloted; no physical rehearsal has been performed. The print PDFs are in [../../week-69/](../../week-69/).

**Problem files, October 23, 2026.** The student packet is stored as [problem files](../problem-files/README.md): `week.toml`, `template.tex` (the old `students.tex` preamble) and one file per problem in `problems/`. The conversion changed no wording or figure: the generated LaTeX differs from the old `students.tex` only by blank lines between sections, and rebuilt here the two give pixel-identical packets (the October 16 print PDF, made with another TeX installation, differs from both by at most 123 pixels a page with identical text). The hand-written `students.tex` and the previous source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

**Card shoulds, October 23, 2026** (GGT69-S-v3, GGT69-FAC-v3), made in the problem files after the conversion. Problem 3's middle board has new homes A (0,0), B (4,2), C (2,4), so it no longer repeats Problem 2's board: every side has choices (15, 6 and 15 shortest routes) and the biggest gap is 3, only at (0,3) or (3,0). Page 2 defines the gap with "the nearer of the other two colored sides" and has no ruled lines under Problem 2; Problem 5 asks for "a gap bigger than 0". The guide's Problem 2 key now uses a gap-2 triangle and saves the left/top choice for Problem 3; its Problem 3 table covers the new board with a child's proof that no gap exceeds 3; it adds two extra copies of pages 1 and 3 per pair, pencil before colour, home counters marked A, B, C, and routes for 2–3 and K–1 tables with a plain-words key. `editable/guide/check_math.py` checks each changed claim (all 1,350 middle-board triangles) and the printed wording. Problem numbers and pages are unchanged; the guide grew to 3 pages. The previous PDFs are in [../../week-69/archive-before-card-fixes-2026-10-23/](../../week-69/archive-before-card-fixes-2026-10-23/) and the conversion's ZIP in [../archive-before-card-fixes-2026-10-23/](../archive-before-card-fixes-2026-10-23/). Unpiloted.

**Critic follow-up, October 23, 2026 (GGT69-FAC-v4).** An independent critic predicted that the K–1 route's discovery, "every road used is coloured twice", would be lost when five- to seven-year-olds drew two colours side by side on roads about 17 mm long, and noted that the route had one tree and no time. The guide's K–1 route now has children lay one paper strip of each route's colour on every road of the route (or the adult colours while they trace), lets them go on to new homes or the second tree on the extra copies of page 1, and takes about 15–20 minutes; the materials add ten 12 by 4 mm strips per colour for that table (no route on either tree has more than six roads). The student packet is unchanged (GGT69-S-v3). `editable/guide/check_math.py` checks the new wording. The v3 guide is in [../../week-69/archive-before-critic-fixes-2026-10-23/](../../week-69/archive-before-critic-fixes-2026-10-23/) and the previous ZIP in [archive-before-critic-fixes-2026-10-23/](archive-before-critic-fixes-2026-10-23/README.md). Unpiloted; the strips are unrehearsed.

- **Student pages:** edit `problems/*.md`, then build and compare:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-69 --out tmp/week-69-views --tex
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-69-views lowell-math-circle-year-2/week-69 week-69
  ```

  Week 69 is a shared-packet week, so its one-page menu in [band-views/week-69/](../../band-views/README.md) is built from the page index `../band-views/indexes/week-69.toml` by `band_views.py build`; update the index when a problem moves to another page.
- **Adult guide:** `editable/guide/facilitator.tex`, built by the package. The problem files carry each problem's one-sentence idea (`kernel`), not its answers.
- **Portable package:** `editable/` is the package (`editable/README.md`, which keeps the week's earlier release notes); `editable/student/regenerate.py` writes `students.tex` from the problem files and the package build runs it first. The [portable source ZIP](../week-69-source.zip) holds the package plus the problem files and tools in `problem-files/`. Rebuild it with

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-69 --zip ../week-69-source.zip --top week-69
  ```

  and check a clean rebuild from the extracted ZIP with `python3 build.py --out output` in its `week-69/` folder. `editable/reference-pdfs/` holds copies of the print PDFs.

The review and research record is in [plans/ggt-prototypes-66-75/week-69/](../../../plans/ggt-prototypes-66-75/week-69/) and the review card in [plans/review/week-69.md](../../../plans/review/week-69.md).
