# Nearest-site regions: Week 15 editable release

## Mathematical overview and examples revision

The guide now begins with a one-page mathematical overview: precise setting and hypotheses, main facts and limits, grade-band progression, and the distinction between experimentation, conjecture and proof. Original detailed solutions remain afterward, with guide-page references updated.

Only the adult guide changes. All three student PDFs are byte-identical to the reviewed revision that removed the older-band Problem 2 P/Q probes. Those probes remain absent. No numbered problem was added or removed. Student page counts are unchanged; the guide has one additional page.

Editable overview content is in `facilitator-src/mathematical-overview.tex`. Edit the student generator for the new examples; normal builds regenerate the supplied LaTeX. Reference PDFs and hashes describe this revision.

## October 3 revision

Grades 2–3 and grades 4–5 Problem 2 now asks only for the three nearest-site regions. Its P/Q probes and corresponding adult-key references have been removed. The three sites, all other student problems, and K–1 are unchanged. The adult key retains the explanation of why only nearest ties survive.

The PDFs in `reference-pdfs/` match this revised delivery. `build.sh` checks the current 46 student probes, and `verify_rebuild.py` compares all 39 rebuilt pages against these revised references. The existing narrative files in `review/` are historical records of the original release; their P/Q descriptions and 50-probe count describe that earlier version. `reference-pdf-sha256.txt` records the current revised files.

**New, unpiloted draft.** Week 15 is an unscheduled activity-library slot, not a calendar booking. The student workflow's writing, adversarial review, and revision stages are completed. Both required wording repairs were applied. The facilitator guide is a separate, untested teaching step with checked mathematical solutions; neither the lesson nor its proposed pacing has been classroom-tested. Prepared October 3, 2026.

## Print-ready PDFs

The four descriptive PDFs delivered alongside this ZIP are unchanged copies of the reviewed final outputs. Identical PDFs inside `reference-pdfs/` provide stable, read-only-by-convention release references for reproducibility checks:

- `k-1.pdf`: 8 US Letter pages, Problems 1–8, packet F15-K-v1.
- `grades-2-3.pdf`: 8 US Letter pages, Problems 1–8, packet F15-23-v1.
- `grades-4-5.pdf`: 8 US Letter pages, Problems 1–8, packet F15-45-v1.
- `facilitator-guide.pdf`: 15 US Letter pages; mathematical overview on page 1, preparation and adult reference on pages 2–3, K–1 solutions on 4–7, grades 2–3 on 8–11, and grades 4–5 on 12–15. All 24 problems have solutions, diagrams, reasoning, held hints, and optional extensions.

Print selected student pages **single-sided on US Letter at 100% / actual size**. The working maps are 5.8 inches square. Do not use the reduced adult answer diagrams as student measurement sheets. Start with one or two pages per child and keep the rest available; finishing every page is not the goal.

## Prerequisites and flexible entry

Grade labels are approximate starting points, not age restrictions. Choose by readiness and interest.

- K–1: compare two lengths and follow a spoken rule; an adult can read directions and scribe letters. No number reading, ruler arithmetic, or coordinate notation is required.
- Grades 2–3: compare several lengths, draw straight lines, and retain all tied nearest sites. Drawing and spoken explanation suffice; numerical measurement is optional.
- Grades 4–5: reason about entire regions, intersect allowed sides, and discuss possibility, impossibility, and a minimum. Algebra and formal proof notation are optional adult tools.

The mathematical progression is nearest-length comparisons → shared ties and whole regions → competition from a third site → insertion and inverse constructions. Sites are fixed, distinct points; straight-line distances go to their centers. The frame is a window on the plane unless a task explicitly restricts attention to it. Shared nearest ties belong to all tied sites.

For ten children, the preparation plan calls for pencils/erasers, straightedges, non-stretch string, foldable translucent paper, and spare Letter paper. Colors are optional. Quantities and the flexible one-hour plan are in the guide; they are proposals, not checked inventory or tested attendance.

## Contents and editing

- `src/build_packets.py`: editable student text, sites, probes, and diagram generator.
- `src/*.tex`: editable generated student LaTeX.
- `facilitator-src/build_guide.py`: editable guide text, exact constructions, and diagrams.
- `facilitator-src/facilitator-guide.tex`: editable generated guide LaTeX.
- `build.sh`: portable, two-pass build of all four PDFs into `build/`.
- `src/check_geometry.py` and `facilitator-src/check_solutions.py`: exact mathematical checks, PDF coverage/layout checks, and reference-file integrity checks.
- `verify_rebuild.py`: compare rebuilt PDFs with reference PDFs, page by page, by text and 100-dpi grayscale rendering.
- `outlines/nearest-site-regions.md`: mathematical kernels, prerequisites, source, and materials.
- `review/`: historical student-draft review, completed facilitator checks, release validation, and reference checksums.

Edit the Python generators for changes that should survive regeneration. The normal build regenerates the `.tex` files. To compile manual `.tex` edits without regeneration, use `bash build.sh --from-tex`. Mathematics checks are tied to this release's examples; update them deliberately if you change the problems or geometry. Reference PDFs and hashes should remain unchanged unless deliberately issuing a new reference release.

## Rebuild on a normal local installation

Requirements:

- Python 3.10 or later, with `pypdf` (`python3 -m pip install -r requirements.txt`).
- A working TeX Live or MacTeX installation providing `pdflatex`, TikZ/PGF, Latin Modern fonts, and the standard LaTeX packages `geometry`, `fontenc`, `amsmath`, `amssymb`, `fancyhdr`, `enumitem`, `hyperref`, and `textcomp`.
- Poppler's `pdftoppm` for the optional release comparison. `pdfinfo` is useful for inspection.

For example, typical Debian/Ubuntu packages are `texlive-latex-base texlive-latex-recommended texlive-latex-extra texlive-pictures lmodern poppler-utils`. A full MacTeX installation covers the TeX requirements; install Poppler separately if needed. Use your normal package manager and local Python environment.

From this directory:

```sh
python3 -m pip install -r requirements.txt
bash build.sh
python3 verify_rebuild.py
```

Set `PYTHON=/path/to/python` if needed. The build invokes ordinary `pdflatex` and uses the TeX distribution's normal configuration. There are no absolute project paths, downloaded dependencies, bundled TeX format files, or cloud-specific environment requirements. It does not modify the reference PDFs. Build logs and intermediate files stay under `build/` and are intentionally not included in this ZIP.

Optional visual review after editing:

```sh
mkdir -p build/preview
pdftoppm -r 100 -png build/facilitator-guide.pdf build/preview/guide
```

Inspect every newly generated page. Changed text or intentional geometry changes will make `verify_rebuild.py` fail against this release's unchanged references; that is expected until you deliberately establish a new reviewed release.

## Review status and sources

The student review examined all 24 pages, independently checked the geometry, and requested two narrow wording changes: every tied letter in K–1 Problem 4, and no point contact with C in grades 2–3 Problem 7. Both are in this release. The guide covers 24 problems with 24 equal-scale answer diagrams. Exact independent checks cover 82 site cells and 46 current student probe points, alongside the constructive and impossibility arguments. See `review/release-validation.md` for the copied-source rebuild and rendering checks.

The primary mathematical reference is David M. Mount, *CMSC 754 Lecture 10: Voronoi Diagrams and Fortune's Algorithm*, Fall 2021, pages 1–3: https://www.cs.umd.edu/class/fall2021/cmsc754/Lects/lect10-vor.pdf. This activity uses closed cells and intentionally includes a four-way tie. Pedagogical consultation is identified on guide page 3. Third-party books, PDFs, downloads, caches, renders, and TeX format binaries are not included in this source bundle.

## Review guidance addendum

See [the approved review guidance addendum](AGENTS-review-guidance.md) when editing this material. It supplements any existing AGENTS.md.
