#!/usr/bin/env python3
"""Diagram checks for Week 88, read from the delivered PDFs with PyMuPDF.

- Every student page: header, footer, consecutive problem numbers 1-11.
- Circles (paths made of four Bezier arcs): printed diameter in mm, equal
  width and height, the label printed inside or beside them, and whether the
  page calls the figure a sketch.  Actual-size circles must measure 40 mm.
- Trays: interior measured between the inner edges of the four border strips.
- The radius bridge on p. 5: radii, tangency and the joined segment.
- Room around the two actual-size 40 mm middle disks (pp. 1 and 5) for a
  six-disk ring, whose outer edge is 60 mm from the middle centre.
- Guide: re-reads the sentences quoted in math.md with pdftotext.

Run: python3 check_diagrams.py   (writes check_diagrams.py.out beside itself)
"""
import math
import re
import subprocess
from pathlib import Path

import pymupdf

HERE = Path(__file__).resolve().parent


def find_repo(start):
    # Committed copy: plans/review/checks/week-88/ -> four folders up.
    cand = start.parents[3] if len(start.parents) > 3 else start
    if (cand / "lowell-math-circle-year-2").is_dir():
        return cand
    for p in [start, *start.parents]:
        if (p / "lowell-math-circle-year-2").is_dir():
            return p
    raise SystemExit("repository not found")


REPO = find_repo(HERE)
WEEK = REPO / "lowell-math-circle-year-2" / "week-88"
STU = WEEK / "week-88-students.pdf"
FAC = WEEK / "week-88-facilitator.pdf"
MM = 25.4 / 72
OUT, FAILS = [], []


def log(s=""):
    OUT.append(s)


def check(cond, msg):
    log(("PASS  " if cond else "FAIL  ") + msg)
    if not cond:
        FAILS.append(msg)


FINDINGS = []


def note(msg):
    log("NOTE  " + msg)


def finding(msg):
    """A located problem reported in math.md (not a failure of this script)."""
    log("FIND  " + msg)
    FINDINGS.append(msg)


doc = pymupdf.open(STU)
check(doc.page_count == 8, f"student PDF has {doc.page_count} pages (8 expected)")
for i, page in enumerate(doc):
    check(abs(page.rect.width - 612) < 0.01 and abs(page.rect.height - 792) < 0.01, f"p.{i+1}: US Letter page")

# ---------------------------------------------------------------- text frame
nums = []
for i, page in enumerate(doc):
    t = page.get_text()
    check("Week 88 / Packing and kissing circles / Grades K–5" in t, f"p.{i+1}: header")
    check("Bellingham Math Circle / Week 88 / W88-shared-v1" in t, f"p.{i+1}: footer")
    nums += [int(n) for n in re.findall(r"Problem (\d+):", t)]
check(nums == list(range(1, 12)), f"problem numbers in order: {nums}")


# ---------------------------------------------------------------- circles
def circles(page):
    out = []
    for d in page.get_drawings():
        kinds = [it[0] for it in d["items"]]
        if kinds.count("c") >= 4 and set(kinds) <= {"c"}:
            r = d["rect"]
            w, h = r.width * MM, r.height * MM
            if w > 3:
                out.append(dict(cx=(r.x0 + r.x1) / 2 * MM, cy=(r.y0 + r.y1) / 2 * MM, w=w, h=h,
                                filled=d.get("fill") is not None))
    return out


def words(page):
    return [(w[4], (w[0] + w[2]) / 2 * MM, (w[1] + w[3]) / 2 * MM, w[1] * MM, w[3] * MM) for w in page.get_text("words")]


def label_near(page, c, maxd=None):
    """Text 'NN mm' whose centre is nearest the circle centre."""
    ws = words(page)
    best = None
    for k in range(len(ws) - 1):
        if re.fullmatch(r"\d+", ws[k][0]) and ws[k + 1][0] == "mm":
            x = (ws[k][1] + ws[k + 1][1]) / 2
            y = ws[k][2]
            dist = math.hypot(x - c["cx"], y - c["cy"])
            if best is None or dist < best[0]:
                best = (dist, int(ws[k][0]))
    if best and (maxd is None or best[0] <= maxd):
        return best[1]
    return None


def text_lines(page):
    return [(b[1] * MM, b[3] * MM, b[4]) for b in page.get_text("blocks")]


log("")
log("== Circles ==")
for i, page in enumerate(doc):
    for c in circles(page):
        check(abs(c["w"] - c["h"]) < 0.01, f"p.{i+1}: circle at ({c['cx']:.1f},{c['cy']:.1f}) mm is round: {c['w']:.3f} x {c['h']:.3f} mm")

# p.1 and p.5 actual-size middles
for pno, label in ((1, "Problem 1"), (5, "Problem 6")):
    page = doc[pno - 1]
    cs = [c for c in circles(page) if c["filled"]]
    mid = cs[-1]
    check(abs(mid["w"] - 40) < 0.01, f"p.{pno} {label}: unlabelled middle disk is printed actual size, {mid['w']:.3f} mm across")
    above = [y1 for y0, y1, t in text_lines(page) if y1 < mid["cy"] and "Week 88" not in t]
    below = [y0 for y0, y1, t in text_lines(page) if y0 > mid["cy"]]
    room_up = mid["cy"] - max(above)
    room_dn = min(below) - mid["cy"]
    log(f"      p.{pno} {label}: from the middle centre, {room_up:.1f} mm clear up to the text above and "
        f"{room_dn:.1f} mm down to the next text; a six-ring reaches 60 mm (54.6 mm if two disks straddle the top)")
    if pno == 1:
        check(room_up >= 60 and room_dn >= 60, "p.1: a six-ring in any rotation stays clear of the text")
    else:
        if room_up < 60:
            finding(f"p.5 Problem 6: a six-ring with one disk straight above the middle covers the problem text by {60 - room_up:.1f} mm; "
                 f"only rotations with two disks straddling the top clear it (by {room_up - (20 * math.sqrt(3) + 20):.1f} mm)")
    halfw = min(mid["cx"] - 18, 197.9 - mid["cx"])
    check(halfw >= 60, f"p.{pno}: {halfw:.1f} mm of text width either side of the middle centre")

# p.3, p.4, p.8 sketches: diameter ratio and labels
log("")
for pno in (3, 4, 8):
    page = doc[pno - 1]
    t = page.get_text()
    for c in circles(page):
        lab = label_near(page, c, maxd=c["w"] / 2 + 12)
        scale = (c["w"] / lab) if lab else None
        log(f"      p.{pno}: circle at y={c['cy']:.1f} mm printed {c['w']:.1f} mm across, label {lab} mm"
            + (f", scale {scale:.2f}" if scale else ""))
    log(f"      p.{pno}: 'not actual size' captions at y = "
        + ", ".join(f"{y0:.1f}" for y0, y1, tt in text_lines(page) if "not actual size" in tt))

# p.3 specifically: does every half-scale figure carry a caption below it before the next problem/answer?
page = doc[2]
cs = sorted(circles(page), key=lambda c: c["cy"])
caps = [y0 for y0, y1, tt in text_lines(page) if "not actual size" in tt]
p3 = [c for c in cs if c["cy"] < 100]
p4 = [c for c in cs if c["cy"] > 100]
check(all(abs(label_near(page, c, 30) / c["w"] - 2) < 0.01 for c in p3) and any(max(c["cy"] for c in p3) < y < 110 for y in caps),
      "p.3 Problem 3: labels are twice the printed diameters and a 'Sketches, not actual size' caption follows the figure")
p4_caption = any(y > max(c["cy"] for c in p4) for y in caps)
p4_desc = ", ".join(f"'{label_near(page, c, 30)} mm' printed {c['w']:.0f} mm across" for c in p4)
if p4_caption:
    check(True, "p.3 Problem 4: figure carries a 'not actual size' caption")
else:
    finding("p.3 Problem 4: half-scale figure (" + p4_desc + ") has no 'not actual size' caption; "
            "the only caption on the page sits under Problem 3's figure, above Problem 3's answer line")

# p.4, p.8 ratios
for pno in (4, 8):
    page = doc[pno - 1]
    ds = sorted({round(c["w"], 2) for c in circles(page) if c["filled"]})
    check(len(ds) == 2 and abs(ds[1] / ds[0] - 2) < 1e-3, f"p.{pno}: 80 mm and 40 mm middles drawn in ratio 2 ({ds})")
    mids = text_lines(page)
    check(any("not actual size" in tt for _, _, tt in mids), f"p.{pno}: page says the sketches are not actual size")

# ---------------------------------------------------------------- trays
log("")
log("== Trays ==")
for pno, H in ((2, 112), (6, 110), (7, 108)):
    page = doc[pno - 1]
    strips = []
    for d in page.get_drawings():
        if d.get("fill") is not None and [it[0] for it in d["items"]] == ["l", "l", "l", "l"] or \
           (d.get("fill") is not None and d["items"] and d["items"][0][0] == "re"):
            r = d["rect"]
            strips.append((r.x0 * MM, r.y0 * MM, r.x1 * MM, r.y1 * MM))
    horiz = sorted([s for s in strips if s[2] - s[0] > 100], key=lambda s: s[1])
    vert = sorted([s for s in strips if s[3] - s[1] > 100], key=lambda s: s[0])
    top_inner, bot_inner = horiz[0][3], horiz[1][1]
    left_inner, right_inner = vert[0][2], vert[1][0]
    W, Hm = right_inner - left_inner, bot_inner - top_inner
    check(abs(W - 160) < 0.01 and abs(Hm - H) < 0.01, f"p.{pno}: tray interior {W:.3f} x {Hm:.3f} mm (label 160 x {H})")
    check(f"160 mm × {H} mm interior" in page.get_text(), f"p.{pno}: caption states 160 mm × {H} mm interior")

# ---------------------------------------------------------------- bridge p.5
log("")
log("== Radius bridge, p.5 ==")
page = doc[4]
cs = sorted([c for c in circles(page) if not c["filled"]], key=lambda c: c["cx"])
pairs = [cs[k:k + 2] for k in range(0, 6, 2)]
for a, b in pairs:
    ra, rb = a["w"] / 2, b["w"] / 2
    dc = math.hypot(a["cx"] - b["cx"], a["cy"] - b["cy"])
    check(abs(ra - 7.5) < 0.01 and abs(rb - 12.5) < 0.01 and abs(dc - (ra + rb)) < 0.01,
          f"pair at x={a['cx']:.1f}: radii {ra:.2f}, {rb:.2f} mm, centres {dc:.2f} mm apart (tangent; half of 15, 25, 40)")
segs = [d["rect"] for d in page.get_drawings() if [it[0] for it in d["items"]] == ["l"] and abs(d["rect"].width * MM - 20) < 0.01]
for s in segs:
    x0 = s.x0 * MM
    match = [a for a, b in pairs if abs(a["cx"] - x0) < 0.01 and abs(b["cx"] - s.x1 * MM) < 0.01]
    check(bool(match), f"segment from x={x0:.2f} to {s.x1 * MM:.2f} mm joins the two centres")
check("15 + 25 = 40 mm" in page.get_text() and "Sketches, not actual size" in page.get_text(), "bridge text: 15 + 25 = 40 mm, labelled as sketches")

# ---------------------------------------------------------------- guide text
log("")
log("== Guide sentences quoted in math.md ==")
gtxt = subprocess.run(["pdftotext", str(FAC), "-"], capture_output=True, text=True).stdout
gflat = re.sub(r"\s+", " ", gtxt)
for q in ["Changing the central disk can change which size consumes the most room.",
          "this guide proves an eleven-disk construction, not that eleven is the unrestricted maximum",
          "No claim is made here about arbitrary 11-disk packings in 108 mm",
          "seven small ones at angles 50,90,130,170,210,250,290 degrees",
          "one large at 0 and four small at 80,140,200,260 degrees"]:
    check(q in gflat, f"guide contains: \"{q}\"")
stxt = re.sub(r"\s+", " ", doc[7].get_text())
check("For each one, can you explain why a ring with more outside disks is impossible?" in stxt,
      "student p.8 contains the Problem 10 sentence quoted in math.md")

log("")
log(f"{len(FAILS)} failure(s); {len(FINDINGS)} located diagram finding(s) reported in math.md")
(HERE / "check_diagrams.py.out").write_text("\n".join(OUT) + "\n")
print("\n".join(OUT))
raise SystemExit(1 if FAILS else 0)
