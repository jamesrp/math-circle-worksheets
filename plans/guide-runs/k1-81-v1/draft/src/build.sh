#!/bin/sh
set -eu
cd "$(dirname "$0")"
python3 check_guide.py --write-data
out=$(mktemp -d)
trap 'rm -rf "$out"' EXIT HUP INT TERM
for pass in 1 2; do
  pdflatex -interaction=nonstopmode -halt-on-error -output-directory="$out" k1-guide.tex > "$out/pass-$pass.txt"
done
if grep -q 'Overfull' "$out/k1-guide.log"; then
  grep -A3 -B2 'Overfull' "$out/k1-guide.log" >&2
  exit 1
fi
cp "$out/k1-guide.pdf" ../k1-guide.pdf
rm -rf "$out"
trap - EXIT HUP INT TERM
python3 check_guide.py
