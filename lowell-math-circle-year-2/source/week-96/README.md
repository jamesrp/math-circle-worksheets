# Week 96: Prime bags and divisor builders

Review draft, awaiting organizer review. Unpiloted; physical preparation, actual-size printing, adult procedures and timing have not been rehearsed. Two student packets: grades 2–3 and 4–5. Equal groups and supported multiplication are entry prerequisites; divisor counting and completeness are deeper continuations. No K–1 coverage is claimed. The guide gives a manageable first route and return visits; completing every page in one hour is not the goal.

**Problem files, October 23, 2026.** The student packets are stored as [problem files](../problem-files/README.md): `week.toml`, `template.tex` (the band files' preamble) and one file per problem in `problems/`, each band's wording inside it. The conversion changed no wording or figure: the package build gives byte-identical PDFs to the previous builder's in the same TeX installation, and the extracted text matches the October 17 print copies, which were compiled with a different TeX installation (a few glyph pixels differ). The static band TeX it replaces, the previous builder and the October 17 source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

**Card fixes, October 23, 2026** (from the [review card](../../../plans/review/week-96.md), verdict keep). In the problem files: Grades 2–3 Problem 3 asks "Find the complete collection for each bag. Does the bag with more tokens make more different values?", since both bags make 8; both bands' rules define a prime as "a number greater than 1 that cannot split" and say "Tokens with the same number are the same"; Grades 4–5 Problem 4 has a larger answer box and Problem 5's example reads as one sentence. In the guide: an adult-led K–1 route (rectangles from counters, sorting 2–20 into "makes a rectangle" and "only one row"), Grades 2–3 page 4 printed and kept at the table, a divisor test by sharing counters, and Problem 3's answer stated. `checks/card_fixes_2026_10_23.py` checks the new claims and wording. The October 17 PDFs and the conversion ZIP are archived in `archive-before-card-fixes-2026-10-23/` folders beside the print copies and here. Deferred: coulds 8 (token size in the problem bags) and 10 (a printable token sheet).

- **Student pages:** edit `problems/*.md`, then build every view:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-96 --out tmp/week-96-views --tex --publish lowell-math-circle-year-2/band-views/week-96
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-96-views lowell-math-circle-year-2/week-96 week-96
  ```

  The first-route and return packets, the one-page problem menu and a key view by problem are published in [band-views/week-96/](../../band-views/README.md#weeks-stored-as-problem-files).
- **Print copies and the adult guide:** `build.py` (below) first runs `student/regenerate.py`, which writes `student/*.tex` from the problem files, then compiles the packets and the guide. The print copies and `reference-pdfs/` come from this build.
- **Portable ZIP:** [week-96-source.zip](../week-96-source.zip) holds this folder with the problem-file tools in `tools/`, written by `python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-96 --flat --zip week-96-source.zip --top week-96`.

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

- `problems/`, `template.tex`, `week.toml`: the student pages' source. `student/*.tex` is generated from them by `student/regenerate.py`; do not edit it.
- `guide/facilitator.tex`: separate theorem-first adult guide. Guide authoring is an untested workflow step.
- `check_math.py`: independent finite checks, supporting rather than replacing the guide's proofs.
- `build.py`: portable deterministic builder.
- `reference-pdfs/`: the current verified outputs, included for comparison.

Source ZIPs include only owned sources, check scripts, documentation and current reference PDFs. Generated stage prompts, borrowed writing-style excerpts, whole downloaded references and build caches are excluded. Print US Letter, single-sided, Actual Size; ordinary table materials do not depend on exact cutout dimensions.
