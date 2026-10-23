# Week 54: Partitions and rebuilding — current editable source

One shared student packet (9 pages, W54-S-v1: Grades 2–5 pages 1–5, Problems 1–5; Grades 4–5 pages 6–9, Problems 6–9) and an 8-page theorem-first adult guide (W54-FAC-v1), with an adult-led K–1 route on guide p. 2. Unpiloted; the cube pretests on guide p. 2 have not been run. The print PDFs are in [../../week-54/](../../week-54/).

**Problem files, October 23, 2026.** The student packet is stored as [problem files](../problem-files/README.md): `week.toml`, `figures.py` (the old `students.tex` preamble as the page template) and one file per problem or shared rule in `problems/`, in the canvas layout. Each page's first text section opens the page with `\beginpage{2--5}` or `\beginpage{4--5}`, which draws that page's header; prompts are placed with `## prompt @y`, and the TikZ drawing code is copied as written. The conversion changed no wording or figure: the rebuilt packet's page content streams are identical to the old `students.tex` compiled with the same TeX, and against the print copy, compiled with a newer pdfTeX (1.40.27, against 1.40.25 here), the old and new sources both differ by the same antialiased glyph pixels (at most 113 on a page at 100 dpi); pages and extracted text are identical. The hand-written `students.tex` and the October 4 source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

**Card fixes, October 23, 2026.** Made after the conversion, from the review card ([plans/review/week-54.md](../../../plans/review/week-54.md)). Guide: an adult-led K–1 route through student pp. 1–3 (Problem 1 with 4 cubes, Problem 3's nine 1s and (5, 3, 1), Problem 2's odd side with 6 cubes), with the parent reading and recording, a plain-words key and two 12-cube kits in place of the Week 1 pattern-block boards; the kits are linking cubes (loose squares hide joins; the longest strip is 24 cm with 2 cm cubes); the Problem 3 bridge says "one legal join is", since two 1s may join first; Problem 2 says why largest size 3 fails for 7; a spoken (6, 6, 1) contrast for Problem 4; the check script's path. Student pages: p. 1 reads "A collection uses all the units, in straight strips."; Problem 6 no longer repeats its picture in words and says "only odd sizes"; Problem 7's answer grids are 5 × 5 cells of 0.22 in, the size of the input squares; Problem 9 ends "Explain how you know." Could 9's printed (6, 6, 1) case is left for the organizer: it adds a non-example to a Grades 2–5 page, so the guide carries it as a spoken contrast. The pages keep their Grades 2–5 and 4–5 headers; the K–1 route is in the guide only. Changed pages: students pp. 1, 6, 7 and 9; guide pp. 1–5 and 8; the other pages are pixel-identical to the previous build. `editable/review/check_card_fixes_2026_10_23.py` checks the K–1 key, the kit, the bridge, the Problem 2 and 4 claims and the Problem 7 grids; `editable/review/check_pdf.py` reads the wording and measures the grids in the PDFs. The previous print copies are in [../../week-54/archive-before-card-fixes-2026-10-23/](../../week-54/archive-before-card-fixes-2026-10-23/README.md). Unpiloted; the K–1 route and the cube kits are physically unrehearsed.

- **Student pages:** edit `problems/*.md`, then build and compare:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-54 --out tmp/week-54-views --tex
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-54-views lowell-math-circle-year-2/week-54 week-54
  ```

  The build also writes a first-route packet, a one-page problem menu and a key view into `tmp/`; they are not published. Week 54 is a shared-packet week, so its band slices and page menu in [band-views/week-54/](../../band-views/README.md) are built from the page index `../band-views/indexes/week-54.toml` by `band_views.py build`; update the index when a page's header range or problems change.
- **Adult guide:** `editable/guide/facilitator.tex`, built by the package. The problem files carry each problem's one-sentence idea (`kernel`), not its answers.
- **Portable package:** `editable/` is the package (`editable/README.md`); `editable/student/regenerate.py` writes `students.tex` from the problem files and the package `build.py` runs it first. `editable/reference-pdfs/` holds copies of the print PDFs. The [portable source ZIP](../week-54-source.zip) holds the package plus the problem files and tools in `problem-files/`. Rebuild it with

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-54 --zip ../week-54-source.zip --top week-54
  ```

  and check a clean rebuild from the extracted ZIP with `python3 week-54/build.py --out rebuilt`.

The research and review record is in [plans/new-themes-52-63/week-54/](../../../plans/new-themes-52-63/week-54/outline.md) and the review card in [plans/review/week-54.md](../../../plans/review/week-54.md).
