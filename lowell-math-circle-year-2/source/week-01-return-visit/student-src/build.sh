#!/bin/sh
set -eu
SRC_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
OUTPUT_DIR=$(dirname -- "$SRC_DIR")
TEX_ENGINE=${TEX_ENGINE:-/Library/TeX/texbin/pdflatex}
mkdir -p "$OUTPUT_DIR/build"
"$TEX_ENGINE" -interaction=nonstopmode -halt-on-error -output-directory="$OUTPUT_DIR/build" "$SRC_DIR/return-visit.tex"
cp "$OUTPUT_DIR/build/return-visit.pdf" "$OUTPUT_DIR/return-visit.pdf"
