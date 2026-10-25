"""Fast bitmask Hex solver for small boards (used to check puzzle positions)."""
from functools import lru_cache
import sys

sys.setrecursionlimit(10000)


class Board:
    def __init__(self, n):
        self.n = n
        self.N = n * n
        self.nb = []
        for i in range(self.N):
            r, c = divmod(i, n)
            m = 0
            for dr, dc in ((0, -1), (0, 1), (-1, 0), (-1, 1), (1, 0), (1, -1)):
                rr, cc = r + dr, c + dc
                if 0 <= rr < n and 0 <= cc < n:
                    m |= 1 << (rr * n + cc)
            self.nb.append(m)
        self.top = sum(1 << c for c in range(n))
        self.bottom = sum(1 << ((n - 1) * n + c) for c in range(n))
        self.left = sum(1 << (r * n) for r in range(n))
        self.right = sum(1 << (r * n + n - 1) for r in range(n))
        self.full = (1 << self.N) - 1
        self._wins = lru_cache(maxsize=None)(self._wins_impl)

    def idx(self, r, c):
        return r * self.n + c

    def grow(self, seed, allowed):
        reach = seed & allowed
        while True:
            new = reach
            m = reach
            while m:
                low = m & -m
                i = low.bit_length() - 1
                new |= self.nb[i] & allowed
                m ^= low
            if new == reach:
                return reach
            reach = new

    def red_wins(self, red):
        return bool(self.grow(self.top, red) & self.bottom)

    def blue_wins(self, blue):
        return bool(self.grow(self.left, blue) & self.right)

    def _wins_impl(self, red, blue, red_to_move):
        """True if the player to move can force a win."""
        empty = self.full & ~(red | blue)
        m = empty
        while m:
            low = m & -m
            m ^= low
            if red_to_move:
                r2 = red | low
                if self.red_wins(r2) or not self._wins(r2, blue, False):
                    return True
            else:
                b2 = blue | low
                if self.blue_wins(b2) or not self._wins(red, b2, True):
                    return True
        return False

    def winning_moves(self, red, blue, red_to_move):
        out = []
        empty = self.full & ~(red | blue)
        for i in range(self.N):
            low = 1 << i
            if not empty & low:
                continue
            if red_to_move:
                r2 = red | low
                if self.red_wins(r2) or not self._wins(r2, blue, False):
                    out.append(divmod(i, self.n))
            else:
                b2 = blue | low
                if self.blue_wins(b2) or not self._wins(red, b2, True):
                    out.append(divmod(i, self.n))
        return out

    def mask(self, cells):
        m = 0
        for r, c in cells:
            m |= 1 << self.idx(r, c)
        return m


def show(n, red, blue, marks=()):
    for r in range(n):
        row = []
        for c in range(n):
            if (r, c) in red:
                row.append('R')
            elif (r, c) in blue:
                row.append('B')
            elif (r, c) in marks:
                row.append('*')
            else:
                row.append('.')
        print(' ' * r + ' '.join(row))
