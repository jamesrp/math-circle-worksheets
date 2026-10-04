# Week 5 return-visit revised sources

This is the reviewed revision: one shared Grades 2–5 packet, three pages,
Problems 1–3. The run outline explicitly replaces the general harness's
three-band output rule and minimum page count.

Build with a TeX Live installation including pdfLaTeX, TikZ, and Latin Modern:

```sh
sh build.sh
```

An optional first argument chooses the build-intermediate directory. `PDFLATEX`
can choose another pdfLaTeX executable. The script writes `../return-visit.pdf`.
No absolute repository path appears in the editable sources.

Check the actual city inputs with Python 3 (standard library only):

```sh
python3 check_math.py
```

Render every page and check text bounds and actual working-grid dimensions
with Python 3 plus PyMuPDF:

```sh
python3 check_and_render.py
```

The large grids on pages 2 and 3 have 25 mm squares. Print on US Letter paper
at 100%. Page 1 cities and page 3 invented cities are explicitly built on the
table; their compact grids are height records. Physical cube fit and classroom
use remain untested.

The fresh critic and independent math critic supported all three investigations.
Problem 1 now specifies one printed city at a time and a reset to that original
city for each trial. No mathematical rules, examples, or grid sizes changed.
