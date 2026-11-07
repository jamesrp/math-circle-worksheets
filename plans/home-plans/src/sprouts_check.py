#!/usr/bin/env python3
"""Check every fact in the Sprouts home plan (2026-11-08-sprouts.md).

    python3 plans/home-plans/src/sprouts_check.py        # spots 1 to 3, a few seconds

(4 spots did not finish in five minutes; the plan's facts about 4 or more are cited.)

A position is a list of regions. A region is a tuple of boundaries; a boundary is the
cyclic walk of spot names met going round one connected piece of the drawing. A spot that
appears twice in a walk has two corners in that region. A line joins two corners of one
region (or one corner to itself, for a loop): corners on different boundaries merge them;
two corners on one boundary split the region in two, and every other boundary of that
region goes to one side or the other (all choices are tried). The new spot sits in the
middle of the line with one life. Adapted from the independent engine in
plans/topic-scouting/drafts/games-decided-before-they-start/math-check/planar.py.
Normal play: whoever makes the last move wins.
"""
import sys
from functools import lru_cache

def rot(b, i):
    return b[i:] + b[:i]

LIVES = 3                               # line ends a spot may have

def start(n):
    return tuple([tuple((v,) for v in range(n))]), tuple([LIVES] * n)

def moves(regions, lives):
    w = len(lives)                      # name of the new spot
    out = []
    for ri, R in enumerate(regions):
        rest = regions[:ri] + regions[ri + 1:]
        corners = [(bi, pi) for bi, b in enumerate(R) for pi in range(len(b))]
        for x in range(len(corners)):
            for y in range(x, len(corners)):
                (bi, pi), (bj, pj) = corners[x], corners[y]
                u, v = R[bi][pi], R[bj][pj]
                if u == v and lives[u] < 2:
                    continue
                if lives[u] < 1 or lives[v] < 1:
                    continue
                nl = list(lives); nl[u] -= 1; nl[v] -= 1; nl.append(LIVES - 2)
                nl = tuple(nl)
                others = [R[k] for k in range(len(R)) if k not in (bi, bj)]
                if bi != bj:            # two pieces become one
                    A, B = rot(R[bi], pi), rot(R[bj], pj)
                    Aw = A + ((u,) if len(A) > 1 else ())
                    Bw = B + ((v,) if len(B) > 1 else ())
                    out.append((rest + (tuple(others) + (Aw + (w,) + Bw + (w,),),), nl))
                else:                   # the region splits in two
                    b = rot(R[bi], pi)
                    t = (pj - pi) % len(b)
                    if t == 0:          # a loop from one corner back to itself
                        s1 = (u, w)
                        s2 = (b if len(b) > 1 else ()) + (u, w)
                        if len(b) == 1:
                            s2 = (u, w)
                    else:
                        s1 = b[:t + 1] + (w,)
                        s2 = b[t:] + (b[0], w)
                    for mask in range(1 << len(others)):
                        g1 = tuple(others[k] for k in range(len(others)) if mask >> k & 1)
                        g2 = tuple(others[k] for k in range(len(others)) if not mask >> k & 1)
                        out.append((rest + (g1 + (s1,), g2 + (s2,)), nl))
    return out

def key(regions, lives):
    """Forget dead spots, then sort, so equal pictures share one entry."""
    rs = []
    for R in regions:
        bs = []
        for b in R:
            c = tuple(x for x in b if lives[x] > 0)
            if c:
                bs.append(min(rot(c, i) for i in range(len(c))))
        if bs:
            rs.append(tuple(sorted(bs)))
    return tuple(sorted(rs)), tuple((x, l) for x, l in enumerate(lives) if l > 0)

LEN, WIN = {}, {}

def lengths(regions, lives):
    k = key(regions, lives)
    if k not in LEN:
        ms = moves(regions, lives)
        LEN[k] = frozenset([0]) if not ms else frozenset(
            1 + x for r, l in ms for x in lengths(r, l))
    return LEN[k]

def mover_wins(regions, lives):
    k = key(regions, lives)
    if k not in WIN:
        WIN[k] = any(not mover_wins(r, l) for r, l in moves(regions, lives))
    return WIN[k]

def joins(regions, lives, u, v):
    """The moves that draw a line between spots u and v (any way round)."""
    out = []
    for r2, l2 in moves(regions, lives):
        used = [x for x in range(len(lives)) if l2[x] < lives[x]]
        if sorted(used) == sorted({u, v}) and (u != v or lives[u] - l2[u] == 2):
            out.append((r2, l2))
    return out

def game_exists(n, pairs):
    """Can the game be played with these joins, in order, and then be over?"""
    def go(r, l, i):
        if i == len(pairs):
            return not moves(r, l)
        return any(go(r2, l2, i + 1) for r2, l2 in joins(r, l, *pairs[i]))
    return go(*start(n), 0)

def main():
    top = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    sys.setrecursionlimit(100000)
    expect_len = {1: {2}, 2: {4, 5}, 3: {6, 7, 8}, 4: set(range(8, 12))}
    expect_first_wins = {1: False, 2: False, 3: True, 4: True}
    for n in range(1, top + 1):
        r, l = start(n)
        L = lengths(r, l)
        f = mover_wins(r, l)
        print(f"{n} spot(s): game lengths {sorted(L)}; 3n-1 = {3*n-1}, 2n = {2*n}; "
              f"first player wins with best play: {f}")
        assert set(L) == expect_len[n], L
        assert max(L) == 3 * n - 1 and min(L) == 2 * n
        assert f == expect_first_wins[n]
        # Every length between the bounds occurs, and moves = 3n - lives left at the end.
        assert set(L) == set(range(2 * n, 3 * n))
    # Lives bookkeeping: every move lowers the total by exactly one, in every reachable
    # position of the 2-spot game, and a finished game has every survivor at one life.
    seen, stack = set(), [start(2)]
    while stack:
        r, l = stack.pop()
        k = key(r, l)
        if k in seen:
            continue
        seen.add(k)
        ms = moves(r, l)
        if not ms:
            assert all(x <= 1 for x in l), l
        for r2, l2 in ms:
            assert sum(l2) == sum(l) - 1
            stack.append((r2, l2))
    print("lives drop by one each move; at the end every spot left alive has one life")
    # The plan's example games. Spots are named in order: A=0, B=1, then each new spot.
    A, B, C, D, E, F = range(6)
    # The picture: A-B (C), then a loop on A (D) kills A.
    r, l = joins(*start(2), A, B)[0]
    assert l == (2, 2, 1)
    r, l = joins(r, l, A, A)[0]
    assert l == (0, 2, 1, 1)
    # A 5-move game (one life left) and a 4-move game (two left) from the same start.
    assert game_exists(2, [(A, B), (A, B), (A, C), (E, B), (D, F)])
    assert game_exists(2, [(A, B), (A, A), (B, C), (B, E)])
    print("example games: the picture's moves, a 5-move and a 4-move 2-spot game")
    # Your strategy going second on 2 spots always makes the 4th and last move.
    r1, l1 = joins(*start(2), A, B)[0]
    rings = [(r, l) for r, l in joins(r1, l1, A, B) if len(r) == 2]   # round the other way
    assert len(rings) == 1
    ring = rings[0]
    for r3, l3 in moves(*ring):        # they join two of the four ring spots
        used = {x for x in range(4) if l3[x] < ring[1][x]}
        z, w = sorted(set(range(4)) - used)
        assert any(not moves(r4, l4) for r4, l4 in joins(r3, l3, z, w)), used
    for first in (A, B):               # they loop a spot; the new spot is C
        other = B if first == A else A
        r1, l1 = joins(*start(2), first, first)[0]
        ok = [(r, l) for r, l in joins(r1, l1, first, C)
              if not any(other in sum(R, ()) and D in sum(R, ()) for R in r)
              and lengths(r, l) == {2}]
        assert ok
    print("strategy: going second on 2 spots, the ring reply and the shut-away reply win")
    # With 4 lives a spot, a new spot keeps 2 and the newest spot can loop for ever.
    global LIVES
    LIVES = 4
    r, l = start(1)
    for i in range(40):
        newest = len(l) - 1
        r, l = joins(r, l, newest, newest)[0]
        assert sum(l) == 4
    LIVES = 3
    print("4 lives: forty loops in a row on the newest spot, total lives stays 4")
    print("all checks passed")

if __name__ == "__main__":
    main()
