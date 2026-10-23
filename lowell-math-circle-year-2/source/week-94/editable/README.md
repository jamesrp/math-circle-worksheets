# Week 94: Calibration lab — review draft

Three student packets: a short two-page K–1 entry, four pages for Grades 2–3, and five pages for Grades 4–5. The five-page theorem-first facilitator guide gives assumptions, preparation, a brief shared launch, first routes, all answers, proofs, hints and return visits. All are unpiloted; printing, cutting, handling, timing and classroom procedures have not been physically rehearsed. Organizer review is pending.

## Build

Python 3.11 or later (standard library only) and pdfLaTeX/TeX Live are required, with TikZ, Latin Modern, geometry, array, fancyhdr, amsmath/amssymb and hyperref. No runtime download or private reference is required.

From this folder:

```sh
python3 build.py --out ../../../week-94 --work ../../../../tmp/week94-build
```

After extracting the portable ZIP:

```sh
python3 week-94/build.py --out rebuilt --work tmp/build
```

The builder creates `week-94-k-1.pdf`, `week-94-grades-2-3.pdf`, `week-94-grades-4-5.pdf`, and `week-94-facilitator.pdf`; it rejects TeX errors and overfull content and runs the independent mathematics checker. Fixed PDF metadata makes clean rebuilds byte-identical. Build logs and intermediates belong in `tmp`, not the editable sources.

## Sources and lineage

- `student/`: the student LaTeX and its independent standalone builder, drafted and revised in separate agents after fresh adversarial and mathematics reviews. Since October 23, 2026 `k-1.tex`, `grades-2-3.tex` and `grades-4-5.tex` are written from the problem files by `student/regenerate.py` (in the repository `../week.toml`, `../template.tex` and `../problems/`; in the ZIP `problem-files/`, with the tools in `problem-files/tools/`); `build.py` runs it first. Edit the problem files, not the `.tex` files.
- `reference-pdfs/`: copies of the current print PDFs.
- `guide/facilitator.tex`: separate guide-authoring step; its final student/guide review is recorded in `QA.md`. This workflow step is untested in class.
- `check_math.py`: portable standard-library checker written by the independent mathematics reviewer.
- `SOURCES.md`, `QA.md`, `revision-response.md`: source attribution and digital verification record.

Print US Letter, single-sided, Actual Size. Printed units are 12 mm; the guide gives exact kit quantities and cutting instructions. The K–1 entry is intentionally short; the upper noise-design page is a readiness-dependent continuation. Commercial cubes are counting objects, not guaranteed to fit the paper scale.

Only owned teaching and build/check sources are bundled. Downloaded books, workflow exemplar excerpts, generated prompt copies, private records, caches and PDFs are excluded from the ZIP.
