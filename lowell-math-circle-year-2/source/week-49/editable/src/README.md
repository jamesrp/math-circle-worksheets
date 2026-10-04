Rebuild the three student packets

Requirements: Python 3, a standard TeX Live installation with pdfLaTeX, TikZ, fancyhdr, amsmath and amssymb, and Poppler pdftoppm.

From this directory run:

    bash build.sh

The script regenerates the TeX files from make.py, compiles the PDFs one directory above, and renders every page into ../qa/. All source dependencies are relative to this directory. Print on US Letter at 100 percent scale.
