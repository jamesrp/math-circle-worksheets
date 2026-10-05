"""Shared helpers for the Week 44 math check (The bag that copies: Polya urn).

Written from scratch for this review.  Nothing here imports or reads the
packet's own checkers (src/check.py, verify.py, verify_math.py,
verify_revision.py, facilitator-src/check_math.py, week-44-bonus/student/verify.py).

The scripts live (when committed) in <repo>/plans/review/checks/week-44/, so
the repository is four folders up.  While they are being written they sit in
<repo>/tmp/review-runs/week-44/, so fall back to searching upward.
"""
import sys
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent


def find_repo():
    cand = HERE.parents[3] if len(HERE.parents) > 3 else None
    if cand and (cand / "lowell-math-circle-year-2" / "week-44").is_dir():
        return cand
    for p in [HERE] + list(HERE.parents):
        if (p / "lowell-math-circle-year-2" / "week-44").is_dir():
            return p
    sys.exit("repository not found above " + str(HERE))


REPO = find_repo()
WEEK = REPO / "lowell-math-circle-year-2" / "week-44"
SRC = REPO / "lowell-math-circle-year-2" / "source" / "week-44"
BONUS_SRC = REPO / "lowell-math-circle-year-2" / "source" / "week-44-bonus"

PDFS = {
    "k-1": WEEK / "week-44-k-1.pdf",
    "grades-2-3": WEEK / "week-44-grades-2-3.pdf",
    "grades-4-5": WEEK / "week-44-grades-4-5.pdf",
    "guide": WEEK / "week-44-facilitator.pdf",
    "bonus": WEEK / "week-44-bonus.pdf",
    "bonus-guide": WEEK / "week-44-bonus-facilitator.pdf",
}


# ---------------------------------------------------------------------------
# Urn models.  A bag is a tuple of counter identities (colour, mark).  A
# history is the tuple of identities drawn.  Every history is produced by
# drawing uniformly among the identities present, so its probability is the
# product of 1/len(bag) over the steps.
# ---------------------------------------------------------------------------

def histories(colours, n, rule, first_mark=0, mark_by="draw"):
    """Yield (history, probability, final_bag) for every n-draw marked history.

    colours: starting colours, one counter each, e.g. "RB" or "RBG".
    rule: "copy" (add one of the drawn colour), "other" (two colours only: add
          one of the other colour) or "none" (return only).
    first_mark: mark of the originals (base packet: 1, bonus: 0).
    mark_by: new counters are marked by the draw number that added them
          ("draw": draw k gets first_mark + k).  The base packet's "first
          added gets 2, next gets 3" with originals 1 is the same rule with
          first_mark=1, since nothing is added without a draw.
    """
    start = tuple((c, first_mark) for c in colours)

    def rec(bag, hist, p, k):
        if k == n:
            yield hist, p, bag
            return
        for ident in bag:
            c = ident[0]
            if rule == "copy":
                new = bag + ((c, first_mark + k + 1),)
            elif rule == "other":
                assert len(colours) == 2
                o = colours[1] if c == colours[0] else colours[0]
                new = bag + ((o, first_mark + k + 1),)
            elif rule == "none":
                new = bag
            else:
                raise ValueError(rule)
            yield from rec(new, hist + (ident,), p * F(1, len(bag)), k + 1)

    yield from rec(start, (), F(1), 0)


def word(hist):
    return "".join(c for c, _ in hist)


def counts(bag, colours):
    return tuple(sum(1 for c, _ in bag if c == x) for x in colours)


def word_prob_copy(w, colours="RB"):
    """Exact probability of a colour word under copying, by the sequential
    product of (current count of drawn colour)/(current bag size)."""
    cnt = {c: 1 for c in colours}
    p = F(1)
    for c in w:
        p *= F(cnt[c], sum(cnt.values()))
        cnt[c] += 1
    return p


def fmt(x):
    return str(x) if isinstance(x, F) else repr(x)


FAILS = []


def ok(cond, msg):
    print(("  ok   " if cond else "  FAIL ") + msg)
    if not cond:
        FAILS.append(msg)
    return cond


def note(msg):
    print("  note " + msg)


def section(title):
    print()
    print("== " + title)
