# Card-stage spot checks: readout counts of mixed binary rings at n = 6, 7, 9;
# binary ring counts for app sizing; counters needed for K-1 P4 side by side.
from itertools import product
def rots(w): return {w[i:]+w[:i] for i in range(len(w))}
for n in (4, 6, 7, 9):
    counts = sorted({len(rots(''.join(w))) for w in product('AB', repeat=n) if len(set(w)) == 2})
    rings = len({min(rots(''.join(w))) for w in product('AB', repeat=n)})
    print(f'n={n}: mixed readout counts {counts}; binary rings {rings}')
print('ternary n=5 rings', len({min(rots(''.join(w))) for w in product('ABC', repeat=5)}))
