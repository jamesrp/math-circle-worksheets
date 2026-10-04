from itertools import product
def score(t, s): return sum(a == b for a, b in zip(t, s))
def fits(records):
    n = len(records[0][0])
    return [''.join(p) for p in product('RY', repeat=n)
            if all(score(t, ''.join(p)) == sc for t, sc in records)]

puzzles = {
 'K1-a': [('RR',2)],
 'K1-b': [('RY',0)],
 'K1-c': [('RR',1)],
 'K1-d': [('RR',1),('YR',0)],
 'K1-e': [('YY',1),('RY',2)],
 '23-a': [('RRR',2)],
 '23-b': [('RRR',2),('YRR',1)],
 '23-c': [('RRR',1),('RYY',2),('YRY',0)],
 '23-d': [('YYY',2),('YRY',1),('YYR',3)],
 '23-e': [('RYR',0),('YYY',2)],
 '23-f': [('RRR',3),('RYR',1)],
 '45-a': [('RRR',1),('YRR',2),('RYR',0)],
 '45-b': [('RRR',2),('RYY',2)],
 '45-c': [('RRRR',2),('YRRR',1),('RYRR',3)],
 '45-d': [('RRRR',2),('YYRR',2),('YRYR',2)],
 '45-e': [('RYRY',1),('RRYY',3),('YYYY',2)],
 '45-f': [('RRRR',1),('YRRR',2),('RYRR',0),('RRYR',0)],
}
for k, rec in puzzles.items():
    print(k, rec, '->', fits(rec))

print('--- more candidates')
more = {
 '23-c2': [('RRR',1),('YRR',2),('RYR',2)],
 '23-d2': [('RYY',2),('RRY',1),('YYY',2)],
 '23-d3': [('RYR',1),('YYR',2)],
 '23-d4': [('RYR',1),('YYR',2),('RRY',0)],
 '23-d5': [('YRY',1),('RRY',2),('YYR',2)],
 '23-d6': [('RYY',1),('YYR',1),('RRR',2)],
 '45-a2': [('RYR',1),('YYR',0),('RRY',2)],
 '45-a3': [('YRR',2),('RRY',2),('RYY',1)],
 '45-c2': [('RRYY',2),('RYRY',2),('RYYR',2)],
 '45-c3': [('RRYY',2),('RYRY',2),('RYYR',4)],
 '45-g': [('RRYY',3),('YRYR',1),('RRRY',2)],
 '45-h': [('RRYY',0),('RYRY',2)],
 '45-i': [('YYRR',1),('RYRY',3),('RRRR',2)],
}
for k, rec in more.items():
    print(k, rec, '->', fits(rec))
