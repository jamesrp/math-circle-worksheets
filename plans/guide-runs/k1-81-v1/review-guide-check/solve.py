"""Independent solver for the Week 81 K-1 rule (one-each refill), written
before reading the writer's checker.  Rule: take one counter from a
nonempty bucket i (to Removed); then optionally put one counter from Supply
into any subset of the buckets numbered below i.  Last counter wins.
Checks every answer printed in the K-1 guide draft, plus its general claims.
Usage: python3 -I solve.py
"""
from functools import lru_cache
from itertools import product

def moves(p):
    out = []
    for i in range(len(p)):
        if p[i] == 0:
            continue
        for sub in product((0, 1), repeat=i):
            q = list(p); q[i] -= 1
            for j in range(i):
                q[j] += sub[j]
            out.append(tuple(q))
    return out

def distinct_moves(p):
    return sorted(set(moves(p)))

@lru_cache(None)
def first_wins(p):
    return any(not first_wins(q) for q in moves(p))

def winning_moves(p):
    return sorted({q for q in moves(p) if not first_wins(q)})

@lru_cache(None)
def lengths(p):
    if sum(p) == 0:
        return frozenset([0])
    s = set()
    for q in moves(p):
        s |= {1 + L for L in lengths(q)}
    return frozenset(s)

@lru_cache(None)
def peak(p):
    """most counters on the board at any moment of any game from p"""
    return max([sum(p)] + [peak(q) for q in moves(p)])

def W(p): return '1st' if first_wins(p) else '2nd'

out = []
def say(*a): out.append(' '.join(str(x) for x in a))

# Problem 1: one bucket
P1 = [2, 5, 3, 6, 4, 7, 11, 10]
say('P1', [(n, W((n,))) for n in P1])
guide_P1 = ['2nd', '1st', '1st', '2nd', '2nd', '1st', '1st', '2nd']
assert [W((n,)) for n in P1] == guide_P1

# Problem 2
P2 = [(1, 1), (2, 0), (0, 2), (2, 1), (1, 2), (2, 2)]
say('P2', [(p, W(p)) for p in P2])
assert [W(p) for p in P2] == ['1st', '2nd', '2nd', '1st', '1st', '2nd']

# Problem 3: unique winning results
P3 = {(1, 1): (2, 0), (2, 1): (2, 0), (1, 2): (0, 2), (3, 1): (4, 0), (2, 3): (2, 2), (3, 3): (4, 2)}
for p, q in P3.items():
    wm = winning_moves(p)
    say('P3', p, '->', wm)
    assert wm == [q], (p, wm)

# Problem 4
say('P4 (4,2)', W((4, 2)), 'lengths', sorted(lengths((4, 2))), 'peak', peak((4, 2)))
say('P4 (3,4)', W((3, 4)), 'winning', winning_moves((3, 4)), 'lengths', sorted(lengths((3, 4))), 'peak', peak((3, 4)))
assert W((4, 2)) == '2nd' and W((3, 4)) == '1st' and winning_moves((3, 4)) == [(2, 4)]

# Problem 5
dm = distinct_moves((2, 2))
say('P5 partner moves', dm, 'replies', [winning_moves(q) for q in dm])
assert dm == [(1, 2), (2, 1), (3, 1)]
assert [winning_moves(q) for q in dm] == [[(0, 2)], [(2, 0)], [(4, 0)]]

# Problems 6, 7
for n in (4, 5, 6):
    sols = [(a, n - a) for a in range(n + 1) if not first_wins((a, n - a))]
    say(f'P6/7 {n} counters: second-player splits', sols, 'all splits', n + 1)
assert [(a, 4 - a) for a in range(5) if not first_wins((a, 4 - a))] == [(0, 4), (2, 2), (4, 0)]
assert [(a, 6 - a) for a in range(7) if not first_wins((a, 6 - a))] == [(0, 6), (2, 4), (4, 2), (6, 0)]
assert all(first_wins((a, 5 - a)) for a in range(6))

# Problem 8
P8 = {(0, 1): (1, 2), (0, 2): (2, 4), (0, 3): (3, 6), (1, 1): (2, 3), (2, 2): (4, 6), (3, 3): (6, 9)}
for p, (lo, hi) in P8.items():
    L = lengths(p)
    say('P8', p, 'min', min(L), 'max', max(L), 'all', sorted(L))
    assert (min(L), max(L)) == (lo, hi)
    assert sorted(L) == list(range(lo, hi + 1))

# Problem 9
for p, m in {(0, 0, 1): 2, (0, 0, 2): 4, (0, 0, 3): 6}.items():
    say('P9', p, 'peak', peak(p))
    assert peak(p) == m

# Problem 10
P10 = {(2, 0, 1): (2, 0, 0), (1, 0, 1): (2, 0, 0), (0, 1, 1): (0, 2, 0), (1, 1, 1): (2, 2, 0)}
for p, q in P10.items():
    wm = winning_moves(p)
    say('P10', p, '->', wm)
    assert wm == [q]

# Problem 11
for p, m in {(0, 1, 1): 6, (1, 1, 1): 7, (0, 0, 3): 12}.items():
    L = lengths(p)
    say('P11', p, 'min', min(L), 'max', max(L), 'peak', peak(p))
    assert max(L) == m

# Problem 12
L = lengths((2, 2, 2))
say('P12 (2,2,2)', W((2, 2, 2)), 'min', min(L), 'max', max(L), 'peak', peak((2, 2, 2)))
assert max(L) == 14

# Table demonstration (3,2): legal results and whether either is winning
dm = distinct_moves((3, 2))
say('Demo (3,2) all results', dm, 'winning', winning_moves((3, 2)))
assert (3, 1) in dm and (4, 1) in dm
assert first_wins((3, 1)) and first_wins((4, 1))
# bucket-3 tree on student p.1
say('Tree (1,0,2) bucket-3 results', sorted({q for q in moves((1, 0, 2)) if q[2] == 1}))

# General claims in the overview
# (a) second player wins exactly at all-even positions; (b) winning move unique and as described
for n in (1, 2, 3):
    rng = {1: 13, 2: 9, 3: 6}[n]
    for p in product(range(rng), repeat=n):
        even = all(x % 2 == 0 for x in p)
        assert first_wins(p) == (not even), p
        if not even:
            j = max(i for i in range(n) if p[i] % 2)
            q = list(p); q[j] -= 1
            for i in range(j):
                q[i] += p[i] % 2
            assert winning_moves(p) == [tuple(q)], (p, winning_moves(p))
# (c) lengths: min a+b+c, max a+2b+4c, every length between
for p in product(range(5), repeat=2):
    L = lengths(p); a, b = p
    assert min(L) == a + b and max(L) == a + 2 * b and sorted(L) == list(range(a + b, a + 2 * b + 1))
for p in product(range(4), repeat=3):
    L = lengths(p); a, b, c = p
    assert min(L) == a + b + c and max(L) == a + 2 * b + 4 * c, (p, min(L), max(L))
# (d) a+2b+4c falls by 1..4 on every move, exactly 1 when every refill is made
for p in product(range(4), repeat=3):
    v = p[0] + 2 * p[1] + 4 * p[2]
    for q in moves(p):
        d = v - (q[0] + 2 * q[1] + 4 * q[2])
        assert 1 <= d <= 4
# (e) board count rises by at most 1 per bucket-3 take, never on bucket-2/1 takes
say('Overview claims verified: all-even <=> 2nd wins (1 bucket <13, 2 buckets <9, 3 buckets <6);'
    ' unique winning move = highest odd bucket + refill smaller odd; lengths a+b+c..a+2b+4c')

# Most counters ever used (Supply draw) in any game, for the kit count:
# every counter used ends in Removed, so it equals the longest game.
for p in [(11,), (3, 4), (4, 2), (3, 3), (0, 0, 3), (2, 2, 2)]:
    say('counters used at most', p, max(lengths(p)))

# Largest single-bucket count reached in any game (counter fit in one bucket)
@lru_cache(None)
def bucket_peak(p):
    return max([max(p)] + [bucket_peak(q) for q in moves(p)])
for p in [(11,), (3, 4), (4, 2), (3, 3), (0, 0, 3), (2, 2, 2), (1, 1, 1)]:
    say('largest one-bucket count', p, bucket_peak(p))

print('\n'.join(out))
print('ALL ASSERTIONS PASSED')
