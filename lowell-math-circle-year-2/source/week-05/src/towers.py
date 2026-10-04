"""Tower-city utilities: views, Latin squares, clue puzzles, uniqueness checks."""
from itertools import permutations, combinations
from collections import Counter

def view(seq):
    best, c = 0, 0
    for h in seq:
        if h > best:
            best, c = h, c + 1
    return c

def lr(seq):
    return (view(seq), view(seq[::-1]))

def latin_squares(n):
    rows = list(permutations(range(1, n + 1)))
    out = []
    def rec(sq):
        if len(sq) == n:
            out.append(tuple(sq)); return
        for r in rows:
            if all(r[c] != s[c] for s in sq for c in range(n)):
                rec(sq + [r])
    rec([])
    return out

def clues_of(sq):
    """All 4n clues: keys ('T',c) top of column c, ('B',c), ('L',r), ('R',r)."""
    n = len(sq)
    d = {}
    for c in range(n):
        col = [sq[r][c] for r in range(n)]
        d[('T', c)] = view(col)
        d[('B', c)] = view(col[::-1])
    for r in range(n):
        d[('L', r)] = view(sq[r])
        d[('R', r)] = view(sq[r][::-1])
    return d

_cache = {}
def all_with_clues(n):
    if n not in _cache:
        _cache[n] = [(sq, clues_of(sq)) for sq in latin_squares(n)]
    return _cache[n]

def solutions(n, clues, givens=None):
    givens = givens or {}
    res = []
    for sq, cl in all_with_clues(n):
        if all(cl[k] == v for k, v in clues.items()) and all(sq[r][c] == v for (r, c), v in givens.items()):
            res.append(sq)
    return res

def show(sq):
    return "\n".join(" ".join(map(str, r)) for r in sq)
