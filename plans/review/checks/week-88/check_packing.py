#!/usr/bin/env python3
"""Numerical exploration of unrestricted tray packings for Week 88.

Question for Problem 2: can twelve 40 mm disks fit the 160 x 112 mm practical
tray?  (Oler's inequality, in check_math.py, proves at most 12.)  Question for
Problem 8's scope: can eleven 40 mm disks fit 160 x 108 mm if the rows need not
be straight?  The guide makes no claim about either; this script only reports
the best arrangements a multi-start search finds.  Numerical evidence, not a
proof.

Method: disk centres lie in a 120 x (H-40) mm box and must be >= 40 mm apart.
In units of 40 mm, each of many random starts is pushed apart by gradient
descent on sum(max(0, t - d)^2), where the target t is always a little above
the start's current smallest distance, so the closest pairs keep separating.
The best starts are then polished with a smaller step and overshoot.  The
largest true minimum centre distance seen is reported: >= 40 mm means the
disks fit.  The sanity cases show how close the search gets to known values.

Needs numpy.  Run: python3 check_packing.py  (writes check_packing.py.out)
"""
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
OUT = []


def log(s=""):
    OUT.append(s)
    print(s, flush=True)


def push(p, w, h, iters, over, lr, rng):
    starts, n, _ = p.shape
    eye = np.eye(n, dtype=bool)[None]
    best = np.zeros(starts)
    best_p = p.copy()
    for k in range(iters):
        diff = p[:, :, None, :] - p[:, None, :, :]
        d = np.sqrt((diff ** 2).sum(-1) + 1e-18)
        m = np.where(eye, 1e9, d).reshape(starts, -1).min(1)
        imp = m > best
        best = np.where(imp, m, best)
        best_p[imp] = p[imp]
        t = np.maximum(m, best) * over
        o = np.where(eye, 0.0, np.clip(t[:, None, None] - d, 0, None))
        g = ((-2 * o / d)[..., None] * diff).sum(2)
        p = p - (lr * (1 - k / iters) + 1e-4) * g + rng.normal(0, 1e-7, p.shape)
        p[..., 0] = np.clip(p[..., 0], 0, w)
        p[..., 1] = np.clip(p[..., 1], 0, h)
    return best, best_p


def best_min_distance(n, w, h, starts=300, seed=1):
    rng = np.random.default_rng(seed)
    p = rng.random((starts, n, 2)) * np.array([w, h])
    best, bp = push(p, w, h, 3000, 1.03, 0.1, rng)
    top = np.argsort(best)[-30:]
    best2, bp2 = push(bp[top].copy(), w, h, 6000, 1.002, 0.02, rng)
    i = int(best2.argmax())
    return float(best2[i]), bp2[i]


def fmt(pts):
    return ", ".join(f"({20 + 40 * x:.1f},{20 + 40 * y:.1f})" for x, y in sorted(pts.tolist()))


CASES = [
    ("sanity: 11 disks, 160 x 110; true value 40 mm (a row of four in 160 mm is exactly 40 apart)", 11, 110),
    ("sanity: 11 disks, 160 x 109.282; 4-3-4 rows give exactly 40 mm", 11, 40 + 40 * 3 ** 0.5),
    ("Problem 2: 12 disks, 160 x 112", 12, 112),
    ("Problem 8 scope: 11 disks, 160 x 108, any arrangement", 11, 108),
]
for label, n, H in CASES:
    m, pts = best_min_distance(n, 3.0, (H - 40) / 40)
    log(f"{label}: best minimum centre distance found {40 * m:.3f} mm "
        f"({'fits' if m >= 1 - 1e-6 else 'does not fit in this search'})")
    log("    centres (mm from lower-left interior corner): " + fmt(pts))

log("")
log("Twelve disks, 160 mm wide, other heights (three straight rows of four need 120 mm):")
for H in (114, 116, 118, 120):
    m, pts = best_min_distance(12, 3.0, (H - 40) / 40, starts=200, seed=3)
    log(f"    height {H} mm: best minimum centre distance found {40 * m:.3f} mm")

(HERE / "check_packing.py.out").write_text("\n".join(OUT) + "\n")
