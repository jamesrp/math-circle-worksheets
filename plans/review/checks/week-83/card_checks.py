# Card-stage checks for Week 83 (independent of the package's check_math.py).
# Stalks are strings read from the ground up. A cut at index j keeps s[:j].
from functools import lru_cache
from fractions import Fraction as F

def norm(board):
    return tuple(sorted(s for s in board if s))

@lru_cache(None)
def wins(board, mover):
    # True if `mover` ('B' or 'R') moving first on board wins (normal play).
    other = 'R' if mover == 'B' else 'B'
    for i, s in enumerate(board):
        for j, c in enumerate(s):
            if c == mover:
                nb = norm(board[:i] + (s[:j],) + board[i+1:])
                if not wins(nb, other):
                    return True
    return False

def outcome(board):
    b = norm(board)
    bf, rf = wins(b, 'B'), wins(b, 'R')
    if bf and not rf: return 'Blue wins whoever starts'
    if rf and not bf: return 'Red wins whoever starts'
    if not bf and not rf: return 'second player wins (balances)'
    return 'first player wins'

def stalk_value(s):
    # sign-expansion rule for a stalk (Berlekamp): run of first colour counts 1 each, then halves.
    v = F(0); i = 0; first = s[0] if s else None
    while i < len(s) and s[i] == first:
        v += 1 if first == 'B' else -1; i += 1
    step = F(1, 2)
    while i < len(s):
        v += step if s[i] == 'B' else -step; step /= 2; i += 1
    return v

tests = {
 'BRR+BRR+R (proposed 3C)': ('BRR','BRR','R'),
 'BRR+BRR+BRR+BRR+R': ('BRR',)*4 + ('R',),
 'BR+BR+RB': ('BR','BR','RB'),
 'BR+RB': ('BR','RB'),
 'BRR+RB (3A)': ('BRR','RB'),
 'BB+RR (K-1 idea)': ('BB','RR'),
 'B+B+RR (K-1 idea)': ('B','B','RR'),
 'BB+R (1D)': ('BB','R'),
 'BBB+RR': ('BBB','RR'),
 'B+B+R': ('B','B','R'),
}
for name, b in tests.items():
    print(f'{name:28s} value {sum(stalk_value(s) for s in b)!s:>5}  {outcome(b)}')

# 1D trap: Blue starting, which first cuts win?
b = norm(('BB','R'))
for i, s in enumerate(b):
    for j, c in enumerate(s):
        if c == 'B':
            nb = norm(b[:i] + (s[:j],) + b[i+1:])
            print('1D Blue cut', s, 'at', j, '->', nb, 'wins' if not wins(nb,'R') else 'loses')

# Nursery: cards days 0-3
cards = {F(0):0, F(-1):1, F(1):1, F(-2):2, F(-1,2):2, F(1,2):2, F(2):2,
         F(-3):3, F(-3,2):3, F(-3,4):3, F(-1,4):3, F(1,4):3, F(3,4):3, F(3,2):3, F(3):3}
def choose(L, R):
    fit = [c for c in cards if L < c < R]
    if not fit: return None
    d = min(cards[c] for c in fit)
    best = [c for c in fit if cards[c] == d]
    assert len(best) == 1
    return best[0]
chosen = {}
for L in cards:
    for R in cards:
        if L < R:
            c = choose(L, R)
            if c is not None:
                chosen.setdefault(c, []).append((L, R))
never = sorted(c for c in cards if c not in chosen)
print('cards no two-card pair L<R chooses:', [str(c) for c in never])
# Each day-n card (n>=1) chosen by two earlier-day bounds?
for c in sorted(cards):
    if cards[c] == 0: continue
    earlier = [(L,R) for (L,R) in chosen.get(c, []) if cards[L] < cards[c] and cards[R] < cards[c]]
    print(f'card {str(c):>5} day {cards[c]}: pairs choosing it {len(chosen.get(c,[])):2d}; from earlier days {[(str(L),str(R)) for L,R in earlier]}')
# Problem 6 copyable from p.5: example (-2,2) and mat (-1,1) both choose 0; mats (0,1),(1/2,1) newer than both bounds
print('(-2,2)->', choose(F(-2),F(2)), ' (-1,1)->', choose(F(-1),F(1)))
for L,R in [(F(0),F(3)),(F(-1),F(1)),(F(0),F(1)),(F(1,2),F(1))]:
    c = choose(L,R); print(f'mat ({L},{R}) -> {c} day {cards[c]}; newer than both bounds: {cards[c] > max(cards[L],cards[R])}')

# App-fit build examples and P3 replacement
for name, b in {'BRB+RBR': ('BRB','RBR'), 'BRB+RB+RBB': ('BRB','RB','RBB'), 'BRB alone': ('BRB',),
                'B+RB+RB': ('B','RB','RB')}.items():
    print(f'{name:28s} value {sum(stalk_value(s) for s in b)!s:>5}  {outcome(b)}')
