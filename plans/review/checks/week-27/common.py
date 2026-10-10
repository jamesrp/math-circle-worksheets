"""Shared helpers for the Week 27 math check (stable pairings).

Written independently of the packet's own builders and checkers: nothing here
imports from lowell-math-circle-year-2/source/, and no answer file
(math_checks.json, math-checks.json, checks.json) is read.

A profile is a pair (L, R) of dicts.  L maps each circle (left side) to its
list of squares, first choice first; R maps each square to its list of
circles.  A list may be incomplete (bonus pages); a pair is allowed only if
each names the other.  A matching is a dict circle -> square (partial
matchings allowed for incomplete lists).
"""
import os
from itertools import permutations

HERE = os.path.dirname(os.path.abspath(__file__))


def find_root():
    # Committed copy lives in plans/review/checks/week-27/: four folders up.
    cand = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..'))
    if os.path.isdir(os.path.join(cand, 'lowell-math-circle-year-2')):
        return cand
    # Fallback for the scratch run folder (tmp/review-runs/week-27/).
    d = HERE
    while d != os.path.dirname(d):
        if os.path.isdir(os.path.join(d, 'lowell-math-circle-year-2')):
            return d
        d = os.path.dirname(d)
    raise SystemExit('repository root not found')


ROOT = find_root()
WEEK = os.path.join(ROOT, 'lowell-math-circle-year-2', 'week-27')
SRC = os.path.join(ROOT, 'lowell-math-circle-year-2', 'source', 'week-27', 'editable', 'src')
BONUS_SRC = os.path.join(ROOT, 'lowell-math-circle-year-2', 'source', 'week-27-bonus', 'student-src')


class Log:
    def __init__(self):
        self.lines = []
        self.fails = 0

    def out(self, *a):
        s = ' '.join(str(x) for x in a)
        print(s)
        self.lines.append(s)

    def check(self, cond, msg):
        tag = 'ok  ' if cond else 'FAIL'
        if not cond:
            self.fails += 1
        self.out(f'[{tag}] {msg}')
        return cond

    def save(self, path):
        self.out(f'--- {self.fails} failed check(s)')
        with open(path, 'w') as f:
            f.write('\n'.join(self.lines) + '\n')


# ------------------------------------------------------------ preferences
def prefers(lst, a, b):
    """True if a is strictly ahead of b in lst.  b may be None (unpaired):
    every listed name beats being unpaired.  An unlisted a never wins."""
    if a not in lst:
        return False
    if b is None or b not in lst:
        return True
    return lst.index(a) < lst.index(b)


def allowed(P, a, s):
    L, R = P
    return s in L.get(a, []) and a in R.get(s, [])


def blockers(P, M):
    """All blocking pairs (circle, square) of matching M (dict circle->square)."""
    L, R = P
    inv = {s: a for a, s in M.items()}
    out = []
    for a in L:
        for s in R:
            if M.get(a) == s or not allowed(P, a, s):
                continue
            if prefers(L[a], s, M.get(a)) and prefers(R[s], a, inv.get(s)):
                out.append(a + s)
    return out


def perfect_matchings(left, right):
    for perm in permutations(right):
        yield dict(zip(left, perm))


def all_matchings(P):
    """Every matching (possibly partial) that uses only allowed pairs."""
    L, R = P
    left = list(L)
    res = []

    def rec(i, used, cur):
        if i == len(left):
            res.append(dict(cur))
            return
        a = left[i]
        rec(i + 1, used, cur)              # a unpaired
        for s in R:
            if s not in used and allowed(P, a, s):
                cur[a] = s
                rec(i + 1, used | {s}, cur)
                del cur[a]
    rec(0, frozenset(), {})
    return res


def stable_perfect(P):
    L, R = P
    return [M for M in perfect_matchings(list(L), list(R)) if not blockers(P, M)]


def stable_all(P):
    return [M for M in all_matchings(P) if not blockers(P, M)]


def mname(M):
    return ' / '.join(a + M[a] for a in sorted(M))


def parse_m(s):
    """'AX / BY / CZ' -> {'A':'X',...}"""
    out = {}
    for part in s.replace(' ', '').split('/'):
        out[part[0]] = part[1]
    return out


def flip(P):
    L, R = P
    return (R, L)


# ------------------------------------------------------------ asking rules
def da_all_schedules(P, askers='L', keep_first=False):
    """Run the asking rules from Problem 2 over EVERY choice of which free asker
    acts next.  Returns {final matching name: set of request counts} and the
    request logs of one run per outcome.  If keep_first, a receiver keeps its
    first asker forever (Grades 4-5 Problem 3's changed rule)."""
    L, R = P if askers == 'L' else flip(P)
    names = list(L)
    outcomes = {}
    logs = {}

    def rec(nxt, hold, log):
        held = set(hold.values())
        free = [a for a in names if a not in held]
        if not free:
            M = {a: r for r, a in hold.items()}
            if askers != 'L':
                M = {r: a for a, r in M.items()}  # back to circle -> square
            key = mname(M)
            outcomes.setdefault(key, set()).add(len(log))
            logs.setdefault(key, list(log))
            return
        for a in free:
            if nxt[a] >= len(L[a]):
                raise RuntimeError('asker ran out of choices')
            r = L[a][nxt[a]]
            nxt2 = dict(nxt)
            nxt2[a] += 1
            hold2 = dict(hold)
            cur = hold.get(r)
            if cur is None:
                hold2[r] = a
                ev = (a, r, a, None)
            elif keep_first:
                ev = (a, r, cur, a)
            elif prefers(R[r], a, cur):
                hold2[r] = a
                ev = (a, r, a, cur)
            else:
                ev = (a, r, cur, a)
            rec(nxt2, hold2, log + [ev])
    rec({a: 0 for a in names}, {}, [])
    return outcomes, logs


def da_outcomes(P, askers='L', keep_first=False):
    """Same as da_all_schedules but memoised and without logs:
    returns {final matching name: set of request counts}."""
    L, R = P if askers == 'L' else flip(P)
    names = sorted(L)
    memo = {}

    def rec(nxt, hold):
        key = (nxt, hold)
        if key in memo:
            return memo[key]
        hd = dict(hold)
        held = set(hd.values())
        free = [a for a in names if a not in held]
        res = set()
        if not free:
            M = {a: r for r, a in hd.items()}
            if askers != 'L':
                M = {r: a for a, r in M.items()}
            res.add((mname(M), 0))
        else:
            for i, a in enumerate(names):
                if a in held:
                    continue
                k = nxt[i]
                if k >= len(L[a]):
                    raise RuntimeError('asker ran out of choices')
                r = L[a][k]
                nxt2 = nxt[:i] + (k + 1,) + nxt[i + 1:]
                cur = hd.get(r)
                hd2 = dict(hd)
                if cur is None or (not keep_first and prefers(R[r], a, cur)):
                    hd2[r] = a
                for m, c in rec(nxt2, tuple(sorted(hd2.items()))):
                    res.add((m, c + 1))
        memo[key] = res
        return res
    out = {}
    for m, c in rec(tuple(0 for _ in names), ()):
        out.setdefault(m, set()).add(c)
    return out


def run_schedule(P, steps, askers='L', keep_first=False):
    """Replay a given request list [(asker, receiver), ...]; check each request
    is legal (asker free, asks its highest not-yet-asked choice).  Returns the
    list of (asker, receiver, kept, released) and the final holds."""
    L, R = P if askers == 'L' else flip(P)
    nxt = {a: 0 for a in L}
    hold = {}
    out = []
    for a, r in steps:
        held = set(hold.values())
        if a in held:
            raise ValueError(f'{a} asks while held')
        if L[a][nxt[a]] != r:
            raise ValueError(f'{a} should ask {L[a][nxt[a]]}, not {r}')
        nxt[a] += 1
        cur = hold.get(r)
        if cur is None:
            hold[r] = a
            out.append((a, r, a, None))
        elif keep_first or not prefers(R[r], a, cur):
            out.append((a, r, cur, a))
        else:
            hold[r] = a
            out.append((a, r, a, cur))
    return out, hold


def all_profiles(left, right):
    """Every complete strict profile on the given sides."""
    lp = list(permutations(right))
    rp = list(permutations(left))

    def rec(i, acc, people, perms):
        if i == len(people):
            yield dict(acc)
            return
        for p in perms:
            acc[people[i]] = list(p)
            yield from rec(i + 1, acc, people, perms)
    for Ld in rec(0, {}, list(left), lp):
        for Rd in rec(0, {}, list(right), rp):
            yield (dict(Ld), dict(Rd))


def rank(lst, x):
    return lst.index(x) + 1
