#!/bin/sh
set -eu
cd "$(dirname "$0")"
python3 check_guide.py --write-tables
work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT HUP INT TERM
pdflatex -halt-on-error -interaction=nonstopmode -output-directory="$work" facilitator.tex > "$work/build.stdout" || { cat "$work/build.stdout" >&2; exit 1; }
pdflatex -halt-on-error -interaction=nonstopmode -output-directory="$work" facilitator.tex >> "$work/build.stdout" || { cat "$work/build.stdout" >&2; exit 1; }
if grep -E 'Overfull \\[hv]box' "$work/facilitator.log"; then
  echo 'Overfull box: build rejected' >&2
  exit 1
fi
cp "$work/facilitator.pdf" ../facilitator.pdf
rm -rf "$work"
trap - EXIT HUP INT TERM
python3 check_guide.py
