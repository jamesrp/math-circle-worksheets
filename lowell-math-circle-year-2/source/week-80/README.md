# Week 80: Midnight laboratory — organizer-approved

Grades 2–3 folding/motion; Grades 3–5 endpoint discussion. A selected-band menu, not a requirement to finish every page in one session. All activities are unpiloted; physical fit, actual-size printing, timing and classroom procedures have not been rehearsed. The theorem-first guide gives assumptions, preparation, launch, first route, solutions, hints and return visits.

## Build the two PDFs

Python 3 (standard library) and pdfLaTeX/TeX Live are required, with TikZ, geometry, fancyhdr, helvet, lmodern, amsmath/amssymb, parskip and hyperref. No font, book, binary, image asset or Python package is bundled.

From this folder, run:

```sh
python3 build.py --out ../../week-80
```

After extracting the portable ZIP, run `python3 week-80/build.py --out rebuilt --work tmp/build`. Paths are resolved against your current directory. Both commands also run the independent mathematical checker. The builder rejects TeX errors and overfull boxes. Intermediates and check evidence go into repository `tmp/` or the supplied `--work` folder; generated files are not source inputs.

## Contents and lineage

- `student/students.tex`: final 5-page student/material draft, created by a fresh writer then revised by a separate agent after independent adversarial and mathematical reviews.
- `guide/facilitator.tex`: separate facilitator step, revised and independently reviewed. This guide-authoring step is untested as a classroom workflow.
- `check_math.py`: portable copy/adaptation of the independent mathematical checker's code; finite computation supports the proofs in the guide.
- `build.py`: both-PDF deterministic builder; [SOURCES.md](SOURCES.md) records attribution.

Print US Letter, single-sided, Actual Size. Cut only the material pages needed for the selected route; preparation details are in the guide. Printable PDFs live in `../../week-80/`. The mobile review index links each PDF individually.

ZIPs contain only owned teaching/build/check sources. Generated stage prompts and borrowed workflow style excerpts remain local and are excluded. No new open research problem is claimed solved, and no Lean certification is claimed.

## October 15 review revision

The opening is grounded in a light OFF at 11:00 p.m., ON at 11:30 and OFF at 11:45. Time-strip labels use clock times; START/END remain only on the separate position strip. Infinite alternation and the unspecified midnight endpoint are unchanged.

See [QA.md](QA.md) for digital checks and independent review. The changes remain unpiloted.

Organizer promotion: October 17, 2026, after review of the current packet. The student and facilitator PDFs are unchanged. Unpiloted; physical preparation, timing and classroom procedures remain untested.
