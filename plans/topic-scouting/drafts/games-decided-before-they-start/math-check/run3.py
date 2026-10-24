import random
from planar import *

def region_lives(R, lives):
    vs = set(x for b in R for x in b)
    return sum(lives[x] for x in vs if lives[x] > 0)

def long_game(n, seed=0):
    g = G('sprouts'); r, l = g.start(n); m = 0
    rng = random.Random(seed)
    while True:
        ms = g.moves(r, l)
        if not ms: return m, sum(v for v in l.values() if v > 0)
        good = [(r2, l2) for r2, l2 in ms
                if max(region_lives(R, l2) for R in r2) == sum(v for v in l2.values() if v > 0)]
        r, l = rng.choice(good if good else ms); m += 1

for n in (2, 3, 4, 10):
    print('sprouts cooperative long game', n, long_game(n), '3n-1 =', 3*n-1, flush=True)

# misreading: a loop is allowed at a dot with only one token (it takes the last token)
class G1(G):
    def moves(self, regions, lives):
        out = super().moves(regions, lives)
        # add loops at 1-life vertices
        extra = []
        for ri, R in enumerate(regions):
            rest_regions = regions[:ri] + regions[ri+1:]
            for bi, b in enumerate(R):
                for pi in range(len(b)):
                    u = b[pi]
                    if lives[u] == 1:
                        nl = dict(lives); nl[u] = 0
                        others = [R[k] for k in range(len(R)) if k != bi]
                        bb = rot(b, pi)
                        s1 = (u,); s2 = bb + (u,)
                        for mask in range(1 << len(others)):
                            g1 = tuple(others[k] for k in range(len(others)) if mask >> k & 1)
                            g2 = tuple(others[k] for k in range(len(others)) if not mask >> k & 1)
                            extra.append((rest_regions + (g1 + (s1,), g2 + (s2,)), nl))
        return out + extra
for n in range(1, 6):
    g = G1('sprigs'); r, l = g.start(n)
    print('sprigs with 1-token loops allowed', n, sorted(lengths(g, r, l, {})))
