# Week 97: Square remainders

Review draft, awaiting organizer review. Unpiloted; physical preparation, actual-size printing, adult procedures and timing have not been rehearsed. One grades 3–5 student packet. Entry requires square arrays, equal bundles and supported multiplication; general prime/composite proofs are later continuations. There is no K–1 packet; the guide gives an adult-led K–1 route. The guide gives a manageable first route and return visits; completing every page in one hour is not the goal.

**Problem files, October 23, 2026.** The student packet is stored as [problem files](../problem-files/README.md): `week.toml` (one band, `3-5`, whose file is the shared `students` packet), `template.tex` (the packet's preamble) and one file per problem in `problems/`. The conversion changed no wording or figure: the package build gives byte-identical PDFs to the previous builder's in the same TeX installation, and the extracted text matches the October 17 print copy, which was compiled with a different TeX installation (a few glyph pixels differ). The static packet TeX it replaces, the previous builder and the October 17 source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

**Card fixes, October 23, 2026** (from the [review card](../../../plans/review/week-97.md), verdict keep). In the problem files: the opening rules lose the sentence "We compare outputs to find which square inputs they can hide"; Problem 3 reads "Use bundles of 7, 8 and 9, each with inputs from 0 to one less than the bundle size. For each bundle size, find all outputs that hide the most possible inputs. Which bundle size has an output that hides the most inputs?", its question about output 0 moving to the guide; Problem 5 drops "Try larger squares, then". In the guide: page 1 names what children find; page 2 gives an adult-led K–1 route (squares 1×1 to 5×5 in groups of 3, then 4) and says to print pages 5 and 6 together; page 5 adds a counters picture for the prime pairing (a 2×2 corner off a 5×5 square leaves 21 counters that re-form as a 3×7 rectangle, three bundles of 7). Student pages 1, 3 and 5 and guide pages 1, 2, 3 and 5 changed. `checks/card_fixes_2026_10_23.py` checks the new claims, the picture's dots and the wording. The October 17 PDFs are archived in `../../week-97/archive-before-card-fixes-2026-10-23/`, and the conversion ZIP in `../archive-before-card-fixes-2026-10-23/`. Deferred: could 8 (print the multiples of 15 for Problem 4), a prediction to test first.

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
- `checks/card_fixes_2026_10_23.py`: checks for the October 23 card fixes; its output is beside it.
- `build.py`: portable deterministic builder.
- `reference-pdfs/`: the current verified outputs, included for comparison.

Source ZIPs include only owned sources, check scripts, documentation and current reference PDFs. Generated stage prompts, borrowed writing-style excerpts, whole downloaded references and build caches are excluded. Print US Letter, single-sided, Actual Size; ordinary table materials do not depend on exact cutout dimensions.
