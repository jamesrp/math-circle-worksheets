#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
work=$(mktemp -d "${TMPDIR:-/tmp}/week91-k1-guide.XXXXXX")
trap 'rm -rf "$work"' EXIT
for pass in 1 2; do
  pdflatex -halt-on-error -interaction=nonstopmode -output-directory="$work" k1-guide.tex > "$work/compile-$pass.txt"
done
if grep -Eq 'Overfull \\[hv]box|LaTeX Error|Missing character:' "$work/k1-guide.log"; then
  cat "$work/k1-guide.log"
  exit 1
fi
cp "$work/k1-guide.pdf" ../k1-guide.pdf
printf 'pdfLaTeX: two passes, no errors, missing glyphs or overfull boxes.\n'
rm -rf "$work"
trap - EXIT
python3 check_guide.py
