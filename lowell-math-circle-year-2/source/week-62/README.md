# Week 62: Conflict networks and scheduling — current editable source

One shared student packet (9 pages, W62-S-v2: Grades 2–5 pages 1–3, Grades 4–5 pages 4–5 and 8–9, Grades 3–5 pages 6–7), a one-page sheet of cards and slot headers (W62-M-v1) and a 10-page theorem-first adult guide (W62-FAC-v2). Unpiloted; card and counter handling, cutting and timing are untested. The print PDFs are in [../../week-62/](../../week-62/).

**Review card fixes, October 23, 2026.** Made in the problem files and the guide after the conversion below. Students: p. 1 says "Put each card in exactly one slot"; p. 3 has "Largest group:" beside each "Fewest slots:" and two answer lines; pp. 6–7 are headed Grades 3–5; Problem 7 says "the first-slot rule", as Problem 8 does; the p. 9 example shows one schedule as cards with slots 1, 2, 3 (slot 3 empty) and lists X 1, Y 2; X 2, Y 1; X 1, Y 3, so it no longer fixes X in slot 1. The new `editable/student/materials.tex` prints three kits of A–H cards and slot headers 1–4 per sheet. The guide gives each slot a counter colour (a key counter on its header, a counter of that colour on each placed card's circle, shown in the launch and used by the checker), adds an adult-led K–1 route on pp. 1–2 with a plain-words key (p. 4), names the p. 6 tree and P7 as Grades 2–3 continuations, prints 32 student sheets and the materials, adds dry-erase markers, gives a 20–25 minute preparation estimate, adds "at least one of them used" to the overview's swapping sentence, and matches its p. 9 note to the new example. `plans/review/checks/week-62/check_card_fixes.py` checks each change. The replaced PDFs are in `../../week-62/archive-before-card-fixes-2026-10-23/`.

**Problem files, October 23, 2026.** The student packet is stored as [problem files](../problem-files/README.md): `week.toml`, `template.tex` (the head of the old `students.tex`), `figures.py` and one file per problem in `problems/`, in the flow layout. This is a shared-packet week: `week.toml` defines one band, `shared`, whose packet is `week-62-students.pdf`, and each page's header range is set by `\gdef\band{...}` at the top of the page's first file. The networks are drawn by `graph()` in `figures.py`, the old `make_source.py`'s drawing code unchanged, which also records every printed network in `GRAPHS`; `editable/student/regenerate.py` writes it to `graphs.json` for `verify.py`. The conversion changed no wording or figure: the generated LaTeX differs from the old `students.tex` only by line breaks around page breaks and a comment. The rebuilt packet matches the old builder's in pages, extracted text and 100-dpi pixels, and `graphs.json` is byte-identical; against the print copy, compiled with a different pdfTeX, the old and new builders both differ by the same small glyph-pixel counts. The old builder, its `students.tex` and the October 4 source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

- **Student pages:** edit `problems/*.md` (and `figures.py` for a network), then build and compare:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-62 --out tmp/week-62-views --tex
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-62-views lowell-math-circle-year-2/week-62 week-62
  ```

  The build also writes a first-route and a return packet, a one-page problem menu and a key view into `tmp/`; they are not published. The published views of this week are its band slices and page menu in [band-views/week-62/](../../band-views/README.md), built from the page index `../band-views/indexes/week-62.toml` by `band_views.py build`; update the index when a page's header range or problems change.
- **Adult guide and materials:** `editable/guide/facilitator.tex` and `editable/student/materials.tex`, built by the package.
- **Portable package:** `editable/` is the package (`editable/README.md`); `editable/student/regenerate.py` writes `students.tex` and `graphs.json` from the problem files, and the package `build.py` runs it before compiling. `editable/reference-pdfs/` holds copies of the print PDFs. The [portable source ZIP](../week-62-source.zip) holds the package plus the problem files and tools in `problem-files/`. Rebuild it with

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-62 --zip ../week-62-source.zip --top week-62
  ```

  and check a clean rebuild from the extracted ZIP with `python3 week-62/build.py --out rebuilt`.

The research record is in `editable/provenance/` and [plans/new-themes-52-63/week-62/](../../../plans/new-themes-52-63/week-62/), and the review card in [plans/review/week-62.md](../../../plans/review/week-62.md).
