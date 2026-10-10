"""This review's own model of the Week 17 card machines.

A machine is (n, start, acc, delta): states 0..n-1, a start state, a tuple of
booleans (YES/NO per state) and delta[(state, letter)] for letters 'R', 'B'.
Everything here is written from the definitions on the student pages; nothing
is imported from the packet.
"""
import itertools
from collections import deque

A = 'RB'


def machine(n, start, acc, table):
    """table: {state: (on_R, on_B)}"""
    delta = {}
    for s, (r, b) in table.items():
        delta[(s, 'R')] = r
        delta[(s, 'B')] = b
    assert len(delta) == 2 * n
    return (n, start, tuple(acc), delta)


def run(m, w, s=None):
    n, start, acc, delta = m
    s = start if s is None else s
    for ch in w:
        s = delta[(s, ch)]
    return s


def accepts(m, w):
    return m[2][run(m, w)]


def strings(L):
    for t in itertools.product(A, repeat=L):
        yield ''.join(t)


def strings_upto(L):
    for k in range(L + 1):
        yield from strings(k)


def reachable(m):
    n, start, acc, delta = m
    seen = {start}
    q = deque([start])
    while q:
        s = q.popleft()
        for a in A:
            t = delta[(s, a)]
            if t not in seen:
                seen.add(t)
                q.append(t)
    return seen


def minimal_size(m):
    """Moore partition refinement on the reachable part."""
    n, start, acc, delta = m
    R = sorted(reachable(m))
    cls = {s: int(acc[s]) for s in R}
    while True:
        sig = {s: (cls[s], cls[delta[(s, 'R')]], cls[delta[(s, 'B')]]) for s in R}
        keys = {}
        new = {s: keys.setdefault(sig[s], len(keys)) for s in R}
        if len(set(new.values())) == len(set(cls.values())):
            return len(set(new.values()))
        cls = new


def equivalent(m1, m2):
    """Exact language equality by product reachability; returns (True, None)
    or (False, shortest counterexample)."""
    s0 = (m1[1], m2[1])
    prev = {s0: ''}
    q = deque([s0])
    while q:
        a, b = q.popleft()
        if m1[2][a] != m2[2][b]:
            return False, prev[(a, b)]
        for ch in A:
            t = (m1[3][(a, ch)], m2[3][(b, ch)])
            if t not in prev:
                prev[t] = prev[(a, b)] + ch
                q.append(t)
    return True, None


def all_machines(n):
    """Every machine with states 0..n-1 and start 0 (labelled, start fixed)."""
    keys = [(s, a) for s in range(n) for a in A]
    for targets in itertools.product(range(n), repeat=2 * n):
        delta = dict(zip(keys, targets))
        for acc in itertools.product((False, True), repeat=n):
            yield (n, 0, acc, delta)


def count_machines(n):
    return n ** (2 * n) * 2 ** n


def brute_min(target, kmax):
    """Smallest k <= kmax with a k-state machine equivalent to target, else None.
    Also returns how many machines were examined."""
    seen = 0
    for k in range(1, kmax + 1):
        for m in all_machines(k):
            seen += 1
            if equivalent(m, target)[0]:
                return k, seen
    return None, seen


def distinguish(pred, u, v, maxlen=8):
    """Shortest suffix z (length <= maxlen) with pred(u+z) != pred(v+z)."""
    for z in strings_upto(maxlen):
        if pred(u + z) != pred(v + z):
            return z
    return None


# ---------------------------------------------------------------- targets

def mod_red(k):
    """Red count divisible by k (my construction: remainder cycle)."""
    return machine(k, 0, [s == 0 for s in range(k)],
                   {s: ((s + 1) % k, s) for s in range(k)})


def even_red():
    return mod_red(2)


def last_is(letter):
    # state 0 = no card or last card is not `letter`, 1 = last card is `letter`
    move = (1 if letter == 'R' else 0, 1 if letter == 'B' else 0)
    return machine(2, 0, [False, True], {0: move, 1: move})


def seen_red():
    return machine(2, 0, [False, True], {0: (1, 0), 1: (1, 1)})


def no_red():
    return machine(2, 0, [True, False], {0: (1, 0), 1: (1, 1)})


def suffix_RB():
    # 0 = nothing useful, 1 = last card R, 2 = last two cards RB
    return machine(3, 0, [False, False, True], {0: (1, 0), 1: (1, 2), 2: (1, 0)})


def exactly_two_red():
    return machine(4, 0, [False, False, True, False],
                   {0: (1, 0), 1: (2, 1), 2: (3, 2), 3: (3, 3)})


def factor_RR():
    return machine(3, 0, [False, False, True], {0: (1, 0), 1: (2, 0), 2: (2, 2)})


def at_least_two_red():
    return machine(3, 0, [False, False, True], {0: (1, 0), 1: (2, 1), 2: (2, 2)})


def factor_RBR():
    return machine(4, 0, [False, False, False, True],
                   {0: (1, 0), 1: (1, 2), 2: (3, 0), 3: (3, 3)})


def even_even():
    # state = 2*redparity + blueparity
    return machine(4, 0, [True, False, False, False],
                   {s: (s ^ 2, s ^ 1) for s in range(4)})


def even_red_last_blue():
    return machine(3, 0, [False, True, False],  # E, F, O
                   {0: (2, 1), 1: (2, 1), 2: (0, 2)})


# predicates straight from the wording ------------------------------------

P = {
    'even_red': lambda w: w.count('R') % 2 == 0,
    'last_R': lambda w: w.endswith('R'),
    'last_B': lambda w: w.endswith('B'),
    'seen_R': lambda w: 'R' in w,
    'no_R': lambda w: 'R' not in w,
    'suffix_RB': lambda w: w.endswith('RB'),
    'exactly_two_R': lambda w: w.count('R') == 2,
    'factor_RR': lambda w: 'RR' in w,
    'at_least_two_R': lambda w: w.count('R') >= 2,
    'factor_RBR': lambda w: 'RBR' in w,
    'even_even': lambda w: w.count('R') % 2 == 0 and w.count('B') % 2 == 0,
    'even_red_last_blue': lambda w: w.count('R') % 2 == 0 and w.endswith('B'),
    'equal': lambda w: w.count('R') == w.count('B'),
}


def mod_pred(k):
    return lambda w: w.count('R') % k == 0


def agrees(m, pred, L):
    """First string of length <= L where machine and predicate disagree."""
    for w in strings_upto(L):
        if accepts(m, w) != pred(w):
            return w
    return None
