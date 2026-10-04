#!/bin/sh
set -eu
src_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
out_dir=${1:-"$src_dir/.."}
mkdir -p "$out_dir"
out_dir=$(CDPATH= cd -- "$out_dir" && pwd)
build_dir=$(mktemp -d "${TMPDIR:-/tmp}/week52-build.XXXXXX")
trap 'rm -rf "$build_dir"' EXIT HUP INT TERM
if ! pdflatex -interaction=nonstopmode -halt-on-error -output-directory "$build_dir" "$src_dir/students.tex" > "$build_dir/console.log"; then
  cat "$build_dir/console.log" >&2
  exit 1
fi
cp "$build_dir/students.pdf" "$out_dir/students.pdf"
printf '%s\n' "$out_dir/students.pdf"
