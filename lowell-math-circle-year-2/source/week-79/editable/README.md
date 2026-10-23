# Week 79: Numbered-ball detectives — revised after organizer approval

**Promoted after organizer review on October 15, 2026; revised October 23, 2026 (v2) from the review card, after that approval.** The approved version is archived in `../../../week-79/archive-organizer-approved-2026-10-15/`.

Grades 2–3 concrete core; Grades 4–5 eventual-membership continuation. A selected-band menu, not a requirement to finish every page in one session. All activities are unpiloted; physical fit, actual-size printing, timing and classroom procedures have not been rehearsed. The theorem-first guide gives assumptions, preparation, launch, first route, solutions, hints and return visits.

October 17, 2026: corrected only the guide page 3 hint to name Problem 4's smallest-card rule, with a card-1 contrast for Problem 3. The student packet is unchanged. Organizer promotion and unpiloted status are unchanged.

October 23, 2026 (v2, 79-ST-v2, 6 pages): Problem 2 asks for the day each card enters A as well as the day it moves to B, with both blanks under each card; a new Problem 4 (Grades 2–5, its own page) lets children choose each move and asks which of three six-card sets B can hold; the old Problem 4 is now Problem 5 and says "card" for "label". The guide adds the changed-rule answer to Problem 5's finite-day question, Problem 4's answers and counting condition, both rules side by side in Problem 3 (one extra card sheet and mat per table), a K–1 route, a corrected band map, the Ross–Littlewood name and the header "Adult guide". `check_math.py` checks Problem 4 by exhaustive search through day 7. This revision post-dates the organizer's approval.

## Build the two PDFs

Python 3.11 or later (standard library) and pdfLaTeX/TeX Live are required, with TikZ, geometry, fancyhdr, helvet, lmodern, amsmath/amssymb, parskip and hyperref. No font, book, binary, image asset or Python package is bundled.

From this folder, run:

```sh
python3 build.py --out ../../../week-79
```

After extracting the portable ZIP, run `python3 week-79/build.py --out rebuilt --work tmp/build`. Paths are resolved against your current directory. Both commands first write `student/students.tex` from the problem files, then build, then run the independent mathematical checker. The builder rejects TeX errors and overfull boxes. Intermediates and check evidence go into repository `tmp/` or the supplied `--work` folder; generated files are not source inputs.

## Contents and lineage

- Student pages: stored as problem files since October 23, 2026 (in the repository `../week.toml`, `../template.tex` and `../problems/`; in the ZIP `problem-files/`, with the tools in `problem-files/tools/`). `student/regenerate.py` writes `student/students.tex` from them; edit the problem files, not `students.tex`. The 6-page student/material packet (5 pages before October 23) was created by a fresh writer, then revised by a separate agent after independent adversarial and mathematical reviews.
- `reference-pdfs/`: copies of the current print PDFs.
- `guide/facilitator.tex`: separate facilitator step, revised and independently reviewed. This guide-authoring step is untested as a classroom workflow.
- `check_math.py`: portable copy/adaptation of the independent mathematical checker's code; finite computation supports the proofs in the guide.
- `build.py`: both-PDF deterministic builder; [SOURCES.md](SOURCES.md) records attribution.

Print US Letter, single-sided, Actual Size. Cut only the material pages needed for the selected route; preparation details are in the guide. Printable PDFs live in `../../../week-79/`. The mobile review index links each PDF individually.

ZIPs contain only owned teaching/build/check sources. Generated stage prompts and borrowed workflow style excerpts remain local and are excluded. No new open research problem is claimed solved, and no Lean certification is claimed.
