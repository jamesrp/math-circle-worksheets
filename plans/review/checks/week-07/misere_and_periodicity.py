"""Two general claims in the adult guide, tested by brute force.

1. Guide p. 8, "Last counter loses": "(The shift by one is special to moves
   1 to k.)"  Test: for every move list S drawn from {1..9} with up to four
   moves, is the single-pile last-counter-loses set of squares to leave
   exactly the ordinary set shifted up by one?  Under the 4-5 opening rule
   (a player who cannot move while counters are left loses) and, for
   comparison, under the textbook misere convention (a player who cannot move
   wins).  Also: does the shift survive with two piles?

2. Guide p. 1, "The pattern always repeats", and p. 8 "Periodicity".
   Test: which move lists have an outcome pattern that repeats only after a
   start-up stretch (non-zero preperiod)?
"""
import os, sys
from itertools import combinations
from functools import lru_cache
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from games import mover_wins_piles, P_positions, outcome_sequence

N = 60


def misere_textbook_P(S, upto):
    """Single pile; taking the last counter loses; a player who cannot move
    (counters left but every move too big) WINS (textbook misere)."""
    @lru_cache(maxsize=None)
    def win(n):
        if n == 0:
            return True
        moves = [s for s in S if s <= n]
        if not moves:
            return True
        return any(not win(n - s) for s in moves)
    return [n for n in range(upto + 1) if not win(n)]


print('1. Last counter loses: is it the ordinary pattern shifted up by one?')
total = 0
fail_page_rule = []
fail_textbook = []
for k in range(1, 5):
    for S in combinations(range(1, 10), k):
        total += 1
        normal = P_positions(S, N)
        shifted = [p + 1 for p in normal if p + 1 <= N]
        mis = P_positions(S, N, misere=True)
        if mis != shifted:
            fail_page_rule.append(S)
        if misere_textbook_P(S, N) != shifted:
            fail_textbook.append(S)
print(f'   move lists tested: {total} (all subsets of 1..9 with 1-4 moves), piles 0..{N}')
print(f'   4-5 page rule (stuck player loses): shift fails for {len(fail_page_rule)} lists {fail_page_rule[:5]}')
print(f'   textbook misere (stuck player wins): shift fails for {len(fail_textbook)} lists; '
      f'any containing 1? {[S for S in fail_textbook if 1 in S][:5]}')
for S in [(1, 3, 4), (1, 4), (2, 3), (1, 3, 5), (2, 5, 6)]:
    print(f'   S={S}: ordinary {P_positions(S, 20)}; last-counter-loses {P_positions(S, 20, misere=True)}')

print('   Two piles, take 1 or 2 from one pile, last counter loses:')
for a, b in [(1, 1), (2, 2), (1, 4), (0, 1), (2, 1)]:
    mis = not mover_wins_piles((a, b), (1, 2), misere=True)
    shifted_normal = not mover_wins_piles((max(a - 1, 0), max(b - 1, 0)), (1, 2))
    print(f'     ({a},{b}): mover loses? {mis}')
lose_two = [(a, b) for a in range(7) for b in range(a, 7) if not mover_wins_piles((a, b), (1, 2), misere=True)]
print(f'     two-pile last-counter-loses squares to leave, piles up to 6: {lose_two}')

print()
print('2. Does every outcome pattern repeat from the start?')


def preperiod(S, L=600):
    q = outcome_sequence(S, L)
    for p in range(1, L // 3):
        t = L - p
        while t > 0 and q[t - 1] == q[t - 1 + p]:
            t -= 1
        if t < L // 3:
            return t, p
    return None


late = []
for k in range(1, 5):
    for S in combinations(range(1, 10), k):
        t, p = preperiod(S)
        if t > 0:
            late.append((S, t, p))
print(f'   move lists (subsets of 1..9, 1-4 moves) whose pattern only repeats after a start-up: {len(late)}')
for S, t, p in late:
    print(f'     S={S}: repeats every {p} only from square {t}; squares to leave up to 30: {P_positions(S, 30)}')
for S in [(1, 2), (1, 2, 3), (1, 3, 4), (1, 4), (2, 3), (1, 3, 5), (2, 5, 6)]:
    print(f'   packet rule S={S}: (start, period) = {preperiod(S)}')
