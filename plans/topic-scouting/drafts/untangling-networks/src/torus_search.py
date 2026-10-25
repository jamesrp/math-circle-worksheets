"""Find straight-line drawings on the flat torus (portal board) for given dot positions.

Each link is a straight segment from u to a translate v+(dx,dy) of v; the search
backtracks over translates so that no two links meet except at shared dots."""
import itertools
import math
import sys

from geom import torus_check, torus_segments_cross, torus_edge_segments, torus_vertex_on_edge


def find_embedding(pos, edges, maxlen=0.95):
    cands = {}
    for (u, v) in edges:
        cs = []
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                s = torus_edge_segments(pos[u], pos[v], (dx, dy))
                L = math.dist(*s)
                if L < maxlen and not torus_vertex_on_edge(pos, s, (u, v), tol=0.05):
                    cs.append((L, (dx, dy)))
        cs.sort()
        cands[(u, v)] = [c[1] for c in cs]
    order = sorted(edges, key=lambda e: len(cands[e]))
    chosen = {}

    def ok(e, off):
        s = torus_edge_segments(pos[e[0]], pos[e[1]], off)
        for f, offf in chosen.items():
            t = torus_edge_segments(pos[f[0]], pos[f[1]], offf)
            if torus_segments_cross(s, t, len(set(e) & set(f))):
                return False
        return True

    def bt(i):
        if i == len(order):
            return True
        e = order[i]
        for off in cands[e]:
            if ok(e, off):
                chosen[e] = off
                if bt(i + 1):
                    return True
                del chosen[e]
        return False

    return dict(chosen) if bt(0) else None


K33 = [(h, w) for h in "ABC" for w in "DEF"]
K5 = list(itertools.combinations("ABCDE", 2))
K6 = list(itertools.combinations("ABCDEF", 2))
K7 = list(itertools.combinations("ABCDEFG", 2))

if __name__ == "__main__":
    # houses in a top row, wells in a bottom row, various shifts
    found = []
    for hy, wy in [(0.75, 0.25), (0.7, 0.3), (0.8, 0.3), (0.65, 0.2)]:
        for shift in (0, 1 / 6):
            pos = {"A": (1 / 6, hy), "B": (1 / 2, hy), "C": (5 / 6, hy),
                   "D": ((1 / 6 + shift) % 1, wy), "E": ((1 / 2 + shift) % 1, wy), "F": ((5 / 6 + shift) % 1, wy)}
            emb = find_embedding(pos, K33)
            print("K33", hy, wy, shift, emb is not None, emb)


def corner_clear(pos, emb, delta=0.08):
    """Minimum distance from any link (in the cover) to any lattice corner point."""
    from geom import point_seg_dist
    best = 9
    for (u, v), off in emb.items():
        s = torus_edge_segments(pos[u], pos[v], off)
        for i in range(-1, 3):
            for j in range(-1, 3):
                best = min(best, point_seg_dist((i, j), *s))
    return best


def search_k33_layouts():
    res = []
    xs_opts = [(0.2, 0.5, 0.8), (1 / 6, 0.5, 5 / 6), (0.18, 0.5, 0.82)]
    for hx in xs_opts:
        for hy in (0.68, 0.7, 0.72, 0.75):
            for wy in (0.25, 0.28, 0.3, 0.32):
                for sh in (0.0, 0.08, -0.08, 0.1, -0.1):
                    pos = {"A": (hx[0], hy), "B": (hx[1], hy), "C": (hx[2], hy),
                           "D": (hx[0] + sh, wy), "E": (hx[1] + sh, wy), "F": (hx[2] + sh, wy)}
                    emb = find_embedding(pos, K33)
                    if emb:
                        res.append((corner_clear(pos, emb), hx, hy, wy, sh, emb))
    res.sort(key=lambda t: -t[0])
    for r in res[:6]:
        print(r)
