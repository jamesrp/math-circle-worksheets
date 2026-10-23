# Week 77: Persistent holes

One shared Grades 4–5 prototype: 6 student pages, a separate 4-page theorem-first adult guide and a 2-page sheet of tiles, edge strips, edge tokens and stage cards to print and cut. Independently reviewed and digitally checked, awaiting organizer review. The week number is a library identifier, not an adopted schedule. Physical preparation/handling and classroom piloting remain unperformed.

## Rebuild from this package

Use Python 3.11+ and normal TeX Live/MacTeX with pdfLaTeX, TikZ/PGF, Computer Modern/Latin Modern, geometry, fancyhdr, AMS packages and the small standard packages listed in the student/guide READMEs. No network, repository files, private reference, external artwork or custom Python library is required.

    python3 build.py --out output
    python3 build.py --verify-only

The first command reconstructs the three named PDFs in the chosen output directory; the second runs independent, student and guide checks without TeX. Build intermediates are isolated. All required authored inputs are packaged.

The student pages are stored as problem files (since October 23, 2026): one file per problem in `problem-files/problems/`, with `problem-files/week.toml` and `problem-files/template.tex` (in the repository, `lowell-math-circle-year-2/source/week-77/`). Edit a problem there. `student/regenerate.py` writes `student/students.tex` from them, and `build.py` runs it first, so do not edit `students.tex` by hand. `problem-files/tools/build.py problem-files --out DIR` builds the same student packet together with a one-page problem menu and first-route and return packets. Edit the adult guide in `guide/facilitator.tex` and the materials sheet in `materials/materials.py`, which writes `materials/materials.tex` (its board coordinates are copied from the problem files). `review/verify_card_fixes_2026_10_23.py` (needs PyMuPDF) checks the October 23, 2026 review-card fixes in built PDFs, including that every printed tile matches its triangle on the student pages. `reference-pdfs/` holds the current print PDFs, for comparing a rebuild.

## Readiness and use

Print single-sided US Letter at 100% / Actual Size. Read student/README.md for reading, arithmetic, spatial and recording prerequisites, and the adult guide for exact materials, a short shared launch, hints, solutions and sensible stopping points. The approximate grade range is not a classroom-readiness guarantee. There is no younger edition; the guide gives an adult-led K–1 and 2–3 route on student page 2 (and page 3). Completing every page is not the goal.

MATHEMATICS.md records precise hypotheses and general arguments. SOURCES.md separates mathematical lineage from independently authored examples. The repository's plans/frontier-prototypes-76-78/week-77/ record preserves reviews, revision decisions, final checks and the actual extracted-ZIP reconstruction result. Different TeX/font versions can affect appearance.

The portable ZIP excludes stage prompts, borrowed style examples, downloaded books/papers, external fonts, runtime format files, caches, render images, logs, superseded drafts and private classroom information.

## October 15 introduction revision

Added a full introductory page: square rim, diagonal, one filled half, both halves, then a complete-loop token example. All six investigations remain; student task pages are now 2–6. “Gone” means a boundary of filled tiles, with all board edges retained. This organizer-directed revision is unpiloted.

## October 23 review-card fixes

F77-45-v3, F77-FAC-v3 and the new F77-M-v1. Problem 3 asks whether the first loop can be gone at stage 5 whichever dashed edge comes first, on the joined board and on Problem 2's square (yes on the joined board; on the square only with AC first), and ends with the hole-count question; Problem 2 no longer states the counts. The joined board's C is raised to (5.8, 1.4) so that its four solid edges bend at C; AB and DE stay 5.8 cm. Problem 5 says "come back". The materials sheet prints the nine tiles at board scale, each with its name, board and edge names, the seven edge strips, 48 tokens and 8 stage cards. The guide corrects the counts-versus-history sentence, states that a loop is gone exactly when every triangle inside it is filled, makes the square the shared launch and the XYZ token test the 4–5 table's own, and adds an adult-led K–1 and 2–3 route with a plain-words key. Unpiloted; the printed pieces are physically unrehearsed.
