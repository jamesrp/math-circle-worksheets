#!/bin/sh
# Build materials.pdf into the parent folder. Intermediates go in ./build/.
# Two runs: the pages are drawn relative to the page corner (remember picture).
set -e
cd "$(dirname "$0")"
mkdir -p build
for run in 1 2; do
  pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build materials.tex >/dev/null || { tail -30 build/materials.log; exit 1; }
done
if grep -E 'Overfull|Underfull|Warning' build/materials.log; then echo "check the warnings above"; fi
cp build/materials.pdf ../materials.pdf
echo "materials: $(pdfinfo ../materials.pdf | awk '/Pages/{print $2}') pages"
