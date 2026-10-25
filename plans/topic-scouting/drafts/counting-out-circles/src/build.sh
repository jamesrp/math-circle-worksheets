#!/bin/sh
# Rebuild the three packets into the draft folder and re-check every answer.
set -e
python3 make_mat32.py
for t in k-1 grades-2-3 grades-4-5; do
  pdflatex -interaction=nonstopmode -halt-on-error $t.tex >/dev/null
  pdflatex -interaction=nonstopmode -halt-on-error $t.tex >/dev/null
  cp $t.pdf ..
done
python3 check.py >/dev/null
python3 check_final.py
