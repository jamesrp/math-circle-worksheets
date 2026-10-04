# Week 63 separate facilitator guide

Original authoring, October 4, 2026; version W63-G-v1. This standalone source corresponds to revised student W63-S-v2 (nine pages) and material W63-M-v2 (three pages). It changes neither packet. The guide has a theorem-first overview, complete P1-9 keys, all four-card intersections and all specified five-card intersection sizes, the complete 44-row adult catalog, reversible original-label constructions, exact base cases/domain, and a practical five-kit plan for eleven KK11 / 3333 / 445 children with three anchored adults. The first hour preserves deeper investigations for return visits. There is no independent K-1 packet.

## Portable build

From any directory, with Python 3 and TeX Live (`pdflatex`, `geometry`, `fontenc`, `helvet`, `amsmath`, `amssymb`, `array`, `booktabs`, `tabularx`, `fancyhdr`, `tikz`, `hyperref`):

```sh
python3 /absolute/path/to/guide/build.py --out /absolute/path/to/build-output
```

The output directory must be outside guide-src. It receives facilitator.pdf plus build intermediates. No repository files or student sources are required, and nothing is written into source. SOURCE_DATE_EPOCH is fixed by the builder for deterministic output. The complete authored source bundle is exactly this README, facilitator.tex, build.py and verify.py; no prompts, borrowed style exemplars, third-party books, reference PDFs or intermediate renders belong in it.

## Independent finite mathematical check

```sh
python3 verify.py --out /absolute/path/to/math.json
python3 verify.py --pdf /absolute/path/to/facilitator.pdf --out /absolute/path/to/math-and-pdf.json
```

The math-only mode needs Python's standard library. The actual-PDF mode additionally needs PyMuPDF (`pymupdf`); the project runtime `tmp/bonus-35-51-venv/bin/python` supplies it. This independently enumerates every permutation for n=0..6, every inclusive specified-home intersection, every per-outcome weight and subset-pair cancellation, and every distinguished-destination reciprocal/longer reduction and inverse. It directly checks the guide's literal catalogs, partial counts, arrow direction, non-task examples, E-at-A reduction table, source dimensions arithmetic and 223-piece kit count. It imports no student/research verifier or builder answer data. It checks the actual ten-page guide, page bounds, headers/version, and the printed catalogs; code is not evidence of physical or classroom readiness or a replacement for the general proofs in the guide.

## Sources and provenance

The author read the actual revised students.pdf/materials.pdf and all twelve fresh renders, their editable source, review.md, review-math.md, revision.md and independent math-qa evidence. Root README.md, AGENTS.md, REPUBLISHING.md, direct stage routing and Week 63 source notes/outline informed the scope. REPUBLISHING.md is preserved. The mathematical content was independently checked as above.

Primary math sources actually read locally: Alan Frieze, CMU Discrete Mathematics [D14 pp. 2-4](https://www.math.cmu.edu/~af1p/Teaching/DM/D14.pdf) and [D16 pp. 1-2, 4-7](https://www.math.cmu.edu/~af1p/Teaching/DM/D16.pdf), on derangements, reciprocal versus longer-cycle deletion, fixed-home intersections and inclusion-exclusion. No source figure or slide prose is copied into this guide.

Teaching passages actually consulted: Givental, Nemirovskaya and Zakharevich, *Math Circle by the Bay*, Preface printed viii-x / PDF 9-11; Rozhkovskaya, *Math Circles for Elementary School Students*, Lesson 3 “At the lesson,” item 1, EPUB OEBPS/part0013.xhtml, and Lesson 8 “At the lesson,” item 2, part0018.xhtml. The guide distinguishes those reported lessons from our age adaptations and forecasts. The source-notes' targeted prior-packet audit records Week 43 upper p. 3 P5's repeated BCA/CAB entry; four/five-card overlap correction and reversible derangement families supply the new direction. This guide does not claim to independently re-audit the full previous library.

## Verification and limits

Build/render/clean-copy/ZIP evidence is stored outside this source folder in the assigned run's guide-evidence folder. Inspect every actual final guide page, then require clean copied-source and ZIP-extracted-source builds to match extracted text, page dimensions and 144-dpi pixel bytes. Original source files only should enter a portable source ZIP. An independent root review remains required before release.

Card placement/bottom alignment, real-size cutting/fit, simultaneous grouping rings or multiple markers, deletion/restoration rehearsal, volunteer workload and classroom piloting remain **UNPERFORMED**. The preparation-time estimates and first-hour route are forecasts. This is a local guide for independent review; no publication, Drive upload, remote-current version or classroom success is claimed.

Package note: this README records the authored stage. External QA paths and
process-status descriptions are historical; current verification is recorded in
`plans/new-themes-52-63/week-NN/release-checks.json` in the repository. Use the
package root `python3 build.py --out output` to build every delivered PDF.
