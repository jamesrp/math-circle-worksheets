#!/bin/sh
# Check every answer, then compile the guide into ../facilitator.pdf.
set -e
cd "$(dirname "$0")"
python3 check_guide.py > check_guide.out && tail -1 check_guide.out
pdflatex -interaction=nonstopmode -halt-on-error facilitator.tex > /dev/null
pdflatex -interaction=nonstopmode -halt-on-error facilitator.tex > /dev/null
grep -E "Overfull|Underfull|Warning" facilitator.log || true
cp facilitator.pdf ../facilitator.pdf
rm -f facilitator.aux facilitator.log facilitator.out facilitator.pdf
