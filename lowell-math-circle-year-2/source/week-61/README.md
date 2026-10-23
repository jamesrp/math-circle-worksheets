# Week 61: Triangles on a ball — current editable source

One shared student packet (7 pages, W61-S-v4: Grades 2–5 pages 1–3, Grades 3–5 page 4, Grades 4–5 pages 5–7) and a 9-page theorem-first adult guide (W61-F-v3). Unpiloted; ball, string, marker and meridian handling are physically unrehearsed. The print PDFs are in [../../week-61/](../../week-61/).

**Review card fixes, October 23, 2026.** Made in the problem files after the conversion below: page 1's rule says only that a shortest route runs along a great circle, so it no longer answers Problem 1; page 2's triangle rule is "Use the smaller region inside the three sides"; page 3 no longer states the equator right angle; Problem 4 uses a 60° gap instead of 72° (on a 15° globe grid); page 5's lune-pair example is a 70-70-70 triangle that no problem uses, with the A and A* labels beside their dots; Problem 7 asks for the rule and why it always works without printing the proof's plan. The guide gains a K–1 route with a plain-words key (p. 3), prints P4 and P5–7 on the first visit, says rough meridian marks suffice, relabels "Outside our rules" (the rule still gives 7/8 for the octant's complement), and moves the proof's two steps into a P7 hint. `plans/review/checks/week-61/check_card_fixes.py` checks each change. The replaced PDFs are in `../../week-61/archive-before-card-fixes-2026-10-23/` and the conversion's ZIP in [archive-before-card-fixes-2026-10-23/](archive-before-card-fixes-2026-10-23/README.md).

**Problem files, October 23, 2026.** The student packet is stored as [problem files](../problem-files/README.md): `week.toml`, `template.tex` (the head of the old `students.tex`), `figures.py` and one file per problem in `problems/`, in the flow layout. This is a shared-packet week: `week.toml` defines one band, `shared`, whose packet is `week-61-students.pdf`, and each page's header range is set by `\band{...}` at the top of the page's first file. The sphere pictures are still drawn by `editable/student/geometry.py`: `figures.py` imports it, and the first file's figure section writes the same macros the old builder wrote to `figures.tex`. The conversion changed no wording or figure. The rebuilt packet matches the old builder's in pages, extracted text and 100-dpi pixels; against the print copy, compiled with a different pdfTeX, the old and new builders both differ by the same small glyph-pixel counts. The hand-written `students.tex` and the October 16 source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

- **Student pages:** edit `problems/*.md`, then build and compare:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-61 --out tmp/week-61-views --tex
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-61-views lowell-math-circle-year-2/week-61 week-61
  ```

  The build also writes a first-route and a return packet, a one-page problem menu and a key view into `tmp/`; they are not published. The published views of this week are its band slices and page menu in [band-views/week-61/](../../band-views/README.md), built from the page index `../band-views/indexes/week-61.toml` by `band_views.py build`; update the index when a page's header range or problems change.
- **Adult guide:** `editable/guide/facilitator.tex`, built by the package.
- **Portable package:** `editable/` is the package (`editable/README.md`); `editable/student/regenerate.py` writes `students.tex` from the problem files, and the package `build.py` runs it before compiling. `editable/reference-pdfs/` holds copies of the print PDFs. The [portable source ZIP](../week-61-source.zip) holds the package plus the problem files and tools in `problem-files/`. Rebuild it with

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-61 --zip ../week-61-source.zip --top week-61
  ```

  and check a clean rebuild from the extracted ZIP with `python3 week-61/build.py --out rebuilt`.

The research record is in `editable/provenance/` and the review card in [plans/review/week-61.md](../../../plans/review/week-61.md).
