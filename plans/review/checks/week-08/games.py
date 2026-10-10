"""My own solvers for the Week 8 games, by direct game-tree search.

No formulas (no xor, no diagonal rule, no Wythoff pairs) are used to decide a
position: a position is a second-player win (P) exactly when every move from it
leads to a first-player win (N); a position with no move is decided by the end
rule of the game.
"""
from functools import lru_cache
from itertools import combinations_with_replacement


# ------------------------------------------------------------ rook race ---
def rook_moves(a, b, queen=False):
    """Token at (a, b) = a squares right of the star, b squares up.
    A move slides straight left or straight down (and, for the queen game,
    diagonally down-left) one or more squares, staying on the board."""
    for k in range(1, a + 1):
        yield (a - k, b)
    for k in range(1, b + 1):
        yield (a, b - k)
    if queen:
        for k in range(1, min(a, b) + 1):
            yield (a - k, b - k)


@lru_cache(maxsize=None)
def rook_P(a, b, queen=False):
    """Whoever moves the token onto the star wins.  (0, 0) is the star: the
    player who just moved there has won, so the player 'to move' has lost."""
    if (a, b) == (0, 0):
        return True
    return all(not rook_P(x, y, queen) for (x, y) in rook_moves(a, b, queen))


def rook_winning_moves(a, b, queen=False):
    return [m for m in rook_moves(a, b, queen) if rook_P(*m, queen)]


# ----------------------------------------------------------------- Nim ---
def nim_moves(piles):
    piles = tuple(piles)
    for i, p in enumerate(piles):
        for k in range(1, p + 1):
            yield piles[:i] + (p - k,) + piles[i + 1:], (i, k)


@lru_cache(maxsize=None)
def _nim_P_sorted(piles, misere):
    if sum(piles) == 0:
        # normal play: the previous player took the last counter and won.
        # misere: the previous player took the last counter and lost.
        return not misere
    return all(not _nim_P_sorted(tuple(sorted(q)), misere) for q, _ in nim_moves(piles))


def nim_P(piles, misere=False):
    return _nim_P_sorted(tuple(sorted(piles)), misere)


def nim_winning_moves(piles, misere=False):
    return [(q, mv) for q, mv in nim_moves(piles) if nim_P(q, misere)]


def multisets(lo, hi, k=3):
    return list(combinations_with_replacement(range(lo, hi + 1), k))


# ---------------------------------------------------- two rook boards ---
@lru_cache(maxsize=None)
def two_rooks_P(x, y, u, v):
    """Choose one board and slide its token left or down; whoever leaves both
    tokens on their stars wins."""
    if (x, y, u, v) == (0, 0, 0, 0):
        return True
    succ = [(a, b, u, v) for (a, b) in rook_moves(x, y)] + \
           [(x, y, a, b) for (a, b) in rook_moves(u, v)]
    return all(not two_rooks_P(*s) for s in succ)


# ------------------------------------------------------- coin row game ---
def coin_moves(coins):
    """coins: increasing square numbers 1..; the wall is left of square 1.
    Slide one coin left through empty squares (at least one), no jumping."""
    coins = tuple(coins)
    for i, c in enumerate(coins):
        lo = coins[i - 1] + 1 if i > 0 else 1
        for t in range(lo, c):
            yield coins[:i] + (t,) + coins[i + 1:]


@lru_cache(maxsize=None)
def coin_P(coins):
    """A player with no move loses."""
    return all(not coin_P(s) for s in coin_moves(coins))


# --------------------------------------------------- subtraction game ---
@lru_cache(maxsize=None)
def subtraction_P(n, moves=(1, 2, 3)):
    if n == 0:
        return True
    return all(not subtraction_P(n - m, moves) for m in moves if m <= n)
