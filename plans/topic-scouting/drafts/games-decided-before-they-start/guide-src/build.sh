#!/bin/sh
# Build the facilitator guide into ../facilitator.pdf. Intermediates go in ./build/.
set -e
cd "$(dirname "$0")"
mkdir -p build
python3 check_guide.py > check_guide.out
for i in 1 2; do
  pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build facilitator.tex >/dev/null || { tail -30 build/facilitator.log; exit 1; }
done
cp build/facilitator.pdf ../facilitator.pdf
echo "facilitator: $(pdfinfo ../facilitator.pdf | awk '/Pages/{print $2}') pages"
grep -E "Overfull|Underfull|Warning" build/facilitator.log || echo "no box or other warnings"
