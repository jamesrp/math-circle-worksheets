"""Read the small side-view tower pictures in the adult guide (K-1 answers, p.3) from their cube
rectangles and print each picture's heights left to right, with the label printed beside it.

Run:  python3 -I guide_towers.py > guide_towers.out
"""
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import PDF  # noqa: E402
import pdfplumber  # noqa: E402

page = pdfplumber.open(PDF["G"]).pages[2]
cubes = [r for r in page.rects if r.get("fill") and isinstance(r.get("non_stroking_color"), (tuple, list))
         and len(r["non_stroking_color"]) == 3 and r["x1"] - r["x0"] < 8]
cols = defaultdict(list)
for r in cubes:
    cols[round(r["x0"], 1)].append(r)
towers = []
for x, rs in cols.items():
    rs.sort(key=lambda r: r["top"])
    stack = [rs[0]]
    for r in rs[1:]:
        if abs(r["top"] - stack[-1]["bottom"]) < 0.5:
            stack.append(r)
        else:
            towers.append((round(stack[-1]["bottom"]), x, len(stack)))
            stack = [r]
    towers.append((round(stack[-1]["bottom"]), x, len(stack)))
towers.sort()
pics = []
for base, x, h in towers:
    if pics and pics[-1][0] == base and x - pics[-1][1][-1][0] < 9:
        pics[-1][1].append((x, h))
    else:
        pics.append((base, [(x, h)]))
words = page.extract_words()
for base, ts in pics:
    x_end = ts[-1][0]
    label = [w["text"] for w in words if abs(w["bottom"] - base) < 6 and x_end < w["x0"] < x_end + 30]
    print(f"picture at y={base}, x={ts[0][0]}: heights {[h for _, h in ts]}; text right after it: {label[:3]}")
