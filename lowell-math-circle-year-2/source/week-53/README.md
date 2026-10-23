# Week 53: Connecting networks — current editable source

One shared student packet (9 pages, W53-networks-v2: pages 1–4 headed Grades K–5, pages 5–9 Grades 4–5) and an 8-page theorem-first adult guide (W53-guide-v2). Unpiloted; the counters, markers and payment tray have not been handled in a session. The print PDFs are in [../../week-53/](../../week-53/).

**Problem files, October 23, 2026.** The student packet is stored as [problem files](../problem-files/README.md): `week.toml`, `template.tex` (the old `students.tex` preamble), `figures.py` and one file per problem in `problems/`, in the flow layout. The maps are still drawn by `editable/student/diagrams.py` from `editable/student/networks.json`; `figures.py` hands their macro definitions to `problems/00-diagram-macros.md` at the start of the packet. The conversion changed no wording or figure: the generated LaTeX differs from the old `students.tex` only by blank lines and by those definitions, which the old builder wrote to a separate file. The rebuilt packet matches the old source's build in pages, extracted text and 100-dpi pixels; the print copy, compiled with TeX Live 2025 (pdfTeX 1.40.27), differs from both builds by the same few glyph pixels (at most 48 on a page at 100 dpi). The hand-written `students.tex` and the October 4 ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

- **Student pages:** edit `problems/*.md` (map data in `editable/student/networks.json`), then build and compare:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-53 --out tmp/week-53-views --tex
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-53-views lowell-math-circle-year-2/week-53 week-53
  ```

  Week 53 is a shared-packet week, so its band slices and one-page menu in [band-views/week-53/](../../band-views/README.md) are built from the page index `../band-views/indexes/week-53.toml` by `band_views.py build`; update the index when a page's grade range or problems change.
- **Adult guide:** `editable/guide/facilitator.tex`, built by the package. The problem files carry each problem's one-sentence idea (`kernel`), not its answers.
- **Portable package:** `editable/` is the package (`editable/README.md`); `editable/student/regenerate.py` writes `students.tex` from the problem files and the package build runs it first. The [portable source ZIP](../week-53-source.zip) holds the package plus the problem files and tools in `problem-files/`. Rebuild it with

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-53 --zip ../week-53-source.zip --top week-53
  ```

  and check a clean rebuild from the extracted ZIP with `python3 week-53/build.py --out rebuilt`.

**Card fixes, October 23, 2026 (v2).** From the review card: the CD, DE and BD price labels on pp. 6 and 8 now sit on their own links (`label_sides`, `label_fractions` and `label_offsets` in `networks.json`, read by `diagrams.py`); every price on Problems 3 and 4 has dots, and dotted labels are placed so their white boxes clear their own links (P1 and P2 labels moved slightly; AC's label on P2 and P3 is inside the triangle); pp. 1–4 are headed Grades K–5 and the guide routes K–1 through them; Problems 2 and 4 print five record maps; Problem 6's answer areas are headed "In every cheapest purchase:" and "In no cheapest purchase:". `plans/review/checks/week-53/check_card_fixes.py` checks the printed labels, dots, headers and the keys. The previous PDFs and the conversion ZIP are in `archive-before-card-fixes-2026-10-23/` folders beside the current files.

The research and review record is in [plans/new-themes-52-63/week-53/](../../../plans/new-themes-52-63/week-53/) and the review card in [plans/review/week-53.md](../../../plans/review/week-53.md).
