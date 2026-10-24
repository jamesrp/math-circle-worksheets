#!/usr/bin/env python3
"""Checks for the 'Games decided before they start' packets.

Planar positions are stored as faces. A face is a list of boundary
components; a component is a cyclic list of vertex occurrences (corners).
An isolated vertex (degree 0) is a component with one occurrence.

Games:
  sprigs(n)    2-Sprigs: n dots, 2 lives each, a curve has no middle vertex.
  sprouts(n)   Sprouts: n spots, 3 lives each, a new spot (1 life) on each curve.
  brussels(n)  Brussels Sprouts: n crosses; each free arm is a pendant tip
               with 1 life; a move joins two tips and puts a new cross on
               the curve with one new arm on each side.

Random play explores many complete games; exact search gives the set of
possible game lengths and the winner under best play for small cases.
"""
import itertools
import random
import sys
from functools import lru_cache


def bar_results():
    bars = [(2, 2), (2, 3), (3, 3), (2, 4), (1, 6), (3, 4),
            (4, 5), (3, 5), (5, 5), (1, 9), (6, 6), (7, 9), (8, 13), (25, 40)]
    for m, n in bars:
        breaks = m * n - 1
        print(f"bar {m} by {n}: {m*n} squares, {breaks} breaks, "
              f"{'1st' if breaks % 2 else '2nd'} player makes the last break")
    for group in [[(2, 3), (3, 3)], [(3, 4), (1, 6)], [(3, 3)] * 3]:
        sq = sum(m * n for m, n in group)
        breaks = sq - len(group)
        print(f"bars {group}: {breaks} breaks, {'1st' if breaks % 2 else '2nd'} wins")


def bar_breaks_any_order(m, n, trials=2000):
    """Break a bar in random orders and confirm the count never changes."""
    counts = set()
    for _ in range(trials):
        pieces = [(m, n)]
        k = 0
        while any(a * b > 1 for a, b in pieces):
            big = [p for p in pieces if p[0] * p[1] > 1]
            a, b = random.choice(big)
            pieces.remove((a, b))
            if a > 1 and (b == 1 or random.random() < 0.5):
                c = random.randint(1, a - 1)
                pieces += [(c, b), (a - c, b)]
            else:
                c = random.randint(1, b - 1)
                pieces += [(a, c), (a, b - c)]
            k += 1
        counts.add(k)
    return counts


class Game:
    def __init__(self, kind, n):
        self.kind = kind
        self.n = n

    def start(self):
        lives = {}
        comps = []
        if self.kind in ("sprigs", "sprouts"):
            L = 2 if self.kind == "sprigs" else 3
            for v in range(self.n):
                lives[v] = L
                comps.append((v,))
            deg = {v: 0 for v in range(self.n)}
        else:  # brussels
            deg = {}
            nxt = 0
            for _ in range(self.n):
                c = nxt; nxt += 1
                lives[c] = 0
                deg[c] = 4
                seq = []
                for _ in range(4):
                    a = nxt; nxt += 1
                    lives[a] = 1
                    deg[a] = 1
                    seq += [c, a]
                comps.append(tuple(seq))
        faces = [tuple(comps)]
        return faces, lives, deg

    # ---- move generation -------------------------------------------------
    def moves(self, faces, lives, deg):
        """Yield (new_faces, new_lives, new_deg) for every legal move."""
        newv = max(lives) + 1
        for fi, face in enumerate(faces):
            others_faces = faces[:fi] + faces[fi + 1:]
            occ = []  # (component index, position)
            for ci, comp in enumerate(face):
                for pi in range(len(comp)):
                    occ.append((ci, pi))
            for a in range(len(occ)):
                for b in range(a, len(occ)):
                    (ci, pi), (cj, pj) = occ[a], occ[b]
                    u = face[ci][pi]
                    v = face[cj][pj]
                    if not self.legal_ends(u, v, a == b, lives, deg):
                        continue
                    for res in self.draw(face, ci, pi, cj, pj, lives, deg, newv):
                        nf, nl, nd = res
                        yield others_faces + nf, nl, nd

    def legal_ends(self, u, v, same_corner, lives, deg):
        if self.kind == "brussels":
            return u != v and lives[u] >= 1 and lives[v] >= 1
        if u == v:
            return lives[u] >= 2
        return lives[u] >= 1 and lives[v] >= 1

    def draw(self, face, ci, pi, cj, pj, lives, deg, w):
        u = face[ci][pi]
        v = face[cj][pj]
        nl = dict(lives)
        nd = dict(deg)
        if u == v:
            nl[u] -= 2
            nd[u] += 2
        else:
            nl[u] -= 1
            nl[v] -= 1
            nd[u] += 1
            nd[v] += 1
        kind = self.kind
        if kind == "sprigs":
            mid1, mid2 = (), ()
        elif kind == "sprouts":
            nl[w] = 1
            nd[w] = 2
            mid1, mid2 = (w,), (w,)
        else:
            b1, b2 = w + 1, w + 2
            nl[w] = 0; nd[w] = 4
            nl[b1] = 1; nd[b1] = 1
            nl[b2] = 1; nd[b2] = 1
            mid1, mid2 = (w, b1, w), (w, b2, w)

        def walk(comp, p, vdeg):
            """Boundary walk of comp starting at position p, then the repeated
            corner if the vertex had positive degree."""
            k = len(comp)
            seq = tuple(comp[(p + t) % k] for t in range(k))
            if vdeg == 0:
                return seq  # isolated vertex: single occurrence, no new corner
            return seq + (comp[p],)

        rest = [face[k] for k in range(len(face)) if k not in (ci, cj)]
        out = []
        if ci != cj:
            # merge two boundary components; the face does not split
            A = walk(face[ci], pi, deg[u])
            B = walk(face[cj], pj, deg[v])
            new = A + mid1 + B + mid2
            out.append(([tuple(rest) + (new,)], nl, nd))
            return out
        comp = face[ci]
        k = len(comp)
        if pi == pj:
            # loop from a corner back to the same corner
            if deg[u] == 0:
                f1 = (u,) + mid1
                f2 = (u,) + mid2
            else:
                f1 = (u,) + mid1
                f2 = walk(comp, pi, deg[u]) + mid2
        else:
            t = (pj - pi) % k
            seq = [comp[(pi + s) % k] for s in range(k)]
            f1 = tuple(seq[: t + 1]) + mid1
            f2 = tuple(seq[t:]) + (seq[0],) + mid2
        # distribute the other components between the two new faces
        for mask in range(1 << len(rest)):
            g1 = [rest[r] for r in range(len(rest)) if mask >> r & 1]
            g2 = [rest[r] for r in range(len(rest)) if not mask >> r & 1]
            out.append(([tuple(g1) + (f1,), tuple(g2) + (f2,)], nl, nd))
        return out

    # ---- play --------------------------------------------------------------
    def random_game(self, rng):
        faces, lives, deg = self.start()
        m = 0
        while True:
            opts = list(self.moves(faces, lives, deg))
            if not opts:
                return m, lives
            faces, lives, deg = rng.choice(opts)
            m += 1

    def lengths(self):
        """Exact set of possible game lengths (exhaustive search)."""
        seen = set()

        def rec(faces, lives, deg, m):
            any_move = False
            for nf, nl, nd in self.moves(faces, lives, deg):
                any_move = True
                rec(nf, nl, nd, m + 1)
            if not any_move:
                seen.add(m)
        rec(*self.start(), 0)
        return seen

    def first_player_wins(self):
        """Normal play: the player who cannot move loses."""
        def canon(faces, lives):
            # exact key (vertex names kept); dead vertices are dropped from
            # boundaries since only live vertices take part in later moves
            fs = []
            for f in faces:
                cs = []
                for c in f:
                    c2 = tuple(x for x in c if lives[x] > 0)
                    if not c2:
                        continue
                    rots = [c2[r:] + c2[:r] for r in range(len(c2))]
                    cs.append(min(rots))
                fs.append(tuple(sorted(cs)))
            live = tuple(sorted((x, l) for x, l in lives.items() if l > 0))
            return (tuple(sorted(fs)), live)

        memo = {}

        def win(faces, lives, deg):
            key = canon(faces, lives)
            if key in memo:
                return memo[key]
            res = False
            for nf, nl, nd in self.moves(faces, lives, deg):
                if not win(nf, nl, nd):
                    res = True
                    break
            memo[key] = res
            return res
        return win(*self.start())


def main():
    random.seed(1)
    print("== bars ==")
    bar_results()
    for m, n in [(2, 3), (3, 3), (3, 4), (2, 4)]:
        print(f"random break orders of {m} by {n}:", bar_breaks_any_order(m, n))

    rng = random.Random(7)
    print("== 2-Sprigs ==")
    for n in range(1, 7):
        lens = {Game("sprigs", n).random_game(rng)[0] for _ in range(3000)}
        print(f"{n} dots: random-play lengths {sorted(lens)}")
    for n in range(1, 4):
        print(f"{n} dots: exact lengths {sorted(Game('sprigs', n).lengths())}")

    print("== Sprouts ==")
    for n in range(1, 4):
        lens = {Game("sprouts", n).random_game(rng)[0] for _ in range(4000)}
        print(f"{n} spots: random-play lengths {sorted(lens)}, bounds {2*n}..{3*n-1}")
    for n in (1, 2):
        g = Game("sprouts", n)
        print(f"{n} spots: exact lengths {sorted(g.lengths())}; first player wins: {g.first_player_wins()}")
    g = Game("sprouts", 3)
    print("3 spots: first player wins:", g.first_player_wins())

    print("== Brussels Sprouts ==")
    for n in range(1, 4):
        lens = {Game("brussels", n).random_game(rng)[0] for _ in range(1500 if n < 3 else 300)}
        print(f"{n} crosses: random-play lengths {sorted(lens)}, 5n-2 = {5*n-2}")
    print("1 cross: exact lengths", sorted(Game("brussels", 1).lengths()))


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    main()
