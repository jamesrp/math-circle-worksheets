"""Check every vote, knockout and build claim on the revised Week 87 K-1 pages (W87-K-v1).

Revision: Problem 5 now asks for C; Problems 6-8 ask for B (so no printed set
or earlier result answers a build problem).  The knockout example on page 2
uses the launch cards DFE, EFD, FED.
"""
from itertools import permutations, product, combinations, combinations_with_replacement

L = "ABC"
CARDS = ["".join(p) for p in permutations(L)]


def pair(cards, x, y):
    vx = sum(1 for c in cards if c.index(x) < c.index(y))
    vy = len(cards) - vx
    assert vx != vy
    return (x, vx, vy) if vx > vy else (y, vy, vx)


def knockout(cards, first, wait):
    w1 = pair(cards, first[0], first[1])[0]
    return w1, pair(cards, w1, wait)[0]


def winners(cards, letters=L):
    out = set()
    for wait in letters:
        a, b = [l for l in letters if l != wait]
        out.add(knockout(cards, (a, b), wait)[1])
        out.add(knockout(cards, (b, a), wait)[1])
    return sorted(out)


def report(name, cards, letters=L):
    print(name, cards)
    for x, y in combinations(letters, 2):
        w, a, b = pair(cards, x, y)
        print(f"   {x} or {y}: {w} wins {a}-{b}")
    print("   letters that can win:", winners(cards, letters))


# Page 1 launch picture: D or E on DFE, EFD, FED
launch = ["DFE", "EFD", "FED"]
ballots = ["D" if c.index("D") < c.index("E") else "E" for c in launch]
print("launch D or E ballots:", ballots, pair(launch, "D", "E"))
assert ballots == ["D", "E", "E"]
# Page 2 knockout example: First pair D E, Waiting F
w1, w = knockout(launch, ("D", "E"), "F")
print("knockout example: first winner", w1, "winner", w, "| final", pair(launch, "E", "F"))
assert (w1, w) == ("E", "F")
report("launch cards", launch, "DEF")
assert winners(launch, "DEF") == ["F"]  # no circle given away

FIXED = ["ABC", "BCA", "CAB"]
report("Problems 1-2 fixed", FIXED)
assert [pair(FIXED, *p)[0] for p in [("A", "B"), ("B", "C"), ("C", "A")]] == ["A", "B", "C"]
for first, wait in [("BC", "A"), ("CA", "B"), ("AB", "C")]:
    r = knockout(FIXED, first, wait)
    print(f"   P2 {first} / {wait} waits -> first winner {r[0]}, winner {r[1]}")
    assert r[1] == wait

P3 = ["CBA", "BAC", "CBA"]
P4 = ["ABC", "BAC", "CAB"]
report("Problem 3", P3)
report("Problem 4", P4)
assert winners(P3) == ["C"] and winners(P4) == ["A"]

# Problem 5: one swap on one fixed card so that C wins every knockout
print("Problem 5 swaps (target C):")
p5_results = []
for i, card in enumerate(FIXED):
    for p, q in combinations(range(3), 2):
        c = list(card); c[p], c[q] = c[q], c[p]; c = "".join(c)
        new = FIXED.copy(); new[i] = c
        ws = winners(new)
        print(f"   V{i+1} {card}->{c}: winners {ws}")
        if ws == ["C"]:
            p5_results.append(new)
print("   swaps that work:", len(p5_results), "of 9")
assert len(p5_results) == 3

# No printed set or Problem 5 result makes B the only winner (Problem 6 must be built fresh)
for s in [P3, P4] + p5_results:
    assert winners(s) != ["B"], s
print("no printed set or Problem 5 result makes B win every knockout: OK")

# Problems 6-8: three cards, each with A, B, C once; B wins every knockout
print("Problems 6-8 (sets of three cards, repeats allowed), target B:")
counts = {}
for tops in range(4):
    good, total = [], 0
    for ms in combinations_with_replacement(CARDS, 3):
        if sum(c[0] == "B" for c in ms) != tops:
            continue
        total += 1
        if winners(list(ms)) == ["B"]:
            good.append(ms)
    counts[tops] = (len(good), total)
    print(f"   B 1st on {tops} cards: {len(good)} of {total} sets work", good if len(good) < 6 else "")
assert counts[1][0] == 2 and counts[0][0] == 0
assert counts[2][0] == counts[2][1] and counts[3][0] == counts[3][1]
# Problem 7 sets must not appear among printed sets / earlier results
p7 = {tuple(sorted(s)) for s in [P3, P4] + p5_results}
assert not any(tuple(sorted(x)) in p7 for x in [("ABC", "BAC", "CBA"), ("ABC", "BCA", "CBA")])

# Global: 12 of 216 ordered profiles are circles; every other profile has one winner, who beats both
circ = [p for p in product(CARDS, repeat=3) if len(winners(list(p))) == 3]
print("circle profiles:", len(circ), "of 216; sets:", sorted({tuple(sorted(p)) for p in circ}))
assert len(circ) == 12
for p in product(CARDS, repeat=3):
    if p in circ:
        continue
    ws = winners(list(p))
    assert len(ws) == 1 and all(pair(list(p), ws[0], o)[0] == ws[0] for o in L if o != ws[0])
print("non-circle: sole winner beats both: OK")
print("ALL CHECKS PASSED")
