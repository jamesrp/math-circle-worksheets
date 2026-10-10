#!/usr/bin/env python3
"""Independent math check for Week 41 (torus portals and lifts) and its bonus.

Written from scratch for the review. It does not import or run any of the
packet's own checkers (src/check_math.py, verify_math.py, facilitator-src/
verify_answers.py, bonus student/verify.py).

Model.  The portal map is the 3x3 torus.  A lifted position is a point of Z^2
with the original H at (0,0); its cell label is LABEL[(x+1)%3, (y+1)%3] and its
copy is (floor((x+1)/3), floor((y+1)/3)).  R,L,U,D are (1,0),(-1,0),(0,1),(0,-1).

Run from anywhere:  python3 check_math.py   (output saved to out_check_math.txt)
"""
import re
import subprocess
import sys
from collections import Counter, defaultdict, deque
from itertools import product
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent


def find_repo():
    cand = HERE.parents[4] if len(HERE.parents) > 4 else None
    if cand and (cand / "lowell-math-circle-year-2").is_dir():
        return cand
    for p in HERE.parents:
        if (p / "lowell-math-circle-year-2").is_dir():
            return p
    sys.exit("repository not found")


REPO = find_repo()
Y2 = REPO / "lowell-math-circle-year-2"
OUT = []
FAIL = []


def log(s=""):
    OUT.append(s)
    print(s)


def check(cond, msg):
    log(("PASS " if cond else "FAIL ") + msg)
    if not cond:
        FAIL.append(msg)


# ---------------------------------------------------------------- model
STEP = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
INV = {"R": "L", "L": "R", "U": "D", "D": "U"}
# (col, row) with row 0 = bottom: F G I / D H E / A B C
GRID = {(0, 2): "A", (1, 2): "B", (2, 2): "C",
        (0, 1): "D", (1, 1): "H", (2, 1): "E",
        (0, 0): "F", (1, 0): "G", (2, 0): "I"}
CELL = {v: k for k, v in GRID.items()}


def label(p):
    return GRID[((p[0] + 1) % 3, (p[1] + 1) % 3)]


def copy_of(p):
    return ((p[0] + 1) // 3, (p[1] + 1) // 3)


def lift(word, start=(0, 0)):
    pts = [start]
    x, y = start
    for c in word:
        dx, dy = STEP[c]
        x, y = x + dx, y + dy
        pts.append((x, y))
    return pts


def disp(word):
    return lift(word)[-1]


def end_label(word, start="H"):
    s = CELL[start]
    return label(lift(word, (s[0] - 1, s[1] - 1))[-1])


def is_loop(word):
    x, y = disp(word)
    return x % 3 == 0 and y % 3 == 0


def words(n):
    return ("".join(w) for w in product("RLUD", repeat=n))


def norm(s):
    return re.sub(r"\s+", " ", s.replace("−", "-").replace("–", "-")).strip()


def pdftext(path):
    return norm(subprocess.run(["pdftotext", "-layout", str(path), "-"],
                               capture_output=True, text=True, check=True).stdout)


GUIDE = pdftext(Y2 / "week-41/week-41-facilitator.pdf")
BGUIDE = pdftext(Y2 / "week-41/week-41-bonus-facilitator.pdf")


def quoted(text, s, where):
    check(norm(s) in text, f"{where} prints: \"{s}\"")


# ---------------------------------------------------------------- printed words from the TeX sources
ARW = {r"\rightarrow": "R", r"\leftarrow": "L", r"\uparrow": "U", r"\downarrow": "D"}


def tex_words(band):
    tex = (Y2 / f"source/week-41/editable/src/{band}.tex").read_text()
    pages = tex.split(r"\newpage")
    res = []
    for i, pg in enumerate(pages, 1):
        for m in re.finditer(r"\{\$((?:\\(?:right|left|up|down)arrow(?:\\;)?)+)\$\}", pg):
            res.append((i, "".join(ARW[a] for a in re.findall(r"\\(?:right|left|up|down)arrow", m.group(1)))))
    return res


log("Week 41 independent math check")
log(f"repository: {REPO.name}")
log("")

# ================================================================ shared page 1
log("== Page-1 worked example (all bands): two steps right from H")
pts = lift("RR")
check([label(p) for p in pts] == ["H", "E", "D"], "RR from H visits H, E, D on the portal map")
check(copy_of(pts[1]) == (0, 0) and copy_of(pts[2]) == (1, 0), "E is in the original copy, D in the next copy right")

for band in ["k-1", "grades-2-3", "grades-4-5"]:
    tw = tex_words(band)
    log(f"   {band}: printed words (page, word) = {tw}")

log("")
log("== Problem 1 (all bands): RRD, UU, LD, UURR from H")
P1 = ["RRD", "UU", "LD", "UURR"]
for band in ["k-1", "grades-2-3", "grades-4-5"]:
    check([w for p, w in tex_words(band) if p == 1] == P1, f"{band} p.1 prints exactly the words {P1}")
ends = [end_label(w) for w in P1]
log(f"   endpoints: {dict(zip(P1, ends))}")
check(ends == ["F", "G", "F", "F"], "endpoints are F, G, F, F (guide pp. 3-5)")
replays = {"RRD": "H→E→D→F", "UU": "H→B→G", "LD": "H→D→F", "UURR": "H→B→G→I→F"}
for w, r in replays.items():
    got = "→".join(label(p) for p in lift(w))
    check(got == r, f"guide p.3 replay of {w}: {r} (computed {got})")
quoted(GUIDE, "The four printed routes end, from top to bottom, at F, G, F, F", "guide p.3")

# ================================================================ K-1
log("")
log("== K-1 Problem 2: every square reachable in exactly two steps from H")
reach2 = {end_label(w) for w in words(2)}
reach2_nb = {end_label(w) for w in words(2) if w[1] != INV[w[0]]}
log(f"   with any steps: {sorted(reach2)} ({len(reach2)})")
log(f"   without an immediate reversal: {sorted(reach2_nb)} ({len(reach2_nb)})")
check(len(reach2) == 9, "all nine cells are reachable in exactly two steps (guide p.3)")
check(reach2_nb == set(GRID.values()) - {"H"}, "without reversals exactly the eight cells other than H")
wit = {"A": "LU", "B": "DD", "C": "RU", "D": "RR", "H": "RL", "E": "LL", "F": "LD", "G": "UU", "I": "RD"}
for c, w in wit.items():
    check(end_label(w) == c and len(w) == 2, f"guide witness {c}: {w}")
nowrap = {end_label(w) for w in words(2) if all(-1 <= p[0] <= 1 and -1 <= p[1] <= 1 for p in lift(w))}
log(f"   cells reachable in two steps without crossing an edge: {sorted(nowrap)}")
check(lift("DD")[1:] and [label(p) for p in lift("DD")] == ["H", "G", "B"] and
      [label(p) for p in lift("UU")] == ["H", "B", "G"], "guide: DD goes H→G→B, UU goes H→B→G")

log("")
log("== K-1 Problem 3: trips from H back to H with 2, 3, 4, 5 steps")
for n in [2, 3, 4, 5]:
    loops = [w for w in words(n) if is_loop(w)]
    log(f"   {n} steps: {len(loops)} closed words, e.g. {loops[:6]}")
    check(len(loops) >= 2, f"more than one trip exists with {n} steps")
check(sorted(w for w in words(3) if is_loop(w)) == ["DDD", "LLL", "RRR", "UUU"], "3-step trips are exactly RRR, LLL, UUU, DDD")
for w in ["RL", "UD", "RRR", "UUU", "RRLL", "RULD", "RRRUD", "UUURL"]:
    check(is_loop(w), f"guide p.3 example {w} returns to H")

log("")
log("== K-1 Problem 4: pawns on H and E, same arrow steps, can they trade places?")
start = (CELL["H"], CELL["E"])
target = (CELL["E"], CELL["H"])
seen = {start}
dq = deque([start])
while dq:
    a, b = dq.popleft()
    for dx, dy in STEP.values():
        na = ((a[0] + dx) % 3, (a[1] + dy) % 3)
        nb = ((b[0] + dx) % 3, (b[1] + dy) % 3)
        if (na, nb) not in seen:
            seen.add((na, nb))
            dq.append((na, nb))
log(f"   reachable pawn-pair states: {len(seen)} (of 81)")
check(target not in seen, "no common word swaps the pawns: answer No (guide p.3)")
check(all(((b[0] - a[0]) % 3, (b[1] - a[1]) % 3) == (1, 0) for a, b in seen),
      "the offset from the H-pawn to the E-pawn stays one cell right (mod 3)")
check((1 - (-1)) % 3 != 0, "guide: +1 and -1 differ mod 3")

# ================================================================ Grades 2-3
log("")
log("== Grades 2-3 Problem 2: closed trips of exactly 3 and 6 steps")
l3 = sorted(w for w in words(3) if is_loop(w))
check(l3 == ["DDD", "LLL", "RRR", "UUU"], "3 steps: complete list RRR, LLL, UUU, DDD (guide p.4)")
l6 = [w for w in words(6) if is_loop(w)]
byd = Counter(disp(w) for w in l6)
log(f"   6-step closed words: {len(l6)}; by displacement {dict(sorted(byd.items()))}")
check(len(l6) == 484, "484 six-step words return to H (guide p.4)")
check(byd[(0, 0)] == 400, "400 balanced words")
check(all(byd[d] == 1 for d in [(6, 0), (-6, 0), (0, 6), (0, -6)]), "one straight word for each of (±6,0),(0,±6)")
check(all(byd[(a, b)] == 20 for a in (3, -3) for b in (3, -3)), "20 words for each of the four (±3,±3)")
check(set(byd) == {(0, 0), (6, 0), (-6, 0), (0, 6), (0, -6), (3, 3), (3, -3), (-3, 3), (-3, -3)},
      "no other six-step return displacement")
# spectral cross-check: closed walks on C3 x C3 = (1/9) sum (λi+λj)^6, λ in {2,-1,-1}
ev = [2, -1, -1]
check(sum((a + b) ** 6 for a in ev for b in ev) // 9 == 484, "spectral count of closed 6-walks is 484")
for w in ["RRRRRR", "LLLLLL", "UUUUUU", "DDDDDD", "RRRUUU", "RURURU", "RRRDDD", "LLLUUU", "LLLDDD", "RLRLRL"]:
    check(is_loop(w), f"guide p.4 six-step example {w} returns to H")
quoted(GUIDE, "There are 400 balanced strings, four straight six-step strings, and 20 for each of the four diagonal sign choices: 484 total", "guide p.4")

log("")
log("== Grades 2-3 Problem 3: finishing copies (and whether the route fits the printed 3x3 array of copies)")
P3_23 = ["RRR", "UUU", "RRRUUU", "RRLL"]
check([w for p, w in tex_words("grades-2-3") if p == 3] == P3_23, f"2-3 p.3 prints {P3_23}")
want = {"RRR": (1, 0), "UUU": (0, 1), "RRRUUU": (1, 1), "RRLL": (0, 0)}
for w in P3_23:
    pts = lift(w)
    inside = all(copy_of(p)[0] in (-1, 0, 1) and copy_of(p)[1] in (-1, 0, 1) for p in pts)
    check(copy_of(pts[-1]) == want[w] and label(pts[-1]) == "H" and inside,
          f"{w}: finishes at H in copy {copy_of(pts[-1])} (guide {want[w]}); stays on printed array: {inside}")
check(copy_of(lift("RRLL")[2]) == (1, 0), "RRLL enters the right copy before returning (guide p.4)")

log("")
log("== Grades 2-3 Problem 4: RRRUUU vs RURURU")
check([w for p, w in tex_words("grades-2-3") if p == 4] == ["RRRUUU", "RURURU"], "2-3 p.4 prints RRRUUU and RURURU")
a, b = lift("RRRUUU"), lift("RURURU")
check(label(a[-1]) == label(b[-1]) == "H" and copy_of(a[-1]) == copy_of(b[-1]) == (1, 1),
      "both finish at H and in copy (1,1): yes and yes (guide p.4)")
check(all(copy_of(p)[0] in (-1, 0, 1) and copy_of(p)[1] in (-1, 0, 1) for p in a + b), "both stay on the printed array")

log("")
log("== Grades 2-3 Problem 5: visit another copy and finish at the original H")
for w, need in [("RRRLLL", {(1, 0)}), ("UUUDDDRRRLLL", {(0, 1), (1, 0)}), ("RRRUUULLLDDD", {(0, 1), (1, 0)})]:
    pts = lift(w)
    visited = {copy_of(p) for p in pts}
    check(pts[-1] == (0, 0) and need <= visited, f"guide p.4 {w}: ends at original H, visits {sorted(visited - {(0, 0)})}")
seq = []
for p in lift("RRRUUULLLDDD"):
    c = copy_of(p)
    if not seq or seq[-1] != c:
        seq.append(c)
log(f"   RRRUUULLLDDD copy sequence: {seq}")
check(seq == [(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)], "it passes right, upper-right, upper, then original (guide p.4)")
shortest = min((w for n in range(1, 9) for w in words(n)
                if disp(w) == (0, 0) and {(0, 1), (1, 0)} <= {copy_of(p) for p in lift(w)}), key=len)
log(f"   shortest closed trip visiting a copy above and a copy right: length {len(shortest)}, e.g. {shortest}")

# ================================================================ Grades 4-5
log("")
log("== Grades 4-5 Problem 2: four trips finishing in different copies")
for w, c in [("RRR", (1, 0)), ("LLL", (-1, 0)), ("UUU", (0, 1)), ("DDD", (0, -1))]:
    check(label(lift(w)[-1]) == "H" and copy_of(lift(w)[-1]) == c, f"guide p.5 {w} -> {c}")

log("")
log("== Grades 4-5 Problem 3: finishing copies")
P3_45 = ["RRRUUU", "UUURRR", "RRLL", "RRRUUULLLDDD"]
check([w for p, w in tex_words("grades-4-5") if p == 3] == P3_45, f"4-5 p.3 prints {P3_45}")
for w, c in zip(P3_45, [(1, 1), (1, 1), (0, 0), (0, 0)]):
    pts = lift(w)
    inside = all(max(abs(q) for q in copy_of(p)) <= 1 for p in pts)
    check(copy_of(pts[-1]) == c and label(pts[-1]) == "H" and inside, f"{w} -> {copy_of(pts[-1])} (guide {c}); on printed array: {inside}")
for coords in [(-1, 1), (0, 1), (1, 1), (-1, 0), (0, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]:
    p = (3 * coords[0], 3 * coords[1])
    check(label(p) == "H" and copy_of(p) == coords, f"copy {coords}: its H is at lifted (3m,3n) = {p}")


# ---- moves on words (4-5 page 4 rules)
def neighbours(w):
    """All words one allowed move away: insert/erase an adjacent inverse pair, or swap an
    adjacent perpendicular pair (two sides of a unit square -> the other two sides)."""
    out = set()
    for i in range(len(w) - 1):
        a, b = w[i], w[i + 1]
        if b == INV[a]:
            out.add(w[:i] + w[i + 2:])
        elif (a in "RL") != (b in "RL"):
            out.add(w[:i] + b + a + w[i + 2:])
    for i in range(len(w) + 1):
        for a in "RLUD":
            out.add(w[:i] + a + INV[a] + w[i:])
    return out


def one_move(u, v):
    return v in neighbours(u)


def slide_ok(u, v):
    """v from u by exactly one square slide; check geometrically on the lift that the two
    replaced steps and the two new steps are the four sides of one unit square."""
    if len(u) != len(v):
        return False
    diff = [i for i in range(len(u)) if u[i] != v[i]]
    if len(diff) != 2 or diff[1] != diff[0] + 1:
        return False
    i = diff[0]
    pu, pv = lift(u), lift(v)
    if pu[i] != pv[i] or pu[i + 2] != pv[i + 2]:
        return False
    corners = {pu[i], pu[i + 1], pu[i + 2], pv[i + 1]}
    xs = {c[0] for c in corners}
    ys = {c[1] for c in corners}
    return len(corners) == 4 and len(xs) == 2 and len(ys) == 2 and max(xs) - min(xs) == 1 and max(ys) - min(ys) == 1


log("")
log("== Grades 4-5 Problem 4: which trip shrinks to staying at H")
check([w for p, w in tex_words("grades-4-5") if p == 4] == ["RRRUUULLLDDD", "RRR", "RRRUUU", "UUURRR"],
      "4-5 p.4 prints RRRUUULLLDDD, RRR (P4) and RRRUUU, UUURRR (P5)")
w = "RRRUUULLLDDD"
chain = [w]
# guide: commute each L leftward across each U (nine slides) -> RRRLLLUUUDDD
cur = list(w)
for k in range(3):          # move the k-th L (positions 6+k) leftward past three U's
    pos = 6 + k
    for _ in range(3):
        cur[pos - 1], cur[pos] = cur[pos], cur[pos - 1]
        pos -= 1
        chain.append("".join(cur))
check(len(chain) - 1 == 9 and chain[-1] == "RRRLLLUUUDDD", "nine slides give RRRLLLUUUDDD (guide p.5)")
check(all(slide_ok(chain[i], chain[i + 1]) for i in range(9)), "each of the nine is a legal square slide")
cur = chain[-1]
while cur:
    for i in range(len(cur) - 1):
        if cur[i + 1] == INV[cur[i]]:
            cur = cur[:i] + cur[i + 2:]
            chain.append(cur)
            break
    else:
        break
check(chain[-1] == "" and len(chain) - 1 == 15, "then six cancellations reach the empty trip (15 moves in all)")
check(all(one_move(chain[i], chain[i + 1]) for i in range(len(chain) - 1)), "every step of the reduction is one allowed move")
allpts = [p for u in chain for p in lift(u)]
check(all(max(abs(q) for q in copy_of(p)) <= 1 for p in allpts), "the whole reduction stays on the printed page-3 array")
check(copy_of(lift("RRR")[-1]) == (1, 0), "RRR finishes in copy (1,0), so it cannot shrink")

log("")
log("== Endpoint invariance of the allowed moves (all words up to length 7)")
bad = 0
for n in range(0, 8):
    for u in words(n):
        for v in neighbours(u):
            if disp(v) != disp(u):
                bad += 1
check(bad == 0, "every allowed move preserves the lifted endpoint")

log("")
log("== Grades 4-5 Problem 5: RRRUUU -> UUURRR")
seq5 = "RRRUUU RRURUU RURRUU URRRUU URRURU URURRU UURRRU UURRUR UURURR UUURRR".split()
check(len(seq5) == 10 and seq5[0] == "RRRUUU" and seq5[-1] == "UUURRR", "guide sequence has nine slides from RRRUUU to UUURRR")
check(all(slide_ok(seq5[i], seq5[i + 1]) for i in range(9)), "each guide step is one legal square slide")
# fewest moves: BFS over words of length <= 8
dist = {"RRRUUU": 0}
dq = deque(["RRRUUU"])
while dq:
    u = dq.popleft()
    if u == "UUURRR":
        break
    for v in neighbours(u):
        if len(v) <= 8 and v not in dist:
            dist[v] = dist[u] + 1
            dq.append(v)
log(f"   fewest allowed moves RRRUUU -> UUURRR (words up to length 8): {dist.get('UUURRR')}")
inv = sum(1 for i in range(6) for j in range(i + 1, 6) if "RRRUUU"[i] == "R" and "RRRUUU"[j] == "U")
log(f"   (R,U) inversions to undo: {inv}")

log("")
log("== Grades 4-5 Problem 6 / guide theorem: moves connect two loops iff same finishing copy")
# union-find over all loop words of length <= 8 using moves that stay within length <= 8
L = 8
loopwords = [u for n in range(0, L + 1) for u in words(n) if is_loop(u)]
idx = {u: i for i, u in enumerate(loopwords)}
par = list(range(len(loopwords)))


def find(i):
    while par[i] != i:
        par[i] = par[par[i]]
        i = par[i]
    return i


for u in loopwords:
    for v in neighbours(u):
        if v in idx:
            a, b = find(idx[u]), find(idx[v])
            if a != b:
                par[a] = b
classes = defaultdict(set)
for u in loopwords:
    classes[find(idx[u])].add(disp(u))
check(all(len(s) == 1 for s in classes.values()), "no move class mixes finishing copies")
check(len(classes) == len({disp(u) for u in loopwords}),
      f"loops of length <= {L} with the same finishing copy are all connected ({len(loopwords)} words, {len(classes)} classes)")
# without square faces, RULD is free-reduced and nonempty
def free_reduce(u):
    st = []
    for c in u:
        if st and st[-1] == INV[c]:
            st.pop()
        else:
            st.append(c)
    return "".join(st)
check(free_reduce("RULD") == "RULD" and disp("RULD") == (0, 0),
      "guide p.5: without faces the commutator RULD does not cancel, though its finishing copy is (0,0)")

log("")
log("== Guide overview: return to H iff both displacements are multiples of 3; copy = (x/3, y/3)")
ok = True
for n in range(0, 9):
    for u in words(n):
        x, y = disp(u)
        back = label((x, y)) == "H"
        if back != (x % 3 == 0 and y % 3 == 0):
            ok = False
        if back and copy_of((x, y)) != (x // 3, y // 3):
            ok = False
check(ok, "checked on all words up to length 8")

# ================================================================ Bonus
log("")
log("== Bonus Problem 1: round-end orbits of a repeated word")


def orbit(word):
    p = (0, 0)
    seen = [label(p)]
    d = disp(word)
    for _ in range(9):
        p = (p[0] + d[0], p[1] + d[1])
        if label(p) == "H":
            break
        seen.append(label(p))
    return seen


for w, exp in [("RL", ["H"]), ("R", ["H", "E", "D"]), ("RU", ["H", "C", "F"]), ("RRR", ["H"]),
               ("RULD", ["H"]), ("RRU", ["H", "A", "I"])]:
    check(orbit(w) == exp, f"{w}: round ends {orbit(w)} (guide {exp})")
mx = max(len(orbit(u)) for n in range(1, 8) for u in words(n))
check(mx == 3, f"no word up to length 7 reaches more than 3 round-end cells (max {mx}); none reaches all nine")
# general claim: period lcm(a/gcd(a,x), b/gcd(b,y)) on an a-by-b portal board


def lcm(a, b):
    return a * b // gcd(a, b)


ok = True
for a in range(1, 8):
    for b in range(1, 8):
        for x in range(-8, 9):
            for y in range(-8, 9):
                p, k = (0, 0), 0
                while True:
                    p = ((p[0] + x) % a, (p[1] + y) % b)
                    k += 1
                    if p == (0, 0):
                        break
                if k != lcm(a // gcd(a, x), b // gcd(b, y)):
                    ok = False
check(ok, "bonus guide period formula lcm(a/gcd(a,x), b/gcd(b,y)) holds for a,b <= 7, |x|,|y| <= 8")

log("")
log("== Bonus Problem 2: nine-step tours of the 3x3 portal board")
tours = []


def dfs(word, pos, visited):
    if len(word) == 9:
        if pos == (0, 0) or label(pos) == "H":
            tours.append(word)
        return
    for c, (dx, dy) in STEP.items():
        q = (pos[0] + dx, pos[1] + dy)
        lq = label(q)
        if len(word) == 8:
            if lq == "H":
                dfs(word + c, q, visited)
        elif lq not in visited:
            dfs(word + c, q, visited | {lq})


dfs("", (0, 0), {"H"})
tc = Counter(copy_of(lift(t)[-1]) for t in tours)
log(f"   tours: {len(tours)}; finishing copies: {dict(sorted(tc.items()))}")
check(len(tours) == 96, "96 rooted oriented tours (bonus guide p.1)")
check(len(tc) == 12, "12 finishing copies")
check((0, 0) not in tc, "no tour finishes in the original copy")
table = {(-2, -1): ("LLDLLDLLD", 3), (-2, 1): ("LLULLULLU", 3), (-1, -2): ("LDDLDDLDD", 3),
         (-1, 0): ("RULLDDLLU", 18), (-1, 2): ("LUULUULUU", 3), (0, -1): ("RRDDLULDD", 18),
         (0, 1): ("RRUULDLUU", 18), (1, -2): ("RDDRDDRDD", 3), (1, 0): ("RRULURRDD", 18),
         (1, 2): ("RUURUURUU", 3), (2, -1): ("RRDRRDRRD", 3), (2, 1): ("RRURRURRU", 3)}
fit = Counter(copy_of(lift(t)[-1]) for t in tours if all(max(abs(q) for q in copy_of(p)) <= 1 for p in lift(t)))
log(f"   tours that stay on the printed 3x3 array of copies, by finishing copy: {dict(sorted(fit.items()))}")
check(set(table) == set(tc), "the guide's 12 copies are exactly the possible ones")
for c, (w, n) in sorted(table.items()):
    check(w in tours and copy_of(lift(w)[-1]) == c and tc[c] == n, f"guide row {c}: {w} is a tour ending there; count {tc[c]} (guide {n})")
SYM = [lambda x, y: (x, y), lambda x, y: (-x, y), lambda x, y: (x, -y), lambda x, y: (-x, -y),
       lambda x, y: (y, x), lambda x, y: (-y, x), lambda x, y: (y, -x), lambda x, y: (-y, -x)]
tourset = set(tours)
LET = {(1, 0): "R", (-1, 0): "L", (0, 1): "U", (0, -1): "D"}
check(all("".join(LET[f(*STEP[c])] for c in t) in tourset for f in SYM for t in tours),
      "the 8 symmetries of the board about H map tours to tours")
orbits = {frozenset(f(*c) for f in SYM) for c in tc}
log(f"   symmetry orbits of finishing copies: {[sorted(o) for o in orbits]}")
check(len(orbits) == 2, "two examples, (1,0) and (2,1), generate all 12 copies under the symmetries (bonus guide extension)")
check(all((x + y) % 2 == 1 for x, y in tc),
      "every finishing copy has m+n odd (nine is odd)")
# undirected Hamiltonian cycles of K3 x K3
check(len({frozenset(frozenset(e) for e in zip([label(p) for p in lift(t)][:-1], [label(p) for p in lift(t)][1:])) for t in tours}) * 2 == 96,
      "96 = 2 orientations x 48 undirected Hamiltonian cycles")

log("")
log("== Bonus Problem 3: shortest routes with B and E closed in every copy")


def blocked(p):
    return label(p) in ("B", "E")


def bfs_from(src, bound=12):
    d = {src: 0}
    dq = deque([src])
    while dq:
        u = dq.popleft()
        if d[u] >= bound:
            continue
        for dx, dy in STEP.values():
            v = (u[0] + dx, u[1] + dy)
            if not blocked(v) and v not in d:
                d[v] = d[u] + 1
                dq.append(v)
    return d


d = bfs_from((0, 0))
for name, tgt, n, wit in [("right copy", (3, 0), 5, "DRRRU"), ("up copy", (0, 3), 5, "LUURU"),
                          ("right + up", (3, 3), 8, "LUURRRRU")]:
    pts = lift(wit)
    legal = all(not blocked(p) for p in pts[1:])
    check(d[tgt] == n, f"{name} {tgt}: BFS distance {d[tgt]} (guide {n})")
    check(legal and pts[-1] == tgt and len(wit) == n, f"guide witness {wit} is legal and reaches {tgt}")
    # all shortest routes, and whether one fits the printed 7x7 patch (-2..4)
    cnt = 0
    inpatch = 0
    for u in words(n):
        q = lift(u)
        if q[-1] == tgt and all(not blocked(p) for p in q[1:]):
            cnt += 1
            if all(-2 <= p[0] <= 4 and -2 <= p[1] <= 4 for p in q):
                inpatch += 1
    log(f"   {name}: {cnt} shortest routes, {inpatch} inside the printed patch")
check(blocked((1, 0)) and blocked((0, 1)) and not blocked((-1, 0)) and not blocked((0, -1)),
      "H's right and up neighbours are closed; left and down are open")

log("")
log("== Bonus pages 1-2: which printed words and tours cross the top/bottom edge (the board marks only left/right seams)")


def vertical_crossings(word, rounds=1):
    pts = lift(word * rounds)
    return sum(1 for a, b in zip(pts, pts[1:]) if copy_of(a)[1] != copy_of(b)[1])


for w in ["R", "RU", "RRR", "RULD", "RRU"]:
    log(f"   P1 word {w}: top/bottom crossings in three rounds = {vertical_crossings(w, 3)}")
check(vertical_crossings("RU", 3) > 0 and vertical_crossings("RRU", 3) > 0,
      "P1: RU and RRU cannot be replayed for three rounds without crossing the top/bottom edge")
vt = sum(1 for t in tours if vertical_crossings(t) > 0)
log(f"   P2: {vt} of {len(tours)} tours cross the top/bottom edge; "
    f"{sum(1 for t in tours if vertical_crossings(t) == 0)} use only left/right seams")
check(all(copy_of(lift(t)[-1])[1] == 0 or vertical_crossings(t) > 0 for t in tours),
      "P2: every tour finishing in a copy with n != 0 crosses the top/bottom edge")
cyl = Counter(copy_of(lift(t)[-1]) for t in tours if vertical_crossings(t) == 0)
log(f"   cylinder reading (no top/bottom wrap): tours by finishing copy {dict(sorted(cyl.items()))}")
check(set(cyl) == {(-1, 0), (1, 0)}, "read as a cylinder, the board allows only 12 tours, finishing in just two copies")
log(f"   RU replayed: round ends {[label(p) for p in lift('RU' * 3)[::2]]}; second round C -R-> A -U-> {label(lift('RU' * 2)[-1])} crosses the top edge")
log(f"   RRU replayed: round ends {[label(p) for p in lift('RRU' * 3)[::3]]}; second round A -R-> B -R-> C -U-> {label(lift('RRU' * 2)[-1])} crosses the top edge")
log("")
log(f"TOTAL: {len(FAIL)} failures")
(HERE / "out_check_math.txt").write_text("\n".join(OUT) + "\n")
