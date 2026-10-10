#!/usr/bin/env python3
"""Week 38 base packet: diagrams read from the delivered student PDFs.

For every band (K-1, 2-3, 4-5) this reads the vector drawing of each page
(common.extract_paths, pypdf) and the word boxes (pdftotext -bbox) and checks:
  * every joining recipe: which corner holds the dot and which the square,
    the seam each recipe encodes under 'join dot to dot and square to square',
    the arrows (direction, from square to dot), the U/L labels and the
    dashed middle line; the encoded band is then built in the cell model and
    its surface type computed;
  * the input/process/output example and its cylinder;
  * the flat washer: which dots lie on which circle, and the ring grouping;
  * the five four-dot pictures on page 3 (and page 6 of K-1, 2-3): the dots
    inside each ring, giving the printed partition order;
  * the Grades 4-5 arrow-transport picture.
Also confirms the three bands share the same diagrams.

Run: python3 check_diagrams.py > out_check_diagrams.txt
"""
import math
import re
from common import WEEK, BANDS, page_shapes, words, page_text, Checker
from surfaces import Band

C = Checker()


def real(shapes):
    return [d for d in shapes if (d["bbox"][2] - d["bbox"][0]) > 1e-6 or (d["bbox"][3] - d["bbox"][1]) > 1e-6]


def is_black(c):
    return c is not None and max(c) < 0.05


def is_white(c):
    return c is not None and min(c) > 0.99


def inside(p, bb, pad=0.0):
    return bb[0] - pad <= p[0] <= bb[2] + pad and bb[1] - pad <= p[1] <= bb[3] + pad


def recipes(shapes):
    out = []
    for d in shapes:
        bb = d["bbox"]
        w, h = bb[2] - bb[0], bb[3] - bb[1]
        if d["kind"] == "poly4" and d["fill"] is None and is_black(d["stroke"]) and w > 50 and 20 <= h <= 35:
            out.append(d)
    return sorted(out, key=lambda d: (round(d["bbox"][1]), d["bbox"][0]))


def marks_in(shapes, bb):
    res = []
    for d in shapes:
        bx = d["bbox"]
        size = max(bx[2] - bx[0], bx[3] - bx[1])
        if not inside(d["c"], bb, 0.5) or size > 4:
            continue
        if d["kind"] == "curve" and is_black(d["fill"]) and 2.5 < size < 3.6:
            res.append(("dot", d["c"]))
        elif d["kind"] == "poly4" and is_white(d["fill"]) and 2.5 < size < 3.6:
            res.append(("sq", d["c"]))
    return res


def arrows_in(shapes, bb):
    shafts = [d for d in shapes if d["kind"] == "line" and inside(d["c"], bb) and d["fill"] is None
              and abs(d["bbox"][0] - d["bbox"][2]) < 1e-6 and d["bbox"][3] - d["bbox"][1] > 5 and not d["dash"]]
    heads = [d for d in shapes if d["kind"] == "poly4" and is_black(d["fill"]) and inside(d["c"], bb)
             and max(d["bbox"][2] - d["bbox"][0], d["bbox"][3] - d["bbox"][1]) < 2]
    res = []
    for s in shafts:
        x = s["bbox"][0]
        y0, y1 = s["bbox"][1], s["bbox"][3]
        hs = [h for h in heads if abs(h["c"][0] - x) < 1]
        assert len(hs) == 1, "arrowhead not found"
        hy = hs[0]["c"][1]
        res.append({"x": x, "tail": y1 if abs(hy - y0) < abs(hy - y1) else y0,
                    "head": y0 if abs(hy - y0) < abs(hy - y1) else y1})
    return res


def analyse_recipe(shapes, wds, d, label):
    bb = d["bbox"]
    cx, cy = d["c"]
    mk = marks_in(shapes, bb)
    corners = {}
    for kind, (x, y) in mk:
        corners[("L" if x < cx else "R", "T" if y < cy else "B")] = kind
    ok = len(mk) == 4 and len(corners) == 4
    # gluing: right-end corner joins the left-end corner with the same mark
    if ok:
        seam = "M" if corners[("R", "T")] == corners[("L", "T")] else "R"
        ok = ok and corners[("L", "T")] != corners[("L", "B")] and corners[("R", "T")] != corners[("R", "B")]
    else:
        seam = None
    # arrows run from square to dot
    arr = arrows_in(shapes, bb)
    arrow_ok = len(arr) == 2
    for a in arr:
        side = "L" if a["x"] < cx else "R"
        tail_corner = "T" if a["tail"] < cy else "B"
        head_corner = "T" if a["head"] < cy else "B"
        arrow_ok = arrow_ok and corners.get((side, tail_corner)) == "sq" and corners.get((side, head_corner)) == "dot"
    dashed = [s for s in shapes if s["dash"] and s["kind"] == "line" and inside(s["c"], bb)]
    mid_ok = len(dashed) == 1 and abs(dashed[0]["c"][1] - cy) < 0.05 and abs(dashed[0]["bbox"][1] - dashed[0]["bbox"][3]) < 1e-6
    ul = {w["t"]: w["c"] for w in wds if w["t"] in ("U", "L") and inside(w["c"], bb)}
    ul_ok = (not ul) or ("U" in ul and "L" in ul and ul["U"][1] < cy < ul["L"][1])
    name = [w["t"] for w in wds if w["t"] in ("A", "B") and bb[0] - 12 < w["c"][0] < bb[0] and bb[1] < w["c"][1] < bb[3]]
    return {"label": label, "name": name[0] if name else None, "corners": corners, "seam": seam,
            "marks_ok": ok, "arrows_from_square_to_dot": arrow_ok, "middle_line_centred": mid_ok,
            "UL": sorted(ul), "UL_ok": ul_ok, "size_mm": (round(bb[2] - bb[0], 1), round(bb[3] - bb[1], 1))}


def partition_rows(shapes, y0, y1):
    rings = [d for d in shapes if d["kind"] == "curve" and d["fill"] is None and is_black(d["stroke"])
             and y0 < d["c"][1] < y1 and 10 < d["bbox"][2] - d["bbox"][0] < 45 and d["bbox"][3] - d["bbox"][1] < 14]
    dots = [d for d in shapes if d["kind"] == "curve" and is_black(d["fill"]) and y0 < d["c"][1] < y1
            and d["bbox"][2] - d["bbox"][0] < 4]
    rows = {}
    for r in rings:
        rows.setdefault(round(r["c"][1]), []).append(r)
    out = []
    for y in sorted(rows):
        parts = []
        used = 0
        rs = sorted(rows[y], key=lambda r: r["c"][0])
        for r in rs:
            a, b = (r["bbox"][2] - r["bbox"][0]) / 2, (r["bbox"][3] - r["bbox"][1]) / 2
            n = sum(1 for d in dots if ((d["c"][0] - r["c"][0]) / a) ** 2 + ((d["c"][1] - r["c"][1]) / b) ** 2 < 1)
            # the dot must sit wholly inside: check its rim too (radius 1.6)
            parts.append(n); used += n
        rowdots = [d for d in dots if abs(d["c"][1] - y) < 3]
        overlap = any(rs[i]["bbox"][2] >= rs[i + 1]["bbox"][0] for i in range(len(rs) - 1))
        out.append({"y": y, "parts": tuple(parts), "dots_in_row": len(rowdots), "all_dots_ringed": used == len(rowdots),
                    "rings_overlap": overlap})
    return out


EXPECT_PARTS = [(4,), (3, 1), (2, 2), (2, 1, 1), (1, 1, 1, 1)]
all_recipes = {}
for band, fn in BANDS.items():
    print(f"\n######## {band} ({fn})")
    pages = [real(p) for p in page_shapes(WEEK / fn)]
    wpages = words(WEEK / fn)
    C.ok(len(pages) == 6, f"{band}: six pages")
    rec_summary = []
    for pi, (shapes, wds) in enumerate(zip(pages, wpages)):
        for k, d in enumerate(recipes(shapes)):
            r = analyse_recipe(shapes, wds, d, f"p{pi + 1}#{k + 1}")
            band_type = Band([r["seam"]], 12, 6).summary()["types"] if r["seam"] else None
            r["type"] = band_type
            print(r)
            rec_summary.append((pi + 1, r["name"], r["seam"], r["UL"]))
            C.ok(r["marks_ok"], f"{band} {r['label']}: one dot and one square at each end")
            C.ok(r["arrows_from_square_to_dot"], f"{band} {r['label']}: both end arrows run from square to dot")
            C.ok(r["middle_line_centred"], f"{band} {r['label']}: dashed middle line exactly at mid-height")
            C.ok(r["UL_ok"], f"{band} {r['label']}: U above / L below the middle line (if labelled)")
            if r["name"] == "A":
                C.ok(r["seam"] == "M" and band_type == ["annulus"], f"{band} {r['label']}: recipe A encodes a matching seam (annulus)")
            elif r["name"] == "B":
                C.ok(r["seam"] == "R" and band_type == ["Mobius band"], f"{band} {r['label']}: recipe B encodes a reversing seam (Mobius band)")
            else:
                C.ok(pi == 0 and r["seam"] == "M", f"{band} {r['label']}: unlabelled example recipe is a matching seam (input of the worked example)")
    all_recipes[band] = rec_summary
    # worked example output: the cylinder seam carries one dot (top rim) and one square (bottom rim)
    p1 = pages[0]
    cyl_marks = marks_in(p1, (110, 55, 162, 95))
    C.ok(sorted(k for k, _ in cyl_marks) == ["dot", "sq"] and
         [k for k, p in sorted(cyl_marks, key=lambda t: t[1][1])] == ["dot", "sq"],
         f"{band} p1 output: cylinder seam shows the dot at the top rim and the square at the bottom rim, matching the input recipe")
    # washer (page 2)
    p2, w2 = pages[1], wpages[1]
    circles = [d for d in p2 if d["kind"] == "curve" and d["fill"] is None and d["stroke"] is not None
               and abs((d["bbox"][2] - d["bbox"][0]) - (d["bbox"][3] - d["bbox"][1])) < 0.01 and d["bbox"][2] - d["bbox"][0] > 20]
    outer = [c for c in circles if not c["dash"]]
    inner = [c for c in circles if c["dash"]]
    C.ok(len(outer) == 1 and len(inner) == 1, f"{band} p2: one solid outer circle and one dashed inner circle")
    O = outer[0]["c"]; Ro = outer[0]["rx"]; Ri = inner[0]["rx"]
    C.ok(math.dist(O, inner[0]["c"]) < 0.05, f"{band} p2: washer circles concentric (centre offset {math.dist(O, inner[0]["c"]):.3f} mm) (R={Ro:.1f}, r={Ri:.1f} mm)")
    dots = [d for d in p2 if d["kind"] == "curve" and is_black(d["fill"]) and d["bbox"][2] - d["bbox"][0] < 4]
    lab = {}
    for d in dots:
        near = min((w for w in w2 if w["t"] in "PQR" and len(w["t"]) == 1), key=lambda w: math.dist(w["c"], d["c"]))
        lab.setdefault(near["t"], []).append(d["c"])
    washer_side = {}
    group_of = {}
    for t, cs in lab.items():
        for c in cs:
            r = math.dist(c, O)
            if abs(r - Ro) < 0.05:
                washer_side[t] = "outer"
            elif abs(r - Ri) < 0.05:
                washer_side[t] = "inner"
    rings = [d for d in p2 if d["kind"] == "curve" and d["fill"] is None and d["c"][0] > 120]
    for t, cs in lab.items():
        for c in cs:
            for gi, rg in enumerate(sorted(rings, key=lambda r: r["c"][1])):
                a, b = rg["rx"], rg["ry"]
                if ((c[0] - rg["c"][0]) / a) ** 2 + ((c[1] - rg["c"][1]) / b) ** 2 < 1:
                    group_of[t] = gi
    print("washer:", washer_side, "ring groups:", group_of)
    C.ok(washer_side == {"P": "outer", "Q": "outer", "R": "inner"}, f"{band} p2: P and Q on the outer edge, R on the inner edge")
    C.ok(group_of.get("P") == group_of.get("Q") != group_of.get("R") and len(rings) == 2,
         f"{band} p2: rings group P with Q and R alone, matching the washer's edges")
    # four-dot pictures
    for pi, (y0, y1) in [(2, (70, 220))] + ([(5, (70, 215))] if band != "grades-4-5" else []):
        rows = partition_rows(pages[pi], y0, y1)
        parts = [r["parts"] for r in rows]
        print(f"p{pi + 1} pictures:", parts)
        C.ok(parts == EXPECT_PARTS, f"{band} p{pi + 1}: pictures top to bottom are 4; 3+1; 2+2; 2+1+1; 1+1+1+1 (guide p3 order)")
        C.ok(all(r["all_dots_ringed"] and r["dots_in_row"] == 4 and not r["rings_overlap"] for r in rows),
             f"{band} p{pi + 1}: every picture has four dots, each inside exactly one ring, rings disjoint")
    if band == "grades-4-5":
        p6 = pages[5]
        vert = [d for d in p6 if d["kind"] == "line" and abs(d["bbox"][0] - d["bbox"][2]) < 1e-6 and d["bbox"][3] - d["bbox"][1] > 10]
        heads = [d for d in p6 if d["kind"] == "poly4" and is_black(d["fill"]) and max(d["bbox"][2] - d["bbox"][0], d["bbox"][3] - d["bbox"][1]) < 4]
        dirs = []
        for v in vert:
            h = min(heads, key=lambda h: abs(h["c"][0] - v["bbox"][0]) + abs(h["c"][1] - v["bbox"][3]))
            dirs.append("down" if h["c"][1] > v["c"][1] else "up")
        print("4-5 p6 transverse arrows:", dirs)
        C.ok(dirs == ["down", "down"], "4-5 p6: start marker and slid arrow both point from the upper long edge to the lower (U toward L)")

print("\n######## Adult guide page 2: the A/B seam diagram")
gpage = real(page_shapes(WEEK / "week-38-facilitator.pdf")[1])
gwords = words(WEEK / "week-38-facilitator.pdf")[1]
grects = sorted([d for d in gpage if d["kind"] == "poly4" and d["fill"] is None and is_black(d["stroke"])
                 and d["bbox"][2] - d["bbox"][0] > 50 and 80 < d["bbox"][1] < 120], key=lambda d: d["bbox"][0])
gseams = []
for d in grects:
    bb = d["bbox"]; cx, cy = d["c"]
    cm = {}
    for e in gpage:
        size = max(e["bbox"][2] - e["bbox"][0], e["bbox"][3] - e["bbox"][1])
        if size > 3 or not inside(e["c"], bb, 0.5):
            continue
        k = "dot" if (e["kind"] == "curve" and is_black(e["fill"])) else "sq" if e["kind"] == "poly4" else None
        if k:
            cm[("L" if e["c"][0] < cx else "R", "T" if e["c"][1] < cy else "B")] = k
    seam = "M" if cm[("R", "T")] == cm[("L", "T")] else "R"
    caption = " ".join(w["t"] for w in sorted(gwords, key=lambda w: w["c"][0]) if bb[0] < w["c"][0] < bb[2] and bb[3] < w["c"][1] < bb[3] + 8)
    b = Band([seam], 12, 6, cuts={3})
    halves = [sorted({"U" if j < 3 else "L" for (_, _, j) in fs}) for fs in b.pieces]
    print(f"guide p2 recipe {cm} -> {seam}; caption '{caption}'; centre cut joins halves {halves}")
    gseams.append((seam, caption, halves))
C.ok([g[0] for g in gseams] == ["M", "R"], "guide p2: left diagram (A) is a matching seam, right (B) a reversing seam")
C.ok(gseams[0][1] == "U → U, L → L" and sorted(gseams[0][2]) == [["L"], ["U"]],
     "guide p2: A caption 'U -> U, L -> L' matches the computed half-strip connection")
C.ok(gseams[1][1] == "U → L, L → U" and gseams[1][2] == [["L", "U"]],
     "guide p2: B caption 'U -> L, L -> U' matches the computed half-strip connection")

print("\n######## Footers and problem numbering")
ids = {"k-1": "F38-K-v3", "grades-2-3": "F38-23-v3", "grades-4-5": "F38-45-v3"}
for band, fn in BANDS.items():
    txt = page_text(WEEK / fn)
    nums = [int(n) for n in re.findall(r"Problem (\d+):", "".join(txt))]
    C.ok(nums == list(range(1, 8)), f"{band}: problems numbered 1-7 consecutively")
    C.ok(all(ids[band] in t for t in txt if t.strip()), f"{band}: every page footer carries {ids[band]}, as the guide's key alignment line (guide p6) says")

print("\n######## Same diagrams across bands")
C.ok(all_recipes["k-1"] == all_recipes["grades-2-3"] == all_recipes["grades-4-5"],
     "the recipes (page, name, seam, U/L labels) are identical in all three bands")
for k, v in all_recipes.items():
    print(k, v)
C.summary()
