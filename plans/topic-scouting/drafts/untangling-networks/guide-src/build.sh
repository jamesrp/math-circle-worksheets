#!/bin/sh
# Rebuild the facilitator guide and re-run its checks.  Needs python3 with networkx, pdflatex, pdftotext.
set -e
cd "$(dirname "$0")"
python3 figs.py
pdflatex -interaction=nonstopmode -halt-on-error facilitator.tex > /dev/null
pdflatex -interaction=nonstopmode -halt-on-error facilitator.tex > /dev/null
grep -E "Overfull|Underfull|Warning" facilitator.log || true
mv facilitator.pdf ../facilitator.pdf
rm -f facilitator.aux facilitator.log facilitator.out
python3 check_guide.py
