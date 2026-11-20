"""Independent reviewer check for the Week 91 K-1 guide draft (F91-K-FAC-v1).

Reads the final student pages and the week's materials, simulates the
machines from every start, and prints the answers the guide should give.
Run: python3 -I check91.py  (from anywhere; paths are relative to this file).
"""
import itertools, math, os, re, sys, warnings
warnings.filterwarnings("ignore")
import fitz

HERE = os.path.dirname(os.path.abspath(__file__))
RUN = os.path.dirname(HERE)
REPO = os.path.abspath(os.path.join(RUN, "..", "..", ".."))
PAGES = os.path.join(REPO, "plans/k1-drafts/week-91/k-1.pdf")
MAT = os.path.join(REPO, "lowell-math-circle-year-2/week-91/week-91-materials.pdf")
BASE = os.path.join(REPO, "lowell-math-circle-year-2/week-91/week-91-facilitator.pdf")
GUIDE = os.path.join(RUN, "draft/k1-guide.pdf")
MM = 25.4 / 72

# ---------------- machines ----------------
def switch(first, n):
    """first in 'XY'; card shows next exit; follow then flip."""
    a, out = first, []
    for _ in range(n):
        out.append(a)
        a = "Y" if a == "X" else "X"
    return "".join(out)

def tree(start, n):
    """start = word over L/R for (top, left lower, right lower)."""
    c = list(start)
    out = []
    for _ in range(n):
        t = c[0]
        c[0] = "R" if t == "L" else "L"
        i = 1 if t == "L" else 2
        lo = c[i]
        c[i] = "R" if lo == "L" else "L"
        out.append({(1, "L"): "A", (1, "R"): "B", (2, "L"): "C", (2, "R"): "D"}[(i, lo)])
    return "".join(out), "".join(c)

STARTS = ["".join(s) for s in itertools.product("LR", repeat=3)]

def piles(word, letters):
    return tuple(word.count(x) for x in letters)

# ---------------- read the student pages ----------------
doc = fitz.open(PAGES)
print("Student pages:", len(doc))

def boxes_and_dots(page, box_w, dot_w):
    boxes, dots = [], []
    for d in page.get_drawings():
        r = d["rect"]
        if abs(r.width - box_w) < 0.6 and abs(r.height - box_w) < 0.6 and d["type"] == "s":
            boxes.append(r)
        if abs(r.width - dot_w) < 0.4 and abs(r.height - dot_w) < 0.4 and d.get("fill") is not None:
            dots.append(r)
    return boxes, dots

def letter_under(page, box, letters):
    best = None
    for w in page.get_text("words"):
        if w[4] in letters:
            cx = (w[0] + w[2]) / 2
            if box.x0 - 2 <= cx <= box.x1 + 2 and 0 <= w[1] - box.y1 < 25:
                best = w[4]
    return best

def pictures(page, box_w, dot_w, letters, ncols):
    """Group exit boxes into pictures by row (box y) and column (page third or half)."""
    boxes, dots = boxes_and_dots(page, box_w, dot_w)
    words = page.get_text("words")
    W = page.rect.width
    groups = {}
    for b in boxes:
        n = sum(1 for d in dots if b.contains(fitz.Point((d.x0 + d.x1) / 2, (d.y0 + d.y1) / 2)))
        col = int(((b.x0 + b.x1) / 2) / (W / ncols))
        groups.setdefault((round(b.y0), col), []).append((b.x0, letter_under(page, b, letters), n, b))
    out = []
    for (y, col), items in sorted(groups.items()):
        items.sort()
        # label: the "N counters" text in this column nearest above-or-below this row
        best, bd = None, 1e9
        for i, w in enumerate(words):
            if w[4] == "counters" and words[i - 1][4].isdigit() and int(((w[0] + w[2]) / 2) / (W / ncols)) in (col,) and i > 0:
                dist = abs(w[1] - y)
                if dist < bd:
                    bd, best = dist, int(words[i - 1][4])
        out.append(((y, col), best, {let: n for _, let, n, _ in items}))
    return out

# Problem 2, page 2
p2 = pictures(doc[1], 53.9, 9.1, {"X", "Y"}, 3)
# Problem 6, page 5
p6 = pictures(doc[4], 35.4, 7.7, {"A", "B", "C", "D"}, 2)

def order_reading(pics):
    return sorted(pics, key=lambda t: (t[0][0], t[0][1]))

print("\nProblem 2 (page 2): pictures in reading order")
p2 = order_reading(p2)
for i, (key, n, pl) in enumerate(p2, 1):
    tot = sum(pl.values())
    ok = [f for f in "XY" if piles(switch(f, tot), "XY") == (pl["X"], pl["Y"])]
    print(f"  picture {i}: label {n} counters, dots X={pl['X']} Y={pl['Y']} (sum {tot}); starts making it: {ok or 'impossible'}")
    assert tot == n

print("\nProblem 6 (page 5): pictures in reading order")
p6 = order_reading(p6)
for i, (key, n, pl) in enumerate(p6, 1):
    tot = sum(pl.values())
    want = tuple(pl[x] for x in "ABCD")
    ok = [s for s in STARTS if piles(tree(s, tot)[0], "ABCD") == want]
    print(f"  picture {i}: label {n}, piles A-D={want} (sum {tot}); starts: {ok if ok else 'impossible'}"
          + (" (all eight)" if len(ok) == 8 else ""))
    assert tot == n

# Grid / tree counts
def count(page, w, h=None, tol=0.6, filled=None):
    h = h or w
    k = 0
    for d in page.get_drawings():
        r = d["rect"]
        if abs(r.width - w) < tol and abs(r.height - h) < tol:
            if filled is None or (d.get("fill") is not None) == filled:
                k += 1
    return k
print("\nRecording space")
print("  P1 page 1 boxes (42.5pt):", count(doc[0], 42.5), "-> rows of 10:", count(doc[0], 42.5) // 10)
print("  P3 page 3 boxes (36.9pt):", count(doc[2], 36.9), "-> rows of 7:", count(doc[2], 36.9) // 7)
print("  P5 page 4 tree circles (51pt):", count(doc[3], 51.0), "-> trees:", count(doc[3], 51.0) // 3,
      "circle diameter %.1f mm" % (51.0 * MM))
print("  page 6 small-tree circles:", count(doc[5], 51.0), "-> P8 trees:", count(doc[5], 51.0) // 3,
      "; large circles:", count(doc[5], 59.5), "-> P7 trees:", count(doc[5], 59.5) // 3)
print("  page 7 tree circles:", count(doc[6], 59.5), "-> P9 trees:", count(doc[6], 59.5) // 3,
      "diameter %.1f mm" % (59.5 * MM))
print("  P2 circle diameter %.1f mm, P2 exit boxes %.1f mm" % (59.5 * MM, 53.9 * MM))

# Problem 9: numbered exits
print("\nProblem 9 (page 7): numbered exits per picture")
pg = doc[6]
bx = [d["rect"] for d in pg.get_drawings() if abs(d["rect"].width - 35.4) < 0.6]
words = pg.get_text("words")
p9 = []
for b in bx:
    num = [w[4] for w in words if w[4] in ("1", "2") and b.contains(fitz.Point((w[0] + w[2]) / 2, (w[1] + w[3]) / 2))]
    let = letter_under(pg, b, {"A", "B", "C", "D"})
    if num:
        p9.append((b.y0, b.x0, let, num[0]))
pics = {}
for y, x, let, num in p9:
    key = (round(y / 100), 0 if x < 306 else 1)
    pics.setdefault(key, {})[num] = let
names = {(None, None): ""}
for key in sorted(pics):
    first, second = pics[key]["1"], pics[key]["2"]
    ok = [s for s in STARTS if tree(s, 2)[0] == first + second]
    pos = ("top" if key[0] == min(k[0] for k in pics) else "bottom") + (" left" if key[1] == 0 else " right")
    print(f"  {pos}: {first} then {second}: {ok or 'impossible'}")

# ---------------- answers ----------------
print("\nProblem 1: X start", switch("X", 10), " Y start", switch("Y", 10))
for f in "XY":
    w = switch(f, 40)
    assert all(w[i] != w[i + 1] for i in range(39))
    for n in range(1, 41):
        a, b = piles(w[:n], "XY")
        assert abs(a - b) <= 1 and (a - b) * (1 if f == "X" else -1) >= 0
print("  no repeats and piles within one, extra to the first arrow, up to 40 counters: OK")

print("\nProblem 4 (card), table order 5, 8, 7, 4:")
for f in "XY":
    w = switch(f, 8)
    print(f"  counter 1 = {f}: ", [w[k - 1] for k in (5, 8, 7, 4)])
print("Problem 4 (coin): fraction of 8-toss orders where counter k matches counter 1:")
for k in (5, 8, 7, 4):
    m = sum(1 for t in itertools.product("XY", repeat=8) if t[k - 1] == t[0])
    print(f"  counter {k}: {m}/256")

print("\nProblem 3 (coin):")
seven = list(itertools.product("XY", repeat=7))
rep = sum(1 for t in seven if any(t[i] == t[i + 1] for i in range(6)))
x5 = sum(1 for t in seven if t.count("X") == 5)
either = sum(1 for t in seven if t.count("X") in (5, 2))
print(f"  orders with a repeat: {rep}/128; 5X2Y: {x5}/128; 5-and-2 either way: {either}/128")
miss6 = (1 - either / 128) ** 6
print(f"  probability six rows all miss the 5-2 split: {miss6:.4f}")
print("  switch, 7 counters, piles:", {f: piles(switch(f, 7), 'XY') for f in 'XY'})

print("\nProblems 5, 7, 8: the eight starts (top, left lower, right lower)")
for s in STARTS:
    w, end4 = tree(s, 4)
    w48, _ = tree(s, 48)
    assert len(set(w)) == 4 and end4 == s
    assert all(len(set(w48[i:i + 4])) == 4 for i in range(45))
    assert w48 == w * 12
    print(f"  {s}: {w}")
print("  every window of four (to counter 48) reaches all exits; cards return after 4: OK")
orders = {tree(s, 4)[0] for s in STARTS}
print("  distinct four-orders:", len(orders), "of", math.factorial(4))

def nth_second(word, ex):
    seen = 0
    for i, c in enumerate(word, 1):
        if c == ex:
            seen += 1
            if seen == 2:
                return i
def first_to_two(word):
    cnt = {}
    for c in word:
        cnt[c] = cnt.get(c, 0) + 1
        if cnt[c] == 2:
            return c
def last_to_two(word):
    t = {x: nth_second(word, x) for x in "ABCD"}
    return max(t, key=t.get)
bfirst = [s for s in STARTS if first_to_two(tree(s, 12)[0]) == "B"]
blast = [s for s in STARTS if last_to_two(tree(s, 12)[0]) == "B"]
print("\nProblem 7: B first to two:", bfirst, [nth_second(tree(s, 12)[0], 'B') for s in bfirst],
      "| B last to two:", blast, [nth_second(tree(s, 12)[0], 'B') for s in blast])
print("  position of B among counters 1-4 for every start:", {s: tree(s, 4)[0].index('B') + 1 for s in STARTS})
print("Problem 8: first counter on C:", [s for s in STARTS if tree(s, 1)[0] == "C"])

# What the cards show after the trial (the hazard the saved cards address)
print("\nCards after the trial, by problem (start -> end):")
for name, n in (("P2 3 ctrs", 3), ("P6 6 ctrs", 6), ("P7 at counter 5", 5), ("P8 1 ctr", 1), ("P9 2 ctrs", 2)):
    if n in (3,):
        print(f"  {name}: one switch flips 3 times -> opposite arrow")
        continue
    print(f"  {name}: " + ", ".join(f"{s}->{tree(s, n)[1]}" for s in STARTS))

# six-counter reachable piles
six = sorted({piles(tree(s, 6)[0], 'ABCD') for s in STARTS})
print("\nReachable piles after 6 counters:", six)
print("Reachable piles after 8 and 12:", {piles(tree(s, 8)[0], 'ABCD') for s in STARTS}, {piles(tree(s, 12)[0], 'ABCD') for s in STARTS})

# ---------------- materials ----------------
print("\nMaterials (week-91-materials.pdf)")
md = fitz.open(MAT)
for pn in (0, 1):
    sizes = sorted({round(d["rect"].width * MM, 1) for d in md[pn].get_drawings()
                    if abs(d["rect"].width - d["rect"].height) < 0.5 and d["rect"].width > 30})
    print(f"  p.{pn + 1} ({'landscape' if md[pn].rect.width > md[pn].rect.height else 'portrait'}): circle diameters mm {sizes}")
cards = sorted({(round(d['rect'].width * MM, 1), round(d['rect'].height * MM, 1)) for d in md[5].get_drawings()
                if d['rect'].width > 20 and d['rect'].height > 20})
print("  p.6 rectangle sizes mm (w,h):", cards[:8])
sq = [d["rect"] for d in md[6].get_drawings() if abs(d["rect"].width * MM - 15) < 0.6 and abs(d["rect"].height * MM - 15) < 0.6]
print("  p.7 15 mm squares:", len(sq), "(", len(sq) // 12, "strips of 12 )")
print("  p.6 tree card labels:", len([w for w in md[5].get_text('words') if w[4] == 'Tree']))

# ---------------- base guide location ----------------
print("\nBase guide: where the K-1 route sits")
bd = fitz.open(BASE)
for i, pg in enumerate(bd):
    t = " ".join(pg.get_text().split())
    for key in ("K–1 route, adult-read", "That K–1 sustains this is a prediction", "K–1 has an adult-read route", "Preparation, launch and visit choices"):
        if key in t:
            print(f"  p.{i + 1}: {key!r}")
lines3 = bd[2].get_text().splitlines()
print("  top of p.3 after header:", lines3[1:3])

# ---------------- guide header/footer ----------------
gd = fitz.open(GUIDE)
print("\nGuide pages:", len(gd))
for i, pg in enumerate(gd):
    t = pg.get_text()
    assert "Week 91 / Rotor-router machines / K–1 adult guide" in t, i
    assert "Bellingham Math Circle / Week 91 / F91-K-FAC-v1" in t, i
print("  header and footer present on every page")

# ---------------- workload behind the first-route timing ----------------
print("\nCounter moves behind the first route (one move = one counter from entry to exit)")
need = []
for key, n, pl in p2:
    ok = [f for f in "XY" if piles(switch(f, n), "XY") == (pl["X"], pl["Y"])]
    need.append((n, len(ok)))
lo = sum(n if k else 2 * n for n, k in need)
hi = sum(2 * n for n, k in need)
print(f"  P2: at least {lo} moves (each possible picture right first time, both arrows tried for the two impossible ones); {hi} if both arrows are tried for every picture")
print("  P1: 10 moves per row; one row from each arrow = 20 moves and 20 letters")
print("  P3: 7 tosses per row, 6 rows = up to 42 tosses and 42 letters")
print("  P5: 4 counters x 8 starts = 32 tree moves (64 card flips) for a complete check; 9 trees x 3 circles = 27 arrows to draw")
