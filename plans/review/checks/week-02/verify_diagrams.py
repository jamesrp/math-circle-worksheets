#!/usr/bin/env python3
"""Check every printed start->target pair against the instance data.

Uses extracted.json (from extract.py, which reads the actual PDFs) and the
graph/instance data files. For each arrow it finds the start and target
pictures, maps printed lamps to data vertices by geometry, and checks:
  * the printed lines equal the data edges,
  * printed ON dots equal the data start/target sets,
  * the picture uses equal x and y scale (regular polygons stay regular),
  * start and target pictures in a pair are drawn at the same size.
Prints one line per pair with the decoded (graph, start, target) for the
mathematical checks in solve.py.
"""
import os as _os
HERE = _os.path.dirname(_os.path.abspath(__file__))
ROOT = _os.path.normpath(_os.path.join(HERE, '..', '..', '..', '..'))
import json
import math

RUN = HERE + '/'
SNAP = ROOT + '/'
EX = json.load(open(RUN + "extracted.json"))
SH = json.load(open(SNAP + "plans/week-02-shared-data.json"))
UP = json.load(open(SNAP + "plans/week-02-catalog-upper-data.json"))


def up_graph(name):
    g = UP["graphs"][name]
    if "cycle" in g:
        n = g["cycle"]
        xy = [(math.sin(2 * math.pi * i / n), math.cos(2 * math.pi * i / n)) for i in range(n)]
        edges = [(i + 1, (i + 1) % n + 1) for i in range(n)]
        return xy, edges
    return [tuple(p) for p in g["xy"]], [tuple(e) for e in g["edges"]]


def sh_graph(name):
    g = SH["graphs"][name]
    return [tuple(p) for p in g["xy"]], [tuple(e) for e in g["edges"]]


# Expected pairs in reading order, per file and page: (label, graphfn, name, start, target)
INST = {c["problem"]: c for c in SH["checks"]}
cat_expected = {1: [], 2: [], 3: [], 4: []}
for prob, page, src in [(1, 1, 2), (2, 1, 5), (3, 1, None), (4, 2, 7), (5, 2, 8),
                        (6, 3, 9), (7, 3, 10), (8, 4, 11)]:
    if src is None:
        cat_expected[page].append((f"P{prob}", sh_graph, "ring6", [1], [1]))
        continue
    c = INST[src]
    for k, t in enumerate(c["targets"]):
        cat_expected[page].append((f"P{prob}.{k+1}", sh_graph, c["graph"], c["start"], t))
up_expected = {}
for p in UP["problems"]:
    up_expected[p["number"]] = [(f"P{p['number']}{chr(65+i)}", up_graph, c["graph"], c["start"], c["target"])
                                for i, c in enumerate(p.get("cases", []))]


def arrows_of(page):
    """Group 3-segment arrows; return list of (orientation, tail, head)."""
    segs = page["arrows"]
    out = []
    # shafts are the long segments
    for a, b in segs:
        if math.dist(a, b) > 12:
            out.append((a, b))
    res = []
    for a, b in out:
        horiz = abs(a[1] - b[1]) < 0.5
        res.append(("h" if horiz else "v", a, b))
    return res


def comps_with_box(page):
    return page["components"]


def pick(page, arrow, ncomp):
    kind, a, b = arrow
    comps = page["components"]
    if kind == "h":
        y = a[1]
        x0, x1 = min(a[0], b[0]), max(a[0], b[0])
        row = [c for c in comps if c["bbox"][1] - 40 <= y <= c["bbox"][3] + 40]
        left = sorted([c for c in row if c["bbox"][2] < x0], key=lambda c: -c["bbox"][2])
        right = sorted([c for c in row if c["bbox"][0] > x1], key=lambda c: c["bbox"][0])
        return left[:ncomp], right[:ncomp]
    x = a[0]
    y0, y1 = min(a[1], b[1]), max(a[1], b[1])
    above = sorted([c for c in comps if c["bbox"][3] < y0], key=lambda c: -c["bbox"][3])
    below = sorted([c for c in comps if c["bbox"][1] > y1], key=lambda c: c["bbox"][1])
    return above[:ncomp], below[:ncomp]


def n_components(xy, edges):
    parent = list(range(len(xy) + 1))

    def f(x):
        while parent[x] != x:
            x = parent[x]
        return x
    for u, v in edges:
        parent[f(u)] = f(v)
    return len({f(i) for i in range(1, len(xy) + 1)})


def match(page, comps, xy, edges, on_expected, label):
    lamp_ids = [i for c in comps for i in c["lamps"]]
    L = page["lamps"]
    pts = [(L[i][0], L[i][1]) for i in lamp_ids]
    exp = [(x, -y) for x, y in xy]  # screen coordinates, y down
    issues = []
    if len(pts) != len(exp):
        return [f"{label}: lamp count {len(pts)} vs data {len(exp)}"], None
    pxs, pys = zip(*pts)
    exs, eys = zip(*exp)
    sx = (max(pxs) - min(pxs)) / (max(exs) - min(exs)) if max(exs) > min(exs) else None
    sy = (max(pys) - min(pys)) / (max(eys) - min(eys)) if max(eys) > min(eys) else None
    s = sx if sx else sy
    if sx and sy and abs(sx - sy) / max(sx, sy) > 0.01:
        issues.append(f"{label}: unequal scale x={sx:.2f} y={sy:.2f}")
    pcx, pcy = (max(pxs) + min(pxs)) / 2, (max(pys) + min(pys)) / 2
    ecx, ecy = (max(exs) + min(exs)) / 2, (max(eys) + min(eys)) / 2
    norm = [((x - pcx) / s, (y - pcy) / s) for x, y in pts]
    expn = [(x - ecx, y - ecy) for x, y in exp]
    mapping = {}
    for k, q in enumerate(norm):
        j = min(range(len(expn)), key=lambda j: math.dist(q, expn[j]))
        if math.dist(q, expn[j]) > 0.02:
            issues.append(f"{label}: lamp at {pts[k]} off data position by {math.dist(q, expn[j]):.3f}")
        mapping[lamp_ids[k]] = j + 1
    if len(set(mapping.values())) != len(xy):
        issues.append(f"{label}: lamp mapping not bijective")
    printed_edges = {frozenset((mapping[i], mapping[j])) for i, j in page["edges"] if i in mapping and j in mapping}
    data_edges = {frozenset(e) for e in edges}
    if printed_edges != data_edges:
        issues.append(f"{label}: edges differ printed-only={printed_edges - data_edges} data-only={data_edges - printed_edges}")
    on = sorted(mapping[i] for i in page["on"] if i in mapping)
    if on != sorted(on_expected):
        issues.append(f"{label}: ON printed {on} vs data {sorted(on_expected)}")
    return issues, (on, s, (max(pxs) - min(pxs), max(pys) - min(pys)))


def run(fileid, expected):
    all_issues = []
    for pg in EX[fileid]:
        pno = pg["page"]
        exp = expected.get(pno, [])
        arr = arrows_of(pg)
        # reading order: by row (rounded y) then x
        arr.sort(key=lambda a: (round(a[1][1] / 20), a[1][0]))
        if len(arr) != len(exp):
            all_issues.append(f"{fileid} p{pno}: {len(arr)} arrows vs {len(exp)} expected pairs")
        for arrow, (label, gf, name, st, tg) in zip(arr, exp):
            xy, edges = gf(name)
            k = n_components(xy, edges)
            left, right = pick(pg, arrow, k)
            iss1, r1 = match(pg, left, xy, edges, st, f"{fileid} p{pno} {label} start")
            iss2, r2 = match(pg, right, xy, edges, tg, f"{fileid} p{pno} {label} target")
            all_issues += iss1 + iss2
            size = ""
            if r1 and r2:
                if abs(r1[1] - r2[1]) > 0.01:
                    all_issues.append(f"{label}: start/target scale differ {r1[1]:.2f} {r2[1]:.2f}")
                size = f"scale {r1[1]:.1f}pt/unit extent {r1[2][0]:.0f}x{r1[2][1]:.0f}pt"
            print(f"{fileid} p{pno} {label:8s} {name:15s} start={r1[0] if r1 else '?'} target={r2[0] if r2 else '?'} {size}")
    return all_issues


if __name__ == "__main__":
    issues = run("cat", cat_expected) + run("up", up_expected)
    # Problem 5 of upper: rings only
    pg = EX["up"][4]
    for c in pg["components"]:
        L = pg["lamps"]
        pts = [(L[i][0], L[i][1]) for i in c["lamps"]]
        n = len(pts)
        cx = sum(p[0] for p in pts) / n
        cy = sum(p[1] for p in pts) / n
        rad = [math.dist(p, (cx, cy)) for p in pts]
        ang = sorted(math.degrees(math.atan2(p[0] - cx, -(p[1] - cy))) % 360 for p in pts)
        gaps = [(ang[(i + 1) % n] - ang[i]) % 360 for i in range(n)]
        deg = {i: 0 for i in c["lamps"]}
        for i, j in pg["edges"]:
            if i in deg:
                deg[i] += 1
                deg[j] += 1
        print(f"up p5 ring n={n} radius spread {max(rad)-min(rad):.3f} gap spread {max(gaps)-min(gaps):.3f} degrees all 2: {set(deg.values())=={2}} on={[i for i in pg['on'] if i in deg]}")
    print("\nISSUES:" if issues else "\nNo diagram/data mismatches.")
    for i in issues:
        print(" ", i)
