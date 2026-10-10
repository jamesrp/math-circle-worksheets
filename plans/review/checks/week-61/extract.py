#!/usr/bin/env python3
"""Week 61 math check, step 1: read the delivered student PDF itself.

Independent of the packet's own generator (geometry.py) and checker
(verify_math.py).  Uses poppler's pdftocairo (vector paths -> SVG) and
pdftotext -bbox (word boxes) on lowell-math-circle-year-2/week-61/week-61-students.pdf
and writes extracted.json next to this script: every drawn path in PDF points
(origin top-left, y down), sampled along Bezier segments, with its stroke/fill
style and dash flag, plus every word with its bounding box.

Run: python3 extract.py      (standard library + poppler-utils only)
"""
import html
import json
import re
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

HERE = Path(__file__).resolve().parent


def find_repo():
    # Committed location: <repo>/plans/review/checks/week-61/<this file>
    cand = HERE.parents[3] if len(HERE.parents) > 3 else None
    if cand and (cand / "lowell-math-circle-year-2").is_dir():
        return cand
    for p in [HERE] + list(HERE.parents):  # fallback: run folder under tmp/
        if (p / "lowell-math-circle-year-2").is_dir():
            return p
    sys.exit("repository not found above " + str(HERE))


REPO = find_repo()
PDF = REPO / "lowell-math-circle-year-2" / "week-61" / "week-61-students.pdf"
SVGNS = "{http://www.w3.org/2000/svg}"


def matmul(m, n):
    a, b, c, d, e, f = m
    a2, b2, c2, d2, e2, f2 = n
    return (a * a2 + c * b2, b * a2 + d * b2, a * c2 + c * d2, b * c2 + d * d2,
            a * e2 + c * f2 + e, b * e2 + d * f2 + f)


def parse_transform(s):
    if not s:
        return (1, 0, 0, 1, 0, 0)
    m = re.match(r"matrix\(([^)]*)\)", s.strip())
    if not m:
        raise ValueError("unhandled transform " + s)
    return tuple(float(x) for x in m.group(1).replace(",", " ").split())


def apply(m, p):
    a, b, c, d, e, f = m
    return (a * p[0] + c * p[1] + e, b * p[0] + d * p[1] + f)


def parse_d(d, m, nsample=12):
    toks = re.findall(r"[MLCZ]|-?\d*\.?\d+(?:e-?\d+)?", d)
    subpaths, cur, i, pos = [], [], 0, None
    raw_nodes = []  # segment end points only (no Bezier samples), for circle fits
    while i < len(toks):
        t = toks[i]
        if t == "M":
            if cur:
                subpaths.append(cur)
            pos = (float(toks[i + 1]), float(toks[i + 2]))
            cur = [apply(m, pos)]
            raw_nodes.append(apply(m, pos))
            i += 3
        elif t == "L":
            pos = (float(toks[i + 1]), float(toks[i + 2]))
            cur.append(apply(m, pos))
            raw_nodes.append(apply(m, pos))
            i += 3
        elif t == "C":
            p1 = (float(toks[i + 1]), float(toks[i + 2]))
            p2 = (float(toks[i + 3]), float(toks[i + 4]))
            p3 = (float(toks[i + 5]), float(toks[i + 6]))
            p0 = pos
            for k in range(1, nsample + 1):
                s = k / nsample
                q = tuple((1 - s) ** 3 * p0[j] + 3 * (1 - s) ** 2 * s * p1[j]
                          + 3 * (1 - s) * s * s * p2[j] + s ** 3 * p3[j] for j in range(2))
                cur.append(apply(m, q))
            raw_nodes.append(apply(m, p3))
            pos = p3
            i += 7
        elif t == "Z":
            cur.append("Z")
            i += 1
        else:
            raise ValueError("unexpected token " + t)
    if cur:
        subpaths.append(cur)
    return subpaths, ("C" in toks)


def rgb(s):
    if not s or s == "none":
        return None
    m = re.match(r"rgb\(([^)]*)\)", s)
    return [round(float(x.strip().rstrip("%")) * 2.55) for x in m.group(1).split(",")]


def svg_paths(svgfile):
    tree = ET.parse(svgfile)
    out = []

    def walk(el, m, inherited):
        tag = el.tag.replace(SVGNS, "")
        if tag == "defs":
            return
        m2 = matmul(m, parse_transform(el.get("transform")))
        style = dict(inherited)
        for k in ("fill", "stroke", "stroke-width", "stroke-dasharray", "fill-opacity", "stroke-opacity"):
            if el.get(k) is not None:
                style[k] = el.get(k)
        if tag == "path":
            subs, curved = parse_d(el.get("d"), m2)
            a, b, c, d, e, f = m2
            scale = abs(a * d - b * c) ** 0.5
            out.append({
                "fill": rgb(style.get("fill")) if el.get("fill") is not None else None,
                "stroke": rgb(style.get("stroke")) if el.get("stroke") is not None else None,
                "stroke_width": float(style.get("stroke-width", 0)) * scale if el.get("stroke") else 0,
                "dashed": "stroke-dasharray" in style and el.get("stroke") is not None,
                "stroke_opacity": float(style.get("stroke-opacity", 1)),
                "fill_opacity": float(style.get("fill-opacity", 1)),
                "curved": curved,
                "subpaths": [[p if p == "Z" else [round(p[0], 5), round(p[1], 5)] for p in s] for s in subs],
            })
        for ch in el:
            walk(ch, m2, style)

    walk(tree.getroot(), (1, 0, 0, 1, 0, 0), {})
    return out


def words(bboxfile):
    pages, cur = [], None
    for line in Path(bboxfile).read_text(encoding="utf-8").splitlines():
        if "<page " in line:
            cur = []
            pages.append(cur)
        m = re.search(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*)</word>', line)
        if m and cur is not None:
            cur.append({"x0": float(m.group(1)), "y0": float(m.group(2)), "x1": float(m.group(3)),
                        "y1": float(m.group(4)), "text": html.unescape(m.group(5))})
    return pages


def main():
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        n = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", str(PDF)], capture_output=True,
                                                             text=True).stdout).group(1))
        pages = []
        subprocess.run(["pdftotext", "-bbox", str(PDF), str(tmp / "bbox.html")], check=True)
        wp = words(tmp / "bbox.html")
        for k in range(1, n + 1):
            svgf = tmp / f"p{k}.svg"
            subprocess.run(["pdftocairo", "-svg", "-f", str(k), "-l", str(k), str(PDF), str(svgf)], check=True)
            pages.append({"page": k, "paths": svg_paths(svgf), "words": wp[k - 1]})
    data = {"pdf": str(PDF.relative_to(REPO)), "pages": pages}
    (HERE / "extracted.json").write_text(json.dumps(data))
    for p in pages:
        print(f"page {p['page']}: {len(p['paths'])} paths, {len(p['words'])} words")


if __name__ == "__main__":
    main()
