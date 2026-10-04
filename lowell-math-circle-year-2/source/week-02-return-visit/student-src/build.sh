#!/bin/sh
set -eu
source_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
draft_dir=$(dirname -- "$source_dir")
build_dir="$draft_dir/build"
mkdir -p "$build_dir"
pdflatex_command=${PDFLATEX:-/Library/TeX/texbin/pdflatex}
"$pdflatex_command" -halt-on-error -interaction=nonstopmode -output-directory "$build_dir" "$source_dir/return-visit.tex"
"$pdflatex_command" -halt-on-error -interaction=nonstopmode -output-directory "$build_dir" "$source_dir/return-visit.tex"
cp "$build_dir/return-visit.pdf" "$draft_dir/return-visit.pdf"
