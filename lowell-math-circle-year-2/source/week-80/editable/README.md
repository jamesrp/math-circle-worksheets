# Week 80: Midnight laboratory — organizer-approved v1, revised v2

Grades 2–3 folding, motion and rule design (Problems 1–3); Grades 4–5 endpoint discussion (Problems 4–6); an adult-led K–1 route in the guide. A selected-band menu, not a requirement to finish every page in one session. All activities are unpiloted; physical fit, actual-size printing, timing and classroom procedures have not been rehearsed. The theorem-first guide gives assumptions, preparation, launch, first route, solutions, hints and return visits.

## Build the two PDFs

Python 3 (standard library) and pdfLaTeX/TeX Live are required, with TikZ, geometry, fancyhdr, helvet, lmodern, amsmath/amssymb, parskip and hyperref. No font, book, binary, image asset or Python package is bundled.

From this folder, run:

```sh
python3 build.py --out ../../../week-80
```

After extracting the portable ZIP, run `python3 week-80/build.py --out rebuilt --work tmp/build`. Paths are resolved against your current directory. Both commands first write `student/students.tex` from the problem files, then build, then run the independent mathematical checker. The builder rejects TeX errors and overfull boxes. Intermediates and check evidence go into repository `tmp/` or the supplied `--work` folder; generated files are not source inputs.

## Contents and lineage

- Student pages: stored as problem files since October 23, 2026 (in the repository `../week.toml`, `../template.tex` and `../problems/`; in the ZIP `problem-files/`, with the tools in `problem-files/tools/`). `student/regenerate.py` writes `student/students.tex` from them; edit the problem files, not `students.tex`. The packet: 6 pages since the October 23 revision (5 pages before), created by a fresh writer then revised by a separate agent after independent adversarial and mathematical reviews.
- `reference-pdfs/`: copies of the current print PDFs.
- `guide/facilitator.tex`: separate facilitator step, revised and independently reviewed. This guide-authoring step is untested as a classroom workflow.
- `check_card_fixes.py`: checks the keys, sizes and wording changed by the October 23 card fixes; the build runs it after `check_math.py`.
- `check_math.py`: portable copy/adaptation of the independent mathematical checker's code; finite computation supports the proofs in the guide.
- `build.py`: both-PDF deterministic builder; [SOURCES.md](SOURCES.md) records attribution.

Print US Letter, single-sided, Actual Size. Cut only the material pages needed for the selected route; preparation details are in the guide. Printable PDFs live in `../../../week-80/`. The mobile review index links each PDF individually.

ZIPs contain only owned teaching/build/check sources. Generated stage prompts and borrowed workflow style excerpts remain local and are excluded. No new open research problem is claimed solved, and no Lean certification is claimed.

## October 15 review revision

The opening is grounded in a light OFF at 11:00 p.m., ON at 11:30 and OFF at 11:45. Time-strip labels use clock times; START/END remain only on the separate position strip. Infinite alternation and the unspecified midnight endpoint are unchanged.

See [QA.md](QA.md) for digital checks and independent review. The changes remain unpiloted.

Organizer promotion: October 17, 2026, after review of the v1 packet. Unpiloted; physical preparation, timing and classroom procedures remain untested.

## October 23 card fixes (v2), after the organizer's approval

From the review card (`plans/review/week-80.md`), made after the organizer's October 17 approval and not yet re-approved. Student pages: a new Grades 2–5 Problem 3 (a card rule that settles, a counter rule that does not get closer and closer to one place), so the old Problems 3–5 are now 4–6; Problem 2's last question is "Does the counter get closer and closer to one place?"; Problem 4 drops "Use the card and switching marks to support your answer." and its MIDNIGHT box is 80 × 58 mm, larger than the 76 × 54 mm card; Problem 5 begins "The switches before midnight stay the same." Guide: the overview states Problem 3's facts and the band map; preparation names a counter at most 15 mm across, scissors and glue, and copying the folded marks onto Problem 1's line; the launch adds one counter move; the route is Problems 1–3 for Grades 2–3 and Problems 4–6 as a Grades 4–5 continuation; a K–1 route uses pages 1 and 6 with an adult; the answers add Problem 3's key, Problem 4's answer and the "flip once more"/"stay as it was" obstacle; "six drawings" is "four drawings"; author-facing lines are cut; the header is "Adult guide". Unpiloted.
