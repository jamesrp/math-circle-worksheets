#!/bin/sh
set -eu
SOURCE_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
OUTPUT_DIR=${1:-"$SOURCE_DIR/.."}
mkdir -p "$OUTPUT_DIR"
OUTPUT_DIR=$(CDPATH= cd -- "$OUTPUT_DIR" && pwd)
BUILD_DIR="$OUTPUT_DIR/build"
mkdir -p "$BUILD_DIR"
if [ -n "${PDFLATEX:-}" ]; then
  TEX_PROGRAM=$PDFLATEX
elif command -v pdflatex >/dev/null 2>&1; then
  TEX_PROGRAM=pdflatex
elif [ -x /Library/TeX/texbin/pdflatex ]; then
  TEX_PROGRAM=/Library/TeX/texbin/pdflatex
else
  printf '%s\n' 'Install a TeX distribution with pdflatex and TikZ, or set PDFLATEX.' >&2
  exit 1
fi
for PASS in 1 2; do
  "$TEX_PROGRAM" -halt-on-error -interaction=nonstopmode -output-directory "$BUILD_DIR" "$SOURCE_DIR/return-visit.tex"
done
cp "$BUILD_DIR/return-visit.pdf" "$OUTPUT_DIR/return-visit.pdf"
