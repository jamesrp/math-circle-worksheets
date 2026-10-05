"""Read every diagram of the delivered Week 60 student PDF back from the PDF
(PyMuPDF text spans and vector drawings) and check it against the text and
the mathematics.

* headers / footers / band per page, problem numbers 1-9 in order;
* page 1 practice-round boxes (legal under the page-1 rules);
* page 2 practice card and its outcome; the nine 0/4/6 two-offer cards;
* page 3: the 27 three-offer cards;
* page 4: the two position boxes (label, current offer, number and roundness
  of the turn counters);
* page 6: the bag labels and the nine cards of each new bag;
* every card: one score line, the right number of dividers, equal sizes.

Run: python3 check_diagrams.py   (needs PyMuPDF; writes out_check_diagrams.txt
and extracted.json beside itself)
"""
import itertools
import json
from collections import Counter

import sys

import pymupdf

sys.dont_write_bytecode = True  # keep the committed checks folder free of __pycache__

from w60common import HERE, REPO, STUDENT_PDF, Log, play

L = Log()
say, check, note = L.say, L.check, L.note
doc = pymupdf.open(str(STUDENT_PDF))
check(doc.page_count == 7, f"student PDF has 7 pages ({doc.page_count})")


def spans(page):
    out = []
    for b in page.get_text("dict")["blocks"]:
        for ln in b.get("lines", []):
            for s in ln["spans"]:
                if s["text"].strip():
                    x0, y0, x1, y1 = s["bbox"]
                    out.append(dict(t=s["text"].strip(), size=round(s["size"], 2),
                                    cx=(x0 + x1) / 2, cy=(y0 + y1) / 2, bbox=(x0, y0, x1, y1)))
    return out


def lines_text(page):
    return [" ".join(ln.split()) for ln in page.get_text().splitlines() if ln.strip()]


def inside(s, r, pad=0.5):
    return r.x0 - pad <= s["cx"] <= r.x1 + pad and r.y0 - pad <= s["cy"] <= r.y1 + pad


def dashed_cards(page):
    cards = []
    for d in page.get_drawings():
        if d.get("dashes", "[] 0") != "[] 0" and len(d["items"]) == 4 and d["rect"].width > 100:
            cards.append(d["rect"])
    return sorted(cards, key=lambda r: (round(r.y0), r.x0))


def solid_vlines_in(page, r):
    n = 0
    for d in page.get_drawings():
        if d.get("dashes", "[] 0") == "[] 0" and len(d["items"]) == 1 and d["items"][0][0] == "l":
            p, q = d["items"][0][1], d["items"][0][2]
            if abs(p.x - q.x) < 0.01 and r.contains(p) and r.contains(q):
                n += 1
    return n


def read_cards(page, nd):
    """Return a list of (word tuple, rect, has_score) for every dashed card."""
    sp = spans(page)
    out = []
    for r in dashed_cards(page):
        digits = sorted((s for s in sp if inside(s, r) and s["t"].isdigit() and s["size"] > 13), key=lambda s: s["cx"])
        score = [s for s in sp if inside(s, r) and s["t"] == "score"]
        out.append(dict(word=tuple(int(s["t"]) for s in digits), rect=r, score=len(score),
                        dividers=solid_vlines_in(page, r), sizes=sorted({s["size"] for s in digits})))
    return out


extracted = {"pdf": str(STUDENT_PDF.relative_to(REPO)), "pages": []}

# ------------------------------------------------------------ headers, footers, problems
say("== Headers, footers, problem numbers ==")
bands = {1: "3–5", 2: "3–5", 3: "3–5", 4: "4–5", 5: "4–5", 6: "3–5", 7: "4–5"}
probs_on = {}
for i, p in enumerate(doc, 1):
    lt = lines_text(p)
    check(lt[0] == f"Week 60 / Take it or pass / Grades {bands[i]}", f"p{i} header: {lt[0]!r}")
    check(any(l == "Bellingham Math Circle / Week 60 / W60-S-v2" for l in lt), f"p{i} footer present")
    probs_on[i] = [int(l.split()[1].rstrip(":")) for l in lt if l.startswith("Problem ") and l.split()[1].rstrip(":").isdigit()]
order = [n for i in range(1, 8) for n in probs_on[i]]
say(f"  problems by page: {probs_on}")
check(order == list(range(1, 10)), "problems numbered 1-9 consecutively")

# ------------------------------------------------------------ page 1 practice round
say("")
say("== Page 1: practice round (tickets 1, 2, 5) ==")
p1 = lines_text(doc[0])
seq = ["offer 2", "two counters", "pass 2; return it", "mix; one counter left", "next offer 1", "must take 1",
       "round score: 1"]
pos = [p1.index(s) if s in p1 else -1 for s in seq]
check(all(x >= 0 for x in pos) and pos == sorted(pos), f"practice boxes read in order: {seq}")
check(play((2, 1), lambda pre, left: False) == 1,
      "legal under the rules: pass 2 with two counters, remove one, compulsory 1 with one counter -> score 1")
check("With one counter left, you must take the offer, even if it is 0. Remove one turn counter after deciding on each offer."
      in " ".join(p1), "counter convention: n counters at the first of n offers; one counter at the last")

# ------------------------------------------------------------ page 2
say("")
say("== Page 2: practice card and the nine 0/4/6 cards ==")
pg = doc[1]
sp = spans(pg)
# practice card: the solid rectangle containing large digits 3 and 1, left of the first arrow
solid = [d["rect"] for d in pg.get_drawings() if d.get("dashes", "[] 0") == "[] 0"
         and 30 < d["rect"].width < 130 and 30 < d["rect"].height < 70 and d["rect"].y1 < 200]
pc = None
for r in solid:
    dg = sorted((s for s in sp if inside(s, r) and s["t"].isdigit()), key=lambda s: s["cx"])
    if len(dg) == 2:
        pc = tuple(int(s["t"]) for s in dg)
check(pc == (3, 1), f"practice complete card reads {pc}")
txt2 = " ".join(lines_text(pg))
check("this rule takes 3 or 5 and passes 1" in txt2 and "take the first offer: 3" in txt2
      and "the later 1 is unseen" in txt2 and "score 3" in txt2, "practice outcome boxes: take 3, later 1 unseen, score 3")
check(play(pc, lambda pre, left: pre[-1] in (3, 5)) == 3, "rule 'take 3 or 5, pass 1' on (3, 1) scores 3")
c2 = read_cards(pg, 2)
words2 = [c["word"] for c in c2]
check(Counter(words2) == Counter(itertools.product((0, 4, 6), repeat=2)),
      f"nine dashed cards are exactly the nine 0/4/6 pairs, once each: {words2}")
extracted["pages"].append({"page": 2, "cards": [list(w) for w in words2]})

# ------------------------------------------------------------ page 3
say("")
say("== Page 3: the 27 three-offer cards ==")
c3 = read_cards(doc[2], 3)
words3 = [c["word"] for c in c3]
check(len(c3) == 27 and Counter(words3) == Counter(itertools.product((0, 4, 6), repeat=3)),
      f"27 dashed cards are exactly the 27 0/4/6 triples, once each ({len(c3)} cards)")
extracted["pages"].append({"page": 3, "cards": [list(w) for w in words3]})
t3 = " ".join(lines_text(doc[2]))
check("A: Take 4 or 6 whenever it appears. Pass 0." in t3 and
      "B: Take only 6 on the first offer. On the second, take 4 or 6 and pass 0." in t3 and
      "Both plans take the last offer if they reach it." in t3, "plans A and B printed as checked in check_math.py")

# ------------------------------------------------------------ page 4
say("")
say("== Page 4: position boxes for Problem 5 ==")
pg = doc[3]
sp = spans(pg)
dr = pg.get_drawings()
boxes = sorted([d["rect"] for d in dr if any(it[0] == "c" for it in d["items"]) and d["rect"].width > 150],
               key=lambda r: r.x0)
circles = [d["rect"] for d in dr if d["items"] and all(it[0] == "c" for it in d["items"]) and len(d["items"]) == 4]
res = []
for b in boxes:
    cs = [c for c in circles if b.contains(c)]
    lab = [s["t"] for s in sp if inside(s, b) and "offers left" in s["t"]]
    big = [s["t"] for s in sp if inside(s, b) and s["t"].isdigit() and s["size"] > 15]
    round_ = all(abs(c.width - c.height) < 0.01 for c in cs)
    radii = {round(c.width, 2) for c in cs}
    res.append((lab, big, len(cs), round_, radii))
    say(f"  box at x={b.x0:.0f}: label {lab}, current {big}, {len(cs)} counters, round={round_}, diameters {radii} pt")
check(len(res) == 2, "two position boxes")
check(res[0][0] == ["2 offers left, including this one"] and res[0][1] == ["4"] and res[0][2] == 2,
      "left box: current 4, 2 offers left, two counters")
check(res[1][0] == ["3 offers left, including this one"] and res[1][1] == ["4"] and res[1][2] == 3,
      "right box: current 4, 3 offers left, three counters")
check(all(r[3] for r in res) and len(set().union(*[r[4] for r in res])) == 1, "all counters are equal circles")
extracted["pages"].append({"page": 4, "positions": [{"label": r[0], "current": r[1], "counters": r[2]} for r in res]})

# ------------------------------------------------------------ page 6
say("")
say("== Page 6: the two new bags ==")
pg = doc[5]
sp = spans(pg)
c6 = read_cards(pg, 2)
labels = []
for b in pg.get_text("dict")["blocks"]:
    for ln in b.get("lines", []):
        t = " ".join(" ".join(x["text"] for x in ln["spans"]).split())
        if t.startswith("Bag:"):
            labels.append(dict(t=t, cy=(ln["bbox"][1] + ln["bbox"][3]) / 2))
labels.sort(key=lambda s: s["cy"])
say(f"  bag labels: {[(s['t'], round(s['cy'])) for s in labels]}")
check([s["t"] for s in labels] == ["Bag: 0, 3, 6", "Bag: 0, 5, 6"], "labels 'Bag: 0, 3, 6' then 'Bag: 0, 5, 6'")
grp1 = [c["word"] for c in c6 if labels[0]["cy"] < c["rect"].y0 < labels[1]["cy"]]
grp2 = [c["word"] for c in c6 if c["rect"].y0 > labels[1]["cy"]]
check(Counter(grp1) == Counter(itertools.product((0, 3, 6), repeat=2)), f"cards under 'Bag: 0, 3, 6' are its nine pairs: {grp1}")
check(Counter(grp2) == Counter(itertools.product((0, 5, 6), repeat=2)), f"cards under 'Bag: 0, 5, 6' are its nine pairs: {grp2}")
extracted["pages"].append({"page": 6, "cards_036": [list(w) for w in grp1], "cards_056": [list(w) for w in grp2]})

# ------------------------------------------------------------ card anatomy and sizes
say("")
say("== Card anatomy and equal sizes ==")
two = c2 + c6
check(all(c["score"] == 1 for c in two + c3), "every card has exactly one 'score' line")
check(all(c["dividers"] == 1 for c in two) and all(c["dividers"] == 2 for c in c3),
      "two-offer cards have one divider, three-offer cards two")
s2 = {(round(c["rect"].width, 2), round(c["rect"].height, 2)) for c in two}
s3 = {(round(c["rect"].width, 2), round(c["rect"].height, 2)) for c in c3}
say(f"  two-offer card sizes (pt): {s2}; three-offer: {s3}")
check(len(s2) == 1 and len(s3) == 1, "all cards of each length have equal size (equal weight when sorted/pooled)")
check(len({tuple(c['sizes']) for c in two}) == 1 and len({tuple(c['sizes']) for c in c3}) == 1,
      "digits on cards of each length share one font size")

# ------------------------------------------------------------ page 7 text
say("")
say("== Page 7 ==")
t7 = " ".join(lines_text(doc[6]))
check("Use a bag with tickets 0, 5, 6." in t7 and "three-offer rounds and for four-offer rounds" in t7,
      "Problem 8 bag 0,5,6, horizons three and four")
check("Could adding one allowed offer lower the best possible average score? Could it leave that average unchanged?" in t7,
      "Problem 9 asks both questions")

(HERE / "extracted.json").write_text(json.dumps(extracted, indent=1))
L.write(HERE / "out_check_diagrams.txt")
