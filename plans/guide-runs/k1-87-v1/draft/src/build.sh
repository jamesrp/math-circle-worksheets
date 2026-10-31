#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT
for pass in 1 2; do
  pdflatex -interaction=nonstopmode -halt-on-error -file-line-error \
    -output-directory="$work" k1-guide.tex > "$work/build-$pass.txt"
done
if grep -Eq 'Overfull|LaTeX Warning|Package .* Warning|Missing character' "$work/k1-guide.log"; then
  cat "$work/k1-guide.log" >&2
  echo "Guide build produced a warning; refusing delivery." >&2
  exit 1
fi
cp "$work/k1-guide.pdf" ../k1-guide.pdf
rm -rf "$work"
trap - EXIT
python3 check_guide.py
