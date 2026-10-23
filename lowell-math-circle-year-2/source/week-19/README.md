# Subset antichains: Week 19 editable release — current editable source

**Problem files, October 23, 2026.** The student packets are stored as [problem files](../problem-files/README.md): `week.toml`, `figures.py` (the old builder's drawing code and page template) and one file per problem in `problems/`, with each band's wording inside it. The conversion changed no wording or figure: the rebuilt LaTeX matches the old builder's byte for byte, and the three print PDFs rebuild with the same pages, extracted text and 100-dpi pixels. The previous builder (`build_packets.py`) and the ZIP it replaced are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

- **Student pages:** edit `problems/*.md` (figures and the page template in `figures.py`), then build every view:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-19 --out tmp/week-19-views --tex --publish lowell-math-circle-year-2/band-views/week-19
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-19-views lowell-math-circle-year-2/week-19 week-19
  ```

  The first-route and return packets, the one-page problem menu and the key arranged by problem are published in [band-views/week-19/](../../band-views/README.md#weeks-stored-as-problem-files).
- **Adult guide:** its source is still `editable/facilitator-src/guide.json`, built by the package.
- **Portable package:** `editable/` is the package. `editable/src/regenerate.py` writes the student LaTeX from the problem files and runs the answer checks (`src/answer_checks.py`); `build.sh` runs it and compiles. The [portable source ZIP](subset-antichains-week19-editable-source.zip) holds the package plus the problem files and tools in `problem-files/`, written by `package.py`:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-19 --zip subset-antichains-week19-editable-source.zip --top subset-antichains-week19-editable-source
  ```

  Check a clean rebuild from the extracted ZIP with `bash build.sh` and `python3 verify_revision.py`.

**Review-card fixes, October 23, 2026 (v3).** From the keep card (`plans/review/week-19.md`): a printable card sheet, [week-19-materials.pdf](../../week-19/week-19-materials.pdf) (sixteen 4.5 cm cards, every card with its top mark, drawn by `card_sheet_tex()` in `figures.py`); "One nested row." as the row example's caption in all three packets; Grades 2–3 Problem 6 without "Explain why you think it is best"; and a guide whose launch builds and sketches one collection that is in no task, makes checking the partner's job, fits the timing to 35–40 working minutes and names the card sheet. `editable/review/card-fixes-2026-10-23.md` says what changed and `editable/review/check_card_fixes.py` checks it; the replaced PDFs are in [../../week-19/archive-before-card-fixes-2026-10-23/](../../week-19/archive-before-card-fixes-2026-10-23/README.md) and the replaced ZIP in [archive-before-card-fixes-2026-10-23/](archive-before-card-fixes-2026-10-23/README.md). Card making and the launch are unrehearsed.

**Critic follow-up, October 23, 2026 (guide only).** After an independent critic's review the same day, the guide's key for Grades 2–3 Problem 6 (p. 8) says "Problem 8 asks why, and Problems 7 and 8 supply the universal argument." instead of "the problem no longer asks why it is best", which was revision history. The student packets, card sheet and views are unchanged. The replaced guide and ZIP are in the `archive-before-critic-fixes-2026-10-23/` folders.

The [portable base source ZIP](subset-antichains-week19-editable-source.zip) and [complete extracted package](editable/README.md) contain the **October 4, 2026 fresh-review revision** with the October 23 problem-file conversion and card fixes. Current print copies are in [../../week-19/](../../week-19/). References are exact duplicates of those print PDFs.

Read `editable/README.md` for dependencies and commands. Copy the complete package to a fresh folder under the project's `tmp/` before rebuilding; keep intermediates out of current print/source folders. `verify_revision.py` checks current pages and permits only specifically audited full-page alternate hashes for pre-existing font/hyphenation differences in unchanged student packets; the original strict verifier remains available. Every changed packet and guide reproduces exact 100-dpi pixels from the extracted ZIP.

The [corpus revision report](../../../plans/fresh-review-revision-2026-10-04/REPORT.md) records per-band decisions, independent mathematical/visual checks, all clean-ZIP rebuilds and physical-testing limits. Previous affected print PDFs and the complete previous source ZIP are separately archived in `archive-before-fresh-review-2026-10-04/` within their print/source folders. Bonus companions are separate; this base ZIP does not incorporate them. The theme remains **unpiloted** and can span several meetings.
