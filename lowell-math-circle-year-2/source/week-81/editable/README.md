# Week 81: Buckets of Fish — organizer-approved draft-v1, revised v2

Grades 2–3 capped games; Grades 4–5 uncapped continuation; an adult-led K–1 route in the guide. A selected-band menu, not a requirement to finish every page in one session. All activities are unpiloted; physical fit, actual-size printing, timing and classroom procedures have not been rehearsed. The theorem-first guide gives assumptions, preparation, launch, first route, solutions, hints and return visits.

## Build the two PDFs

Python 3 (standard library) and pdfLaTeX/TeX Live are required, with TikZ, geometry, fancyhdr, helvet, lmodern, amsmath/amssymb, parskip and hyperref. No font, book, binary, image asset or Python package is bundled.

From this folder, run:

```sh
python3 build.py --out ../../../week-81
```

After extracting the portable ZIP, run `python3 week-81/build.py --out rebuilt --work tmp/build`. Paths are resolved against your current directory. Both commands first write `student/students.tex` from the problem files, then build, then run the independent mathematical checker. The builder rejects TeX errors and overfull boxes. Intermediates and check evidence go into repository `tmp/` or the supplied `--work` folder; generated files are not source inputs.

## Contents and lineage

- Student pages: stored as problem files since October 23, 2026 (in the repository `../week.toml`, `../template.tex` and `../problems/`; in the ZIP `problem-files/`, with the tools in `problem-files/tools/`). `student/regenerate.py` writes `student/students.tex` from them; edit the problem files, not `students.tex`. The packet: final 5-page student/material draft, created by a fresh writer then revised by a separate agent after independent adversarial and mathematical reviews.
- `reference-pdfs/`: copies of the current print PDFs.
- `guide/facilitator.tex`: separate facilitator step, revised and independently reviewed. This guide-authoring step is untested as a classroom workflow.
- `check_card_fixes.py`: checks the keys, starts and wording changed by the October 23 card fixes; the build runs it after `check_math.py`.
- `check_math.py`: portable copy/adaptation of the independent mathematical checker's code; finite computation supports the proofs in the guide.
- `build.py`: both-PDF deterministic builder; [SOURCES.md](SOURCES.md) records attribution.

Print US Letter, single-sided, Actual Size. Cut only the material pages needed for the selected route; preparation details are in the guide. Printable PDFs live in `../../../week-81/`. The mobile review index links each PDF individually.

ZIPs contain only owned teaching/build/check sources. Generated stage prompts and borrowed workflow style excerpts remain local and are excluded. No new open research problem is claimed solved, and no Lean certification is claimed.

## October 15 review revision

All small starting boxes and sorting cards show counters, including empty boxes for zero. The five-page packet omits the former blank quantity-card page. Written finite quantities remain permitted during upper-level play; rules and all printed starting positions are unchanged.

See [QA.md](QA.md) for digital checks and independent review. The changes remain unpiloted.

Organizer promotion: October 17, 2026, after review of the draft-v1 packet. Unpiloted; physical preparation, timing and classroom procedures remain untested.

## October 23 card fixes (v2), after the organizer's approval

From the review card (`plans/review/week-81.md`), made after the organizer's October 17 approval and not yet re-approved. A critic's follow-up the same day made W81-S-v3 (Problem 5's (0, 3) picture in the P1–P3 style) and W81-FAC-v2 (a footer id and the K–1 rule "Take one. If you took it from bucket 2, you may put one in bucket 1."). Student pages: page 1's cap names the left side one way; Problem 3 starts from (2, 0, 2) instead of repeating Problem 1's (2, 2, 2); Problem 5 starts from each of two pictures, (0, 3) drawn like Problem 4's beside (1, 1, 1), and asks for an explanation only if a child thinks every game ends; the footer is W81-S-v2. Guide: the corrected repair move; the Grades 4–5 route on pages 1 and 2; a K–1 route; the cap in the launch; "written count" for "count card"; keys for (2, 0, 2) and (0, 3); a capped longest-game return visit (7 moves from (1, 1, 1) with a cap of one); the header "Adult guide". Unpiloted.
