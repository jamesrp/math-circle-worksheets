# Revised student packet

The student pages' source is the Week 42 problem files: `week.toml`, `figures.py` and `problems/*.md`, in `../problem-files/` inside the portable ZIP and in `lowell-math-circle-year-2/source/week-42/` in the repository. Edit a problem there, not here. `regenerate.py` writes `k-1.tex`, `grades-2-3.tex` and `grades-4-5.tex` from them; the builder they replaced, `write.py`, is archived in the repository's `source/week-42/archive-before-problem-files-2026-10-23/`.

Run bash build.sh in this directory with Python 3.11+, pdfLaTeX, TikZ, Latin Modern, and Poppler installed. The build regenerates the three editable TeX files, runs the author check `check.py`, compiles each file twice with `common.py`, saves the three PDFs one directory above, and renders every page into ../render/. To compile manual TeX edits without regenerating them, run python3 common.py. Independent revision verification is in ../qa/.
