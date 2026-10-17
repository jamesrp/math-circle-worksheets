# Week 95: Count the unseen — review draft

Two student packets, for Grades 2–3 and 4–5, plus a theorem-first facilitator guide. The guide states assumptions and limits, preparation, a brief shared demonstration, flexible routes, all answers, proofs, hints and return visits. There is no forced K–1 version. All material is unpiloted; physical preparation, marking, mixing, resetting and classroom timing have not been rehearsed. Organizer review is pending.

## Build

Python 3 standard library and pdfLaTeX/TeX Live are required, with TikZ, Latin Modern, geometry, array, fancyhdr, amsmath/amssymb and hyperref. No runtime downloads or private reference inputs are required.

From this folder:

```sh
python3 build.py --out ../../week-95 --work ../../../tmp/week95-build
```

After extracting the portable ZIP:

```sh
python3 week-95/build.py --out rebuilt --work tmp/build
```

The builder creates `week-95-grades-2-3.pdf`, `week-95-grades-4-5.pdf` and `week-95-facilitator.pdf`; it rejects TeX errors and overfull boxes and runs independent mathematics checks. Fixed PDF metadata permits byte-identical clean rebuilds. Build intermediates belong in `tmp`, not the editable sources.

`student/build.py` contains editable student text and vector diagrams; its independent builder accepts `--output-dir`. `guide/facilitator.tex` is the editable guide. `check_math.py` is the independent reviewer's exact checker. `SOURCES.md`, `QA.md` and `revision-response.md` record attribution and review. Full reviews and production provenance are retained in the repository's `plans/new-families-92-97/week-95/`.

Print US Letter, single-sided. Student diagrams illustrate operations and are not cutouts. Use identical counters or cards with marks that can be seen but not detected by touch. See the guide for kit counts, how to hold a population fixed, resetting, and the distinction between blind sampling and deliberately arranging a legal possible record. Keep the deep allocation and model-testing problems for children who are ready, including return visits.

Only owned teaching and build/check sources are bundled. Downloaded books, workflow exemplar excerpts, generated prompt copies, private records, caches and PDFs are excluded from the source ZIP.
