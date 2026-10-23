#!/usr/bin/env python3
"""Independent mathematical checks for Week 97 (Square remainders).

Written for the math-check stage of the review. It does not import or run the
package's own check_math.py. Standard library only.

Squares are built by repeated addition of the side length and outputs by
repeatedly removing complete bundles (repeated subtraction), as the page
describes; Python's % is used only as a cross-check.

What it checks
- Every printed square-fact card on the student pages (a x a = b) and which
  inputs each page's cards cover.
- The opening bundles-of-4 collection, read from the printed table.
- Problems 1-6: every finite collection, the requested maxima/minima and
  missing outputs, with alternative readings of Problem 3's "most
  possibilities".
- Problem 5 and the overview identity: periodicity of square outputs, the
  identity n^2 - s^2 = mq(mq+2s), and the strip decomposition
  n^2 = mq*n + mq*s + s^2.
- Problem 6 and the guide's prime theorem: the collision criterion
  (x^2 = y^2 mod p  iff  x = y or x + y = p) and the (p+1)/2 count for every
  odd prime below 400; the counts and non-opposite collisions for 8, 9, 15.
- The guide's tables (bundle sizes 5, 7, 8, 9, 15, 3, 11), parsed from
  guide/facilitator.tex and compared with the computed collections.
- The optional product-class table (Q*Q=Q, Q*N=N, N*N=Q) for every odd prime
  below 400, and the printed size-7 examples.
- Material claims: counters needed for the squares children build, number of
  input cards, the 36-counter bound in the optional visit.

Run: python3 check_math.py   (writes check_math.py.out beside itself)
"""
import re
from itertools import combinations
from pathlib import Path

HERE = Path(__file__).resolve().parent


def find_repo(here):
    """Four folders up from plans/review/checks/week-NN/; else walk up."""
    if len(here.parents) > 3 and (here.parents[3] / 'AGENTS.md').is_file() and \
            (here.parents[3] / 'lowell-math-circle-year-2').is_dir():
        return here.parents[3]
    for p in here.parents:
        if (p / 'AGENTS.md').is_file() and (p / 'lowell-math-circle-year-2').is_dir():
            return p
    raise SystemExit('repository not found above ' + str(here))


REPO = find_repo(HERE)
SRC = REPO / 'lowell-math-circle-year-2' / 'source' / 'week-97'
STUDENT_TEX = (SRC / 'student' / 'students.tex').read_text()
GUIDE_TEX = (SRC / 'guide' / 'facilitator.tex').read_text()
OUT, FAIL = [], []


def say(*a):
    OUT.append(' '.join(str(x) for x in a))


def check(cond, msg):
    say(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAIL.append(msg)


# ------------------------------------------------------------ the operation
def square(n):
    """n x n counters, counted by adding n rows of n."""
    total = 0
    for _ in range(n):
        total += n
    return total


def output(n, m):
    """Remove complete bundles of m from the n x n square until < m remain."""
    left = square(n)
    while left >= m:
        left -= m
    return left


def collections(m, inputs):
    """output -> sorted list of inputs producing it."""
    col = {}
    for n in inputs:
        col.setdefault(output(n, m), []).append(n)
    return dict(sorted(col.items()))


def fmt(col):
    return '; '.join('%d:{%s}' % (k, ','.join(map(str, v))) for k, v in col.items())


def is_prime(n):
    return n >= 2 and all(n % d for d in range(2, int(n ** 0.5) + 1))


# cross-check the slow operation against %
check(all(output(n, m) == (n * n) % m for m in range(1, 30) for n in range(0, 60)),
      'repeated addition / bundle removal agrees with n*n % m for m<30, n<60')

# ------------------------------------------------------- printed fact cards
say('\n== Student fact cards ==')
pages = STUDENT_TEX.split('\\newpage')
check(len(pages) == 6, 'student source has 6 pages (split on \\newpage): %d' % len(pages))
all_cards = []
need = {2: set(range(0, 7)), 3: set(range(0, 9)), 4: set(range(0, 15)),
        5: set(range(7, 16)), 6: set(range(0, 11))}
for i, pg in enumerate(pages, start=1):
    cards = [(int(a), int(b)) for a, b in re.findall(r'\\support\{(\d+)\}\{(\d+)\}', pg)]
    cards = [c for c in cards]  # keep order
    # the \newcommand definition line uses #1/#2, so it is not matched
    all_cards += cards
    if cards:
        bad = [c for c in cards if c[1] != c[0] * c[0]]
        check(not bad, 'page %d: %d cards, all a x a = a^2 %s' % (i, len(cards), bad or ''))
        got = {a for a, _ in cards}
        check(got == need[i], 'page %d: cards cover inputs %s (needed %s)' %
              (i, sorted(got), sorted(need[i])))
check(len(all_cards) == 51, 'total printed card occurrences: %d (QA says 51)' % len(all_cards))

# ---------------------------------------------------------------- opening
say('\n== Opening example (p. 1) ==')
check(square(3) == 9 and 9 == 4 + 4 + 1 and output(3, 4) == 1,
      'input 3: 3x3 = 9 = 4 + 4 + 1, output 1')
m = re.search(r'Input & ([\d &]+)\\\\\s*Output & ([\d &]+)', STUDENT_TEX)
ins = [int(x) for x in m.group(1).split('&')]
outs = [int(x) for x in m.group(2).split('&')]
check(ins == [0, 1, 2, 3], 'printed inputs 0-3: %s' % ins)
check(outs == [output(n, 4) for n in ins], 'printed outputs %s = computed %s' %
      (outs, [output(n, 4) for n in ins]))
c4 = collections(4, range(4))
check(c4[1] == [1, 3], 'output 1 hides exactly inputs 1 and 3 (%s)' % c4[1])
check(sorted(c4) == [0, 1], 'two different outputs 0 and 1')
say('   bundles of 4, inputs 0-3:', fmt(c4))

# ---------------------------------------------------------------- Problem 1
say('\n== Problem 1: bundles of 5, inputs 0-4 ==')
c5 = collections(5, range(5))
say('  ', fmt(c5))
pairs = [(a, b) for a, b in combinations(range(5), 2) if output(a, 5) == output(b, 5)]
check(pairs == [(1, 4), (2, 3)], 'equal-output pairs of different inputs: %s' % pairs)
missing = [r for r in range(5) if r not in c5]
check(missing == [2, 3], 'outputs 0-4 that cannot occur: %s' % missing)
check(all(output(n, 5) in c5 for n in range(2000)),
      'no input below 2000 gives a missing output (2, 3 never occur at all)')

# ---------------------------------------------------------------- Problem 2
say('\n== Problem 2: bundles of 7, inputs 0-6 ==')
c7 = collections(7, range(7))
say('  ', fmt(c7))
mx = max(len(v) for v in c7.values()); mn = min(len(v) for v in c7.values())
most = [k for k, v in c7.items() if len(v) == mx]
fewest = [k for k, v in c7.items() if len(v) == mn]
check(most == [1, 2, 4] and mx == 2, 'most possibilities: outputs %s with %d each' % (most, mx))
check(fewest == [0] and mn == 1, 'fewest possibilities among occurring outputs: %s with %d' % (fewest, mn))
check([r for r in range(7) if r not in c7] == [3, 5, 6], 'absent outputs 3, 5, 6')

# ---------------------------------------------------------------- Problem 3
say('\n== Problem 3: bundles of 7 (0-6), 8 (0-7), 9 (0-8) ==')
res3 = {}
for mm in (7, 8, 9):
    c = collections(mm, range(mm))
    mxx = max(len(v) for v in c.values())
    res3[mm] = (c, mxx, [k for k, v in c.items() if len(v) == mxx])
    say('   size %d: %s ; max %d at outputs %s' % (mm, fmt(c), mxx, res3[mm][2]))
check(res3[7][2] == [1, 2, 4] and res3[7][1] == 2, 'size 7: outputs 1, 2, 4 tie with 2')
check(res3[8][2] == [1] and res3[8][1] == 4, 'size 8: output 1 alone, 4 inputs')
check(res3[9][2] == [0] and res3[9][1] == 3, 'size 9: output 0 alone, 3 inputs')
best = max((7, 8, 9), key=lambda k: res3[k][1])
check(best == 8, 'largest single collection: size %d' % best)
# alternative readings of "lets a secret input hide among the most possibilities"
for label, f in [('expected collection size of a uniformly chosen secret',
                  lambda c, mm: sum(len(v) ** 2 for v in c.values()) / mm),
                 ('fewest distinct outputs (negated)', lambda c, mm: -len(c)),
                 ('largest collection', lambda c, mm: max(len(v) for v in c.values()))]:
    vals = {mm: f(res3[mm][0], mm) for mm in (7, 8, 9)}
    win = max(vals, key=vals.get)
    check(win == 8 and list(vals.values()).count(vals[8]) == 1,
          'reading "%s": %s -> size %d' % (label, {k: round(v, 3) for k, v in vals.items()}, win))
zero = {mm: res3[mm][0][0] for mm in (7, 8, 9)}
check(zero == {7: [0], 8: [0, 4], 9: [0, 3, 6]}, 'output 0 collections: %s' % zero)

# ---------------------------------------------------------------- Problem 4
say('\n== Problem 4: bundles of 15, inputs 0-14 ==')
c15 = collections(15, range(15))
say('  ', fmt(c15))
check(c15[1] == [1, 4, 11, 14], 'output 1 hides %s' % c15[1])
mx15 = max(len(v) for v in c15.values())
check(mx15 == 4 and [k for k, v in c15.items() if len(v) == 4] == [1, 4],
      'no output hides more than 4; output 4 ties (%s)' % c15[4])
check(sorted(len(v) for v in c15.values()) == sorted([1, 4, 4, 2, 2, 2]) and
      sum(len(v) for v in c15.values()) == 15, 'collection sizes 1,4,4,2,2,2 sum to 15')
check([square(n) for n in c15[1]] == [1, 16, 121, 196] and
      all((square(n) - 1) % 15 == 0 for n in c15[1]), 'squares 1,16,121,196 are each 1 above a multiple of 15')

# ---------------------------------------------------------------- Problem 5
say('\n== Problem 5: bundles of 7, larger inputs ==')
seq = [output(n, 7) for n in range(7, 16)]
check(seq == [0, 1, 4, 2, 2, 4, 1, 0, 1], 'inputs 7..15 give %s (guide: 0,1,4,2,2,4,1,0,1)' % seq)
check({(n * n) % 7 for n in range(100000)} == {0, 1, 2, 4},
      'inputs 0..99999 give only outputs 0,1,2,4 (mod 7)')
ok_id = all((m_ * q + s) ** 2 - s * s == m_ * q * (m_ * q + 2 * s)
            for m_ in range(1, 40) for q in range(0, 40) for s in range(m_))
check(ok_id, 'identity n^2 - s^2 = mq(mq+2s) for m<40, q<40, 0<=s<m')
ok_strip = all((m_ * q + s) ** 2 == m_ * q * (m_ * q + s) + m_ * q * s + s * s
               for m_ in range(1, 40) for q in range(0, 40) for s in range(m_))
check(ok_strip, 'strip decomposition n^2 = mq*n + mq*s + s^2 (columns, rows, small square)')
check(100 == 70 + 21 + 9 and 100 == 14 * 7 + 2 and 9 == 1 * 7 + 2 and output(10, 7) == output(3, 7) == 2,
      'guide worked example: 100 = 70 + 21 + 9, 100 = 14*7 + 2, 9 = 1*7 + 2')
check(all(((n + 7) ** 2 - n * n) % 7 == 0 for n in range(1000)),
      'hint "what adding seven to a side adds": (n+7)^2 - n^2 = 7(2n+7)')

# ---------------------------------------------------------------- Problem 6
say('\n== Problem 6: odd primes 3, 5, 7, 11 and sizes 8, 9, 15 ==')
counts = {mm: len(collections(mm, range(mm))) for mm in (3, 5, 7, 11, 8, 9, 15)}
say('   number of different outputs (0 included):', counts)
check([counts[p] for p in (3, 5, 7, 11)] == [2, 3, 4, 6] ==
      [(p + 1) // 2 for p in (3, 5, 7, 11)], 'odd primes 3,5,7,11: 2,3,4,6 = (p+1)/2')
check([counts[m_] for m_ in (8, 9, 15)] == [3, 4, 6], 'sizes 8, 9, 15: 3, 4, 6')
check(all(2 * counts[m_] != m_ + 1 for m_ in (8, 9, 15)), 'rule (m+1)/2 fails for 8, 9 and 15')
c3, c11 = collections(3, range(3)), collections(11, range(11))
say('   size 3:', fmt(c3)); say('   size 11:', fmt(c11))
primes = [p for p in range(3, 400) if is_prime(p)]
crit = all(((x * x - y * y) % p == 0) == (x == y or x + y == p)
           for p in primes for x in range(p) for y in range(p))
check(crit, 'for every odd prime p < 400 and x,y in 0..p-1: equal outputs iff x=y or x+y=p')
check(all(len(collections(p, range(p))) == (p + 1) // 2 for p in primes),
      'for every odd prime p < 400: (p+1)/2 outputs including 0')
check(all(collections(p, range(p))[0] == [0] for p in primes), 'odd primes: only input 0 gives output 0')
# odd composites: does the (m+1)/2 count ever hold?  (side fact, not on page)
oc = [m_ for m_ in range(9, 400, 2) if not is_prime(m_)]
hold = [m_ for m_ in oc if 2 * len(collections(m_, range(m_))) == m_ + 1]
check(not hold, 'no odd composite below 400 has (m+1)/2 outputs (holds for: %s)' % hold)
check(len(collections(2, range(2))) == 2, 'side note: even prime 2 has 2 outputs, not (2+1)/2')
# non-opposite collisions named in the guide
for m_, a, b in ((8, 1, 3), (9, 0, 3), (15, 1, 4)):
    check(output(a, m_) == output(b, m_) and a != b and a + b != m_,
          'size %d: inputs %d and %d collide and are not opposite' % (m_, a, b))
check((4 - 1) * (4 + 1) % 15 == 0 and 3 % 15 and 5 % 15, '15 divides 3*5 but neither factor')
check(collections(8, range(8))[1] == [1, 3, 5, 7] and collections(9, range(9))[0] == [0, 3, 6]
      and c15[1] == [1, 4, 11, 14] and c15[4] == [2, 7, 8, 13],
      'overview composite claims: 8 -> output 1 four inputs; 9 -> output 0 three; 15 -> outputs 1 and 4 four each')
sqfree_comp = [m_ for m_ in range(4, 100) if not is_prime(m_) and
               all(m_ % (d * d) for d in range(2, 10)) and collections(m_, range(m_))[0] == [0]]
check(15 in sqfree_comp, 'overview limit: some composites (e.g. 15, 6, 10, 21) give output 0 only from 0: %s'
      % sqfree_comp[:8])

# Euclid lemma used in the guide, finite sanity check
check(all((a * b) % p != 0 or a % p == 0 or b % p == 0
          for p in primes[:15] for a in range(1, 3 * p) for b in range(1, 3 * p)),
      'prime divides a product -> divides a factor (finite sanity check, p < 50)')


# ------------------------------------------------------ guide tables parsed
say('\n== Guide tables compared with computed collections ==')
def parse_coll(text):
    """Parse '0:\\{0\\};\\quad1:\\{1,4\\}' style or '0&0&1&1,4' rows."""
    return {int(k): [int(x) for x in v.split(',')] for k, v in
            re.findall(r'(\d+):\\\{([\d,]+)\\\}', text)}

for size in (5, 7, 8, 9):
    row = re.search(r'^%d & (.*?)\\\\' % size, GUIDE_TEX, re.M)
    got = parse_coll(row.group(1)) if row else None
    check(got == collections(size, range(size)), 'guide p.3 table, size %d: %s' % (size, got))
# Problem 6 array: lines for 3 and 11 (11 spans two lines)
blk = GUIDE_TEX[GUIDE_TEX.index('3&0:'):GUIDE_TEX.index('\\end{array}', GUIDE_TEX.index('3&0:'))]
part3 = blk[:blk.index('11&')]
part11 = blk[blk.index('11&'):]
check(parse_coll(part3) == c3, 'guide p.5 inventory, size 3: %s' % parse_coll(part3))
check(parse_coll(part11) == c11, 'guide p.5 inventory, size 11: %s' % parse_coll(part11))
# Problem 4 array: rows "0&0&1&1,4,11,14\\"
arr = GUIDE_TEX[GUIDE_TEX.index('\\text{output}&\\text{inputs}'):]
arr = arr[:arr.index('\\end{array}')]
g15 = {}
for line in arr.split('\\\\')[1:]:
    cells = [c.strip().replace('\\hline', '').strip() for c in line.split('&')]
    if len(cells) == 4:
        g15[int(cells[0])] = [int(x) for x in cells[1].split(',')]
        g15[int(cells[2])] = [int(x) for x in cells[3].split(',')]
check(dict(sorted(g15.items())) == c15, 'guide p.4 inventory, size 15: %s' % dict(sorted(g15.items())))

# ----------------------------------------------------- optional products
say('\n== Optional return visit: product classes ==')
Q7 = sorted({output(n, 7) for n in range(1, 7)})
N7 = [r for r in range(1, 7) if r not in Q7]
check(Q7 == [1, 2, 4] and N7 == [3, 5, 6], 'size 7: Q = %s, N = %s' % (Q7, N7))


def cls(r, Q):
    return 'Q' if r in Q else 'N'


ok_tab = True
for p in primes:
    Q = {(x * x) % p for x in range(1, p)}
    for a in range(1, p):
        for b in range(1, p):
            pr = (a * b) % p
            exp = 'Q' if cls(a, Q) == cls(b, Q) else 'N'
            if pr == 0 or cls(pr, Q) != exp:
                ok_tab = False
    if len(Q) != (p - 1) // 2:
        ok_tab = False
check(ok_tab, 'every odd prime p < 400: QQ=Q, QN=NQ=N, NN=Q, products never 0, |Q| = (p-1)/2')
check((2 * 4) % 7 == 1 and (2 * 3) % 7 == 6 and (3 * 5) % 7 == 1 and 15 - 2 * 7 == 1,
      'printed examples: 2*4 -> 1, 2*3 -> 6, 3*5 = 15 -> two bundles of 7, 1 left')
check(max(a * b for a in range(1, 7) for b in range(1, 7)) == 36, 'six labels: at most 36 counters')
bad_comp = []
for m_ in (8, 9, 15):
    Q = {(x * x) % m_ for x in range(1, m_)} - {0}
    N = set(range(1, m_)) - Q
    for a in N:
        for b in N:
            if (a * b) % m_ not in Q:
                bad_comp.append((m_, a, b, (a * b) % m_)); break
check(bad_comp != [], 'side note: the class table is not asserted for composites, and it fails there, e.g. %s'
      % bad_comp[:3])

# ----------------------------------------------------- materials
say('\n== Material claims ==')
check(max(square(n) for n in range(9)) == 64, 'largest square children build (P3, input 8): 64 counters = kit size')
check(len(range(0, 16)) == 16, 'inputs 0-15 used on P4-P5: 16 input cards')

say('\nFAILURES: %d' % len(FAIL))
for f in FAIL:
    say('  ' + f)
text = '\n'.join(OUT) + '\n'
(HERE / 'check_math.py.out').write_text(text)
print(text)
