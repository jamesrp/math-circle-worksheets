#!/bin/sh
set -eu
SOURCE_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
OUTPUT_DIR=${1:-}
if [ -z "$OUTPUT_DIR" ]; then
  OUTPUT_DIR=$(mktemp -d "${TMPDIR:-/tmp}/week-13-return-visit-build.XXXXXX")
fi
mkdir -p "$OUTPUT_DIR"
OUTPUT_DIR=$(CDPATH= cd -- "$OUTPUT_DIR" && pwd)
if [ -x /Library/TeX/texbin/pdflatex ]; then TEX=/Library/TeX/texbin/pdflatex; else TEX=pdflatex; fi
(cd "$SOURCE_DIR/student" && "$TEX" -halt-on-error -interaction=nonstopmode -output-directory="$OUTPUT_DIR" return-visit.tex > "$OUTPUT_DIR/student-compile.txt")
mv "$OUTPUT_DIR/return-visit.pdf" "$OUTPUT_DIR/week-13-return-visit.pdf"
(cd "$SOURCE_DIR" && "$TEX" -halt-on-error -interaction=nonstopmode -output-directory="$OUTPUT_DIR" facilitator.tex > "$OUTPUT_DIR/guide-compile.txt")
mv "$OUTPUT_DIR/facilitator.pdf" "$OUTPUT_DIR/week-13-return-visit-facilitator.pdf"
python3 "$SOURCE_DIR/independent_checks.py" 13
printf '%s\n' "$OUTPUT_DIR/week-13-return-visit.pdf" "$OUTPUT_DIR/week-13-return-visit-facilitator.pdf"
