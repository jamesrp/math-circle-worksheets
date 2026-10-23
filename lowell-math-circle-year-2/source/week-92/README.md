# Week 92: Fold-and-stretch predictions — current editable source

One shared student packet (7 pages, W92-S-v3: pages 1–2 and 4 Grades 2–5, page 3 Grades 2–3, pages 5–7 Grades 4–5) and a 5-page theorem-first adult guide. Unpiloted; physical rehearsal untested. The print PDFs are in [../../week-92/](../../week-92/).

**Problem files, October 23, 2026.** The student packet is stored as [problem files](../problem-files/README.md): `week.toml`, `figures.py` (the old `students.tex` preamble and drawing macros, as its page template) and one file per problem or shared rule in `problems/`, in the canvas layout: each page is one TikZ picture, each prompt and text sits at the height its heading gives, and each figure is the old TikZ code verbatim. `band(...)` at the top of a page sets the grade range its header prints. The conversion changed no wording or figure: the rebuilt packet is byte-identical to the old source's build in this container. Against the print copy, compiled with a newer pdfTeX (1.40.27), the old and new sources both differ by the same antialiased glyph pixels (at most 76 on a page at 100 dpi); pages and extracted text are identical. The hand-written `students.tex` and the previous source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

- **Student pages:** edit `problems/*.md`, then build and compare:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-92 --out tmp/week-92-views --tex
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-92-views lowell-math-circle-year-2/week-92 week-92
  ```

  Week 92 is a shared-packet week, so its band slices and one-page menu in [band-views/week-92/](../../band-views/README.md) are built from the page index `../band-views/indexes/week-92.toml` by `band_views.py build`; update the index when a problem moves to another page or a page's grade range changes.
- **Adult guide:** `editable/guide/facilitator.tex`, built by the package. The problem files carry each problem's one-sentence idea (`kernel`), not its answers.
- **Portable package:** `editable/` is the package (`editable/README.md`); `editable/student/regenerate.py` writes `students.tex` from the problem files and the package build runs it first, then the mathematical checker. The [portable source ZIP](../week-92-source.zip) holds the package plus the problem files and tools in `problem-files/`. Rebuild it with

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-92 --zip ../week-92-source.zip --top week-92
  ```

  and check a clean rebuild from the extracted ZIP with `python3 week-92/build.py --out rebuilt --work tmp/build`.

**Card fixes, October 23, 2026 (W92-S-v3).** Every should and the small coulds of [the review card](../../../plans/review/week-92.md) are done in the problem files and the guide: `band('Grades 2--5')` heads pages 1–2 and 4 (and the page index changed with it); Problem 3 prints six after-tracks per band, 14 mm apart; Problem 4's tracks move up and Problem 5 gets two Start/After pairs in place of a drawing line; the sentence about one marker on page 2 and Problem 4's "Is 12 the only possible next place?" are cut. The guide adds the K–1 fold-and-hop route with a plain-words key, the upper table's first hour, optional tracing-paper strips, and fixes two Problem 1 sentences. `editable/check_math.py` checks the new claims (six-track histories, the four-move gap 1, 2, 4, 8, 16, and that odd starts take five moves to reach 0). Unchanged pages 5–7 differ from the v2 print copy only in the footer's version digit. The previous PDFs are in [../../week-92/archive-before-card-fixes-2026-10-23/](../../week-92/archive-before-card-fixes-2026-10-23/README.md). The P5 drawing line and the K–1 route are unrehearsed.

The production record is in [plans/new-families-92-97/](../../../plans/new-families-92-97/STATUS.md) and the review card in [plans/review/week-92.md](../../../plans/review/week-92.md).
