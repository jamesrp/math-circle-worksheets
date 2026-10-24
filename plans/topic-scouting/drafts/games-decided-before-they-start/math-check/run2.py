import time, random
from planar import *
g = G('sprigs'); r, l = g.start(6); memo = {}
t=time.time(); print('sprigs 6', sorted(lengths(g, r, l, memo)), len(memo), round(time.time()-t,1), flush=True)
rng = random.Random(12345)
for n in (6, 7, 10):
    s = {randgame(G('sprigs'), n, rng)[0] for _ in range(300)}
    print('sprigs random', n, sorted(s), flush=True)
for n in (1, 2, 3):
    g = G('sprouts'); r, l = g.start(n)
    print('sprouts first player wins', n, win(g, r, l, {}), flush=True)
s = {}
for _ in range(400):
    m, left = randgame(G('brussels'), 3, rng); s[m] = s.get(m, 0) + 1
print('brussels 3 random lengths', s, flush=True)
s = {}
for _ in range(1000):
    m, left = randgame(G('brussels'), 2, rng); s[m] = s.get(m, 0) + 1
print('brussels 2 random lengths', s, flush=True)
for n in (3, 4, 10):
    s = {}
    for _ in range(300 if n < 10 else 60):
        m, left = randgame(G('sprouts'), n, rng); s[m] = s.get(m, 0) + 1
    print('sprouts random', n, sorted(s.items()), flush=True)
