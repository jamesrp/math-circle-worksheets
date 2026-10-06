# Week 64: Straight paths on strange surfaces

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
