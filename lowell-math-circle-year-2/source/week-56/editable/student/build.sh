#!/bin/sh
set -eu
SRC=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
OUT=${1:-"$SRC/.."}
mkdir -p "$OUT"
OUT=$(CDPATH= cd -- "$OUT" && pwd)
BUILD=$(mktemp -d "${TMPDIR:-/tmp}/week56-build.XXXXXX")
trap 'rm -rf "$BUILD"' EXIT HUP INT TERM
for DOC in students materials; do
  (cd "$SRC" && pdflatex -interaction=nonstopmode -halt-on-error -output-directory="$BUILD" "$DOC.tex" > "$BUILD/$DOC-build.txt") || { cat "$BUILD/$DOC-build.txt"; exit 1; }
  cp "$BUILD/$DOC.pdf" "$OUT/$DOC.pdf"
done
printf 'Built %s/students.pdf and materials.pdf\n' "$OUT"
