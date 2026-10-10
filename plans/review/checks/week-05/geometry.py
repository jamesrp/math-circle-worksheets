"""Side-view geometry of the 'eye down at the table' rule (guide p.2, 'Test with the real cubes').

Towers of 3/4-inch cubes stand in a row; the eye is at height e above the table and distance d
from the near face of the first tower.  A tower counts as visible when some point of its front face
or top face can be joined to the eye by a segment that misses every tower in front of it.
We compare the visible count with the printed rule ("taller than every tower in front of it") for
every row of three and four, and report the thinnest visible strip of a tower that should be seen.

Run:  python3 -I geometry.py > geometry.out
"""
from itertools import permutations

C = 0.75  # cube edge, inches


def visible_strip(row, d, e, s):
    """For each tower: the visible height (inches) of its front face, or of its top face depth,
    whichever is larger; 0 when hidden."""
    xs = [d + i * s for i in range(len(row))]
    out = []
    for j, h in enumerate(row):
        H = h * C
        best = 0.0
        # sample points on the front face (x = xs[j], y in [0, H]) and the top face (y = H)
        # the top face can only be seen from above it
        pts = [(xs[j], H * t / 200) for t in range(201)] + \
            [(xs[j] + C * t / 50, H) if e > H else (xs[j], -1.0) for t in range(51)]
        vis = []
        for px, py in pts:
            blocked = False
            for k in range(j):
                Hk = row[k] * C
                for x in (xs[k], xs[k] + C):
                    y = e + (py - e) * x / px
                    if y < Hk - 1e-9:
                        blocked = True
                        break
                if blocked:
                    break
            vis.append(not blocked)
        front = [py for (px, py), v in zip(pts[:201], vis[:201]) if v]
        top = sum(v for (px, py), v in zip(pts[201:], vis[201:]) if py >= 0)
        if front:
            best = H - min(front)
        if top:
            best = max(best, C * top / 50)
        out.append(best)
    return out


def rule(row):
    best, res = 0, []
    for h in row:
        res.append(h > best)
        best = max(best, h)
    return res


def check(d, e, s, n):
    wrong, thinnest = [], 9.0
    for row in permutations(range(1, n + 1)):
        strips = visible_strip(row, d, e, s)
        want = rule(row)
        got = [v > 1e-9 for v in strips]
        if got != want:
            wrong.append("".join(map(str, row)))
        for v, w in zip(strips, want):
            if w:
                thinnest = min(thinnest, v)
    return wrong, thinnest


print("Row 3,1,2,4 on a 1-inch grid, eye at table level (e = 0): is the 4 visible over the 3?")
for d in (6, 8, 8.9, 9.1, 10, 12):
    print(f"  d = {d:>4} in: visible strip of the 4 = {visible_strip((3, 1, 2, 4), d, 0.0, 1.0)[3]:.3f} in")
print()
for s, label in ((1.0, "1-inch grid"), (0.75, "towers touching")):
    for d in (9, 12):
        for e in (0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5):
            res = []
            for n in (3, 4):
                wrong, thin = check(d, e, s, n)
                res.append(f"n={n}: {len(wrong)} wrong {wrong[:4]}, thinnest seen strip {thin:.2f} in")
            print(f"{label}, d={d} in, eye {e} in: " + "; ".join(res))
