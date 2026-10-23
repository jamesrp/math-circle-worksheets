# Week 76: Substitution strips

One shared Grades 3–5 prototype: 4 student pages, a separate 5-page theorem-first adult guide and a page of letter tiles to print and cut. Independently reviewed and digitally checked. **Promoted after organizer review on October 15, 2026.** The week number is a library identifier, not an adopted schedule. Physical preparation/handling and classroom piloting remain unperformed.

## Rebuild from this package

Use Python 3.11+ and normal TeX Live/MacTeX with pdfLaTeX, TikZ/PGF, Computer Modern/Latin Modern, geometry, fancyhdr, AMS packages and the small standard packages listed in the student/guide READMEs. No network, repository files, private reference, external artwork or custom Python library is required.

    python3 build.py --out output
    python3 build.py --verify-only

The first command reconstructs the three named PDFs in the chosen output directory; the second runs independent, student and guide checks without TeX. Build intermediates are isolated. All required authored inputs are packaged.

The student pages are stored as problem files (since October 23, 2026): one file per problem in `problem-files/problems/`, with `problem-files/week.toml` and `problem-files/template.tex` (in the repository, `lowell-math-circle-year-2/source/week-76/`). Edit a problem there. `student/regenerate.py` writes `student/students.tex` from them, and `build.py` runs it first, so do not edit `students.tex` by hand. `problem-files/tools/build.py problem-files --out DIR` builds the same student packet together with a one-page problem menu and first-route and return packets. Edit the adult guide in `guide/facilitator.tex` and the tile page in `materials/materials.tex`. `review/verify_card_fixes_2026_10_23.py` (needs PyMuPDF) checks the October 23, 2026 review-card fixes in built PDFs. `reference-pdfs/` holds the current print PDFs, for comparing a rebuild.

## Readiness and use

Print single-sided US Letter at 100% / Actual Size. Read student/README.md for reading, arithmetic, spatial and recording prerequisites, and the adult guide for exact materials, a short shared launch, hints, solutions and sensible stopping points. The approximate grade range is not a classroom-readiness guarantee. No K–1 edition is implied, and completing every page is not the goal.

MATHEMATICS.md records precise hypotheses and general arguments. SOURCES.md separates mathematical lineage from independently authored examples. The repository's plans/frontier-prototypes-76-78/week-76/ record preserves reviews, revision decisions, final checks and the actual extracted-ZIP reconstruction result. Different TeX/font versions can affect appearance.

The portable ZIP excludes stage prompts, borrowed style examples, downloaded books/papers, external fonts, runtime format files, caches, render images, logs, superseded drafts and private classroom information.
