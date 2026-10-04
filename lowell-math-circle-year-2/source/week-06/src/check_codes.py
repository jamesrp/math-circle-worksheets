from itertools import product
from functools import lru_cache

def score(t, s):
    return sum(a == b for a, b in zip(t, s))

for n in (2, 3, 4):
    codes = [''.join(p) for p in product('RY', repeat=n)]

    @lru_cache(None)
    def know(cands):
        # min worst-case tests needed to be sure of the secret
        if len(cands) <= 1:
            return 0
        best = 99
        for t in codes:
            parts = {}
            for s in cands:
                parts.setdefault(score(t, s), []).append(s)
            if len(parts) == 1:
                continue
            w = 1 + max(know(tuple(v)) for v in parts.values())
            best = min(best, w)
        return best

    @lru_cache(None)
    def hit(cands):
        # min worst-case tests until a test scores n
        best = 99
        for t in codes:
            parts = {}
            for s in cands:
                parts.setdefault(score(t, s), []).append(s)
            w = 0
            for sc, v in parts.items():
                if sc == n:
                    w = max(w, 1)
                else:
                    if len(v) == len(cands) and t not in cands:
                        w = 99; break
                    w = max(w, 1 + hit(tuple(v)))
            best = min(best, w)
        return best

    print(n, 'secrets', len(codes), 'know:', know(tuple(codes)), 'hit:', hit(tuple(codes)))
