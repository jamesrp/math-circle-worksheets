"""Shared helpers for the independent Week 60 math check (take it or pass).

Nothing here is imported from the packet's own builders or checkers.

* find_repo(): the repository root, from this file's own location.  The
  committed copy lives in <repo>/plans/review/checks/week-60/ (four folders
  up); the working copy lives in <repo>/tmp/review-runs/week-60/ (three up).
* A small exact model of the game: a known bag (list of ticket scores, each
  ticket equally likely), draws with replacement, a fixed number n of offers,
  take-and-stop or pass-forever, the n-th offer compulsory, reward = the one
  taken score.  Everything is computed with integers (totals over all
  len(bag)**n equally likely complete words) or Fractions.
"""
import itertools
import sys
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent


def find_repo():
    for cand in (HERE.parents[3] if len(HERE.parents) > 3 else None,
                 HERE.parents[2] if len(HERE.parents) > 2 else None):
        if cand is not None and (cand / "lowell-math-circle-year-2").is_dir():
            return cand
    for p in [HERE] + list(HERE.parents):
        if (p / "lowell-math-circle-year-2").is_dir():
            return p
    sys.exit("repository not found above " + str(HERE))


REPO = find_repo()
WEEK = REPO / "lowell-math-circle-year-2" / "week-60"
STUDENT_PDF = WEEK / "week-60-students.pdf"
GUIDE_PDF = WEEK / "week-60-facilitator.pdf"
WEEK1_GUIDE_PDF = REPO / "lowell-math-circle-year-2" / "week-01" / "week-01-facilitator.pdf"


class Log:
    def __init__(self):
        self.lines, self.fails = [], []

    def say(self, *a):
        self.lines.append(" ".join(str(x) for x in a))

    def check(self, cond, msg):
        self.say(("ok   " if cond else "FAIL ") + msg)
        if not cond:
            self.fails.append(msg)
        return cond

    def note(self, msg):
        self.say("NOTE " + msg)

    def write(self, path):
        self.say("")
        self.say(f"{len(self.fails)} FAIL line(s)")
        for f in self.fails:
            self.say("  FAIL: " + f)
        Path(path).write_text("\n".join(self.lines) + "\n")
        print("\n".join(self.lines))


# ---------------------------------------------------------------- the game
def words(bag, n):
    """All len(bag)**n equally likely complete words (ticket multiplicity kept)."""
    return list(itertools.product(bag, repeat=n))


def play(word, decide):
    """Score of one complete word under decide(prefix_including_current, turns_left_incl_current).
    The last offer is compulsory, whatever decide says."""
    n = len(word)
    for k in range(n):
        left = n - k
        if left == 1 or decide(word[:k + 1], left):
            return word[k]
    raise AssertionError("unreachable")


def total(bag, n, decide):
    return sum(play(w, decide) for w in words(bag, n))


def history_policies(bag, n):
    """Every deterministic history-dependent policy for n offers: a take/pass bit
    for every observed prefix of length 1..n-1 (the last offer is forced).
    Yields (table, decide).  Count = 2**(k + k^2 + ... + k^(n-1)), k = len(set(bag))."""
    vals = sorted(set(bag))
    nodes = [p for L in range(1, n) for p in itertools.product(vals, repeat=L)]
    for bits in itertools.product((False, True), repeat=len(nodes)):
        table = dict(zip(nodes, bits))
        yield table, (lambda pre, left, t=table: t[tuple(pre)])


def tree_optimum(bag, n, prefix=()):
    """Exact best TOTAL over all complete words extending `prefix` (prefix = offers
    already passed), maximised over every history-dependent policy, by evaluating
    the whole history tree (decisions at different nodes act on disjoint word sets,
    so node-wise maximisation is the optimum over all such policies).
    Returns the integer total over len(bag)**(n-len(prefix)) words."""
    k = len(prefix)
    rest = n - k  # offers still to come, the next one included
    best = 0
    for x in bag:
        left = rest
        take = x * len(bag) ** (left - 1)
        if left == 1:
            best += take
        else:
            best += max(take, tree_optimum(bag, n, prefix + (x,)))
    return best


def V_recursion(bag, n):
    """V_1 = mean; V_m = mean(max(x, V_{m-1})).  Exact Fractions."""
    m = F(sum(bag), len(bag))
    V = [None, m]
    for _ in range(2, n + 1):
        V.append(sum((max(F(x), V[-1]) for x in bag), F(0)) / len(bag))
    return V


def first_offer_rules(bag):
    """All 2**k first-offer take/pass choice sets for two-offer rounds.
    Returns list of (frozenset_taken_values, total on the k^2 cards)."""
    vals = sorted(set(bag))
    out = []
    for r in range(len(vals) + 1):
        for taken in itertools.combinations(vals, r):
            T = frozenset(taken)
            out.append((T, total(bag, 2, lambda pre, left, T=T: pre[-1] in T)))
    return out


def fmt(fr):
    fr = F(fr)
    return str(fr.numerator) if fr.denominator == 1 else f"{fr.numerator}/{fr.denominator}"
