#!/bin/sh
set -eu
SRC=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
OUT=${1:-"$SRC/../build"}
mkdir -p "$OUT"
python3 "$SRC/generate.py"
TEX=${PDFLATEX:-pdflatex}
for PASS in 1 2; do
  "$TEX" -interaction=nonstopmode -halt-on-error -output-directory="$OUT" "$SRC/return-visit.tex" > "$OUT/compile-$PASS.txt"
done
cp "$OUT/return-visit.pdf" "$OUT/../return-visit.pdf"
