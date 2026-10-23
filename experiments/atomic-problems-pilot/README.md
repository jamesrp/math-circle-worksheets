# Problem files with grade-band views: pilot

October 22, 2026. The pilot that tested storing each problem once, with its band differences inside it, so that band packets and shorter formats are views built from the same files. The proposal and survey are in the doc [Problem files with grade-band views](https://claude.ai/artifact/Lb9Te71sBtpkekWWrw4KNi). The current Week 50 PDFs remain the print copies.

**Outcome.** The organizer chose on October 22 to store weeks as problem files when they are next revised, and to build band slices of the shared packets now. The tools moved to [lowell-math-circle-year-2/source/problem-files/](../../lowell-math-circle-year-2/source/problem-files/README.md), which describes the format; the band slices are in [lowell-math-circle-year-2/band-views/](../../lowell-math-circle-year-2/band-views/README.md). The Week 52 slice from this pilot is superseded there.

## What is here

| Path | What it shows |
|---|---|
| `week-50/problems/*.md` | Week 50 as ten problem files: one shared rule and nine problems, each with its grades, route, optional app link, band-specific wording and adult key. |
| `week-50/week.toml`, `figures.py`, `guide/` | The week's band styles, the figure code carried over unchanged from the current builder, and the week-level guide prose. |
| `output/week-50/` | The views built from those files. `session-pack.pdf` is not committed. |
| `week-03/` (moved) | Added October 23: Week 3 (Shuffle machines) in the flow layout, the worked example of a flowing LaTeX week carried over verbatim. On October 23 it became the week's own source: its `week.toml`, `template.tex` and `problems/` moved to [lowell-math-circle-year-2/source/week-03/](../../lowell-math-circle-year-2/source/week-03/README.md), which now builds the print packets. |

## Result

From the repository root:

```sh
python3 lowell-math-circle-year-2/source/problem-files/build.py experiments/atomic-problems-pilot/week-50 --out tmp/week-50-views --tables K-1=3,2-3=4,4-5=3
python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-50-views lowell-math-circle-year-2/week-50 week-50
```

The three band packets rebuilt from the problem files have the same page counts and identical extracted text as the current print PDFs, and no pixel differs at 100 dpi (TeX Live 2023, Ubuntu 24.04; checked again after the tools moved).

| View | Pages |
|---|---|
| Full packet, K–1 / 2–3 / 4–5 | 5 / 5 / 6 (unchanged) |
| First route (P1–3) | 3 per band |
| Return visit | 2 / 2 / 3 |
| Problem menu | 1 |
| Adult key, one entry per problem | 4 |
| Session pack for KK1 / 3333 / 445, first route only | 30, against 53 for full packets |

The Week 3 flow example (now in `source/week-03/`) rebuilds the same way. At the conversion its pages, extracted text and every pixel at 100 dpi matched the K–1, 2–3 and 4–5 packets of that day (10, 11 and 8 pages; October 23, TeX Live 2023); the same day the review card's page fixes were made in those files, so the current packets are built from them and the commands below now compare a rebuild with them:

```sh
python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-03 --out tmp/week-03-views --tex
python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-03-views lowell-math-circle-year-2/week-03 week-03
```

## Limits

- One week converted in the pilot, in the canvas layout; the flow layout was added on October 23 with Week 3 as its example, and Week 43 was the first week converted for revision.
- The adult key view is a new layout built from the same text as the current guide, not a replacement for it.
- Digital checks only. Unpiloted, as the source week is.
