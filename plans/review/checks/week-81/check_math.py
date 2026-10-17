"""Independent mathematical check of Week 81 (Buckets of Fish, Hamkins's game).

Does not import or run the package's check_math.py or any author checker.
Everything here is computed from the move rule as printed on student p. 1:

  Take turns. Remove one counter from a nonempty bucket. You may then add
  counters only to buckets strictly to its left. If you cannot move, you lose.
  For Problems 1-3, add at most one counter to each earlier bucket.
  For Problems 4-5, a refill may be any finite number of counters.

States are tuples read left to right: index 0 is Bucket 1 (the leftmost).
A move takes r counters (r = 1; r in {1,2,3} for the guide's encore) from
bucket j, then adds d_i in 0..cap to every bucket i < j.

The uncapped game has infinitely many moves from most positions, so it cannot
be enumerated. It is checked (a) through explicit constructions (Problem 4),
(b) through every finite cap K = 1..6 as a proxy (the parity answer must not
depend on K), and (c) through long random plays with large refills (Problem 5,
termination and the ordinal). The infinite statements are proved by hand in
math.md.

Run: python3 check_math.py   (writes check_math.py.out beside itself)
"""
from functools import lru_cache
from itertools import product
from pathlib import Path
import random
import re
import sys

sys.setrecursionlimit(100000)
HERE = Path(__file__).resolve().parent


def find_repo(here):
    """Four folders up from plans/review/checks/week-NN/; else walk up."""
    four_up = here.parents[3]
    if (four_up / 'AGENTS.md').is_file() and (four_up / 'lowell-math-circle-year-2').is_dir():
        return four_up
    for p in here.parents:
        if (p / 'AGENTS.md').is_file() and (p / 'lowell-math-circle-year-2').is_dir():
            return p
    raise SystemExit('repository not found above ' + str(here))


REPO = find_repo(HERE)
SRC = REPO / 'lowell-math-circle-year-2' / 'source' / 'week-81'
OUT, FAIL = [], []


def say(*a):
    OUT.append(' '.join(str(x) for x in a))


def check(cond, msg):
    if not cond:
        FAIL.append(msg)
    say(('ok   ' if cond else 'FAIL ') + msg)


# ---------------------------------------------------------------- the game
def moves(state, cap=1, take=(1,), mode='each'):
    """All successor states. mode:
    'each'     printed rule: add 0..cap to each bucket strictly left of j
    'total1'   misreading: at most one counter in total, to one left bucket
    'adjacent' misreading: add 0..cap only to the bucket just left of j
    """
    out = []
    n = len(state)
    for j in range(n):
        for r in take:
            if state[j] < r:
                continue
            base = list(state)
            base[j] -= r
            if mode == 'each':
                for adds in product(range(cap + 1), repeat=j):
                    s = base[:]
                    for i, d in enumerate(adds):
                        s[i] += d
                    out.append(tuple(s))
            elif mode == 'total1':
                out.append(tuple(base))
                for i in range(j):
                    s = base[:]
                    s[i] += 1
                    out.append(tuple(s))
            elif mode == 'adjacent':
                if j == 0:
                    out.append(tuple(base))
                else:
                    for d in range(cap + 1):
                        s = base[:]
                        s[j - 1] += d
                        out.append(tuple(s))
    return out


@lru_cache(maxsize=None)
def win(state, cap=1, take=(1,), mode='each'):
    """True if the player to move wins (normal play). Computed only from moves()."""
    return any(not win(s, cap, take, mode) for s in moves(state, cap, take, mode))


@lru_cache(maxsize=None)
def maxlen(state, cap=1):
    ms = moves(state, cap)
    return 0 if not ms else 1 + max(maxlen(s, cap) for s in ms)


@lru_cache(maxsize=None)
def minlen(state, cap=1):
    ms = moves(state, cap)
    return 0 if not ms else 1 + min(minlen(s, cap) for s in ms)


def winning_moves(state, cap=1, take=(1,), mode='each'):
    return sorted({s for s in moves(state, cap, take, mode) if not win(s, cap, take, mode)})


def all_even(s):
    return all(a % 2 == 0 for a in s)


def ordinal_less(new, old):
    """Compare omega^(m-1) a_(m-1) + ... + a_0, i.e. lexicographic from the RIGHT end."""
    for a, b in zip(reversed(new), reversed(old)):
        if a != b:
            return a < b
    return False


def name(s):
    return '(' + ','.join(map(str, s)) + ')'


# ------------------------------------------------------- printed data (tex)
tex = (SRC / 'student' / 'students.tex').read_text()
smallstarts = [tuple(map(int, m)) for m in re.findall(r'\\smallstart\{(\d+)\}\{(\d+)\}\{(\d+)\}', tex)]
paircards = [tuple(map(int, m)) for m in re.findall(r'\\paircard\{(\d+)\}\{(\d+)\}', tex)]
P1 = smallstarts[0:4]
P3 = smallstarts[4:10]
P5 = smallstarts[10:]
say('== Printed data read from students.tex ==')
say('Problem 1 starts:', ', '.join(map(name, P1)))
say('Problem 2 cards (reading order):', ', '.join(map(name, paircards)))
say('Problem 3 starts:', ', '.join(map(name, P3)))
say('Problem 5 start:', ', '.join(map(name, P5)))
check(P1 == [(0, 0, 1), (1, 1, 0), (2, 1, 1), (2, 2, 2)], 'Problem 1 has the four starts the guide names')
check(P3 == [(2, 2, 2), (1, 2, 2), (2, 1, 2), (2, 2, 1), (0, 2, 0), (3, 3, 1)], 'Problem 3 has the six starts the guide names')
check(P5 == [(1, 1, 1)], 'Problem 5 start is one counter in each of three buckets')
check(sorted(paircards) == sorted(product(range(4), repeat=2)) and len(paircards) == 16,
      'Problem 2: sixteen distinct cards, every (left,right) with 0..3 each')
db = re.findall(r'\\dotsbucket\{([\d.]+)\}\{([\d.-]+)\}\{(\d+)\}\{(\d+)\}', tex)
opening = [int(c) for _, y, c, _ in db[:9]]
check(opening == [1, 1, 2, 1, 1, 1, 2, 2, 1], 'opening visual counts: Before (1,1,2), after removal (1,1,1), after refill (2,2,1)')
p4 = [int(c) for _, y, c, _ in db[9:]]
check(p4 == [0, 1], 'Problem 4 picture is (0,1)')

# ------------------------------------------------ the opening worked visual
say('\n== Opening rule and worked visual (p. 1) ==')
check((2, 2, 1) in moves((1, 1, 2), 1), '(1,1,2) -> (2,2,1) is legal under the printed capped rule')
check((2, 2, 1) not in moves((1, 1, 2), 1, mode='total1'),
      'it is NOT legal if "at most one" were read as one counter in total, so the picture rules that reading out')
check((2, 2, 1) not in moves((1, 1, 2), 1, mode='adjacent'),
      'it is NOT legal if "to its left" meant only the adjacent bucket, so the picture rules that reading out too')
check(sum((2, 2, 1)) > sum((1, 1, 2)), 'total counters rose from 4 to 5: count is not a decreasing quantity (guide p. 4)')

# ---------------------------------------------------------------- Problem 1
say('\n== Problem 1 (capped, three buckets) ==')
for s in P1:
    w = win(s)
    say(f'  {name(s)}: {"FIRST" if w else "SECOND"} player wins; winning moves {list(map(name, winning_moves(s)))};'
        f' game length {minlen(s)}..{maxlen(s)} moves')
check([win(s) for s in P1] == [True, True, True, False],
      'guide: (0,0,1), (1,1,0), (2,1,1) first-player wins; (2,2,2) second-player win')

# ---------------------------------------------------------------- Problem 2
say('\n== Problem 2 (capped, two buckets) ==')
grid = []
for b in range(4):
    row = []
    for a in range(4):
        row.append('2nd' if not win((a, b)) else '1st')
    grid.append(row)
    say(f'  right={b}: ' + '  '.join(f'({a},{b})={row[a]}' for a in range(4)))
P2_second = sorted(s for s in paircards if not win(s))
say('  second-player cards:', ', '.join(map(name, P2_second)))
check(P2_second == [(0, 0), (0, 2), (2, 0), (2, 2)], 'guide: exactly (0,0),(0,2),(2,0),(2,2) are second-player wins')
check(moves((0, 0)) == [], '(0,0): the first player has no move and loses at once (a legitimate card under the printed rule)')
say('  longest capped two-bucket game on a card: (3,3) lasts', maxlen((3, 3)), 'moves at most,', minlen((3, 3)), 'at least')

# ---------------------------------------------------------------- Problem 3
say('\n== Problem 3 (capped, three buckets) ==')
for s in P3:
    wm = winning_moves(s)
    say(f'  {name(s)}: {"FIRST" if win(s) else "SECOND"}; winning moves {list(map(name, wm))}')
check([win(s) for s in P3] == [False, True, True, True, False, True],
      'guide: (2,2,2) and (0,2,0) second-player wins, the other four first-player')
check(all(len(winning_moves(s)) == 1 for s in P3 if win(s)),
      'under the cap each first-player start has exactly ONE winning move (so a rule can name it exactly)')
check(all(all_even(winning_moves(s)[0]) for s in P3 if win(s)), 'each of those winning moves goes to all-even')
check(winning_moves((3, 3, 1)) == [(4, 4, 0)], '(3,3,1): the only winning move removes from 3 and adds one to 1 AND 2')

# ------------------------------------------ the parity theorem, finitely
say('\n== Parity theorem: P-positions are exactly the all-even ones ==')
for cap in range(1, 7):
    bad = []
    count = 0
    for n in range(1, 5 if cap <= 2 else 4):
        hi = 5 if cap <= 2 else 4
        for s in product(range(hi + 1), repeat=n):
            count += 1
            if win(s, cap) == all_even(s):
                bad.append(s)
    check(not bad, f'cap {cap}: {count} starts (1-{4 if cap <= 2 else 3} buckets, 0-{5 if cap <= 2 else 4} each), outcome = "not all-even"'
          + (f'; counterexamples {bad[:5]}' if bad else ''))
# uniqueness of the winning move under cap 1
uniq_bad = [s for n in range(1, 5) for s in product(range(6), repeat=n)
            if win(s) and len(winning_moves(s)) != 1]
check(not uniq_bad, 'cap 1: every first-player position (1-4 buckets, 0-5 each) has exactly one winning move')
# the repair move described by the guide (p. 3)
def repair(s):
    odd = [i for i, a in enumerate(s) if a % 2]
    j = max(odd)
    t = list(s)
    t[j] -= 1
    for i in range(j):
        t[i] += t[i] % 2   # add one to each earlier odd bucket, zero to even
    return tuple(t)
rep_bad = [s for n in range(1, 5) for s in product(range(6), repeat=n)
           if not all_even(s) and (repair(s) not in moves(s, 1) or not all_even(repair(s)))]
check(not rep_bad, 'guide p. 3 repair move (rightmost odd -1; +1 to each earlier odd) is legal under the cap and gives all-even')
ae_bad = [s for n in range(1, 5) for s in product(range(0, 6, 2), repeat=n)
          if any(all_even(t) for t in moves(s, 3))]
check(not ae_bad, 'from every all-even start (1-4 buckets, 0-4 each) no move with refills up to 3 reaches all-even')

# literal reading of the overview sentence
say('\n== Guide p. 1 overview sentence, read literally ==')
say('  "remove from the rightmost odd bucket and add 0 or 1 to each earlier odd bucket to restore all-even"')
s = (1, 0, 1)
lit = (1, 0, 0)  # remove from bucket 3, add 0 to the earlier odd bucket 1
check(lit in moves(s) and not all_even(lit),
      'counterexample: from (1,0,1), taking from bucket 3 and adding 0 to odd bucket 1 gives (1,0,0), still odd')
check(repair(s) == (2, 0, 0) and all_even(repair(s)), 'the correct repair adds exactly 1 to the earlier odd bucket: (2,0,0)')
say('  Each earlier ODD bucket needs +1 (an odd amount, uncapped); each earlier EVEN bucket needs +0 (an even amount).')

# ------------------------------------------------ lengths and termination
say('\n== Lengths: capped warm-up versus larger refill caps ==')
for cap in range(1, 7):
    f = lambda s: sum(a * (cap + 1) ** i for i, a in enumerate(s))
    say(f'  cap {cap}: from (0,1) lengths {1 + min(minlen(t, cap) for t in moves((0,1), cap))}..{maxlen((0, 1), cap)};'
        f' from (1,1,1) longest {maxlen((1, 1, 1), cap)}')
    check(maxlen((0, 1), cap) == cap + 1, f'cap {cap}: longest game from (0,1) is cap+1 = {cap + 1}')
    check(maxlen((1, 1, 1), cap) == f((1, 1, 1)), f'cap {cap}: longest game from (1,1,1) = 1+(K+1)+(K+1)^2 = {f((1, 1, 1))}')
check(maxlen((0, 1), 1) == 2, 'warm-up cap: no game from (0,1) lasts more than 2 moves, so Problem 4 needs the lifted cap')

say('\n== Problem 4 (uncapped, start (0,1)) ==')
check([j for j in range(2) if (0, 1)[j] >= 1] == [1], 'from (0,1) the only bucket you can take from is bucket 2')
for target in (10, 30, 100, 1000):
    M = target - 1
    # first move: take the counter from bucket 2, refill bucket 1 with M
    state, length = (M, 0), 1
    while True:
        ms = moves(state, 0)  # bucket 1 has nothing to its left: refills impossible
        if not ms:
            break
        assert len(ms) == 1, state
        state = ms[0]
        length += 1
    check(length == target, f'refill {M} on the first move gives a game of exactly {target} moves (forced after move 1)')
say('  So the possible lengths from (0,1) are exactly 1, 2, 3, ... (refill M gives M+1): every finite number is beaten,')
say('  every play is finite, and no single bound covers all plays.')

say('\n== Problem 5 (uncapped, start (1,1,1)): random long plays with large refills ==')
rng = random.Random(81)
longest = 0
for trial in range(300):
    s = [1, 1, 1]
    steps = 0
    big = rng.choice([5, 20, 60])
    while any(s):
        j = rng.choice([i for i, a in enumerate(s) if a])
        old = tuple(s)
        s[j] -= 1
        for i in range(j):
            s[i] += rng.randint(0, big)
        steps += 1
        assert ordinal_less(tuple(s), old), (old, s)
    longest = max(longest, steps)
check(True, f'300 random plays from (1,1,1) with refills up to 5/20/60 per bucket all ended (longest {longest} moves);'
      ' the ordinal omega^2 a3 + omega a2 + a1 fell at every move')
# adversarial "try to last forever" strategy: always take from the leftmost nonempty
# bucket except refill hugely whenever forced to the right
s, steps = [1, 1, 1], 0
while any(s):
    j = min(i for i, a in enumerate(s) if a)
    s[j] -= 1
    for i in range(j):
        s[i] += 500
    steps += 1
say(f'  a deliberately long play (always take leftmost, refill 500 each time) still ends after {steps} moves')

# --------------------------------------------- the ordinal claim (guide p. 3)
say('\n== Ordinal description (guide p. 3) ==')
bad = 0
for trial in range(5000):
    n = rng.randint(1, 5)
    s = tuple(rng.randint(0, 6) for _ in range(n))
    if not any(s):
        continue
    j = rng.choice([i for i, a in enumerate(s) if a])
    t = list(s)
    t[j] -= 1
    for i in range(j):
        t[i] += rng.randint(0, 10 ** rng.randint(0, 6))
    if not ordinal_less(tuple(t), s):
        bad += 1
check(bad == 0, '5000 random uncapped moves: omega^(m-1) a_(m-1)+...+a_0 always decreases, first difference at the bucket taken from')

# --------------------------------------------------- encore (guide p. 4)
say('\n== Encore: take 1, 2 or 3; losing target multiples of four ==')
mult4 = lambda s: all(a % 4 == 0 for a in s)
for cap in (1, 2, 3, 4, 6):
    bad = []
    for n in range(1, 4):
        for s in product(range(8), repeat=n):
            if win(s, cap, (1, 2, 3)) == mult4(s):
                bad.append(s)
    holds = not bad
    say(f'  refill cap {cap}: P-positions = all multiples of 4 on 1-3 buckets, 0-7 each? {holds}'
        + (f' (first counterexamples {bad[:4]})' if bad else ''))
    if cap >= 3:
        check(holds, f'encore with refill cap {cap}: multiples of four are exactly the losing positions')
    else:
        check(not holds, f'encore with refill cap {cap}: the multiples-of-four rule fails, as the guide warns (cap must be lifted)')
check(not win((1, 1), 2, (1, 2, 3)), 'cap 2 counterexample: (1,1) is a second-player win though not all multiples of 4')

# ---------------------------------------------- guide p. 4 return visit
say('\n== Guide p. 4 return visit ==')
check(all(minlen((n,), c) == maxlen((n,), c) == n for n in range(8) for c in (1, 3)),
      'one bucket of n: every game lasts exactly n moves')
check(all(minlen((a, b)) < maxlen((a, b)) for a in range(4) for b in range(1, 4)),
      'two buckets with the right one nonempty: lengths vary')
check(maxlen((3, 0)) == 3 and maxlen((0, 1), 5) == 6,
      'a start that looks larger can finish sooner: (3,0) always 3 moves, (0,1) can last 6 with refills up to 5')

# --------------------------------------------- materials (guide p. 2)
say('\n== Counters needed in capped play from every printed start (guide p. 2: "thirty loose counters") ==')


@lru_cache(maxsize=None)
def most_added(state):
    """Most counters added during the rest of a capped play (if removed counters are never reused)."""
    best = 0
    n = len(state)
    for j in range(n):
        if state[j]:
            for adds in product((0, 1), repeat=j):
                t = list(state)
                t[j] -= 1
                for i, d in enumerate(adds):
                    t[i] += d
                best = max(best, sum(adds) + most_added(tuple(t)))
    return best


def reachable(state):
    seen, stack = {state}, [state]
    while stack:
        for t in moves(stack.pop()):
            if t not in seen:
                seen.add(t)
                stack.append(t)
    return seen


worst_board = worst_bucket = worst_used = 0
for s in P1 + paircards + P3:
    R = reachable(s)
    worst_board = max(worst_board, max(sum(t) for t in R))
    worst_bucket = max(worst_bucket, max(max(t) for t in R))
    worst_used = max(worst_used, sum(s) + most_added(s))
say(f'  most counters on the board at once: {worst_board}; most in one bucket: {worst_bucket};'
    f' most counters a single play ever needs (no reuse of removed counters): {worst_used}')
check(worst_used <= 30, 'thirty counters cover every capped play from every printed start, even without reusing removed ones')

# --------------------------------------- alternative readings (context only)
say('\n== Other readings of the rule (context only; the p. 1 picture excludes the first two) ==')
for mode in ('total1', 'adjacent'):
    diffs = [s for s in P1 + paircards + P3 if win(s, 1, (1,), mode) != win(s)]
    say(f'  {mode}: printed starts whose outcome would change: {list(map(name, diffs)) or "none"}')

say('\nFAILURES:', len(FAIL))
for f in FAIL:
    say('  ' + f)
(HERE / 'check_math.py.out').write_text('\n'.join(OUT) + '\n')
print('\n'.join(OUT))
sys.exit(1 if FAIL else 0)
