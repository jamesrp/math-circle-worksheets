#!/bin/sh
# Build the three packets and copy them to final/
set -e
cd "$(dirname "$0")"
for f in k-1 grades-2-3 grades-4-5; do
  xelatex -interaction=nonstopmode -halt-on-error $f.tex > $f.build.log 2>&1 || { echo "FAILED $f"; tail -30 $f.build.log; exit 1; }
  cp $f.pdf ../$f.pdf
done
