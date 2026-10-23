#!/bin/sh
set -eu
src=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
out=${1:?Usage: sh build.sh /absolute/output/directory}
mkdir -p "$out"
out=$(CDPATH= cd -- "$out" && pwd)
work=$(mktemp -d "${TMPDIR:-/tmp}/week52-guide-build.XXXXXX")
trap 'rm -rf "$work"' EXIT HUP INT TERM
export SOURCE_DATE_EPOCH=1791072000
export FORCE_SOURCE_DATE=1
cd "$src"
pdflatex -interaction=nonstopmode -halt-on-error -output-directory="$work" facilitator.tex > "$work/build.log"
pdflatex -interaction=nonstopmode -halt-on-error -output-directory="$work" facilitator.tex >> "$work/build.log"
if grep -E 'Overfull \\hbox|Overfull \\vbox' "$work/facilitator.log"; then exit 1; fi
cp "$work/facilitator.pdf" "$out/facilitator.pdf"
