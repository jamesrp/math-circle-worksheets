# Week 64: Straight paths on strange surfaces

**Problem files, October 23, 2026.** The student packet is stored as [problem files](../problem-files/README.md) in this folder, in the canvas layout: `week.toml`, `figures.py` (the old `student/generate.py`'s page template and drawing code) and one file per problem in `problems/`. This is a shared-packet week with one band, `shared`; each page's first figure, `page_start(level)`, prints that page's grade range. `student/regenerate.py` writes `student/students.tex` from the problem files, and `build.py` and `student/build.sh` run it before compiling; edit the problem files, not `students.tex`. The conversion changed no wording or figure: the new `students.tex` differs from the old only by writing page 1's paragraph break as `\par`, and the packet rebuilds with the same pages, text and 100-dpi pixels as the print copy. The old generator, its `students.tex` and the October 5 source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md); `source-manifest.json` and `RECOVERY.md` describe the October 6 recovery package and still name `generate.py`.

**Review card fixes, October 23, 2026 (W64-G35-v2, W64-FAC-v2).** After the conversion, the [review card](../../../plans/review/week-64.md)'s shoulds 1–2 and coulds 3, 4 and 6–9: `octagon(..., ticks=True)` in `figures.py` prints seven numbered ticks per edge, counted from the arrow's tail, on the octagons of pp. 1–3, and the p. 1 rule says to match them; p. 3 drops "Treat overlapping copies as separate sheets."; p. 5 says "around the point where they meet"; the L rules are a setup file (`problems/05a-l-rules.md`) above Problem 6; Problem 7 asks which dots each trip passes, in order; Problems 7 and 8 lose the arrow sentence. The guide adds a K–1 adult-led route with a plain-words key (p. 1), a B-edge crossing and tick matching in the launch, a print note for p. 9 and the math check's wording for P1 hint 3. Could 5 (a glued hexagon) is deferred. The v1 PDFs are in [week-64/archive-before-card-fixes-2026-10-23/](../../week-64/archive-before-card-fixes-2026-10-23/README.md); the check is `plans/review/checks/week-64/check_card_fixes.py`.

- **Student pages:** edit `problems/*.md` (figures and the page template in `figures.py`), then build and compare:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-64 --out tmp/week-64-views --tex
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-64-views lowell-math-circle-year-2/week-64 week-64
  ```

  Its band slices and page menu in [band-views/week-64/](../../band-views/README.md) are built from `../band-views/indexes/week-64.toml` by `band_views.py build`; update the index when a page's grade range or problems change.
- **Portable ZIP:** [../week-64-source.zip](../week-64-source.zip) holds this folder with the problem-file tools in `tools/`, written by `python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-64 --flat --zip week-64-source.zip --top week-64-source`.

The rest of this README records the October 5 package; where it says `student/generate.py`, read `student/regenerate.py` and the problem files.

A newly authored, unpiloted packet for Grades 3–5, with readiness-dependent Grades 4–5 continuations. It develops opposite-edge translation paths on a regular octagon, its exceptional corner point, and exact path experiments on a three-square L surface. These are two different flat metrics on genus-two surfaces. They are not a hyperbolic octagon tessellation.

## Printable outputs

- `week-64-students.pdf`: 9 pages and 9 substantial investigations. The essential corner cutouts are on page 5; no separate materials file is required.
- `week-64-facilitator.pdf`: 12 pages with a theorem-first overview, common launch, prerequisites, materials, flexible routes, hints, complete solutions and proofs, and source references.

Suggested starting route: student pages 1–3 for octagon trips and translated copies. Pages 4–5 investigate which corners meet and the resulting three full turns around one point. Pages 6–9 are a separate return route using the exact square grid. Finishing every page in one session is not the goal.

Reading may be supported by an adult. Children need to match positions along arrows, use a ruler and tracing paper, and keep a direction unchanged. The later pages require reliable eighth-grid tracing and reasoning about repeated states. No square-root calculations, formal topology or advanced algebra are required of students. An adult remains available for the shared rules and physical handling; the mathematical choices belong to the children.

Per pair/trio: pencils and eraser, ruler, colored pencils, tracing paper, plain paper, scissors, a small counter and a separate direction arrow. Print single-sided on US Letter at 100%, without fit-to-page scaling. The guide explains workspace and preparation, including the larger tracing-paper area needed for developed copies. Rehearse the actual kit before use.

## Rebuild both PDFs

Requirements: Python 3 standard library and a normal TeX Live/MacTeX installation with pdfLaTeX, TikZ/PGF, Helvetica and standard LaTeX packages. No repository paths, network access, downloaded books, external picture files or local absolute paths are required.

From this package root:

    python3 build.py --out output

This writes the two named PDFs into `output/`. Compilation takes place in temporary directories. Sources remain editable in `student/` and `guide/`; their READMEs give the individual build commands. `student/generate.py` generates its editable TikZ/LaTeX file.

Run mathematical checks with:

    python3 student/verify.py
    python3 guide/verify.py

Optional PDF comparison uses PyMuPDF:

    python3 compare_pdfs.py original.pdf rebuilt.pdf --out comparison.json

It compares page dimensions, exact extracted text and rendered pixels at 144 dpi. A different TeX/font/rendering version may change pixels without changing the mathematics.

## Verification and limits

All student and guide pages were rendered and visually inspected. Independent mathematical checks covered every problem, prescribed first return and corner collision, endpoint identifications, cone angles, development diagrams and finite-permutation arguments. All three targeted wording findings were resolved. Clean portable-source builds matched the delivered PDFs in page dimensions, exact text and rendered pixels across all 21 pages in the production environment.

These are digital checks. Physical cutting, tracing, material fit and classroom use remain untested. The packet is ready for organizer review, not represented as classroom-piloted. No density, equidistribution or ergodicity conclusion is inferred from a finite drawing, and the square-grid rational-direction argument is not transferred to the regular octagon.

## Authorship and sources

Student wording, diagrams, exercises, teaching suggestions and the guide are newly authored around established mathematics; novel theorems are not claimed. Primary mathematical sources and their exact scope are recorded in `guide/PROVENANCE.md` and the printed guide. This source package contains no downloaded books, source-page reproductions, borrowed worksheet examples or generated workflow prompts.
