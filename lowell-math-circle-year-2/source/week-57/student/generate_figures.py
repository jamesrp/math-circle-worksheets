#!/usr/bin/env python3
"""Generate original equal-scale TikZ diagrams from the checked polygon data."""
import argparse
import json
from pathlib import Path


def cross(a, b, p):
    return (b[0]-a[0])*(p[1]-a[1])-(b[1]-a[1])*(p[0]-a[0])


def category(poly, p):
    winding = 0
    for a,b in zip(poly, poly[1:]+poly[:1]):
        c = cross(a,b,p)
        if c == 0 and min(a[0],b[0]) <= p[0] <= max(a[0],b[0]) and min(a[1],b[1]) <= p[1] <= max(a[1],b[1]):
            return "boundary"
        if a[1] <= p[1] < b[1] and c > 0: winding += 1
        if b[1] <= p[1] < a[1] and c < 0: winding -= 1
    return "inside" if winding else "outside"


def path(vertices):
    return " -- ".join(f"({x},{y})" for x,y in vertices) + " -- cycle"


def figure(case):
    w,h = case["board"]
    mm = case["size_mm"]
    out = [fr"\begin{{tikzpicture}}[x={mm}mm,y={mm}mm]",
           fr"\path[use as bounding box] (-.12,-.12) rectangle ({w+.12},{h+.12});",
           fr"\path[fill=black!5] {path(case['vertices'])};"]
    for hole in case.get("holes", []):
        out.append(fr"\path[fill=white] {path(hole)};")
    # A unique color lets the PDF verifier locate the authored polygon outlines.
    out.append(fr"\draw[draw=polygonline,line width=.9pt,line join=round] {path(case['vertices'])};")
    for hole in case.get("holes", []):
        out.append(fr"\draw[draw=polygonline,line width=.9pt,line join=round] {path(hole)};")
    for a,b in case.get("seams", []):
        out.append(fr"\draw[dashed,line width=.7pt] ({a[0]},{a[1]}) -- ({b[0]},{b[1]});")
    # Dots are painted last, so dots between vertices remain visible on sides.
    for x in range(w+1):
        for y in range(h+1):
            out.append(fr"\fill[black] ({x},{y}) circle[radius=.55mm];")
            if case.get("mark_counts"):
                c = category(case["vertices"], (x,y))
                if c == "boundary":
                    out.append(fr"\draw[line width=.6pt] ({x},{y}) circle[radius=1.8mm];")
                elif c == "inside":
                    out.append(fr"\draw[line width=.6pt] ({x-.09},{y-.09}) rectangle ({x+.09},{y+.09});")
    out.append(r"\end{tikzpicture}")
    return "\n".join(out)


def generate(output):
    data = json.loads(Path(__file__).with_name("assets").joinpath("polygons.json").read_text())
    lines = [r"\newcommand{\Figure}[1]{\csname figure#1\endcsname}"]
    for name,case in data.items():
        if case.get("draw", True):
            lines.append(r"\expandafter\def\csname figure" + name + r"\endcsname{%" + "\n" + figure(case) + "\n}")
    Path(output).write_text("\n".join(lines)+"\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("output")
    generate(parser.parse_args().output)
