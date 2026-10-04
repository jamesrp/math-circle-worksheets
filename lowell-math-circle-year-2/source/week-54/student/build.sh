#!/bin/sh
# Build with TeX Live. Usage: sh build.sh OUTPUT_DIRECTORY
set -eu
src_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
output_dir=${1:?Provide an output directory}
mkdir -p "$output_dir"
output_dir=$(CDPATH= cd -- "$output_dir" && pwd)
build_dir=$(mktemp -d "${TMPDIR:-/tmp}/week54-build.XXXXXX")
trap 'rm -rf "$build_dir"' EXIT HUP INT TERM
if ! pdflatex -interaction=nonstopmode -halt-on-error -output-directory "$build_dir" "$src_dir/students.tex" > "$build_dir/compile.txt"; then
  cat "$build_dir/compile.txt"
  exit 1
fi
if ! pdflatex -interaction=nonstopmode -halt-on-error -output-directory "$build_dir" "$src_dir/students.tex" >> "$build_dir/compile.txt"; then
  cat "$build_dir/compile.txt"
  exit 1
fi
cp "$build_dir/students.pdf" "$output_dir/students.pdf"
if grep -E 'Overfull|Underfull|Warning|Error' "$build_dir/students.log"; then :; fi
printf '%s\n' "$output_dir/students.pdf"
