# Shortest reflected paths: Week 21 editable release — current editable source

**Review-card fixes, October 23, 2026.** The keep card's five shoulds and coulds 6–9 are done: Grades 2–3 Problem 7 asks the Grades 4–5 question (W21-23-v3; K–1 and Grades 4–5 unchanged), and the guide gives contacts from the end mark, says what string can settle, plans for eleven children and twelve strings, fixes the matching diagram's labels and the hour's timing, and numbers the route update 18 / 18. [editable/review/card-fixes-2026-10-23.md](editable/review/card-fixes-2026-10-23.md) lists them; `editable/review/check_card_fixes.py` checks them. The replaced Grades 2–3 packet and guide are in [../../week-21/archive-before-card-fixes-2026-10-23/](../../week-21/archive-before-card-fixes-2026-10-23/README.md) and the replaced ZIP in [archive-before-card-fixes-2026-10-23/](archive-before-card-fixes-2026-10-23/README.md).

**Problem files, October 23, 2026.** The student packets are stored as [problem files](../problem-files/README.md): `week.toml`, `figures.py` (the old builder's board data, drawing code and page template) and one file per problem in `problems/`; a problem used by several bands is one file with each band's wording inside it, and the shared rules are `problems/00-rules.md`. The conversion changed no wording or figure: the rebuilt LaTeX matches the old builder's line for line (only the file's final newline differs), and the three print PDFs rebuild with the same pages, extracted text and 100-dpi pixels. The previous builder (`build_packets.py`) and the ZIP it replaced are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

- **Student pages:** edit `problems/*.md` (boards and the page template in `figures.py`), then build every view:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-21 --out tmp/week-21-views --tex --publish lowell-math-circle-year-2/band-views/week-21
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-21-views lowell-math-circle-year-2/week-21 week-21
  ```

  The first-route and return packets (from the guide's entry problems and its return-visit note), the one-page problem menu and the key arranged by problem are published in [band-views/week-21/](../../band-views/README.md#weeks-stored-as-problem-files). A return packet's first page holds the rules alone, since Problem 1 (which shares their page) is not in it.
- **Adult guide:** its source is still `editable/facilitator-src/`, built by the package. `facilitator-src/check_geometry.py` now reads the board data from `figures.py` and each band's board order from the problem files.
- **Portable package:** `editable/` is the package. `editable/src/regenerate.py` writes the student LaTeX from the problem files and runs the old builder's board checks (`src/geometry-checks.json`); `build.sh` runs it and compiles. The [portable source ZIP](shortest-reflected-paths-week21-editable-source.zip) holds the package plus the problem files and tools in `problem-files/`, written by `package.py`:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-21 --zip shortest-reflected-paths-week21-editable-source.zip --top shortest-reflected-paths-week21-editable-source
  ```

  Check a clean rebuild from the extracted ZIP with `bash build.sh` and `python3 verify_revision.py`.

The [portable base source ZIP](shortest-reflected-paths-week21-editable-source.zip) and [complete extracted package](editable/README.md) contain the current **October 23, 2026 card-fix revision**, built on the October 4, 2026 fresh-review revision. Current print copies are in [../../week-21/](../../week-21/). References are exact duplicates of those print PDFs.

Read `editable/README.md` for dependencies and commands. Copy the complete package to a fresh folder under the project's `tmp/` before rebuilding; keep intermediates out of current print/source folders. `verify_revision.py` checks current pages and permits only specifically audited full-page alternate hashes for pre-existing font/hyphenation differences in unchanged student packets; the original strict verifier remains available. Every changed packet and guide reproduces exact 100-dpi pixels from the extracted ZIP.

The [corpus revision report](../../../plans/fresh-review-revision-2026-10-04/REPORT.md) records per-band decisions, independent mathematical/visual checks, all clean-ZIP rebuilds and physical-testing limits. Previous affected print PDFs and the complete previous source ZIP are separately archived in `archive-before-fresh-review-2026-10-04/` within their print/source folders. Bonus companions are separate; this base ZIP does not incorporate them. The theme remains **unpiloted** and can span several meetings.
