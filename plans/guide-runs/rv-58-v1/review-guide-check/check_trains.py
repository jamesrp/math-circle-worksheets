"""Independent reviewer check: trains (all bands), K-1 P3/P5 counts, 2-3 P4 / 4-5 P2 bound.
Trains were read from the rendered student PDFs (pages viewed as images) and cross-checked
against the lists in the page generator. Every check is exhaustive: every set of gaps and
every assignment of pieces to two trays."""
from itertools import combinations, product
from math import comb

def shares(train, gaps):
    """Return True if cutting at gaps (positions 1..n-1, gap g is after card g) allows
    an assignment of pieces to two trays with equal reds and equal blues."""
    cuts = [0] + list(gaps) + [len(train)]
    pieces = [train[cuts[i]:cuts[i+1]] for i in range(len(cuts)-1)]
    R = train.count('R'); B = train.count('B')
    if R % 2 or B % 2:
        return False
    for assign in product([0, 1], repeat=len(pieces)):
        if assign[0] == 1:
            continue  # fix first piece in tray 0 (tray swap symmetry)
        r = sum(p.count('R') for p, a in zip(pieces, assign) if a == 0)
        b = sum(p.count('B') for p, a in zip(pieces, assign) if a == 0)
        if r == R // 2 and b == B // 2:
            return True
    return False

def min_cuts(train, kmax=4):
    R = train.count('R'); B = train.count('B')
    if R % 2 or B % 2:
        return None, []
    n = len(train)
    for k in range(0, kmax + 1):
        sols = [g for g in combinations(range(1, n), k) if shares(train, g)]
        if k == 0:
            # zero cuts only if empty halves: never for nonempty with something to share
            sols = [g for g in sols if (R + B) == 0]
        if sols:
            return k, sols
    return '>' + str(kmax), []

def split_str(train, gaps):
    out = ''
    for i, c in enumerate(train):
        if i in gaps:
            out += '|'
        out += c
    return out

pages = {
    'K-1 P1': ["RBRB", "RRBB", "BRRB", "BBRR", "RBBR", "BRBR"],
    'K-1 P2': ["RRRRBB", "BRRBRR", "RBRBR", "RRBBBBRR", "RRRRBBBB", "RRRBBBBRRR", "RRRRRRBBBB"],
    '2-3 P2': ["RRRRBB", "RBBRRR", "BRRBRRBB", "RRRBBBBR", "RBRRBRB", "RRBRRRBBBR", "RBBRRRRBBR"],
    '4-5 P1': ["RRRBBBBR", "BRRBRBBR", "RRRRBBBB", "RBRRRRBRBB", "BBRRRRRRBB", "RRRRRRBB"],
}
# The guide's printed splits (guide pp. 3, 5, 6), in row order.
guide = {
    'K-1 P1': ["RB|RB", "R|RB|B", "BR|RB", "B|BR|R", "RB|BR", "BR|BR"],
    'K-1 P2': ["RR|RRB|B", "BRR|BRR", None, "RRBB|BBRR", "RR|RRBB|BB", "RRRBB|BBRRR", "RRR|RRRBB|BB"],
    '2-3 P2': ["RR|RRB|B", "RB|BRR|R", "BRRB|RRBB", "R|RRBB|BBR", None, "RR|BRRRB|BBR", "RBBRR|RRBBR"],
    '4-5 P1': ["R|RRBB|BBR", "BRRB|RBBR", "RR|RRBB|BB", "RBRR|RRBRB|B", "BBRRR|RRRBB", "RRR|RRRB|B"],
}
bad = 0
for key, trains in pages.items():
    print('==', key)
    for i, t in enumerate(trains):
        k, sols = min_cuts(t)
        g = guide[key][i]
        if k is None:
            status = 'impossible'
            ok = g is None
        else:
            status = f'{k} cut(s); minimal gap sets: ' + ', '.join(split_str(t, s) for s in sols)
            if g is None:
                ok = False
            else:
                gaps = tuple(j for j in range(1, len(t)) if g.replace('|', '')[:j] and g[:len(g)].count('|') >= 0)
                # recover gaps from guide string
                gaps = []
                pos = 0
                for ch in g:
                    if ch == '|':
                        gaps.append(pos)
                    else:
                        pos += 1
                ok = (g.replace('|', '') == t) and (len(gaps) == k) and shares(t, tuple(gaps))
        if not ok:
            bad += 1
        print(f'  row {i+1}: {t:<11} {status}   guide: {g}  -> {"OK" if ok else "MISMATCH"}')

# 2-3 P1: all orders of 2R2B
orders = sorted(set(''.join(p) for p in __import__('itertools').permutations('RRBB')))
print('== 2-3 P1 orders:', len(orders), [(o, min_cuts(o)[0]) for o in orders])

# K-1 P3 / 4-5 P1 general question: 4R4B orders
orders = [''.join('R' if i in s else 'B' for i in range(8)) for s in combinations(range(8), 4)]
one = [o for o in orders if min_cuts(o)[0] == 1]
two = [o for o in orders if min_cuts(o)[0] == 2]
crit = all((o[:4].count('R') == 2) == (o in one) for o in orders)
from collections import Counter
dist = Counter(o[:4].count('R') for o in two)
print('== 4R4B: total', len(orders), 'one-cut', len(one), 'two-cut', len(two),
      'criterion first-four-has-two-reds exact:', crit, 'first-half red counts of two-cut orders:', dict(sorted(dist.items())))

# K-1 P5: every nonempty train with at most 6 reds and at most 4 blues
cnt = Counter()
total = 0
for r in range(7):
    for b in range(5):
        if r + b == 0:
            continue
        n = r + b
        for s in combinations(range(n), r):
            t = ''.join('R' if i in s else 'B' for i in range(n))
            k, _ = min_cuts(t)
            cnt['impossible' if k is None else k] += 1
            total += 1
print('== K-1 P5: trains', total, dict(cnt))

# 2-3 P4 / 4-5 P2: even-even trains up to 14 cards, maximum fewest cuts
worst = 0
for n in range(2, 15, 2):
    for r in range(0, n + 1, 2):
        for s in combinations(range(n), r):
            t = ''.join('R' if i in s else 'B' for i in range(n))
            # fast test: one cut iff first half balanced; else window gives 2
            k, _ = min_cuts(t, kmax=3) if n <= 10 else (None, None)
            if n <= 10:
                worst = max(worst, k)
print('== even-even trains up to 10 cards (full brute force): max fewest cuts =', worst)
# up to 14 cards by the half-window test (one cut iff first half balanced; else a balanced window exists)
def balanced_window(t):
    n = len(t); h = n // 2; R = t.count('R')
    return any(t[i:i+h].count('R') == R // 2 for i in range(0, h + 1))
ok = True
for n in range(2, 15, 2):
    for r in range(0, n + 1, 2):
        for s in combinations(range(n), r):
            t = ''.join('R' if i in s else 'B' for i in range(n))
            ok &= balanced_window(t)
print('== even-even trains up to 14 cards: a balanced half-window always exists:', ok)

# launch example not a task instance
alltask = set(sum(pages.values(), []))
print('== launch RBRBRR in task trains?', 'RBRBRR' in alltask, '; RBR|BRR valid:', shares('RBRBRR', (3,)))
print('MISMATCHES:', bad)
