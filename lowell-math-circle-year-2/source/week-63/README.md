# Week 63: Cards away from home — current editable source

One shared student packet (9 pages, W63-S-v3: Grades K–5 pages 1–3, Grades 3–5 pages 4–5, Grades 4–5 pages 6–9), a 3-page materials file of cards, home strips and outcome decks (W63-M-v3) and an 11-page theorem-first adult guide (W63-G-v2). Unpiloted; cutting, placement and the reversal rehearsal are physically unperformed. The print PDFs are in [../../week-63/](../../week-63/).

**K–1 route, October 23, 2026 (review card fixes).** Pages 1–3 are headed Grades K–5, and guide p. 3 is a K–1 route for the parent's table: P1, P2's two-ring sort, P3 split by the card in home A and pooled to nine, then "Can exactly three of A, B, C, D be home?", with a plain-words key. The home cells (materials p. 1) and the six A–C outcome cards and group labels (p. 2) now show each card's picture beside its letter. Problem 8 lost its two worked removals, which are now a held hint in the guide, and gained twelve A–E boards; Problem 9 asks for a rule for three or more cards and offers homes B, C, D for E. Pages 1 and 2 lost two redundant sentences. The counts and pictures are checked by `plans/review/checks/week-63/check_k1_route.py`. The previous PDFs are in `../../week-63/archive-before-card-fixes-2026-10-23/`. Unpiloted; cutting and placement are physically unrehearsed.

**Problem files, October 23, 2026.** The student packet is stored as [problem files](../problem-files/README.md): `week.toml`, `template.tex` (the head of the old `students.tex`) and one file per problem in `problems/`, in the flow layout. This is a shared-packet week: `week.toml` defines one band, `shared`, whose packet is `week-63-students.pdf`, and each page's header range is set by `\band` in the problem files. The conversion changed no wording or figure: the generated LaTeX differs from the old `students.tex` only by blank lines between sections, the footer id written as a placeholder, and an `\\InputIfFileExists` that finds `editable/student/common.tex` from either folder. The rebuilt packet matches the old builder's in pages, extracted text and 100-dpi pixels; against the print copy, compiled with a newer pdfTeX (1.40.27), the old and new builders both differ by the same small glyph-pixel counts. The hand-written `students.tex` and the October 4 source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

- **Student pages:** edit `problems/*.md`, then build and compare:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-63 --out tmp/week-63-views --tex
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-63-views lowell-math-circle-year-2/week-63 week-63
  ```

  The build also writes a first-route and a return packet, a one-page problem menu and a key view into `tmp/`; they are not published. The published views of this week are its band slices and page menu in [band-views/week-63/](../../band-views/README.md), built from the page index `../band-views/indexes/week-63.toml` by `band_views.py build`; update the index when a page's header range or problems change.
- **Adult guide and materials:** `editable/guide/facilitator.tex` and `editable/student/materials.tex`, built by the package.
- **Portable package:** `editable/` is the package (`editable/README.md`); `editable/student/regenerate.py` writes `students.tex` from the problem files, and the package `build.py` runs it before compiling. `editable/reference-pdfs/` holds copies of the print PDFs. The [portable source ZIP](../week-63-source.zip) holds the package plus the problem files and tools in `problem-files/`. Rebuild it with

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-63 --zip ../week-63-source.zip --top week-63
  ```

  and check a clean rebuild from the extracted ZIP with `python3 week-63/build.py --out rebuilt`. To run the problem-file tools inside the extracted ZIP, set `TEXINPUTS` to the absolute path of `week-63/student/` followed by a colon, so the template finds `common.tex`.

The research and review record is in [plans/new-themes-52-63/week-63/](../../../plans/new-themes-52-63/week-63/outline.md) and the review card in [plans/review/week-63.md](../../../plans/review/week-63.md).
