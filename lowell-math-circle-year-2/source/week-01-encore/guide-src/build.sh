#!/bin/sh
# Recheck every answer (writes the answer pictures to figs/), then build ../facilitator.pdf.
# Pass --fast to skip the slow full game search on the 4-by-4 board.
set -e
cd "$(dirname "$0")"
python3 check.py "$@"
for i in 1 2; do
  pdflatex -interaction=nonstopmode -halt-on-error facilitator.tex > /dev/null || { tail -30 facilitator.log; exit 1; }
done
cp facilitator.pdf ../facilitator.pdf
