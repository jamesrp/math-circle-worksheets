#!/bin/bash
# usage: build.sh name prefix
D=/home/claude/genlab/runs/A1-B-r1/src
cd "$D" || exit 1
xelatex -interaction=nonstopmode -halt-on-error "$1.tex" > /dev/null 2>&1
xelatex -interaction=nonstopmode -halt-on-error "$1.tex" > /dev/null 2>&1
echo "== $1"; grep -E "^!|Overfull|Underfull \\\\vbox" "$1.log" | head; pdfinfo "$1.pdf" | grep Pages
mkdir -p "$D/png"
pdftoppm -r 60 -png "$1.pdf" "$D/png/$2"
