# Problem files with grade-band views: pilot

October 22, 2026. A design pilot, not a change to the current print set. Nothing under `lowell-math-circle-year-2/` is touched; the current Week 50 and Week 52 PDFs remain the print copies.

The question: can each problem be stored once, with its band differences inside it, so that a K–1, 2–3 or 4–5 packet (and shorter formats) are views built from the same files? The full proposal, survey numbers and recommendation are in the project doc linked from the thread; this folder holds the working pieces.

## What is here

| Path | What it shows |
|---|---|
| `week-50/problems/*.md` | Week 50 as ten problem files: one shared rule and nine problems. Each file carries its grades, route (first or return), an optional app link, the student wording with band-specific variants, and its adult key. |
| `week-50/week.toml`, `figures.py`, `guide/` | The week's band styles (header, footer tag, prompt size), the figure code carried over unchanged from the current builder, and the week-level guide prose (theorem-first overview, launch, hints, sources). |
| `atoms.py`, `canvas.py`, `build.py` | Parser, composer and views. About 300 lines in all; Python 3.11+ standard library, pdfLaTeX with TikZ, and `pypdf` for the session pack. |
| `compare.py` | Checks the rebuilt band packets against the current print PDFs: page count, extracted text and 100-dpi pixels. |
| `slice_existing.py`, `week-52/pages.toml` | Band views of an existing shared packet (Weeks 52–93) read from its page headers, with no source change. `--survey` reports every shared packet. |
| `output/week-50/`, `output/week-52/` | The built views. |

## A problem file

```
+++
id = "w50.same-length"
title = "A one-step and a two-step staircase"
grades = ["K-1", "2-3", "4-5"]
route = "first"
scale = "actual"
+++

## prompt [K-1]
Follow both staircases with string. Compare the two pieces of string.

## prompt
Compare the lengths of these two staircases. Find their exact lengths using the width and height.

## figure
diagram(42, [...])

## key
Both solid and dashed routes are 280 mm. ...
```

Consecutive sections of one kind are alternatives: a band uses the section that names it, else the unqualified one, else nothing. Problem numbers are not stored; each view numbers its problems. `page = "same"` keeps a problem on the previous problem's page. `scale = "actual"` marks a problem that must print at 100% (string and ruler work here), so no shrinking format may use it.

## Build and check

```sh
python3 build.py week-50 --out output/week-50 --tables K-1=3,2-3=4,4-5=3
python3 compare.py output/week-50 ../../lowell-math-circle-year-2/week-50 week-50
python3 slice_existing.py ../../lowell-math-circle-year-2/week-52/week-52-students.pdf --index week-52/pages.toml --out output/week-52
python3 slice_existing.py --survey ../../lowell-math-circle-year-2
```

Results on October 22, 2026 (TeX Live 2023, Ubuntu 24.04): the three Week 50 band packets rebuilt from the problem files have the same page counts and identical extracted text as the current print PDFs, and no pixel differs at 100 dpi. The Week 50 views:

| View | Pages |
|---|---|
| Full packet, K–1 / 2–3 / 4–5 | 5 / 5 / 6 (unchanged) |
| First route (P1–3) | 3 per band |
| Return visit | 2 / 2 / 3 |
| Problem menu | 1 |
| Adult key, one entry per problem | 4 |
| Session pack for KK1 / 3333 / 445, first route only | 30, against 53 for full packets |

`session-pack.pdf` is not committed; rebuild it with `--tables`. The Week 52 slices are 2 pages for K–1, 7 for 2–3 and 8 for 4–5, from one 12-page packet.

## Limits

- One week converted. Week 50's builder already drew every page from Python, so its problem files keep its exact canvas positions (`@x,y`). Weeks written as flowing LaTeX would use the same files without positions; that composer is not built yet.
- The adult key view is a new layout built from the same text as the current guide; it is not a replacement for that guide, whose layout differs.
- The page index for Week 52 is read from page headers and labels whole pages. It is a draft to check by eye.
- Digital checks only. Unpiloted, as the source week is.
