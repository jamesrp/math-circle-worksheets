"""Check that the editable sources match the delivered PDFs.

Base packets: every \\draw rectangle, dashed middle line, tick and motif scope in
src/*.tex is printed at the same place (TikZ coordinates are cm from the page's
top-left corner plus the (1.5, 1.5) shift, y downwards).
Bonus packet: the words and their order in student/build.py match the print.
Also compares the delivered PDFs with the source reference copies byte for byte.
"""
import hashlib
import json
import re
from common import HERE, SRC, BONUS_SRC, WEEK, PT_PER_CM, Tee

out = Tee(HERE / "out_compare_source.txt")
D = json.loads((HERE / "extracted.json").read_text())
bad = 0


def md5(p):
    return hashlib.md5(p.read_bytes()).hexdigest()


pairs = [("week-35-k-1.pdf", SRC / "reference-pdfs/k-1.pdf"),
         ("week-35-grades-2-3.pdf", SRC / "reference-pdfs/grades-2-3.pdf"),
         ("week-35-grades-4-5.pdf", SRC / "reference-pdfs/grades-4-5.pdf"),
         ("week-35-facilitator.pdf", SRC / "reference-pdfs/facilitator-guide.pdf"),
         ("week-35-bonus.pdf", BONUS_SRC / "reference-pdfs/week-35-bonus.pdf"),
         ("week-35-bonus-facilitator.pdf", BONUS_SRC / "reference-pdfs/week-35-bonus-facilitator.pdf")]
for a, b in pairs:
    same = md5(WEEK / a) == md5(b)
    out(f"  {a} identical to source reference copy: {same}")
    bad += not same

for band, tex in (("k-1", "k-1.tex"), ("2-3", "grades-2-3.tex"), ("4-5", "grades-4-5.tex")):
    text = (SRC / "src" / tex).read_text()
    pages = text.split("\\newpage")
    for i, src in enumerate(pages):
        pg = D[band][i]
        yshift = 0.0
        m = re.search(r"\\begin\{scope\}\[shift=\{\(0,(-?[\d.]+)\)\}\]", src)
        if m:
            yshift = float(m.group(1))
        rects = re.findall(r"\\draw\[gray!50,line width=\.6pt\] \(([\d.]+),([\d.]+)\) rectangle \(([\d.]+),([\d.]+)\)", src)
        for x0, y0, x1, y1 in rects:
            want = [(float(v) + 1.5) * PT_PER_CM for v in (x0, y0, x1, y1)]
            ok = any(all(abs(a - b) < 0.05 for a, b in zip(want, (r["x0"], r["y0"], r["x1"], r["y1"]))) for r in pg["rects"])
            bad += not ok
            if not ok:
                out(f"  {band} p{i+1}: rectangle {x0},{y0} not found in print")
        ticks = re.findall(r"\\draw\[gray!45\] \(([\d.]+),([\d.]+)\)", src)
        for x, y in ticks:
            ok = any(abs(l["x0"] - (float(x) + 1.5) * PT_PER_CM) < 0.05 and abs(l["y0"] - (float(y) + 1.5) * PT_PER_CM) < 0.05
                     for l in pg["lines"])
            bad += not ok
        motifs = re.findall(r"shift=\{\(([\d.]+),([\d.]+)\)\},rotate=0,xscale=([-\d.]+),yscale=([-\d.]+)", src)
        polys = sorted([c for c in pg["curves"] if len(c["pts"]) == 13], key=lambda c: c["pts"][0][0])
        for (x, y, xs, ys), c in zip(sorted(motifs, key=lambda t: float(t[0])), polys):
            cx = (float(x) + 1.5) * PT_PER_CM
            cy = (float(y) + yshift + 1.5) * PT_PER_CM
            px = [p[0] for p in c["pts"]]; py = [p[1] for p in c["pts"]]
            ok = abs((min(px) + max(px)) / 2 - cx) < 0.05 and abs((min(py) + max(py)) / 2 - cy) < 0.05
            # first vertex (-1.3,-1.1) scaled; y-down TikZ, so yscale sign shows the flip
            fx = cx + float(xs) * -1.3 * PT_PER_CM
            fy = cy + float(ys) * -1.1 * PT_PER_CM
            ok = ok and abs(c["pts"][0][0] - fx) < 0.05 and abs(c["pts"][0][1] - fy) < 0.05
            bad += not ok
            out(f"  {band} p{i+1}: motif scope at ({x},{y}) yscale {ys}: printed at that place and orientation: {ok}")
        out(f"  {band} p{i+1}: {len(rects)} boxes, {len(ticks)} ticks checked")

# bonus words
build = (BONUS_SRC / "student" / "build.py").read_text()
for word in ("RBB", "RRB", "RRBRRB", "RBBBRB", "RBBBBRRB", "RRBBRB"):
    assert f"'{word}'" in build
rows = re.findall(r"\(\d+,'([RB]+)',(\d)\)", build)
out(f"  bonus P2 source rows and slides: {rows}")
printed = []
pg = D["bonus"][1]
for y in sorted({w["top"] for w in pg["words"] if w["text"] in "RB" and w["top"] > 300}):
    printed.append("".join(w["text"] for w in sorted(pg["words"], key=lambda w: w["x0"]) if w["top"] == y and w["text"] in ("R", "B")))
slides = [w2["text"] for w1, w2 in zip(pg["words"], pg["words"][1:]) if w1["text"] == "slide" and w2["text"].isdigit()]
out(f"  bonus P2 printed rows {printed}, slide labels {slides}")
ok = [r[0] for r in rows] == printed and [r[1] for r in rows] == slides
bad += not ok
out(f"  bonus P2 source = print: {ok}")
out(f"\nmismatches: {bad}")
out.save()
