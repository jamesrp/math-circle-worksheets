#!/bin/sh
set -eu
cd "$(dirname "$0")"
work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT HUP INT TERM
export SOURCE_DATE_EPOCH=1793404800
for pass in 1 2; do
  if ! pdflatex -interaction=nonstopmode -halt-on-error -output-directory="$work" k1-guide.tex >"$work/console.txt" 2>&1; then
    cat "$work/console.txt" >&2
    exit 1
  fi
done
if grep -E 'Overfull \\[hv]box|^!' "$work/k1-guide.log"; then
  echo 'TeX overflow/error found; guide not installed.' >&2
  exit 1
fi
cp "$work/k1-guide.pdf" ../k1-guide.pdf
rm -rf "$work"
trap - EXIT HUP INT TERM
python3 check_guide.py
