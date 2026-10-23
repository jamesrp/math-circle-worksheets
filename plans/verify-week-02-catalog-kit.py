#!/usr/bin/env python3
"""Check the compact Week 2 catalog's boards, counters and adult guide.

Mathematics, from plans/week-02-catalog-kit-data.json and the shared graph data:
replays every answer in the guide press by press; checks the walking-light
answers keep one lamp ON; checks the parity theorem the guide states (a target
is reachable exactly when every island has an even number of changed lamps) on
every board, including the islands with each of the 16 bridges, over all
states; checks Problem 8's impossibility, Problem 9's 16 bridges, Problem 5's
uniqueness, the Problem 3 counterexample without the one-light rule, and the
Problem 10 counterexamples to "reversing always succeeds".

PDFs: reads week-02-shared-catalog-boards.pdf and
week-02-shared-catalog-facilitator.pdf (or the paths given as arguments) and
checks lamp diameter, board shapes against the graph data with equal x and y
scaling, regular square and hexagon, the edges drawn, the counter grid and its
straight cuts, the 10 cm scale line, headers, footers and print counts, and
that the guide prints each checked answer. Confirms the approved catalog PDF is
unchanged. Writes plans/week-02-catalog-kit-checks.json.
"""
from itertools import combinations, product
from pathlib import Path
import hashlib
import json
import math
import re
import sys

import pymupdf

ROOT = Path(__file__).resolve().parents[1]
W02 = ROOT / "lowell-math-circle-year-2/week-02"
BOARDS = Path(sys.argv[1]) if len(sys.argv) > 1 else W02 / "week-02-shared-catalog-boards.pdf"
GUIDE = Path(sys.argv[2]) if len(sys.argv) > 2 else W02 / "week-02-shared-catalog-facilitator.pdf"
SHARED = json.loads((ROOT / "plans/week-02-shared-data.json").read_text())
KIT = json.loads((ROOT / "plans/week-02-catalog-kit-data.json").read_text())
GRAPHS = SHARED["graphs"]
CATALOG_SHA = "c76eb5ffc07ab06515db3c92fc46e083bed814dd50738a8037f1c12e9754c2f0"   # F02-S-CAT-v2, approved
MM = 72 / 25.4
results = []


def ok(name, cond, detail=""):
    results.append({"check": name, "pass": bool(cond), "detail": str(detail)})
    if not cond:
        print("FAIL", name, detail)


# ---------------------------------------------------------------- mathematics
def press(state, line):
    a, b = line
    return state ^ {a, b}


def replay(start, presses):
    s = set(start)
    trail = [frozenset(s)]
    for line in presses:
        s = press(s, line)
        trail.append(frozenset(s))
    return s, trail


def islands(n, edges):
    parent = list(range(n + 1))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for a, b in edges:
        parent[find(a)] = find(b)
    groups = {}
    for v in range(1, n + 1):
        groups.setdefault(find(v), set()).add(v)
    return list(groups.values())


def reachable_changes(n, edges):
    """All change sets reachable from any start: closure of the presses (BFS over 2^n)."""
    seen = {frozenset()}
    todo = [frozenset()]
    while todo:
        s = todo.pop()
        for e in edges:
            t = frozenset(set(s) ^ set(e))
            if t not in seen:
                seen.add(t)
                todo.append(t)
    return seen


def theorem_holds(n, edges):
    reach = reachable_changes(n, edges)
    parts = islands(n, edges)
    for bits in product((0, 1), repeat=n):
        change = frozenset(v for v in range(1, n + 1) if bits[v - 1])
        even = all(len(change & part) % 2 == 0 for part in parts)
        if even != (change in reach):
            return False
    return True


def solutions(n, edges, start, target):
    need = set(start) ^ set(target)
    out = []
    for choice in product((0, 1), repeat=len(edges)):
        s = set()
        for used, e in zip(choice, edges):
            if used:
                s ^= set(e)
        if s == need:
            out.append(choice)
    return out


orig = {c["problem"]: c for c in SHARED["checks"]}
for p in KIT["problems"]:
    n_cat = p["catalog"]
    if p.get("invented"):
        continue
    g = GRAPHS[p["graph"]]
    edges = [tuple(e) for e in g["edges"]]
    n = len(g["xy"])
    if p["original"] in orig:
        o = orig[p["original"]]
        ok(f"P{n_cat}: start and targets match the catalog data (original problem {p['original']})",
           o["graph"] == p["graph"] and o["start"] == p["start"]
           and [a["target"] for a in p["answers"]] == o["targets"], (o, p["start"]))
    else:
        ok(f"P{n_cat}: the tour starts and ends at lamp 1 on the six-ring (drawn by the catalog builder)",
           p["graph"] == "ring6" and p["start"] == [1] and p["answers"][0]["target"] == [1])
    for a in p["answers"]:
        if p.get("impossible"):
            sols = solutions(n, edges, p["start"], a["target"])
            ok(f"P{n_cat}: {p['start']} -> {a['target']} is impossible (no set of lines works)", not sols, len(sols))
            parts = islands(n, edges)
            odd = [sorted(part) for part in parts if len((set(p["start"]) ^ set(a["target"])) & part) % 2]
            ok(f"P{n_cat}: the obstruction is an island with an odd number of changed lamps", bool(odd), odd)
            continue
        use = edges + ([tuple(a["bridge"])] if "bridge" in a else [])
        ok(f"P{n_cat}: every press is a line of the board", all(tuple(l) in use or tuple(l[::-1]) in use
                                                             for l in a["presses"]), a["presses"])
        end, trail = replay(p["start"], a["presses"])
        ok(f"P{n_cat}: {p['start']} -> {a['target']} by {a['presses']}", end == set(a["target"]), sorted(end))
        if p.get("one_light"):
            ok(f"P{n_cat}: one lamp ON after every press", all(len(t) == 1 for t in trail), [sorted(t) for t in trail])
        if p.get("visit_all"):
            ok(f"P{n_cat}: the light visits every lamp", set().union(*trail) == set(range(1, n + 1)))
        if p.get("unique"):
            ok(f"P{n_cat}: exactly one set of lines works on the tree",
               len(solutions(n, edges, p["start"], a["target"])) == 1)
    if "without_one_light_rule" in p:
        end, trail = replay(p["start"], p["without_one_light_rule"]["presses"])
        ok(f"P{n_cat}: without the one-light rule, lighting and undoing visits every lamp and returns home",
           end == {1} and set().union(*trail) == set(range(1, 7)) and max(len(t) for t in trail) > 1,
           [sorted(t) for t in trail])
    if p.get("any_bridge"):
        left = islands(n, edges)[0]
        right = set(range(1, n + 1)) - left
        good = 0
        for a_ in sorted(left):
            for b_ in sorted(right):
                if solutions(n, edges + [(a_, b_)], p["start"], p["answers"][0]["target"]):
                    good += 1
        ok(f"P{n_cat}: every one of the 16 bridges makes the trip possible", good == 16 == len(left) * len(right), good)

# the theorem the guide states, on every board and every bridged islands board
for name, g in GRAPHS.items():
    edges = [tuple(e) for e in g["edges"]]
    ok(f"theorem holds on the {name} board, all {2 ** len(g['xy'])} change sets", theorem_holds(len(g["xy"]), edges))
isl = GRAPHS["islands8"]
bridged = all(theorem_holds(8, [tuple(e) for e in isl["edges"]] + [(a, b)]) for a in range(1, 5) for b in range(5, 9))
ok("theorem holds on the islands with each of the 16 bridges", bridged)
p10 = next(p for p in KIT["problems"] if p.get("invented"))
for cx in p10["counterexamples"]:
    g = GRAPHS[cx["graph"]]
    sols = solutions(len(g["xy"]), [tuple(e) for e in g["edges"]], cx["start"], cx["target"])
    ok(f"P10: a drawn puzzle can be impossible: {cx['graph']} {cx['start']} -> {cx['target']}", not sols)
ok("P10: the islands counterexample changes an even number of lamps in all", len(p10["counterexamples"][1]["target"]) % 2 == 0)
# a puzzle made by presses is undone by the same presses, on any board
for name, g in GRAPHS.items():
    edges = [tuple(e) for e in g["edges"]]
    for k in range(1, 4):
        for seq in combinations(edges, k):
            mid, _ = replay([], seq)
            back, _ = replay(mid, seq[::-1])
            if back:
                ok(f"reversal undoes a made puzzle on {name}", False, seq)
ok("reversal undoes every puzzle made by up to three distinct presses, all boards", True)

# ----------------------------------------------------------------------- PDFs
catalog = W02 / "week-02-shared-catalog.pdf"
ok("approved catalog PDF unchanged (F02-S-CAT-v2)", hashlib.sha256(catalog.read_bytes()).hexdigest() == CATALOG_SHA)

doc = pymupdf.open(BOARDS)
spec = KIT["boards"]
ok("boards: four pages", len(doc) == 4, len(doc))
sets = spec["sets"]
want = f"K–1 {sets['K-1']} · Grades 2–3 {sets['Grades 2-3']} · Grades 4–5 {sets['Grades 4-5']} · adults {sets['adults']}"
for i, page in enumerate(doc, 1):
    text = " ".join(page.get_text().split())
    ok(f"boards p{i}: US Letter", (round(page.rect.width), round(page.rect.height)) == (612, 792))
    ok(f"boards p{i}: header", text.startswith("Week 2 / Lamp lab / Boards and counters"), text[:40])
    ok(f"boards p{i}: footer", "Bellingham Math Circle / Week 2 / F02-S-CAT-BRD-v1 / physically unrehearsed" in text)
    ok(f"boards p{i}: print counts per table", want in text, want)
    segs = [(it[1], it[2]) for d in page.get_drawings() for it in d["items"] if it[0] == "l"]
    scale = [s for s in segs if abs(s[0].y - s[1].y) < .01 and abs(abs(s[1].x - s[0].x) - 100 * MM) < .05]
    ok(f"boards p{i}: 10 cm scale line", len(scale) == 1 and "10 cm check" in text)
    if i <= 3:
        ok(f"boards p{i}: copy paper", "Print on copy paper, at 100%" in text)
        lamps = [d["rect"] for d in page.get_drawings() if d["items"] and d["items"][0][0] == "c"]
        ok(f"boards p{i}: every lamp 22 mm across", all(abs(r.width / MM - 22) < .05 and abs(r.height / MM - 22) < .05
                                                       for r in lamps), sorted({round(r.width / MM, 2) for r in lamps}))
        centres = [((r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2) for r in lamps]
        labels = sorted((w[1], w) for w in page.get_text("words") if w[4] == "workspace:")
        ok(f"boards p{i}: each board labelled extra workspace", len(labels) == len(spec["pages"][i - 1]), len(labels))
        ys = [lab[0] for lab in labels] + [715]      # the scale line sits at y = 730
        for k, b in enumerate(spec["pages"][i - 1]):
            g = GRAPHS[b["graph"]]
            mine = [c for c in centres if ys[k] < c[1] < ys[k + 1]]
            u = b["spacing_mm"] * MM
            ok(f"boards p{i} {b['graph']}: {len(g['xy'])} lamps", len(mine) == len(g["xy"]), len(mine))
            if len(mine) != len(g["xy"]):
                continue
            # equal x and y scaling: the data, scaled by u in both axes (y down), must match after one translation
            data = [(x * u, -y * u) for x, y in g["xy"]]
            dx = min(c[0] for c in mine) - min(p[0] for p in data)
            dy = min(c[1] for c in mine) - min(p[1] for p in data)
            placed = [(x + dx, y + dy) for x, y in data]
            match = [min(range(len(mine)), key=lambda j: math.dist(q, mine[j])) for q in placed]
            err = max(math.dist(q, mine[j]) for q, j in zip(placed, match))
            ok(f"boards p{i} {b['graph']}: lamps where the data put them, {b['spacing_mm']} mm per unit in x and y",
               err < .05 and len(set(match)) == len(match), round(err, 4))
            drawn = 0
            for a, c in g["edges"]:
                pa, pc = placed[a - 1], placed[c - 1]
                drawn += any((math.dist((s[0].x, s[0].y), pa) < .05 and math.dist((s[1].x, s[1].y), pc) < .05)
                             or (math.dist((s[0].x, s[0].y), pc) < .05 and math.dist((s[1].x, s[1].y), pa) < .05)
                             for s in segs)
            board_segs = [s for s in segs if ys[k] < s[0].y < ys[k + 1] and ys[k] < s[1].y < ys[k + 1]]
            ok(f"boards p{i} {b['graph']}: exactly the graph's {len(g['edges'])} lines",
               drawn == len(g["edges"]) == len(board_segs), (drawn, len(board_segs)))
            if b["graph"] == "square":
                sides = [math.dist(placed[a - 1], placed[c - 1]) for a, c in g["edges"]]
                diag = [math.dist(placed[0], placed[2]), math.dist(placed[1], placed[3])]
                ok("square board is a square", max(sides) - min(sides) < .01 and abs(diag[0] - diag[1]) < .01)
            if b["graph"] == "ring6":
                sides = [math.dist(placed[a - 1], placed[c - 1]) for a, c in g["edges"]]
                cxy = (sum(p[0] for p in placed) / 6, sum(p[1] for p in placed) / 6)
                radii = [math.dist(p, cxy) for p in placed]
                ok("six-ring board is a regular hexagon (sides and radii within 0.1 mm)",
                   (max(sides) - min(sides)) / MM < .1 and (max(radii) - min(radii)) / MM < .1,
                   (round((max(sides) - min(sides)) / MM, 3), round((max(radii) - min(radii)) / MM, 3)))
            gaps = [math.dist(placed[a - 1], placed[c - 1]) / MM - 22 for a, c in g["edges"]]
            ok(f"boards p{i} {b['graph']}: at least 12 mm of line shows between neighbouring lamps", min(gaps) >= 12,
               round(min(gaps), 1))
            ok(f"boards p{i} {b['graph']}: inside the page margins",
               all(14 * MM - 1 < x < 612 - 14 * MM + 1 for x, _ in mine))
# counters
page = doc[3]
text = " ".join(page.get_text().split())
ok("counters on card stock", "Print on card stock, at 100%" in text)
segs = [(it[1], it[2]) for d in page.get_drawings() for it in d["items"] if it[0] == "l"]
side = spec["counter_side_mm"] * MM
grid = [s for s in segs if abs(abs(s[1].x - s[0].x) - 100 * MM) > .05 and s[0].y > 60 and s[0].y < 720]
hor = sorted({round(s[0].y, 2) for s in grid if abs(s[0].y - s[1].y) < .01})
ver = sorted({round(s[0].x, 2) for s in grid if abs(s[0].x - s[1].x) < .01})
ok("counters: 11 straight vertical and 8 horizontal cut lines, each across the whole grid",
   len(ver) == 11 and len(hor) == 8
   and all(abs(abs(s[1].x - s[0].x) - 10 * side) < .05 for s in grid if abs(s[0].y - s[1].y) < .01)
   and all(abs(abs(s[1].y - s[0].y) - 7 * side) < .05 for s in grid if abs(s[0].x - s[1].x) < .01), (len(ver), len(hor)))
ok("counters: 18 mm squares", all(abs((b - a) / MM - 18) < .02 for a, b in zip(ver, ver[1:]))
   and all(abs((b - a) / MM - 18) < .02 for a, b in zip(hor, hor[1:])))
dots = [d["rect"] for d in page.get_drawings() if d["items"] and d["items"][0][0] == "c"]
ok("counters: 70 dots of 10 mm, one centred in each square", len(dots) == 70
   and all(abs(r.width / MM - 10) < .05 for r in dots)
   and len({(int(((r.x0 + r.x1) / 2 - ver[0]) // side), int(((r.y0 + r.y1) / 2 - hor[0]) // side)) for r in dots}) == 70)
nsets = sum(sets.values())
per = spec["counters_per_set"]
ok("counters: enough for the biggest board in every set, with spares",
   per >= max(len(g["xy"]) for g in GRAPHS.values()) and nsets * per <= 70, (nsets, per))
ok("counters heading gives sets and spares", f"Cut it into {nsets} sets of {per} counters" in text
   and f"{70 - nsets * per} are spare" in text)

# guide
g = pymupdf.open(GUIDE)
gtext = " ".join(" ".join(p.get_text() for p in g).split())
ok("guide: three pages", len(g) == 3, len(g))
for i, p in enumerate(g, 1):
    t = " ".join(p.get_text().split())
    ok(f"guide p{i}: header and footer", t.startswith("Week 2 / Lamp lab / Adult guide to the compact catalog")
       and "Bellingham Math Circle / Week 2 / F02-S-CAT-FAC-v1 / unpiloted" in t)
first = " ".join(g[0].get_text().split())
ok("guide opens with the mathematical overview and theorem", first.index("Mathematical overview") < first.index("Theorem.")
   < first.index("Materials and preparation"))
for phrase in ["even number of lamps that differ between start and target", "Press:", "Press again:", "One target:",
               "Keep exactly one lamp ON after every press", "reversing the moves always succeeds",
               "week-02-shared-catalog-boards.pdf", "18 sheets", "six sets of 11"]:
    ok(f"guide says: {phrase}", phrase in gtext)
for p in KIT["problems"]:
    for a in p.get("answers", []):
        if a.get("presses"):
            s = "{" + ", ".join(map(str, a["target"])) + "}: " + ", ".join(f"{x}-{y}" for x, y in a["presses"])
            if p["catalog"] == 9:
                s = "With bridge 2-5: 1-2, 2-5"
            ok(f"guide prints the checked answer for P{p['catalog']}: {s}", s in gtext)
board_sheets = sum(sets.values()) * 3
ok("guide's sheet total matches the boards' print counts", f"{board_sheets} sheets" in gtext, board_sheets)

fails = [r for r in results if not r["pass"]]
out = ROOT / "plans/week-02-catalog-kit-checks.json"
out.write_text(json.dumps({"boards": BOARDS.name, "guide": GUIDE.name, "checks": len(results), "failures": len(fails),
                           "results": results}, indent=1, ensure_ascii=False) + "\n")
print(f"{len(results)} checks, {len(fails)} failures")
sys.exit(1 if fails else 0)
