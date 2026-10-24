"""Chomp checker. A position is a tuple of row lengths, bottom row first
(the poison is row 1, column 1), non-increasing, trailing zeros removed.
A bite at (r, c) (1-based) cuts every row i >= r to length min(len, c-1).
The bite at (1,1) eats the poison and loses, so we never consider it as a
move; the position (1,) (only the poison) is lost for the player to move."""
from functools import lru_cache

def norm(rows):
    rows = list(rows)
    while rows and rows[-1] == 0:
        rows.pop()
    return tuple(rows)

def moves(pos):
    out = []
    for r in range(len(pos)):
        for c in range(pos[r]):
            if r == 0 and c == 0:
                continue
            new = list(pos)
            for i in range(r, len(pos)):
                new[i] = min(new[i], c)
            out.append(((r + 1, c + 1), norm(new)))
    return out

@lru_cache(maxsize=None)
def win(pos):
    """True if the player to move can force the opponent to eat the poison."""
    return any(not win(q) for _, q in moves(pos))

def winning_moves(pos):
    return [(m, q) for m, q in moves(pos) if not win(q)]

def rect(rows, cols):
    return tuple([cols] * rows)

def positions_in_box(rows, cols):
    """All non-empty Young diagrams (with the poison) fitting in rows x cols."""
    res = []
    def rec(prefix, maxlen):
        if len(prefix) == rows:
            p = norm(prefix)
            if p:
                res.append(p)
            return
        for L in range(maxlen, -1, -1):
            rec(prefix + [L], L)
    rec([], cols)
    return sorted(set(res), key=lambda p: (sum(p), p))

if __name__ == "__main__":
    import sys
    # Rectangles
    for r in range(1, 5):
        for c in range(1, 8):
            pos = rect(r, c)
            if pos == (1,):
                continue
            wm = winning_moves(pos)
            print(f"{r} rows x {c} cols: first player wins={win(pos)}; winning bites (row,col)->rows:",
                  [(m, q) for m, q in wm])
    # Two-row P positions
    p2 = [p for p in positions_in_box(2, 12) if not win(p)]
    print("two-row losing positions up to length 12:", p2)
    ok = all((len(p) == 1 and p == (1,)) or (len(p) == 2 and p[1] == p[0] - 1) for p in p2)
    print("rule 'top = bottom - 1' matches:", ok)
    # L shapes: rows (a+1, 1, 1, ... b times)
    for a in range(0, 5):
        for b in range(0, 5):
            pos = norm([a + 1] + [1] * b)
            print(f"L arms right={a} up={b}: mover wins={win(pos)}")
