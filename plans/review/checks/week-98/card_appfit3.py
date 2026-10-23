"""4x4: inclusion-minimal filling starts of every size 9-16 (completes the 4x4 search)."""
from itertools import combinations
a = b = 4
n = a * b
nb = [[(r+dr)*b + c+dc for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)) if 0 <= r+dr < a and 0 <= c+dc < b]
      for r, c in (divmod(i, b) for i in range(n))]
full = (1 << n) - 1
def clo(x):
    while True:
        y = x
        for i in range(n):
            if not (x >> i) & 1 and sum((x >> j) & 1 for j in nb[i]) >= 2:
                x |= 1 << i
        if x == y:
            return x
for s in range(9, n + 1):
    cnt = 0
    for S in combinations(range(n), s):
        x = sum(1 << i for i in S)
        if clo(x) == full and all(clo(x & ~(1 << i)) != full for i in S):
            cnt += 1
    print(f"4x4 size {s}: {cnt} inclusion-minimal filling starts")
