"""Recheck every count the reconciled Week 44 card's App fit and Fix list give.

Standalone: enumerates marked histories of the copying bag (Polya urn), the
return-only bag and the bonus add-the-other-colour rule, with exact fractions.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import product


def histories(n, rule, start=(("R", 1), ("B", 1))):
    """Yield (identity history, colour word, final bag, probability)."""
    def rec(bag, hist, p, step):
        if step == n:
            word = "".join(c for c, _ in hist)
            final = (sum(1 for c, _ in bag if c == "R"), sum(1 for c, _ in bag if c == "B"))
            yield tuple(hist), word, final, p
            return
        for ctr in bag:
            nb = list(bag)
            colour = ctr[0]
            if rule == "copy":
                k = 1 + sum(1 for c, _ in bag if c == colour)
                nb.append((colour, k))
            elif rule == "other":
                oc = "B" if colour == "R" else "R"
                k = 1 + sum(1 for c, _ in bag if c == oc)
                nb.append((oc, k))
            yield from rec(nb, hist + [ctr], p / len(bag), step + 1)
    yield from rec(list(start), [], F(1), 0)


def show(label, value, expect):
    ok = "ok " if value == expect else "FAIL"
    print(f"{ok} {label}: {value}")


for n, total in [(2, 6), (3, 24), (4, 120)]:
    hs = list(histories(n, "copy"))
    show(f"copying, {n} draws, marked histories", len(hs), total)
    show(f"  all equally likely", len({p for *_, p in hs}), 1)
    by_red = Counter(w.count("R") for _, w, _, _ in hs)
    show(f"  histories per red total", sorted(by_red.values()), [total // (n + 1)] * (n + 1))
    by_bag = Counter(f for _, _, f, _ in hs)
    show(f"  bins by final bag", len(by_bag), n + 1)

hs2 = list(histories(2, "copy"))
words2 = Counter(w for _, w, _, _ in hs2)
show("two draws: histories per colour word RR, RB, BR, BB",
     [words2[w] for w in ("RR", "RB", "BR", "BB")], [2, 1, 1, 2])
colour_bins = Counter(f for f in {(w, f) for _, w, f, _ in hs2})
colour_per_bag = Counter(f for w, f in {(w, f) for _, w, f, _ in hs2})
show("two draws: colour stories per final bag (1R/3B, 2R/2B, 3R/1B)",
     [colour_per_bag[b] for b in ((1, 3), (2, 2), (3, 1))], [1, 2, 1])
# K-1 P1 identity reading: distinct draw stories per bag
id_per_bag = Counter(f for _, _, f, _ in hs2)
show("K-1 P1 identity reading: stories per bag", sorted(id_per_bag.values()), [2, 2, 2])

ret = Counter(sum(1 for c in w if c == "R") for w in product("RB", repeat=2))
show("return only, two draws: words per red total 0,1,2", [ret[0], ret[1], ret[2]], [1, 2, 1])

hs3 = list(histories(3, "copy"))
w3 = Counter(w for _, w, _, _ in hs3)
show("three draws: RRB, RBR, BRR histories", [w3["RRB"], w3["RBR"], w3["BRR"]], [2, 2, 2])
show("three draws: RRR and BBB histories", [w3["RRR"], w3["BBB"]], [6, 6])
p3 = {}
for _, w, _, p in hs3:
    p3[w] = p3.get(w, 0) + p
show("three draws: P(RRB), P(RBR), P(BRR)", [p3["RRB"], p3["RBR"], p3["BRR"]], [F(1, 12)] * 3)
bags3 = sorted({f for _, _, f, _ in hs3})
show("K-1 P2: possible three-draw bags", bags3, [(1, 4), (2, 3), (3, 2), (4, 1)])
show("K-1 P2: colour stories for 3R/2B", sorted({w for _, w, f, _ in hs3 if f == (3, 2)}), ["BRR", "RBR", "RRB"])

hs4 = list(histories(4, "copy"))
w4 = Counter(w for _, w, _, _ in hs4)
show("four draws: RRBB and RBRB histories", [w4["RRBB"], w4["RBRB"]], [4, 4])
show("four draws: RRRR histories", w4["RRRR"], 24)
c4 = Counter(f for f in {(w, f) for _, w, f, _ in hs4})
cs4 = Counter(f for w, f in {(w, f) for _, w, f, _ in hs4})
show("four draws: colour stories for 5R/1B, 4R/2B, 3R/3B",
     [cs4[(5, 1)], cs4[(4, 2)], cs4[(3, 3)]], [1, 4, 6])
show("four draws: blue-majority bags", sorted(b for b in cs4 if b[1] > b[0]), [(1, 5), (2, 4)])
p4 = {}
for _, _, f, p in hs4:
    p4[f] = p4.get(f, 0) + p
show("2-3 replacement P6: P(5R/1B) and P(3R/3B)", [p4[(5, 1)], p4[(3, 3)]], [F(1, 5), F(1, 5)])
show("  RRRR share and one 2R2B word's share", [F(w4["RRRR"], 120), F(w4["RRBB"], 120)], [F(24, 120), F(4, 120)])

# K-1 P4: predecessors one draw back
for fin in [(5, 1), (4, 2), (3, 3)]:
    pre = sorted({(fin[0] - 1, fin[1]) if True else None} | {(fin[0], fin[1] - 1)})
    pre = [b for b in pre if b[0] >= 1 and b[1] >= 1 and b in set(bags3)]
    print(f"     K-1 P4: {fin[0]}R/{fin[1]}B before the last draw: {pre}")

# Kit: counters of one colour needed
need = max(max(f) for _, _, f, _ in histories(5, "copy"))
show("five-draw story, most counters of one colour", need, 6)
show("K-1 P1 three bags at once: reds and blues", (3 + 2 + 1, 1 + 2 + 3), (6, 6))

oth = list(histories(2, "other"))
oc = Counter(w.count("R") for _, w, _, _ in oth)
show("bonus add-other rule, two draws: histories per red total 0,1,2", [oc[0], oc[1], oc[2]], [1, 4, 1])

# three colours, two draws
def tri(n):
    def rec(bag, hist, step):
        if step == n:
            yield tuple(hist), tuple(sorted(Counter(c for c, _ in bag).items()))
            return
        for ctr in bag:
            col = ctr[0]
            k = sum(1 for c, _ in bag if c == col)
            yield from rec(bag + [(col, k)], hist + [ctr], step + 1)
    yield from rec([("R", 0), ("B", 0), ("G", 0)], [], 0)

t2 = list(tri(2))
tb = Counter(b for _, b in t2)
show("bonus three-colour bag, two draws: histories", len(t2), 12)
show("  bins and histories per bin", (len(tb), sorted(set(tb.values()))), (6, [2]))
