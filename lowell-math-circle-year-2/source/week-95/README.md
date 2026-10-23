# Week 95: Count the unseen — review draft

**Problem files, October 23, 2026.** The student packets are stored as [problem files](../problem-files/README.md): `week.toml`, `template.tex` (the old builder's preamble), `figures.py` (its table and catch-record helpers, unchanged) and one file per problem in `problems/`, each band's wording inside it. The conversion changed no wording or figure: the package build gives byte-identical student PDFs to the old builder's in the same TeX installation, and the extracted text matches the print copies. The print copies were compiled with a different TeX installation, whose table rows are about half a millimetre shorter; that is the only pixel difference. The previous builder and the October 17 source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

**Card fixes, October 23, 2026.** Made in the problem files and guide after the conversion, from the review card (`plans/review/week-95.md`, verdict keep). Guide p. 2: the adult is the keeper for Problem 1 and fills each bag from the letter-down, mixed kit, so the highest letter caught no longer gives the total away; distinct letters seen are welcomed as a lower bound; a K–1 route (5 counters, 3 dotted: can a catch of 3 miss every dot?). Grades 4–5 Problem 5 now asks which catch sizes rule out an overlap of 0 when the bag holds at most 20, with its key on guide p. 4. Smaller fixes: the arranged-catch rule reads "no object appears twice in one catch"; the demo arrow reads "catch 2 objects"; two narrating sentences in 4–5 Problem 4 and one in Problem 3 are cut; 2–3 Problem 6 centres its bag totals; a held hint for 2–3 Problem 4. `review/check_card_fixes_2026_10_23.py` checks the letter leak before and after, the Problem 5 key and the K–1 route. The replaced PDFs are in `../../week-95/archive-before-card-fixes-2026-10-23/`. Deferred: the card's coulds 6 (demo box headings), 7 (4–5 Problem 6's printed average) and 12 (rules as actions). Unpiloted; marks, mixing and the keeper's filling are physically unrehearsed.

Two student packets, for Grades 2–3 and 4–5, plus a theorem-first facilitator guide. The guide states assumptions and limits, preparation, a brief shared demonstration, flexible routes, all answers, proofs, hints and return visits. There is no forced K–1 version. All material is unpiloted; physical preparation, marking, mixing, resetting and classroom timing have not been rehearsed. Organizer review is pending.

## Build

Python 3 standard library and pdfLaTeX/TeX Live are required, with TikZ, Latin Modern, geometry, array, fancyhdr, amsmath/amssymb and hyperref. No runtime downloads or private reference inputs are required.

From this folder:

```sh
python3 build.py --out ../../week-95 --work ../../../tmp/week95-build
```

After extracting the portable ZIP:

```sh
python3 week-95/build.py --out rebuilt --work tmp/build
```

The ZIP is written by `python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-95 --flat --zip week-95-source.zip --top week-95`.

The builder creates `week-95-grades-2-3.pdf`, `week-95-grades-4-5.pdf` and `week-95-facilitator.pdf`; it rejects TeX errors and overfull boxes and runs independent mathematics checks. Fixed PDF metadata permits byte-identical clean rebuilds. Build intermediates belong in `tmp`, not the editable sources.

Edit the student pages in `problems/*.md` (helpers in `figures.py`, preamble in `template.tex`); `build.py` writes their LaTeX with the problem-file tools, which the ZIP carries in `tools/`. The first-route and return packets, a one-page problem menu and a key view are built by `python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-95 --out tmp/week-95-views --publish lowell-math-circle-year-2/band-views/week-95` and published in [band-views/week-95/](../../band-views/README.md#weeks-stored-as-problem-files). `guide/facilitator.tex` is the editable guide. `check_math.py` is the independent reviewer's exact checker. `SOURCES.md`, `QA.md` and `revision-response.md` record attribution and review. Full reviews and production provenance are retained in the repository's `plans/new-families-92-97/week-95/`.

Print US Letter, single-sided. Student diagrams illustrate operations and are not cutouts. Use identical counters or cards with marks that can be seen but not detected by touch. See the guide for kit counts, how to hold a population fixed, resetting, and the distinction between blind sampling and deliberately arranging a legal possible record. Keep the deep allocation and model-testing problems for children who are ready, including return visits.

Only owned teaching and build/check sources are bundled. Downloaded books, workflow exemplar excerpts, generated prompt copies, private records, caches and PDFs are excluded from the source ZIP.
