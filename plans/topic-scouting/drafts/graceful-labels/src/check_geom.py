"""Geometry checks for every network drawn by gen.py (figs/registry.json).

For each network it reports, in centimetres:
  vis    shortest piece of link line visible between a dot and a box
  boxdot smallest gap between any box and any dot circle
  boxlnk smallest gap between a box and a link it does not belong to
  lnkdot smallest gap between a link and a dot that is not one of its ends
  card   largest square card (or tower foot) centred on a dot that covers
         no box and no other card ('card' and 'tower' boards only)
and flags anything below the thresholds.
"""
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
REG = json.load(open(os.path.join(HERE, "figs", "registry.json")))

MIN_VIS = 0.2
MIN_GAP = 0.12
MIN_BOXLINK = 0.25
CARD_TARGET = {"card": 2.4, "tower": 2.0}


def seg_point_dist(p, q, x):
    px, py = p; qx, qy = q
    dx, dy = qx - px, qy - py
    L2 = dx * dx + dy * dy
    t = max(0.0, min(1.0, ((x[0] - px) * dx + (x[1] - py) * dy) / L2))
    return math.hypot(px + t * dx - x[0], py + t * dy - x[1])


def rect_point_dist(c, h, x):
    return math.hypot(max(abs(x[0] - c[0]) - h, 0), max(abs(x[1] - c[1]) - h, 0))


def seg_rect_dist(p, q, c, h, n=600):
    return min(rect_point_dist(c, h, (p[0] + k / n * (q[0] - p[0]), p[1] + k / n * (q[1] - p[1])))
               for k in range(n + 1))


bad = 0
for net in REG:
    pts = [tuple(p) for p in net["pts"]]
    edges = [tuple(e) for e in net["edges"]]
    boxes = [tuple(b) for b in net["boxes"]]
    r, b = net["r"], net["box"]
    h = b / 2
    vis = boxdot = boxlnk = lnkdot = 1e9
    for i, (a, c) in enumerate(edges):
        p, q = pts[a], pts[c]
        L = math.dist(p, q)
        ux, uy = (q[0] - p[0]) / L, (q[1] - p[1]) / L
        tc = math.dist(p, boxes[i])
        half = h / max(abs(ux), abs(uy))
        vis = min(vis, tc - half - r, L - tc - half - r)
        for j, (a2, c2) in enumerate(edges):
            if j != i:
                boxlnk = min(boxlnk, seg_rect_dist(pts[a2], pts[c2], boxes[i], h))
        for k, x in enumerate(pts):
            if k not in (a, c):
                lnkdot = min(lnkdot, seg_point_dist(p, q, x) - r)
    for bc in boxes:
        for x in pts:
            boxdot = min(boxdot, rect_point_dist(bc, h, x) - r)
    card = None
    if net["kind"] in CARD_TARGET:
        card = 1e9
        for x in pts:
            for bc in boxes:
                card = min(card, 2 * max(abs(bc[0] - x[0]), abs(bc[1] - x[1])) - b)
            for y in pts:
                if y != x:
                    card = min(card, max(abs(y[0] - x[0]), abs(y[1] - x[1])))
    flags = []
    if vis < MIN_VIS: flags.append("vis")
    if boxdot < MIN_GAP: flags.append("boxdot")
    if boxlnk < MIN_BOXLINK: flags.append("boxlnk")
    if lnkdot < MIN_GAP: flags.append("lnkdot")
    if card is not None and card < CARD_TARGET[net["kind"]]: flags.append("card")
    bad += bool(flags)
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    size = f"{max(xs) - min(xs) + 2 * r:5.2f} x {max(ys) - min(ys) + 2 * r:5.2f}"
    cs = f" card {card:4.2f}" if card is not None else ""
    lk = f" boxlnk {boxlnk:4.2f}" if boxlnk < 1e8 else ""
    ld = f" lnkdot {lnkdot:4.2f}" if lnkdot < 1e8 else ""
    print(f"{net['name']:16s} {net['kind']:5s} dots {len(pts):2d} links {len(edges):2d} "
          f"dot {2 * r:.2f} box {b:.2f} size {size}  vis {vis:4.2f} boxdot {boxdot:4.2f}{lk}{ld}{cs}"
          f"  [{net['caption'] or ''}] {'  <-- ' + ','.join(flags) if flags else ''}")
print("networks flagged:", bad)
