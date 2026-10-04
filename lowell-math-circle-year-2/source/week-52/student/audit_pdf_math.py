#!/usr/bin/env python3
"""Re-run the independently authored Week 52 audit on a selected PDF.

Copied from the independent math-review stage; only its input/output routing
was adapted during revision. No author verification outputs are inputs.
Run from any directory with PyMuPDF installed.
"""
import argparse
from collections import Counter
from itertools import combinations
from math import cos, sin, hypot, sqrt
from pathlib import Path
import json
import pymupdf

parser = argparse.ArgumentParser()
parser.add_argument("pdf", type=Path)
parser.add_argument("report", type=Path)
args = parser.parse_args()
PDF = args.pdf.resolve()


def components(m, n, edges):
    adjacency = {f"R{i}": set() for i in range(1, m + 1)}
    adjacency.update({f"C{j}": set() for j in range(1, n + 1)})
    for i, j in edges:
        adjacency[f"R{i}"].add(f"C{j}")
        adjacency[f"C{j}"].add(f"R{i}")
    todo = set(adjacency)
    result = []
    while todo:
        seed = min(todo)
        stack, found = [seed], {seed}
        while stack:
            for v in adjacency[stack.pop()]:
                if v not in found:
                    found.add(v)
                    stack.append(v)
        todo -= found
        result.append(sorted(found))
    return result


def connected(m, n, edges):
    return len(components(m, n, edges)) == 1


def covers(m, n, edges):
    return {i for i, j in edges} == set(range(1, m + 1)) and {
        j for i, j in edges
    } == set(range(1, n + 1))


def universe(m, n):
    return [(i, j) for i in range(1, m + 1) for j in range(1, n + 1)]


def enumeration(m, n, count=None):
    cells = universe(m, n)
    counts = range(len(cells) + 1) if count is None else [count]
    table, examples = {}, {}
    for b in counts:
        totals = Counter()
        for E in combinations(cells, b):
            k = len(components(m, n, E))
            totals["all"] += 1
            totals[f"components_{k}"] += 1
            if k == 1:
                totals["connected"] += 1
                examples.setdefault("connected", E)
            if covers(m, n, E):
                totals["covered"] += 1
                if k != 1:
                    totals["covered_disconnected"] += 1
                    examples.setdefault("covered_disconnected", E)
        table[str(b)] = dict(totals)
    return {"counts": table, "examples": examples}


def finite_witness(m, n, edges, t=0.18, side=60.0):
    """Exact-form motion from the square grid, sampled only for length checks.

    Horizontal column vectors and upward vertical row vectors in one graph
    component receive the same rotation t. Other components stay unchanged.
    Vertices are sums of the strip vectors; all square-cell diagonals in E
    retain sqrt(2)*side. A cell joining different components changes shape.
    """
    groups = components(m, n, edges)
    assert len(groups) > 1
    rotated = set(groups[0])
    def direction(x, y, name):
        a = t if name in rotated else 0
        return (side * (cos(a) * x - sin(a) * y),
                side * (sin(a) * x + cos(a) * y))
    U = {j: direction(1, 0, f"C{j}") for j in range(1, n + 1)}
    V = {i: direction(0, 1, f"R{i}") for i in range(1, m + 1)}
    vertices = {}
    for y in range(m + 1):
        for x in range(n + 1):
            # bottom strip is Rm; top strip is R1
            vectors = [U[j] for j in range(1, x + 1)] + [
                V[i] for i in range(m - y + 1, m + 1)
            ]
            vertices[x, y] = tuple(sum(v[k] for v in vectors) for k in (0, 1))
    def length(a, b):
        return hypot(vertices[a][0] - vertices[b][0], vertices[a][1] - vertices[b][1])
    errors = []
    for y in range(m + 1):
        for x in range(n):
            errors.append(abs(length((x, y), (x + 1, y)) - side))
    for x in range(n + 1):
        for y in range(m):
            errors.append(abs(length((x, y), (x, y + 1)) - side))
    brace_errors = [abs(length((j - 1, m - i), (j, m - i + 1)) - side * sqrt(2))
                    for i, j in edges]
    changed = [(i, j, length((j - 1, m - i), (j, m - i + 1)))
               for i, j in universe(m, n)
               if abs(length((j - 1, m - i), (j, m - i + 1)) - side * sqrt(2)) > 0.01]
    assert changed
    assert max(errors + brace_errors, default=0) < 1e-10
    return {"rotated_component": sorted(rotated), "t_radians": t,
            "max_side_length_error_mm": max(errors, default=0),
            "max_brace_length_error_mm": max(brace_errors, default=0),
            "changed_unbraced_cell_diagonals_mm": changed,
            "vertices_mm": {f"{x},{y}": p for (x, y), p in vertices.items()}}


def close(a, b, tol=0.015):
    return abs(a - b) < tol


def black_grid_line(d):
    return d["color"] == (0, 0, 0) and close(d["width"], 0.89664, 0.001) and all(
        item[0] == "l" for item in d["items"]
    )


def blue(d):
    c = d["color"]
    return c and c[0] < 0.1 and c[2] > 0.4


def inside(p, bbox):
    x0, y0, x1, y1 = bbox
    return x0 - .02 <= p.x <= x1 + .02 and y0 - .02 <= p.y <= y1 + .02


def read_pdf_geometry():
    doc = pymupdf.open(PDF)
    assert len(doc) == 12
    result = []
    for page_number, page in enumerate(doc, 1):
        drawings = page.get_drawings()
        grids = []
        cursor = 0
        while cursor < len(drawings):
            if not black_grid_line(drawings[cursor]):
                cursor += 1
                continue
            items = []
            while cursor < len(drawings) and black_grid_line(drawings[cursor]):
                items += drawings[cursor]["items"]
                cursor += 1
            points = [point for item in items for point in item[1:]]
            x0, y0 = min(p.x for p in points), min(p.y for p in points)
            x1, y1 = max(p.x for p in points), max(p.y for p in points)
            xs = sorted({round(item[1].x, 3) for item in items if close(item[1].x, item[2].x)})
            ys = sorted({round(item[1].y, 3) for item in items if close(item[1].y, item[2].y)})
            m, n = len(ys) - 1, len(xs) - 1
            assert m > 0 and n > 0
            side_x, side_y = (x1 - x0) / n, (y1 - y0) / m
            assert close(side_x, side_y)
            for a, b in zip(xs, xs[1:]):
                assert close(b - a, side_x)
            for a, b in zip(ys, ys[1:]):
                assert close(b - a, side_y)
            bbox = [x0, y0, x1, y1]
            braces = []
            for d in drawings:
                if blue(d) and close(d["width"], 1.99255, .001):
                    for kind, a, b in d["items"]:
                        assert kind == "l"
                        if inside(a, bbox) and inside(b, bbox):
                            assert close(abs(a.x-b.x), side_x)
                            assert close(abs(a.y-b.y), side_y)
                            i = round((min(a.y, b.y) - y0) / side_y) + 1
                            j = round((min(a.x, b.x) - x0) / side_x) + 1
                            braces.append([i, j])
            assert len(braces) == len(set(map(tuple, braces)))
            grids.append({"rows": m, "columns": n, "cell_mm": side_x * 25.4 / 72,
                          "bbox_pdf_pt": bbox, "braces": sorted(braces)})
        # Link dots have a different circle radius and pen width from frame pins.
        link_groups = []
        cursor = 0
        while cursor < len(drawings):
            d = drawings[cursor]
            is_link_dot = d["type"] == "fs" and close(d["width"], .79701, .001) and close(d["rect"].width, 5.3799, .01)
            if not is_link_dot or page_number < 6:
                cursor += 1
                continue
            dots = []
            while cursor < len(drawings):
                d = drawings[cursor]
                if not (d["type"] == "fs" and close(d["width"], .79701, .001) and close(d["rect"].width, 5.3799, .01)):
                    break
                dots.append(((d["rect"].x0 + d["rect"].x1) / 2, (d["rect"].y0 + d["rect"].y1) / 2))
                cursor += 1
            left, right = min(x for x, y in dots), max(x for x, y in dots)
            rowdots = sorted((x, y) for x, y in dots if close(x, left))
            coldots = sorted((x, y) for x, y in dots if close(x, right))
            assert len(rowdots) + len(coldots) == len(dots)
            labels = {"R"+str(i+1): point for i, point in enumerate(rowdots)}
            labels.update({"C"+str(j+1): point for j, point in enumerate(coldots)})
            links = []
            for d in drawings:
                if not (blue(d) and close(d["width"], 1.49442, .001)):
                    continue
                for kind, a, b in d["items"]:
                    assert kind == "l"
                    matched = []
                    for point in (a, b):
                        names = [name for name, xy in labels.items() if hypot(point.x-xy[0], point.y-xy[1]) < .02]
                        matched.append(names)
                    if all(matched):
                        names = sorted([matched[0][0], matched[1][0]])
                        assert names[0][0] == "C" and names[1][0] == "R"
                        links.append([int(names[1][1:]), int(names[0][1:])])
            # Verify each circle's nearest appropriate text is its own label.
            words = page.get_text("words")
            for name, (x, y) in labels.items():
                matching = [w for w in words if w[4] == name and abs((w[1]+w[3])/2-y) < 5
                            and abs((w[2] if name[0] == "R" else w[0])-x) < 11]
                assert len(matching) == 1, (page_number, name, matching)
            link_groups.append({"rows": len(rowdots), "columns": len(coldots),
                                "dots_pdf_pt": labels, "links": sorted(links)})
        result.append({"page": page_number, "grids": grids, "link_graphs": link_groups})
    # Polygon side counts and regularity, measured from actual PDF vectors.
    polygons = []
    for d in doc[0].get_drawings():
        if d["type"] == "s" and d["color"] == (0, 0, 0) and close(d["width"], 1.99255, .001):
            lengths = [hypot(a.x-b.x, a.y-b.y) for k, a, b in d["items"] if k == "l"]
            assert len(lengths) in (3, 4)
            assert max(lengths) - min(lengths) < .001
            polygons.append({"side_count": len(lengths), "side_lengths_mm": [a*25.4/72 for a in lengths]})
    assert [p["side_count"] for p in polygons] == [3, 4]
    return {"pages": result, "page_1_polygons": polygons}


def main():
    geometry = read_pdf_geometry()
    by_page = {d["page"]: d for d in geometry["pages"]}
    # Expected diagrams are transcribed independently from the printed pages.
    expected = {
        2: [(1,1,[]), (1,1,[])],
        3: [(2,2,[(1,1)]), (2,2,[(1,1),(2,2)]),
            (2,2,[(1,1),(1,2),(2,1)]), (2,2,universe(2,2))],
        4: [(2,2,[])]*4,
        5: [(2,3,[])]*4,
        6: [(1,3,[(1,2)])]*2 + [(2,3,[(1,1),(1,2),(2,1),(2,2)]),
            (2,3,[(1,1),(1,2),(1,3),(2,1)])],
        7: [(3,3,[(1,1),(1,2),(2,1),(2,2),(3,3)]),
            (3,3,[(1,1),(1,2),(1,3),(2,1),(3,1)])],
        8: [(2,3,[(1,1),(1,2),(1,3),(2,1),(2,2)])] + [(2,3,universe(2,3))]*4,
        9: [(3,3,[(1,1),(1,2),(2,1),(2,2)]),
            (3,3,[(1,1),(1,2),(2,2),(3,3)])],
        10: [(4,5,[])], 11: [(3,3,[])]*2, 12: [(4,4,[])]
    }
    for p, layouts in expected.items():
        actual = by_page[p]["grids"]
        assert len(actual) == len(layouts), (p, len(actual), len(layouts))
        for a, (m,n,E) in zip(actual, layouts):
            assert (a["rows"], a["columns"], a["braces"]) == (m,n,sorted(map(list,E))), (p,a,E)
    assert by_page[6]["link_graphs"][0]["links"] == [[1,2]]
    assert len(by_page[6]["link_graphs"]) == 3
    for p in [6,7,9]:
        assert all(not g["links"] for g in by_page[p]["link_graphs"][-2:])
        for frame, graph in zip(by_page[p]["grids"][-2:], by_page[p]["link_graphs"][-2:]):
            assert (frame["rows"],frame["columns"]) == (graph["rows"],graph["columns"])
        a,b = by_page[p]["link_graphs"][-2:]
        def relative(g):
            x0,y0=g["dots_pdf_pt"]["R1"]
            return {k:[round(x-x0,2),round(y-y0,2)] for k,(x,y) in g["dots_pdf_pt"].items()}
        assert relative(a) == relative(b), (p,a,b)
    assert by_page[8]["link_graphs"][0]["links"] == by_page[8]["grids"][0]["braces"]
    datasets = {}
    for name,p,index in [("P4A",3,0),("P4B",3,1),("P4C",3,2),("P4D",3,3),
                          ("P7A",6,2),("P7B",6,3),("P8A",7,0),("P8B",7,1),
                          ("P9",8,0),("P11A",9,0),("P11B",9,1)]:
        g=by_page[p]["grids"][index]
        m,n,E=g["rows"],g["columns"],list(map(tuple,g["braces"]))
        info={"rows":m,"columns":n,"braces":E,"components":components(m,n,E)}
        if not connected(m,n,E):
            info["finite_motion_witness"]=finite_witness(m,n,E)
        if name=="P9":
            info["removable_individually"]=[e for e in E if connected(m,n,[f for f in E if f!=e])]
        if name.startswith("P11"):
            info["single_additions_that_rigidify"]=[e for e in universe(m,n) if e not in E and connected(m,n,E+[e])]
        datasets[name]=info
    all23=universe(2,3)
    datasets["P10"]={"rigid_removed_pairs":[],"flexible_removed_pairs":[]}
    for removed in combinations(all23,2):
        E=[e for e in all23 if e not in removed]
        key="rigid_removed_pairs" if connected(2,3,E) else "flexible_removed_pairs"
        datasets["P10"][key].append(removed)
    assert len(datasets["P10"]["rigid_removed_pairs"])==12
    assert len(datasets["P10"]["flexible_removed_pairs"])==3
    datasets["P12"]={"minimum":8,"example":[(1,j) for j in range(1,6)]+[(i,1) for i in range(2,5)]}
    assert connected(4,5,datasets["P12"]["example"])
    E14=[e for e in universe(3,3) if e!=(3,3)]+[(4,4)]
    assert len(E14)==9 and covers(4,4,E14) and not connected(4,4,E14)
    datasets["P14"]={"counterexample":E14,"components":components(4,4,E14),
                     "finite_motion_witness":finite_witness(4,4,E14)}
    enum={"2x2":enumeration(2,2),"2x3":enumeration(2,3),"3x3":enumeration(3,3),
          "4x4_nine":enumeration(4,4,9)}
    assert enum["2x2"]["counts"]["3"]["connected"]==4
    assert enum["2x3"]["counts"]["4"]["connected"]==12
    assert enum["3x3"]["counts"]["6"]["covered"]==78
    assert enum["3x3"]["counts"]["6"].get("covered_disconnected",0)==0
    assert enum["4x4_nine"]["counts"]["9"]["covered_disconnected"]==144
    report={"input_pdf":str(PDF),"geometry":geometry,"problems":datasets,"enumerations":enum}
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps({"grid_diagrams":sum(len(p["grids"]) for p in geometry["pages"]),
                      "link_diagrams":sum(len(p["link_graphs"]) for p in geometry["pages"]),
                      "enumerations":enum,"problems":{k:{a:b for a,b in v.items() if a!="finite_motion_witness"} for k,v in datasets.items()}},indent=2))


if __name__ == "__main__":
    main()
