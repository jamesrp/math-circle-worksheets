#!/usr/bin/env python3
"""Check every claim changed by the October 23, 2026 card shoulds and coulds.

    python3 review/verify_card_fixes_2026_10_23.py [build-folder]

The build folder (default build/) holds k-1.pdf, grades-2-3.pdf, grades-4-5.pdf and
facilitator-guide.pdf from build.sh. Needs PyMuPDF.
"""
import itertools
import json
import random
import sys
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parent.parent
build = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'build'
DATA = json.loads((ROOT / 'src' / 'math_checks.json').read_text())
GUIDE_DATA = json.loads((ROOT / 'facilitator-src' / 'math-checks.json').read_text())
checks = 0


def ok(cond, what):
    global checks
    assert cond, what
    checks += 1


def pages(name):
    return [' '.join(p.get_text().replace('–', '-').split()) for p in pymupdf.open(build / name)]


def blockers(L, R, m):
    inv = {v: k for k, v in m.items()}
    return [(a, x) for a in L for x in R if m[a] != x and L[a].index(x) < L[a].index(m[a]) and R[x].index(a) < R[x].index(inv[x])]


def stable(L, R):
    return [dict(zip(L, p)) for p in itertools.permutations(R) if not blockers(L, R, dict(zip(L, p)))]


def run(L, R, choose=lambda free: free[0]):
    """Deferred acceptance with L asking; choose picks the next free asker. Returns pairing and requests."""
    held, nxt, requests = {}, {p: 0 for p in L}, []
    while True:
        free = [p for p in L if p not in held.values()]
        if not free:
            return {p: r for r, p in held.items()}, requests
        p = choose(free)
        r = L[p][nxt[p]]
        nxt[p] += 1
        requests.append((p, r, nxt[p]))
        old = held.get(r)
        if old is None or R[r].index(p) < R[r].index(old):
            held[r] = p


# ---------------------------------------------------------------- student pages
k, m, h = pages('k-1.pdf'), pages('grades-2-3.pdf'), pages('grades-4-5.pdf')
for band, tag, n in ((k, 'K-v3', 7), (m, '23-v4', 6), (h, '45-v3', 6)):
    ok(len(band) == n and all(f'Bellingham Math Circle / Week 27 / W27-{tag}' in t for t in band), tag + ' footers')

# Second run's should 4: Grades 2-3 Problem 1 asks for a blocking pair, not two letters who want to change.
ok('On each other pairing, join a circle and a square that would both rather be together.' in m[1], '2-3 P1 wording')
ok('both want to change' not in ' '.join(m), 'old wording gone')
L, R = DATA['k_unique_shared']['left'], DATA['k_unique_shared']['right']
ok(blockers(L, R, {'A': 'Y', 'B': 'X'}) == [('A', 'X')] and not blockers(L, R, {'A': 'X', 'B': 'Y'}), 'top case: only AX / BY stays; A and X block the other')
L, R = DATA['k_two_stable']['left'], DATA['k_two_stable']['right']
ok(len(stable(L, R)) == 2, 'bottom case: both stay')
for pairing in ({'A': 'X', 'B': 'Y'}, {'A': 'Y', 'B': 'X'}):
    inv = {v: k for k, v in pairing.items()}
    circles = [a for a in L if L[a][0] != pairing[a]]
    squares = [x for x in R if R[x][0] != inv[x]]
    ok(len(circles) == 2 or len(squares) == 2, 'two letters on one side want to change, yet the pairing stays')

# Should 5: six boards for Grades 2-3 Problem 4, which has four stable pairings among 24.
L, R = DATA['middle_four']['left'], DATA['middle_four']['right']
ok(len(stable(L, R)) == 4 and len(list(itertools.permutations(R))) == 24, 'four stable of 24')
ok(pymupdf.open(build / 'grades-2-3.pdf')[4].get_text().split('\n').count('W') == 4 + 1 + 6, 'six boards on 2-3 p. 5 (W in four strips, one square token, six boards)')
ok(not any(all(L[a][0] == p[a] for a in L) and all(R[x][0] == {v: k for k, v in p.items()}[x] for x in R) for p in (dict(zip(L, q)) for q in itertools.permutations(R))), 'no pairing gives all eight first choices')

# Could 9: record boxes labelled by asking side.
ok('A, B, C, D asking' in h[1] and 'W, X, Y, Z asking' in h[1], '4-5 P2 record labels')
L, R = DATA['older_four']['left'], DATA['older_four']['right']
left_pairing, left_req = run(L, R)
right_pairing, right_req = run(R, L)
ok(left_pairing == {'A': 'W', 'B': 'Y', 'C': 'Z', 'D': 'X'} and len(left_req) == 8, 'circles asking: AW / BY / CZ / DX in 8')
ok({v: k for k, v in right_pairing.items()} == {'A': 'Z', 'B': 'Y', 'C': 'W', 'D': 'X'} and len(right_req) == 7, 'squares asking: AZ / BY / CW / DX in 7')

# ---------------------------------------------------------------- the guide
g = pages('facilitator-guide.pdf')
G = ' '.join(g)
ok(len(g) == 19, 'overview, 17 guide pages and the route note')
ok('Start in P1; ask each piece in turn, as in the P1 held hint' in g[0] and 'Start in P1; ask each piece in turn, as in the P1 held hint.' in g[1], 'should 7: overview and p. 1')
ok('Participation requires' not in G and 'only after the child can check' not in G and 'logical gate' not in G, 'gate wording gone')
ok('Keys packets W27-K-v3, W27-23-v4 and W27-45-v3.' in g[1], 'guide names the current packets')
ok("a case's four strips serve both of its pairings" in g[2], 'could 8: launch')
ok('Two voices for one check.' in g[2] and 'The pair blocks only when both say yes.' in g[2], 'should 6')
ok('ask "Is there another way?" before confirming it' in g[5], 'should 5: K-1 P6')
two = [bits for bits in itertools.product([0, 1], repeat=4)
       if len(stable({p: list('XY')[::(-1 if b else 1)] for p, b in zip('AB', bits[:2])},
                     {p: list('AB')[::(-1 if b else 1)] for p, b in zip('XY', bits[2:])})) == 2]
ok(len(two) == 2, 'K-1 P6 has exactly two answers, so "another way" is worth asking once')
ok('Each row shows one blocker; a child may find another.' in g[6] and 'the checker records all blockers' not in G, 'should 3')
cands = {r['matching']: r['blockers'] for r in GUIDE_DATA['unique3']['candidates']}
multi = [c for c, b in cands.items() if len(b) > 1]
ok(len(multi) >= 2, 'some rejected candidates have more than one blocker')
ok('The six blank boards are workspace, not a count of answers.' in g[8], 'should 5: 2-3 P4 note')
ok("This instance-specific count" not in G, 'could 11: p. 11 hedge cut')

# Should 4: 16 is a sufficient bound; the sharp bound is n(n-1) + 1, reached for n = 4.
ok('A sufficient answer: 16 requests; 100 with ten per side' in g[13] and 'Exact expected answer' not in G, 'retitled')
ok('at most 4 x 3 + 1 = 13 requests, and 10 x 9 + 1 = 91 with ten' in g[13], 'sharper count in the guide')
ok(4 * 3 + 1 == 13 and 10 * 9 + 1 == 91, 'arithmetic')
perms3, rperms3 = list(itertools.permutations('XYZ')), list(itertools.permutations('ABC'))
most = 0
for ls in itertools.product(perms3, repeat=3):
    L3 = {a: list(v) for a, v in zip('ABC', ls)}
    for rs in itertools.product(rperms3, repeat=3):
        R3 = {x: list(v) for x, v in zip('XYZ', rs)}
        _, req = run(L3, R3)
        last = [i for i, (p, r, rank) in enumerate(req) if rank == 3]
        ok(last in ([], [len(req) - 1]), 'only the final request can be a last choice (three pairs)')
        most = max(most, len(req))
ok(most == 3 * 2 + 1, 'three pairs: the most requests is 7 = 3 x 2 + 1 (all 46,656 profiles)')
L13 = {'A': list('XWYZ'), 'B': list('XYWZ'), 'C': list('WYXZ'), 'D': list('YWXZ')}
R13 = {'W': list('BDAC'), 'X': list('DCAB'), 'Y': list('ADCB'), 'Z': list('BDCA')}
ok('A: XWYZ; B: XYWZ; C: WYXZ; D: YWXZ; W: BDAC; X: DCAB; Y: ADCB; Z: BDCA' in g[13], 'the 13-request example is printed')
rng = random.Random(27)
outcomes = set()
for trial in range(500):
    pairing, req = run(L13, R13, choose=lambda free: rng.choice(free))
    ok(len(req) == 13 and not blockers(L13, R13, pairing), '13 requests in every asking order tried, ending stable')
    outcomes.add(tuple(sorted(pairing.items())))
ok(len(outcomes) == 1, 'the same final pairing for every order tried')
for trial in range(3000):
    L4 = {a: rng.sample('WXYZ', 4) for a in 'ABCD'}
    R4 = {x: rng.sample('ABCD', 4) for x in 'WXYZ'}
    _, req = run(L4, R4, choose=lambda free: rng.choice(free))
    ok(len(req) <= 13 and [i for i, (p, r, rank) in enumerate(req) if rank == 4] in ([], [len(req) - 1]), 'four pairs: at most 13, last choice only at the end')

# Could 10: Problem 1's bottom lists, run from either side.
ok("run the rules on Problem 1's bottom lists" in g[14] and 'either side asking gives AY / BZ / CX' in g[14], 'could 10 in the guide')
L, R = DATA['middle_unique']['left'], DATA['middle_unique']['right']
a, _ = run(L, R)
b, _ = run(R, L)
ok(a == {'A': 'Y', 'B': 'Z', 'C': 'X'} and {v: k for k, v in b.items()} == a and stable(L, R) == [a], 'AY / BZ / CX from either side, the only stable pairing')

# Could 11: residue.
ok('library label' not in G and 'Fidelity' not in G and 'Checks packaged' not in G, 'residue cut')
ok('Sources and local evidence' in g[17], 'p. 17 heading')

print(f'PASS: {checks} checks of the October 23 card fixes')
