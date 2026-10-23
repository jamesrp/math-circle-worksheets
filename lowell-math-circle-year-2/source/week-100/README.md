# Week 100: Distance in nested worlds

Prepared for organizer review. Unpiloted; printing, preparation, material handling, adult procedures and timing have not been physically rehearsed. This family has one Grades 3–5 packet, selected by prerequisites rather than forced K–5 coverage. No K–1 packet is claimed; the guide gives an adult-led K–1 route with the page-1 shape cards. Entry: comparing labels, tracking nested memberships and three pairwise relations. Later number work adds parity and remainders; it is not required for the complete object route. Ordinary adult reading or recording is supported; children should retain the mathematical choices. The guide gives a manageable first visit and later routes rather than requiring every page in one hour.

**Problem files, October 23, 2026.** The student packet is stored as [problem files](../problem-files/README.md): `week.toml`, `template.tex` (the old preamble with the header, footer, page frame and prompt placement) and one file per problem in `problems/`, each holding its prompt and its page's TikZ drawing code; the rules, the letter cards and the number cards are setup files. The conversion changed no wording or drawing: the packet rebuilds with the same pages, extracted text and 100-dpi pixels as the October 17 print copy. The static TeX it replaces, the previous builder and the October 17 source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

**Card fixes, October 23, 2026** (from the [review card](../../../plans/review/week-100.md), verdict keep). In the problem files (W100-G35-v2): Problem 4 now ends "Draw your world. Could loops around different sets of cards fit the same ten clues?" instead of asking for two different-looking drawings; Problem 5 says "Change exactly one of these ten clues, with A–C = 2"; Problem 10 adds the end rule "Then the builder shows the secret world: if any distance in the drawing is different, the round is lost." Only pages 4, 5 and 8 changed above the footer. In the guide (W100-FAC-v2): an adult-led K–1 route with a plain-words key; the page-8 frame named as the workmat, loop counts and cord lengths, and a third 4-label for Problem 10; the first route named; keys for the new Problem 4 question and the Problem 10 end rule; a hunt for partly overlapping balls before Problem 7's argument; the two "page 1" references now point to the mathematical overview. `checks/card_fixes_2026_10_23.py` checks these claims and the printed wording. The v1 PDFs are in [../../week-100/archive-before-card-fixes-2026-10-23/](../../week-100/archive-before-card-fixes-2026-10-23/README.md) and the conversion's source ZIP in [archive-before-card-fixes-2026-10-23/](archive-before-card-fixes-2026-10-23/README.md). Still unpiloted and physically unrehearsed.

- **Student pages:** edit `problems/*.md`, then build every view:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-100 --out tmp/week-100-views --tex --publish lowell-math-circle-year-2/band-views/week-100
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-100-views lowell-math-circle-year-2/week-100 week-100
  ```

  The first-route and return packets, the one-page problem menu and a key view by problem are published in [band-views/week-100/](../../band-views/README.md#weeks-stored-as-problem-files).
- **Print copies and the adult guide:** `build.py` (below) first runs `student/regenerate.py`, which writes `student/grades-3-5.tex` from the problem files, then compiles the packet and the guide (`guide/*.tex`). The print copies come from this build.
- **Portable ZIP:** [week-100-source.zip](../week-100-source.zip) holds this folder with the problem-file tools in `tools/`, written by `python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-100 --flat --zip week-100-source.zip --top week-100`.

## Rebuild

Requires Python 3 and a configured TeX Live/pdfLaTeX installation with TikZ, geometry, fancyhdr, lmodern, amsmath, amssymb, array, booktabs, hyperref and the standard article/extarticle classes. No private reference, external image, nonstandard font or network download is needed by the builder.

From this source folder:

```sh
python3 build.py --out ../../week-100
```

From an extracted source ZIP:

```sh
python3 week-100/build.py --out rebuilt --work tmp/build
```

`build.py` runs the independent mathematical checks, rejects TeX errors and overfull boxes, and builds the targets listed in `build-targets.json`. Intermediates go to repository `tmp/` or the supplied work directory. The source files omit volatile PDF dates/IDs; the build fixes SOURCE_DATE_EPOCH for reproducibility. A normal TeX installation must have its format and font-map configuration in place. The cloud verification used the already installed TeX files with a local runtime configuration; no machine-specific cache is packaged.

## Editable contents

- `week.toml`, `template.tex`, `problems/*.md`: the student pages' source (problem files), from fresh writer, critic, mathematical review and reviser stages. `student/regenerate.py` writes `student/grades-3-5.tex` from them; do not edit it directly. In the ZIP, `tools/` holds the problem-file tools it needs.
- `guide/facilitator.tex` and `guide/solutions.tex`: separately authored theorem-first adult guide. Guide authoring is an untested addition to the tested student workflow.
- `check_math.py`: independent standard-library finite checks. It prints its results without changing the source tree.
- `checks/`: checks of later revisions.
- `build.py` and `build-targets.json`: portable build entry point and exact output list.
- `reference-pdfs/`: current verified PDFs for comparison.
- `QA.md` and `SOURCES.md`: verification, status, scholarly sources and precise overlap boundaries.

The adjacent source ZIP contains the same owned editables and reference PDFs. Generated workflow prompts, borrowed style excerpts, raw session traces, build caches and downloaded works are excluded. Print US Letter single-sided at Actual Size. Keep facilitator pages separate. The guide identifies any separate reusable workmat and extra cutting copies needed for the small student reference diagrams.
