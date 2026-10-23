"""Largest inclusion-minimal filling starts on 4x4 and 5x5 (bitmask search)."""
from itertools import combinations
from math import comb

def make(a, b):
    n = a * b
    nb = []
    for i in range(n):
        r, c = divmod(i, b)
        m = []
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            rr, cc = r + dr, c + dc
            if 0 <= rr < a and 0 <= cc < b:
                m.append(rr * b + cc)
        nb.append(m)
    full = (1 << n) - 1
    def clo(x):
        while True:
            y = x
            for i in range(n):
                if not (x >> i) & 1:
                    k = 0
                    for j in nb[i]:
                        if (x >> j) & 1:
                            k += 1
                    if k >= 2:
                        x |= 1 << i
            if x == y:
                return x
    return n, full, clo

for a, b, sizes in ((4, 4, range(6, 9)), (5, 5, range(7, 9))):
    n, full, clo = make(a, b)
    for s in sizes:
        cnt = 0
        for S in combinations(range(n), s):
            x = 0
            for i in S:
                x |= 1 << i
            if clo(x) != full:
                continue
            if all(clo(x & ~(1 << i)) != full for i in S):
                cnt += 1
        print(f"{a}x{b} size {s}: {cnt} inclusion-minimal filling starts (of {comb(n, s)})", flush=True)
