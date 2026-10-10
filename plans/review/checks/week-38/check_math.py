#!/usr/bin/env python3
"""Week 38 (Seams and cuts) base packet: independent mathematics.

Builds the uncut and centre-cut bands A (matching seam) and B (reversing seam)
in the cell-complex model of surfaces.py and computes, without using any
packet answer: pieces, boundary circles, surface types, which circles are old
edges and which are new cut edges, the U/L half-strip connections, transverse
arrow transport, and every dot task by brute force over actual boundary sides.
The guide's answers are transcribed by hand (page numbers of
week-38-facilitator.pdf) and compared with the computed ones.

Run: python3 check_math.py > out_check_math.txt
"""
from itertools import combinations
from surfaces import Band
from common import Checker

C = Checker()
PICTURES = [(4,), (3, 1), (2, 2), (2, 1, 1), (1, 1, 1, 1)]   # printed order, checked in check_diagrams.py
NAMES = ["4", "3+1", "2+2", "2+1+1", "1+1+1+1"]


def build(kind, cut, L=12, W=6):
    return Band([kind], L, W, cuts=({W // 2} if cut else ()))


print("== Surfaces ==")
models = {}
for kind, name in (("M", "A"), ("R", "B")):
    for cut in (False, True):
        b = build(kind, cut)
        s = b.summary()
        models[(name, cut)] = b
        print(f"{name} {'after centre cut' if cut else 'uncut'}: {s}")
        C.ok(s["boundary_is_manifold"], f"{name} {'cut' if cut else 'uncut'}: every boundary vertex has degree 2")

A0, B0, A1, B1 = models[("A", False)], models[("B", False)], models[("A", True)], models[("B", True)]
C.ok(A0.summary()["types"] == ["annulus"], "uncut A is one annulus (2 boundary circles)")
C.ok(B0.summary()["types"] == ["Mobius band"], "uncut B is one Mobius band (1 boundary circle)")
C.ok(A1.summary()["types"] == ["annulus", "annulus"], "cut A: two annuli, 4 boundary circles in all")
C.ok(B1.summary()["types"] == ["annulus"], "cut B: one annulus with 2 boundary circles")

# old edge vs new cut edge membership
kindsA1 = sorted(sorted(A1.circle_sides(c)) for c in A1.circles)
kindsB1 = sorted(sorted(B1.circle_sides(c)) for c in B1.circles)
print("cut A circle side-kinds:", kindsA1)
print("cut B circle side-kinds:", kindsB1)
C.ok(kindsB1 == [["bottom", "top"], ["cut"]],
     "cut B: one circle is the whole old edge (top+bottom), the other is the whole new cut edge (guide p4 'proof with the materials')")
C.ok(sorted(sorted(B0.circle_sides(c)) for c in B0.circles) == [["bottom", "top"]],
     "uncut B: the upper and lower long edges form ONE circle (guide p5 P1-2)")
C.ok(sorted(sorted(A0.circle_sides(c)) for c in A0.circles) == [["bottom"], ["top"]],
     "uncut A: the upper edge closes on itself and the lower edge closes on itself")
per_piece = []
for idx in range(len(A1.pieces)):
    per_piece.append(sorted(sorted(A1.circle_sides(c)) for c in A1.circles if A1.piece_of_circle(c) == idx))
C.ok(all(len(p) == 2 and ["cut"] in p for p in per_piece), f"cut A: each piece has one old edge and one cut edge {per_piece}")

# U/L half-strip connectivity: rows 0..2 are U, 3..5 are L
for name, b in (("A", A1), ("B", B1)):
    pieces_rows = [sorted({('U' if j < 3 else 'L') for (_, _, j) in fs}) for fs in b.pieces]
    print(f"cut {name}: half-strips per piece {pieces_rows}")
C.ok(sorted(sorted({('U' if j < 3 else 'L') for (_, _, j) in fs}) for fs in A1.pieces) == [["L"], ["U"]],
     "cut A: U and L are separate pieces (U->U, L->L)")
C.ok([sorted({('U' if j < 3 else 'L') for (_, _, j) in fs}) for fs in B1.pieces] == [["L", "U"]],
     "cut B: one piece runs through both U and L (U->L, L->U)")

print("\n== Transverse arrow (Grades 4-5 Problem 6), odd width so the middle line runs through cells ==")
for kind, name in (("M", "A"), ("R", "B")):
    b = Band([kind], 12, 5)
    s1, n1 = b.transport(0, 2, 1)
    s2, n2 = b.transport(0, 2, 2)
    print(f"{name}: after one trip sign {s1:+d} ({n1} cell steps), after two trips {s2:+d}")
    if name == "A":
        C.ok(s1 == 1, "A: arrow returns pointing U->L after one trip")
    else:
        C.ok(s1 == -1 and s2 == 1, "B: arrow returns reversed (L->U) after one trip, restored after two")
# the reversal is not an artefact of the row: every row of B returns to its own cell only after 2 trips
b = Band(["R"], 12, 5)
C.ok(all(b.transport(0, j, 1)[1] == (12 if j == 2 else 24) for j in range(5)),
     "B: only the middle row closes after one longitudinal trip; other rows need two (edge trip doubles)")

print("\n== Dot tasks by brute force over boundary sides (small mesh) ==")


def small(kind, cut):
    return Band([kind], 4, 2, cuts=({1} if cut else ()))


def placements(b, ndots):
    """All ways to put ndots dots on distinct boundary sides; yields the list of
    (circle index, piece index) for each dot."""
    side_circle = {}
    for ci, circ in enumerate(b.circles):
        for fs in circ:
            side_circle[fs] = ci
    sides = sorted(side_circle)
    for combo in combinations(sides, ndots):
        yield [(side_circle[s], b.piece_of_face[s[0]]) for s in combo]


def shapes(b):
    out = set()
    for pl in placements(b, 4):
        cnt = {}
        for ci, _ in pl:
            cnt[ci] = cnt.get(ci, 0) + 1
        out.add(tuple(sorted(cnt.values(), reverse=True)))
    return out


smallm = {(n, c): small(k, c) for k, n in (("M", "A"), ("R", "B")) for c in (False, True)}
for key, b in smallm.items():
    C.ok(b.summary() == models[key].summary(), f"small mesh {key} agrees with large mesh: {b.summary()['types']}")

# Problem 2 (all bands): two dots on one trip / on different trips
for name in "AB":
    b = smallm[(name, False)]
    same = any(p[0][0] == p[1][0] for p in placements(b, 2))
    diff = any(p[0][0] != p[1][0] for p in placements(b, 2))
    print(f"P2 {name}: a pair on one trip possible={same}; a pair on no common trip possible={diff}")
    C.ok(same, f"P2 {name}: two dots on one edge trip is possible")
    C.ok(diff == (name == "A"), f"P2 {name}: 'no one trip reaches both' is {'possible' if name == 'A' else 'impossible'}")

# Problem 3 (before cutting) and Problem 6 (after cutting)
table = {}
for key, b in smallm.items():
    sh = shapes(b)
    table[key] = [p in sh for p in PICTURES]
    print(f"{key[0]} {'cut' if key[1] else 'uncut'}: realizable pictures", [n for n, ok in zip(NAMES, table[key]) if ok])

YES, NO = True, False
# Guide transcriptions
C.ok(table[("A", False)] == [YES, YES, YES, NO, NO], "guide p3 K-1 P3 table, A column: Yes Yes Yes No No")
C.ok(table[("B", False)] == [YES, NO, NO, NO, NO], "guide p3 K-1 P3 table, B column: Yes No No No No")
C.ok(table[("A", False)] == [YES, YES, YES, NO, NO] and table[("B", False)] == [YES, NO, NO, NO, NO],
     "guide p4 2-3 P3 and guide p5 4-5 P3 ('A: yes, yes, yes, no, no. B: yes, no, no, no, no')")
C.ok(table[("A", True)] == [YES] * 5, "guide p4 2-3 P6 table, Cut A: all Yes; guide p3 K-1 P6; guide p5 4-5 P7")
C.ok(table[("B", True)] == [YES, YES, YES, NO, NO], "guide p4 2-3 P6 table, Cut B: Yes Yes Yes No No; K-1 P6 'only 4, 3+1, 2+2'")

# Partition theorem of the overview: realizable iff number of groups <= number of circles
for key, b in smallm.items():
    nb = len(b.circles)
    C.ok(table[key] == [len(p) <= nb for p in PICTURES],
         f"overview 'partitions of 4 into at most b groups' holds for {key} with b={nb}")

# Problem 5: two dots on one piece but different closed edges
for name in "AB":
    b = smallm[(name, True)]
    ex = any(p[0][1] == p[1][1] and p[0][0] != p[1][0] for p in placements(b, 2))
    C.ok(ex, f"P5 cut {name}: two dots on the same piece but different closed edges is possible (guide: yes for both)")

# Problem 7: four dots, every cut piece has a dot, no circle holds two dots
for name in "AB":
    b = smallm[(name, True)]
    ok7 = any(len({ci for ci, _ in pl}) == 4 and len({pi for _, pi in pl}) == len(b.pieces) for pl in placements(b, 4))
    print(f"P7 cut {name}: possible={ok7}")
    C.ok(ok7 == (name == "A"), f"P7 cut {name}: {'possible' if name == 'A' else 'impossible'} (guide K-1 p3, 2-3 p4)")

# Problem 4 piece counts
C.ok(len(A1.pieces) == 2 and len(B1.pieces) == 1, "P4: A cuts into 2 pieces, B into 1 (guide p3, p4, p5)")
C.ok(len(A1.circles) == 4 and len(B1.circles) == 2, "4-5 P4: boundary components 4 total for cut A, 2 for cut B")

print("\n== Other readings ==")
# An off-centre cut of B (one closed curve that runs twice around) gives two pieces:
# the guide's caveat 'an off-center ... cut is a different experiment' is right.
b = Band(["R"], 12, 6, cuts={2, 4})  # an off-centre longitudinal cut closes up through y=2 and y=4
print("B cut at 1/3 (closes through 2/3):", b.summary())
C.ok(sorted(b.summary()["types"]) == ["Mobius band", "annulus"],
     "B cut off-centre: a Mobius band plus an annulus, so the guide's caveat that an off-centre cut is a different experiment is right")

C.summary()
