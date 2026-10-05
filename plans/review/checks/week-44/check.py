#!/usr/bin/env python3
"""Week 44 (The bag that copies) math check: independent brute-force verification.

Uses only my own code (common.py) and the standard library.  Printed bags and
history cards come from extracted.json (made by extract.py from the delivered
PDFs).  Every claim from the student pages and both adult guides is
transcribed by hand below and tested by exhaustive enumeration of marked
histories with exact fractions.

Run: python3 check.py > out_check.txt
"""
import json
import re
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import product
from math import comb, factorial

from common import (BONUS_SRC, FAILS, HERE, histories, counts, note, ok, section,
                    word, word_prob_copy)

DATA = json.loads((HERE / "extracted.json").read_text())


def bag_str(c):
    return "/".join(f"{k}{x}" for k, x in zip("RBG", c))


def boxes_by_size(page, w, h, tol=2.0):
    return [b for b in page["boxes"] if abs((b[2] - b[0]) - w) < tol and abs((b[3] - b[1]) - h) < tol]


def printed_bags(page):
    return [(bag["colours"].count("R"), bag["colours"].count("B"))
            for bag in page["bags"] if bag["discs"]]


def colour_stories(n, final):
    """Colour words of length n (copying, start RB) ending at bag `final`=(R,B)."""
    return ["".join(w) for w in product("RB", repeat=n)
            if (w.count("R") + 1, w.count("B") + 1) == tuple(final)]


def reachable(n):
    return sorted({(r + 1, n - r + 1) for r in range(n + 1)})


# ---------------------------------------------------------------------------
section("A. The one-copy urn (base guide p. 1 overview), n = 1..8")
for n in range(1, 9):
    H = list(histories("RB", n, "copy", first_mark=1))
    probs = {p for _, p, _ in H}
    ok(len(H) == factorial(n + 1) and probs == {F(1, factorial(n + 1))},
       f"n={n}: {len(H)} marked histories = (n+1)! and all equally likely")
    tot = Counter()
    for h, p, bag in H:
        r = word(h).count("R")
        tot[r] += p
        assert counts(bag, "RB") == (r + 1, n - r + 1)
        assert min(counts(bag, "RB")) >= 1
    ok(all(tot[r] == F(1, n + 1) for r in range(n + 1)),
       f"n={n}: red-draw total uniform, each 1/{n + 1}; bag (r+1, n-r+1), both colours present")
    wp = defaultdict(F)
    for h, p, _ in H:
        wp[word(h)] += p
    ok(all(wp[w] == F(factorial(w.count('R')) * factorial(n - w.count('R')), factorial(n + 1))
           == word_prob_copy(w) for w in wp) and len(wp) == 2 ** n,
       f"n={n}: every colour word has probability r!(n-r)!/(n+1)! (order-free); {2 ** n} words")
    # 'after red, the next red chance is 2/3' as a marginal conditional at every position
    if n >= 2:
        good = True
        for k in range(n - 1):
            pr = sum(p for w, p in wp.items() if w[k] == "R")
            prr = sum(p for w, p in wp.items() if w[k] == "R" and w[k + 1] == "R")
            pbr = sum(p for w, p in wp.items() if w[k] == "B" and w[k + 1] == "R")
            good &= prr / pr == F(2, 3) and pbr / (1 - pr) == F(1, 3)
        ok(good, f"n={n}: P(next R | previous R) = 2/3 and P(next R | previous B) = 1/3 at every position")
H2 = list(histories("RB", 2, "copy", first_mark=1))
H2w = defaultdict(F)
for h, p, _ in H2:
    H2w[word(h)] += p
ok(dict(H2w) == {"RR": F(1, 3), "RB": F(1, 6), "BR": F(1, 6), "BB": F(1, 3)},
   "RR, RB, BR, BB have probabilities 1/3, 1/6, 1/6, 1/3")
note("conditional on a full history the next-red chance is (r+1)/(n+2), e.g. after RBR it is "
     f"{F(3, 5)}; the guide's 2/3 sentence is true as the marginal one-step conditional (checked above)")
N2 = list(histories("RB", 2, "none", first_mark=1))
tot = Counter()
for h, p, _ in N2:
    tot[word(h).count("R")] += p
ok(len(N2) == 4 and {p for _, p, _ in N2} == {F(1, 4)} and
   [tot[0], tot[1], tot[2]] == [F(1, 4), F(1, 2), F(1, 4)],
   "return-only: four histories each 1/4; totals 1/4, 1/2, 1/4")

# ---------------------------------------------------------------------------
section("B. Launch figures (all three base bands) and marked example (2-3 p. 2, 4-5 p. 1)")
for band in ("k-1", "grades-2-3", "grades-4-5"):
    pg = DATA[band][0]
    bags = printed_bags(pg)
    ok(bags[:2] == [(1, 1), (2, 1)], f"{band} p.1 launch: RB -> draw R -> RRB (boxes hold {bags[:2]})")
for band, pno in (("grades-2-3", 2), ("grades-4-5", 1)):
    pg = DATA[band][pno - 1]
    row = sorted([d for d in pg["discs"] if d["label"] in ("R1", "B1", "R2") and d["cy"] < 300 and
                  abs(d["cy"] - min(x["cy"] for x in pg["discs"] if x["label"] == "R2")) < 2],
                 key=lambda d: d["cx"])
    labs = [d["label"] for d in row]
    ok(labs == ["R1", "R1", "B1", "R2", "R2"],
       f"{band} p.{pno} marked example reads R1 -> R1 B1 R2 -> R2 (got {labs}); "
       "drawing R1 then adding R2 is legal, and R2 is then drawable")

# ---------------------------------------------------------------------------
section("C. K-1")
# P1
two = {}
for r in range(3):
    fin = (r + 1, 3 - r)
    two[fin] = colour_stories(2, fin)
ok(sorted(two) == [(1, 3), (2, 2), (3, 1)], "P1: exactly three two-draw bags: 3R/1B, 2R/2B, 1R/3B")
ok([f for f, s in two.items() if len(s) >= 2] == [(2, 2)] and sorted(two[(2, 2)]) == ["BR", "RB"],
   "P1 (colour stories): only 2R/2B has two stories (RB, BR)  [K-1 key p. 3]")
pg = DATA["k-1"][0]
big = boxes_by_size(pg, 8 * 28.3465, 4 * 28.3465)
small = boxes_by_size(pg, 3.5 * 28.3465, 1.8 * 28.3465)
ok(len(big) == 3 and len(small) == 4,
   f"P1 page: {len(big)} bag boxes (= 3 bags) and {len(small)} story cells (two 2-cell rows = RB, BR)")
ident = Counter()
for h, p, bag in H2:
    ident[counts(bag, "RB")] += 1
note(f"P1 other reading - marked (which-counter) stories per bag: "
     f"{ {bag_str(k): v for k, v in sorted(ident.items())} }; every bag then has two")
# P2
pg = DATA["k-1"][1]
bags = printed_bags(pg)
ok(bags == [(4, 1), (2, 3), (5, 0), (1, 4)], f"P2 printed bags (reading order): {[bag_str(b) for b in bags]}")
poss3 = reachable(3)
for b in bags:
    st = colour_stories(3, b)
    note(f"P2 {bag_str(b)}: {'possible via ' + ', '.join(st) if st else 'impossible'}")
ok([b in poss3 for b in bags] == [True, True, False, True],
   "P2: 4R/1B, 2R/3B, 1R/4B possible; 5R/0B impossible  [K-1 key]")
missing = [b for b in poss3 if b not in bags]
ok(missing == [(3, 2)] and colour_stories(3, (3, 2)) == ["RRB", "RBR", "BRR"],
   f"P2: possible three-draw bags are {[bag_str(b) for b in poss3]}; "
   f"not printed: {[bag_str(b) for b in missing]} (stories RRB, RBR, BRR)  [key: 'also includes 3R/2B']")
cells = boxes_by_size(pg, 2.5 * 28.3465, 1.8 * 28.3465)
ok(len(cells) == 12, f"P2 page: {len(cells)} story cells = 4 bags x 3 draws; no box for a fifth bag")
# P3
pg = DATA["k-1"][2]
bags = printed_bags(pg)
ok(bags == [(3, 3)], f"P3 printed bag {bag_str(bags[0])} (6 counters = four draws)")
st = colour_stories(4, (3, 3))
ok(sorted(st) == sorted(["RRBB", "RBRB", "RBBR", "BRRB", "BRBR", "BBRR"]),
   f"P3: {len(st)} four-draw colour stories end at 3R/3B: {', '.join(st)}  [key]")
cells = boxes_by_size(pg, 1.9 * 28.3465, 1.8 * 28.3465)
ok(len(cells) == 24, f"P3 page: {len(cells)} cells = 6 rows of 4 (one row per colour story)")
H4 = list(histories("RB", 4, "copy", first_mark=1))
n33 = sum(1 for h, p, bag in H4 if counts(bag, "RB") == (3, 3))
note(f"P3 other reading - marked stories ending 3R/3B: {n33} (= 6 words x 2!2!)")
bm = [b for b in reachable(4) if b[1] > b[0]]
ok(bm == [(1, 5), (2, 4)] and colour_stories(4, (1, 5)) == ["BBBB"] and
   sorted(colour_stories(4, (2, 4))) == sorted(["RBBB", "BRBB", "BBRB", "BBBR"]),
   "P3: blue-majority four-draw bags are 1R/5B (BBBB) and 2R/4B (RBBB, BRBB, BBRB, BBBR)  [key]")
# P4
pg = DATA["k-1"][3]
bags = printed_bags(pg)
ok(bags == [(5, 1), (4, 2), (3, 3)], f"P4 printed finishes {[bag_str(b) for b in bags]}")
key = {(5, 1): [((4, 1), "R")], (4, 2): [((3, 2), "R"), ((4, 1), "B")],
       (3, 3): [((2, 3), "R"), ((3, 2), "B")]}
for fin in bags:
    pre = []
    for prev in reachable(3):
        for c, d in (("R", (1, 0)), ("B", (0, 1))):
            if (prev[0] + d[0], prev[1] + d[1]) == fin:
                pre.append((prev, c))
    ok(sorted(pre) == sorted(key[fin]),
       f"P4 {bag_str(fin)}: bags before the last draw {[(bag_str(p), c) for p, c in pre]}  [key table]")
ok(all(min(counts(bag, "RB")) >= 1 for n in range(1, 8) for _, _, bag in histories("RB", n, "copy", 1)),
   "P4/2-3 P6: no colour can vanish (all histories up to n=7)")

# ---------------------------------------------------------------------------
section("D. Grades 2-3")
ok({w: (w.count("R") + 1, w.count("B") + 1) for w in ("RR", "RB", "BR", "BB")} ==
   {"RR": (3, 1), "RB": (2, 2), "BR": (2, 2), "BB": (1, 3)},
   "P1: RR->3R/1B, RB->2R/2B, BR->2R/2B, BB->1R/3B; only 2R/2B has more than one story")
pg = DATA["grades-2-3"][0]
note(f"P1 page boxes: {len(pg['boxes'])} (2 launch + 4 two-cell stories + 4 final-bag boxes = 14)")
# P2 tree
pg = DATA["grades-2-3"][1]
roots = [d["label"] for d in pg["discs"] if d["w"] > 30]
ok(sorted(roots) == ["B1", "R1"] and len(pg["boxes"]) == 12,
   f"P2 tree: roots {roots}, {len(pg['boxes'])} boxes = 6 second-draw + 6 colour boxes")
rows = [(h[0][0] + str(h[0][1]), h[1][0] + str(h[1][1]), counts(bag, "RB"), word(h).count("R"))
        for h, p, bag in H2]
guide_rows = [("R1", "R1", (3, 1), 2), ("R1", "R2", (3, 1), 2), ("R1", "B1", (2, 2), 1),
              ("B1", "R1", (2, 2), 1), ("B1", "B1", (1, 3), 0), ("B1", "B2", (1, 3), 0)]
ok(sorted(rows) == sorted(guide_rows), "P2: the six marked histories and finals equal the guide's table")
per = Counter(r[2] for r in rows)
ok(set(per.values()) == {2}, f"P2: histories per final colours {dict(per)} - all tied, none has most")
# P3
cp = Counter()
for h, p, _ in H2:
    cp[word(h).count("R")] += p
nn = Counter()
for h, p, _ in N2:
    nn[word(h).count("R")] += p
ok([cp[i] for i in range(3)] == [F(1, 3)] * 3 and [nn[i] for i in range(3)] == [F(1, 4), F(1, 2), F(1, 4)],
   "P3: copying 1/3,1/3,1/3 (all tied); return-only 1/4,1/2,1/4 (one red greatest)")
rep_c = H2w["RR"] + H2w["BB"]
ok(rep_c == F(2, 3) and nn[0] + nn[2] == F(1, 2), "P3 key: copying raises P(repeat first colour) 1/2 -> 2/3")
# P4
H3 = list(histories("RB", 3, "copy", first_mark=1))
st = colour_stories(3, (3, 2))
pr = {w: word_prob_copy(w) for w in st}
mult = Counter(word(h) for h, _, _ in H3)
ok(sorted(st) == ["BRR", "RBR", "RRB"] and set(pr.values()) == {F(1, 12)} and
   all(mult[w] == 2 for w in st),
   "P4: 3R/2B stories RRB, RBR, BRR, each 1/12 and each 2 of 24 marked histories")
ok(F(1, 2) * F(2, 3) * F(1, 4) == F(1, 2) * F(1, 3) * F(2, 4) == F(1, 12),
   "P4 key factors (1/2)(2/3)(1/4) and (1/2)(1/3)(2/4) are the sequential draw chances and equal 1/12")
# P5
pg = DATA["grades-2-3"][3]
bags = printed_bags(pg)
ok(bags == [(5, 1), (4, 2), (3, 3)], f"P5 printed bags {[bag_str(b) for b in bags]}")
ok([len(colour_stories(4, b)) for b in bags] == [1, 4, 6] and colour_stories(4, (5, 1)) == ["RRRR"],
   "P5: 5R/1B only RRRR; 4R/2B has 4 stories; 3R/3B has 6  [key lists match]")
ok(sorted(colour_stories(4, (4, 2))) == sorted(["RRRB", "RRBR", "RBRR", "BRRR"]), "P5 key: 4R/2B list")

# ---------------------------------------------------------------------------
section("E. Grades 4-5")
ok(sorted((h[0][0] + str(h[0][1]), h[1][0] + str(h[1][1])) for h, _, _ in H2) ==
   sorted([("R1", "R1"), ("R1", "R2"), ("R1", "B1"), ("B1", "R1"), ("B1", "B1"), ("B1", "B2")]),
   "P1: the six marked histories equal the guide's list; totals tied two each")
ok(all(word_prob_copy(w) == F(1, 12) for w in ("RRB", "RBR", "BRR")), "P3: RRB, RBR, BRR each 1/12")
ok(len(H3) == 24, "P4: 24 equally likely marked histories for three draws")
c3 = Counter(word(h).count("R") for h, _, _ in H3)
ok([c3[i] for i in range(4)] == [6, 6, 6, 6], f"P4: histories per red total {[c3[i] for i in range(4)]}")
ok(mult["RRR"] == mult["BBB"] == 6 and all(mult[w] == 2 for w in mult if 0 < w.count("R") < 3)
   and len(mult) == 8, "P4 key: RRR, BBB 1x2x3 = 6 each; the six mixed words 2 each; 8 words cover 24")
c4 = Counter(word(h).count("R") for h, _, _ in H4)
ok(len(H4) == 120 and [c4[i] for i in range(5)] == [24] * 5, "P5: 120 histories, 24 per total, chance 1/5 each")
# guide's transition table: from 3-draw total t, the fourth draw adds blue (4-t identities) or red (t+1)
trans = defaultdict(lambda: [0, 0])
for h, _, _ in H4:
    r3 = word(h[:3]).count("R")
    t = word(h).count("R")
    trans[t][0 if h[3][0] == "B" else 1] += 1
key_tab = {0: (24, 0), 1: (18, 6), 2: (12, 12), 3: (6, 18), 4: (0, 24)}
ok(all(tuple(trans[t]) == key_tab[t] for t in range(5)),
   f"P5 key table (6x4,0 | 6x3,6x1 | 6x2,6x2 | 6x1,6x3 | 0,6x4): {dict((t, tuple(v)) for t, v in sorted(trans.items()))}")
H5 = list(histories("RB", 5, "copy", first_mark=1))
c5 = Counter(word(h).count("R") for h, _, _ in H5)
ok(len(H5) == 720 and set(c5.values()) == {120} and len(c5) == 6, "P6: five draws, 720 histories, 1/6 per total")

# ---------------------------------------------------------------------------
section("F. Materials arithmetic (base guide p. 2: per pair five red plus five blue)")
for n in range(1, 7):
    mx = max(max(counts(bag, "RB")) for _, _, bag in histories("RB", n, "copy", 1))
    need6 = sum(p for _, p, bag in histories("RB", n, "copy", 1) if max(counts(bag, "RB")) > 5)
    note(f"{n} draws: largest single-colour count {mx}; P(a story needs a 6th counter of one colour) = {need6}")
k1p1 = [(3, 1), (2, 2), (1, 3)]
p44 = sum(p for h, p, _ in histories("RB", 5, "copy", 1) if len(set(word(h))) == 1)
p4 = sum(p for h, p, _ in H4 if len(set(word(h))) == 1)
note(f"five draws: P(first four one colour) = {p4}, then fifth repeats it with 5/6; "
     f"P(RRRRR or BBBBB) = {p44}: the fifth copy needs a sixth counter")
note(f"K-1 P1 all three two-draw bags at once: R={sum(b[0] for b in k1p1)}, B={sum(b[1] for b in k1p1)}")
note("2-3 P1 all four story finals at once: R=8, B=8;  K-1 P4 all five predecessor bags at once: "
     f"R={4 + 3 + 4 + 2 + 3}, B={1 + 2 + 1 + 3 + 2}")

# ---------------------------------------------------------------------------
section("G. Bonus companion")
# demo figure p.1
pg = DATA["bonus"][0]
labs = [d["label"] for d in sorted(pg["discs"], key=lambda d: d["cx"])]
ok(labs == ["R0", "B0", "R0", "R0", "B0", "B1"], f"p.1 demo reads R0 B0 | draw R0 | R0 B0 B1: {labs}")
O1 = [(h, p, b) for h, p, b in histories("RB", 1, "other", first_mark=0)]
ok(sorted(counts(b, "RB") for _, _, b in O1) == [(1, 2), (2, 1)] and
   any(h[0] == ("R", 0) and ("B", 1) in b for h, _, b in O1), "p.1 demo: draw R0 under add-other adds B1")
# P1
res = {}
for rule in ("copy", "other", "none"):
    H = list(histories("RB", 2, rule, first_mark=0))
    dist = Counter()
    for h, p, _ in H:
        dist[word(h).count("R")] += p
    res[rule] = (len(H), [dist[i] for i in range(3)], {p for _, p, _ in H})
    note(f"P1 {rule:5s}: {len(H)} marked stories, each {res[rule][2]}, totals 0/1/2 = {res[rule][1]}")
ok(res["copy"][1] == [F(1, 3)] * 3 and res["other"][1] == [F(1, 6), F(2, 3), F(1, 6)] and
   res["none"][1] == [F(1, 4), F(1, 2), F(1, 4)],
   "P1 / overview: copy 2/6,2/6,2/6; other 1/6,4/6,1/6; none 1/4,2/4,1/4")
ok(max(res, key=lambda r: res[r][1][1]) == "other", "P1: add-other-colour most often gives one red and one blue")
Ho = list(histories("RB", 2, "other", first_mark=0))
one = sorted((h[0][0] + str(h[0][1]), h[1][0] + str(h[1][1])) for h, _, _ in Ho if word(h).count("R") == 1)
ok(one == sorted([("R0", "B0"), ("R0", "B1"), ("B0", "R0"), ("B0", "R1")]),
   f"P1 key: one-red opposite histories {one}")
fo = {word(h): counts(b, "RB") for h, _, b in Ho}
ok(fo == {"RR": (1, 3), "RB": (2, 2), "BR": (2, 2), "BB": (3, 1)}, "P1 key: opposite finals RR 1R/3B ... BB 3R/1B")
col = boxes_by_size(pg, 166, 285)
lines_in = [sum(1 for s in pg["segments"] if s[1] == s[3] and b[0] < s[0] < b[2] and b[1] < s[1] < b[3])
            for b in sorted(col)]
ok(len(col) == 3 and lines_in == [6, 6, 6], f"P1 page: three rule columns with {lines_in} lines "
   "(copy 6, other 6, none 4 stories)")
for n in (3, 4, 5):
    d = Counter()
    for h, p, _ in histories("RB", n, "other", first_mark=0):
        d[word(h).count("R")] += p
    note(f"P1 extension, add-other, {n} draws: totals {[str(d[i]) for i in range(n + 1)]}")
# P2
fc = {w: F(w.count("R") + 1, 6) for w in ("".join(x) for x in product("RB", repeat=4))}
ok(max(fc.values()) == F(5, 6) and [w for w in fc if fc[w] == F(5, 6)] == ["RRRR"] and
   min(fc.values()) == F(1, 6) and [w for w in fc if fc[w] == F(1, 6)] == ["BBBB"],
   "P2: most likely 5/6 only by RRRR; least 1/6 only by BBBB")
tie = sorted(w for w in fc if fc[w] == F(1, 2))
ok(tie == sorted(["RRBB", "RBRB", "RBBR", "BRRB", "BRBR", "BBRR"]), "P2: tied 1/2 by exactly the six 2R2B words")
by = Counter(fc.values())
ok(sorted(by.items()) == [(F(1, 6), 1), (F(1, 3), 4), (F(1, 2), 6), (F(2, 3), 4), (F(5, 6), 1)],
   "P2 key: forecasts 1/6..5/6 with 1,4,6,4,1 stories; RRRB, RRBR -> 2/3; RBBB, BRBB -> 1/3")
# forecast equals the true conditional chance after each marked history
good = True
for h, p, bag in H4:
    c = counts(bag, "RB")
    good &= F(c[0], sum(c)) == F(word(h).count("R") + 1, 6)
ok(good, "P2: next-red forecast (r+1)/(r+b+2) = red share of the current bag after every 4-draw history")
# P3: printed cards
pg = DATA["bonus"][2]
cards = sorted(tuple(bag["discs"]) for bag in pg["bags"] if len(bag["discs"]) == 2)
H3c = list(histories("RBG", 2, "copy", first_mark=0))
true = sorted((h[0][0] + str(h[0][1]), h[1][0] + str(h[1][1])) for h, _, _ in H3c)
ok(cards == true and len(cards) == 12, "P3: the 12 printed cards are exactly the 12 marked two-draw histories")
ok({p for _, p, _ in H3c} == {F(1, 12)}, "P3: each card 1/(3x4) = 1/12")
fb = Counter(counts(b, "RBG") for _, _, b in H3c)
ok(sorted(fb) == sorted([(3, 1, 1), (1, 3, 1), (1, 1, 3), (2, 2, 1), (2, 1, 2), (1, 2, 2)]) and
   set(fb.values()) == {2}, f"P3: six final bags, two cards each: {dict(fb)}")
ww = defaultdict(F)
for h, p, _ in H3c:
    ww[word(h)] += p
ok(ww["RR"] == F(1, 6) and ww["RG"] == F(1, 12), "P3: colour words not equal (RR 1/6, RG 1/12)")
for n in range(1, 7):
    H = list(histories("RBG", n, "copy", first_mark=0))
    vec = Counter()
    wpr = defaultdict(F)
    for h, p, bag in H:
        c = counts(bag, "RBG")
        vec[(c[0] - 1, c[1] - 1, c[2] - 1)] += 1
        wpr[word(h)] += p
    nvec = comb(n + 2, 2)
    formula = all(wpr[w] == F(2 * factorial(w.count("R")) * factorial(w.count("B")) * factorial(w.count("G")),
                               factorial(n + 2)) for w in wpr)
    ok(len(H) == factorial(n + 2) // 2 and len(vec) == nvec and set(vec.values()) == {factorial(n)}
       and formula and len(wpr) == 3 ** n,
       f"three colours n={n}: {len(H)} = (n+2)!/2 histories, {nvec} = C(n+2,2) vectors, n! = "
       f"{factorial(n)} each; word prob 2r!b!g!/(n+2)!")
H33 = list(histories("RBG", 3, "copy", first_mark=0))
m33 = Counter(word(h) for h, _, _ in H33)
ok(m33["RRR"] == 6 and m33["RRB"] == m33["RBR"] == m33["BRR"] == 2 and m33["RBG"] == 1,
   "P3 key: (3,0,0) word 6 histories; (2,1,0) three words x 2; (1,1,1) six words x 1")
ok(len(H33) == 60 and 12 * 5 == 60 and 3 ** 3 == 27, "bonus guide: 60 histories = 12 cards x 5 third identities; 27 colour words")
ok(5 * 6 == 30 and 5 * 10 == 50 and 5 * 30 == 150 and 5 * 2 == 10,
   "bonus guide, eleven children: 5 kits x 6 = 30 per colour, 50 cards, 150 slips, 10 sheets")
for n, rule, cols in ((4, "copy", "RB"), (2, "other", "RB"), (3, "copy", "RBG")):
    mx = max(max(counts(b, cols)) for _, _, b in histories(cols, n, rule, 0))
    note(f"bonus materials: {rule} {cols} {n} draws needs at most {mx} of one colour (kit: six per colour)")

# ---------------------------------------------------------------------------
section("H. Printed guide text against its source (rendering)")
gtxt = " ".join(p["text"] for p in DATA["bonus-guide"])
gtxt = re.sub(r"\s+", " ", gtxt)
src = (BONUS_SRC / "guide.md").read_text()
for s_src in re.findall(r"\d\*\d\*[^ ;,]*", src):
    note(f"guide.md has '{s_src}'")
prod = re.search(r"the one color word has (\S+) identity histories", gtxt).group(1)
ok(prod in ("1*2*3=6", "1×2×3=6", "1·2·3=6"),
   f"bonus guide p.3 prints the product for (3,0,0) correctly (printed '{prod}'; guide.md has '1*2*3=6')")
tot = re.search(r"Total histories are (\S+)=\(n\+2\)!/2", gtxt).group(1)
ok(tot in ("3*4*...*(n+2)", "3×4×...×(n+2)", "3·4·...·(n+2)"),
   f"bonus guide p.3 prints the total-histories product correctly (printed '{tot}'; guide.md has '3*4*...*(n+2)')")
m = re.search(r"Total histories are ([^=]*)=", gtxt)
note(f"printed: 'Total histories are {m.group(1)}=(n+2)!/2'")

print()
print("FAILURES:", len(FAILS))
for f in FAILS:
    print("  " + f)
