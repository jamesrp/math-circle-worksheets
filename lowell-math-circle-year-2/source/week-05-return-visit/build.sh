#!/bin/sh
set -eu
TASK_SOURCE_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
TASK_OUTPUT_DIR=${1:-$(mktemp -d "${TMPDIR:-/tmp}/math-circle-week-05-return-visit.XXXXXX")}
mkdir -p "$TASK_OUTPUT_DIR"
TASK_OUTPUT_DIR=$(CDPATH= cd -- "$TASK_OUTPUT_DIR" && pwd)
TASK_TEX_BUILD="$TASK_OUTPUT_DIR/tex-build"
mkdir -p "$TASK_TEX_BUILD/student" "$TASK_TEX_BUILD/guide"
TASK_PDFLATEX=${PDFLATEX:-pdflatex}
if ! command -v "$TASK_PDFLATEX" >/dev/null 2>&1; then
  if [ -x /Library/TeX/texbin/pdflatex ]; then TASK_PDFLATEX=/Library/TeX/texbin/pdflatex; else printf '%s\n' 'pdfLaTeX with TikZ and Latin Modern is required.' >&2; exit 1; fi
fi
export SOURCE_DATE_EPOCH=1791072000
export FORCE_SOURCE_DATE=1
(cd "$TASK_SOURCE_DIR/student-src" && for TASK_TEX_PASS in 1 2; do "$TASK_PDFLATEX" -interaction=nonstopmode -halt-on-error -output-directory="$TASK_TEX_BUILD/student" return-visit.tex > "$TASK_TEX_BUILD/student/compile.txt"; done)
(cd "$TASK_SOURCE_DIR/guide-src" && for TASK_TEX_PASS in 1 2; do "$TASK_PDFLATEX" -interaction=nonstopmode -halt-on-error -output-directory="$TASK_TEX_BUILD/guide" facilitator.tex > "$TASK_TEX_BUILD/guide/compile.txt"; done)
cp "$TASK_TEX_BUILD/student/return-visit.pdf" "$TASK_OUTPUT_DIR/week-05-return-visit.pdf"
cp "$TASK_TEX_BUILD/guide/facilitator.pdf" "$TASK_OUTPUT_DIR/week-05-return-visit-facilitator.pdf"
printf '%s\n' "$TASK_OUTPUT_DIR/week-05-return-visit.pdf" "$TASK_OUTPUT_DIR/week-05-return-visit-facilitator.pdf"
