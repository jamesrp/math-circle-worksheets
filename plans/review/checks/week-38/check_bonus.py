#!/usr/bin/env python3
"""Week 38 bonus packet (W38-BONUS-v1) and its adult guide: independent check.

Reads the delivered week-38-bonus.pdf (vector paths with pypdf, word boxes
with pdftotext) and rebuilds every printed band in the cell model of
surfaces.py:
  P1  the four lane recipes: corner marks -> seam, dashed lane lines -> cuts,
      end labels checked against the seam; pieces and closed edges per piece.
  P2  the local two-strip visual: which marks the alignment lines pair, and
      what seam that pairing is given the 'before joining' marks; the four
      three-strip seam words; the parity rule over all words up to length 6;
      the guide's four-strip designs.
  P3  bands A-D rasterised from the printed rectangles, corner marks and grey
      holes/notches (clip boxes respected); closed edges and pieces; the
      four-edge designs from the guide.
Guide claims are transcribed by hand from week-38-bonus-facilitator.pdf.

Run: python3 check_bonus.py > out_check_bonus.txt
"""
import itertools
import math
from common import WEEK, BONUS, page_shapes, words, Checker
from surfaces import Band

C = Checker()
pages = [[d for d in p if (d["bbox"][2] - d["bbox"][0]) > 1e-6 or (d["bbox"][3] - d["bbox"][1]) > 1e-6]
         for p in page_shapes(WEEK / BONUS)]
wpages = words(WEEK / BONUS)


def black(c):
    return c is not None and max(c) < 0.05


def white(c):
    return c is not None and min(c) > 0.99


def inside(p, bb, pad=0.0):
    return bb[0] - pad <= p[0] <= bb[2] + pad and bb[1] - pad <= p[1] <= bb[3] + pad


def corner_marks(shapes, bb, pad=1.5):
    cx, cy = (bb[0] + bb[2]) / 2, (bb[1] + bb[3]) / 2
    res = {}
    for d in shapes:
        size = max(d["bbox"][2] - d["bbox"][0], d["bbox"][3] - d["bbox"][1])
        if size > 3 or not inside(d["c"], bb, pad):
            continue
        if d["kind"] == "curve" and black(d["fill"]):
            k = "dot"
        elif d["kind"] == "poly4" and white(d["fill"]):
            k = "sq"
        else:
            continue
        res[("L" if d["c"][0] < cx else "R", "T" if d["c"][1] < cy else "B")] = k
    return res


def seam_from_marks(cm):
    """'join matching corner marks': right-end corner pairs with the left-end
    corner bearing the same mark."""
    return "M" if cm[("R", "T")] == cm[("L", "T")] else "R"


def big_rects(shapes, minw):
    return sorted([d for d in shapes if d["kind"] == "poly4" and d["fill"] is None and black(d["stroke"])
                   and d["bbox"][2] - d["bbox"][0] > minw], key=lambda d: (round(d["bbox"][1]), d["bbox"][0]))


print("######## Problem 1 (page 1): lane recipes")
p1, w1 = pages[0], wpages[0]
results = {}
for rect in big_rects(p1, 100):
    bb = rect["bbox"]
    cm = corner_marks(p1, bb)
    seam = seam_from_marks(cm)
    lanes_y = sorted(d["c"][1] for d in p1 if d["dash"] and d["kind"] == "line" and inside(d["c"], bb))
    n = len(lanes_y) + 1
    h = bb[3] - bb[1]
    expected = [bb[1] + h * j / n for j in range(1, n)]
    equal = all(abs(a - b) < 0.05 for a, b in zip(lanes_y, expected))
    cap = [w["t"] for w in w1 if bb[1] + h < w["c"][1] < bb[3] + 10 and w["t"] in ("M", "R")]
    left = sorted([(w["c"][1], int(w["t"])) for w in w1 if w["t"].isdigit() and abs(w["c"][0] - (bb[0] - 5)) < 3 and bb[1] < w["c"][1] < bb[3]])
    right = sorted([(w["c"][1], int(w["t"])) for w in w1 if w["t"].isdigit() and abs(w["c"][0] - (bb[2] + 5)) < 3 and bb[1] < w["c"][1] < bb[3]])
    # lane centres
    centres = [bb[1] + h * (j + .5) / n for j in range(n)]
    lab_ok = all(abs(y - c) < 1.5 for (y, _), c in zip(left, centres)) and all(abs(y - c) < 1.5 for (y, _), c in zip(right, centres))
    # labels consistent with the seam: left lane j (row j from top) is joined to right-end row sigma(j);
    # 'join matching' means the right label at row sigma(j) equals the left label at row j
    sigma = (lambda j: j) if seam == "M" else (lambda j: n - 1 - j)
    lab_consistent = all(left[j][1] == right[sigma(j)][1] for j in range(n))
    W = 2 * n
    band = Band([seam], 16, W, cuts=[2 * j for j in range(1, n)])
    s = band.summary()
    key = f"{n}{seam}"
    results[key] = s
    print(f"{n} lanes, marks {cm}, seam {seam}, caption {cap}, left labels {[t for _, t in left]}, right {[t for _, t in right]}")
    print(f"   cut result: {s}")
    C.ok(cap == [seam], f"P1 {n} lanes: corner marks encode {seam}, as captioned")
    C.ok(equal and n in (3, 4), f"P1 {n} lanes: dashed lane lines equally spaced")
    C.ok(lab_ok and lab_consistent, f"P1 {n} lanes / {seam}: end labels sit at lane centres and matching labels agree with the corner-mark seam")
    lanes_per_piece = sorted(sorted({j // 2 + 1 for (_, _, j) in fs}) for fs in band.pieces)
    print("   lanes per piece:", lanes_per_piece)
    results[key + "_lanes"] = lanes_per_piece

C.ok(results["3M"]["pieces"] == 3 and results["3M"]["boundary_circles"] == 6 and results["3M"]["types"] == ["annulus"] * 3,
     "guide P1: 3M three annuli, total six edges")
C.ok(results["3R"]["pieces"] == 2 and results["3R"]["per_piece_boundaries"] == [1, 2] and sorted(results["3R"]["types"]) == ["Mobius band", "annulus"]
     and results["3R_lanes"] == [[1, 3], [2]], "guide P1: 3R lanes 1/3 annulus + lane 2 Mobius band, edges 2 and 1, total 3")
C.ok(results["4M"]["pieces"] == 4 and results["4M"]["boundary_circles"] == 8, "guide P1: 4M four annuli, total 8")
C.ok(results["4R"]["pieces"] == 2 and results["4R"]["boundary_circles"] == 4 and results["4R"]["types"] == ["annulus"] * 2
     and results["4R_lanes"] == [[1, 4], [2, 3]], "guide P1: 4R lane pairs 1/4 and 2/3, two annuli, total 4")
mixed = [k for k in ("3M", "3R", "4M", "4R") if set(results[k]["per_piece_boundaries"]) >= {1, 2}]
C.ok(mixed == ["3R"], "P1 question: only 3R has both a one-edge and a two-edge piece (guide)")

# overview: general n
for n in range(1, 9):
    for seam in "MR":
        b = Band([seam], 8, 2 * n, cuts=[2 * j for j in range(1, n)])
        s = b.summary()
        if seam == "M":
            exp = (n, 2 * n, ["annulus"] * n)
        else:
            exp = ((n + 1) // 2, 2 * (n // 2) + (n % 2), sorted(["annulus"] * (n // 2) + (["Mobius band"] if n % 2 else [])))
        C.ok((s["pieces"], s["boundary_circles"], sorted(s["types"])) == exp,
             f"overview lanes n={n} {seam}: {s['pieces']} pieces, {s['boundary_circles']} edges, {sorted(s['types'])}")

print("\n######## Problem 2 (page 2): the local two-strip visual")
p2, w2 = pages[1], wpages[1]
rows = {}
for d in p2:
    size = max(d["bbox"][2] - d["bbox"][0], d["bbox"][3] - d["bbox"][1])
    if d["c"][1] > 80 or size > 3:
        continue
    if d["kind"] == "curve" and black(d["fill"]):
        k = "dot"
    elif d["kind"] == "poly4" and white(d["fill"]):
        k = "sq"
    else:
        continue
    row = "M" if d["c"][1] < 60 else "R"
    rows.setdefault(row, []).append((k, d["c"]))
grey = [d for d in p2 if d["kind"] == "line" and d["stroke"] and abs(d["stroke"][0] - 0.55) < 0.01 and d["c"][1] < 80]
for row in ("M", "R"):
    marks = rows[row]
    before = [(k, c) for k, c in marks if c[0] < 60]
    s1 = {("T" if c[1] < min(cc[1] for _, cc in before) + 2 else "B"): k for k, c in before if c[0] < 37}
    s2 = {("T" if c[1] < min(cc[1] for _, cc in before) + 2 else "B"): k for k, c in before if c[0] > 37}
    pairs = []
    for g in grey:
        if (row == "M") != (g["c"][1] < 60):
            continue
        a, b = g["pts"][0], g["pts"][-1]
        if a[0] > b[0]:
            a, b = b, a
        ka = min(marks, key=lambda m: math.dist(m[1], a))[0]
        kb = min(marks, key=lambda m: math.dist(m[1], b))[0]
        pairs.append((ka, kb, "crossing" if abs(a[1] - b[1]) > 1 else "straight"))
    pairs = sorted(set(pairs))
    # the pairing as a map of strip-1 corners to strip-2 corners (flat positions before joining)
    corner_map = {}
    for ka, kb, _ in pairs:
        t1 = [pos for pos, k in s1.items() if k == ka][0]
        t2 = [pos for pos, k in s2.items() if k == kb][0]
        corner_map[t1] = t2
    implied = "M" if corner_map.get("T") == "T" else "R"
    print(f"row {row}: before joining strip1 end {s1}, strip2 end {s2}; alignment lines pair {pairs}; "
          f"strip1 corner -> strip2 corner {corner_map} => seam {implied}")
    rows[row] = implied
C.ok(rows["M"] == "M", "P2 visual, M row: aligning the same marks (dot-dot) with unchanged marks is a matching seam")
C.ok(rows["R"] == "R",
     "P2 visual, R row: the drawn pairing should be a reversing seam (top corner of strip 1 to bottom corner of strip 2);"
     " a FAIL here means the R row pairs the same corners as the M row (finding in math.md)")

# what the literal 'align the same marks' rule builds from the four printed circles
words_p2 = {}
for w in w2:
    if w["t"] in ("M", "R") and w["c"][1] > 110:
        words_p2.setdefault(w["c"][1], []).append(w)
labels = sorted([(w["c"][1], w["c"][0], w["t"]) for w in w2 if w["t"] in ("M", "R") and w["c"][1] > 110])
row_tops = sorted({round(d["bbox"][1], 1) for d in big_rects(p2, 30) if d["bbox"][1] > 110})
seq = []
for top in row_tops:
    mids = [t for (y, x, t) in sorted(labels, key=lambda r: r[1]) if top - 1 < y < top + 16]
    close = [t for (y, x, t) in labels if top + 16 < y < top + 34]
    seq.append("".join(mids) + "".join(close))
print("P2 printed seam words (between strips, then closing seam):", seq)
C.ok(seq == ["MMM", "MMR", "MRR", "RRR"], "P2: printed words are MMM, MMR, MRR, RRR (guide order)")
edges = {}
for word in seq:
    b = Band(list(word), 6, 4)
    edges[word] = b.summary()
    print(f"   {word}: {b.summary()}")
C.ok([edges[w]["boundary_circles"] for w in seq] == [2, 1, 2, 1] and all(edges[w]["pieces"] == 1 for w in seq),
     "guide P2: MMM 2 edges, MMR 1, MRR 2, RRR 1 (one connected band each)")
lit = [Band(["M"] * 3, 6, 4).summary()["boundary_circles"] for _ in seq]
print("   if every seam pairs dot with dot (the R row's 'align the same marks' taken literally): edges", lit)
allok = True
for L in range(1, 7):
    for word in itertools.product("MR", repeat=L):
        b = Band(list(word), 3, 2, lengths=[3 + (i % 2) for i in range(L)])
        nb = b.summary()["boundary_circles"]
        allok &= (b.summary()["pieces"] == 1 and nb == (1 if word.count("R") % 2 else 2))
C.ok(allok, "overview parity rule: every M/R word of length 1-6 (unequal strip lengths too) gives 1 edge iff #R odd")
for word, exp in (("RMMM", 1), ("RRMM", 2), ("MMMM", 2)):
    C.ok(Band(list(word), 6, 4).summary()["boundary_circles"] == exp, f"guide P2 four-strip design {word}: {exp} edge(s)")

print("\n######## Problem 3 (page 3): holes and notches")
p3, w3 = pages[2], wpages[2]
STEP = 0.5  # mm per cell


def raster(rect, holes, seam):
    bb = rect["bbox"]
    L = round((bb[2] - bb[0]) / STEP)
    W = round((bb[3] - bb[1]) / STEP)
    removed = set()
    for i in range(L):
        for j in range(W):
            x = bb[0] + (i + .5) * STEP
            y = bb[1] + (j + .5) * STEP
            for hc, r, clip in holes:
                if math.dist((x, y), hc) < r and inside((x, y), clip):
                    removed.add((0, i, j))
    return Band([seam], L, W, removed=removed), L, W, removed


p3res = {}
for rect in big_rects(p3, 50):
    bb = rect["bbox"]
    if bb[3] - bb[1] > 35:
        continue
    cm = corner_marks(p3, bb)
    seam = seam_from_marks(cm)
    holes = [(d["c"], d["rx"], d["clip"]) for d in p3 if d["kind"] == "curve" and d["fill"] and abs(d["fill"][0] - 0.7) < 0.01
             and d["clip"] and math.dist(((d["clip"][0] + d["clip"][2]) / 2, (d["clip"][1] + d["clip"][3]) / 2), rect["c"]) < 0.1]
    cap = [w["t"] for w in w3 if bb[0] < w["c"][0] < bb[2] and bb[3] < w["c"][1] < bb[3] + 10 and w["t"] not in ("/",)]
    name, capseam = cap[0], cap[-1]
    band, L, W, removed = raster(rect, holes, seam)
    s = band.summary()
    p3res[name] = s
    where = []
    for hc, r, clip in holes:
        where.append(("interior" if inside(hc, (bb[0] + r, bb[1] + r, bb[2] - r, bb[3] - r)) else
                      "long edge" if abs(hc[1] - bb[1]) < .1 or abs(hc[1] - bb[3]) < .1 else
                      "short end" if abs(hc[0] - bb[0]) < .1 or abs(hc[0] - bb[2]) < .1 else "?",
                      round((hc[1] - bb[1]) / (bb[3] - bb[1]), 3)))
    print(f"{name}/{capseam}: marks {cm} -> {seam}; holes {where}; {L}x{W} cells, {len(removed)} removed; {s}")
    C.ok(seam == capseam, f"P3 {name}: corner marks encode the captioned seam {capseam}")
exp = {"A": 3, "B": 2, "C": 1, "D": 3}
for k, v in exp.items():
    C.ok(p3res[k]["pieces"] == 1 and p3res[k]["boundary_circles"] == v, f"guide P3: band {k} is one piece with {v} closed edge(s)")

# D's half-holes are one hole because they sit at the same height on both ends (printed: 0.5 and 0.5).
# Offset copy for contrast: unmatched half-holes at a matching seam leave two separate openings.
Lc, Wc = 40, 20
left = {(0, 0, j) for j in range(3, 7)}
right_same = {(0, Lc - 1, j) for j in range(3, 7)}
right_off = {(0, Lc - 1, j) for j in range(12, 16)}
s_same = Band(["M"], Lc, Wc, removed=left | right_same).summary()
s_off = Band(["M"], Lc, Wc, removed=left | right_off).summary()
print("matched half-holes:", s_same, " offset half-holes:", s_off)
C.ok(s_same["boundary_circles"] == 3 and s_off["boundary_circles"] == 4,
     "D contrast: matched half-holes form one hole (3 edges); offset ones would form two (4 edges), as the guide's extension says")
for name, seam, holes, expect in [
    ("M + 2 interior disks", "M", 2, 4), ("R + 3 interior disks", "R", 3, 4),
    ("M + 1 disk", "M", 1, 3), ("R + 2 disks", "R", 2, 3)]:
    L, W = 60, 12
    removed = set()
    for h in range(holes):
        ci = 10 + 20 * h
        removed |= {(0, i, j) for i in range(ci, ci + 2) for j in range(5, 7)}
    b = Band([seam], L, W, removed=removed)
    C.ok(b.summary()["pieces"] == 1 and b.summary()["boundary_circles"] == expect, f"guide P3 design check: {name} -> {expect} closed edges")

print("\n######## Guide arithmetic")
C.ok(4 + 3 + 4 + 2 == 13, "per pair: 4 + 3 + 4 + 2 = 13 strips")
C.ok(6 * 13 == 78 and 24 + 18 + 24 + 12 == 78 and 6 * 4 == 24 and 6 * 3 == 18 and 6 * 2 == 12 and 6 * 12 == 72,
     "six kits: 78 strips = 24 + 18 + 24 + 12, 72 edge dots")
C.ok(abs(80 / 3 - 26.667) < 1e-3 and [80 * j / 4 for j in (1, 2, 3)] == [20, 40, 60], "lane cut positions 80/3, 160/3 mm and 20/40/60 mm")
C.summary()
