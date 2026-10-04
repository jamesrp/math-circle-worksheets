# Revised student packet

Run bash build.sh in this directory with Python 3, pdfLaTeX, TikZ, Latin Modern, and Poppler installed. Sources are self-contained and use relative paths. The build regenerates the three editable TeX files, compiles each twice, saves the three PDFs one directory above, and renders every page into ../render/. To compile manual TeX edits without regenerating them, run python3 common.py. The original author check is check.py; independent revision verification is in ../qa/.
