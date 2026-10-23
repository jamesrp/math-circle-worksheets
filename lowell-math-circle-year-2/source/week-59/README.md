# Week 59: Constant-width shapes — current editable source

One shared student packet (6 pages, W59-S-v4: Grades 2–5 page 1, Grades K–5 page 2, Grades 3–5 pages 3–5, Grades 4–5 page 6), a 3-page materials file of full-size pieces, a grid mat and compass templates (W59-M-v1) and an 8-page theorem-first adult guide (W59-F-v3). Unpiloted; cutting, rails and compass handling are physically unrehearsed. The print PDFs are in [../../week-59/](../../week-59/).

**Review-card fixes, October 23, 2026.** The [review card](../../../plans/review/week-59.md)'s five shoulds and coulds 6–11: page 2 is headed Grades K–5 and the guide's K–1 paragraph becomes an adult-led route through the launch and Problem 2 (sort the pieces into gets stuck, spins with a gap and spins snug, then count grid squares) with a plain-words key; Problem 2 closes the edges on the disk instead of setting 60 mm, and the guide tapes the rails against the kit's own disk with square-edged rails and accepts a blank deciding position; Problem 4 asks for every position between the drawings; Problem 6 loses the large circle and its sentence (the drawing is now the guide's held hint) and asks "Explain how you know."; page 1 says drawings are smaller than the real pieces; the guide makes card backing the default for Problem 3, sizes the launch parallelogram at 46 × 32 mm and cuts build residue. The replaced PDFs are in [../../week-59/archive-before-card-fixes-2026-10-23/](../../week-59/archive-before-card-fixes-2026-10-23/).

**Critic follow-up, October 23, 2026 (W59-S-v4, W59-F-v3).** An independent critic noted that Problem 6 still drew arc BC of the curved triangle bold, a silent pointer to the first step of the guide's held hint, and that the guide's K–1 route counted grid squares with nowhere to record them. All three arcs are now drawn at the same weight (`editable/student/make_assets.py`; only page 6 changed above the footer), and the adult writes the two counts beside each piece's name on page 2. The materials stay W59-M-v1. The replaced PDFs are in [../../week-59/archive-before-critic-fixes-2026-10-23/](../../week-59/archive-before-critic-fixes-2026-10-23/) and the previous ZIP in [archive-before-critic-fixes-2026-10-23/](archive-before-critic-fixes-2026-10-23/README.md). Unpiloted.

**Problem files, October 23, 2026.** The student packet is stored as [problem files](../problem-files/README.md): `week.toml`, `template.tex` (the head of the old `students.tex`, without `\input{assets.tex}`), `figures.py` and one file per problem in `problems/`, in the flow layout. This is a shared-packet week: `week.toml` defines one band, `shared`, whose packet is `week-59-students.pdf`, and each page's header range is set by `\renewcommand{\band}` in the text that opens the page. The pictures are still drawn by `editable/student/make_assets.py`: a figure section calls `asset(name)` in `figures.py`, which returns the TikZ code that the old `assets.tex` macro of that name held. The conversion changed no wording or figure: the rebuilt packet matches the old builder's in pages, extracted text and 100-dpi pixels; against the print copy, compiled with a newer pdfTeX (1.40.27), the old and new builders both differ by the same small pixel counts. The hand-written `students.tex` and the October 4 source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

- **Student pages:** edit `problems/*.md` (or a picture in `editable/student/make_assets.py`), then build and compare:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-59 --out tmp/week-59-views --tex
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-59-views lowell-math-circle-year-2/week-59 week-59
  ```

  The build also writes a first-route and a return packet, a one-page problem menu and a key view into `tmp/`; they are not published. The published views of this week are its band slices and page menu in [band-views/week-59/](../../band-views/README.md), built from the page index `../band-views/indexes/week-59.toml` by `band_views.py build`; update the index when a page's header range or problems change.
- **Adult guide and materials:** `editable/guide/facilitator.tex` and `editable/student/materials.tex` (whose pictures `make_assets.py` writes into `assets.tex` at build time), built by the package.
- **Portable package:** `editable/` is the package (`editable/README.md`); `editable/student/regenerate.py` writes `students.tex` from the problem files, and the package `build.py` runs it before compiling. `editable/reference-pdfs/` holds copies of the print PDFs. The [portable source ZIP](../week-59-source.zip) holds the package plus the problem files and tools in `problem-files/`. Rebuild it with

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-59 --zip ../week-59-source.zip --top week-59
  ```

  and check a clean rebuild from the extracted ZIP with `python3 week-59/build.py --out rebuilt`.

The research and review record is in [plans/new-themes-52-63/week-59/](../../../plans/new-themes-52-63/week-59/outline.md) and the review card in [plans/review/week-59.md](../../../plans/review/week-59.md).
