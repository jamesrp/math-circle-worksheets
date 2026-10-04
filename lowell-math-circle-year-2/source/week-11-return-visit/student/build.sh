#!/bin/sh
set -eu
SRC_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
OUT_DIR=$(CDPATH= cd -- "$SRC_DIR/.." && pwd)
BUILD_DIR="$OUT_DIR/build"
mkdir -p "$BUILD_DIR"
if [ -x /Library/TeX/texbin/pdflatex ]; then
  PDFLATEX=/Library/TeX/texbin/pdflatex
else
  PDFLATEX=pdflatex
fi
"$PDFLATEX" -halt-on-error -interaction=nonstopmode -output-directory="$BUILD_DIR" "$SRC_DIR/return-visit.tex" > "$BUILD_DIR/compiler.log"
cp "$BUILD_DIR/return-visit.pdf" "$OUT_DIR/return-visit.pdf"
