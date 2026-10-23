# Week 84: Public knowledge — current editable source

One shared Grades 2–5 student packet (8 pages, W84-PK-draft-v2: Problems 1–4 on pages 1–3, cards and labels on pages 4–8) and a 5-page theorem-first adult guide. Unpiloted, and awaiting the organizer's first review; the cards, dolls and reply slots have not been handled in a session. The print PDFs are in [../../week-84/](../../week-84/).

**Problem files, October 23, 2026.** The student packet is stored as [problem files](../problem-files/README.md): `week.toml`, `template.tex` (the old `students.tex` preamble) and one file per problem or card page in `problems/`, in the flow layout. The conversion changed no wording or figure: the generated LaTeX differs from the old `students.tex` only by blank lines between sections. The rebuilt packet matches the old builder's in pages, extracted text and 100-dpi pixels; against the print copy, compiled with a newer pdfTeX (1.40.27), the old and new builders both differ by the same glyph pixels on pages 1–2 (at most 81). The hand-written `students.tex` and the previous source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

- **Student pages:** edit `problems/*.md`, then build and compare:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-84 --out tmp/week-84-views --tex
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-84-views lowell-math-circle-year-2/week-84 week-84
  ```

  Week 84 is a shared-packet week, so its one-page menu in [band-views/week-84/](../../band-views/README.md) is built from the page index `../band-views/indexes/week-84.toml` by `band_views.py build`; update the index when a problem moves to another page.
- **Adult guide:** `editable/guide/facilitator.tex`, built by the package. The problem files carry each problem's one-sentence idea (`kernel`), not its answers.
- **Portable package:** `editable/` is the package (`editable/README.md`); `editable/student/regenerate.py` writes `students.tex` from the problem files and the package build runs it first, then the mathematical checker. The [portable source ZIP](../week-84-source.zip) holds the package plus the problem files and tools in `problem-files/`. Rebuild it with

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-84 --zip ../week-84-source.zip --top week-84
  ```

  and check a clean rebuild from the extracted ZIP with `python3 week-84/build.py --out rebuilt --work tmp/build`.

The research and review record is in [plans/infinity-prototypes-79-84/](../../../plans/infinity-prototypes-79-84/README.md) and the review card in [plans/review/week-84.md](../../../plans/review/week-84.md).
