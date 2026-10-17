# Week 82: Endless class lines — organizer-approved

Grades 3–5; infinite-rule and order reasoning. A selected-band menu, not a requirement to finish every page in one session. All activities are unpiloted; physical fit, actual-size printing, timing and classroom procedures have not been rehearsed. The theorem-first guide gives assumptions, preparation, launch, first route, solutions, hints and return visits.

## Build the two PDFs

Python 3 (standard library) and pdfLaTeX/TeX Live are required, with TikZ, geometry, fancyhdr, helvet, lmodern, amsmath/amssymb, parskip and hyperref. No font, book, binary, image asset or Python package is bundled.

From this folder, run:

```sh
python3 build.py --out ../../week-82
```

After extracting the portable ZIP, run `python3 week-82/build.py --out rebuilt --work tmp/build`. Paths are resolved against your current directory. Both commands also run the independent mathematical checker. The builder rejects TeX errors and overfull boxes. Intermediates and check evidence go into repository `tmp/` or the supplied `--work` folder; generated files are not source inputs.

## Contents and lineage

- `student/students.tex`: final 6-page student/material draft, created by a fresh writer then revised by a separate agent after independent adversarial and mathematical reviews.
- `guide/facilitator.tex`: separate facilitator step, revised and independently reviewed. This guide-authoring step is untested as a classroom workflow.
- `check_math.py`: portable copy/adaptation of the independent mathematical checker's code; finite computation supports the proofs in the guide.
- `build.py`: both-PDF deterministic builder; [SOURCES.md](SOURCES.md) records attribution.

Print US Letter, single-sided, Actual Size. Cut only the material pages needed for the selected route; preparation details are in the guide. Printable PDFs live in `../../week-82/`. The mobile review index links each PDF individually.

ZIPs contain only owned teaching/build/check sources. Generated stage prompts and borrowed workflow style excerpts remain local and are excluded. No new open research problem is claimed solved, and no Lean certification is claimed.

## October 15 review revision

The opening contrasts an order-preserving five-to-five complete match, a crossed five-to-five complete match, and an impossible five-to-six complete match. Labels are identifiers, not matching constraints. Problem 3 D is one horizontal concatenation of endless red and endless blue rows; Problem 2 retains its distinct prepended/appended star pictures.

See [QA.md](QA.md) for digital checks and independent review. The changes remain unpiloted.

## October 17 organizer feedback

The accepted matching diagrams now use two classes of kids lining up, with the organizer's opening wording. The identifier-only convention first appears in Problem 2. Removed only the former student page 5 (four continuation-strip cutouts); Problems 1–4 and their workspaces remain, and the remaining cards/panels are now pages 5–6. The guide describes drawing continuation arrows on blank paper. This revision is organizer-approved and promoted following the organizer’s “LGTM” approval. The accepted student and facilitator PDFs are unchanged. Unpiloted; physical preparation and procedures remain untested.
