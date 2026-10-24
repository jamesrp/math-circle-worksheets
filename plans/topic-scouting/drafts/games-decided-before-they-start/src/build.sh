#!/bin/sh
# Build the three packets into the parent folder. Intermediates go in ./build/.
set -e
cd "$(dirname "$0")"
mkdir -p build
for f in k-1 grades-2-3 grades-4-5; do
  [ -f "$f.tex" ] || continue
  pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build "$f.tex" >/dev/null || { tail -30 "build/$f.log"; exit 1; }
  cp "build/$f.pdf" "../$f.pdf"
  echo "$f: $(pdfinfo ../$f.pdf | awk '/Pages/{print $2}') pages"
done
