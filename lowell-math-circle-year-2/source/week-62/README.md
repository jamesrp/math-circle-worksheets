# Week 62: Conflict networks and scheduling — current editable source

One shared student packet (9 pages, W62-S-v1: Grades 2–5 pages 1–3, Grades 4–5 pages 4–9) and a 10-page theorem-first adult guide (W62-FAC-v1). Unpiloted; card handling and timing are untested. The print PDFs are in [../../week-62/](../../week-62/).

**Problem files, October 23, 2026.** The student packet is stored as [problem files](../problem-files/README.md): `week.toml`, `template.tex` (the head of the old `students.tex`), `figures.py` and one file per problem in `problems/`, in the flow layout. This is a shared-packet week: `week.toml` defines one band, `shared`, whose packet is `week-62-students.pdf`, and each page's header range is set by `\gdef\band{...}` at the top of the page's first file. The networks are drawn by `graph()` in `figures.py`, the old `make_source.py`'s drawing code unchanged, which also records every printed network in `GRAPHS`; `editable/student/regenerate.py` writes it to `graphs.json` for `verify.py`. The conversion changed no wording or figure: the generated LaTeX differs from the old `students.tex` only by line breaks around page breaks and a comment. The rebuilt packet matches the old builder's in pages, extracted text and 100-dpi pixels, and `graphs.json` is byte-identical; against the print copy, compiled with a different pdfTeX, the old and new builders both differ by the same small glyph-pixel counts. The old builder, its `students.tex` and the October 4 source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

- **Student pages:** edit `problems/*.md` (and `figures.py` for a network), then build and compare:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-62 --out tmp/week-62-views --tex
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-62-views lowell-math-circle-year-2/week-62 week-62
  ```

  The build also writes a first-route and a return packet, a one-page problem menu and a key view into `tmp/`; they are not published. The published views of this week are its band slices and page menu in [band-views/week-62/](../../band-views/README.md), built from the page index `../band-views/indexes/week-62.toml` by `band_views.py build`; update the index when a page's header range or problems change.
- **Adult guide:** `editable/guide/facilitator.tex`, built by the package.
- **Portable package:** `editable/` is the package (`editable/README.md`); `editable/student/regenerate.py` writes `students.tex` and `graphs.json` from the problem files, and the package `build.py` runs it before compiling. `editable/reference-pdfs/` holds copies of the print PDFs. The [portable source ZIP](../week-62-source.zip) holds the package plus the problem files and tools in `problem-files/`. Rebuild it with

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-62 --zip ../week-62-source.zip --top week-62
  ```

  and check a clean rebuild from the extracted ZIP with `python3 week-62/build.py --out rebuilt`.

The research record is in `editable/provenance/` and [plans/new-themes-52-63/week-62/](../../../plans/new-themes-52-63/week-62/), and the review card in [plans/review/week-62.md](../../../plans/review/week-62.md).
