#!/usr/bin/env python3
"""Week 39 math check: confirm the editable source (source/week-39/editable/src/
make_packets.py) describes the same maps, routes and problem texts as the
delivered PDFs (extracted.json from extract.py).  Positions are compared after
converting the source's mm grid (x=1mm, y=-1mm from the top) to pt.
Standard library only.  Run: python3 compare_source.py > out_compare_source.txt
"""
import ast
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def find_repo():
    cand = HERE.parents[3] if len(HERE.parents) > 3 else None
    if cand and (cand / "lowell-math-circle-year-2").is_dir():
        return cand
    for p in [HERE] + list(HERE.parents):
        if (p / "lowell-math-circle-year-2").is_dir():
            return p
    sys.exit("repository not found above " + str(HERE))


REPO = find_repo()
SRC = (REPO / "lowell-math-circle-year-2/source/week-39/editable/src/make_packets.py").read_text()
PDF = json.loads((HERE / "extracted.json").read_text())
MM = 72 / 25.4
FAIL = []


def ok(c, m):
    print(("  ok   " if c else "  FAIL ") + m)
    if not c:
        FAIL.append(m)


def const(name):
    m = re.search(rf"^{name}=(.*)$", SRC, re.M)
    return ast.literal_eval(m.group(1))


NODES = {"tree": const("TREE"), "ring": const("RING"), "bow": const("EIGHT")}
EDGES = {"tree": const("TEDGES"), "ring": const("REDGES"), "bow": const("EEDGES")}
# graph(x, y, sc, NODES, EDGES) calls, in source order, per band branch.
calls = [(float(a), float(b), float(c), n) for a, b, c, n in
         re.findall(r"graph\((\d+),(\d+),(\d+),(TREE|RING|EIGHT),", SRC)]
print("source graph() calls:", calls)
kind = {"TREE": "tree", "RING": "ring", "EIGHT": "bow"}

for band, pages in PDF.items():
    for pg in pages:
        m = pg["map"]
        if not m["nodes"]:
            continue
        P = {n["label"]: (n["x"], n["y"]) for n in m["nodes"]}
        k = "bow" if "H" in P else "tree" if "E" in P else "ring"
        # Find a source call reproducing these centres.
        hit = None
        for x, y, sc, nm in calls:
            if kind[nm] != k:
                continue
            if all(abs((x + a * sc) * MM - P[v][0]) < 0.05 and abs((y + b * sc) * MM - P[v][1]) < 0.05
                   for v, (a, b) in NODES[k].items()):
                hit = (x, y, sc)
        edges_pdf = sorted("".join(sorted(e["a"] + e["b"])) for e in m["edges"])
        edges_src = sorted("".join(sorted(e)) for e in EDGES[k])
        ok(hit is not None and edges_pdf == edges_src,
           f"{band} p{pg['page']}: {k} centres = source graph{hit}, edges identical")

routes_src = re.findall(r"routes\(\d+,(\[[^\]]*\])", SRC)
routes_src = [ast.literal_eval(r) for r in routes_src]
pdf_routes = [[r["route"] for r in pg["routes"] if r["route"]] for band in ("grades-2-3", "grades-4-5")
              for pg in PDF[band] if any(r["route"] for r in pg["routes"])]
ok(sorted(map(tuple, routes_src)) == sorted(set(map(tuple, pdf_routes))),
   f"printed routes match source lists {routes_src}")


def norm(s):
    return re.sub(r"\s+", " ", s.replace("\\textbf{", "").replace("}", "")).strip()


src_q = [norm(q) for q in re.findall(r"problem\(\d+,\d+,'([^']*)'", SRC)] + \
        [norm(q) for q in re.findall(r"q='([^']*)'", SRC)]
for band, pages in PDF.items():
    for pg in pages:
        for p in pg["problems"]:
            body = norm(p["text"].split(":", 1)[1])
            ok(body in src_q, f"{band} p{pg['page']} {p['text'][:10]}: text matches source")
print("\nSUMMARY:", "all checks passed" if not FAIL else f"{len(FAIL)} failed")
