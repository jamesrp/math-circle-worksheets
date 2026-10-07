# Week 78: Three-armed lines

One shared Grades 4–5 prototype: 4 student pages and a separate 4-page theorem-first adult guide. Independently reviewed and digitally checked, awaiting organizer review. The week number is a library identifier, not an adopted schedule. Physical preparation/handling and classroom piloting remain unperformed.

## Rebuild from this package

Use Python 3 and normal TeX Live/MacTeX with pdfLaTeX, TikZ/PGF, Computer Modern/Latin Modern, geometry, fancyhdr, AMS packages and the small standard packages listed in the student/guide READMEs. No network, repository files, private reference, external artwork or custom Python library is required.

    python3 build.py --out output
    python3 build.py --verify-only

The first command reconstructs both named PDFs in the chosen output directory; the second runs independent, student and guide checks without TeX. Build intermediates are isolated. Edit student/students.tex and guide/facilitator.tex; when a diagram is generated, edit its included data/generator and rebuild. All required authored inputs are packaged.

## Readiness and use

Print single-sided US Letter at 100% / Actual Size. Read student/README.md for reading, arithmetic, spatial and recording prerequisites, and the adult guide for exact materials, a short shared launch, hints, solutions and sensible stopping points. The approximate grade range is not a classroom-readiness guarantee. No K–1 edition is implied, and completing every page is not the goal.

MATHEMATICS.md records precise hypotheses and general arguments. SOURCES.md separates mathematical lineage from independently authored examples. The repository's plans/frontier-prototypes-76-78/week-78/ record preserves reviews, revision decisions, final checks and the actual extracted-ZIP reconstruction result. Different TeX/font versions can affect appearance.

The portable ZIP excludes stage prompts, borrowed style examples, downloaded books/papers, external fonts, runtime format files, caches, render images, logs, superseded drafts and private classroom information.
