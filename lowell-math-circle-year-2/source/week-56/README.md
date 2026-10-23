# Week 56: Corners of a solid — current editable source

One shared student packet (9 pages, N56-S-v3: Grades K–5 pages 1 and 3–5, Grades 2–5 pages 2 and 6, Grades 4–5 pages 7–9), a 5-page materials file of nets, fan pieces and gap circles (N56-M-v2) and an 11-page theorem-first adult guide (N56-FAC-v2). Unpiloted; folding, fit and timing are physically unrehearsed. The print PDFs are in [../../week-56/](../../week-56/).

**K–1 route, October 23, 2026 (review card fixes).** Younger children now take Problem 1 for the cube and tetrahedron, Problem 3, Problem 4 for the same two solids by copying each corner's gap from a paper circle and gathering the copies into whole circles, and Problem 5, which now asks which pyramid corner leaves the bigger gap before the total. Pages 1 and 3–5 are headed Grades K–5; materials p. 5 has six gap circles; the guide has a K–1 route section, a print row for 14 circles per younger pair and a no-cut option. Problem 6 now says each change starts from the original cube, and the Problem 1 tetrahedron and octahedron icons were redrawn. The gap counts are checked by `plans/review/checks/week-56/check_k1_route.py`. The previous PDFs are in `../../week-56/archive-before-card-fixes-2026-10-23/`. Unpiloted; the gap-copy cutting is physically unrehearsed.

**Problem files, October 23, 2026.** The student packet is stored as [problem files](../problem-files/README.md): `week.toml`, `template.tex` (the head of the old `students.tex`) and one file per problem in `problems/`, in the flow layout. This is a shared-packet week: `week.toml` defines one band, `shared`, whose packet is `week-56-students.pdf`, and each page's header range is set by `\band` in the problem files. The conversion changed no wording or figure: the generated LaTeX differs from the old `students.tex` only by blank lines between sections. The rebuilt packet matches the old builder's in pages, extracted text and 100-dpi pixels; against the print copy, compiled with a newer pdfTeX (1.40.27), the old and new builders both differ by the same small glyph-pixel counts. The hand-written `students.tex` and the October 4 source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

- **Student pages:** edit `problems/*.md`, then build and compare:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-56 --out tmp/week-56-views --tex
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-56-views lowell-math-circle-year-2/week-56 week-56
  ```

  The build also writes a first-route and a return packet, a one-page problem menu and a key view into `tmp/`; they are not published. The published views of this week are its band slices and page menu in [band-views/week-56/](../../band-views/README.md), built from the page index `../band-views/indexes/week-56.toml` by `band_views.py build`; update the index when a page's header range or problems change.
- **Adult guide and materials:** `editable/guide/facilitator.tex` and `editable/student/materials.tex`, built by the package.
- **Portable package:** `editable/` is the package (`editable/README.md`); `editable/student/regenerate.py` writes `students.tex` from the problem files, and the package `build.py` runs it before compiling. `editable/reference-pdfs/` holds copies of the print PDFs. The [portable source ZIP](../week-56-source.zip) holds the package plus the problem files and tools in `problem-files/`. Rebuild it with

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-56 --zip ../week-56-source.zip --top week-56
  ```

  and check a clean rebuild from the extracted ZIP with `python3 week-56/build.py --out rebuilt`.

The research and review record is in [plans/new-themes-52-63/week-56/](../../../plans/new-themes-52-63/week-56/outline.md) and the review card in [plans/review/week-56.md](../../../plans/review/week-56.md).
