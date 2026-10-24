"""Independent planar-game engine for 2-Sprigs, Sprouts, Brussels Sprouts.

Position: tuple of regions; region = tuple of boundaries; boundary = tuple
(cyclic) of vertex ids (corner occurrences). lives: dict vertex -> lives.
"""
import sys, random
from functools import lru_cache
sys.setrecursionlimit(100000)

def rot(b, i):
    return b[i:] + b[:i]

class G:
    def __init__(self, kind):
        self.kind = kind  # 'sprigs','sprouts','brussels'

    def start(self, n):
        lives = {}
        bounds = []
        if self.kind in ('sprigs', 'sprouts'):
            L = 2 if self.kind == 'sprigs' else 3
            for v in range(n):
                lives[v] = L
                bounds.append((v,))
        else:
            k = 0
            for _ in range(n):
                c = k; k += 1
                lives[c] = 0
                b = []
                for _ in range(4):
                    t = k; k += 1
                    lives[t] = 1
                    b += [c, t]
                bounds.append(tuple(b))
        return (tuple(bounds),), lives

    def moves(self, regions, lives):
        w = max(lives) + 1
        out = []
        for ri, R in enumerate(regions):
            rest_regions = regions[:ri] + regions[ri+1:]
            corners = [(bi, pi) for bi, b in enumerate(R) for pi in range(len(b))]
            for x in range(len(corners)):
                for y in range(x, len(corners)):
                    bi, pi = corners[x]; bj, pj = corners[y]
                    u = R[bi][pi]; v = R[bj][pj]
                    # life check
                    if u == v:
                        if self.kind == 'brussels':
                            continue
                        if lives[u] < 2:
                            continue
                    else:
                        if lives[u] < 1 or lives[v] < 1:
                            continue
                    nl = dict(lives)
                    nl[u] -= 1; nl[v] -= 1
                    if self.kind == 'sprigs':
                        m1 = (); m2 = ()
                    elif self.kind == 'sprouts':
                        nl[w] = 1; m1 = (w,); m2 = (w,)
                    else:
                        nl[w] = 0; nl[w+1] = 1; nl[w+2] = 1
                        m1 = (w, w+1, w); m2 = (w, w+2, w)
                    others = [R[k] for k in range(len(R)) if k not in (bi, bj)]
                    if bi != bj:
                        A = rot(R[bi], pi); B = rot(R[bj], pj)
                        # walk: u, m1, v, B[1:], (v again if B nontrivial), m2 reversed?, u, A[1:]
                        # the path u->v is traversed u..v on one side and v..u on other
                        Aw = A + ((u,) if len(A) > 1 else ())  # u a1..ak u  (u twice if not isolated)
                        Bw = B + ((v,) if len(B) > 1 else ())
                        if len(A) == 1: Aw = (u,)
                        if len(B) == 1: Bw = (v,)
                        # cyclic: Aw (ending at u) -> m1 -> Bw (v .. v) -> m2 reversed -> back to start u
                        newb = Aw + m1 + Bw + tuple(reversed(m2))
                        newR = tuple(others) + (newb,)
                        out.append((rest_regions + (newR,), nl))
                    else:
                        b = rot(R[bi], pi)
                        t = (pj - pi) % len(b)
                        if t == 0:
                            if len(b) == 1:
                                s1 = (u,) + m1
                                s2 = (u,) + tuple(reversed(m2))
                            else:
                                s1 = (u,) + m1
                                s2 = b + (u,) + tuple(reversed(m2))
                        else:
                            s1 = b[:t+1] + tuple(reversed(m1))
                            s2 = b[t:] + (b[0],) + m2
                        for mask in range(1 << len(others)):
                            g1 = tuple(others[k] for k in range(len(others)) if mask >> k & 1)
                            g2 = tuple(others[k] for k in range(len(others)) if not mask >> k & 1)
                            out.append((rest_regions + (g1 + (s1,), g2 + (s2,)), nl))
        return out

def canon(regions, lives):
    """Relabel-free-ish key: drop dead vertices from boundaries, drop empty
    boundaries; normalise rotations and orderings. Keep labels (exact)."""
    rs = []
    for R in regions:
        bs = []
        for b in R:
            c = tuple(x for x in b if lives[x] > 0)
            if not c:
                continue
            bs.append(min(rot(c, i) for i in range(len(c))))
        bs.sort()
        if bs:
            rs.append(tuple(bs))
    rs.sort()
    lv = tuple(sorted((x, l) for x, l in lives.items() if l > 0))
    return (tuple(rs), lv)

def relabel_canon(regions, lives):
    """Canonical form up to renaming of live vertices (brute but ok for small)."""
    key = canon(regions, lives)
    rs, lv = key
    # rename vertices by first appearance in sorted structure, iterate to fixpoint-ish
    # (heuristic; exact labels as fallback are still correct, just less sharing)
    return key

def lengths(g, regions, lives, memo):
    key = canon(regions, lives)
    if key in memo:
        return memo[key]
    ms = g.moves(regions, lives)
    if not ms:
        res = frozenset([0])
    else:
        s = set()
        for r2, l2 in ms:
            for x in lengths(g, r2, l2, memo):
                s.add(x + 1)
        res = frozenset(s)
    memo[key] = res
    return res

def win(g, regions, lives, memo):
    key = canon(regions, lives)
    if key in memo:
        return memo[key]
    res = False
    for r2, l2 in g.moves(regions, lives):
        if not win(g, r2, l2, memo):
            res = True; break
    memo[key] = res
    return res

def randgame(g, n, rng):
    r, l = g.start(n)
    m = 0
    while True:
        ms = g.moves(r, l)
        if not ms:
            return m, sum(l.values())
        r, l = rng.choice(ms); m += 1
