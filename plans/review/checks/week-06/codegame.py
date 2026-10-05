"""Independent solver for the Week 6 code game (red/yellow rows, score = number
of places where test and secret agree), the yes-or-no question games and the
return-visit weighing, message and code-book tasks.

Written for the math check; it imports nothing from the packet's own sources.
Every search is exhaustive: no formula from the guide is assumed.
"""
import os
from itertools import product, combinations
from functools import lru_cache

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..'))
if not os.path.isdir(os.path.join(ROOT, 'lowell-math-circle-year-2')):
    # Running from the run folder (tmp/review-runs/week-06) rather than from
    # plans/review/checks/week-06: walk up until the repository is found.
    d = HERE
    while d != os.path.dirname(d) and not os.path.isdir(os.path.join(d, 'lowell-math-circle-year-2')):
        d = os.path.dirname(d)
    ROOT = d
PKT = os.path.join(ROOT, 'lowell-math-circle-year-2', 'week-06')
SRC = os.path.join(ROOT, 'lowell-math-circle-year-2', 'source', 'week-06')
RV_SRC = os.path.join(ROOT, 'lowell-math-circle-year-2', 'source', 'week-06-return-visit')


# ---------------------------------------------------------------- code game
def codes(n):
    return [''.join(p) for p in product('RY', repeat=n)]


def score(t, s):
    return sum(a == b for a, b in zip(t, s))


def flip(row, places):
    return ''.join(({'R': 'Y', 'Y': 'R'}[c] if i in places else c) for i, c in enumerate(row))


def fits(records, n=None):
    """All secrets that agree with every (test, score) record."""
    n = n or len(records[0][0])
    return [s for s in codes(n) if all(score(t, s) == sc for t, sc in records)]


def split(tests, cands, t):
    parts = {}
    for s in cands:
        parts.setdefault(score(t, s), []).append(s)
    return parts


def can_identify(n, k):
    """True if some adaptive way of choosing tests always identifies the
    secret after at most k tests (the breaker may stop as soon as only one
    secret fits)."""
    T = codes(n)

    @lru_cache(None)
    def ok(cands, k):
        if len(cands) <= 1:
            return True
        if k == 0:
            return False
        for t in T:
            parts = split(T, cands, t)
            if len(parts) == 1:
                continue
            if all(ok(tuple(p), k - 1) for p in parts.values()):
                return True
        return False
    return ok(tuple(T), k)


def min_identify(n):
    k = 0
    while not can_identify(n, k):
        k += 1
    return k


def can_end(n, k):
    """True if some adaptive way always produces a test scoring n (the test is
    the secret) within k tests."""
    T = codes(n)

    @lru_cache(None)
    def ok(cands, k):
        if not cands:
            return True          # no secret left in this branch
        if k == 0:
            return False
        for t in T:
            parts = split(T, cands, t)
            good = True
            for sc, p in parts.items():
                if sc == n:
                    continue      # the test was the secret: game over
                if not ok(tuple(p), k - 1):
                    good = False
                    break
            if good:
                return True
        return False
    return ok(tuple(T), k)


def min_end(n):
    k = 1
    while not can_end(n, k):
        k += 1
    return k


def separates(tests, n):
    vecs = [tuple(score(t, s) for t in tests) for s in codes(n)]
    return len(set(vecs)) == len(vecs)


def min_fixed(n, upto=None):
    """Smallest number of tests fixed in advance that give every secret a
    different list of scores."""
    T = codes(n)
    for k in range(0, (upto or n) + 1):
        for ts in combinations(T, k):
            if separates(ts, n):
                return k, ts
    return None, None


# --------------------------------------------------- yes-or-no questions
@lru_cache(None)
def min_questions_any(N):
    """Fewest yes-or-no questions (any question about the set) that always
    identify one of N things, by search over every split size."""
    if N <= 1:
        return 0
    return 1 + min(max(min_questions_any(a), min_questions_any(N - a)) for a in range(1, N))


@lru_cache(None)
def min_questions_pointing(N):
    """Questions must be 'Is it this one?'.  Stop when sure."""
    if N <= 1:
        return 0
    # yes ends the round; no leaves N-1
    return 1 + min_questions_pointing(N - 1)


def leaves_of_tree(items, tree):
    """tree: function(items_left, depth) -> predicate or None.  Returns a dict
    item -> answer pattern by playing the adaptive questions."""
    out = {}
    for x in items:
        left = list(items)
        pat = ''
        depth = 0
        while len(left) > 1:
            q = tree(tuple(left), depth)
            a = q(x)
            pat += 'Y' if a else 'N'
            left = [y for y in left if q(y) == a]
            depth += 1
        out[x] = (pat, left)
    return out


# ------------------------------------------------------- return visit
def weighing_min(N, max_k=4):
    """Fewest weighings (equal numbers of cards on each pan, any cards,
    including cards already ruled out) that always find the one heavy card
    among N.  State = (candidates, known-light cards)."""
    @lru_cache(None)
    def ok(c, g, k):
        if c <= 1:
            return True
        if k == 0:
            return False
        # a candidates + x known cards on the left, b candidates + y known on the right
        for a in range(0, c + 1):
            for b in range(0, c - a + 1):
                if a == 0 and b == 0:
                    continue
                # can the pans be made equal with the known cards?  need |a-b| <= g
                if abs(a - b) > g:
                    continue
                parts = [a, b, c - a - b]
                if max(parts) == c:
                    continue
                if all(ok(p, g + c - p, k - 1) for p in parts):
                    return True
        return False
    for k in range(0, max_k + 1):
        if ok(N, 0, k):
            return k
    return None


def weighing_min_bruteforce(labels, max_k=3):
    """Direct search over actual card sets for small N (no counting shortcut)."""
    labels = tuple(labels)

    @lru_cache(None)
    def ok(cands, k):
        if len(cands) <= 1:
            return True
        if k == 0:
            return False
        for a in range(1, len(labels) // 2 + 1):
            for L in combinations(labels, a):
                rest = [x for x in labels if x not in L]
                for R in combinations(rest, a):
                    out = {}
                    for s in cands:
                        o = 'L' if s in L else 'R' if s in R else 'B'
                        out.setdefault(o, []).append(s)
                    if len(out) == 1:
                        continue
                    if all(ok(tuple(v), k - 1) for v in out.values()):
                        return True
        return False
    for k in range(0, max_k + 1):
        if ok(labels, k):
            return k
    return None


def full_binary_depth_profiles(m):
    """Multisets of leaf depths of full binary trees with m leaves."""
    if m == 1:
        return {(0,)}
    out = set()
    for a in range(1, m):
        for L in full_binary_depth_profiles(a):
            for R in full_binary_depth_profiles(m - a):
                out.add(tuple(sorted(d + 1 for d in L + R)))
    return out


def concat(book, msg):
    return ''.join(book[c] for c in msg)


def collisions(book, maxlen):
    seen = {}
    found = []
    letters = sorted(book)
    for L in range(1, maxlen + 1):
        for msg in product(letters, repeat=L):
            row = concat(book, msg)
            if row in seen and seen[row] != msg:
                found.append((seen[row], msg, row))
            seen.setdefault(row, msg)
    return found


def sardinas_patterson(words):
    """True iff the code is uniquely decodable."""
    words = set(words)

    def dangling(A, B):
        out = set()
        for a in A:
            for b in B:
                if a != b and b.startswith(a):
                    out.add(b[len(a):])
        return out
    S = dangling(words, words)
    seen = set()
    while S:
        if S & words:
            return False
        key = frozenset(S)
        if key in seen:
            return True
        seen.add(key)
        S = dangling(S, words) | dangling(words, S)
    return True
