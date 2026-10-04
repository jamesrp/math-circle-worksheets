#!/usr/bin/env python3
"""Recompute every answer printed in the Week 6 adult guide (facilitator.tex).

Puzzles, boards and trays are read from the student sources in ../src/*.tex,
so the answers are tied to what is printed on the pages.  Nothing here uses
the student sources' comments, the authors' scripts, or the reviews.

Run:  python3 check_guide.py      (exits non-zero if any printed answer is wrong)
It also writes lookup3.tex, the score table used in the guide.
"""
import re
import sys
from itertools import product, combinations
from functools import lru_cache
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE.parent / "src"
FAIL = []


def check(label, got, want):
    ok = got == want
    print(f"[{'ok' if ok else 'FAIL'}] {label}: {got}" + ("" if ok else f"   (guide says {want})"))
    if not ok:
        FAIL.append(label)


def codes(n):
    return ["".join(p) for p in product("RY", repeat=n)]


def score(t, s):
    return sum(a == b for a, b in zip(t, s))


def flip(row, places):
    return "".join(("Y" if c == "R" else "R") if i in places else c for i, c in enumerate(row))


# ---------------------------------------------------------------- read pages
tex = {b: (SRC / f"{b}.tex").read_text() for b in ("k-1", "grades-2-3", "grades-4-5")}


def problems(src):
    """Split a packet source into problems (list of source chunks, Problem 1 first)."""
    body = src.split(r"\begin{document}", 1)[1]
    return body.split(r"\problem")[1:]


def parse_rows(spec):
    return [(c, int(sc)) for c, sc in (x.split("/") for x in spec.split(","))]


P = {b: problems(t) for b, t in tex.items()}
print("problems per packet:", {b: len(v) for b, v in P.items()})
check("K-1 / 2-3 / 4-5 problem counts", tuple(len(P[b]) for b in P), (9, 11, 10))

# ---------------------------------------------------------------- blocks
BLOCKS = ["green triangle", "blue rhombus", "red trapezoid", "yellow hexagon",
          "purple chevron", "pink right triangle", "teal kite", "gray dart"]
SIDES = {"green triangle": 3, "blue rhombus": 4, "red trapezoid": 4, "yellow hexagon": 6,
         "purple chevron": 6, "pink right triangle": 3, "teal kite": 4, "gray dart": 4}
# side counts recomputed from the polygon coordinates in common.tex
common = (SRC / "common.tex").read_text()
for name, macro in [("green triangle", "bTri"), ("blue rhombus", "bRhombus"), ("red trapezoid", "bTrap"),
                    ("yellow hexagon", "bHex"), ("purple chevron", "bChevron"),
                    ("pink right triangle", "bRight"), ("teal kite", "bKite"), ("gray dart", "bDart")]:
    m = re.search(r"\\newcommand\{\\" + macro + r"\}\{\\blockpic\{\w+\}\{(.*?)\}\{" + name + r"\}\}", common)
    pts = re.findall(r"\(([-\d.]+),([-\d.]+)\)", m.group(1))
    check(f"sides of {name} (drawing)", len(pts), SIDES[name])
check("K-1 P1 shows the first four blocks", r"\fourblocks" in P["k-1"][0], True)


def worst_questions(n):
    """Fewest yes/no questions that always single out one of n things."""
    return 0 if n <= 1 else 1 + worst_questions((n + 1) // 2)


check("K-1 P1: two questions always find 1 of 4 blocks", worst_questions(4) <= 2, True)
check("K-1 P2 / 2-3 P1: point-only, most questions before sure (8 blocks)", 8 - 1, 7)
check("K-1 P2: point-only, if the round ends only on a yes", 8, 8)
check("K-1 P3 / 2-3 P2: three questions always find 1 of 8", worst_questions(8), 3)
check("K-1 P4 / 2-3 P3: answer patterns from two questions", 2 ** 2, 4)
check("K-1 P4 / 2-3 P3: two questions can be enough for 8 blocks", 2 ** 2 >= 8, False)

# The example questions printed in the guide.
TOP = set(BLOCKS[:4])
Q1 = lambda b: b in TOP                                   # top row of the page
Q2 = lambda b: SIDES[b] == 4                              # exactly four sides
Q3 = lambda b: b.split()[0] in ("red", "yellow", "purple", "gray")
pats = {b: (Q1(b), Q2(b), Q3(b)) for b in BLOCKS}
check("2-3 P2 example: 8 different answer patterns", len(set(pats.values())), 8)
for b in BLOCKS:
    print("      ", b, "".join("Y" if x else "N" for x in pats[b]))
# K-1 P1 example on the four blocks: 'four sides?' then 'is it blue / is it the triangle?'
four = BLOCKS[:4]
check("K-1 P1 example: four sides? splits 4 into 2+2",
      sorted(len([b for b in four if Q2(b) == v]) for v in (True, False)), [2, 2])
# K-1 P3 example: top row? then four sides? then one block -> each step halves
groups = {}
for b in BLOCKS:
    groups.setdefault((Q1(b), Q2(b)), []).append(b)
check("K-1 P3 example: top row? + four sides? leave 2 each", sorted(len(g) for g in groups.values()), [2, 2, 2, 2])

# ---------------------------------------------------------------- numbers
check("4-5 P1: 1 to 16", worst_questions(16), 4)
check("4-5 P1: 3 questions give fewer than 16 patterns", 2 ** 3 < 16, True)
check("4-5 P1: 1 to 20", worst_questions(20), 5)
check("4-5 P1: 4 questions give fewer than 20 patterns", 2 ** 4 < 20, True)
check("fallback 2-3: 1 to 16", worst_questions(16), 4)
check("fallback 4-5: 1 to 100", worst_questions(100), 7)
check("fallback 4-5: 6 questions give fewer than 100 patterns", 2 ** 6 < 100, True)

# ---------------------------------------------------------------- code game minimax


def partition(test, cands):
    parts = {}
    for s in cands:
        parts.setdefault(score(test, s), []).append(s)
    return parts


def know_min(n):
    allc = codes(n)

    @lru_cache(None)
    def f(cands):
        if len(cands) <= 1:
            return 0
        best = 10 ** 9
        for t in allc:
            parts = partition(t, cands)
            if len(parts) == 1:
                continue
            best = min(best, 1 + max(f(tuple(v)) for v in parts.values()))
        return best
    return f(tuple(allc))


def hit_min(n):
    """Fewest tests that always include one scoring n (game ends on a full score)."""
    allc = codes(n)
    full = "R" * n

    @lru_cache(None)
    def g(cands):
        best = 10 ** 9
        for t in allc:
            parts = partition(t, cands)
            worst = 0
            for sc, v in parts.items():
                if sc == n:
                    worst = max(worst, 1)
                elif len(v) == len(cands):
                    worst = 10 ** 9   # no progress
                    break
                else:
                    worst = max(worst, 1 + g(tuple(v)))
            best = min(best, worst)
        return best
    return g(tuple(allc))


KNOW = {n: know_min(n) for n in (2, 3, 4)}
HIT = {n: hit_min(n) for n in (2, 3, 4)}
check("fewest tests that always tell the secret, n=2,3,4", (KNOW[2], KNOW[3], KNOW[4]), (2, 3, 4))
check("fewest tests to end on a full score, n=2,3,4", (HIT[2], HIT[3], HIT[4]), (3, 4, 5))

# Answers that follow
check("K-1 P5 / number of 2-counter secrets", len(codes(2)), 4)
check("K-1 P8 / number of 3-counter secrets", len(codes(3)), 8)
check("K-1 P6 / 2-3 P5: one test always enough for 2 counters", KNOW[2] <= 1, False)
check("K-1 P6 / 2-3 P5: two tests always enough for 2 counters", KNOW[2] <= 2, True)
check("K-1 P9 / 2-3 P8 / 4-5 P4: three tests always enough for 3 counters", KNOW[3] <= 3, True)
check("2-3 P9: game ending on score 3 always ends by test 4", HIT[3] <= 4, True)
check("2-3 P11 / 4-5 P6: four tests always enough for 4 counters", KNOW[4] <= 4, True)
check("4-5 P8: two tests always enough for 3 counters", KNOW[3] <= 2, False)
check("4-5 P9: three tests always enough for 4 counters", KNOW[4] <= 3, False)
check("4-5 P10: tests needed to end, 3 and 4 counters", (HIT[3], HIT[4]), (4, 5))

# trays and boards on the pages
k1 = P["k-1"]
check("K-1 P5 two-counter trays printed", k1[4].count(r"\slotrow{2}"), 6)
check("K-1 P8 three-counter trays printed", k1[7].count(r"\slotrow{3}"), 10)
boards = {b: [tuple(map(int, m)) for m in re.findall(r"\\board\{(\d)\}\{(\d)\}", tex[b])] for b in tex}
check("boards (counters, test rows) per packet", boards,
      {"k-1": [(2, 3), (3, 4)], "grades-2-3": [(2, 3), (3, 4), (4, 4)], "grades-4-5": [(3, 4), (4, 4)]})
for b, lst in boards.items():
    for n, rows in lst:
        check(f"{b} {n}-counter board has rows for a sure strategy", rows >= KNOW[n], True)
COUNTERS_FULL = {n: n + n + n * rows for n, rows in [(2, 3), (3, 4), (4, 4)]}
check("counters to fill a whole board (secret+copy+tests), n=2,3,4", COUNTERS_FULL, {2: 10, 3: 18, 4: 24})
check("K-1 pair: 8 three-counter secrets laid out + full 3-counter board", 8 * 3 + COUNTERS_FULL[3], 42)

# ---------------------------------------------------------------- printed strategies


def nonadaptive_ok(tests, n):
    return len({tuple(score(t, s) for t in tests) for s in codes(n)}) == 2 ** n


def one_at_a_time(n):
    """All red, then turn over place 1, 2, ..., n-1 (one at a time, from all red)."""
    return ["R" * n] + [flip("R" * n, {i}) for i in range(n - 1)]


for n in (2, 3, 4):
    tests = one_at_a_time(n)
    check(f"change-one-at-a-time tests {tests} tell every {n}-counter secret", nonadaptive_ok(tests, n), True)
    # rule: score of test i+1 is (number of reds) - 1 if place i is red, + 1 if yellow
    rule = all(score(tests[i + 1], s) == s.count("R") + (1 if s[i] == "Y" else -1)
               for s in codes(n) for i in range(n - 1))
    check(f"n={n}: first score = reds; turning over place i moves the score -1 (red) / +1 (yellow)",
          rule and all(score("R" * n, s) == s.count("R") for s in codes(n)), True)
    check(f"n={n}: testing every place without the count needs", len(one_at_a_time(n)) + 1, n + 1)

# K-1 two-counter plan: RR; if 1, then RY
plan2 = {}
for s in codes(2):
    a = score("RR", s)
    plan2[s] = ("RR", a) if a != 1 else ("RR", a, "RY", score("RY", s))
check("K-1 P6 plan: RR then (if 1) RY separates all four",
      len(set(plan2.values())), 4)
check("K-1 P6: after RR scores 1, second tests that separate RY and YR",
      sorted(t for t in codes(2) if score(t, "RY") != score(t, "YR")), ["RY", "YR"])
check("one test, 2 counters: every test gives score 1 to two secrets",
      all(sum(score(t, s) == 1 for s in codes(2)) == 2 for t in codes(2)), True)

# small facts printed in the guide
check("K-1 P8: three-counter secrets with 3, 2, 1, 0 reds",
      [sum(c.count("R") == r for c in codes(3)) for r in (3, 2, 1, 0)], [1, 3, 3, 1])
check("2-3 P5: fixed tests RR and RY give (RR, RY, YR, YY) these score pairs",
      [(score("RR", s), score("RY", s)) for s in ("RR", "RY", "YR", "YY")], [(2, 1), (1, 2), (1, 0), (0, 1)])
check("one test RR settles a 2-counter secret when it scores", sorted(sc for sc in range(3)
      if sum(score("RR", s) == sc for s in codes(2)) == 1), [0, 2])
check("launch: secret RY scores RR and RY", (score("RR", "RY"), score("RY", "RY")), (1, 2))
check("sharing: 2-counter secrets vs possible scores of one test", (len(codes(2)), len({0, 1, 2})), (4, 3))

# lookup table for the guide (3 counters)
T3 = one_at_a_time(3)
rows = []
for s in sorted(codes(3), key=lambda c: (-c.count("R"), c)):
    rows.append(rf"\cd{{{s}}} & " + " & ".join(str(score(t, s)) for t in T3) + r" \\")
(HERE / "lookup3.tex").write_text(
    "% generated by check_guide.py\n"
    r"\begin{tabular}{@{}l ccc@{}}\toprule" "\n"
    r"Secret & \cd{RRR} & \cd{YRR} & \cd{RYR} \\\midrule" "\n"
    + "\n".join(rows) + "\n" r"\bottomrule\end{tabular}" "\n")

# ---------------------------------------------------------------- puzzles from the pages
PRINTED = {
    ("k-1", 6, 0): ["RR"], ("k-1", 6, 1): ["YR"], ("k-1", 6, 2): ["RY", "YR"],
    ("k-1", 6, 3): ["RY"], ("k-1", 6, 4): ["YY"],
    ("grades-2-3", 6, 0): ["RRY", "RYR", "YRR"], ("grades-2-3", 6, 1): ["YRR", "YYY"],
    ("grades-2-3", 6, 2): ["RRY"], ("grades-2-3", 6, 3): ["RRR"], ("grades-2-3", 6, 4): [],
    ("grades-4-5", 2, 0): ["RRR"], ("grades-4-5", 2, 1): ["RRY", "RYR"],
    ("grades-4-5", 2, 2): ["RYYY"], ("grades-4-5", 2, 3): ["RRRR", "YYYY"],
    ("grades-4-5", 2, 4): [],
}
found = {}
for b, pnum, pat in [("k-1", 6, r"\\kpuzzle\{([RY/0-9,]+)\}"),
                     ("grades-2-3", 6, r"\\puzzlebox\{\d\}\{([RY/0-9,]+)\}"),
                     ("grades-4-5", 2, r"\\puzzlebox\{\d\}\{([RY/0-9,]+)\}")]:
    specs = re.findall(pat, P[b][pnum])
    for k, spec in enumerate(specs):
        recs = parse_rows(spec)
        n = len(recs[0][0])
        sols = [s for s in codes(n) if all(score(t, s) == sc for t, sc in recs)]
        found[(b, pnum, k)] = sols
        check(f"{b} P{pnum + 1} game {k + 1} {spec}", sols, PRINTED[(b, pnum, k)])
check("all printed puzzles found on pages", sorted(found) == sorted(PRINTED), True)
check("K-1 P7: no row needs more than the 2 trays", max(len(v) for k, v in found.items() if k[0] == "k-1") <= 2, True)

# explanations of the impossible puzzles
check("2-3 P7 game 5: RRR scoring 3 forces RRR, which scores on RYR", score("RYR", "RRR"), 2)
par = all(len({score(t, s) % 2 for t in ("RYRY", "RRYY", "YYYY")}) == 1 for s in codes(4))
check("4-5 P3 game 5: tests with even #Y give scores all of one parity", par, True)
check("4-5 P3 game 5: tests differ in 2 places -> scores differ by 0 or 2",
      all(abs(score("RRYY", s) - score("YYYY", s)) in (0, 2) for s in codes(4)), True)

# 2-3 P7 game 3: is every row needed?
g3 = parse_rows(re.findall(r"\\puzzlebox\{\d\}\{([RY/0-9,]+)\}", P["grades-2-3"][6])[2])
check("2-3 P7 game 3: secrets fitting each single row",
      [len([s for s in codes(3) if score(t, s) == sc]) for t, sc in g3], [3, 3, 3])

# ---------------------------------------------------------------- symmetry and proofs
check("4-5 P7: turning over one place in both rows keeps the score",
      all(score(t, s) == score(flip(t, {j}), flip(s, {j}))
          for n in (2, 3, 4) for t in codes(n) for s in codes(n) for j in range(n)), True)

# one-flip argument (4-5 P8, 3 counters): neighbours of test 1 get only two scores on any test 2
ok = True
for t1 in codes(3):
    nb = [flip(t1, {i}) for i in range(3)]
    for t2 in codes(3):
        vals = {score(t2, s) for s in nb}
        base = score(t2, t1)
        ok &= len(vals) <= 2 and vals <= {base - 1, base + 1}
        ok &= all(score(t1, s) == 2 for s in nb)
check("4-5 P8: three secrets one flip from test 1 get at most 2 scores on any test 2", ok, True)

# two-flip argument (4-5 P9, 4 counters)
ok = True
splits = set()
for t1 in codes(4):
    two = [flip(t1, set(q)) for q in combinations(range(4), 2)]
    assert all(score(t1, s) == 2 for s in two)
    for t2 in codes(4):
        D = {i for i in range(4) if t2[i] != t1[i]}
        base = score(t2, t1)
        for q in combinations(range(4), 2):
            s = flip(t1, set(q))
            ok &= score(t2, s) == base - 2 + 2 * len(D & set(q))
        parts = partition(t2, two)
        splits.add(tuple(sorted(len(v) for v in parts.values())))
        big = [v for v in parts.values() if len(v) >= 3]
        ok &= bool(big)
        for v in big:
            for t3 in codes(4):
                ok &= len(partition(t3, v)) < len(v)
check("4-5 P9: score formula base-2+2|Q&D| and no test 2, test 3 separate the six", ok, True)
check("4-5 P9: ways a test splits the six two-flip secrets", sorted(splits), [(1, 1, 4), (3, 3), (6,)])

# reduction used in 4-5 P10: a way that ends by test n would know after n-1 tests
check("4-5 P10: hit = know + 1 for n=2,3,4", all(HIT[n] == KNOW[n] + 1 for n in (2, 3, 4)), True)

# where it goes: five counters, four fixed tests are enough
five = codes(5)
four_ok = next((ts for ts in combinations(five, 4) if nonadaptive_ok(ts, 5)), None)
check("5 counters: some 4 fixed tests tell every secret", four_ok is not None, True)
print("      example:", four_ok)
check("5 counters: fewest tests that always tell the secret", know_min(5), 4)

print()
if FAIL:
    print("FAILED:", FAIL)
    sys.exit(1)
print("all printed answers check out")
