# Independent Week 10 mathematics evidence

`independent_check.py` is the fresh CRITIC-MATH checker. It does not import, call or copy logic from the writer's `check_math.py` or `check_pdf.py`. Its bundled `towns.json` is an exact copy of the authoritative draft data. The JSON result records hashes of the reviewed PDF and data.

Requirements: Python 3 with PyMuPDF (`import pymupdf`). This is optional QA, outside the worksheet's standard-library/TeX build.

From this directory, using a Python interpreter with PyMuPDF:

```sh
python3 independent_check.py --pdf ../draft/return-visit.pdf --out . > independent-check.txt
```

Supply any paths when the evidence is packaged elsewhere:

```sh
python3 /path/to/independent_check.py --pdf /path/to/return-visit.pdf --out /path/to/results
```

By default the checker reads `towns.json` beside itself. `--towns /path/to/towns.json` overrides that path. It writes `independent-check.json` to the explicit output directory; standard output is the readable enumeration and clearance report.

The checker exhausts directed trails from every starting vertex, undirected trails from every actual star, every binary row through length 10 and circle through length 8, and rotation classes of the shortest circles. It independently parses actual PDF vectors and text to verify inch scaling, labeled islands, edges, midpoint counters, arrow orientation and full footprint clearance, stars, and all three convention examples.

`page-01.png` through `page-07.png` are fresh renders inspected during this review. The accompanying text and drawings JSON files preserve extraction evidence. They need not be included in a portable source package. Physical material fit and classroom piloting were not rehearsed.
