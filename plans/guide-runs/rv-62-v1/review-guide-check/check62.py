#!/usr/bin/env python3
"""Independent reviewer check for the Week 62 return-visit facilitator guide.

Written by the reviewer, without reading the writer's check_guide.py or the
student-page generator (instances.py, mathlib.py).  Boards were transcribed by
eye from the rendered final student PDFs; the working boards (20 mm circles,
lines, arrows, allowed-slot labels) are also parsed from the generated TeX and
compared with the transcription.  Every answer the guide prints is then
re-derived by brute force.

Usage: python3 -I check62.py [path-to-student-src]
"""
import os as _os
_REPO = _os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "..", "..", ".."))
import itertools
import math
import re
import sys
from collections import deque

SRC = sys.argv[1] if len(sys.argv) > 1 else \
    _REPO + "/plans/return-visit-drafts/week-62/src"

FAIL = []


def check(cond, msg):
    print(("ok   " if cond else "FAIL ") + msg)
    if not cond:
        FAIL.append(msg)


def E(s):
    """'AB BC' -> set of frozenset edges."""
    return {frozenset(p) for p in s.split()}


def L(s):
    """'A:13 B:2' -> dict of allowed lists."""
    out = {}
    for tok in s.split():
        k, v = tok.split(":")
        out[k] = tuple(int(c) for c in v)
    return out


def ring(letters):
    return {frozenset((letters[i], letters[(i + 1) % len(letters)]))
            for i in range(len(letters))}


# ---------------------------------------------------------------------------
# Transcription from the rendered final PDFs (reviewer's own reading)
# ---------------------------------------------------------------------------
STAR5 = E("AB AC AD AE AF")
SQUARE = E("AB BC CD DA")
TRI = E("AB BC CA")
SIXCARD = E("AC AD AE AF BC BD BE BF")
FIVECARD = E("AC AD AE BC BD BE")
TREE8 = E("CB BH HA HD DE DF FG")
RING6LEAVES = ring("ABCDEF") | E("GA HD")
RING5LEAF = ring("ABCDE") | E("AF")

K1_LIST = [  # (problem, edges, lists)
    ("K1 P1 path", E("AB BC"), L("A:2 B:23 C:13")),
    ("K1 P1 triangle", TRI, L("A:12 B:1 C:123")),
    ("K1 P1 star", E("AB AC AD"), L("A:123 B:1 C:2 D:13")),
    ("K1 P1 square", SQUARE, L("A:1 B:12 C:123 D:13")),
    ("K1 P2 triangle", TRI, L("A:12 B:12 C:12")),
    ("K1 P2 square", SQUARE, L("A:12 B:12 C:12 D:12")),
    ("K1 P2 path3", E("AB BC"), L("A:1 B:12 C:2")),
    ("K1 P2 path4", E("AB BC CD"), L("A:1 B:12 C:23 D:13")),
    ("K1 P3 six-ring", ring("ABCDEF"), L("A:1 B:12 C:23 D:13 E:12 F:13")),
    ("K1 P3 AB-CDE", FIVECARD, L("A:123 B:124 C:1 D:2 E:3")),
]
M_LIST = [
    ("M P1 tree", TREE8, L("A:24 B:23 C:13 D:13 E:14 F:23 G:2 H:12")),
    ("M P1 ring+leaves", RING6LEAVES,
     L("A:13 B:12 C:23 D:23 E:24 F:14 G:3 H:3")),
    ("M P2 five-ring 12", ring("ABCDE"), L("A:12 B:12 C:12 D:12 E:12")),
    ("M P2 five-ring C13", ring("ABCDE"), L("A:12 B:12 C:13 D:12 E:12")),
    ("M P2 six-ring 12", ring("ABCDEF"),
     L("A:12 B:12 C:12 D:12 E:12 F:12")),
    ("M P2 five-ring leaf 23", RING5LEAF,
     L("A:23 B:23 C:23 D:23 E:23 F:13")),
    ("M P3 six-card top", SIXCARD,
     L("A:12 B:34 C:13 D:14 E:23 F:24")),
    ("M P3 six-card bottom", SIXCARD,
     L("A:12 B:34 C:13 D:14 E:23 F:34")),
]
U_LIST = [
    ("U P1 six-card top", SIXCARD, L("A:12 B:34 C:13 D:14 E:23 F:24")),
    ("U P1 six-card bottom", SIXCARD, L("A:12 B:34 C:13 D:14 E:23 F:34")),
    ("U P4 five-ring 12", ring("ABCDE"), L("A:12 B:12 C:12 D:12 E:12")),
    ("U P4 five-ring mixed", ring("ABCDE"), L("A:12 B:23 C:13 D:12 E:23")),
    ("U P4 ring+leaf", RING5LEAF, L("A:12 B:12 C:13 D:12 E:12 F:12")),
    ("U P4 six-ring 34", ring("ABCDEF"),
     L("A:34 B:34 C:34 D:34 E:34 F:34")),
]
# Blank boards (lists to be invented): edges and printed fixed lists
M_P4 = [("M P4 six-card, A fixed 13", SIXCARD, L("A:13")),
        ("M P4 five-card, A fixed 13", FIVECARD, L("A:13"))]
U_P2 = ("U P2 five-card", FIVECARD, {})
U_P3 = ("U P3 tree", TREE8, {})

# Arrow boards (u, v) means u -> v
def A(s):
    return [tuple(p) for p in s.split()]

ARROW_P9 = A("AB BC CD EB FC GH")
M_P10 = [("M P10 UL", A("AB BC CA")), ("M P10 UR", A("AB BC CD DE")),
         ("M P10 LL", A("AD BD BE CE DF EF FG")),
         ("M P10 LR", A("AD BD BE CE DF EF FG ED"))]
U_P10 = [("U P10 top", A("HA AC BC CF GD DE EF")),
         ("U P10 bottom", A("HA AC BC CF GD DE EF EC"))]


# ---------------------------------------------------------------------------
# TeX parse of working boards (20 mm circles) for comparison
# ---------------------------------------------------------------------------
NUM = r"(-?[\d.]+)"


def parse_boards(path):
    text = open(path).read()
    pics = re.findall(r"\\begin\{tikzpicture\}(.*?)\\end\{tikzpicture\}", text,
                      re.S)
    boards = []
    for pic in pics:
        circ = {}
        for m in re.finditer(r"\\draw\[line width=0\.9pt, fill=white\] \(" + NUM
                             + "," + NUM + r"\) circle \(10\.0mm\);\s*\\node\[font=\\Large\\bfseries\] at \("
                             + NUM + "," + NUM + r"\) \{([A-H])\};", pic):
            circ[m.group(5)] = (float(m.group(1)), float(m.group(2)))
        if not circ:
            continue
        pos2l = {v: k for k, v in circ.items()}

        def at(x, y):
            for (cx, cy), k in pos2l.items():
                if abs(cx - x) < 0.05 and abs(cy - y) < 0.05:
                    return k
            return None
        edges, arrows = set(), []
        for m in re.finditer(r"\\draw\[line width=0\.9pt(,midarrow)?\] \(" + NUM
                             + "," + NUM + r"\) -- \(" + NUM + "," + NUM + r"\);", pic):
            a = at(float(m.group(2)), float(m.group(3)))
            b = at(float(m.group(4)), float(m.group(5)))
            if a and b:
                if m.group(1):
                    arrows.append((a, b))
                else:
                    edges.add(frozenset((a, b)))
        lists = {}
        for m in re.finditer(r"\\node\[font=\\large\\bfseries, inner sep=0\.5mm, anchor=[\d]+\] at \("
                             + NUM + "," + NUM + r"\) \{([\d\\,]+)\};", pic):
            x, y = float(m.group(1)), float(m.group(2))
            nums = tuple(int(c) for c in re.findall(r"\d", m.group(3)))
            # nearest working circle
            best = min(circ, key=lambda k: math.hypot(circ[k][0] - x, circ[k][1] - y))
            d = math.hypot(circ[best][0] - x, circ[best][1] - y)
            others = sorted(math.hypot(circ[k][0] - x, circ[k][1] - y)
                            for k in circ if k != best)
            lists[best] = nums
            if others and others[0] < d + 6:
                print(f"   note: label {nums} near {best} ({d:.1f} mm) is "
                      f"within {others[0]:.1f} mm of another circle")
        boards.append(dict(circles=sorted(circ), edges=edges, arrows=arrows,
                           lists=lists))
    return boards


def same_graph(b, edges, lists, arrows=None):
    ok = b["edges"] == set(edges) if arrows is None else \
        sorted(b["arrows"]) == sorted(arrows)
    if lists is not None:
        ok = ok and b["lists"] == lists
    return ok


# ---------------------------------------------------------------------------
# Solvers
# ---------------------------------------------------------------------------
def vertices(edges, lists=None):
    vs = set()
    for e in edges:
        vs |= set(e)
    if lists:
        vs |= set(lists)
    return sorted(vs)


def list_solutions(edges, lists):
    vs = vertices(edges, lists)
    sols = []
    for combo in itertools.product(*(lists[v] for v in vs)):
        col = dict(zip(vs, combo))
        if all(col[a] != col[b] for a, b in map(tuple, edges)):
            sols.append("".join(str(col[v]) for v in vs))
    return sols


def legal(state, vs, edges):
    col = dict(zip(vs, state))
    return all(col[a] != col[b] for a, b in map(tuple, edges))


def neighbours(edges, v):
    return [next(iter(e - {v})) for e in edges if v in e]


def moves_from(state, vs, edges, k):
    idx = {v: i for i, v in enumerate(vs)}
    for i, v in enumerate(vs):
        blocked = {state[idx[u]] for u in neighbours(edges, v)}
        for c in range(1, k + 1):
            if c != state[i] and c not in blocked:
                yield v + str(c), state[:i] + (c,) + state[i + 1:]


def bfs(edges, start, goal, k):
    vs = vertices(edges)
    s = tuple(start[v] for v in vs)
    g = tuple(goal[v] for v in vs)
    prev = {s: None}
    q = deque([s])
    while q:
        cur = q.popleft()
        if cur == g:
            path = []
            while prev[cur]:
                cur, mv = prev[cur]
                path.append(mv)
            return path[::-1]
        for mv, nxt in moves_from(cur, vs, edges, k):
            if nxt not in prev:
                prev[nxt] = (cur, mv)
                q.append(nxt)
    return None


def replay(edges, start, word, k):
    vs = vertices(edges)
    col = dict(start)
    for mv in word.split():
        v, c = mv[0], int(mv[1:])
        if c == col[v] or c < 1 or c > k:
            return None
        if any(col[u] == c for u in neighbours(edges, v)):
            return None
        col[v] = c
    return col


def S(s, letters="ABCDEFGH"):
    return {letters[i]: int(c) for i, c in enumerate(s)}


def legal_states(edges, k):
    vs = vertices(edges)
    return [st for st in itertools.product(range(1, k + 1), repeat=len(vs))
            if legal(st, vs, edges)]


def components(edges, k):
    vs = vertices(edges)
    states = legal_states(edges, k)
    seen, comps = set(), []
    for s in states:
        if s in seen:
            continue
        comp, q = {s}, deque([s])
        seen.add(s)
        while q:
            cur = q.popleft()
            for _, nxt in moves_from(cur, vs, edges, k):
                if nxt not in seen:
                    seen.add(nxt)
                    comp.add(nxt)
                    q.append(nxt)
        comps.append(comp)
    return comps


def stuck_states(edges, k):
    vs = vertices(edges)
    return [s for s in legal_states(edges, k)
            if not any(True for _ in moves_from(s, vs, edges, k))]


def longest_path_cards(arrows):
    vs = sorted({x for a in arrows for x in a})
    succ = {v: [b for a, b in arrows if a == v] for v in vs}
    memo, onstack = {}, set()

    def lp(v):
        if v in onstack:
            raise ValueError("cycle")
        if v in memo:
            return memo[v]
        onstack.add(v)
        r = 1 + max((lp(w) for w in succ[v]), default=0)
        onstack.discard(v)
        memo[v] = r
        return r
    try:
        return max(lp(v) for v in vs)
    except ValueError:
        return None


def min_headers(arrows, cap=6):
    """Brute force: fewest k such that every arrow goes to a strictly larger slot."""
    vs = sorted({x for a in arrows for x in a})
    for k in range(1, cap + 1):
        for combo in itertools.product(range(1, k + 1), repeat=len(vs)):
            col = dict(zip(vs, combo))
            if all(col[a] < col[b] for a, b in arrows):
                return k
    return None


def schedule_ok(arrows, sched, k):
    slot = {}
    for s, cards in sched.items():
        for c in cards:
            slot[c] = s
    vs = {x for a in arrows for x in a}
    return set(slot) == vs and max(slot.values()) <= k and \
        all(slot[a] < slot[b] for a, b in arrows)


def earliest(arrows):
    vs = sorted({x for a in arrows for x in a})
    slot = {}
    changed = True
    for v in vs:
        slot[v] = 1
    for _ in range(len(vs)):
        for a, b in arrows:
            if slot[b] < slot[a] + 1:
                slot[b] = slot[a] + 1
    return slot


def two_sets():
    return list(itertools.combinations((1, 2, 3, 4), 2))


def count_failing(edges, fixed, blanks):
    pairs = two_sets()
    fails, total = [], 0
    for combo in itertools.product(pairs, repeat=len(blanks)):
        lists = dict(fixed)
        lists.update(dict(zip(blanks, combo)))
        total += 1
        if not has_solution(edges, lists):
            fails.append(combo)
    return fails, total


def has_solution(edges, lists):
    vs = vertices(edges, lists)
    nb = {v: neighbours(edges, v) for v in vs}
    order = sorted(vs, key=lambda v: len(lists[v]))
    col = {}

    def go(i):
        if i == len(order):
            return True
        v = order[i]
        for c in lists[v]:
            if all(col.get(u) != c for u in nb[v]):
                col[v] = c
                if go(i + 1):
                    return True
                del col[v]
        return False
    return go(0)


def tree_never_fails(edges):
    """Every two-number assignment from 1-4 on a tree works: check via the
    rooted argument by DP (count failing assignments exactly, no shortcut)."""
    vs = vertices(edges)
    pairs = two_sets()
    nb = {v: neighbours(edges, v) for v in vs}
    root = vs[0]
    # number of failing assignments = total - #assignments with a colouring.
    # Use DP over (list, colour) feasibility sets.  For exactness, enumerate
    # the set of colours feasible at the root given the subtree's lists, per
    # subtree, as a distribution over frozensets.
    from collections import Counter

    def dist(v, parent):
        # returns Counter mapping (frozenset of feasible colours at v) -> count
        child_dists = [dist(u, v) for u in nb[v] if u != parent]
        out = Counter()
        for lst in pairs:
            # combine children: colour c feasible at v iff for every child,
            # child's feasible set contains a colour != c
            partial = Counter({frozenset(lst): 1})
            for cd in child_dists:
                new = Counter()
                for feas, n1 in partial.items():
                    for cfeas, n2 in cd.items():
                        f = frozenset(c for c in feas if cfeas - {c})
                        new[f] += n1 * n2
                partial = new
            out.update(partial)
        return out
    d = dist(root, None)
    total = sum(d.values())
    failing = sum(n for f, n in d.items() if not f)
    return failing, total


def orientations(edges):
    el = [tuple(sorted(e)) for e in edges]
    for bits in itertools.product((0, 1), repeat=len(el)):
        yield [(a, b) if t == 0 else (b, a) for (a, b), t in zip(el, bits)]


# ---------------------------------------------------------------------------
# 1. Compare transcription with TeX parse
# ---------------------------------------------------------------------------
print("== Transcription vs generated TeX (working boards) ==")
kb = parse_boards(f"{SRC}/k-1.tex")
mb = parse_boards(f"{SRC}/grades-2-3.tex")
ub = parse_boards(f"{SRC}/grades-4-5.tex")
print(f"   working boards parsed: K-1 {len(kb)}, 2-3 {len(mb)}, 4-5 {len(ub)}")

k_expect = [(e, l) for _, e, l in K1_LIST] + [
    (E("AB"), {}), (E("AB"), {}), (E("AB BC"), {}), (STAR5, {}), (SQUARE, {}),
    (TRI, {}), (TRI, {})]
for i, (b, (e, l)) in enumerate(zip(kb, k_expect)):
    check(same_graph(b, e, l), f"K-1 working board {i + 1} matches transcription")
check(len(kb) == len(k_expect), "K-1 board count")

m_expect = [(e, l) for _, e, l in M_LIST] + [
    (SIXCARD, L("A:13")), (FIVECARD, L("A:13")),
    (E("AB"), {}), (E("AB BC"), {}), (E("AB BC CD"), {}), (STAR5, {}),
    (TRI, {}), (TRI, {}),
    (ring("ABCD"), {}), (ring("ABCDE"), {}), (ring("ABCDEF"), {}),
    (ring("ABCDEFG"), {})]
for i, (b, (e, l)) in enumerate(zip(mb, m_expect)):
    check(same_graph(b, e, l), f"2-3 working board {i + 1} matches transcription")
m_arrow = [ARROW_P9] + [a for _, a in M_P10]
for i, (b, a) in enumerate(zip(mb[len(m_expect):], m_arrow)):
    check(same_graph(b, None, None, a), f"2-3 arrow board {i + 1} matches transcription")
check(len(mb) == len(m_expect) + len(m_arrow), "2-3 board count")

u_expect = [(e, l) for _, e, l in U_LIST[:2]] + [(FIVECARD, {}), (TREE8, {})] + \
    [(e, l) for _, e, l in U_LIST[2:]] + [
    (TRI, {}), (TRI, {}),
    (ring("ABCD"), {}), (ring("ABCDE"), {}), (ring("ABCDEF"), {}),
    (ring("ABCDEFG"), {}), (ring("ABCDE"), {}), (ring("ABCDE"), {})]
for i, (b, (e, l)) in enumerate(zip(ub, u_expect)):
    check(same_graph(b, e, l), f"4-5 working board {i + 1} matches transcription")
u_arrow = [ARROW_P9] + [a for _, a in U_P10]
rest = ub[len(u_expect):]
for i, (b, a) in enumerate(zip(rest, u_arrow)):
    check(same_graph(b, None, None, a), f"4-5 arrow board {i + 1} matches transcription")
tail = rest[len(u_arrow):]
check(len(tail) == 2 and tail[0]["edges"] == RING5LEAF and tail[1]["edges"] == RING6LEAVES,
      "4-5 P11 boards are five-ring+leaf AF and six-ring+leaves GA, HD")

# ---------------------------------------------------------------------------
# 2. Allowed-list answers printed in the guide
# ---------------------------------------------------------------------------
print("\n== Allowed lists ==")
guide_list_answers = {
    "K1 P1 path": ["231"], "K1 P1 triangle": ["213"], "K1 P1 star": ["3121"],
    "K1 P1 square": ["1213"], "K1 P2 triangle": [], "K1 P2 square": ["1212", "2121"],
    "K1 P2 path3": [], "K1 P2 path4": ["1231"], "K1 P3 six-ring": ["123123"],
    "K1 P3 AB-CDE": [],
    "M P1 tree": ["43114322"], "M P1 ring+leaves": [],
    "M P2 five-ring 12": [], "M P2 five-ring C13": ["12312", "21321"],
    "M P2 six-ring 12": ["121212", "212121"], "M P2 five-ring leaf 23": [],
    "M P3 six-card top": [], "M P3 six-card bottom": ["241133", "243133"],
    "U P1 six-card top": [], "U P1 six-card bottom": ["241133", "243133"],
    "U P4 five-ring 12": [],
    "U P4 five-ring mixed": ["12123", "12312", "12313", "12323", "13123", "23123"],
    "U P4 ring+leaf": ["123122", "213211"],
    "U P4 six-ring 34": ["343434", "434343"],
}
for name, e, l in K1_LIST + M_LIST + U_LIST:
    sols = list_solutions(e, l)
    check(sorted(sols) == sorted(guide_list_answers[name]),
          f"{name}: solutions {sols} == guide {guide_list_answers[name]}")

print("\n== Invented lists ==")
fails, total = count_failing(SIXCARD, L("A:13"), list("BCDEF"))
check(total == 7776 and len(fails) == 24,
      f"2-3 P4 six-card with A=13: {len(fails)} failing of {total} (guide: 24 of 7,776)")
check(all(f[0] == (2, 4) and sorted(f[1:]) == [(1, 2), (1, 4), (2, 3), (3, 4)]
          for f in fails), "every failing design has B=24 and C-F the four mixed pairs")
fails, total = count_failing(FIVECARD, L("A:13"), list("BCDE"))
check(total == 1296 and not fails,
      f"2-3 P4 five-card with A=13: {len(fails)} failing of {total} (guide: 0 of 1,296)")
fails, total = count_failing(FIVECARD, {}, list("ABCDE"))
check(total == 7776 and not fails,
      f"4-5 P2 five-card: {len(fails)} failing of {total} (guide: 0 of 7,776)")
fails, total = count_failing(SIXCARD, {}, list("ABCDEF"))
check(total == 46656 and len(fails) == 144,
      f"(context) six-card all blank: {len(fails)} failing of {total}")
f, t = tree_never_fails(TREE8)
check(t == 1679616 and f == 0, f"4-5 P3 tree: {f} failing of {t} (guide: 0 of 1,679,616)")
# also brute-force a sample check of the DP on the five-card tree-like? (DP only valid for trees)
f2, t2 = tree_never_fails(E("AB BC AD BE CF"))
check(f2 == 0 and t2 == 46656, "(context) tree AB BC AD BE CF never fails")

# ring rule on rings 3-7 with lists from 1-4
ok = True
for n in range(3, 8):
    letters = "ABCDEFG"[:n]
    edges = ring(letters)
    for combo in itertools.product(two_sets(), repeat=n):
        lists = dict(zip(letters, combo))
        fails_ = not has_solution(edges, lists)
        predicted = (n % 2 == 1) and len(set(combo)) == 1
        if fails_ != predicted:
            ok = False
check(ok, "ring rule: two-number lists from 1-4 fail exactly when odd ring and all lists equal (n=3..7)")

# ---------------------------------------------------------------------------
# 3. Moves
# ---------------------------------------------------------------------------
print("\n== Single moves ==")
move_tasks = [
    # name, edges, start, goal, k, guide fewest (None = unreachable), guide word
    ("K1 P4 upper AB (1,2)", E("AB"), S("12"), S("21"), 2, None, None),
    ("K1 P4 lower AB (1-3)", E("AB"), S("12"), S("21"), 3, 3, "A3 B1 A2"),
    ("K1 P5 path ABC", E("AB BC"), S("121"), S("212"), 3, 4, "B3 A2 C2 B1"),
    ("K1 P6 star", STAR5, S("122222"), S("211111"), 3, 7, "A3 B1 C1 D1 E1 F1 A2"),
    ("K1 P7 square", SQUARE, S("1212"), S("2121"), 3, 6, "A3 C3 B1 D1 A2 C2"),
    ("K1 P8 triangle (1-3)", TRI, S("123"), S("231"), 3, None, None),
    ("K1 P8 triangle (1-4)", TRI, S("123"), S("231"), 4, 4, "A4 C1 B3 A2"),
    ("M P5 AB", E("AB"), S("12"), S("21"), 3, 3, "A3 B1 A2"),
    ("M P5 ABC", E("AB BC"), S("121"), S("212"), 3, 4, "B3 A2 C2 B1"),
    ("M P6 ABCD", E("AB BC CD"), S("1212"), S("2121"), 3, 6, "A3 C3 B1 A2 D1 C2"),
    ("M P6 star", STAR5, S("122222"), S("211111"), 3, 7, "A3 B1 C1 D1 E1 F1 A2"),
    ("M P7 triangle (1-3)", TRI, S("123"), S("231"), 3, None, None),
    ("M P7 triangle (1-4)", TRI, S("123"), S("231"), 4, 4, "A4 C1 B3 A2"),
    ("U P5 triangle (1-3)", TRI, S("123"), S("231"), 3, None, None),
    ("U P5 triangle (1-4)", TRI, S("123"), S("231"), 4, 4, "A4 C1 B3 A2"),
    ("U P7 Goal 1", ring("ABCDE"), S("12312"), S("23123"), 3, 5, "E3 D2 C1 B3 A2"),
    ("U P7 Goal 2", ring("ABCDE"), S("12312"), S("13213"), 3, None, None),
    ("U P8 with 4", ring("ABCDE"), S("12312"), S("13213"), 4, 4, "B4 C2 B3 E3"),
]
for name, e, st, gl, k, fewest, word in move_tasks:
    path = bfs(e, st, gl, k)
    got = None if path is None else len(path)
    check(got == fewest, f"{name}: fewest {got} (guide {fewest}); one BFS route {path}")
    if word:
        end = replay(e, st, word, k)
        check(end == gl and len(word.split()) == fewest,
              f"{name}: guide word '{word}' replays legally to Goal")
# start positions with no legal move where the guide says stuck
for name, e, st, k in [("K1 P4 upper", E("AB"), S("12"), 2),
                       ("triangle 1-3", TRI, S("123"), 3)]:
    vs = vertices(e)
    check(not list(moves_from(tuple(st[v] for v in vs), vs, e, k)), f"{name}: Start has no legal move")

print("\n== Stuck rings and families ==")
for n in range(3, 9):
    letters = "ABCDEFGH"[:n]
    st = stuck_states(ring(letters), 3)
    expect = 6 if n % 3 == 0 else 0
    check(len(st) == expect, f"ring {n}, counters 1-3: {len(st)} stuck legal placements (expect {expect})")
    if n == 6:
        strs = sorted("".join(map(str, s)) for s in st)
        check(strs == ["123123", "132132", "213213", "231231", "312312", "321321"],
              f"six-ring stuck list {strs} matches guide")
comps = components(ring("ABCDE"), 3)
check(sorted(len(c) for c in comps) == [15, 15], f"five-ring 1-3: families {sorted(len(c) for c in comps)}")


def ups(s):
    n = len(s)
    return sum(1 for i in range(n) if (s[(i + 1) % n] - s[i]) % 3 == 1)


check(all(len({ups(s) for s in c}) == 1 for c in comps) and
      sorted(ups(next(iter(c))) for c in comps) == [1, 4],
      "five-ring families have constant up-counts 1 and 4")
vs5 = list("ABCDE")
check(all(list(moves_from(s, vs5, ring("ABCDE"), 3)) for c in comps for s in c),
      "every legal five-ring placement with 1-3 has a legal move")
check(ups((1, 2, 3, 1, 2)) == 4 and ups((2, 3, 1, 2, 3)) == 4 and ups((1, 3, 2, 1, 3)) == 1,
      "guide's up-count table: Start 4, Goal 1 4, Goal 2 1")
ok4 = all(len(components(ring("ABCDEFGH"[:n]), 4)) == 1 for n in range(3, 8))
check(ok4, "rings 3-7 with counters 1-4: one connected family")
# up-count invariant also for the guide's local example 2 1 2 -> 2 3 2
check(((1 - 2) % 3, (2 - 1) % 3) == (2, 1) and ((3 - 2) % 3, (2 - 3) % 3) == (1, 2),
      "local example 212 -> 232: DU becomes UD")

# Problem 8 2-3 / Problem 6 4-5: also check that an illegal all-1 placement is excluded by wording
# (no computation needed)

# ---------------------------------------------------------------------------
# 4. Arrows
# ---------------------------------------------------------------------------
print("\n== Arrows ==")
check(longest_path_cards(ARROW_P9) == 4 and min_headers(ARROW_P9) == 4, "P9 instance needs 4 headers")
check(schedule_ok(ARROW_P9, {1: "AEFG", 2: "BH", 3: "C", 4: "D"}, 4), "P9 guide schedule legal")
check(earliest(ARROW_P9) == {"A": 1, "E": 1, "F": 1, "G": 1, "B": 2, "H": 2, "C": 3, "D": 4},
      "P9 guide schedule equals earliest placement")
expect = {"M P10 UL": None, "M P10 UR": 5, "M P10 LL": 4, "M P10 LR": 5,
          "U P10 top": 4, "U P10 bottom": 5}
for name, arr in M_P10 + U_P10:
    lp = longest_path_cards(arr)
    mh = min_headers(arr)
    check(lp == expect[name] and mh == expect[name],
          f"{name}: longest path {lp}, fewest headers {mh} (guide {expect[name]})")
check(schedule_ok(M_P10[2][1], {1: "ABC", 2: "DE", 3: "F", 4: "G"}, 4), "2-3 P10 LL guide schedule")
check(earliest(M_P10[3][1]) == {"A": 1, "B": 1, "C": 1, "E": 2, "D": 3, "F": 4, "G": 5},
      "2-3 P10 LR guide earliest placement")
check(schedule_ok(U_P10[0][1], {1: "BGH", 2: "AD", 3: "CE", 4: "F"}, 4), "4-5 P10 top guide schedule")
check(earliest(U_P10[1][1]) == {"B": 1, "G": 1, "H": 1, "A": 2, "D": 2, "E": 3, "C": 4, "F": 5},
      "4-5 P10 bottom guide earliest placement")

for name, edges, k_expected, n_orient in [("five-ring+leaf", RING5LEAF, 3, 64),
                                           ("six-ring+leaves", RING6LEAVES, 2, 256)]:
    best, cnt, nopt, dist = None, 0, 0, {}
    for o in orientations(edges):
        cnt += 1
        lp = longest_path_cards(o)
        dist[lp] = dist.get(lp, 0) + 1
        if lp is not None and (best is None or lp < best):
            best, nopt = lp, 0
        if lp == best:
            nopt += 1
    check(cnt == n_orient and best == k_expected,
          f"P11 {name}: {cnt} orientations, min longest path {best} (guide {k_expected}); dist {dist}")
    if name.startswith("six"):
        check(nopt == 2, f"six-ring+leaves: {nopt} optimal orientations (guide: the two bipartition ones)")
ori = A("AB CB CD DE AE AF")
check(longest_path_cards(ori) == 3, "4-5 P11 guide orientation has longest path 3 cards")
check(schedule_ok(ori, {1: "AC", 2: "BDF", 3: "E"}, 4), "4-5 P11 guide schedule follows its arrows")
check(legal(tuple(S("12121221")[v] for v in "ABCDEFGH"), list("ABCDEFGH"), RING6LEAVES),
      "six-ring+leaves A,C,E,H in 1 / B,D,F,G in 2 is legal")

# ---------------------------------------------------------------------------
# 5. Launch demos
# ---------------------------------------------------------------------------
print("\n== Launch / demos ==")
check("32" in list_solutions(E("AB"), L("A:13 B:23")),
      "A-B launch demo: A3 B2 is a legal completion")
print("   A-B demo completions:", list_solutions(E("AB"), L("A:13 B:23")))
paw = E("AB BC CA CD")
check(replay(paw, S("1232"), "D1", 3) == S("1231"), "paw demo D1 is legal")

print("\nFAILURES:", len(FAIL))
for f in FAIL:
    print("  -", f)
