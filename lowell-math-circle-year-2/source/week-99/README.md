# Week 99: Moving piles with the least work

Prepared for organizer review. Unpiloted; printing, preparation, material handling, adult procedures and timing have not been physically rehearsed. This family has Grades 2–3 and Grades 4–5, selected by prerequisites rather than forced K–5 coverage. No K–1 packet is claimed; the guide gives an adult-led K–1 route on the line mat. Entry: counting small piles and counter-steps while keeping a fixed target visible. Later work adds unavoidable-crossing certificates, position totals and comparisons between whole arrangements. Ordinary adult reading or recording is supported; children should retain the mathematical choices. The guide gives a manageable first visit and later routes rather than requiring every page in one hour.

**Critic coulds, October 23, 2026.** From an independent critic's review: the guide's "Readiness and discovery" says K–1 has an adult-led route on page 2 instead of "No K–1 coverage … is implied" (W99-FAC-v3), and Grades 4–5 Problem 5 labels its third, blank star pair "Extra workspace" (W99-45-v3). The replaced PDFs and ZIP are in the `archive-before-critic-m-fixes-2026-10-23/` folders. Unpiloted.

**Problem files, October 23, 2026.** The student packets are stored as [problem files](../problem-files/README.md): `week.toml`, `template.tex` (the page frame: portrait and landscape headers, footer, page number and prompt placement) and one file per problem in `problems/`, each holding its prompt and its page's TikZ drawing code, with band differences inside it. Each packet is now one document whose last page is landscape, instead of six documents merged. The conversion changed no wording or drawing: both packets rebuild with the same pages, extracted text and 100-dpi pixels as the October 17 print copies. The twelve static page files, the previous builder and target list and the October 17 source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

**Card fixes, October 23, 2026** (from the [review card](../../../plans/review/week-99.md), verdict keep). New print file `week-99-materials.pdf` (W99-MAT-v1, two landscape pages): the line mat the guide asks for (six 30 mm bins 35 mm apart, a target row and a move strip) and the three-leaf star board (35 mm circles, with a small target star), built from `materials/materials.tex` and measured by `materials/check_materials.py`; physically unrehearsed. In the problem files (v2 footers): Problem 1 no longer asks for two best move records (every printed best matching is unique), with one record line per pair; the rules say "Write each move as you make it" and the rule picture's last panel reads "end"; Problem 3's delivery sentence is plainer and the Grades 2–3 tie sentence is gone; Grades 4–5 Problem 5 drops its method sentence. Only pages 1 and 3 of both packets and Grades 4–5 page 5 changed above the footer. In the guide (W99-FAC-v2): an adult-led K–1 route on the mat; the mats named in the materials list and preparation; the "Different plans" paragraph corrected; the launch on numbered bins; the first route named; a prefix-count reason for Grades 4–5 Problem 4. `checks/card_fixes_2026_10_23.py` checks the new claims, the printed wording and the mats. The v1 PDFs and the conversion ZIP are archived in `archive-before-card-fixes-2026-10-23/` folders here and beside the print copies. Deferred: coulds 12 and 13 (new questions for Grades 4–5 Problems 2 and 3).

- **Student pages:** edit `problems/*.md`, then build every view:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-99 --out tmp/week-99-views --tex --publish lowell-math-circle-year-2/band-views/week-99
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-99-views lowell-math-circle-year-2/week-99 week-99
  ```

  The first-route and return packets, the one-page problem menu and a key view by problem are published in [band-views/week-99/](../../band-views/README.md#weeks-stored-as-problem-files).
- **Print copies and the adult guide:** `build.py` (below) first runs `student/regenerate.py`, which writes `student/*.tex` from the problem files, then compiles the packets and the guide (`guide/*.tex`). The print copies come from this build.
- **Portable ZIP:** [week-99-source.zip](../week-99-source.zip) holds this folder with the problem-file tools in `tools/`, written by `python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-99 --flat --zip week-99-source.zip --top week-99`.

## Rebuild

Requires Python 3 and a configured TeX Live/pdfLaTeX installation with TikZ, geometry, fancyhdr, lmodern, amsmath, amssymb, array, booktabs, hyperref and the standard article/extarticle classes. No private reference, external image, nonstandard font or network download is needed by the builder.

From this source folder:

```sh
python3 build.py --out ../../week-99
```

From an extracted source ZIP:

```sh
python3 week-99/build.py --out rebuilt --work tmp/build
```

`build.py` runs the independent mathematical checks, rejects TeX errors and overfull boxes, and builds the targets listed in `build-targets.json`. Intermediates go to repository `tmp/` or the supplied work directory. The source files omit volatile PDF dates/IDs; the build fixes SOURCE_DATE_EPOCH for reproducibility. A normal TeX installation must have its format and font-map configuration in place. The cloud verification used the already installed TeX files with a local runtime configuration; no machine-specific cache is packaged.

## Editable contents

- `week.toml`, `template.tex`, `problems/*.md`: the student pages' source (problem files), from fresh writer, critic, mathematical review and reviser stages. `student/regenerate.py` writes `student/grades-2-3.tex` and `student/grades-4-5.tex` from them; do not edit `student/*.tex` directly. In the ZIP, `tools/` holds the problem-file tools it needs.
- `guide/facilitator.tex` and `guide/solutions.tex`: separately authored theorem-first adult guide. Guide authoring is an untested addition to the tested student workflow.
- `check_math.py`: independent standard-library finite checks. It prints its results without changing the source tree.
- `build.py` and `build-targets.json`: portable build entry point and exact output list.
- `materials/materials.tex`: the line mat and star board (`week-99-materials.pdf`); `materials/check_materials.py` measures the printed PDF.
- `checks/`: checks of later revisions.
- `reference-pdfs/`: current verified PDFs for comparison.
- `QA.md` and `SOURCES.md`: verification, status, scholarly sources and precise overlap boundaries.

The adjacent source ZIP contains the same owned editables and reference PDFs. Generated workflow prompts, borrowed style excerpts, raw session traces, build caches and downloaded works are excluded. Print US Letter single-sided at Actual Size. Keep facilitator pages separate. `week-99-materials.pdf` prints the line mat and star board; print it at Actual Size, landscape. The guide names the extra copy of Grades 4–5 page 4 to cut into cards.
