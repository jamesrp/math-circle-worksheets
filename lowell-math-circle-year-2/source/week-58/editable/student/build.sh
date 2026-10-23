#!/bin/sh
set -eu
# Usage: sh build.sh /absolute/or/relative/output-directory
# Standard TeX Live: pdflatex, TikZ, helvet, fancyhdr, geometry, pdflscape.
task_src=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
task_out=${1:-"$task_src/.."}
mkdir -p "$task_out"
task_out=$(CDPATH= cd -- "$task_out" && pwd)
task_build=$(mktemp -d "${TMPDIR:-/tmp}/week58-build.XXXXXX")
trap 'rm -rf "$task_build"' EXIT HUP INT TERM
export SOURCE_DATE_EPOCH=1791072000
export FORCE_SOURCE_DATE=1
cd "$task_src"
for task_doc in students materials; do
  if ! pdflatex -interaction=nonstopmode -halt-on-error -output-directory="$task_build" "$task_doc.tex" > "$task_build/$task_doc-build.log"; then
    cat "$task_build/$task_doc-build.log" >&2
    exit 1
  fi
  cp "$task_build/$task_doc.pdf" "$task_out/$task_doc.pdf"
done
