# Week 60 adult guide: Take it or pass

Separately authored adult guide for the final seven-page student packet W60-S-v2.
Guide footer: W60-FAC-v1. Eight US Letter pages. The concrete student route is
pages 1-3 and 6, Grades 3-5; pages 4-5 and 7 are readiness-dependent upper
continuations or return visits. KK11 uses separate prior tiling; no new K-1
stopping theme is claimed. Physical rehearsal and classroom piloting are unperformed.

## Portable build

```sh
python3 build.py /absolute/path/to/output-directory
python3 check_answers.py
python3 check_pdf.py /absolute/path/to/output-directory/facilitator.pdf
```

The output directory must be outside this source directory. The build writes
facilitator.pdf and its .guide-build/ intermediates there. Mathematical checking
uses Python 3's standard library; check_pdf.py needs PyMuPDF and Pillow. In this
repository the supplied runtime is tmp/bonus-35-51-venv/bin/python. Required
standard TeX Live packages: pdfLaTeX, article, geometry, T1 fontenc, helvet,
amsmath, amssymb, array, booktabs, enumitem, TikZ/arrows.meta, fancyhdr, hyperref.
No external fonts, images, books, network or repository-relative files are needed.

All figures are original editable TikZ. build.py rejects output inside source
and rejects overfull TeX boxes. check_pdf.py renders every page, checks text
bounds/header/footer/problem coverage, copies these six authored source files
to a new directory, and creates/extracts a lean six-file source ZIP. The two
clean builds must reproduce identical text, page dimensions and every rendered
pixel at 1.7 scale. The mathematical checker is rerun from extracted source.
QA ZIPs, renders, evidence and intermediates stay in the output's guide-qa/,
outside source. Visual inspection remains required in addition to these checks.

## Independent mathematics

check_answers.py was written from the final student pages. It imports no student
author or reviewer code/results. It recomputes both worked conventions, the
non-target average example, complete policy score lists and case totals, opposite
six-round match constructions, all 8 two-offer and 4096 three-offer deterministic
history policies for each of the three actual bags, and the exact recurrence.
At four offers it audits 512 current-score/turn policies; it does not enumerate
the 2^39 full-history policies. The induction in the guide establishes that
stronger bound. General extra-offer examples include 125 bags with duplicate and
negative scores through six horizons; they support the proof rather than replace it.

To additionally verify the printed source packet's complete ordered cards and
position counters, use the optional PDF-dependent audit:

```sh
python3 check_answers.py --students /path/to/students.pdf --out /path/to/answers.json
```

The actual seven-page final student PDF was read and inspected in this guide
stage. Its card collections have 9, 27, 9 and 9 full words. Keeping full words,
unseen suffixes and multiplicities is essential to equal-weight comparison.

The guide gives exact current-roster preparation counts, single-record handling,
after-decision counter timing, table-pooling, saved labelled totals before erasing,
physical pretests and multiple-visit pacing. Material/staffing estimates are
proposals, not rehearsal results. Root independently reviews the guide before
release; release placement and combined source packaging belong to root.

## Provenance and package boundary

See provenance.md for exact primary mathematical and teaching references, read
locally, and the boundary between source observations and our proposed adaptations.
This source bundle contains only six authored files: facilitator.tex, build.py,
check_answers.py, check_pdf.py, README.md and provenance.md. It excludes prompts,
style exemplars, third-party books/reference PDFs, copied source figures and renders.
REPUBLISHING.md was read and left unchanged. No student page, prior week, workflow,
global index or remote copy is edited by this guide stage.

Package note: this README records the authored stage. External QA paths and
process-status descriptions are historical; current verification is recorded in
`plans/new-themes-52-63/week-NN/release-checks.json` in the repository. Use the
package root `python3 build.py --out output` to build every delivered PDF.
