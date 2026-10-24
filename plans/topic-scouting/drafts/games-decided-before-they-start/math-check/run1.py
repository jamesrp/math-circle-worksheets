import time, random
from planar import *
for n in range(1, 6):
    g = G('sprigs'); r, l = g.start(n); memo = {}
    t = time.time()
    L = lengths(g, r, l, memo)
    print('sprigs', n, sorted(L), len(memo), round(time.time()-t, 1), flush=True)
for n in range(1, 4):
    g = G('sprouts'); r, l = g.start(n); memo = {}
    t = time.time()
    L = lengths(g, r, l, memo)
    print('sprouts', n, sorted(L), len(memo), round(time.time()-t, 1), flush=True)
for n in range(1, 3):
    g = G('brussels'); r, l = g.start(n); memo = {}
    t = time.time()
    L = lengths(g, r, l, memo)
    print('brussels', n, sorted(L), len(memo), round(time.time()-t, 1), flush=True)
