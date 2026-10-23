Rebuild the three student packets

The student pages' source is the Week 47 problem files: `week.toml`, `figures.py` and `problems/*.md`, in `../problem-files/` inside the portable ZIP and in `lowell-math-circle-year-2/source/week-47/` in the repository. Edit a problem there, not here.

Requirements: Python 3.11+, a standard TeX Live installation with pdfLaTeX, TikZ, fancyhdr, amsmath and amssymb, and Poppler pdftoppm.

From this directory run:

    bash build.sh

The script runs `regenerate.py`, which writes `k-1.tex`, `grades-2-3.tex` and `grades-4-5.tex` from the problem files, then `check.py` (the old builder's enumeration of the seven-site problem, which writes `checks.txt`) and `check_examples.py` (the page 1 example), compiles the PDFs one directory above, and renders every page into ../qa/. The builder these files replaced, `make.py` with `draw.py` and `examples.py`, is archived in the repository's `source/week-47/archive-before-problem-files-2026-10-23/`. Print on US Letter at 100 percent scale.
