#!/usr/bin/env python3
"""Week 66 (Lamplighter streets) independent math check.

Written for the math-check stage of the review; it does not import or run the
author's checkers. It
  * runs BFS on the lamplighter graph Z2 wr Z (states (p, lit set), moves L, R, F)
    with no coordinate bound, and on the printed finite street -4..4;
  * checks the guide's distance formula against BFS on every state within the radius;
  * checks the Cayley graph is bipartite (each move changes distance by exactly 1);
  * replays every word printed in the delivered guide PDF and checks its end
    state, length, walks+flips split and optimality;
  * checks the guide's lower-bound sentences;
  * checks the Problem 3 dead end and both readings of Problem 5;
  * lists all dead ends at small distance for context.
Run: python3 check_math.py  (finds the repository four folders up).
"""
import re
from collections import deque
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
GUIDE = REPO / 'lowell-math-circle-year-2/week-66/week-66-facilitator.pdf'

fails = 0
checks = 0


def ok(cond, msg):
    global fails, checks
    checks += 1
    if not cond:
        fails += 1
    print(('PASS ' if cond else 'FAIL ') + msg)


START = (0, frozenset())


def moves(s, lo=None, hi=None):
    p, L = s
    out = []
    if lo is None or p - 1 >= lo:
        out.append(('L', (p - 1, L)))
    if hi is None or p + 1 <= hi:
        out.append(('R', (p + 1, L)))
    out.append(('F', (p, L ^ {p})))
    return out


def bfs(radius, lo=None, hi=None):
    dist = {START: 0}
    q = deque([START])
    while q:
        s = q.popleft()
        if dist[s] == radius and lo is None:
            continue
        for _, t in moves(s, lo, hi):
            if t not in dist:
                dist[t] = dist[s] + 1
                q.append(t)
    return dist


def formula(p, S):
    l = min(S | {0})
    r = max(S | {0})
    return len(S) + min(-l + (r - l) + abs(p - r), r + (r - l) + abs(p - l))


def replay(word):
    s = START
    for c in word:
        s = dict(moves(s))[c]
    return s


R = 14
D = bfs(R)
inner = {s: d for s, d in D.items() if d <= R - 1}
ok(all(formula(p, S) == d for (p, S), d in D.items()),
   f'guide formula equals BFS distance on all {len(D)} states within distance {R} (unbounded street)')
n12 = sum(1 for d in D.values() if d <= 12)
print(f'INFO states within distance 12: {n12} (source MATHEMATICS.md says 4,167)')
ok(n12 == 4167, 'MATHEMATICS.md count 4,167 states at distance <= 12')
bip = all(abs(D[t] - d) == 1 for s, d in inner.items() for _, t in moves(s))
ok(bip, 'every move changes distance by exactly +-1 (graph is bipartite): "harder"/"easier" is a dichotomy')

# finite street -4..4
DF = bfs(10**6, -4, 4)
ok(len(DF) == 9 * 512, f'finite street has {len(DF)} reachable states (9 * 2^9 = 4608)')
ok(all(formula(p, S) == d for (p, S), d in DF.items()),
   'formula also equals BFS distance on every state of the finite -4..4 street')

T = lambda p, *S: (p, frozenset(S))
targets = {
    'P1A': (T(1, 1), 2), 'P1B': (T(1, -1, 1), 5), 'P1C': (T(0, 0, 2), 6),
    'P2A': (T(-2, -2, 0, 2), 9), 'P2B': (T(0, -2, 0, 2), 11), 'P2C': (T(2, -2, 0, 2), 9),
    'P3': (T(0, -1, 0, 1), 7),
    'P4L': (T(-1, -1, 0, 1), 6), 'P4R': (T(1, -1, 0, 1), 6), 'P4F': (T(0, -1, 1), 6),
}
for k, (s, d) in targets.items():
    ok(D[s] == d and DF[s] == d, f'{k} target {s[0]},{sorted(s[1])}: distance {D[s]} (guide {d}); finite street {DF[s]}')

# P4 targets are exactly the three neighbours of P3
p3 = targets['P3'][0]
nb = {c: t for c, t in moves(p3)}
ok(nb['L'] == targets['P4L'][0] and nb['R'] == targets['P4R'][0] and nb['F'] == targets['P4F'][0],
   'P4 table states are exactly L, R, F applied to the P3 target')
ok(all(D[t] == D[p3] - 1 for t in nb.values()), 'P3 target is a dead end: all three neighbours are at distance 6')

# every move along every optimal route stays inside [-2,2]; minimum walks per target
for k, (s, d) in targets.items():
    p, S = s
    l, r = min(S | {0, p}), max(S | {0, p})
    ok(-4 <= l and r <= 4, f'{k}: optimal route stays inside [{l},{r}] within the printed street')

# --- replay the words printed in the delivered guide ---
import pymupdf as fitz
gtext = '\n'.join(pg.get_text() for pg in fitz.open(GUIDE))
words = re.findall(r'\b[LRF]{2,}\b', gtext)
print('INFO words found in guide:', words)
expected_words = {
    'RF': 'P1A', 'LFRRF': 'P1B', 'FRRFLL': 'P1C',
    'FRRFLLLLF': 'P2A', 'FLLFRRRRFLL': 'P2B', 'FLLFRRRRF': 'P2C',
    'FLFRRFL': 'P3', 'FRFLLF': 'P4L', 'FLFRRF': 'P4R', 'LFRRFL': 'P4F'}
for w in words:
    if w not in expected_words:
        continue
    k = expected_words[w]
    s, d = targets[k]
    end = replay(w)
    ok(end == s and len(w) == D[s], f'guide word {w} reaches {k} in {len(w)} = fewest moves')
ok(set(expected_words) <= set(words), 'every expected guide word is present in the delivered guide text')
# walks + flips splits printed in the tables
splits = {'P1A': (1, 1), 'P1B': (3, 2), 'P1C': (4, 2), 'P4L': (3, 3), 'P4R': (3, 3), 'P4F': (4, 2)}
for w, k in expected_words.items():
    if k in splits:
        ok((len(w) - w.count('F'), w.count('F')) == splits[k], f'{k} walks+flips {splits[k]} matches word {w}')
for pat in ['1 + 1', '3 + 2', '4 + 2', '3 + 3']:
    ok(pat in gtext.replace(' ', ' ') or pat.replace(' ', '') in gtext.replace(' ', ''), f'guide table shows "{pat}"')


def min_walks(p, S):
    return formula(p, S) - len(S)


ok(min_walks(1, frozenset({-1, 1})) == 3, 'P1B: "visiting -1 then ending at 1 needs at least three walks"')
ok(min_walks(0, frozenset({0, 2})) == 4, 'P1C: "reaching 2 and returning needs at least four"')
ok(min_walks(-2, frozenset({-2, 0, 2})) == 6 and min_walks(2, frozenset({-2, 0, 2})) == 6,
   'P2: "to end at an extreme requires at least six walks"')
ok(min_walks(0, frozenset({-2, 0, 2})) == 8, 'P2: "returning to 0 requires eight"')
ok(min_walks(0, frozenset({-1, 0, 1})) == 4, 'P3: "visiting both -1 and 1 and returning to 0 forces four walks"')
ok(len('FLFRRFL') + 1 == 8 and D[replay('FLFRRFLL')] == 6,
   'P4 guide: appending a letter to the 7-move word gives an 8-letter word for a distance-6 target')

# --- Problem 5: two readings ---
# Reading A (intended): from every target, does SOME move increase distance?  No: P3 is a dead end.
# Reading B: does EVERY (or the chosen) next move always increase distance?  Trivially no.
deads = sorted((d, s[0], sorted(s[1])) for s, d in inner.items()
               if all(D[t] < d for _, t in moves(s)) and s != START)
print('INFO dead ends (no move increases distance) with distance <= 9:',
      [x for x in deads if x[0] <= 9])
ok(deads[0][0] == 7 and deads[0][1:] == (0, [-1, 0, 1]),
   'smallest-distance dead end is exactly the P3 target (distance 7); unique at that distance: '
   + str(sum(1 for x in deads if x[0] == 7) == 1))
a = targets['P1A'][0]
ok(D[dict(moves(a))['F']] == 1 and D[dict(moves(a))['L']] == 3,
   'Reading B is settled by P1 target A alone: F gives distance 1 (easier), L gives 3 (harder)')
nondecreasing_everywhere = all(any(D[t] > d for _, t in moves(s)) for s, d in inner.items() if d <= 6)
ok(nondecreasing_everywhere,
   'every state at distance <= 6 has at least one move that makes it harder (so no smaller counterexample to Reading A)')

print(f'\n{checks} checks, {fails} failures')
