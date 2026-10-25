#!/bin/sh
# Build materials.pdf from materials.tex and check it.
# Run from anywhere: sh src/build.sh
set -e
SRC=$(cd "$(dirname "$0")" && pwd)
RUN=$(dirname "$SRC")
OUT=$(mktemp -d)
pdflatex -interaction=nonstopmode -halt-on-error -output-directory "$OUT" "$SRC/materials.tex" >/dev/null
pdflatex -interaction=nonstopmode -halt-on-error -output-directory "$OUT" "$SRC/materials.tex" >/dev/null
if grep -E "Overfull|Underfull|Warning|Error" "$OUT/materials.log"; then
  echo "LaTeX log has warnings or errors (see above)"; exit 1
fi
cp "$OUT/materials.pdf" "$RUN/materials.pdf"
rm -rf "$OUT"
python3 "$SRC/check_materials.py" "$RUN/materials.pdf"
