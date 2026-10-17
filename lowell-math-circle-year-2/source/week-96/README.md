# Week 96: Prime bags and divisor builders

Review draft, awaiting organizer review. Unpiloted; physical preparation, actual-size printing, adult procedures and timing have not been rehearsed. Two student packets: grades 2–3 and 4–5. Equal groups and supported multiplication are entry prerequisites; divisor counting and completeness are deeper continuations. No K–1 coverage is claimed. The guide gives a manageable first route and return visits; completing every page in one hour is not the goal.

## Rebuild

Requires Python 3 standard library and TeX Live/pdfLaTeX with TikZ, geometry, fancyhdr, lmodern, amsmath and hyperref. No external font, image, paper, book or Python dependency is bundled.

```sh
python3 build.py --out ../../week-96
```

From an extracted portable archive:

```sh
python3 week-96/build.py --out rebuilt --work tmp/build
```

The builder runs the independent mathematical checks, rejects TeX errors and overfull boxes, and writes intermediates to repository `tmp/` or the supplied work folder. PDF metadata is deterministic. See [QA.md](QA.md) for the actual verified build and review evidence, and [SOURCES.md](SOURCES.md) for scholarly sources and prior-use boundaries.

## Contents

- `student/`: final student LaTeX from fresh writer, critic, math checker and reviser stages.
- `guide/facilitator.tex`: separate theorem-first adult guide. Guide authoring is an untested workflow step.
- `check_math.py`: independent finite checks, supporting rather than replacing the guide's proofs.
- `build.py`: portable deterministic builder.
- `reference-pdfs/`: the current verified outputs, included for comparison.

Source ZIPs include only owned sources, check scripts, documentation and current reference PDFs. Generated stage prompts, borrowed writing-style excerpts, whole downloaded references and build caches are excluded. Print US Letter, single-sided, Actual Size; ordinary table materials do not depend on exact cutout dimensions.
