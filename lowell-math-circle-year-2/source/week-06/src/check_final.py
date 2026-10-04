from itertools import product, combinations
def score(t, s): return sum(a == b for a, b in zip(t, s))
def fits(rec):
    n = len(rec[0][0])
    return [''.join(p) for p in product('RY', repeat=n)
            if all(score(t, ''.join(p)) == sc for t, sc in rec)]
P = {
 'K1 P7a': [('RR',2)], 'K1 P7b': [('RY',0)], 'K1 P7c': [('RR',1)],
 'K1 P7d': [('RR',1),('YR',0)], 'K1 P7e': [('RY',1),('RR',0)],
 '23 P7a': [('RRR',2)], '23 P7b': [('RYR',1),('YYR',2)],
 '23 P7c': [('RYY',2),('YRY',2),('RRR',2)],
 '23 P7d': [('RRY',2),('RYR',2),('YRR',2)], '23 P7e': [('RRR',3),('RYR',1)],
 '45 P3a': [('RRY',2),('RYR',2),('YRR',2)], '45 P3b': [('RRR',2),('RYY',2)],
 '45 P3c': [('RRYY',3),('YRYR',1),('RRRY',2)],
 '45 P3d': [('RRYY',2),('RYRY',2),('RYYR',2)],
 '45 P3e': [('RYRY',1),('RRYY',3),('YYYY',2)],
}
for k, r in P.items(): print(k, r, '->', fits(r))
r = P['23 P7c']
print('23 P7c single rows:', [len(fits([x])) for x in r], 'pairs:', [len(fits(list(c))) for c in combinations(r,2)])
# swap symmetry check: turning over the counters in one place of both rows keeps the score
def flip(row, j): return ''.join(({'R':'Y','Y':'R'}[c] if i == j else c) for i, c in enumerate(row))
ok = all(score(t, s) == score(flip(t, j), flip(s, j))
         for n in (2, 3, 4)
         for t in map(''.join, product('RY', repeat=n))
         for s in map(''.join, product('RY', repeat=n))
         for j in range(n))
print('swap one place in both rows keeps score:', ok)
