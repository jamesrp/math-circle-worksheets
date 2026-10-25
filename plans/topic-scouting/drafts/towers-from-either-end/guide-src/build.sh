#!/bin/sh
# Rebuild ../facilitator.pdf with pdfLaTeX (two passes), then re-run the answer checks.
set -e
cd "$(dirname "$0")"
for i in 1 2; do pdflatex -interaction=nonstopmode -halt-on-error facilitator.tex > /dev/null; done
grep -E "Overfull|Underfull" facilitator.log || true
mv facilitator.pdf ../facilitator.pdf
rm -f facilitator.aux facilitator.log facilitator.out
python3 check_guide.py | tail -1
