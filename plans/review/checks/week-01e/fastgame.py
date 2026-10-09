"""Bitmask Sprague-Grundy solver for the rhombus-placement game (my own code).

A position is the set of free cells.  A move removes two edge-adjacent free cells.
Independent components add by XOR (normal play).  Component values are memoised on
the bitmask, reduced by the symmetries of the board that map it to itself."""
import sys
from lat import adjacent, SYMS, map_cells

sys.setrecursionlimit(10000)


class Board:
    def __init__(self, R):
        self.cells = sorted(R, key=lambda c: sorted(c))
        self.idx = {c: k for k, c in enumerate(self.cells)}
        n = len(self.cells)
        self.nb = [0] * n
        for a in range(n):
            for b in range(n):
                if a != b and adjacent(self.cells[a], self.cells[b]):
                    self.nb[a] |= 1 << b
        self.moves = [(1 << a) | (1 << b) for a in range(n) for b in range(a + 1, n) if self.nb[a] >> b & 1]
        # automorphisms: lattice symmetries + translation mapping R onto itself
        self.perms = []
        Rset = frozenset(R)
        for f in SYMS:
            img = map_cells(f, R)
            a = min(v for c in img for v in c)
            b = min(v for c in R for v in c)
            # translate so the minimum vertices agree; check all translations that could work
            for d in {(b[0] - a[0] + di, b[1] - a[1] + dj) for di in range(-3, 4) for dj in range(-3, 4)}:
                img2 = frozenset(frozenset((v[0] + d[0], v[1] + d[1]) for v in c) for c in img)
                if img2 == Rset:
                    perm = []
                    for c in self.cells:
                        ci = frozenset((f(v)[0] + d[0], f(v)[1] + d[1]) for v in c)
                        perm.append(self.idx[ci])
                    self.perms.append(perm)
        self.memo = {}
        self.n = n

    def apply(self, perm, m):
        out = 0
        while m:
            low = m & -m
            k = low.bit_length() - 1
            out |= 1 << perm[k]
            m ^= low
        return out

    def key(self, m):
        return min(self.apply(p, m) for p in self.perms) if len(self.perms) > 1 else m

    def comps(self, m):
        out = []
        while m:
            seed = m & -m
            comp = seed
            frontier = seed
            while frontier:
                low = frontier & -frontier
                frontier ^= low
                k = low.bit_length() - 1
                new = self.nb[k] & m & ~comp
                comp |= new
                frontier |= new
            out.append(comp)
            m &= ~comp
        return out

    def g(self, m):
        x = 0
        for c in self.comps(m):
            x ^= self.gc(c)
        return x

    def gc(self, c):
        if c & (c - 1) == 0:
            return 0
        k = self.key(c)
        v = self.memo.get(k)
        if v is not None:
            return v
        opts = set()
        for mv in self.moves:
            if mv & c == mv:
                opts.add(self.g(c & ~mv))
        v = 0
        while v in opts:
            v += 1
        self.memo[k] = v
        return v

    def solve(self):
        full = (1 << self.n) - 1
        win_first = [mv for mv in self.moves if self.g(full & ~mv) == 0]
        return ('1st' if win_first else '2nd'), win_first, self.moves

    def move_cells(self, mv):
        return frozenset(self.cells[k] for k in range(self.n) if mv >> k & 1)
