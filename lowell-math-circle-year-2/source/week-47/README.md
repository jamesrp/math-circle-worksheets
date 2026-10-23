# Week 47 Gentle step landscapes editable source — current editable source

**Problem files, October 23, 2026.** The student packets are stored as [problem files](../problem-files/README.md): `week.toml`, `figures.py` (the old builder's drawing code; the pages use the house canvas template) and one file per problem in `problems/`, with each band's wording inside it. The conversion changed no wording or figure: the rebuilt LaTeX is byte-identical to the old builder's, the three PDFs are pixel-identical to the old builder's compiled on the same machine, and against the print PDFs `compare.py` finds identical pages and text, with the same 0, 48 and 21 differing pixels at most per page (K–1, 2–3, 4–5) that the old builder itself gives there. The previous builder (`make.py`, `draw.py`, `examples.py`) and the ZIP it came in are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

- **Student pages:** edit `problems/*.md` (figures in `figures.py`), then build every view:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-47 --out tmp/week-47-views --tex --publish lowell-math-circle-year-2/band-views/week-47
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-47-views lowell-math-circle-year-2/week-47 week-47
  ```

  The first-route and return packets, the one-page problem menu and the key of each problem's idea are published in [band-views/week-47/](../../band-views/README.md#weeks-stored-as-problem-files).
- **Adult guide:** its source is still `editable/facilitator-src/content.json` (ReportLab) with `route-note.json`, built by the package.
- **Portable package:** `editable/` is the package; `editable/src/regenerate.py` writes the student LaTeX from the problem files, and the package build runs it before compiling. The [portable source ZIP](gentle-step-landscapes-week47-editable-source.zip) holds the package plus the problem files and tools in `problem-files/`. Rebuild it with `python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-47 --zip gentle-step-landscapes-week47-editable-source.zip --top gentle-step-landscapes-week47-source` and check a clean rebuild from the extracted ZIP (`python3 build.py`, then `python3 verify_revision.py`).

The [portable base source ZIP](gentle-step-landscapes-week47-editable-source.zip) and [complete extracted package](editable/README.md) contain the current **October 4, 2026 fresh-review revision**. Current print copies are in [../../week-47/](../../week-47/). References are exact duplicates of those print PDFs.

Read `editable/README.md` for dependencies and commands. Copy the complete package to a fresh folder under the project's `tmp/` before rebuilding; keep intermediates out of current print/source folders. `verify_revision.py` checks current pages and permits only specifically audited full-page alternate hashes for pre-existing font/hyphenation differences in unchanged student packets; the original strict verifier remains available. Every changed packet and guide reproduces exact 100-dpi pixels from the extracted ZIP.

The [corpus revision report](../../../plans/fresh-review-revision-2026-10-04/REPORT.md) records per-band decisions, independent mathematical/visual checks, all clean-ZIP rebuilds and physical-testing limits. Previous affected print PDFs and the complete previous source ZIP are separately archived in `archive-before-fresh-review-2026-10-04/` within their print/source folders. Bonus companions are separate; this base ZIP does not incorporate them. The theme remains **unpiloted** and can span several meetings.
