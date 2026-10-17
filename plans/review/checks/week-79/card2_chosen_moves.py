"""Second card run, Week 79: what happens when the child chooses which card leaves A.

Same process as the packet (two new cards into A each day, one card from A to B),
but the mover may pick any card in A. Checks two claims the card uses:

1. Bowls reachable at the end of day n: A can be any n-card set S of 1..2n with
   |S & {1..2t}| <= t for every t <= n, and these number 2, 5, 14, 42, 132
   (Catalan numbers) for n = 1..5. Found by trying every choice sequence.
2. Keeping cards forever: a set S of labels can be exactly the cards that never
   leave A iff |S & {1..2t}| <= t for every t. Tested on the card's example sets
   by the greedy "move the smallest card in A that is not in S", run 400 days,
   against the counting condition.
Also: with the target A fixed, any choice of a non-target card works, so the
choice among non-target cards never matters (the app-fit point).
"""
from itertools import combinations

def reachable(n):
    states = {frozenset()}
    for day in range(1, n + 1):
        nxt = set()
        for a in states:
            a2 = a | {2 * day - 1, 2 * day}
            for c in a2:
                nxt.add(a2 - {c})
        states = nxt
    return states

def ballot_ok(s, n):
    return all(len([x for x in s if x <= 2 * t]) <= t for t in range(1, n + 1))

fails = 0
def check(ok, msg):
    global fails
    print(("ok   " if ok else "FAIL ") + msg)
    if not ok:
        fails += 1

counts = []
for n in range(1, 7):
    r = reachable(n)
    pred = {frozenset(c) for c in combinations(range(1, 2 * n + 1), n) if ballot_ok(c, n)}
    check(r == pred, f"day {n}: reachable A sets = n-sets of 1..{2*n} with at most t of 1..2t ({len(r)})")
    counts.append(len(r))
check(counts == [2, 5, 14, 42, 132, 429], f"counts {counts} are Catalan numbers C(n+1)")

# Any non-target choice works: for a reachable target S on day n, every sequence
# that never moves a card of S succeeds, whichever non-target card it moves.
def all_nontarget_paths_succeed(S, n):
    paths = [frozenset()]
    for day in range(1, n + 1):
        nxt = []
        for a in paths:
            a2 = a | {2 * day - 1, 2 * day}
            options = [c for c in a2 if c not in S]
            if not options:
                return False
            nxt.extend(a2 - {c} for c in options)
        paths = nxt
    return all(a == S for a in paths)

n = 5
r = reachable(n)
check(all(all_nontarget_paths_succeed(S, n) for S in r),
      f"day {n}: for every reachable target, every never-move-a-target sequence reaches it")

DAYS = 400
def greedy_keep(S_pred):
    """Run DAYS days moving the smallest non-S card; return labels never moved
    (among labels <= DAYS, so every label has had DAYS/2 days to move), or None if stuck."""
    A, moved_day = set(), {}
    for day in range(1, DAYS + 1):
        A |= {2 * day - 1, 2 * day}
        options = sorted(c for c in A if not S_pred(c))
        if not options:
            return None
        c = options[0]
        A.remove(c)
        moved_day[c] = day
    return {k for k in range(1, DAYS + 1) if k not in moved_day}

def cond(S_pred, upto=DAYS):
    return all(sum(1 for x in range(1, 2 * t + 1) if S_pred(x)) <= t for t in range(1, upto + 1))

examples = {
    "card 1 alone": lambda k: k == 1,
    "cards 1 and 3": lambda k: k in (1, 3),
    "cards 1 and 2": lambda k: k in (1, 2),
    "cards 2, 3 and 4": lambda k: k in (2, 3, 4),
    "every odd card": lambda k: k % 2 == 1,
    "every multiple of 3": lambda k: k % 3 == 0,
    "every card but card 1": lambda k: k != 1,
    "no card": lambda k: False,
}
for name, S in examples.items():
    kept = greedy_keep(S)
    c = cond(S)
    want = {k for k in range(1, DAYS + 1) if S(k)}
    if c:
        check(kept == want, f"{name}: condition holds and the greedy keeps exactly it (to day {DAYS})")
    else:
        check(kept is None, f"{name}: condition fails and the greedy gets stuck (some day A holds only kept cards)")
print(f"\n{fails} failure(s)")
