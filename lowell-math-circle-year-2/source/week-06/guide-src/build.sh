#!/bin/sh
# Build the Week 6 adult guide: recheck every answer, then compile and copy to final/.
set -e
cd "$(dirname "$0")"
python3 check_guide.py > check_guide.out || { cat check_guide.out; echo "ANSWER CHECK FAILED"; exit 1; }
for i in 1 2; do
  pdflatex -interaction=nonstopmode -halt-on-error facilitator.tex > facilitator.build.log 2>&1 || { tail -40 facilitator.build.log; exit 1; }
done
cp facilitator.pdf ../facilitator.pdf
grep -E "Overfull|Underfull .hbox .badness 10000" facilitator.log || true
pdfinfo ../facilitator.pdf | grep Pages
