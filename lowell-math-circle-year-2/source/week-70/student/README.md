# Week 70 student prototype

One four-page shared Grades 4–5 independently reviewed prototype awaiting organizer review, unpiloted. Requires straightedge use, matching points in repeated squares, and following a continuous line through portals. The last page asks for a general explanation and minimality argument; it is readiness-dependent. These are ideal point shields, with no positive blocking radius. Physical tracing and counter use have not been rehearsed with children.

Build with `python3 build.py` or `python3 build.py --out /chosen/directory`; Python 3 and a working pdfLaTeX installation with TikZ, geometry, fancyhdr, amsmath, amssymb, array and Latin Modern are required. No network or repository files are needed. Run `python3 check_math.py` for exact rational checks of 10,201 target lifts, first-target normalization, the four midpoint locations, the revised repeated-shield seam example and all four required target choices. The disjoint open quadrants of the four short diagonal shots supply the lower bound independently of the numerical sample.

Primary mathematical reference: Samuel Lelièvre, Thierry Monteil and Barak Weiss, *Everything is illuminated*, Lemma 12, PDF p. 12: https://arxiv.org/pdf/1407.2975 . Student wording and diagrams are newly authored; no reference text is bundled.

Digital QA: four final pages built, rendered and inspected individually at 120 dpi; isolated source-only rebuild and exact mathematical checks pass, with no overfull box warnings. `students.tex` is the editable entrypoint. The build writes `students.pdf` and `build.log` into the requested output directory.
