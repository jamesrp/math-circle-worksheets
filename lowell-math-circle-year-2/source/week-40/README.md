# Week 40 Loop color certificates editable source — current editable source

**Review-card fixes, October 23, 2026 (v3).** The keep card's shoulds 1–12 and coulds 13–17 ([plans/review/week-40.md](../../../plans/review/week-40.md)) were made in the problem files and the guide after the conversion: Problem 1 counts the figure-eight's arcs in every band, K–1 has the missing colors as Problem 2, the end dot R is S, the two-crossing move has a nine-row table, grades 4–5 check a curl and a slide before the certificate and color a drawn figure-eight, and the guide has one 40-minute route per band, cords tagged A–D, taped joins and crossing referees. See [editable/review/card-shoulds-2026-10-23.md](editable/review/card-shoulds-2026-10-23.md). The v2 PDFs and the conversion ZIP are archived in `archive-before-card-fixes-2026-10-23/` in the print and source folders.

**Problem files, October 23, 2026.** The student packets are stored as [problem files](../problem-files/README.md): `week.toml`, `figures.py` (the old builder's drawing code and page template, unchanged) and one file per problem in `problems/`, with each band's wording inside it. The conversion changed no wording or figure: the rebuilt LaTeX is byte-identical to the previous builder's, and the rebuilt PDFs match the print PDFs in pages, text and 100-dpi pixels. The previous builder (`make_packets.py`, `common.py`) and source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

- **Student pages:** edit `problems/*.md` (figures in `figures.py`), then build and compare:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-40 --out tmp/week-40-views --tex
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-40-views lowell-math-circle-year-2/week-40 week-40
  ```
- **Adult guide:** its source is still in `editable/facilitator-src/`, built by the package. The problem files carry each problem's one-sentence idea (`kernel`), not its answers.
- **Portable package:** `editable/` is the package; `editable/src/regenerate.py` writes the student LaTeX from the problem files, and the package build runs it before compiling. The [portable source ZIP](loop-color-certificates-week40-editable-source.zip) holds the package plus the problem files and tools in `problem-files/`, written by `package.py`:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-40 --zip loop-color-certificates-week40-editable-source.zip --top loop-color-certificates-week40-source
  ```

  Rebuild it after any change and check a clean rebuild from the extracted ZIP (`python3 build.py` in the extracted folder, then `python3 verify_revision.py`).

The [portable base source ZIP](loop-color-certificates-week40-editable-source.zip) and [complete extracted package](editable/README.md) contain the current **October 23, 2026 review-card revision (v3)**. Current print copies are in [../../week-40/](../../week-40/). References are exact duplicates of those print PDFs.

Read `editable/README.md` for dependencies and commands. Copy the complete package to a fresh folder under the project's `tmp/` before rebuilding; keep intermediates out of current print/source folders. `verify_revision.py` and `verify.py` check every page against `editable/reference-pdfs/`; since v3 every packet and the guide reproduce exact 100-dpi pixels from the extracted ZIP, so no font alternates are allowed.

The [corpus revision report](../../../plans/fresh-review-revision-2026-10-04/REPORT.md) records per-band decisions, independent mathematical/visual checks, all clean-ZIP rebuilds and physical-testing limits. Previous affected print PDFs and the complete previous source ZIP are separately archived in `archive-before-fresh-review-2026-10-04/` within their print/source folders. Bonus companions are separate; this base ZIP does not incorporate them. The theme remains **unpiloted** and can span several meetings.
