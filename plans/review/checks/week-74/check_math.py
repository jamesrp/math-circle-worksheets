"""Independent mathematical check of Week 74 (doubling elevators).

Model (student p. 1 shared rules): states (x, h), x any integer, h >= 0.
U: h+1.  D: h-1 (not below 0).  R/L: x +/- 2**h.  Every move costs 1.
Start (0, 0); every task ends on level 0.

Own breadth-first search and exhaustive word enumeration; no writer, guide
or source checker is imported.  Checks every student problem's intended
answer, the height bound in the guide overview, every move word, table and
case bound printed in the delivered facilitator PDF (read with pdftotext),
and alternative readings of Problems 2 and 4.
Run: python3 check_math.py   (writes check_math.out beside itself)
"""
import itertools
import re
import subprocess
from collections import deque
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
WEEK = REPO / 'lowell-math-circle-year-2' / 'week-74'
STUDENT = WEEK / 'week-74-students.pdf'
GUIDE = WEEK / 'week-74-facilitator.pdf'

OUT, FAIL = [], []


def say(*a):
    OUT.append(' '.join(str(x) for x in a))


def check(cond, msg):
    say(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAIL.append(msg)


def step(state, m):
    x, h = state
    if m == 'U':
        return (x, h + 1)
    if m == 'D':
        return (x, h - 1) if h > 0 else None
    if m == 'R':
        return (x + 2 ** h, h)
    if m == 'L':
        return (x - 2 ** h, h)
    raise ValueError(m)


def run(word, start=(0, 0)):
    s, path = start, [start]
    for m in word:
        s = step(s, m)
        if s is None:
            return None, path
        path.append(s)
    return s, path


def bfs(moves='UDRL', depth=13):
    dist = {(0, 0): 0}
    q = deque([(0, 0)])
    while q:
        s = q.popleft()
        if dist[s] == depth:
            continue
        for m in moves:
            t = step(s, m)
            if t is not None and t not in dist:
                dist[t] = dist[s] + 1
                q.append(t)
    return dist


def ground_words(n_max, moves='UDRL'):
    """All words of length <= n_max from (0,0) ending on level 0, with
    (word, final x, max height, max |x| visited)."""
    res = []

    def rec(word, x, h, H, X):
        if h == 0:
            res.append((word, x, H, X))
        if len(word) == n_max:
            return
        if h > n_max - len(word):      # cannot get home: prune
            return
        for m in moves:
            t = step((x, h), m)
            if t is None:
                continue
            rec(word + m, t[0], t[1], max(H, t[1]), max(X, abs(t[0])))
    rec('', 0, 0, 0, 0)
    return res


DIST = bfs('UDRL', 13)
NOLEFT = bfs('UDR', 13)


def gdist(n, table=DIST):
    return table.get((n, 0))


# ---------------------------------------------------------------- example
say('== Shared example (student p. 1): U R D from coordinate 1, level 0')
end, path = run('URD', (1, 0))
check(path == [(1, 0), (1, 1), (3, 1), (3, 0)],
      f'example path {path} = printed (1,0)->(1,1)->(3,1)->(3,0), 3 moves')
check(run('R', (1, 1))[0] == (3, 1) and run('R', (1, 2))[0] == (5, 2),
      'guide rehearsal: R from (1,1) -> (3,1); from (1,2) -> (5,2)')

# ---------------------------------------------------------------- P1
say('\n== Problem 1 (p. 1): shortest ground trips to 3 and 7')
W6 = ground_words(6)
for n, claim in [(3, 3), (7, 6)]:
    d = gdist(n)
    best = sorted(w for w, x, H, X in W6 if x == n and len(w) == d)
    check(d == claim, f'dist(0,0)->({n},0) = {d} (guide {claim}); '
          f'{len(best)} shortest word(s): {best}')
mx5 = max(abs(x) for w, x, H, X in ground_words(5))
mx2 = max(abs(x) for w, x, H, X in ground_words(2))
check(mx2 == 2, f'guide: two moves reach at most 2 -> brute force {mx2}')
check(mx5 == 6, f'guide: five moves reach at most 6 -> brute force {mx5}')
check([(5 - 2 * H) * 2 ** H for H in range(3)] == [5, 6, 4],
      'guide P1 height bounds H=0,1,2 for N=5 are 5,6,4')

# ---------------------------------------------------------------- P2 / P4
say('\n== Problems 2 and 4 (pp. 2-3): coordinate 16')
W8 = ground_words(8)
d16 = gdist(16)
best16 = sorted(w for w, x, H, X in W8 if x == 16 and len(w) == 8)
check(d16 == 8, f'dist to (16,0) = {d16}; {len(best16)} distinct 8-move '
      f'words reach (16,0), so "two different trips tied" is available')
say('     8-move words to 16:', ' '.join(best16))
W7 = ground_words(7)
mx7 = max(abs(x) for w, x, H, X in W7)
vis7 = max(X for w, x, H, X in W7)
check(mx7 == 12, f'P4: max |final x| over all ground trips <= 7 moves = {mx7} < 16')
check(vis7 == 12, f'P4 other reading ("touch 16 at any level, then return to '
      f'level 0 anywhere"): max |x| ever visited in <= 7-move ground trips = {vis7} < 16')
vis_any7 = max(abs(x) for (x, h), dd in DIST.items() if dd <= 7)
say(f'     (for contrast: |x| = {vis_any7} can be touched within 7 moves if the '
    f'trip need not come down; e.g. (16,3) is at distance {DIST[(16, 3)]})')
check([(7 - 2 * H) * 2 ** H for H in range(4)] == [7, 10, 12, 8],
      'guide P4 table (7-2H)2^H for H=0..3 = 7,10,12,8')

# ---------------------------------------------------------------- height bound
say('\n== Guide overview: ground trips with <= N moves and max height H '
    'have |x| <= (N-2H)2^H, attained')
for N in range(0, 11):
    WN = ground_words(N)
    for H in range(0, N // 2 + 1):
        got = max(abs(x) for w, x, HH, X in WN if HH == H)
        bound = (N - 2 * H) * 2 ** H
        if got != bound:
            check(False, f'N={N} H={H}: brute max {got} vs bound {bound}')
    far = max(x for w, x, H, X in WN)
    pred = max((N - 2 * H) * 2 ** H for H in range(N // 2 + 1))
    if far != pred:
        check(False, f'N={N}: farthest {far} vs max bound {pred}')
check(not FAIL, 'bound (N-2H)2^H is exact for every N<=10 and every H<=N/2 '
      '(exhaustive enumeration of all words incl. L and repeated climbs)')

# ---------------------------------------------------------------- P3
say('\n== Problem 3 (p. 3): farthest right on level 0 within budget N')
W = {N: ground_words(N) for N in range(4, 9)}
for N, claim in [(4, 4), (5, 6), (6, 8), (7, 12), (8, 16)]:
    far = max(x for w, x, H, X in W[N])
    wit = sorted(w for w, x, H, X in W[N] if x == far)
    check(far == claim, f'budget {N}: farthest {far} (guide {claim}); '
          f'{len(wit)} attaining words, shortest {min(wit, key=len)}')

# ---------------------------------------------------------------- P5
say('\n== Problem 5 (p. 4): 9, 15, 17, 23 with and without L')
for n, cl, cnl in [(9, 7, 7), (15, 9, 9), (17, 9, 9), (23, 10, 11)]:
    d, dn = gdist(n), gdist(n, NOLEFT)
    check(d == cl and dn == cnl,
          f'{n}: min {d} (guide {cl}), min with no L {dn} (guide {cnl})')

say('\n-- guide case bounds (exhaustive):')
W9 = ground_words(9)
cases = [
    ('15, budget 8, H=2, odd endpoint: 1+4+4+4=13', W8, 2, 13),
    ('15, budget 8, H=3, odd endpoint: 1+8=9', W8, 3, 9),
    ('23, budget 9, H=3, odd endpoint: 1+8+8=17', W9, 3, 17),
]
for label, WW, H, claim in cases:
    got = max(abs(x) for w, x, HH, X in WW if HH == H and x % 2)
    check(got == claim, f'{label} -> brute max odd |x| = {got}')
check([(8 - 2 * H) * 2 ** H for H in range(5)][:2] == [8, 12],
      'guide: budget 8 heights 0,1 allow 8 and 12')
check([(9 - 2 * H) * 2 ** H for H in range(5)] == [9, 14, 20, 24, 16],
      'guide: budget 9 height bounds 9,14,20,24,16')
check(max(abs(x) for w, x, H, X in W9 if x % 2) == 17
      and gdist(23) == 10, 'no 9-move ground trip ends at an odd |x| > 17')


def coins(n, H):
    """Fewest coins of values 1,2,...,2^H totalling n (DP)."""
    INF = 10 ** 9
    best = [0] + [INF] * n
    for v in range(1, n + 1):
        best[v] = min(best[v - 2 ** k] + 1 for k in range(H + 1) if 2 ** k <= v)
    return best[n]


def cH(n, H):
    return n // 2 ** H + bin(n % 2 ** H).count('1')


okc = all(coins(n, H) == cH(n, H) for n in range(0, 130) for H in range(0, 7))
check(okc, 'guide formula c_H(n) = floor(n/2^H) + ones(n mod 2^H) equals '
      'DP coin minimum for n<130, H<7')
# no-left minimum with level cap H equals min_{H'<=H} 2H' + c_H'(n)
okcap = True
for H in range(0, 6):
    capped = {}
    q = deque([(0, 0)])
    capped[(0, 0)] = 0
    while q:
        s = q.popleft()
        if capped[s] >= 14:
            continue
        for m in 'UDR':
            t = step(s, m)
            if t is None or t[1] > H or t[0] > 64 or t in capped:
                continue
            capped[t] = capped[s] + 1
            q.append(t)
    for n in range(1, 40):
        pred = min(2 * h + cH(n, h) for h in range(H + 1))
        got = capped.get((n, 0))
        if pred <= 14 and got != pred:
            okcap = False
            say(f'     mismatch n={n} cap={H}: bfs {got} formula {pred}')
check(okcap, 'no-left BFS with level cap H matches min over H\'<=H of '
      '2H\'+c_H\'(n) (n<40, H<=5, all values <= 14)')
check([2 * H + cH(23, H) for H in range(5)] == [23, 14, 11, 11, 12],
      'guide no-left bounds for 23 at H=0..4: 23,14,11,11,12')

# where does L strictly help?  (deeper search so every n <= 64 is reached)
D16, N16 = bfs('UDRL', 16), bfs('UDR', 16)
assert all((n, 0) in D16 and (n, 0) in N16 for n in range(1, 65))
strict = [n for n in range(1, 65) if D16[(n, 0)] < N16[(n, 0)]]
say(f'     destinations 1..64 where an L-trip strictly beats every no-L trip: {strict}')
check(strict[0] == 23, '23 is the smallest destination where L strictly helps')
check(23 in strict and not any(n in strict for n in (9, 15, 17)),
      'among 9, 15, 17, 23 only 23 shows a strict saving from L')

# ---------------------------------------------------------------- guide words
say('\n== Every move word printed in the delivered guide')
gtext = subprocess.run(['pdftotext', '-layout', str(GUIDE), '-'],
                       capture_output=True, text=True, check=True).stdout
words = sorted(set(re.findall(r'\b[UDRL]{3,}\b', gtext)))
expect_end = {
    'RRR': 3, 'URRRDR': 7, 'UURRRRDD': 16, 'UUURRDDD': 16, 'RRRR': 4,
    'URRRD': 6, 'UURRDD': 8, 'UURRRDD': 12, 'UURRDDR': 9,
    'UUURRDDDL': 15, 'UUURRDDDR': 17, 'UUURRRDDDL': 23,
    'UUURRDRDRDR': 23, 'UURRRDRDR': 15,
}
# URD is the launch example (from coordinate 1), checked above; not a trip from 0
words = [w for w in words if w != 'URD']
say('     words found in guide text:', ' '.join(words))
check(set(words) == set(expect_end), 'guide words = the expected set')
role = {  # word -> (kind, value)
    'RRR': ('opt', None), 'URRRDR': ('opt', None), 'UURRRRDD': ('opt', None),
    'UUURRDDD': ('opt', None), 'UURRDDR': ('opt', None),
    'UUURRDDDL': ('opt', None), 'UUURRDDDR': ('opt', None),
    'UUURRRDDDL': ('opt', None), 'UURRRDRDR': ('opt', None),
    'UUURRDRDRDR': ('noleft', None),
    'RRRR': ('budget', 4), 'URRRD': ('budget', 5), 'UURRDD': ('budget', 6),
    'UURRRDD': ('budget', 7),
}
for w in words:
    end, path = run(w)
    target = expect_end.get(w)
    legal = end is not None and end[1] == 0 and end[0] == target
    kind, val = role.get(w, ('opt', None))
    if kind == 'opt':
        good = len(w) == gdist(target)
        why = f'shortest possible ({gdist(target)})'
    elif kind == 'noleft':
        good = 'L' not in w and len(w) == gdist(target, NOLEFT)
        why = f'shortest without L ({gdist(target, NOLEFT)})'
    else:
        far = max(x for ww, x, H, X in ground_words(val))
        good = len(w) <= val and target == far
        why = f'budget-{val} witness, farthest = {far}'
    check(legal and good, f'{w}: ends at {end}, {len(w)} moves, {why}; path {path}')
check('USAGE' not in gtext, 'guide text read')

# ---------------------------------------------------------------- student text
say('\n== Student text numbers')
stext = subprocess.run(['pdftotext', '-layout', str(STUDENT), '-'],
                       capture_output=True, text=True, check=True).stdout
for frag in ['Reach coordinate 3 and return to level 0', 'Then try coordinate 7',
             'Reach coordinate 16 and return to level 0',
             'seven or fewer moves', 'to 9, 15, 17 and 23, ending on level 0',
             'Example: U R D costs 3 moves.']:
    check(frag in ' '.join(stext.split()), f'student text contains "{frag}"')
p3 = stext[stext.index('Problem 3:'):stext.index('Problem 4:')]
budgets = re.findall(r'^\s*([4-8])\s*$', p3, re.M)
check(budgets == ['4', '5', '6', '7', '8'], f'P3 budget rows {budgets}')

say('\nRESULT:', 'all checks pass' if not FAIL else f'{len(FAIL)} FAIL(s)')
(HERE / 'check_math.out').write_text('\n'.join(OUT) + '\n')
print('\n'.join(OUT))
