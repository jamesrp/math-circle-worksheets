# Week 94: Calibration lab — current editable source

Three student packets (K–1, W94-K; Grades 2–3, W94-M; Grades 4–5, W94-U) and a 6-page theorem-first adult guide (W94-F). Unpiloted; organizer review pending; printing, cutting, handling and the games are unrehearsed. The print PDFs are in [../../week-94/](../../week-94/).

**Problem files, October 23, 2026.** The student packets are stored as [problem files](../problem-files/README.md): `week.toml`, `template.tex` (the old `common.tex` preamble and drawing macros, with each band's header, footer id and type size as placeholders) and one file per problem or shared rule in `problems/`, in the flow layout. The conversion changed no wording or figure: the generated LaTeX differs from the old band files only by blank lines between sections and `common.tex` written in place of `\input{common.tex}`, and in this container all three packets compile to PDFs byte-identical to the old source's. Against the print copies, compiled with a newer pdfTeX (1.40.27), the old and new sources both differ by the same antialiased glyph pixels (at most 105 on a page at 100 dpi); pages and extracted text are identical. The hand-written band files, `common.tex` and the previous source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

**Card fixes, October 23, 2026.** From the review card (`plans/review/week-94.md`), K–1 gains Problems 4–6 on two new pages, playing the secret-extra machine with cube towers. These are K–1 variants inside problem files 10, 11, 12 and 14. Grades 2–3 Problem 2 loses its method sentence; Grades 4–5 page 3 now says "For Problems 3–4", and Problem 7 is reworded. The guide gains the K–1 route, answers, timing and materials, and its Problem 7 example now uses a stretch of 3. All footers became v2; the v1 PDFs are in [week-94/archive-before-card-fixes-2026-10-23/](../../week-94/archive-before-card-fixes-2026-10-23/README.md). Later that day an independent critic reviewed the new K–1 pages ([its review](../../../plans/review/checks/week-94/k1-critic-2026-10-23/README.md)); its four shoulds are fixed in W94-K-v3 and W94-F-v3, with the v2 PDFs in [week-94/archive-before-critic-fixes-2026-10-23/](../../week-94/archive-before-critic-fixes-2026-10-23/README.md). The K–1 pages remain unpiloted.

- **Student pages:** edit `problems/*.md`, then build every view and compare:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-94 --out tmp/week-94-views --tex --publish lowell-math-circle-year-2/band-views/week-94
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-94-views lowell-math-circle-year-2/week-94 week-94
  python3 lowell-math-circle-year-2/source/band-views/band_views.py readme
  ```

  The first-route and return packets, the one-page problem menu and the key of the problems' ideas are published in [band-views/week-94/](../../band-views/README.md#weeks-stored-as-problem-files).
- **Adult guide:** `editable/guide/facilitator.tex`, built by the package. The problem files carry each problem's one-sentence idea (`kernel`), not its answers.
- **Portable package:** `editable/` is the package (`editable/README.md`); `editable/student/regenerate.py` writes the band LaTeX from the problem files and the package build runs it first, then the mathematical checker. The [portable source ZIP](../week-94-source.zip) holds the package plus the problem files and tools in `problem-files/`. Rebuild it with

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-94 --zip ../week-94-source.zip --top week-94
  ```

  and check a clean rebuild from the extracted ZIP with `python3 week-94/build.py --out rebuilt --work tmp/build`.

The production record is in [plans/new-families-92-97/](../../../plans/new-families-92-97/STATUS.md) and the review card in [plans/review/week-94.md](../../../plans/review/week-94.md).
