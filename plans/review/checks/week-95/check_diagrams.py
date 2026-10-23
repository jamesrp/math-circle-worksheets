#!/usr/bin/env python3
"""Diagram and printed-data checks for Week 95 student PDFs (PyMuPDF).

Reads the delivered PDFs, not the builder. For every card (11.9 x 13.0 pt
rectangle) it finds the letter printed inside it and whether a marker dot
(2 pt filled circle) lies inside it, groups cards into the panels of each
diagram and compares them with what the text of the page says. It also reads
the printed tables, headers, footers and problem numbers.

Run: python3 check_diagrams.py   (writes check_diagrams.py.out beside itself)
"""
from pathlib import Path
import re
import sys
import warnings

warnings.filterwarnings("ignore")
import pymupdf as fitz  # noqa: E402

HERE = Path(__file__).resolve().parent


def find_repo(start):
    # Committed copy lives in plans/review/checks/week-95/ (repo = four folders up);
    # the working copy lives in tmp/review-runs/week-95/. Walk up to the repo root.
    for p in [start] + list(start.parents):
        if (p / "AGENTS.md").exists() and (p / "lowell-math-circle-year-2").is_dir():
            return p
    raise SystemExit("repository root not found")


REPO = find_repo(HERE)
# Reads the version reviewed on October 23 (366c49d, footers W95-*-v1). Week 95 was since converted
# to problem files (e93a136) and revised (1e29ee4 card shoulds, dfbc5e4 footer ids), so the reviewed
# PDFs come from archive-before-card-fixes (MD5-identical to 366c49d). DELIVERED is the current print
# folder; source/week-95/review/check_card_fixes_2026_10_23.py checks the current packets.
DELIVERED = REPO / "lowell-math-circle-year-2" / "week-95"
WEEK = DELIVERED / "archive-before-card-fixes-2026-10-23"
OUT, FAILS = [], []


def log(s=""):
    OUT.append(s)


def check(cond, msg):
    log(("PASS " if cond else "FAIL ") + msg)
    if not cond:
        FAILS.append(msg)


def cards(page):
    rects, dots, circles, letters = [], [], [], []
    for d in page.get_drawings():
        r = d["rect"]
        w, h = round(r.width, 1), round(r.height, 1)
        if d["type"] == "s" and (w, h) == (11.9, 13.0):
            rects.append(r)
        elif d["type"] == "f" and (w, h) == (2.0, 2.0):
            dots.append(r)
        elif d["type"] == "f" and (w, h) == (3.1, 3.1):
            dots.append(r)
        elif d["type"] == "s" and (w, h) == (13.0, 13.0):
            circles.append(r)
    for b in page.get_text("dict")["blocks"]:
        for line in b.get("lines", []):
            for s in line["spans"]:
                t = s["text"].strip()
                if len(t) == 1 and t.isalpha() and abs(s["size"] - 8.0) < 0.2:
                    letters.append((fitz.Rect(s["bbox"]), t))
    out = []
    for r in rects:
        lab = [t for bb, t in letters if r.contains(fitz.Point((bb.x0 + bb.x1) / 2, (bb.y0 + bb.y1) / 2))]
        dot = any(r.contains(fitz.Point((q.x0 + q.x1) / 2, (q.y0 + q.y1) / 2)) for q in dots)
        out.append(dict(x=r.x0, y=r.y0, label="".join(lab), marked=dot))
    return out, circles, dots


def rows(cs, x0=0, x1=1e9, y0=0, y1=1e9):
    sel = [c for c in cs if x0 <= c["x"] <= x1 and y0 <= c["y"] <= y1]
    sel.sort(key=lambda c: (round(c["y"]), c["x"]))
    return [(c["label"] + ("*" if c["marked"] else "")) for c in sel]


def text_of(page):
    return page.get_text()


docs = {k: fitz.open(WEEK / f"week-95-{k}.pdf") for k in ("grades-2-3", "grades-4-5")}

# ---------------------------------------------------- headers, footers, problems
for k, band, ident in (("grades-2-3", "2–3", "23"), ("grades-4-5", "4–5", "45")):
    d = docs[k]
    nums = []
    for i, p in enumerate(d):
        t = text_of(p)
        check(f"Week 95 / Count the unseen / Grades {band}" in t, f"{k} p{i+1}: header")
        check(f"Bellingham Math Circle / Week 95 / W95-{ident}-v1" in t, f"{k} p{i+1}: footer")
        nums += [int(m) for m in re.findall(r"Problem (\d+):", t)]
    check(nums == list(range(1, len(nums) + 1)), f"{k}: problems numbered consecutively {nums}")

# ------------------------------------------------------------- page-1 demo
for k in docs:
    p = docs[k][0]
    cs, circles, _ = cards(p)
    start = rows(cs, y0=210, y1=225)
    bag1 = rows(cs, x1=230, y0=285, y1=300)
    caught1 = rows(cs, x1=230, y0=320, y1=335)
    mixed = rows(cs, x0=240, x1=380)
    bag2 = rows(cs, x0=390, y0=285, y1=300)
    caught2 = rows(cs, x0=390, y0=320, y1=335)
    log(f"{k} demo: start {start}; bag after 1st {bag1}; 1st catch {caught1}; mixed {mixed}; "
        f"bag after 2nd {bag2}; 2nd catch {caught2}")
    check(start == list("ABCDEF"), f"{k} demo: start shows six unmarked A-F")
    check(bag1 == list("BDEF"), f"{k} demo: bag after first catch B,D,E,F unmarked (matches 'Bag: B, D, E, F')")
    check(caught1 == ["A", "C", "A*", "C*"], f"{k} demo: first catch A,C then the same A,C marked")
    check(sorted(mixed) == sorted(["D", "A*", "F", "C*", "E", "B"]), f"{k} demo: returned bag = same six, A and C marked")
    check(bag2 == ["A*", "B", "E"], f"{k} demo: bag after second catch A*,B,E (matches 'Bag: A, B, E')")
    check(caught2 == ["C*", "D", "F"], f"{k} demo: second catch C*,D,F; one overlap")
    # the overlap ring (20.4 pt circle) must surround C
    ring = [d["rect"] for d in p.get_drawings() if d["type"] == "s"
            and round(d["rect"].width, 1) == 20.4 and round(d["rect"].height, 1) == 20.4]
    cC = [c for c in cs if c["label"] == "C" and c["x"] > 390][0]
    check(len(ring) == 1 and ring[0].contains(fitz.Point(cC["x"] + 6, cC["y"] + 6)), f"{k} demo: overlap ring is around C")
    t = text_of(p)
    if "catch 2" in t and "First catch: A, C" in t:
        log(f"NOTE {k} demo: the arrow into 'First catch: A, C' is labelled 'catch 2' "
            f"(means 'catch two objects'; reads like 'catch #2' beside 'Second catch')")

# ------------------------------------------------------------- Grades 2-3 p2
p = docs["grades-2-3"][1]
cs, _, _ = cards(p)
ys = sorted({round(c["y"]) for c in cs})
log(f"grades-2-3 p2 card rows at y = {ys}")
r = [rows(cs, y0=y - 1, y1=y + 1) for y in ys]
check(r[0] == list("ABCDE") and r[1] == ["B*", "D*", "E*", "F", "G"],
      f"G23 P2 record: first {r[0]}, second {r[1]} (dots exactly on repeated B, D, E)")
check(r[2] == list("ABCDE") and r[3] == list("FGHIJ"), f"G23 P3 record: first {r[2]}, second {r[3]}, no dots")

# ------------------------------------------------------------- tables
t23 = [text_of(p) for p in docs["grades-2-3"]]
t45 = [text_of(p) for p in docs["grades-4-5"]]


def table_after(text, header, nrows):
    i = text.index(header)
    toks = text[i + len(header):].split()
    return toks[: nrows * 2]


tok = table_after(t23[2], "Guess: 8 or 16", 6)
check(tok == ["1", "2", "2", "1", "3", "3", "4", "1", "5", "2", "6", "0"], f"G23 P4 table rounds/overlaps {tok}")
check("Bag total" in t23[3] and all(x in t23[3].split() for x in ("6", "8", "12")), "G23 P6 table rows 6, 8, 12")
i = t45[2].index("Rule’s guess") if "Rule’s guess" in t45[2] else t45[2].index("Rule's guess")
seg = t45[2][i:].split("Problem 5")[0].split()
log(f"G45 P4 table tokens: {seg}")
check(seg[2:14] == ["1", "1", "36", "2", "2", "18", "3", "3", "12", "4", "2", "18"]
      and seg[14:16] == ["5", "0"] and "No matching total" in " ".join(seg), "G45 P4 table matches 36/R")
seg2 = t45[1].split("Smallest total")[1].split("Problem 3")[0].split()
check(seg2 == ["A", "2", "B", "0"], f"G45 P2 table records A:2, B:0 {seg2}")

# ------------------------------------------------------------- Grades 4-5 p2 (P3)
p = docs["grades-4-5"][1]
cs, circles, dots = cards(p)
ex = rows(cs, x1=200)
model = rows(cs, x0=200)
check(ex == ["A*", "B", "C"], f"G45 P3 example sample {ex}: 1 marked out of 3")
check(model == ["A*", "B", "C", "D*", "E", "F"], f"G45 P3 model groups {model}: 1 of 3 in each, 2 of 6")
check("Example: 2 marked in the bag" in t45[1] and "Rule’s guess: 6 total" in t45[1].replace("'", "’"),
      "G45 P3 example text: 2 marked, guess 6")
# open circles: bag after marking (left) and second catch (right)
left = [c for c in circles if c.x0 < 300]
right = [c for c in circles if c.x0 > 300]
def dotted(c):
    return any(c.contains(fitz.Point((q.x0 + q.x1) / 2, (q.y0 + q.y1) / 2)) for q in dots if round(q.width, 1) == 3.1)
check(len(left) == 6 and all(dotted(c) for c in left), "G45 P3 'Whole bag after marking': 6 circles, all marked")
check(len(right) == 6 and sum(dotted(c) for c in right) == 2, "G45 P3 'Second catch': 6 circles, 2 marked")
check(all(abs(c.width - c.height) < 0.05 for c in circles), "G45 P3 circles drawn with equal x/y scaling")

log("")
log(f"{len(FAILS)} failures")
(HERE / "check_diagrams.py.out").write_text("\n".join(OUT) + "\n")
print("\n".join(OUT))
sys.exit(1 if FAILS else 0)
