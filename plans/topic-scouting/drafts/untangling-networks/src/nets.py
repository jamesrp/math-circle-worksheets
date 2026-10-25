"""Network data for Week NN (untangling networks) and TikZ snippet generation.

Run:  python3 nets.py      (writes gen/*.tex and prints the checks)
"""
import itertools
import math
import os

import networkx as nx

from geom import clarity, crossings, torus_check
from tikzgen import SEAM, dot, game_board, house, link_list, network, portal_frame, well

HERE = os.path.dirname(os.path.abspath(__file__))
GEN = os.path.join(HERE, "gen")
os.makedirs(GEN, exist_ok=True)


def E(s):
    return [tuple(x) for x in s.split()]


def pentagon(labels, R=2.6, cx=3.0, cy=2.6, start=90):
    return {v: (cx + R * math.cos(math.radians(start + 72 * i)), cy + R * math.sin(math.radians(start + 72 * i)))
            for i, v in enumerate(labels)}


# ---------------------------------------------------------------- tangled pictures
# name: (positions in grid units, links, expected crossings, planar?)
PICS = {
    # K-1, Problem 1 (four dots)
    "k_bowtie": ({"A": (1, 5), "B": (5, 0), "C": (4, 5), "D": (0, 0)}, E("AB BC CD AD"), 1, True),
    "k_kite": ({"A": (0, 4), "B": (5, 1), "C": (1, 0), "D": (4, 5)}, E("AB AC BC BD CD"), 1, True),
    "k_k4": ({"A": (0.5, 5), "B": (5, 5), "C": (5, 0.5), "D": (0.5, 0.5)}, E("AB AC AD BC BD CD"), 1, True),
    # K-1, Problem 4 (five dots)
    "k_star": (pentagon("ADBEC"), E("AB BC CD DE AE"), 5, True),
    "k_fan": ({"A": (1, 5), "B": (4, 0), "C": (4, 5), "D": (6, 3), "E": (0, 2)}, E("AB BC CD AE BE CE DE"), 3, True),
    # K-1, Problem 4 (six dots)
    "k_prism": ({"A": (4, 0), "B": (1, 3), "C": (0, 1), "D": (2, 5), "E": (5, 5), "F": (6, 3)},
                E("AB AC BC DE DF EF AD BE CF"), 4, True),
    # K-1, Problem 5 (all five joined)
    "k_k5": (pentagon("ABCDE"), E("AB AC AD AE BC BD BE CD CE DE"), 5, False),
    # Grades 2-3 and 4-5, Problem 1
    "n1": ({"A": (4, 5), "B": (0, 3), "C": (6, 2), "D": (4, 0), "E": (2, 1)}, E("AB AC AD AE BC CD DE"), 2, True),
    "n2": ({"A": (1, 5), "B": (5, 4), "C": (3, 1), "D": (6, 0), "E": (0, 0)},
           E("AB AC AD AE BC BD BE CD CE DE"), 3, False),
    "n3": ({"A": (1, 5), "B": (3, 0), "C": (6, 5), "D": (6, 1), "E": (0, 1)},
           E("AB AC AD AE BC BD BE CD CE"), 3, True),
    "n4": ({"A": (1, 4), "B": (2, 0), "C": (4, 1), "D": (4, 5), "E": (0, 1), "F": (6, 3)},
           E("AB AC BC DE DF EF AD BE CF"), 4, True),
    "n5": ({"A": (6, 3), "B": (3, 0), "C": (4, 5), "D": (5, 1), "E": (0, 0), "F": (0, 4)},
           E("AD AE AF BD BE BF CD CE CF"), 5, False),
    "n6": ({"A": (4, 0), "B": (2, 5), "C": (0, 3), "D": (6, 1), "E": (6, 5), "F": (4, 3)},
           E("AB AC AD AE BC BE BF CD CF DE DF EF"), 4, True),
}

# rescale the pentagon pictures into the same 0..6 x 0..5 box
for nm in ("k_star", "k_k5"):
    pos, ed, nc, pl = PICS[nm]
    xs = [p[0] for p in pos.values()]
    ys = [p[1] for p in pos.values()]
    k = 5 / (max(ys) - min(ys))  # same factor on both axes keeps the pentagon regular
    PICS[nm] = ({v: ((p[0] - min(xs)) * k + 0.4, (p[1] - min(ys)) * k) for v, p in pos.items()}, ed, nc, pl)


def check_pictures():
    print("== tangled pictures ==")
    ok = True
    for nm, (pos, ed, nc, pl) in PICS.items():
        G = nx.Graph(ed)
        G.add_nodes_from(pos)
        planar, emb = nx.check_planarity(G)
        c = clarity(pos, ed)
        V, Ecount = len(pos), len(ed)
        assert len(set(map(frozenset, ed))) == Ecount, nm + " has a repeated link"
        assert nx.is_connected(G), nm
        F = Ecount - V + 2 if planar else None
        flag = ""
        if c["n_cross"] != nc or planar != pl:
            flag = "  <-- MISMATCH"
            ok = False
        if c["vdist"] < 0.45 or c["cv"] < 0.45:
            flag += "  <-- CLARITY"
        print(f"{nm:9s} V={V} E={Ecount} planar={planar} F={F} crossings={c['n_cross']} "
              f"vdist={c['vdist']:.2f} cc={c['cc']:.2f} cv={c['cv']:.2f} ang={c['ang']:.0f} vangle={c['vangle']:.0f}{flag}")
        if planar:
            # count faces of the combinatorial embedding as a cross-check of V - E + F = 2
            nf = 0
            seen = set()
            for u, v in emb.edges():
                if (u, v) in seen:
                    continue
                face = emb.traverse_face(u, v, mark_half_edges=seen)
                nf += 1
            assert nf == F, (nm, nf, F)
    return ok


PIC_SCALE = {"k_bowtie": (0.9, 0.42), "k_kite": (0.9, 0.42), "k_k4": (0.9, 0.42),
             "k_star": (0.88, 0.42), "k_fan": (0.88, 0.42), "k_prism": (0.88, 0.42), "k_k5": (1.12, 0.45)}
# network 5 is the houses-and-wells network: A, B, C are houses and D, E, F are wells
PIC_ICONS = {"n5": {"A": "house", "B": "house", "C": "house", "D": "well", "E": "well", "F": "well"}}


def write_pictures():
    for nm, (pos, ed, nc, pl) in PICS.items():
        big = nm.startswith("k_")
        scale, r = PIC_SCALE.get(nm, (0.98, 0.42) if big else (0.78, 0.32))
        font = r"\sffamily\bfseries\Large" if big else r"\sffamily\bfseries"
        body = network(pos, ed, scale, r, font=font, link_w="1.6pt" if big else "1.3pt", icons=PIC_ICONS.get(nm))
        xs = [p[0] * scale for p in pos.values()]
        ys = [p[1] * scale for p in pos.values()]
        rb = 1.2 * r if nm in PIC_ICONS else r  # house roofs reach a little higher than a dot
        bb = f"\\useasboundingbox ({min(xs) - rb:.3f},{min(ys) - rb:.3f}) rectangle ({max(xs) + rb:.3f},{max(ys) + rb:.3f});\n"
        with open(os.path.join(GEN, f"pic_{nm}.tex"), "w") as f:
            f.write("\\begin{tikzpicture}[baseline=(current bounding box.center)]\n" + bb + body + "\\end{tikzpicture}%\n")
        print(f"  pic_{nm}: {max(xs) - min(xs) + 2 * r:.2f} x {max(ys) - min(ys) + 2 * r:.2f} cm")
        cols = 1 if len(ed) <= 6 else 2
        lf = r"\sffamily\Large" if big else r"\sffamily"
        with open(os.path.join(GEN, f"list_{nm}.tex"), "w") as f:
            f.write(link_list(sorted(ed), cols=cols, font=lf) + "%\n")


# ---------------------------------------------------------------- crossing-number witnesses (checks only)
def best_straight_drawing(edges, verts, target, trials=4000, seed=7):
    import random
    rnd = random.Random(seed)
    grid = [(x, y) for x in range(7) for y in range(7)]
    best = None
    for _ in range(trials):
        pos = dict(zip(verts, rnd.sample(grid, len(verts))))
        c = clarity(pos, edges)
        if c["vdist"] < 0.2:
            continue
        if best is None or c["n_cross"] < best[0]:
            best = (c["n_cross"], pos)
            if best[0] <= target:
                break
    return best


def check_crossing_numbers():
    print("== fewest-crossing witnesses (straight links) ==")
    K5 = list(itertools.combinations("ABCDE", 2))
    K33 = [(h, w) for h in "ABC" for w in "DEF"]
    K6 = list(itertools.combinations("ABCDEF", 2))
    for nm, ed, vs, tgt in (("K5", K5, "ABCDE", 1), ("K3,3", K33, "ABCDEF", 1), ("K6", K6, "ABCDEF", 3)):
        n, pos = best_straight_drawing(ed, vs, tgt)
        print(f"{nm}: drawing with {n} crossings found, e.g. {pos}")
        assert n == tgt
    # lower bounds from E <= 3V-6 (and E <= 2V-4 without triangles): delete one link per crossing
    print("lower bounds: K5 10-(3*5-6)=1, K3,3 9-(2*6-4)=1, K6 15-(3*6-6)=3")
    print("game length 3n-6: n=4 -> 6 (second player), n=5 -> 9 (first), n=6 -> 12 (second)")


# ---------------------------------------------------------------- portal boards
K33 = [(h, w) for h in "ABC" for w in "DEF"]
K5L = list(itertools.combinations("ABCDE", 2))
K6L = list(itertools.combinations("ABCDEF", 2))
K7L = list(itertools.combinations("ABCDEFG", 2))

# Dot positions are fractions of the board side (y up).  Each layout was moved by a torus
# translation (or symmetry of the square) from the draft so that no dot sits on or next to a
# Week 41 seam mark; translations keep every portal drawing valid, and check_portals re-checks.
TOR_K33 = {"A": (0.15, 0.75), "B": (0.45, 0.75), "C": (0.75, 0.75), "D": (0.25, 0.25), "E": (0.55, 0.25), "F": (0.85, 0.25)}
# K5: the lattice generated by (2/5, -1/5), on the grid of odd tenths
TOR_K5 = {"A": (0.5, 0.9), "B": (0.9, 0.7), "C": (0.3, 0.5), "D": (0.7, 0.3), "E": (0.1, 0.1)}
# K7: the 7-point lattice generated by (1/7, 3/7), on the grid of odd fourteenths; K6 drops G
_pts7 = [((5 / 14 + k / 7) % 1, (13 / 14 + 3 * k / 7) % 1) for k in range(7)]
TOR_K6 = dict(zip("ABCDEF", sorted([p for k, p in enumerate(_pts7) if k != 6], key=lambda p: (-p[1], p[0]))))
TOR_K7 = dict(TOR_K6, G=_pts7[6])  # same six dots and letters, plus G

PORTAL_SIZES = {"k33": 7.2, "k5": 7.2, "k6": 8.2, "k7": 8.2, "blank": 5.6, "blank_big": 8.2, "example": 5.0}


def seam_clearance(pos, S, r):
    """Smallest gap (cm) between a dot of radius r and a seam mark or the board's edge."""
    from geom import point_seg_dist
    pts = [((0, SEAM["circle_y"]), 0.17), ((1, SEAM["circle_y"]), 0.17), ((SEAM["diamond_x"], 0), 0.18), ((SEAM["diamond_x"], 1), 0.18)]
    (a0, a1), (b0, b1) = SEAM["arrow_tb"], SEAM["arrow_lr"]
    segs = [((a0, 0), (a1, 0)), ((a0, 1), (a1, 1)), ((0, b0), (0, b1)), ((1, b0), (1, b1))]
    worst = 99
    for x, y in pos.values():
        c = (x * S, y * S)
        for m, mr in pts:
            worst = min(worst, math.dist(c, (m[0] * S, m[1] * S)) - r - mr)
        for a, b in segs:
            worst = min(worst, point_seg_dist(c, (a[0] * S, a[1] * S), (b[0] * S, b[1] * S)) - r - 0.13)
        worst = min(worst, min(x, 1 - x, y, 1 - y) * S - r)
    return worst


def check_portals():
    from torus_search import find_embedding
    print("== portal-board embeddings (straight links through portals) ==")
    for nm, key, pos, ed in (("K3,3", "k33", TOR_K33, K33), ("K5", "k5", TOR_K5, K5L), ("K6", "k6", TOR_K6, K6L), ("K7", "k7", TOR_K7, K7L)):
        emb = find_embedding(pos, ed)
        assert emb is not None, nm
        assert torus_check(pos, emb) == [], nm
        n_portal = sum(1 for o in emb.values() if o != (0, 0))
        gap = seam_clearance(pos, PORTAL_SIZES[key], 0.36 if key == "k33" else 0.3)
        print(f"{nm}: crossing-free on the portal board; {n_portal} of {len(ed)} links use a portal; "
              f"dots clear seam marks and edges by {gap:.2f} cm")
        assert gap > 0.25, nm
        # also: these cannot be drawn without crossings in the plane
        assert not nx.check_planarity(nx.Graph(ed))[0]


def write_portals():
    def board(pos, size, kind, r=0.3):
        out = portal_frame(0, 0, size)
        for v, (x, y) in pos.items():
            p = (x * size, y * size)
            if kind == "hw":
                out += house(p, 0.38, v) if v in "ABC" else well(p, 0.36, v)
            elif kind == "dots":
                out += dot(v, p, r)
        return out

    def save(nm, body):
        with open(os.path.join(GEN, f"{nm}.tex"), "w") as f:
            f.write("\\begin{tikzpicture}[baseline=(current bounding box.center)]\n" + body + "\\end{tikzpicture}%\n")

    S = PORTAL_SIZES
    save("portal_k33", board(TOR_K33, S["k33"], "hw"))
    save("portal_k5", board(TOR_K5, S["k5"], "dots"))
    save("portal_k6", board(TOR_K6, S["k6"], "dots"))
    save("portal_k7", board(TOR_K7, S["k7"], "dots"))
    save("portal_blank", board({}, S["blank"], "none"))
    save("portal_blank_big", board({}, S["blank_big"], "none"))

    # Convention example (not one of the task networks): three lettered dots joined in a
    # triangle.  A-B leaves through the right side and comes back in on the left (marked 1);
    # A-C leaves through the top and comes back in at the bottom (marked 2); B-C stays inside.
    # Links are straight in the repeated plane.  The crossing places avoid the seam marks.
    s = S["example"]
    ex = portal_frame(0, 0, s)
    A, B, C = (0.74, 0.50), (0.22, 0.68), (0.34, 0.20)
    t = (1 - A[0]) / (B[0] + 1 - A[0])          # A -> B + (1, 0)
    h = A[1] + t * (B[1] - A[1])
    t2 = (1 - A[1]) / (C[1] + 1 - A[1])         # A -> C + (0, 1)
    w = A[0] + t2 * (C[0] - A[0])
    assert SEAM["arrow_lr"][1] + 0.1 < h < SEAM["circle_y"] - 0.1, h
    assert SEAM["diamond_x"] + 0.1 < w < SEAM["arrow_tb"][0] - 0.1, w
    segs = [(A, (1, h)), ((0, h), B), (A, (w, 1)), ((w, 0), C), (B, C)]
    for a, b in segs:
        ex += f"\\draw[line width=1.3pt] ({a[0] * s:.3f},{a[1] * s:.3f}) -- ({b[0] * s:.3f},{b[1] * s:.3f});\n"
    for v, p in (("A", A), ("B", B), ("C", C)):
        ex += dot(v, (p[0] * s, p[1] * s), 0.27, font=r"\sffamily\bfseries\small")
    g = 0.32
    lab = r"\sffamily\bfseries\small"
    for x, y, txt in ((s + g, h * s, "1"), (-g, h * s, "1"), (w * s, s + g, "2"), (w * s, -g, "2")):
        ex += f"\\node[font={lab}, inner sep=1pt] at ({x:.3f},{y:.3f}) {{{txt}}};\n"
    print(f"portal example: right/left crossing at height {h:.3f}, top/bottom crossing at x = {w:.3f}")
    save("portal_example", ex)


# ---------------------------------------------------------------- link-game boards
def game_points(n, seed, w, h, starts=60, steps=1500):
    """n dots for the link game: a large triangle with n - 3 dots inside it, in general position.

    With exactly three dots on the outside, every finished game drawn with straight links
    has 3n - 6 links, the same as when links bend, so a game cannot look finished too early.
    The inside dots are spread by a seeded hill climb that keeps every dot away from the
    other dots and from every straight segment joining two other dots."""
    import random
    from geom import point_seg_dist
    rnd = random.Random(seed)
    T = [(0.12 * w, 0.13 * h), (0.88 * w, 0.13 * h), (0.5 * w, 0.89 * h)]

    def inside(p, m):
        # p at least m (cm) inside every side of T
        for i in range(3):
            a, b, c = T[i], T[(i + 1) % 3], T[(i + 2) % 3]
            cross = (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0])
            side = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
            if cross * side <= 0 or abs(cross) / math.dist(a, b) < m:
                return False
        return True

    def score(pts):
        dmin = min(math.dist(p, q) for p, q in itertools.combinations(pts, 2))
        lmin = min(point_seg_dist(pts[k], pts[i], pts[j])
                   for i, j in itertools.combinations(range(n), 2) for k in range(n) if k not in (i, j))
        return min(dmin, 2.2 * lmin), dmin, lmin

    best = None
    for _ in range(starts):
        pts = list(T)
        while len(pts) < n:
            p = (rnd.uniform(0, w), rnd.uniform(0, h))
            if inside(p, 0.55):
                pts.append(p)
        sc = score(pts)
        for it in range(steps):
            k = rnd.randrange(3, n)
            step = 0.3 * (1 - it / steps) + 0.02
            q = (pts[k][0] + rnd.gauss(0, step), pts[k][1] + rnd.gauss(0, step))
            if not inside(q, 0.55):
                continue
            cand = pts[:k] + [q] + pts[k + 1:]
            s2 = score(cand)
            if s2[0] > sc[0]:
                pts, sc = cand, s2
        if best is None or sc[0] > best[0]:
            best = (sc[0], pts, sc[1], sc[2])
    return best


def check_game_board(pts):
    """Three dots on the outside, no three in a line, and a greedy straight triangulation has 3n - 6 links."""
    from geom import seg_intersection
    n = len(pts)
    hull = []  # gift wrapping
    start = min(range(n), key=lambda i: pts[i])
    i = start
    while True:
        hull.append(i)
        j = (i + 1) % n
        for k in range(n):
            o = (pts[j][0] - pts[i][0]) * (pts[k][1] - pts[i][1]) - (pts[j][1] - pts[i][1]) * (pts[k][0] - pts[i][0])
            if o < 0:
                j = k
        i = j
        if i == start:
            break
    assert len(hull) == 3, hull
    links = []
    for a, b in sorted(itertools.combinations(range(n), 2), key=lambda e: math.dist(pts[e[0]], pts[e[1]])):
        if all(set((a, b)) & set(e) or seg_intersection(pts[a], pts[b], pts[e[0]], pts[e[1]]) is None for e in links):
            links.append((a, b))
    assert len(links) == 3 * n - 6, (n, len(links))
    return len(links)


GAME_BOARDS = {}  # name -> (points as fractions, w, h)


def write_game_boards():
    print("== link-game boards ==")
    specs = {"k": (5.6, 6.3, (4, 5), 0.25), "o": (5.6, 5.6, (4, 5, 6), 0.22)}
    for band, (w, h, ns, r) in specs.items():
        for n in ns:
            score, pts, dmin, lmin = game_points(n, 100 + n, w, h)
            for flip in (False, True):
                q = [(x, h - y) if flip else (x, y) for x, y in pts]
                links = check_game_board(q)
                frac = [(x / w, y / h) for x, y in q]
                nm = f"game_{band}{n}{'b' if flip else 'a'}"
                with open(os.path.join(GEN, nm + ".tex"), "w") as f:
                    f.write("\\begin{tikzpicture}[baseline=(current bounding box.center)]\n" + game_board(frac, w, h, r) + "\\end{tikzpicture}%\n")
            print(f"{band}{n}: {n} dots, closest pair {dmin:.2f} cm, closest dot to another pair's link {lmin:.2f} cm; "
                  f"every finished straight-link game has {links} links")


# ---------------------------------------------------------------- other figures
def write_misc():
    # region example: 4 dots, 5 links, 3 regions (regions numbered, outside included)
    P = {1: (0, 0), 2: (4.0, 0), 3: (4.0, 2.8), 4: (0, 2.8)}
    ed = [(1, 2), (2, 3), (3, 4), (4, 1), (1, 3)]
    body = ""
    for a, b in ed:
        body += f"\\draw[line width=1.3pt] ({P[a][0]},{P[a][1]}) -- ({P[b][0]},{P[b][1]});\n"
    for p in P.values():
        body += f"\\draw[line width=1pt, fill=white] ({p[0]},{p[1]}) circle (0.22);\n"
    lab = r"\sffamily\bfseries\large\color{black!60}"
    body += f"\\node[font={lab}] at (2.75,0.85) {{1}};\n\\node[font={lab}] at (1.2,1.95) {{2}};\n"
    body += f"\\node[font={lab}] at (4.75,1.4) {{3}};\n"
    with open(os.path.join(GEN, "region_example.tex"), "w") as f:
        f.write("\\begin{tikzpicture}[baseline=(current bounding box.center)]\n" + body + "\\end{tikzpicture}%\n")

    # houses and wells starting pictures for K-1 (letters match the kit dots)
    def hw(nh, nw, width=6.6, height=5.6):
        out = f"\\useasboundingbox (0,0) rectangle ({width},{height});\n"
        hx = [width * (i + 0.5) / nh for i in range(nh)]
        wx = [width * (i + 0.5) / nw for i in range(nw)]
        letters = iter("ABCDEF")
        for x in hx:
            out += house((x, height - 0.85), 0.72, next(letters), font=r"\sffamily\bfseries\Large")
        for x in wx:
            out += well((x, 0.75), 0.68, next(letters), font=r"\sffamily\bfseries\Large")
        return out

    for nm, (nh, nw) in (("hw23", (2, 3)), ("hw33", (3, 3))):
        with open(os.path.join(GEN, f"{nm}.tex"), "w") as f:
            f.write("\\begin{tikzpicture}[baseline=(current bounding box.center)]\n" + hw(nh, nw) + "\\end{tikzpicture}%\n")


if __name__ == "__main__":
    ok = check_pictures()
    check_crossing_numbers()
    check_portals()
    write_pictures()
    write_portals()
    write_game_boards()
    write_misc()
    print("pictures ok" if ok else "PICTURE MISMATCH")
