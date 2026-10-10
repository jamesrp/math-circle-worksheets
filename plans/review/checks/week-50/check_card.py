"""Card-stage checks for Week 50 (fewest turns in a strip of half-height d).

Rectangle 160 x 120 mm, diagonal y = 3x/4, strip |y - 3x/4| <= d (closed).
1. Lower bound from horizontal spans: interior horizontal piece <= 2d*(4/3),
   a piece at y=0 or y=120 <= d*(4/3).  Minimise turns over end types.
2. Exact witnesses checked with fractions.
3. 0-1 BFS on a lattice containing the witnesses' coordinates (upper bound).
Run: python3 check_card.py
"""
from fractions import Fraction as F
from collections import deque

W, H = F(160), F(120)


def gap(x, y):
    return y - F(3, 4) * x


def lower_bound(d):
    span, end = F(4, 3) * 2 * d, F(4, 3) * d
    best = None
    for pieces in range(1, 200):
        # alternating H/V pieces; try both starting types
        for start_h in (True, False):
            types = [(i % 2 == 0) == start_h for i in range(pieces)]
            hs = [i for i, t in enumerate(types) if t]
            vs = [i for i, t in enumerate(types) if not t]
            if not hs or not vs:
                continue
            cap = sum(end if i in (0, pieces - 1) else span for i in hs)
            # vertical capacity similarly (vertical span 2d; ends d)
            vcap = sum(d if i in (0, pieces - 1) else 2 * d for i in vs)
            if cap >= W and vcap >= H:
                t = pieces - 1
                if best is None or t < best:
                    best = t
        if best is not None:
            return best
    return None


def check_path(moves, d):
    x, y = F(0), F(0)
    pts = [(x, y)]
    for m, L in moves:
        L = F(L)
        if m == 'R':
            x += L
        elif m == 'U':
            y += L
        else:
            raise ValueError
        pts.append((x, y))
    ok = (x, y) == (W, H) and all(abs(gap(*p)) <= d for p in pts)
    turns = sum(1 for a, b in zip(moves, moves[1:]) if a[0] != b[0])
    length = sum(F(L) for _, L in moves)
    return ok, turns, length


def bfs_min_turns(d, dx, dy):
    nx, ny = int(W / dx), int(H / dy)
    assert nx * dx == W and ny * dy == H
    inside = lambda i, j: abs(gap(i * dx, j * dy)) <= d
    INF = 10 ** 9
    dist = {}
    dq = deque()
    for dirn in (0, 1):  # 0 = right, 1 = up
        dist[(0, 0, dirn)] = 0
        dq.append((0, 0, dirn))
    while dq:
        i, j, dirn = dq.popleft()
        c = dist[(i, j, dirn)]
        # continue straight (cost 0)
        ni, nj = (i + 1, j) if dirn == 0 else (i, j + 1)
        if ni <= nx and nj <= ny and inside(ni, nj):
            if dist.get((ni, nj, dirn), INF) > c:
                dist[(ni, nj, dirn)] = c
                dq.appendleft((ni, nj, dirn))
        # turn (cost 1)
        od = 1 - dirn
        if dist.get((i, j, od), INF) > c + 1:
            dist[(i, j, od)] = c + 1
            dq.append((i, j, od))
    return min(dist.get((nx, ny, 0), INF), dist.get((nx, ny, 1), INF))


if __name__ == '__main__':
    for d in (F(15), F(8), F(15, 2)):
        print(f"d = {d} mm: lower bound on turns = {lower_bound(d)}")

    w15 = [('R', 20)] + [('U', 30), ('R', 40)] * 3 + [('U', 30), ('R', 20)]
    print("d=15 witness (guide p.2):", check_path(w15, F(15)))

    w8 = [('R', F(32, 3))] + [('U', 16), ('R', F(64, 3))] * 7 + [('U', 8)]
    print("d=8 witness R32/3,(U16,R64/3)x7,U8:", check_path(w8, F(8)))
    g8 = [('U', F(15, 2))] + [('R', 20), ('U', 15)] * 7 + [('R', 20), ('U', F(15, 2))]
    print("d=8 guide staircase:", check_path(g8, F(8)))

    w75 = g8
    print("d=7.5 witness (same staircase):", check_path(w75, F(15, 2)))

    # lattice upper bounds; lattices contain the witnesses' coordinates
    print("BFS d=15, lattice 5 x 3.75 mm:", bfs_min_turns(F(15), F(5), F(15, 4)))
    print("BFS d=7.5, lattice 5 x 3.75 mm:", bfs_min_turns(F(15, 2), F(5), F(15, 4)))
    print("BFS d=8, lattice 5 x 3.75 mm (misses 32/3):",
          bfs_min_turns(F(8), F(5), F(15, 4)))
    print("BFS d=8, lattice 16/3 x 4 mm (contains 32/3, 16):",
          bfs_min_turns(F(8), F(16, 3), F(4)))
