"""Independent math check for Week 96 (Prime bags), both student bands and the guide.

Reads the printed numbers from the student LaTeX sources and the current PDFs'
text, then recomputes everything from scratch: splitting routes, sub-bag
values, divisor counts, count patterns, least numbers, and every numeric claim
the adult guide makes. Does not import or trust the week's own check_math.py.

Finds the repository by walking up from this file until it sees
lowell-math-circle-year-2/ (four folders up from plans/review/checks/week-96/).
"""
import re
import subprocess
from collections import Counter
from functools import lru_cache
from itertools import product
from math import gcd, prod
from pathlib import Path

HERE = Path(__file__).resolve()
ROOT = next(p for p in HERE.parents if (p / 'lowell-math-circle-year-2').is_dir())
SRC = ROOT / 'lowell-math-circle-year-2' / 'source' / 'week-96'
PDF = ROOT / 'lowell-math-circle-year-2' / 'week-96'

fails = []


def check(cond, msg):
    print(('ok    ' if cond else 'FAIL  ') + msg)
    if not cond:
        fails.append(msg)


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def tau(n):
    return len(divisors(n))


def is_prime(n):
    return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))


def pdftext(name):
    return subprocess.run(['pdftotext', '-layout', str(PDF / name), '-'],
                          capture_output=True, text=True, check=True).stdout


# ---------------------------------------------------------------- printed data
tex23 = (SRC / 'student' / 'grades-2-3.tex').read_text()
tex45 = (SRC / 'student' / 'grades-4-5.tex').read_text()
guide = (SRC / 'guide' / 'facilitator.tex').read_text()


def split_problems(tex):
    body = tex.split(r'\begin{document}', 1)[1]
    parts = re.split(r'\\problem\{(\d+)\}', body)
    return {int(parts[i]): parts[i + 1] for i in range(1, len(parts), 2)}


P23, P45 = split_problems(tex23), split_problems(tex45)


def cards_in(chunk):
    # route cards are drawn as rounded-corner nodes at x=.5 beside a workbox
    return [int(v) for v in re.findall(r'at\(\.5,[\d.]+\)\{(\d+)\}', chunk)]


def bags_in(chunk):
    return [([int(t) for t in toks.split(',')], int(val))
            for toks, val in re.findall(r'\\bag\{([\d,]+)\}\\quad value (\d+)', chunk)]


print('== printed data')
cards23, cards45 = cards_in(P23[1]), cards_in(P45[1])
print('2-3 P1 cards', cards23, '| 4-5 P1 cards', cards45)
for band, P in (('2-3', P23), ('4-5', P45)):
    for k, chunk in sorted(P.items()):
        for toks, val in bags_in(chunk):
            check(prod(toks) == val and all(is_prime(t) for t in toks),
                  f'{band} P{k}: bag {toks} is all primes and its printed value {val} = product')
# the cards named in 4-5 P1's text match the drawn cards
check(re.search(r'routes for 36, 48 and 60', P45[1]) is not None and cards45 == [36, 48, 60],
      '4-5 P1 text names the drawn cards 36, 48, 60')
# the PDFs carry the same numbers as the sources
t23, t45 = pdftext('week-96-grades-2-3.pdf'), pdftext('week-96-grades-4-5.pdf')
for v in ('value 12', 'value 18', 'value 24', 'value 30'):
    check(v in t23, f'2-3 PDF shows "{v}"')
for v in ('value 24', 'value 30', 'value 36', 'value 60', 'value 72', 'seven 2 tokens and four 3 tokens',
          'exactly 6, 8, 9, 10 and 12 divisors'):
    check(v in t45, f'4-5 PDF shows "{v}"')

# ---------------------------------------------------------------- splitting routes
print('\n== splitting routes (all legal routes, every step splits one composite card into a*b, a,b>=2)')


def splits(n):
    return [(a, n // a) for a in range(2, int(n ** 0.5) + 1) if n % a == 0]


@lru_cache(None)
def finals(state):
    """All finished bags reachable from a sorted tuple of cards, and the number of routes."""
    comps = [i for i, c in enumerate(state) if not is_prime(c)]
    if not comps:
        return frozenset([state]), 1
    out, nroutes = set(), 0
    for i in set(comps):
        for a, b in splits(state[i]):
            nxt = tuple(sorted(state[:i] + state[i + 1:] + (a, b)))
            f, r = finals(nxt)
            out |= f
            nroutes += r
    return frozenset(out), nroutes


for n in sorted(set([20] + cards23 + cards45)):
    f, r = finals((n,))
    first = splits(n)
    check(len(f) == 1, f'{n}: every route ends in the same bag {sorted(next(iter(f)))}; '
                       f'{r} split sequences; {len(first)} distinct first splits {first}')
    check(len(first) >= 2, f'{n}: at least two genuinely different first splits exist')

# the guide's routes: each arrow splits exactly one card, product preserved, ends in primes
print('\n== guide routes')
# join the whole guide so routes broken across display lines are read whole
flat = re.sub(r'\s+', '', guide)
routes = re.findall(r'\d+(?:\\cdot\d+)*(?:\\to\d+(?:\\cdot\d+)*)+', flat)
check(len(routes) == 12, f'found all 12 guide routes ({len(routes)})')
seen = set()
for r in routes:
    r = re.sub(r'\s+', '', r).rstrip(',.')
    if r in seen or r.count('\\to') < 1:
        continue
    seen.add(r)
    states = [Counter(int(x) for x in s.split('\\cdot')) for s in r.split('\\to')]
    okay = True
    for a, b in zip(states, states[1:]):
        removed, added = a - b, b - a
        if not (sum(removed.values()) == 1 and sum(added.values()) == 2):
            okay = False
            break
        (c,), (x, y) = list(removed.elements()), list(added.elements())
        if not (x * y == c and x >= 2 and y >= 2):
            okay = False
    okay = okay and all(is_prime(t) for t in states[-1].elements())
    check(okay, f'guide route {r.replace(chr(92) + "to", " -> ").replace(chr(92) + "cdot", "*")}: one split per arrow, ends at primes')

# ---------------------------------------------------------------- sub-bag values
print('\n== sub-bag values (choose any subset of token positions)')


def subbag_values(toks):
    vals = set()
    for mask in product([0, 1], repeat=len(toks)):
        vals.add(prod(t for t, m in zip(toks, mask) if m))
    return sorted(vals)


claimed_lists = {12: [1, 2, 3, 4, 6, 12], 18: [1, 2, 3, 6, 9, 18], 24: [1, 2, 3, 4, 6, 8, 12, 24],
                 30: [1, 2, 3, 5, 6, 10, 15, 30], 36: [1, 2, 3, 4, 6, 9, 12, 18, 36],
                 60: [1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60],
                 72: [1, 2, 3, 4, 6, 8, 9, 12, 18, 24, 36, 72]}
for band, P in (('2-3', P23), ('4-5', P45)):
    for k, chunk in sorted(P.items()):
        for toks, val in bags_in(chunk):
            vals = subbag_values(toks)
            check(vals == divisors(val), f'{band} P{k} bag {toks}: values {vals} = divisors of {val} '
                                         f'({len(vals)} values from {2 ** len(toks)} labelled selections)')
            check(claimed_lists[val] == vals, f'guide list for {val} matches')
# the example on the shared-rules page
check(2 * 5 == 10 and 20 // 10 == 2 and 20 % 10 == 0, 'example: shaded 2,5 -> 10, unshaded 2 = 20/10')

# 2-3 P3: "Which can make more different values?"
v24, v30 = len(subbag_values([2, 2, 2, 3])), len(subbag_values([2, 3, 5]))
print(f'2-3 P3: 24 bag (4 tokens) makes {v24}; 30 bag (3 tokens) makes {v30}; '
      f'strictly more for one bag? {v24 != v30}')
check(v24 == v30 == 8, 'guide: both P3 bags make eight values (a tie)')
# guide counting claims for 4-5 P3
check(3 * 3 == len(subbag_values([2, 2, 3, 3])), 'guide 4-5 P3: 36 -> 3*3 = 9')
check(3 * 2 * 2 == len(subbag_values([2, 2, 3, 5])), 'guide 4-5 P3: 60 -> 3*2*2 = 12')
check(4 * 3 == len(subbag_values([2, 2, 2, 3, 3])), 'guide 4-5 P3: 72 -> 4*3 = 12')
# guide 2-3 P2 organization
check(2 * 3 == 6 and 2 * 3 == len(subbag_values([2, 3, 3])), 'guide 2-3 P2: 12 and 18 organized as 2 x 3 = 6')

# ---------------------------------------------------------------- 4-5 P4
print('\n== 4-5 P4')
n = 2 ** 7 * 3 ** 4
check(n == 10368, '2^7 * 3^4 = 10,368')
check(tau(n) == 40 == 8 * 5, 'tau(10368) = 40 = 8*5 by trial division')
check(tau(2 ** 5) == 6, 'guide check: five 2s give six divisors (not 5, not 32)')

# ---------------------------------------------------------------- patterns
print('\n== count patterns')


def mult_partitions(D, least=2):
    """Unordered factorizations of D into factors >= least (nonincreasing)."""
    if D == 1:
        return [[]]
    out = []
    for f in range(least, D + 1):
        if D % f == 0:
            for rest in mult_partitions(D // f, f):
                out.append([f] + rest)
    return out


def pattern_of(n):
    exps, p = [], 2
    while n > 1:
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        if e:
            exps.append(e)
        p += 1
    return tuple(sorted(exps, reverse=True))


guide_table = {4: {(1, 1): 6, (3,): 8}, 6: {(2, 1): 12, (5,): 32},
               8: {(1, 1, 1): 30, (3, 1): 24, (7,): 128}, 9: {(2, 2): 36, (8,): 256},
               10: {(4, 1): 48, (9,): 512},
               12: {(2, 1, 1): 60, (3, 2): 72, (5, 1): 96, (11,): 2048}}
LIMIT = 5000
least_by_pattern = {}
for m in range(2, LIMIT):
    pat = pattern_of(m)
    least_by_pattern.setdefault(pat, m)

for D, table in guide_table.items():
    algebraic = {tuple(sorted((f - 1 for f in fs), reverse=True)) for fs in mult_partitions(D)}
    # brute force with labels 2, 3, 5 only (4-5 P5, 2-3 P4)
    with235 = set()
    for a, b, c in product(range(D), repeat=3):
        if (a + 1) * (b + 1) * (c + 1) == D:
            with235.add(tuple(sorted([e for e in (a, b, c) if e], reverse=True)))
    # brute force with any primes, every integer below LIMIT
    anyp = {pattern_of(m) for m in range(2, LIMIT) if tau(m) == D} if D <= 12 else set()
    check(algebraic == with235 == anyp == set(table),
          f'D={D}: patterns {sorted(algebraic, key=lambda p: (len(p), p))} complete; all realizable with 2,3,5')
    for pat, v in table.items():
        check(least_by_pattern[pat] == v, f'D={D}: least number with pattern {pat} is {v}')
check(2 ** 4 == 16 > 12, 'four distinct primes force at least 16 divisors, above every target')

# ---------------------------------------------------------------- least numbers
print('\n== least number with each divisor count')
for D, claim in zip((4, 6, 8, 9, 10, 12), (6, 12, 24, 36, 48, 60)):
    least = next(m for m in range(1, LIMIT) if tau(m) == D)
    smooth = next(m for m in range(1, LIMIT) if tau(m) == D and pattern_of(m) and
                  all(p in (2, 3, 5) for p in range(2, m + 1) if m % p == 0 and is_prime(p)))
    check(least == claim == smooth, f'D={D}: least any-prime {least}, least with labels 2,3,5 {smooth}, guide {claim}')
check(2 * 3 ** 3 == 54 and 2 ** 3 * 3 == 24, 'guide: three 2s and one 3 = 24; one 2 and three 3s = 54')

# ---------------------------------------------------------------- gcd / lcm return visit
print('\n== gcd and lcm')
check(gcd(24, 36) == 12 == 2 ** 2 * 3, 'largest bag inside both 24 and 36 is 2^2*3 = 12')
check(24 * 36 // gcd(24, 36) == 72 == 2 ** 3 * 3 ** 2, 'smallest bag holding both is 2^3*3^2 = 72')
check(12 * 72 == 24 * 36, '12*72 = 24*36')

# ---------------------------------------------------------------- token kit
print('\n== token kit (eight 2s, six 3s, four 5s, two 7s): bags shown together on one page')
KIT = Counter({2: 8, 3: 6, 5: 4, 7: 2})


def need(bags):
    c = Counter()
    for b in bags:
        c.update(b)
    return c


for band, P in (('2-3', P23), ('4-5', P45)):
    for k, chunk in sorted(P.items()):
        bags = [t for t, _ in bags_in(chunk)]
        if k == 1:
            bags = [sorted(next(iter(finals((c,))[0]))) for c in cards_in(chunk)]
        if bags:
            c = need(bags)
            check(all(c[p] <= KIT[p] for p in c), f'{band} P{k}: all its bags at once need {dict(c)}')
c = Counter({2: 7, 3: 4})
check(all(c[p] <= KIT[p] for p in c), '4-5 P4 bag (seven 2s, four 3s) fits the kit')
over = {pat: v for t in guide_table.values() for pat, v in t.items() if pat[0] > 8}
print('patterns needing more than eight copies of one prime (must be drawn):', sorted(over))

# ---------------------------------------------------------------- page references
print('\n== page references in the guide')


def pages(name):
    return pdftext(name).split('\f')


stud = {'2-3': pages('week-96-grades-2-3.pdf'), '4-5': pages('week-96-grades-4-5.pdf')}
gpages = pages('week-96-facilitator.pdf')
gflat = re.sub(r'\s+', ' ', guide)
for band, sect in (('2-3', gflat.split('Grades 2--3: answers')[1].split('Grades 4--5: from')[0]),
                   ('4-5', gflat.split('Grades 4--5: from')[1].split('Proof support')[0])):
    for k, pg in re.findall(r'\\sub\{Problem (\d+), page (\d+):', sect):
        actual = next(i + 1 for i, t in enumerate(stud[band]) if f'Problem {k}:' in t)
        check(int(pg) == actual, f'guide: {band} Problem {k} is on student page {pg} (actual {actual})')
for phrase, page in (('Why prime splitting is unique', 6), ('Problem 5, page 4: complete token-count patterns', 5),
                     ('Problem 1, page 1: different splitting routes', 3)):
    actual = next(i + 1 for i, t in enumerate(gpages) if phrase in re.sub(r'\s+', ' ', t))
    check(actual == page, f'guide page {page} holds "{phrase}" (actual {actual})')
for band, n in (('2-3', 4), ('4-5', 6)):
    nums = [int(x) for t in stud[band] for x in re.findall(r'Problem (\d+):', t)]
    check(nums == list(range(1, n + 1)), f'{band}: problems numbered consecutively {nums}')

print('\nFAILURES:', len(fails))
for f in fails:
    print('  ', f)
