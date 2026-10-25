#!/usr/bin/env python3
"""Independent checks for every answer printed in the facilitator guide
for "Breaking and drawing games" (outline: "Games decided before they start").

Written for the guide, against the final student pages
(k-1.pdf 7 pp., grades-2-3.pdf 7 pp., grades-4-5.pdf 9 pp.).

Sections
  1. Bars: every break order, winners, the K-1 Problem 8 groups.
  2. A planar game engine (faces as boundary walks), used exhaustively for
     2-Sprigs (1-6 dots), Sprouts (1-3 spots), Brussels Sprouts (1-2 crosses)
     and 3-Sprigs (2-5 dots, extension only).
  3. Abstract models for larger boards: 2-Sprigs up to 25 dots, Brussels
     Sprouts by component sizes.
  4. Sprouts: cooperative longest games (3n-1) and shortest games (2n),
     including 10 spots; the example games printed in the guide.
  5. Grades 4-5 Problem 11 drawings: dots, lines, regions by rasterizing the
     TikZ coordinates of the page; the finished 1-cross game.
  6. Boards and materials: board spacings from the pages; the bars and the
     2-spot Sprouts boards read from the delivered materials.pdf (kit stage),
     the per-pair and per-table allocation, totals and trimmer cuts.
Revision (final/): adds the explicit 8-move 3-spot game, the counterexample to
"never shut a spot in alone", the Brussels regions-minus-pieces count, the
K-1 Problem 8 alternative source bars, and the materials-file checks.
Set MATERIALS_PDF to check a packaged copy of materials.pdf elsewhere.
Every check asserts; the script stops at the first failure.
"""
import itertools
import random
import re
import sys
from functools import lru_cache

sys.setrecursionlimit(100000)
OK = []


def ok(msg):
    OK.append(msg)
    print("ok  " + msg, flush=True)


# ---------------------------------------------------------------- 1. bars
@lru_cache(maxsize=None)
def break_counts(a, b):
    """Set of possible numbers of breaks splitting an a-by-b bar into squares,
    over every order (one piece per break, full straight grid line)."""
    if a == 1 and b == 1:
        return frozenset([0])
    out = set()
    for c in range(1, a):
        for x in break_counts(c, b):
            for y in break_counts(a - c, b):
                out.add(1 + x + y)
    for c in range(1, b):
        for x in break_counts(a, c):
            for y in break_counts(a, b - c):
                out.add(1 + x + y)
    return frozenset(out)


def pieces_key(pieces):
    return tuple(sorted(tuple(sorted(p)) for p in pieces if p != (1, 1)))


@lru_cache(maxsize=None)
def first_player_wins_bars(key):
    """Normal play: whoever makes the last break wins."""
    pieces = list(key)
    for i, (a, b) in enumerate(pieces):
        rest = pieces[:i] + pieces[i + 1:]
        for c in range(1, a):
            if not first_player_wins_bars(pieces_key(rest + [(c, b), (a - c, b)])):
                return True
        for c in range(1, b):
            if not first_player_wins_bars(pieces_key(rest + [(a, c), (a, b - c)])):
                return True
    return False


def can_split(bar, pieces):
    """Can the multiset `pieces` (rotations allowed) be broken from `bar`?"""
    a, b = bar
    norm = lambda p: tuple(sorted(p))
    pieces = sorted(norm(p) for p in pieces)
    if sum(x * y for x, y in pieces) != a * b:
        return False
    if len(pieces) == 1:
        return pieces[0] == norm(bar)
    for c in range(1, a):
        for r in range(1, len(pieces)):
            for sub in set(itertools.combinations(pieces, r)):
                rest = list(pieces)
                for s in sub:
                    rest.remove(s)
                if can_split((c, b), sub) and can_split((a - c, b), rest):
                    return True
    for c in range(1, b):
        for r in range(1, len(pieces)):
            for sub in set(itertools.combinations(pieces, r)):
                rest = list(pieces)
                for s in sub:
                    rest.remove(s)
                if can_split((a, c), sub) and can_split((a, b - c), rest):
                    return True
    return False


def apply_breaks(bar, seq):
    """Apply a written break sequence: (piece, (cut piece 1, cut piece 2))."""
    pieces = [tuple(bar)]
    for p, (q, r) in seq:
        pieces.remove(p)
        assert (q[0] == r[0] == p[0] and q[1] + r[1] == p[1]) or \
               (q[1] == r[1] == p[1] and q[0] + r[0] == p[0]), (p, q, r)
        pieces += [q, r]
    return pieces


def check_bars():
    printed = {  # bar: breaks printed in the guide
        (2, 2): 3, (2, 3): 5, (1, 6): 5, (3, 4): 11, (3, 3): 8, (2, 4): 7,
        (4, 5): 19, (3, 5): 14, (5, 5): 24, (1, 9): 8, (6, 6): 35,
        (7, 9): 62, (8, 13): 103, (25, 40): 999}
    for (a, b), k in printed.items():
        s = break_counts(a, b)
        assert s == {k} == {a * b - 1}, (a, b, s)
    ok("bars: every order gives squares-1 breaks: " +
       ", ".join(f"{a}x{b}:{k}" for (a, b), k in printed.items()))
    winners = {(3, 3): False, (2, 4): True, (2, 3): True, (4, 5): True,
               (3, 5): False, (5, 5): False, (1, 9): False, (6, 6): True}
    for bar, w in winners.items():
        assert first_player_wins_bars(pieces_key([bar])) == w, bar
        assert ((bar[0] * bar[1] - 1) % 2 == 1) == w
    ok("last break wins (game search): 1st wins 2x4, 2x3, 4x5, 6x6; 2nd wins 3x3, 3x5, 5x5, 1x9")
    for bar, w in {(7, 9): False, (8, 13): True, (25, 40): True}.items():
        assert ((bar[0] * bar[1] - 1) % 2 == 1) == w
    ok("parity: 7x9 2nd (62), 8x13 1st (103), 25x40 1st (999)")
    two = pieces_key([(2, 3), (2, 4)])
    assert first_player_wins_bars(two) is False
    assert 6 + 8 - 2 == 12
    ok("2x3 and 2x4 together: 12 breaks, 2nd player wins (game search agrees)")
    # stacking extension: 3x4 in 4 cuts, and 3 cuts give at most 8 pieces
    assert 2 ** 3 < 12 <= 2 ** 4
    ok("stacking extension: 4 cuts for 3x4 (3 cuts make at most 8 pieces)")

    # K-1 Problem 8: pieces read from k-1.tex, \piece{rows}{cols}
    groups = [((2, 3), [(2, 2), (1, 1), (1, 1)]),
              ((3, 3), [(3, 1), (1, 2), (2, 1), (1, 1), (1, 1)]),
              ((3, 4), [(1, 4), (2, 1), (1, 2), (1, 1), (1, 1), (1, 1), (1, 1)])]
    answers = [2, 4, 6]
    for (bar, ps), k in zip(groups, answers):
        assert can_split(bar, ps), bar
        assert len(ps) - 1 == k
        assert sum(x * y for x, y in ps) - 1 != k  # the squares-1 trap differs
    # the written break sequences in the guide
    s1 = [((2, 3), ((2, 2), (2, 1))), ((2, 1), ((1, 1), (1, 1)))]
    s2 = [((3, 3), ((3, 1), (3, 2))), ((3, 2), ((1, 2), (2, 2))),
          ((2, 2), ((2, 1), (2, 1))), ((2, 1), ((1, 1), (1, 1)))]
    s3 = [((3, 4), ((1, 4), (2, 4))), ((2, 4), ((2, 1), (2, 3))),
          ((2, 3), ((1, 3), (1, 3))), ((1, 3), ((1, 2), (1, 1))),
          ((1, 3), ((1, 1), (1, 2))), ((1, 2), ((1, 1), (1, 1)))]
    for (bar, ps), seq in zip(groups, [s1, s2, s3]):
        got = sorted(tuple(sorted(p)) for p in apply_breaks(bar, seq))
        assert got == sorted(tuple(sorted(p)) for p in ps), (bar, got)
    ok("K-1 P8: groups come from 2x3, 3x3, 3x4 bars; 2, 4, 6 breaks (trap 5, 8, 11); written sequences valid")
    # the source bar is not forced (the guide says "for example"): list every bar
    # of the right area that the pieces can be broken from
    srcs = []
    for bar, ps in groups:
        area = bar[0] * bar[1]
        srcs.append(sorted((a, area // a) for a in range(1, area + 1)
                           if area % a == 0 and a <= area // a and can_split((a, area // a), ps)))
    assert srcs == [[(2, 3)], [(1, 9), (3, 3)], [(1, 12), (2, 6), (3, 4)]], srcs
    ok("K-1 P8: possible source bars 2x3; 1x9 or 3x3; 1x12, 2x6 or 3x4 (so 'for example'); "
       "the answer pieces-1 does not depend on the bar")


# ------------------------------------------------------- 2. planar engine
class Game:
    """kind: 'sprigs' (L lives per dot, no new vertex), 'sprouts' (3 lives,
    new spot with 1 life on each curve), 'brussels' (crosses; free arms are
    pendant tips with 1 life; a move joins two tips and adds a cross whose
    two new arms point to opposite sides of the curve).

    A position is (faces, lives, deg). A face is a tuple of boundary
    components; a component is a cyclic tuple of corners (vertex labels),
    walked with the face on the left. An isolated vertex is one corner."""

    def __init__(self, kind, n, L=None):
        self.kind, self.n = kind, n
        self.L = L if L is not None else {"sprigs": 2, "sprouts": 3}.get(kind)

    def start(self):
        lives, deg, comps = {}, {}, []
        if self.kind in ("sprigs", "sprouts"):
            for v in range(self.n):
                lives[v], deg[v] = self.L, 0
                comps.append((v,))
        else:
            nxt = 0
            for _ in range(self.n):
                c = nxt; nxt += 1
                lives[c], deg[c] = 0, 4
                walk = []
                for _ in range(4):
                    t = nxt; nxt += 1
                    lives[t], deg[t] = 1, 1
                    walk += [c, t]
                comps.append(tuple(walk))
        return (tuple(comps),), lives, deg

    def legal(self, u, v, lives):
        if self.kind == "brussels":
            return u != v and lives[u] == 1 and lives[v] == 1
        if u == v:
            return lives[u] >= 2
        return lives[u] >= 1 and lives[v] >= 1

    def moves(self, faces, lives, deg):
        w = max(lives) + 1
        for fi, face in enumerate(faces):
            others = faces[:fi] + faces[fi + 1:]
            occ = [(ci, pi) for ci, comp in enumerate(face)
                   for pi in range(len(comp)) if lives[comp[pi]] >= 1]
            for a in range(len(occ)):
                for b in range(a, len(occ)):
                    (ci, pi), (cj, pj) = occ[a], occ[b]
                    u, v = face[ci][pi], face[cj][pj]
                    if not self.legal(u, v, lives):
                        continue
                    for nf, nl, nd in self.draw(face, ci, pi, cj, pj, lives, deg, w):
                        yield others + tuple(nf), nl, nd

    def draw(self, face, ci, pi, cj, pj, lives, deg, w):
        u, v = face[ci][pi], face[cj][pj]
        nl, nd = dict(lives), dict(deg)
        nl[u] -= 1; nl[v] -= 1; nd[u] += 1; nd[v] += 1
        if self.kind == "sprigs":
            m1 = m2 = ()
        elif self.kind == "sprouts":
            nl[w], nd[w] = 1, 2
            m1 = m2 = (w,)
        else:
            b1, b2 = w + 1, w + 2
            nl[w], nd[w] = 0, 4
            nl[b1], nd[b1], nl[b2], nd[b2] = 1, 1, 1, 1
            m1, m2 = (w, b1, w), (w, b2, w)
        rot = lambda comp, p: comp[p:] + comp[:p]
        rest = [face[k] for k in range(len(face)) if k not in (ci, cj)]
        if ci != cj:  # join two boundary components: the face does not split
            A, B = rot(face[ci], pi), rot(face[cj], pj)
            new = ((u,) + m1 + (v,) + B[1:] + ((v,) if deg[v] else ()) + m2 +
                   ((u,) if deg[u] else ()) + A[1:])
            yield [tuple(rest) + (new,)], nl, nd
            return
        S = rot(face[ci], pi)
        if pi == pj:  # loop drawn inside one corner
            f1 = (u,) + m1
            f2 = (u,) + m2 + (((u,) + S[1:]) if deg[u] else ())
        else:
            t = (pj - pi) % len(S)
            f1 = S[:t + 1] + m1
            f2 = S[t:] + (S[0],) + m2
        for mask in range(1 << len(rest)):
            g1 = tuple(rest[r] for r in range(len(rest)) if mask >> r & 1)
            g2 = tuple(rest[r] for r in range(len(rest)) if not mask >> r & 1)
            yield [g1 + (f1,), g2 + (f2,)], nl, nd


def canon(faces, lives):
    """Sound memo key: drop dead corners, sort by label-free signatures,
    relabel live vertices in order of first appearance (a bijection, so equal
    keys mean isomorphic positions). Lives fix the degree information the
    engine needs (untouched spot <-> full lives; tips always degree 1)."""
    fl = []
    for f in faces:
        cs = []
        for c in f:
            c2 = tuple(x for x in c if lives[x] > 0)
            if c2:
                pats = [tuple(lives[x] for x in c2[r:] + c2[:r]) for r in range(len(c2))]
                r = min(range(len(c2)), key=lambda r: pats[r])
                cs.append((pats[r], c2[r:] + c2[:r]))
        if cs:
            cs.sort(key=lambda t: t[0])
            fl.append((tuple(t[0] for t in cs), [t[1] for t in cs]))
    fl.sort(key=lambda t: t[0])
    lab = {}
    out = []
    for sig, cs in fl:
        out.append(tuple(tuple((lab.setdefault(x, len(lab)), lives[x]) for x in c) for c in cs))
    return tuple(out)


def lengths(game):
    memo = {}

    def rec(faces, lives, deg):
        k = canon(faces, lives)
        if k in memo:
            return memo[k]
        res = set()
        for nf, nl, nd in game.moves(faces, lives, deg):
            res |= {1 + x for x in rec(nf, nl, nd)}
        if not res:
            res = {0}
        memo[k] = frozenset(res)
        return memo[k]
    return set(rec(*game.start()))


def lengths_from(game, st):
    """Possible numbers of further moves from position st."""
    memo = {}

    def rec(faces, lives, deg):
        k = canon(faces, lives)
        if k in memo:
            return memo[k]
        res = set()
        for nf, nl, nd in game.moves(faces, lives, deg):
            res |= {1 + x for x in rec(nf, nl, nd)}
        memo[k] = frozenset(res) if res else frozenset([0])
        return memo[k]
    return set(rec(*st))


def drawing_pieces(faces):
    """Number of separate pieces of the drawing: vertices next to each other on
    a boundary walk are joined by a line."""
    parent = {}

    def find(x):
        parent.setdefault(x, x)
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for f in faces:
        for c in f:
            for i in range(len(c)):
                a, b = find(c[i]), find(c[(i + 1) % len(c)])
                parent[a] = b
    return len({find(x) for x in parent})


def first_player_wins(game):
    memo = {}

    def win(faces, lives, deg):
        k = canon(faces, lives)
        if k in memo:
            return memo[k]
        res = any(not win(nf, nl, nd) for nf, nl, nd in game.moves(faces, lives, deg))
        memo[k] = res
        return res
    return win(*game.start())


def check_engine():
    for n in range(1, 7):
        L = lengths(Game("sprigs", n))
        assert L == {n}, (n, L)
    ok("2-Sprigs exhaustive, 1-6 dots: every game lasts exactly n moves")
    exp = {1: {2}, 2: {4, 5}, 3: {6, 7, 8}}
    for n, e in exp.items():
        L = lengths(Game("sprouts", n))
        assert L == e, (n, L)
    ok("Sprouts exhaustive: 1 spot {2}; 2 spots {4,5}; 3 spots {6,7,8}")
    for n, w in {1: False, 2: False, 3: True}.items():
        assert first_player_wins(Game("sprouts", n)) == w
    ok("Sprouts best play: 1 and 2 spots 2nd player, 3 spots 1st player")
    for n in (1, 2):
        L = lengths(Game("brussels", n))
        assert L == {5 * n - 2}, (n, L)
    ok("Brussels Sprouts exhaustive: 1 cross {3}, 2 crosses {8}")
    exp3 = {2: {3}, 3: {4}, 4: {5, 6}, 5: {6, 7}}
    for n, e in exp3.items():
        L = lengths(Game("sprigs", n, L=3))
        assert L == e, (n, L)
    ok("3-Sprigs (extension): 2 dots {3}, 3 dots {4}, 4 dots {5,6}, 5 dots {6,7}")


# --------------------------------------------------- 3. abstract models
def sprigs_abstract(n):
    """Faces as (isolated dots, open paths). Uses the lemma that both ends
    of a path border the same face."""
    @lru_cache(maxsize=None)
    def rec(state):
        res = set()
        st = list(state)
        for k, (i, p) in enumerate(st):
            rest = st[:k] + st[k + 1:]

            def go(newfaces):
                s = tuple(sorted([f for f in rest + newfaces if f != (0, 0)]))
                for x in rec(s):
                    res.add(1 + x)
            if i >= 1:  # loop at an untouched dot: splits the face
                for i1 in range(i):
                    for p1 in range(p + 1):
                        go([(i1, p1), (i - 1 - i1, p - p1)])
            if i >= 2:
                go([(i - 2, p + 1)])
            if i >= 1 and p >= 1:
                go([(i - 1, p)])
            if p >= 2:
                go([(i, p - 1)])
            if p >= 1:  # close a path into a loop: splits the face
                for i1 in range(i + 1):
                    for p1 in range(p):
                        go([(i1, p1), (i - i1, p - 1 - p1)])
        return frozenset(res) if res else frozenset([0])
    return set(rec(((n, 0),)))


def brussels_abstract(n):
    """Faces as multisets of component sizes (free arms on each boundary
    walk). Joining arms on two walks merges them (sizes add: -2 used, +2
    new). Joining two arms on one walk of size c splits the face into walks
    of sizes t and c-t (each side gains one new arm), 1 <= t <= c-1."""
    @lru_cache(maxsize=None)
    def rec(state):
        res = set()
        st = list(state)
        for k, face in enumerate(st):
            rest = st[:k] + st[k + 1:]
            comps = list(face)

            def go(newfaces):
                fs = [tuple(sorted(f)) for f in newfaces]
                s = tuple(sorted([f for f in rest + fs if sum(f) >= 2] +
                                 [f for f in rest + fs if sum(f) < 2]))
                s = tuple(sorted(s))
                for x in rec(s):
                    res.add(1 + x)
            for a in range(len(comps)):
                for b in range(a + 1, len(comps)):
                    others = comps[:a] + comps[a + 1:b] + comps[b + 1:]
                    go([others + [comps[a] + comps[b]]])
            for a in range(len(comps)):
                c = comps[a]
                others = comps[:a] + comps[a + 1:]
                for t in range(1, c):
                    for mask in range(1 << len(others)):
                        g1 = [others[r] for r in range(len(others)) if mask >> r & 1]
                        g2 = [others[r] for r in range(len(others)) if not mask >> r & 1]
                        go([g1 + [t], g2 + [c - t]])
        return frozenset(res) if res else frozenset([0])
    return set(rec(((4,) * n,)))


def check_abstract():
    for n in list(range(1, 13)) + [25]:
        L = sprigs_abstract(n)
        assert L == {n}, (n, L)
    ok("2-Sprigs face model: exactly n moves for 1-12 and 25 dots (10 dots: 2nd wins; 25: 1st)")
    for n in range(1, 6):
        L = brussels_abstract(n)
        assert L == {5 * n - 2}, (n, L)
    ok("Brussels face model: 1-5 crosses last exactly 3, 8, 13, 18, 23 moves")
    rng = random.Random(1)
    for n in (1, 2, 3, 4):
        g = Game("brussels", n)
        for _ in range(300 if n < 4 else 60):
            st = g.start()
            m = 0
            assert len(st[0]) - drawing_pieces(st[0]) == 1 - n
            while True:
                opts = list(g.moves(*st))
                if not opts:
                    break
                st = rng.choice(opts)
                m += 1
                assert len(st[0]) - drawing_pieces(st[0]) == 1 - n + m
            # finished: one piece, 4n regions, one free arm in each
            assert drawing_pieces(st[0]) == 1 and len(st[0]) == 4 * n and m == 5 * n - 2
            for f in st[0]:
                assert sum(1 for c in f for x in c if st[1][x] == 1) == 1
    ok("Brussels random games (1-4 crosses): regions minus pieces of the drawing starts at 1-n, "
       "rises by exactly 1 each move, ends at 4n-1 with the drawing in one piece, one free arm per region")


# ------------------------------------------------------------ 4. Sprouts
def live_total(lives):
    return sum(l for l in lives.values() if l > 0)


def all_live_in_one_face(faces, lives):
    live = {v for v, l in lives.items() if l > 0}
    return any(live <= {x for c in f for x in c} for f in faces)


def cooperative_long(n, seed=0):
    """Keep every spot with a life on the edge of one region."""
    rng = random.Random(seed)
    g = Game("sprouts", n)
    faces, lives, deg = g.start()
    m = 0
    while True:
        opts = []
        for nf, nl, nd in g.moves(faces, lives, deg):
            if all_live_in_one_face(nf, nl):
                opts.append((nf, nl, nd))
                if len(opts) > 40:
                    break
        if not opts:
            assert not any(True for _ in g.moves(faces, lives, deg))
            return m, live_total(lives)
        faces, lives, deg = rng.choice(opts)
        m += 1


def shortest_by_pattern(n):
    """For each original spot: loop, then join the spot to the loop's new
    spot inside the loop. Two moves per spot."""
    g = Game("sprouts", n)
    faces, lives, deg = g.start()
    m = 0
    for s in range(n):
        # move 1: loop at s with nothing else inside
        found = None
        for nf, nl, nd in g.moves(faces, lives, deg):
            if nl[s] == 1 and max(nl) == max(lives) + 1 and nd[s] == 2:
                w = max(nl)
                if any(set(x for c in f for x in c) == {s, w} for f in nf):
                    found = (nf, nl, nd, w)
                    break
        faces, lives, deg, w = found
        m += 1
        # move 2: join s and w inside that face
        found = None
        for nf, nl, nd in g.moves(faces, lives, deg):
            if nl[s] == 0 and nl[w] == 0:
                found = (nf, nl, nd)
                break
        faces, lives, deg = found
        m += 1
    assert not any(True for _ in g.moves(faces, lives, deg)), "game should be over"
    return m


def check_sprouts():
    for n in (2, 3, 4, 10):
        m, left = cooperative_long(n)
        assert m == 3 * n - 1 and left == 1, (n, m, left)
    ok("Sprouts cooperative strategy reaches 3n-1: 5, 8, 11 and 29 moves for 2, 3, 4, 10 spots")
    for n in (1, 2, 3, 10):
        assert shortest_by_pattern(n) == 2 * n
    ok("Sprouts loop-then-join pattern ends after 2n moves: 2, 4, 6, 20")
    # the example games printed in the guide, replayed move by move
    # labels: A=0, B=1, new spots 2, 3, 4, ... in order (C, D, E, ...)
    def step(g, st, pred):
        for nxt in g.moves(*st):
            if pred(st, nxt):
                return nxt
        raise AssertionError("move not found")

    def share(faces, x, y):
        return any(x in {v for c in f for v in c} and y in {v for c in f for v in c} for f in faces)

    def alone(faces, lives, x):
        return all(not any(lives[v] > 0 and v != x for c in f for v in c)
                   for f in faces if x in {v for c in f for v in c})

    g = Game("sprouts", 1)
    st = g.start()
    st = step(g, st, lambda a, b: b[1][0] == 1)                    # A loops (B)
    st = step(g, st, lambda a, b: b[1][0] == 0 and b[1][1] == 0)   # A-B (C)
    assert not any(True for _ in g.moves(*st))
    ok("1 spot: loop, then join the two spots; the third spot is alone: 2 moves")

    g = Game("sprouts", 2)
    st = g.start()
    st = step(g, st, lambda a, b: b[1][0] == 2 and b[1][1] == 2)   # 1. A-B (C)
    st = step(g, st, lambda a, b: b[1][0] == 1 and b[1][1] == 1)   # 2. A-B again: ring (D)
    st = step(g, st, lambda a, b: b[1][0] == 0 and b[1][2] == 0)   # 3. A-C inside (E)
    st = step(g, st, lambda a, b: b[1][1] == 0 and b[1][3] == 0 and share(b[0], 4, 5))  # 4. B-D (F)
    st = step(g, st, lambda a, b: b[1][4] == 0 and b[1][5] == 0)   # 5. E-F (G)
    assert not any(True for _ in g.moves(*st)) and live_total(st[1]) == 1
    ok("2-spot long example: A-B, A-B (ring), A-C, B-D beside E, E-F: 5 moves, 1st player wins")

    st = g.start()
    st = step(g, st, lambda a, b: b[1][0] == 1 and
              any({v for c in f for v in c} == {0, 2} for f in b[0]))   # 1. A loops (C)
    st = step(g, st, lambda a, b: b[1][0] == 0 and b[1][2] == 0 and alone(b[0], b[1], 3))  # 2. A-C (D)
    st = step(g, st, lambda a, b: b[1][1] == 1)                         # 3. B loops (E)
    st = step(g, st, lambda a, b: b[1][1] == 0 and b[1][4] == 0)        # 4. B-E (F)
    assert not any(True for _ in g.moves(*st)) and live_total(st[1]) == 2
    ok("2-spot short example: A loops, A-C inside, B loops, B-E: 4 moves, 2nd player wins")

    # Grades 2-3 Problem 8 (and 4-5 Problem 7): an explicit 8-move 3-spot game.
    # A=0, B=1, C=2; new spots D=3, E=4, F=5, G=6, H=7, I=8, J=9, K=10.
    # Every move keeps all spots with a token on the edge of one region.
    g = Game("sprouts", 3)
    st = g.start()
    seq = [(0, 1), (1, 2), (0, 2), (0, 3), (6, 1), (7, 4), (8, 2), (9, 5)]
    for k, (x, y) in enumerate(seq, 1):
        st = step(g, st, lambda a, b, x=x, y=y: b[1][x] == a[1][x] - 1 - (x == y) and
                  b[1][y] == a[1][y] - 1 - (x == y) and all_live_in_one_face(b[0], b[1]))
        if k == 3:  # A-C closes the ring A-D-B-E-C-F: two regions
            assert len(st[0]) == 2
    assert not any(True for _ in g.moves(*st)) and live_total(st[1]) == 1
    assert [v for v, l in st[1].items() if l > 0] == [10]
    # the other side of the ring is untouched: a region bounded by exactly A, D, B, E, C, F
    assert any({x for c in f for x in c} == {0, 1, 2, 3, 4, 5} for f in st[0])
    ok("3-spot 8-move game: A-B (D); B-C (E); A-C (F) closes a ring; on one side A-D (G), G-B (H), "
       "H-E (I), I-C (J), J-F (K); game over, only K keeps a token")

    # 'Never shut a spot with a token in alone' is not enough for 3n-1:
    # A-B (D); A-B again round C (E); D-E on the side of the ring away from C (F).
    def shut_alone(faces, lives):
        return any(l == 1 and alone(faces, lives, v) for v, l in lives.items())

    st = g.start()
    st = step(g, st, lambda a, b: b[1][0] == 2 and b[1][1] == 2)                         # A-B (D)
    assert not shut_alone(st[0], st[1])
    st = step(g, st, lambda a, b: b[1][0] == 1 and b[1][1] == 1)   # A-B (E): a ring with C on one side
    assert not shut_alone(st[0], st[1]) and len(st[0]) == 2
    st = step(g, st, lambda a, b: b[1][3] == 0 and b[1][4] == 0 and
              not any({2, 5} <= {x for c in f for x in c} for f in b[0]))                # D-E away from C (F)
    assert not shut_alone(st[0], st[1]) and not all_live_in_one_face(st[0], st[1])
    rest = lengths_from(g, st)
    assert {3 + x for x in rest} == {6, 7}, rest
    ok("counterexample: A-B, A-B round C, D-E away from C shuts no spot in alone, "
       "yet every continuation ends after 6 or 7 moves, not 8")


# ------------------------------------------------- 5. Problem 11 drawings
def bezier(p0, p1, p2, p3, k=400):
    pts = []
    for i in range(k + 1):
        t = i / k
        s = 1 - t
        pts.append((s ** 3 * p0[0] + 3 * s * s * t * p1[0] + 3 * s * t * t * p2[0] + t ** 3 * p3[0],
                    s ** 3 * p0[1] + 3 * s * s * t * p1[1] + 3 * s * t * t * p2[1] + t ** 3 * p3[1]))
    return pts


def seg(p, q, k=200):
    return [(p[0] + (q[0] - p[0]) * i / k, p[1] + (q[1] - p[1]) * i / k) for i in range(k + 1)]


def regions(polylines, res=0.1, pad=6):
    """Count connected regions of the plane minus the drawing (outside
    included) by rasterizing at `res` mm per pixel."""
    import numpy as np
    from collections import deque
    xs = [x for pl in polylines for x, _ in pl]
    ys = [y for pl in polylines for _, y in pl]
    x0, y0 = min(xs) - pad, min(ys) - pad
    W = int((max(xs) + pad - x0) / res) + 1
    H = int((max(ys) + pad - y0) / res) + 1
    grid = np.zeros((H, W), dtype=np.int32)
    for pl in polylines:
        for (ax, ay), (bx, by) in zip(pl, pl[1:]):
            steps = int(max(abs(bx - ax), abs(by - ay)) / (res / 3)) + 1
            for i in range(steps + 1):
                x = ax + (bx - ax) * i / steps
                y = ay + (by - ay) * i / steps
                cx, cy = int((x - x0) / res), int((y - y0) / res)
                grid[max(cy - 1, 0):cy + 2, max(cx - 1, 0):cx + 2] = -1
    lab = 0
    for sy in range(H):
        for sx in range(W):
            if grid[sy, sx] == 0:
                lab += 1
                grid[sy, sx] = lab
                dq = deque([(sy, sx)])
                while dq:
                    y, x = dq.popleft()
                    for ny, nx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
                        if 0 <= ny < H and 0 <= nx < W and grid[ny, nx] == 0:
                            grid[ny, nx] = lab
                            dq.append((ny, nx))
    return lab, (lambda p: int(grid[int((p[1] - y0) / res), int((p[0] - x0) / res)])), grid


def crossings(curves):
    """Pairs of distinct curves whose polylines intersect away from shared
    endpoints (endpoints within 0.3 mm count as shared)."""
    def inter(p1, p2, p3, p4):
        d = lambda a, b, c: (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
        d1, d2, d3, d4 = d(p3, p4, p1), d(p3, p4, p2), d(p1, p2, p3), d(p1, p2, p4)
        return (d1 * d2 < 0) and (d3 * d4 < 0)
    bad = []
    names = list(curves)
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            A, B = curves[names[i]], curves[names[j]]
            ends = [A[0], A[-1], B[0], B[-1]]
            for a1, a2 in zip(A, A[1:]):
                for b1, b2 in zip(B, B[1:]):
                    near = any(min((q[0] - e[0]) ** 2 + (q[1] - e[1]) ** 2 for q in (a1, a2, b1, b2)) < 0.09
                               for e in ends)
                    if not near and inter(a1, a2, b1, b2):
                        bad.append((names[i], names[j]))
                        break
                else:
                    continue
                break
    return bad


def check_drawings():
    # Drawing 1 (tree): \draw (0,-7)--(12,0)--(24,0); (12,0)--(12,13); (24,0)--(24,-12)
    d1 = [seg((0, -7), (12, 0)), seg((12, 0), (24, 0)), seg((12, 0), (12, 13)), seg((24, 0), (24, -12))]
    F1 = regions(d1)[0]
    # Drawing 2: square with a diagonal
    sq = [(0, 0), (20, 0), (20, 20), (0, 20)]
    d2 = [seg(sq[i], sq[(i + 1) % 4]) for i in range(4)] + [seg((0, 0), (20, 20))]
    F2 = regions(d2)[0]
    # Drawing 3: lens and a loop
    d3 = [bezier((0, 0), (6, 9), (14, 9), (20, 0)), bezier((0, 0), (6, -9), (14, -9), (20, 0)),
          bezier((20, 0), (33, 12), (33, -12), (20, 0))]
    F3 = regions(d3)[0]
    # Drawing 4: finished 1-cross game (coordinates from grades-4-5.tex)
    c1 = bezier((0, 4.5), (0, 21), (21, 0), (4.5, 0))
    c2 = bezier((0, -4.5), (0, -21), (-21, 0), (-4.5, 0))
    c3 = (bezier((11.62, 11.62), (16.6, 16.6), (27, 11), (27, 0)) +
          bezier((27, 0), (27, -17), (17, -27), (0, -27))[1:] +
          bezier((0, -27), (-13, -27), (-17, -17), (-11.62, -11.62))[1:])
    arms_O = [seg((-4.5, 0), (4.5, 0)), seg((0, -4.5), (0, 4.5))]
    bar1 = seg((5.26, 5.26), (11.62, 11.62))
    bar2 = seg((-5.26, -5.26), (-11.62, -11.62))
    bar3 = seg((22.5, 0), (31.5, 0))
    # the bars sit at the middle of their curves
    mid = lambda pl: pl[len(pl) // 2]
    for c, b in ((c1, bar1), (c2, bar2)):
        m = mid(c)
        cx, cy = (b[0][0] + b[-1][0]) / 2, (b[0][1] + b[-1][1]) / 2
        assert abs(m[0] - cx) < 0.05 and abs(m[1] - cy) < 0.05
    assert min(abs(x - 27) + abs(y) for x, y in c3) < 0.05
    # no curve crosses another curve or a bar (bars cross only their own curve)
    bad = crossings({"c1": c1, "c2": c2, "c3": c3, "bar2": bar2, "bar3a": seg((22.5, 0), (26.6, 0)),
                     "bar1in": seg((5.26, 5.26), (8.0, 8.0))})
    assert not bad, bad
    d4 = arms_O + [c1, c2, c3, bar1, bar2, bar3]
    F4, where, _ = regions(d4)
    # free arms: inner arm of bar 1, inner arm of bar 2, both arms of bar 3
    tips = {"bar1 inner": (5.26 - 0.6, 5.26 - 0.6), "bar2 inner": (-5.26 + 0.6, -5.26 + 0.6),
            "bar3 inner": (22.5 - 0.8, 0), "bar3 outer": (31.5 + 0.8, 0)}
    regs = {k: where(p) for k, p in tips.items()}
    counts = {(5, 4): F1, (4, 5): F2, (2, 3): F3, (4, 6): F4}
    assert (F1, F2, F3, F4) == (1, 3, 3, 4), (F1, F2, F3, F4)
    assert len(set(regs.values())) == 4 and all(r > 0 for r in regs.values()), regs
    for (V, E), F in counts.items():
        assert V - E + F == 2
    ok("P11 drawings: (dots, lines, regions) = (5,4,1), (4,5,3), (2,3,3), (4,6,4); V-E+F=2 each")
    ok("P11 drawing 4: legal (no crossings), 4 regions, one free arm in each, so the game is over")
    # finished games from Problem 9: V = n + m, E = 2m, F = 4n
    for n in (1, 2):
        m = 5 * n - 2
        assert (n + m) - 2 * m + 4 * n == 2
    ok("P9 finished games: 1 cross 4-6+4; 2 crosses 10-16+8; both give 2")
    for n, m in ((3, 13), (10, 48)):
        assert 5 * n - 2 == m
    ok("P10: 3 crosses 13 moves, 10 crosses 48")


def check_boards():
    """Dot layouts and board sizes as cited in the guide (from bmc.sty and the .tex)."""
    from math import dist
    L = {"two": [(-25, 0), (25, 0)], "three": [(-25, -21.65), (25, -21.65), (0, 21.65)],
         "four": [(-24, -24), (24, -24), (24, 24), (-24, 24)],
         "five": [(0, 31.66), (-33.29, 7.48), (-20.57, -31.66), (20.57, -31.66), (33.29, 7.48)],
         "sixwide": [(-45, -22.5), (0, -22.5), (45, -22.5), (-45, 22.5), (0, 22.5), (45, 22.5)],
         "sixtall": [(-21, -42), (21, -42), (-21, 0), (21, 0), (-21, 42), (21, 42)],
         "twospot": [(-22, 0), (22, 0)], "twospotwide": [(-42, 0), (42, 0)],
         "threespotbig": [(-48, -24), (48, -24), (0, 26)]}
    md = {k: min(dist(p, q) for p, q in itertools.combinations(v, 2)) for k, v in L.items()}
    assert min(md[k] for k in ("two", "three", "four", "five", "sixwide", "sixtall")) > 41
    assert abs(md["twospot"] - 44) < 1e-9 and abs(md["twospotwide"] - 84) < 1e-9
    assert round(md["threespotbig"]) == 69
    ok("boards: Sprigs dots at least 41 mm apart; 4-5 P6 spots 44 mm apart (91x96 board); "
       "2-3 P6-P7 spots 84 mm apart; 3-spot boards 69-96 mm")


import os
MATERIALS = os.environ.get(
    "MATERIALS_PDF",
    os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "materials.pdf"))


def read_materials(path=MATERIALS):
    """Bars (rows, cols) on each page of the delivered materials.pdf, read from
    the light-grey filled rectangles; spots and boards on page 3."""
    import pymupdf
    PT = 25.4 / 72
    doc = pymupdf.open(path)
    pages = []
    for page in doc:
        bars, spots, boards = [], [], []
        for d in page.get_drawings():
            r = d["rect"]
            w, h = r.width * PT, r.height * PT
            if d.get("fill") and all(abs(c - 0.9) < 0.02 for c in d["fill"]):
                rows, cols = round(h / 25), round(w / 25)
                assert abs(h - 25 * rows) < 0.5 and abs(w - 25 * cols) < 0.5, (w, h)
                bars.append(((r.x0 * PT, r.y0 * PT, r.x1 * PT, r.y1 * PT), (rows, cols)))
            elif d.get("fill") and all(c < 0.05 for c in d["fill"]) and w < 5:
                spots.append(((r.x0 + r.x1) / 2 * PT, (r.y0 + r.y1) / 2 * PT))
            elif d.get("color") and w > 150 and h > 80 and not d.get("fill"):
                boards.append((round(w), round(h)))
        pages.append({"bars": bars, "spots": spots, "boards": boards,
                      "text": page.get_text()})
    return pages


def guillotine_cuts(rects, region):
    """Fewest straight trimmer cuts that free every bar in `rects` from
    `region` (x0, y0, x1, y1), cutting only along full lines of the current
    piece and never through a bar."""
    eps = 0.01

    @lru_cache(maxsize=None)
    def rec(rs, reg):
        if not rs:
            return 0
        bx0 = min(r[0] for r in rs); by0 = min(r[1] for r in rs)
        bx1 = max(r[2] for r in rs); by1 = max(r[3] for r in rs)
        trims = sum(abs(a - b) > eps for a, b in ((bx0, reg[0]), (by0, reg[1]), (bx1, reg[2]), (by1, reg[3])))
        reg = (bx0, by0, bx1, by1)
        if len(rs) == 1:
            return trims
        best = None
        for axis in (0, 1):
            lines = sorted({r[axis] for r in rs} | {r[axis + 2] for r in rs})
            for t in lines:
                if not (reg[axis] + eps < t < reg[axis + 2] - eps):
                    continue
                if any(r[axis] + eps < t < r[axis + 2] - eps for r in rs):
                    continue  # would cut a bar
                lo = tuple(r for r in rs if r[axis + 2] <= t + eps)
                hi = tuple(r for r in rs if r[axis] >= t - eps)
                rlo = (reg[0], reg[1], t, reg[3]) if axis == 0 else (reg[0], reg[1], reg[2], t)
                rhi = (t, reg[1], reg[2], reg[3]) if axis == 0 else (reg[0], t, reg[2], reg[3])
                c = 1 + rec(lo, rlo) + rec(hi, rhi)
                best = c if best is None else min(best, c)
        assert best is not None
        return trims + best
    return rec(tuple(sorted(tuple(round(v, 2) for v in r) for r in rects)), region)


def check_materials():
    """Materials file (kit stage): what each sheet holds, the allocation the
    guide prints, spares, totals, trimmer cuts, the Grades 4-5 Problem 6 boards,
    and the packet page count."""
    from collections import Counter
    from math import dist
    pages = read_materials()
    assert len(pages) == 3
    norm = lambda rc: rc  # (rows, cols), as labelled on the sheets ("3 by 4")
    sheet1 = Counter(norm(rc) for _, rc in pages[0]["bars"])
    sheet2 = Counter(norm(rc) for _, rc in pages[1]["bars"])
    assert "Bars, sheet 1" in pages[0]["text"] and "Bars, sheet 2" in pages[1]["text"]
    assert sheet1 == Counter({(3, 4): 2, (3, 3): 2, (2, 4): 1, (2, 3): 1, (1, 6): 1}), sheet1
    assert sheet2 == Counter({(3, 4): 1, (3, 3): 1, (2, 4): 2, (2, 3): 1, (2, 2): 2, (2, 5): 1}), sheet2
    sq = lambda c: sum(a * b * k for (a, b), k in c.items())
    assert (sum(sheet1.values()), sq(sheet1), sum(sheet2.values()), sq(sheet2)) == (7, 62, 8, 61)
    # labels on the sheets match the bars ("3 by 4" = 3 rows, 4 columns)
    for pg, c in ((pages[0], sheet1), (pages[1], sheet2)):
        labels = Counter(tuple(int(x) for x in m) for m in re.findall(r"(\d+) by (\d+)", pg["text"]))
        assert labels == c, (labels, c)
    ok("materials p1 'Bars, sheet 1': two 3x4, two 3x3, 2x4, 2x3, 1x6 (7 bars, 62 squares); "
       "p2 'Bars, sheet 2': 3x4, 3x3, two 2x4, 2x3, two 2x2, 2x5 (8 bars, 61 squares); 25 mm squares")

    # Allocation printed in the guide: a pair gets sheet 1 plus a 2x4 and a 2x2
    # from its table's sheet 2; the rest of sheet 2 is the table's spare pool;
    # the 4-5 trio gets both sheets.
    pair_kit = sheet1 + Counter({(2, 4): 1, (2, 2): 1})
    pool = sheet2 - Counter({(2, 4): 2, (2, 2): 2})
    assert sum(pair_kit.values()) == 9 and sq(pair_kit) == 74
    assert pool == Counter({(3, 4): 1, (3, 3): 1, (2, 3): 1, (2, 5): 1})
    # needs read from the pages (first routes: K-1 P1-P3, 2-3 P1-P2, 4-5 P1-P2)
    need = {"K-1": Counter({(2, 2): 1, (2, 3): 1, (1, 6): 1, (3, 4): 1, (3, 3): 2, (2, 4): 2}),
            "2-3": Counter({(3, 3): 2, (2, 4): 2, (3, 4): 1, (1, 6): 1, (2, 2): 1}),
            "4-5": Counter({(3, 3): 2, (2, 4): 2, (3, 4): 1})}
    for band in ("K-1", "2-3"):
        assert not (need[band] - pair_kit), band
    trio = sheet1 + sheet2
    assert not (need["4-5"] - trio)
    # spares the solutions mention: K-1 P2 second try and 2-3 P2 shortcut try
    # (a second 3x4 per pair); K-1 P8 check (2x3, 3x3, 3x4 from the pool);
    # 4-5: a third 3x3 and 2x4 for the third child, a second 3x4, a 2x3 and a 2x4
    # left for the two-bar question of Problem 3
    assert (pair_kit - need["K-1"])[(3, 4)] == 1 and (pair_kit - need["2-3"])[(3, 4)] == 1
    assert not (Counter({(2, 3): 1, (3, 3): 1, (3, 4): 1}) - pool)
    left45 = trio - need["4-5"]
    assert left45[(3, 3)] >= 1 and left45[(2, 4)] >= 1 and left45[(3, 4)] >= 1 and left45[(2, 3)] >= 1
    assert left45 == Counter({(3, 4): 2, (3, 3): 1, (2, 4): 1, (2, 3): 2, (1, 6): 1, (2, 2): 2, (2, 5): 1})
    ok("allocation: a pair gets sheet 1 + a 2x4 and a 2x2 from sheet 2 (9 bars, 74 squares, covers K-1 P1-P3 "
       "and 2-3 P1-P2 with a second 3x4); table pool 3x4, 3x3, 2x3, 2x5 (K-1 P8 check); 4-5 trio both sheets")

    # current group: two K-1 pairs, two 2-3 pairs, one 4-5 trio
    n1, n2 = 2 + 2 + 1, 3
    bars = n1 * 7 + n2 * 8
    squares = n1 * 62 + n2 * 61
    assert (n1 + n2, bars, squares) == (8, 59, 493)
    W, H = 215.9, 279.4
    cuts1 = guillotine_cuts([b for b, _ in pages[0]["bars"]], (0, 0, W, H))
    cuts2 = guillotine_cuts([b for b, _ in pages[1]["bars"]], (0, 0, W, H))
    assert (cuts1, cuts2) == (11, 12), (cuts1, cuts2)
    assert n1 * cuts1 + n2 * cuts2 == 91
    ok("print: 5 copies of p1 and 3 of p2 = 8 card sheets, 59 bars, 493 squares; trimmer cuts "
       "11 per p1 and 12 per p2, 91 in all")

    # cuts children make on the first route (bars broken into squares)
    cuts = lambda bs: sum(a * b - 1 for a, b in bs)
    k1 = cuts([(2, 2), (2, 3), (1, 6)]) + cuts([(3, 4)]) + cuts([(3, 3), (3, 3), (2, 4), (2, 4)])
    t23 = cuts([(3, 3), (3, 3), (2, 4), (2, 4)]) + cuts([(3, 4), (1, 6), (2, 2)])
    t45 = cuts([(3, 3), (3, 3), (2, 4), (2, 4)]) + cuts([(3, 4)])
    assert (k1, t23, t45) == (54, 49, 41), (k1, t23, t45)
    ok("children's cuts per pair on the first route: 54 (K-1 P1-P3), 49 (2-3 P1-P2), 41 (4-5 P1-P2)")

    # page 3: two boards for Grades 4-5 Problem 6
    p3 = pages[2]
    assert "2-spot Sprouts boards" in p3["text"] and "Problem 6" in p3["text"]
    assert sorted(p3["boards"]) == [(186, 102), (186, 102)], p3["boards"]
    sp = sorted(p3["spots"], key=lambda q: (round(q[1]), q[0]))
    assert len(sp) == 4
    assert abs(dist(sp[0], sp[1]) - 90) < 0.5 and abs(dist(sp[2], sp[3]) - 90) < 0.5
    ok("materials p3: two 2-spot Sprouts boards 186x102 mm, spots 90 mm apart (Grades 4-5 Problem 6)")

    pages_packets = 4 * 7 + 4 * 7 + 3 * 9
    assert pages_packets == 83
    ok("packets: 83 pages for the current eleven children (4 K-1, 4 Grades 2-3, 3 Grades 4-5)")


if __name__ == "__main__":
    check_bars()
    check_engine()
    check_abstract()
    check_sprouts()
    check_drawings()
    check_boards()
    check_materials()
    print(f"\nall {len(OK)} checks passed")
