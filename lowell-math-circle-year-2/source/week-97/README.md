# Week 97: Square remainders

Review draft, awaiting organizer review. Unpiloted; physical preparation, actual-size printing, adult procedures and timing have not been rehearsed. One grades 3–5 student packet. Entry requires square arrays, equal bundles and supported multiplication; general prime/composite proofs are later continuations. No K–1 coverage is claimed. The guide gives a manageable first route and return visits; completing every page in one hour is not the goal.

**Problem files, October 23, 2026.** The student packet is stored as [problem files](../problem-files/README.md): `week.toml` (one band, `3-5`, whose file is the shared `students` packet), `template.tex` (the packet's preamble) and one file per problem in `problems/`. The conversion changed no wording or figure: the package build gives byte-identical PDFs to the previous builder's in the same TeX installation, and the extracted text matches the October 17 print copy, which was compiled with a different TeX installation (a few glyph pixels differ). The static packet TeX it replaces, the previous builder and the October 17 source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

- **Student pages:** edit `problems/*.md`, then check the packet against the print copy:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-97 --out tmp/week-97-views --tex
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-97-views lowell-math-circle-year-2/week-97 week-97
  ```

  As a shared-packet week, its published views remain the band slices and page menu in [band-views/week-97/](../../band-views/README.md), cut from the print PDF by `source/band-views/band_views.py` from its checked page index; the problem-file menu, key and route packets stay in `tmp/`.
- **Print copies and the adult guide:** `build.py` (below) first runs `student/regenerate.py`, which writes `student/students.tex` from the problem files, then compiles the packet and the guide. The print copies and `reference-pdfs/` come from this build.
- **Portable ZIP:** [week-97-source.zip](../week-97-source.zip) holds this folder with the problem-file tools in `tools/`, written by `python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-97 --flat --zip week-97-source.zip --top week-97`.

## Rebuild

Requires Python 3 standard library and TeX Live/pdfLaTeX with TikZ, geometry, fancyhdr, lmodern, amsmath, amssymb, array, booktabs and hyperref. No external font, image, paper, book or Python dependency is bundled.

```sh
python3 build.py --out ../../week-97
```

From an extracted portable archive:

```sh
python3 week-97/build.py --out rebuilt --work tmp/build
```

The builder runs the independent mathematical checks, rejects TeX errors and overfull boxes, and writes intermediates to repository `tmp/` or the supplied work folder. PDF metadata is deterministic. See [QA.md](QA.md) for the actual verified build and review evidence, and [SOURCES.md](SOURCES.md) for scholarly sources and prior-use boundaries.

## Contents

- `problems/`, `template.tex`, `week.toml`: the student pages' source. `student/students.tex` is generated from them by `student/regenerate.py`; do not edit it.
- `guide/facilitator.tex`: separate theorem-first adult guide. Guide authoring is an untested workflow step.
- `check_math.py`: independent finite checks, supporting rather than replacing the guide's proofs.
- `build.py`: portable deterministic builder.
- `reference-pdfs/`: the current verified outputs, included for comparison.

Source ZIPs include only owned sources, check scripts, documentation and current reference PDFs. Generated stage prompts, borrowed writing-style excerpts, whole downloaded references and build caches are excluded. Print US Letter, single-sided, Actual Size; ordinary table materials do not depend on exact cutout dimensions.
