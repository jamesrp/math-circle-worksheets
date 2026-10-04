#!/bin/sh
# Portable guide build: sh build.sh OUTPUT_DIRECTORY
set -eu
src_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
output_dir=${1:?Provide an output directory}
mkdir -p "$output_dir"
output_dir=$(CDPATH= cd -- "$output_dir" && pwd)
build_dir=$(mktemp -d "${TMPDIR:-/tmp}/week54-guide-build.XXXXXX")
trap 'rm -rf "$build_dir"' EXIT HUP INT TERM
for pass in 1 2; do
  if ! pdflatex -interaction=nonstopmode -halt-on-error -output-directory "$build_dir" "$src_dir/facilitator.tex" > "$build_dir/compile-$pass.txt"; then
    cat "$build_dir/compile-$pass.txt"
    exit 1
  fi
done
cp "$build_dir/facilitator.pdf" "$output_dir/facilitator.pdf"
if grep -E 'Overfull|Underfull|Warning|Error' "$build_dir/facilitator.log"; then :; fi
printf '%s\n' "$output_dir/facilitator.pdf"
