Rebuild the three student packets

The student pages' source is the Week 49 problem files: `week.toml`, `figures.py` and `problems/*.md`, in `../problem-files/` inside the portable ZIP and in `lowell-math-circle-year-2/source/week-49/` in the repository. Edit a problem there, not here.

Requirements: Python 3.11+, a standard TeX Live installation with pdfLaTeX, TikZ, fancyhdr, amsmath and amssymb, and Poppler pdftoppm.

From this directory run:

    bash build.sh

The script runs `regenerate.py`, which writes `k-1.tex`, `grades-2-3.tex` and `grades-4-5.tex` from the problem files, compiles the PDFs one directory above, and renders every page into ../qa/. `check.py` holds the checks the old builder ran (`checks.txt` records their results) and, since the October 23, 2026 card fixes, checks of every changed order, run, count and key. The builder these files replaced, `make.py` with `draw.py`, is archived in the repository's `source/week-49/archive-before-problem-files-2026-10-23/`. Print on US Letter at 100 percent scale.
