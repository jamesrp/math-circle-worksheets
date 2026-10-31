#!/bin/sh
set -eu
cd "$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
python3 check_guide.py --write-answers
work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT HUP INT TERM
for pass in 1 2; do
  pdflatex -interaction=nonstopmode -halt-on-error -file-line-error \
    -output-directory "$work" k1-guide.tex > "$work/pass-$pass.txt" 2>&1 || {
      cat "$work/pass-$pass.txt" >&2; exit 1;
    }
done
if grep -E 'Overfull|^!' "$work/k1-guide.log"; then
  echo 'Build rejected: TeX error or overfull box.' >&2; exit 1
fi
cp "$work/k1-guide.pdf" ../k1-guide.pdf
rm -rf "$work"
trap - EXIT HUP INT TERM
python3 check_guide.py
