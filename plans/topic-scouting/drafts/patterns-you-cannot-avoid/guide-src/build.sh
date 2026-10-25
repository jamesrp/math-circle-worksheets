#!/bin/sh
# Check every number in the guide, draw the figures, compile, and put facilitator.pdf in the folder above.
set -e
cd "$(dirname "$0")"
python3 check_guide.py > check_guide.out
python3 figs.py
pdflatex -interaction=nonstopmode -halt-on-error facilitator.tex > /dev/null
pdflatex -interaction=nonstopmode -halt-on-error facilitator.tex > /dev/null
grep -E "Overfull|Underfull|Warning" facilitator.log && exit 1 || true
mv facilitator.pdf ../facilitator.pdf
rm -f facilitator.aux facilitator.log
