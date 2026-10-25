#!/bin/sh
# Build the Hidden armies facilitator guide: checks every answer, then compiles
# facilitator.tex (which inputs solutions.tex) into ../facilitator.pdf.
# Run from this folder: sh build.sh
set -e
cd "$(dirname "$0")"
python3 check_guide.py > check_guide.out
tail -1 check_guide.out
OUT="${TMPDIR:-/tmp}/hidden-armies-guide-build"
mkdir -p "$OUT"
for i in 1 2; do
  pdflatex -interaction=nonstopmode -halt-on-error -output-directory "$OUT" facilitator.tex > "$OUT/run.txt"
done
grep -E "Overfull|Underfull|LaTeX Warning|Error" "$OUT/facilitator.log" || echo "log clean"
cp "$OUT/facilitator.pdf" ../facilitator.pdf
echo "wrote $(cd .. && pwd)/facilitator.pdf"
