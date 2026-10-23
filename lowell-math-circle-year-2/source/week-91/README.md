# Week 91: Rotor-router machines — current editable source

One shared student packet (6 pages, Problems 1–7), a Grades 4–5 return-visit packet on roads (4 pages), 7 materials pages and a 6-page theorem-first adult guide. Unpiloted; printing, cutting, flipping, counter placement and timing are physically unrehearsed. The print PDFs are in [../../week-91/](../../week-91/).

**Problem files, October 23, 2026.** The student packet is stored as [problem files](../problem-files/README.md): `week.toml`, `figures.py` (the old generator's drawing helpers, unchanged, and the page template) and one file per problem in `problems/`, in the canvas layout. Each page's first file draws its header with `head(...)`, since the pages name different grade ranges. The conversion changed no wording or figure: the generated LaTeX is the old generator's byte for byte apart from a final newline, and in this container both compile to the same PDF. Against the print copy, compiled with a newer pdfTeX, both differ by the same antialiased glyph pixels (at most 133 on a page at 100 dpi); pages and extracted text are identical. The old generator and the previous source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

**Card fixes, October 23, 2026.** Made in the problem files after the conversion: pages 1–3 are headed Grades 2–5, Problem 4's target words sit level with their own trees, Problem 5 asks how many orders the eight-exit tree can make, and the footers are F91-S-v1, F91-RV-v1 and F91-M-v1. The guide has a K–1 route, the corrected return key (0040) with the first-block rule, a reconciled first-visit route and the new Problem 5 key. Student pages 1–5, the return-visit and materials footers and all guide pages changed. [editable/review/card-fixes-2026-10-23.md](editable/review/card-fixes-2026-10-23.md) lists what changed, what was deferred and how it was checked. The ZIP from the conversion is in [archive-before-card-fixes-2026-10-23/](archive-before-card-fixes-2026-10-23/README.md), and the replaced print PDFs are beside the current ones. The adult guide had printed F91-FAC-v1 before these changes too, so its id was then bumped to F91-FAC-v2 for the October 23 changes; nothing else changed in that bump.

- **Student pages:** edit `problems/*.md` (figures in `figures.py`), then build and compare:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-91 --out tmp/week-91-views --tex
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-91-views lowell-math-circle-year-2/week-91 week-91
  ```

  Week 91 is a shared-packet week, so its band slices and one-page menu in [band-views/week-91/](../../band-views/README.md) are built from the page index `../band-views/indexes/week-91.toml` by `band_views.py build`; update the index when a page's header or problems change.
- **Return visit, materials and adult guide:** `editable/student/generate.py` (return-visit packet and materials) and `editable/guide/facilitator.tex`, built by the package. The problem files carry each problem's one-sentence idea (`kernel`), not its answers.
- **Portable package:** `editable/` is the package (`editable/README.md`); `editable/student/regenerate.py` writes `students.tex` from the problem files and the package build runs it first. The [portable source ZIP](../week-91-source.zip) holds the package plus the problem files and tools in `problem-files/`. Rebuild it with

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-91 --zip ../week-91-source.zip --top week-91
  ```

  and check a clean rebuild from the extracted ZIP with `python3 week-91/build.py --out rebuilt --work tmp/build`.

The production record is in [plans/seven-families-85-91/](../../../plans/seven-families-85-91/README.md) and the review card in [plans/review/week-91.md](../../../plans/review/week-91.md).
