"""Independent mathematical check of Week 79 (numbered-ball detectives).

Does not import or run the package's check_math.py or any guide checker.
- Replays both transfer rules day by day with explicit sets (no closed-form
  formulas are used to drive the replay; formulas are only compared against it).
  Smallest rule: each day add the next two labels to A, move min(A) to B.
  Changed rule: each day add the next two labels to A, move the larger new one.
- Opening diagram (day 1), Problem 1 (counts, day 6/10/12 states, card supply,
  mat occupancy), Problem 2 (entry and move days, labels 3, 6, 10, 20, 8),
  Problem 3 (count histories identical, memberships differ, a one-card witness),
  Problem 4 (eventual membership for each rule; which finite days could show
  the settled arrangement, under two readings of "that arrangement").
- Guide claims: overview formulas, induction step, each printed answer, the
  p. 3 hint sentences tested against BOTH rules, the p. 4 limit-interchange
  facts, and the first-route timing.
Finite replays are evidence; the infinite statements are proved by hand in
math.md (an induction on n and explicit witnesses).
Run: python3 check_math.py   (writes check_math.py.out beside itself)
"""
import os
from pathlib import Path

HERE = Path(__file__).resolve().parent


def find_repo(here):
    """Four folders up from plans/review/checks/week-NN/; else walk up."""
    four_up = here.parents[3]
    if (four_up / 'AGENTS.md').is_file():
        return four_up
    for p in here.parents:
        if (p / 'AGENTS.md').is_file() and (p / 'lowell-math-circle-year-2').is_dir():
            return p
    raise SystemExit('repository not found above ' + str(here))


REPO = find_repo(HERE)
OUT, FAIL = [], []
H = 1500  # days replayed per rule


def say(*a):
    OUT.append(' '.join(str(x) for x in a))


def check(cond, msg):
    say(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAIL.append(msg)


def replay(rule, days):
    """Return lists end[n] = (A, B) after completed day n (end[0] empty),
    mid[n] = (A, B) after adding day n's two labels, before the move,
    moved[n] = label moved on day n, entered[label] = day."""
    A, B = set(), set()
    end, mid, moved, entered = [(frozenset(), frozenset())], [None], [None], {}
    for n in range(1, days + 1):
        new = [2 * n - 1, 2 * n]
        for c in new:
            A.add(c)
            entered[c] = n
        mid.append((frozenset(A), frozenset(B)))
        if rule == 'smallest':
            m = min(A)
        elif rule == 'larger_new':
            m = max(new)
        else:
            raise ValueError(rule)
        A.remove(m)
        B.add(m)
        moved.append(m)
        end.append((frozenset(A), frozenset(B)))
    return end, mid, moved, entered


S_end, S_mid, S_moved, S_entered = replay('smallest', H)
C_end, C_mid, C_moved, C_entered = replay('larger_new', H)
move_day_S = {lab: n for n, lab in enumerate(S_moved) if lab is not None}
move_day_C = {lab: n for n, lab in enumerate(C_moved) if lab is not None}


def ceil_half(k):
    return (k + 1) // 2


# ---------------------------------------------------------------- opening
say('== Opening diagram (day 1, smallest rule)')
check(S_end[0] == (frozenset(), frozenset()), 'Before: both bowls empty')
check(S_mid[1] == (frozenset({1, 2}), frozenset()), 'Add 1 and 2: A = {1,2}, B = {}')
check(S_end[1] == (frozenset({2}), frozenset({1})), 'Move 1 to B: A = {2}, B = {1}')

# ---------------------------------------------------------------- P1
say('== Problem 1')
check(all(len(S_end[n][0]) == len(S_end[n][1]) == n for n in range(H + 1)),
      f'smallest rule: |A| = |B| = n at the end of every day 0..{H} (never different)')
check(all(len(S_mid[n][0]) == n + 1 and len(S_mid[n][1]) == n - 1 for n in range(1, H + 1)),
      'mid-day (after adding, before moving) counts are n+1 and n-1')
for n in (6, 10, 12):
    A, B = S_end[n]
    say(f'   day {n}: A = {sorted(A)}  B = {sorted(B)}')
check(S_end[6] == (frozenset(range(7, 13)), frozenset(range(1, 7))), 'day 6: A = {7..12}, B = {1..6} (guide)')
check(S_end[10] == (frozenset(range(11, 21)), frozenset(range(1, 11))), 'day 10: A = {11..20}, B = {1..10} (guide)')
check(S_end[12] == (frozenset(range(13, 25)), frozenset(range(1, 13))),
      'day 12 (the page\'s printed continuation): A = {13..24}, B = {1..12} -- not stated in the guide')
check(max(max(S_end[6][0] | S_end[6][1]), 0) == 12, 'six days use exactly cards 1-12')
check(max(S_end[12][0] | S_end[12][1]) == 24, 'twelve days use exactly cards 1-24')
occA = max(len(S_mid[n][0]) for n in range(1, 13))
occB = max(len(S_end[n][1]) for n in range(1, 13))
occA_C = max(len(C_mid[n][0]) for n in range(1, 13))
say(f'   max cards ever in A during 12 days: smallest {occA}, changed {occA_C}; max in B: {occB}')
check(occA == 13 and occB == 12 and occA_C == 13, 'a bowl/mat region must hold up to 13 cards at once in 12 days')
# formula vs replay (overview + induction)
check(all(S_end[n] == (frozenset(range(n + 1, 2 * n + 1)), frozenset(range(1, n + 1))) for n in range(H + 1)),
      f'overview: A_n = {{n+1..2n}}, B_n = {{1..n}} for n = 0..{H}')
# induction step stated in guide: from A_n, add 2n+1, 2n+2, min is n+1
ok = True
for n in range(0, 300):
    An = set(range(n + 1, 2 * n + 1))
    An |= {2 * n + 1, 2 * n + 2}
    m = min(An)
    An.remove(m)
    ok &= (m == n + 1 and An == set(range(n + 2, 2 * n + 3)))
check(ok, 'guide induction step: min({n+1..2n+2}) = n+1 and A_{n+1} = {n+2..2n+2} (n = 0..299)')

# ---------------------------------------------------------------- P2
say('== Problem 2')
check(all(move_day_S[k] == k for k in range(1, H + 1)), f'smallest rule: card k moves to B on day k (k = 1..{H})')
check(all(S_entered[k] == ceil_half(k) for k in range(1, 2 * H + 1)), 'card k enters A on day ceil(k/2)')
for k, enter, move in ((3, 2, 3), (6, 3, 6), (10, 5, 10), (20, 10, 20)):
    check(S_entered[k] == enter and move_day_S[k] == move,
          f'card {k}: enters day {enter}, moves day {move} (guide)')
check(S_entered[8] == 4 and move_day_S[8] == 8 and all(8 in S_end[n][0] for n in range(4, 8))
      and 8 not in S_end[3][0] and 8 in S_end[8][1], 'card 8: enters day 4, in A at the end of days 4-7, moves day 8 (guide)')
check(max(S_end[20][0] | S_end[20][1]) == 40 and move_day_S[20] == 20, 'running to card 20 would need 20 days = cards 1-40 > 24 supplied (so prediction is required, as printed)')
check(all(any(lab == k for lab in S_moved[1:]) for k in range(1, 200)), 'every card eventually moves ("any numbered card" has an answer)')

# ---------------------------------------------------------------- P3
say('== Problem 3 (changed rule: move the larger of today\'s two new cards)')
check(all(C_moved[n] == 2 * n for n in range(1, H + 1)), 'the larger new card is 2n; it moves on its entry day')
check(all(C_end[n] == (frozenset(range(1, 2 * n, 2)), frozenset(range(2, 2 * n + 1, 2))) for n in range(H + 1)),
      'changed rule: A_n = odd labels 1..2n-1, B_n = even labels 2..2n (overview)')
check(all(len(C_end[n][0]) == len(S_end[n][0]) and len(C_end[n][1]) == len(S_end[n][1]) for n in range(H + 1)),
      'end-of-day count histories identical under both rules')
check(all(len(C_mid[n][0]) == len(S_mid[n][0]) and len(C_mid[n][1]) == len(S_mid[n][1]) for n in range(1, H + 1)),
      'mid-day count histories identical too (no count at any moment tells the rules apart)')
check(all(C_end[n] != S_end[n] for n in range(1, H + 1)), 'the card arrangements differ on every day n >= 1')
check(C_end[1] == (frozenset({1}), frozenset({2})) and S_end[1] == (frozenset({2}), frozenset({1})),
      'day 1 already shows it: A = {1} (changed) vs A = {2} (smallest)')
check(all(1 in C_end[n][0] and 1 in S_end[n][1] for n in range(1, H + 1)),
      'one-card witness: card 1 is in B under the smallest rule and in A under the changed rule on every day >= 1')

# ---------------------------------------------------------------- P4
say('== Problem 4 (eventual membership)')


def settled(end, k, horizon):
    """Bowl k occupies from its last change on through the horizon, and that day."""
    where = [('A' if k in a else 'B' if k in b else None) for a, b in end[:horizon + 1]]
    last = max(i for i in range(len(where)) if i == 0 or where[i] != where[i - 1])
    return where[-1], last


K = 600
sS = {k: settled(S_end, k, H) for k in range(1, K + 1)}
sC = {k: settled(C_end, k, H) for k in range(1, K + 1)}
check(all(sS[k] == ('B', k) for k in range(1, K + 1)),
      f'smallest rule: label k last changes on day k and stays in B to day {H} (k = 1..{K})')
check(all(sC[k] == ('B' if k % 2 == 0 else 'A', ceil_half(k)) for k in range(1, K + 1)),
      f'changed rule: label k last changes on day ceil(k/2); odd -> A, even -> B (k = 1..{K})')
# finite days vs the settled arrangement, reading 1: the whole arrangement
check(all((n + 1) in S_end[n][0] for n in range(1, H + 1)),
      'smallest rule, every day N >= 1: label N+1 is in A, so A is never empty after day 0 (guide witness)')
check(S_end[0] == (frozenset(), frozenset()), 'smallest rule, day 0: A empty but B empty too (guide: day 0 is not the arrangement)')
check(all(len(C_end[n][0] | C_end[n][1]) == 2 * n for n in range(H + 1)),
      'both rules: a finite day holds only 2N labels, so "all labels settled" never appears in full')
# reading 2: is every card present already in its settled bowl?
present_ok_S = [n for n in range(1, 300) if all(sS[k][0] == ('A' if k in S_end[n][0] else 'B')
                                                 for k in S_end[n][0] | S_end[n][1])]
present_ok_C = [n for n in range(0, 300) if all(sC[k][0] == ('A' if k in C_end[n][0] else 'B')
                                                 for k in C_end[n][0] | C_end[n][1])]
check(present_ok_S == [], 'smallest rule: no day 1..299 has every present card in its settled bowl (N+1..2N sit in A)')
check(present_ok_C == list(range(0, 300)),
      'changed rule: on EVERY day each card present is already in its settled bowl (A odds, B evens) -- '
      'a child reading "that arrangement" as "odds in A, evens in B" can truthfully answer yes')

# ---------------------------------------------------------------- guide p. 3 hint sentences, both rules
say('== Guide p. 3 "Problems 3-4" sentences tested on both rules')
lst = range(1, 7)
s_ok = min(n for n in range(H + 1) if all(k in S_end[n][1] for k in lst)) == 6
c_never = [k for k in lst if all(k not in C_end[n][1] for n in range(H + 1))]
check(s_ok, 'smallest rule: labels 1-6 are all in B from day 6 on ("any fixed finite list eventually ... in B" true)')
check(c_never == [1, 3, 5],
      f'changed rule: labels {c_never} of the list 1-6 are never in B through day {H} -> the sentence is FALSE for Problem 3\'s rule')
c_cex = [n for n in range(1, 12) if (n + 1) not in C_end[n][0]]
check(c_cex == [1, 3, 5, 7, 9, 11],
      f'changed rule: "label N+1 is still in A" fails on days {c_cex} (every odd N; e.g. N = 1: label 2 is in B)')
lst12 = range(1, 13)
check(min(n for n in range(H + 1) if all(k in S_end[n][1] for k in lst12)) == 12,
      'smallest rule: labels 1-12 all in B from day 12')

# ---------------------------------------------------------------- guide p. 4 limits
say('== Guide p. 4 adult analysis')
N = 400
a = lambda n, k: 1 if k in S_end[n][0] else 0
check(all(a(n, k) == 0 for k in range(1, 200) for n in range(k, N)), 'a_n(k) = 0 for all n >= k: pointwise limit 0')
check(all(sum(a(n, k) for k in range(1, 2 * n + 2)) == n for n in range(N)), 'sum_k a_n(k) = n -> infinity')
check(all(max(a(n, k) for k in range(1, 2 * n + 2)) == 1 for n in range(1, N)) and max(a(0, k) for k in range(1, 3)) == 0,
      'sup_k a_n(k) = 1 for every n >= 1 and 0 for n = 0 (guide)')
env = [max(a(n, k) for n in range(N)) for k in range(1, 199)]
check(env[0] == 0 and all(e == 1 for e in env[1:]),
      'sup_n a_n(k) = 1 for every k >= 2: the least majorant is not summable (guide: no summable majorant)')
check(all(S_end[n][1] <= S_end[n + 1][1] for n in range(H)), 'B_n is increasing (monotone membership), |B_n| = n')
# a uniformly convergent example where sum and limit still do not interchange
u = lambda n, k: (1.0 / n) if k <= n else 0.0
check(all(abs(sum(u(n, k) for k in range(1, n + 1)) - 1.0) < 1e-9 for n in range(1, 200))
      and max(u(n, k) for k in range(1, n + 1)) == 1.0 / n,
      'support for "nonuniformity alone is not a universal explanation": 1/n on k <= n converges uniformly to 0 yet sums to 1')

# ---------------------------------------------------------------- guide p. 2 timing
say('== Guide p. 2 first route')
parts = {'movement break': 5, 'handle cards': 2, 'launch': 3, 'six days': 15, 'adopt labels': 10,
         'changed rule': 10, 'shared explanations': 5, 'questions/replay (at least)': 5}
check(sum(parts.values()) == 55, f'first route totals {sum(parts.values())} minutes <= 60')

say()
say(f'{len(FAIL)} failure(s)')
(HERE / 'check_math.py.out').write_text('\n'.join(OUT) + '\n')
print('\n'.join(OUT))
