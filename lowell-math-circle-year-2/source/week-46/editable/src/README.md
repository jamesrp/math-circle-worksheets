# Student packets

The student pages' source is the Week 46 problem files: `week.toml`, `figures.py` and `problems/*.md`, in `../problem-files/` inside the portable ZIP and in `lowell-math-circle-year-2/source/week-46/` in the repository. Edit a problem there, not here.

Run `bash build.sh` in this directory with Python 3.11+, pdfLaTeX, TikZ, Latin Modern and Poppler installed. It runs `regenerate.py`, which writes `k-1.tex`, `grades-2-3.tex` and `grades-4-5.tex` from the problem files, then `common.py`, which compiles each twice, saves the three PDFs one directory above and renders every page into `../render/`. `check.py` is the original enumeration check. The builder these files replaced, `write.py`, is archived in the repository's `source/week-46/archive-before-problem-files-2026-10-23/`.
