#!/bin/sh
# Re-check every answer, then build the guide into ../facilitator.pdf.
set -e
cd "$(dirname "$0")"
python3 check_guide.py > check_guide.out
mkdir -p build
for i in 1 2; do
  pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build facilitator.tex > /dev/null
done
cp build/facilitator.pdf ../facilitator.pdf
grep -E "Overfull|Underfull|Warning" build/facilitator.log || true
tail -1 check_guide.out
