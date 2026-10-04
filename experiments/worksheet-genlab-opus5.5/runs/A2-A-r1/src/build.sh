#!/bin/sh
# Build all three packets: regenerate figures, compile, copy to ../final, render previews.
set -e
cd "$(dirname "$0")"
python3 figs.py > figs.log; head -1 figs.log
for f in k-1 grades-2-3 grades-4-5; do
  pdflatex -interaction=nonstopmode -halt-on-error $f.tex > $f.build.log 2>&1 || { echo "FAILED $f"; tail -30 $f.build.log; exit 1; }
  pdflatex -interaction=nonstopmode -halt-on-error $f.tex > $f.build.log 2>&1
  cp $f.pdf ../final/$f.pdf
  grep -E "Overfull|Underfull|Warning" $f.log | grep -v "Underfull \\\\hbox" | head -5 || true
  echo "$f: $(pdfinfo $f.pdf | grep Pages)"
done
mkdir -p ../preview  # page previews for checking
rm -f ../preview/*.png
for f in k-1 grades-2-3 grades-4-5; do
  pdftoppm -r 60 -png ../final/$f.pdf ../preview/$f
done
