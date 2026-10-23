#!/usr/bin/env python3
"""Independent mathematical checks for Week 83 (Hackenbush balances).

Written for the math-check stage of the review. It does not import or run the
package's own check_math.py. Standard library only, exact Fractions.

What it checks
- A red/blue(/green) Hackenbush engine on grounded stalks (strings read from
  the ground up; a cut at index i leaves stalk[:i]). Outcomes come from plain
  minimax with no theory. Values are computed separately for whole positions
  (never by adding stalk values) as the simplest number between the best
  left and right options, and the simplest number is computed two ways:
  from the birthday tree and from a closed form.
- The theory the guide relies on, replayed on every board of at most 8
  segments made of stalks of length <= 4: value sign == outcome class,
  additivity of values, sign-expansion rule for single stalks, negation by
  colour swap, and "equal value => same outcome with every test stalk".
- Every printed board (read from student/students.tex): outcome class,
  value, every winning move for each starter.
- The guide's three-case response proof for BR+BR+R, replayed as a strategy
  against every opponent move.
- Problem 4: the guide's examples, the copy shortcut, and new examples.
- The Grades 4-5 nursery: birthday catalog days 0-3 against the 15 printed
  cards, the opening example, Problem 5 answers, the guide's Problem 6
  examples, uniqueness of the earliest card for every pair of bounds, and
  which invented pairs have no card (and why).
- Material counts, the guide's edge-count hint and the green-edge remark.

Run: python3 check_math.py   (writes check_math.py.out beside itself)
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations_with_replacement, product
from pathlib import Path
import math
import re

HERE = Path(__file__).resolve().parent


def find_repo(here):
    """Four folders up from plans/review/checks/week-NN/; else walk up."""
    if len(here.parents) > 3 and (here.parents[3] / 'AGENTS.md').is_file() and (here.parents[3] / 'lowell-math-circle-year-2').is_dir():
        return here.parents[3]
    for p in here.parents:
        if (p / 'AGENTS.md').is_file() and (p / 'lowell-math-circle-year-2').is_dir():
            return p
    raise SystemExit('repository not found above ' + str(here))


REPO = find_repo(HERE)
SRC = REPO / 'lowell-math-circle-year-2/source/week-83'
OUT, FAIL = [], []


def say(*a):
    OUT.append(' '.join(str(x) for x in a))


def check(cond, msg):
    say(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAIL.append(msg)


def fmt(x):
    if isinstance(x, F):
        return str(x.numerator) if x.denominator == 1 else f'{x.numerator}/{x.denominator}'
    return str(x)


def bname(board):
    return ' + '.join(board) if board else '(empty)'


# ------------------------------------------------------------------ engine
def norm(stalks):
    return tuple(sorted(s for s in stalks if s))


def moves(board, who):
    """who in 'BR'. Blue may cut B or G, Red may cut R or G."""
    out = []
    for i, s in enumerate(board):
        for j, c in enumerate(s):
            if c == who or c == 'G':
                out.append(((i, j), norm(board[:i] + (s[:j],) + board[i + 1:])))
    return out


@lru_cache(None)
def mover_wins(board, who):
    other = 'R' if who == 'B' else 'B'
    return any(not mover_wins(nb, other) for _, nb in moves(board, who))


def outcome(board):
    b, r = mover_wins(board, 'B'), mover_wins(board, 'R')
    return {(True, False): 'Blue', (False, True): 'Red',
            (False, False): 'second player', (True, True): 'first player'}[(b, r)]


# --------------------------------------------------- simplest number, 2 ways
def birthday_tree(days):
    born = {F(0): 0}
    for d in range(1, days + 1):
        old = sorted(born)
        new = [old[0] - 1, old[-1] + 1] + [(a + b) / 2 for a, b in zip(old, old[1:])]
        for x in new:
            born[x] = d
    return born


TREE = birthday_tree(12)


def simplest_tree(lo, hi):
    """Earliest-born number with lo < x < hi (None = no bound)."""
    fits = [x for x in TREE if (lo is None or x > lo) and (hi is None or x < hi)]
    if not fits:
        raise ValueError('tree too small')
    d = min(TREE[x] for x in fits)
    first = [x for x in fits if TREE[x] == d]
    assert len(first) == 1, (lo, hi, first)
    return first[0]


def simplest_closed(lo, hi):
    """Closed-form simplicity rule (integers by size, else least power of 2)."""
    if lo is not None and hi is not None:
        assert lo < hi
    if (lo is None or lo < 0) and (hi is None or hi > 0):
        return F(0)
    if lo is not None and lo >= 0:
        n = math.floor(lo) + 1               # least integer > lo
        if hi is None or n < hi:
            return F(n)
    if hi is not None and hi <= 0:
        n = math.ceil(hi) - 1                # greatest integer < hi
        if lo is None or n > lo:
            return F(n)
    k = 1
    while True:                              # no integer inside: least 2^k denominator
        den = 2 ** k
        m = math.floor(lo * den) + 1
        if F(m, den) < hi:
            return F(m, den)
        k += 1


@lru_cache(None)
def value(board):
    """Value of a red/blue board from its options only (no additivity)."""
    L = [value(nb) for _, nb in moves(board, 'B')]
    R = [value(nb) for _, nb in moves(board, 'R')]
    lo = max(L) if L else None
    hi = min(R) if R else None
    assert lo is None or hi is None or lo < hi, ('not a number', board)
    a = simplest_tree(lo, hi)
    b = simplest_closed(lo, hi)
    assert a == b, (board, lo, hi, a, b)
    return a


def sign_expansion(s):
    """Berlekamp: first run counts +-1 each, then halves after a colour change."""
    v, step, changed = F(0), F(1), False
    for i, c in enumerate(s):
        sg = 1 if c == 'B' else -1
        if i > 0 and c != s[i - 1]:
            changed = True
        if changed:
            step /= 2
        v += sg * step
    return v


def swap(s):
    return s.translate(str.maketrans('BR', 'RB'))


# ------------------------------------------------------------ theory replay
say('== Theory replay on small boards ==')
stalks4 = [''.join(p) for n in range(1, 5) for p in product('BR', repeat=n)]
boards = set()
for k in range(0, 4):
    for combo in combinations_with_replacement(stalks4, k):
        if sum(map(len, combo)) <= 8:
            boards.add(norm(combo))
boards = sorted(boards)
bad_sign = bad_add = bad_neg = 0
for b in boards:
    v = value(b)
    o = outcome(b)
    exp = 'Blue' if v > 0 else 'Red' if v < 0 else 'second player'
    bad_sign += (o != exp)
    bad_add += (v != sum((value((s,)) for s in b), F(0)))
    bad_neg += (value(norm(tuple(swap(s) for s in b))) != -v)
check(bad_sign == 0, f'value sign equals minimax outcome on all {len(boards)} boards (<=3 stalks of length <=4, <=8 segments)')
check(bad_add == 0, f'value of whole board (from options) equals sum of stalk values on all {len(boards)} boards')
check(bad_neg == 0, 'swapping colours negates the value on every board')
singles = [''.join(p) for n in range(1, 9) for p in product('BR', repeat=n)]
check(all(value((s,)) == sign_expansion(s) for s in singles), f'sign-expansion rule matches computed value for all {len(singles)} stalks of length 1-8')
for s, want in [('B', 1), ('R', -1), ('BR', F(1, 2)), ('BRR', F(1, 4)), ('RB', F(-1, 2))]:
    check(value((s,)) == want, f'guide overview: {s} = {fmt(F(want))}')
check(value(('BR', 'BR', 'R')) == 0 and value(('BRR', 'BRR', 'RB')) == 0, 'guide overview: BR+BR+R = 0 and BRR+BRR+RB = 0')
# options as the guide states them
check(sorted(value(nb) for _, nb in moves(('BR',), 'B')) == [0] and sorted(value(nb) for _, nb in moves(('BR',), 'R')) == [1],
      'guide: BR = {0 | 1}')
check(sorted(value(nb) for _, nb in moves(('BRR',), 'B')) == [0] and sorted(value(nb) for _, nb in moves(('BRR',), 'R')) == [F(1, 2), 1],
      'guide: BRR = {0 | 1, 1/2}; upper R cut leaves BR, lower R cut leaves B')

# equal value => indistinguishable by any test stalk (encore)
tests = [()] + [(s,) for s in stalks4]
pairs = [(('BR', 'BR'), ('B',)), (('BRR', 'BRR'), ('BR',)), (('BR', 'BR', 'R'), ()), (('BRR', 'BRR', 'RB'), ('BR', 'RB'))]
for g, h in pairs:
    same = all(outcome(norm(g + t)) == outcome(norm(h + t)) for t in tests)
    check(value(norm(g)) == value(norm(h)) and same, f'encore: {bname(g)} and {bname(h)} (both {fmt(value(norm(g)))}) give the same outcome with each of {len(tests)} test stalks')
# and different values are told apart by some test stalk
g, h = ('BR',), ('BRR',)
wit = [t for t in tests if outcome(norm(g + t)) != outcome(norm(h + t))]
check(bool(wit), f'encore: BR and BRR are told apart by a test stalk, e.g. adding {bname(wit[0])}')

# ------------------------------------------------------------ printed boards
say('')
say('== Printed boards (parsed from student/students.tex) ==')
# Re-pointed on 2026-10-23: the problem-file conversion (8e59b53) and the card's shoulds and coulds (ff74daa)
# changed and moved the packet sources, so the review checks read the copies as reviewed:
# week-83/archive-before-card-fixes-2026-10-23/ and the reviewed TeX in
# source/week-83/archive-before-problem-files-2026-10-23/week-83-source.zip (identical to the reviewed files).
tex = (SRC / 'archive-before-problem-files-2026-10-23' / 'students.tex').read_text()
body = tex.split('\\begin{document}')[1]
sheets = re.findall(r'\\begin\{sheet\}(.*?)\\end\{sheet\}', body, re.S)
check(len(sheets) == 7, f'7 sheets in source (found {len(sheets)})')


def parse_boards(sheet):
    cases = [(float(x), float(y), l) for x, y, l in re.findall(r'\\case\{([\d.]+)\}\{([\d.]+)\}\{(\w)\}', sheet)]
    grounds = [(float(x), float(y), float(w)) for x, y, w in re.findall(r'\\ground\{([\d.]+)\}\{([\d.]+)\}\{([\d.]+)\}', sheet)]
    stalks = [(float(x), float(y), s.replace(',', '')) for x, y, s in re.findall(r'\\stalk\{([\d.]+)\}\{([\d.]+)\}\{([BR,]+)\}', sheet)]
    out = {}
    for gx, gy, gw in grounds:
        on = sorted((x, s) for x, y, s in stalks if y == gy and gx <= x <= gx + gw)
        # label: the \case nearest above this ground whose x is left of the ground's right end
        cands = [(cy - gy + abs(cx - gx), l) for cx, cy, l in cases if cy > gy and cx <= gx + gw and cx >= gx - 15]
        if not cands or not on:
            continue
        lab = min(cands)[1]
        out[lab] = tuple(s for _, s in on)
    assigned = sum(len(v) for v in out.values())
    return out, assigned, len(stalks)


expected = {
    1: {'A': ('B',), 'B': ('R',), 'C': ('B', 'R'), 'D': ('BB', 'R')},
    2: {'A': ('BR', 'R'), 'B': ('BR', 'BR', 'R'), 'C': ('BR', 'BR', 'BR', 'R')},
    3: {'A': ('BRR', 'RB'), 'B': ('BRR', 'BRR', 'RB'), 'C': ('BRR', 'BRR', 'BRR', 'RB')},
}
printed = {}
for p in (1, 2, 3):
    bd, assigned, total = parse_boards(sheets[p - 1])
    if p == 1:
        bd.pop(None, None)
    # page 1 also holds the worked example (BRB) which has no \case label
    ex = [s for s in re.findall(r'\\stalk\{[\d.]+\}\{119\}\{([BR,]+)\}', sheets[0])]
    if p == 1:
        check(ex[0].replace(',', '') == 'BRB', 'p.1 worked example starts as B,R,B; after Red cuts R only B is left: ' + str(norm(('BRB'[:1],))))
        check(moves(('BRB',), 'R') == [((0, 1), ('B',))], 'p.1 worked example: Red\'s only cut on BRB leaves B (top B drops)')
        check(value(('BRB',)) == F(3, 4), 'p.1 worked example BRB has value 3/4 and is not a task board')
    printed[p] = bd
    check(bd == expected[p], f'p.{p} boards read from source: ' + '; '.join(f'{k}={bname(v)}' for k, v in sorted(bd.items())))

guide_classes = {1: ['Blue', 'Red', 'second player', 'Blue'],
                 2: ['Red', 'second player', 'Blue'],
                 3: ['Red', 'second player', 'Blue']}


def winning_moves(board, who):
    other = 'R' if who == 'B' else 'B'
    res = []
    for (i, j), nb in moves(board, who):
        if not mover_wins(nb, other):
            res.append(f'cut {board[i]}[{j}] (segment {j + 1} from ground) -> {bname(nb)}')
    return res


for p in (1, 2, 3):
    for k, (lab, b) in enumerate(sorted(printed[p].items())):
        b = norm(b)
        o, v = outcome(b), value(b)
        say(f'  Problem {p}{lab}: {bname(b)}  value {fmt(v)}  outcome {o}')
        for who in 'BR':
            wm = winning_moves(b, who)
            say(f'     {"Blue" if who == "B" else "Red"} to move: ' + ('; '.join(wm) if wm else 'no winning move' if moves(b, who) else 'no move at all'))
        check(o == guide_classes[p][k], f'guide winner class for Problem {p}{lab}: {guide_classes[p][k]}')
say('  Problem 1 "one color always win": A, B, D yes; C no (second player wins).')
check([lab for lab, b in sorted(printed[2].items()) if outcome(norm(b)) == 'second player'] == ['B'], 'Problem 2: only board B balances')
check([lab for lab, b in sorted(printed[3].items()) if outcome(norm(b)) == 'second player'] == ['B'], 'Problem 3: only board B balances')

# ------------------------------------- reply tables for the winner (key)
say('')
say('== Reply tables: the winner\'s answers to every opening (for "whoever starts") ==')


def desc(board, nb):
    """Name the cut that turns board into nb."""
    for (i, j), x in moves(board, 'B') + moves(board, 'R'):
        if x == nb:
            return f'{board[i]} at segment {j + 1}'
    return '?'


def reply_table(board, opener):
    other = 'R' if opener == 'B' else 'B'
    seen = set()
    for _, nb in moves(board, opener):
        if nb in seen:
            continue
        seen.add(nb)
        wins = sorted({x for _, x in moves(nb, other) if not mover_wins(x, opener)})
        say(f'     {"Blue" if opener == "B" else "Red"} cuts {desc(board, nb)} -> {bname(nb)} ({fmt(value(nb))}); '
            f'{"Red" if opener == "B" else "Blue"} wins by: ' + ('; '.join(f'{desc(nb, x)} -> {bname(x)} ({fmt(value(x))})' for x in wins) or 'NONE'))
        if not wins and moves(nb, other):
            FAIL.append(f'no winning reply at {bname(nb)}')


for lab, opener in [('2A', 'B'), ('2B', 'B'), ('2B', 'R'), ('2C', 'R'), ('3A', 'B'), ('3B', 'B'), ('3B', 'R'), ('3C', 'R'), ('1D', 'R')]:
    b = norm(printed[int(lab[0])][lab[1]])
    say(f'  Problem {lab} {bname(b)}, {"Blue" if opener == "B" else "Red"} starts:')
    reply_table(b, opener)

# ------------------------------------------------ guide's response proof
say('')
say('== Guide response proof for BR+BR+R (replayed against every reply) ==')


def guide_response(board, mover_just_moved):
    """Second player's reply as the guide states it, given the board after the opener."""
    b = norm(board)
    if mover_just_moved == 'B':   # Blue opened
        if b == ('BR', 'R'):              # Blue cut a BR base
            return ('B', 'R')              # Red cuts the other BR's top R
        if b == ('R',):                    # after Blue removes B from B+R
            return ()                      # Red removes R last
    else:                          # Red opened
        if b == ('BR', 'BR'):             # Red cut the lone R
            return ('BR',)                 # Blue removes one whole BR
        if b == ('B', 'BR', 'R'):         # Red cut a BR top R
            return ('B', 'R')              # Blue removes the other whole BR
        if b == ('B',):                    # Red cut remaining top R / or the R of B+R
            return ()                      # Blue removes the base / B last
    return None


def strategy_wins(board, opener):
    """True if the guide's replies (second player) beat every opener move."""
    responder = 'R' if opener == 'B' else 'B'
    opts = moves(board, opener)
    if not opts:
        return True
    for _, nb in opts:
        reply = guide_response(nb, opener)
        if reply is None:
            say('     no guide reply for', bname(nb))
            return False
        if reply not in [x for _, x in moves(nb, responder)]:
            say('     guide reply illegal at', bname(nb))
            return False
        if not strategy_wins(norm(reply), opener):
            return False
    return True


check(strategy_wins(('BR', 'BR', 'R'), 'B'), 'Blue opens: guide\'s Red replies win against every Blue line')
check(strategy_wins(('BR', 'BR', 'R'), 'R'), 'Red opens: guide\'s Blue replies win against every Red line')

# ------------------------------------------------------------- Problem 4
say('')
say('== Problem 4: balanced boards with a stalk of at least two segments ==')
for b in [('BR', 'BR', 'R'), ('BRR', 'BRR', 'RB')]:
    check(outcome(norm(b)) == 'second player', f'guide example {bname(b)} balances')
say('  Note: both guide examples are exactly the balanced boards printed as Problems 2B and 3B.')
new = [('BR', 'RB'), ('B', 'RB', 'RB'), ('BBR', 'R', 'RB'), ('BR', 'BRR', 'BRR', 'R'), ('BRB', 'RBR'), ('BB', 'RR'), ('BRR', 'BRR', 'BRR', 'BRR', 'R')]
for b in new:
    check(outcome(norm(b)) == 'second player' and value(norm(b)) == 0, f'other balanced board: {bname(b)}')
# mirror boards always balance
mirrors = [norm((s, swap(s))) for s in stalks4]
check(all(outcome(m) == 'second player' for m in mirrors), f'every stalk plus its colour-swapped copy balances ({len(mirrors)} stalks of length <= 4)')
bal = [b for b in boards if b and outcome(b) == 'second player' and max(map(len, b)) >= 2]
say(f'  balanced boards among the small-board family with a stalk of length >= 2: {len(bal)}')

# ------------------------------------------------------------- materials
say('')
say('== Materials: segments per printed board ==')
mx = {'B': 0, 'R': 0}
for p in (1, 2, 3):
    for lab, b in printed[p].items():
        s = ''.join(b)
        mx['B'] = max(mx['B'], s.count('B'))
        mx['R'] = max(mx['R'], s.count('R'))
check(mx['B'] <= 12 and mx['R'] <= 12, f'largest printed board needs {mx["B"]} blue and {mx["R"]} red segments (guide: at least twelve of each)')

# --------------------------------------------------- guide hints and asides
say('')
say('== Guide hints ==')
say(f'  edge-count hint: B alone value {fmt(value(("B",)))} ({outcome(("B",))}); BR alone value {fmt(value(("BR",)))} ({outcome(("BR",))}); '
    f'blue-minus-red edge counts 1 and 0.  B + RB (B "versus" BR) value {fmt(value(("B", "RB")))} ({outcome(norm(("B", "RB")))}).')
check(outcome(('G',)) == 'first player', 'a single green edge is a first-player win (star)')
nonzero = [x for x in TREE if TREE[x] <= 3 and x != 0]
# * + (-x): represent -x by a red/blue stalk of that value
stalk_of = {value((s,)): s for s in singles}
ok = all(outcome(norm(('G', stalk_of[-x]))) != 'second player' for x in nonzero if -x in stalk_of)
check(ok and outcome(('G',)) != 'second player', 'a green edge equals no number of birthday <= 3: G plus the stalk for -x is never a second-player win')

# ------------------------------------------------------------- nursery
say('')
say('== Grades 4-5 nursery ==')
want = {F(0): 0, F(-1): 1, F(1): 1, F(-2): 2, F(-1, 2): 2, F(1, 2): 2, F(2): 2}
for x in [-3, F(-3, 2), F(-3, 4), F(-1, 4), F(1, 4), F(3, 4), F(3, 2), 3]:
    want[F(x)] = 3
tree3 = {x: d for x, d in TREE.items() if d <= 3}
check(tree3 == want, 'birthday tree days 0-3 equals the guide\'s list (15 numbers)')
# printed cards
cards_src = re.search(r'\\foreach \\num/\\day/\\col/\\row in \{(.*?)\}\{%', tex, re.S).group(1)
cards = {}
for item in cards_src.split(','):
    num, day, col, row = item.split('/')
    num = num.strip()
    m = re.fullmatch(r'(-?)\\frac(\d)(\d)', num)
    x = F(int(m.group(2)), int(m.group(3))) * (-1 if m.group(1) else 1) if m else F(int(num))
    cards[x] = int(day)
check(cards == want, 'the 15 printed cards on p.6 carry the right first birthdays, each number once')
check(len({(c.split('/')[2], c.split('/')[3]) for c in cards_src.split(',')}) == 15, '15 distinct card grid slots')


def pick(lo_cards, hi_cards, catalog):
    fits = [x for x in catalog if all(x > a for a in lo_cards) and all(x < b for b in hi_cards)]
    if not fits:
        return None, []
    d = min(catalog[x] for x in fits)
    return [x for x in fits if catalog[x] == d], fits


p, fits = pick([F(-2)], [F(2)], cards)
check(p == [0] and {F(-1), F(0), F(1)} <= set(fits), 'opening example: bounds -2, 2 -> 0 (day 0); -1, 0, 1 all fit')
for (lo, hi), ans in zip([(0, 3), (-1, 1), (0, 1), (F(1, 2), 1)], [1, 0, F(1, 2), F(3, 4)]):
    p, _ = pick([F(lo)], [F(hi)], cards)
    check(p == [F(ans)] and simplest_tree(F(lo), F(hi)) == ans, f'Problem 5: greater than {fmt(F(lo))}, less than {fmt(F(hi))} -> {fmt(F(ans))} (unique; also the true simplest number)')
check(F(3, 2) != 1, 'guide: {0|3} is 1, not the midpoint 3/2')
# all pairs of single cards
vals = sorted(cards)
amb = nofit_ok = nofit_order = 0
newer_both, older_both, same_choice = [], [], {}
for lo in vals:
    for hi in vals:
        p, _ = pick([lo], [hi], cards)
        if lo >= hi:
            nofit_order += (p is None)
            continue
        if p is None:
            nofit_ok += 1
            continue
        amb += (len(p) != 1)
        x = p[0]
        check_true = (x == simplest_tree(lo, hi))
        if not check_true:
            FAIL.append(f'catalog pick differs from simplest for {lo},{hi}')
        same_choice.setdefault(x, []).append((lo, hi))
        if cards[x] > cards[lo] and cards[x] > cards[hi]:
            newer_both.append((lo, hi, x))
        if cards[x] < cards[lo] and cards[x] < cards[hi]:
            older_both.append((lo, hi, x))
n_lt = sum(1 for lo in vals for hi in vals if lo < hi)
check(amb == 0, f'every pair of card bounds with left < right that some card fits has exactly one earliest card ({n_lt} ordered pairs)')
check(not [f for f in FAIL if f.startswith('catalog pick')], 'whenever a card fits, the catalog pick is the true simplest number')
say(f'  pairs with left < right but no card fits (simplest number born on day 4+): {nofit_ok}, e.g. ' +
    ', '.join(f'({fmt(lo)}, {fmt(hi)}) -> {fmt(simplest_tree(lo, hi))} day {TREE[simplest_tree(lo, hi)]}'
              for lo, hi in [(F(1, 4), F(1, 2)), (F(2), F(3)), (F(3, 4), F(1))]))
say(f'  pairs with left >= right (no number of any day fits): {nofit_order} of {len(vals) ** 2}; e.g. (1, 1), (1, 1/2), (2, -2)')
check(nofit_order == len(vals) ** 2 - n_lt, 'every pair with left >= right has no fitting card')
say(f'  pairs choosing a card newer than both bounds: {len(newer_both)}, e.g. ' + ', '.join(f'({fmt(a)}, {fmt(b)}) -> {fmt(c)}' for a, b, c in newer_both))
say(f'  pairs choosing a card older than both bounds: {len(older_both)}')
check(cards[F(1, 2)] > cards[F(0)] and cards[F(1, 2)] > cards[F(1)], 'guide Problem 6: (0, 1) -> 1/2 is newer than both bounds')
check(pick([F(-1)], [F(1)], cards)[0] == [0] and pick([F(-1, 2)], [F(1, 2)], cards)[0] == [0], 'guide Problem 6: (-1, 1) and (-1/2, 1/2) both choose 0')
check(any(len(v) >= 2 for v in same_choice.values()), 'Problem 6 first task is possible')
check(len(newer_both) > 0, 'Problem 6 second task is possible with printed cards only')

say('')
say(f'FAILURES: {len(FAIL)}')
for f in FAIL:
    say('  ' + f)
(HERE / 'check_math.py.out').write_text('\n'.join(OUT) + '\n')
print('\n'.join(OUT))
