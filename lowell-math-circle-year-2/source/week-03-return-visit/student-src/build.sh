#!/bin/sh
set -eu
task_src=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
task_out=${1:-"$task_src/../build"}
mkdir -p "$task_out"
task_out=$(CDPATH= cd -- "$task_out" && pwd)
if [ -n "${PDFLATEX:-}" ]; then task_tex=$PDFLATEX
elif command -v pdflatex >/dev/null 2>&1; then task_tex=$(command -v pdflatex)
else task_tex=/Library/TeX/texbin/pdflatex
fi
cd "$task_src"
"$task_tex" -interaction=nonstopmode -halt-on-error -output-directory="$task_out" return-visit.tex
"$task_tex" -interaction=nonstopmode -halt-on-error -output-directory="$task_out" return-visit.tex
cp "$task_out/return-visit.pdf" "$task_src/../return-visit.pdf"
