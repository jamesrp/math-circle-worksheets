#!/usr/bin/env python3
"""Week 34 math check: read every ring back out of the delivered PDFs.

Reads only the final PDFs in lowell-math-circle-year-2/week-34/ (not the
sources): the grey/black ring outlines, the spot circles on them, the marks in
each spot (filled dot, hollow ring, outline square, letter), the motion-card
arrows and the dashed flip line.  For every ring it reports the number of spots,
whether the spots are equally spaced on a circle starting at the top (a regular
polygon with equal x/y scale), spot diameters, centre spacing and gaps, and the
clockwise contents from the top spot.

Output: extracted.json next to this script and a readable summary on stdout.
Run: python3 extract.py > out_extract.txt   (needs PyMuPDF: pip install pymupdf)
"""
import json
import math
from pathlib import Path

import pymupdf

from common import HERE, WEEK, PT_PER_MM

FILES = ["week-34-k-1.pdf", "week-34-grades-2-3.pdf", "week-34-grades-4-5.pdf",
         "week-34-bonus.pdf", "week-34-facilitator.pdf", "week-34-bonus-facilitator.pdf"]


def mm(v):
    return round(v / PT_PER_MM, 2)


def is_black(c):
    return c is not None and max(c) < 0.05


def is_white(c):
    return c is not None and min(c) > 0.95


def is_grey(c):
    return c is not None and 0.3 < min(c) and max(c) < 0.9


def cw_angle(cx, cy, x, y):
    """Clockwise angle in degrees from 'up' (PDF y grows downward)."""
    a = math.degrees(math.atan2(x - cx, -(y - cy))) % 360
    return 0.0 if a > 359.9 else a


def page_objects(page):
    circles, squares, arcs, lines, heads = [], [], [], [], []
    for d in page.get_drawings():
        kinds = [it[0] for it in d["items"]]
        r = d["rect"]
        dashed = bool(d.get("dashes")) and d.get("dashes") not in ("[] 0", "")
        if kinds == ["c"] * 4:
            circles.append(dict(cx=(r.x0 + r.x1) / 2, cy=(r.y0 + r.y1) / 2, w=r.width, h=r.height,
                                type=d["type"], fill=d.get("fill"), color=d.get("color")))
        elif kinds == ["l"] * 4 and d["type"] == "fs" and r.width < 8 and r.height < 8:
            heads.append([(it[1].x, it[1].y) for it in d["items"]])
        elif kinds == ["l"] * 4 and d["type"] == "s" and r.width < 8 and r.height < 8:
            squares.append(dict(cx=(r.x0 + r.x1) / 2, cy=(r.y0 + r.y1) / 2, w=r.width, h=r.height))
        elif kinds and all(k == "c" for k in kinds) and d["type"] == "s":
            p0 = d["items"][0][1]
            p1 = d["items"][-1][-1]
            arcs.append(dict(start=(p0.x, p0.y), end=(p1.x, p1.y), mid=None))
        elif kinds == ["l"] and d["type"] == "s":
            p, q = d["items"][0][1], d["items"][0][2]
            lines.append(dict(p=(p.x, p.y), q=(q.x, q.y), dashed=dashed))
    words = page.get_text("words")
    return circles, squares, arcs, lines, heads, words


def build_rings(circles, squares, arcs, lines, heads, words):
    outlines = [c for c in circles if c["type"] == "s" and (is_grey(c["color"]) or is_black(c["color"]))
                and c["w"] > 30]
    spots = [c for c in circles if c["type"] == "fs" and is_white(c["fill"]) and is_black(c["color"])]
    dots = [c for c in circles if c["type"] == "f" and is_black(c["fill"])]
    hollow = [c for c in circles if c["type"] == "s" and is_black(c["color"]) and c["w"] < 15]
    rings = []
    used = set()
    for o in sorted(outlines, key=lambda c: (round(c["cy"]), c["cx"])):
        R = (o["w"] + o["h"]) / 4
        mine = [i for i, s in enumerate(spots)
                if i not in used and abs(math.hypot(s["cx"] - o["cx"], s["cy"] - o["cy"]) - R) < 1.0]
        if not mine:
            continue
        used.update(mine)
        n = len(mine)
        pts = sorted((cw_angle(o["cx"], o["cy"], spots[i]["cx"], spots[i]["cy"]), i) for i in mine)
        ang_err = max(abs(((a - 360 * k / n + 180) % 360) - 180) for k, (a, _) in enumerate(pts))
        rad_err = max(abs(math.hypot(spots[i]["cx"] - o["cx"], spots[i]["cy"] - o["cy"]) - R) for _, i in pts)
        diam = [(spots[i]["w"], spots[i]["h"]) for _, i in pts]
        centres = [(spots[i]["cx"], spots[i]["cy"]) for _, i in pts]
        adj = [math.dist(centres[k], centres[(k + 1) % n]) for k in range(n)]
        dmax = max(max(w, h) for w, h in diam)
        contents = []
        for _, i in pts:
            s = spots[i]
            rad = s["w"] / 2

            def inside(x, y, s=s, rad=rad):
                return math.hypot(x - s["cx"], y - s["cy"]) < rad - 0.3
            marks = []
            if any(inside(c["cx"], c["cy"]) and c["w"] < s["w"] for c in dots):
                marks.append("dot")
            if any(inside(c["cx"], c["cy"]) and c["w"] < s["w"] - 2 for c in hollow):
                marks.append("ring")
            if any(inside(q["cx"], q["cy"]) for q in squares):
                marks.append("square")
            for w in words:
                if inside((w[0] + w[2]) / 2, (w[1] + w[3]) / 2):
                    marks.append(w[4])
            contents.append("+".join(marks) if marks else "-")
        # label: words just below the ring
        bottom = o["cy"] + R + dmax / 2
        lab = [w for w in words if bottom - 2 < w[1] < bottom + 30
               and o["cx"] - R - dmax < (w[0] + w[2]) / 2 < o["cx"] + R + dmax]
        if lab:
            top = min(w[1] for w in lab)
            lab = [w for w in lab if w[1] < top + 3]
        lab.sort(key=lambda w: (round(w[1]), w[0]))
        label = " ".join(w[4] for w in lab)
        # arcs and dashed lines attached to this ring
        ring_arcs = []
        for a in arcs:
            d0 = math.dist(a["start"], (o["cx"], o["cy"]))
            if R < d0 < R + 25:
                a0 = cw_angle(o["cx"], o["cy"], *a["start"])
                a1 = cw_angle(o["cx"], o["cy"], *a["end"])
                # arrow tip: the arrowhead vertex reached furthest clockwise from the arc start
                tip = None
                for hd in heads:
                    if min(math.dist(v, a["end"]) for v in hd) < 3:
                        tip = max((cw_angle(o["cx"], o["cy"], *v) - a0) % 360 for v in hd)
                ring_arcs.append(dict(start_deg=round(a0, 1), end_deg=round(a1, 1),
                                      sweep_cw_deg=round((a1 - a0) % 360, 1),
                                      tip_sweep_cw_deg=None if tip is None else round(tip, 1),
                                      tip_sweep_in_spots=None if tip is None else round(tip / (360 / n), 2)))
        ring_lines = []
        for ln in lines:
            if not ln["dashed"]:
                continue
            (x0, y0), (x1, y1) = ln["p"], ln["q"]
            # distance of ring centre from the infinite line
            num = abs((x1 - x0) * (y0 - o["cy"]) - (x0 - o["cx"]) * (y1 - y0))
            den = math.hypot(x1 - x0, y1 - y0)
            if den and num / den < 2 and min(math.dist(ln["p"], (o["cx"], o["cy"])),
                                             math.dist(ln["q"], (o["cx"], o["cy"]))) < R + 25:
                on = []
                for k, (_, i) in enumerate(pts):
                    s = spots[i]
                    dd = abs((x1 - x0) * (y0 - s["cy"]) - (x0 - s["cx"]) * (y1 - y0)) / den
                    if dd < 0.5:
                        on.append(k)
                ring_lines.append(dict(through_centre_pt=round(num / den, 3),
                                       spots_on_line=on,
                                       angle_deg=round(cw_angle(0, 0, x1 - x0, y1 - y0) % 180, 2)))
        gaps = [d - dmax for d in adj]
        rings.append(dict(
            n=n, centre_mm=[mm(o["cx"]), mm(o["cy"])], ring_radius_mm=mm(R),
            outline="grey" if is_grey(o["color"]) else "black",
            spot_diam_mm=[mm(min(min(w, h) for w, h in diam)), mm(max(max(w, h) for w, h in diam))],
            spot_round=max(abs(w - h) for w, h in diam) < 0.05,
            max_angle_error_deg=round(ang_err, 3), max_radius_error_mm=round(rad_err / PT_PER_MM, 3),
            first_spot_angle_deg=round(pts[0][0], 3),
            adjacent_centre_mm=[mm(min(adj)), mm(max(adj))], min_gap_mm=mm(min(gaps)),
            contents_cw_from_top=contents, label=label, arcs=ring_arcs, dashed_lines=ring_lines,
            spot_centres_mm=[[round(x / PT_PER_MM, 4), round(y / PT_PER_MM, 4)] for x, y in centres]))
    leftover = [spots[i] for i in range(len(spots)) if i not in used]
    return rings, leftover


def main():
    out = {}
    for fn in FILES:
        doc = pymupdf.open(WEEK / fn)
        out[fn] = []
        print(f"== {fn} ({doc.page_count} pages)")
        for pno, page in enumerate(doc, start=1):
            circles, squares, arcs, lines, heads, words = page_objects(page)
            rings, leftover = build_rings(circles, squares, arcs, lines, heads, words)
            out[fn].append(dict(page=pno, rings=rings, unassigned_spots=len(leftover)))
            if not rings and not leftover:
                continue
            print(f"  p{pno}: {len(rings)} rings, {len(leftover)} unassigned spot circles")
            for r in rings:
                print(f"    n={r['n']} R={r['ring_radius_mm']}mm spot={r['spot_diam_mm']}mm "
                      f"round={r['spot_round']} angErr={r['max_angle_error_deg']}deg "
                      f"radErr={r['max_radius_error_mm']}mm top={r['first_spot_angle_deg']}deg "
                      f"adj={r['adjacent_centre_mm']}mm gap={r['min_gap_mm']}mm "
                      f"[{' '.join(r['contents_cw_from_top'])}] label='{r['label']}'")
                for a in r["arcs"]:
                    print(f"      arc: {a}")
                for ln in r["dashed_lines"]:
                    print(f"      dashed line: {ln}")
    (HERE / "extracted.json").write_text(json.dumps(out, indent=1))
    print("wrote extracted.json")


if __name__ == "__main__":
    main()
