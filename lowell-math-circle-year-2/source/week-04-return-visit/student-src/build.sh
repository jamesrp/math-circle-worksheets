#!/bin/sh
set -eu
task_src=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
task_engine=${PDFLATEX:-pdflatex}
if ! command -v "$task_engine" >/dev/null 2>&1 && [ -x /Library/TeX/texbin/pdflatex ]; then
  task_engine=/Library/TeX/texbin/pdflatex
fi
task_build=${1:-"$task_src/../build"}
mkdir -p "$task_build"
task_build=$(CDPATH= cd -- "$task_build" && pwd)
cd "$task_src"
"$task_engine" -interaction=nonstopmode -halt-on-error -output-directory="$task_build" return-visit.tex >/dev/null
"$task_engine" -interaction=nonstopmode -halt-on-error -output-directory="$task_build" return-visit.tex >/dev/null
cp "$task_build/return-visit.pdf" "$task_src/../return-visit.pdf"
