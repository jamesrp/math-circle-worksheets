# Week 85: Drawing machines — current editable source

Two student packets, shared Grades 2–5 (4 pages, W85-S-v1) and upper Grades 4–5 (4 pages, W85-U-v1, the return visit), a 10-page materials packet (W85-M-v1) and a 5-page theorem-first adult guide. Unpiloted; no pantograph has been built, and the guide's rehearsal has not been done. The print PDFs are in [../../week-85/](../../week-85/).

**Problem files, October 23, 2026.** The student packets are stored as [problem files](../problem-files/README.md): `week.toml`, `figures.py` (the old generator's drawing code, page template and materials pages, unchanged) and one file per problem in `problems/`. The two packets are the week's two bands. The conversion changed no wording or drawing: the LaTeX of the shared, upper and materials packets is byte-identical to the old generator's, and the package build gives byte-identical PDFs. The print copies were compiled with a newer pdfTeX (1.40.27), so a rebuild here, by the old builder or the new, differs from them only in glyph rasters (at most 35 pixels on a page at 100 dpi). The old generator and the previous source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

- **Student pages:** edit `problems/*.md` (drawings in `figures.py`), then build every view:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-85 --out tmp/week-85-views --tex --publish lowell-math-circle-year-2/band-views/week-85
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-85-views lowell-math-circle-year-2/week-85 week-85
  python3 lowell-math-circle-year-2/source/band-views/band_views.py readme
  ```

  The first-route packet (shared), the return packet (upper), the one-page problem menu and the key view are published in [band-views/week-85/](../../band-views/README.md#weeks-stored-as-problem-files).
- **Materials and adult guide:** the materials pages are drawn by `materials_tex()` in `figures.py`; the guide's source is `editable/guide/facilitator.tex`. The problem files carry each problem's one-sentence idea (`kernel`), not its answers.
- **Portable package:** `editable/` is the package (README, mathematical checks, guide source, reference PDFs). `editable/student/build.py` writes the student and materials LaTeX from the problem files, and `editable/build.py` builds all four PDFs. The [portable source ZIP](../week-85-source.zip) holds the package plus the problem files and tools in `problem-files/`, written by `package.py`:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-85 --zip ../week-85-source.zip --top week-85
  ```

  Check a clean rebuild from the extracted ZIP with `python3 week-85/build.py --out rebuilt --work tmp/build`.

Read `editable/README.md` for printing, dependencies and evidence. The production record is in [plans/seven-families-85-91/production/](../../../plans/seven-families-85-91/production/STATUS.md) and the review card in [plans/review/week-85.md](../../../plans/review/week-85.md).
