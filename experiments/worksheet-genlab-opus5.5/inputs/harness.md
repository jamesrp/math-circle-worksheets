Technical instructions

Your working directory is {{RUN_DIR}}. Keep all your files inside it: LaTeX sources in {{RUN_DIR}}/src/ and the three finished PDFs at exactly these paths:

  {{RUN_DIR}}/final/k-1.pdf
  {{RUN_DIR}}/final/grades-2-3.pdf
  {{RUN_DIR}}/final/grades-4-5.pdf

The deliverable is the student pages only. There is no separate facilitator guide.

Tools available: pdflatex, xelatex, lualatex (TeX Live with TikZ and texlive-fonts-extra), python3, pdftoppm, pdftotext. Draw diagrams with TikZ or with Python-generated TikZ. Before you finish, compile each PDF, render its pages to PNG (for example `pdftoppm -r 60 -png file.pdf prefix`), and look at every page with the Read tool to check that the diagrams are correct and nothing overflows or overlaps. Fix what you find.

Isolation: this is a controlled experiment. Use only the information in these instructions. Do not read any file outside {{RUN_DIR}} (in particular nothing elsewhere under /home/claude/genlab and nothing under /mnt/user-data), do not use web search or web fetch, and do not use any remote-device, computer, or browser tools.

When you are done, reply with the three PDF paths and their page counts, in under 80 words.
