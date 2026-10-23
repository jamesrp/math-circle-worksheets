# Week 34 Hidden turns editable source — current editable source

**Card fixes, October 23, 2026 (v3).** The review card's shoulds 1-5 and coulds 6-10 (`plans/review/week-34.md`): page 1's example adds a flip panel with its axis drawn and draws every arrow from the start; the rules say "Turn or flip (turn over)" and "neighbors may be the same kind" and drop the symbol-direction clause; every goal reads "a pattern that no turn or flip can match"; K-1 Problem 1 asks for a pattern the partner cannot match; Grades 2-3 Problem 1 drops "Use up to three kinds"; Grades 4-5 get a sixth page of extra workspace for Problem 5 (a seven-ring and a nine-ring). The guide says how to make a coloured tracing copy, with coloured pencils and about ten sheets per pair, makes one in the launch, plans eleven children and a 35-40 minute table time, and keys the kind swap (K-1 P6) and the odd-ring witnesses. Could 11 (the route note repeating page 2's routes) is left for the organizer. Checked by `plans/review/checks/week-34/check_card_fixes.py`. The v2 PDFs and the conversion ZIP are archived in `archive-before-card-fixes-2026-10-23/` here and in the print folder.

**Problem files, October 23, 2026.** The student packets are stored as [problem files](../problem-files/README.md): `week.toml`, `figures.py` (the old builder's drawing code and page template, unchanged) and one file per problem in `problems/`, with each band's wording inside it. The conversion changed no wording or figure: the rebuilt LaTeX is byte-identical to the previous builder's, and `compare.py` finds the same text and no differing pixel at 100 dpi against the print copies. The previous builder (`build_packets.py`) and the October 4 source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md); its finite checks run unchanged as `editable/src/check_distinguishing.py`.

- **Student pages:** edit `problems/*.md` (figures in `figures.py`), then build and compare:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-34 --out tmp/week-34-views --tex
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-34-views lowell-math-circle-year-2/week-34 week-34
  ```

- **Adult guide:** its source is still `editable/facilitator-src/guide.md` with `route-note.json`, built by the package. The problem files carry each problem's one-sentence idea (`kernel`), not its answers.
- **Portable package:** `editable/` is the package; `editable/src/regenerate.py` writes the student LaTeX from the problem files, and the package build runs it before compiling. The portable source ZIP holds the package plus the problem files and tools in `problem-files/`, written by `package.py`:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-34 --zip symmetry-breaking-week34-editable-source.zip --top symmetry-breaking-week34-source
  ```

The [portable base source ZIP](symmetry-breaking-week34-editable-source.zip) and [complete extracted package](editable/README.md) contain the current **October 23, 2026 card-fix revision (v3)**, built on the October 4 fresh-review revision. Current print copies are in [../../week-34/](../../week-34/). References are exact duplicates of those print PDFs.

Read `editable/README.md` for dependencies and commands. Copy the complete package to a fresh folder under the project's `tmp/` before rebuilding; keep intermediates out of current print/source folders. `verify_revision.py` checks current pages; since the card fixes changed every student packet, it allows no alternate hashes. The original strict verifier remains available. Every packet and the guide reproduce exact 100-dpi pixels from the extracted ZIP.

The [corpus revision report](../../../plans/fresh-review-revision-2026-10-04/REPORT.md) records per-band decisions, independent mathematical/visual checks, all clean-ZIP rebuilds and physical-testing limits. Previous affected print PDFs and the complete previous source ZIP are separately archived in `archive-before-fresh-review-2026-10-04/` within their print/source folders. Bonus companions are separate; this base ZIP does not incorporate them. The theme remains **unpiloted** and can span several meetings.
