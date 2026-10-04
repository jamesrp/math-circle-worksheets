#!/bin/sh
set -eu
src=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
out=${1:?Usage: sh build.sh OUTPUT_DIRECTORY}
mkdir -p "$out"
out=$(CDPATH= cd -- "$out" && pwd)
work=$(mktemp -d "${TMPDIR:-/tmp}/week56-guide.XXXXXX")
trap 'rm -rf "$work"' EXIT HUP INT TERM
cp "$src/facilitator.tex" "$work/"
cd "$work"
pdflatex -interaction=nonstopmode -halt-on-error facilitator.tex > build.log 2>&1 || { cat build.log; exit 1; }
pdflatex -interaction=nonstopmode -halt-on-error facilitator.tex >> build.log 2>&1 || { cat build.log; exit 1; }
if grep -E 'Overfull|Missing character' build.log; then exit 1; fi
cp facilitator.pdf "$out/facilitator.pdf"
