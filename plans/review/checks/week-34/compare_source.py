#!/usr/bin/env python3
"""Week 34 math check: confirm the editable sources describe the rings in the
delivered PDFs (extracted.json from extract.py).

Base packets: every `\\draw[line width=1pt,fill=white] (x,y) circle (r);` in
source/week-34/editable/src/<band>.tex (TikZ cm, y downward, shifted 1.5 cm)
must be a spot printed at the same place with the same size.
Bonus: the \\ring macro calls give the same ring sizes and starting words.
Run: python3 compare_source.py > out_compare_source.txt
"""
import json
import math
import re

from common import HERE, SRC, BONUS_SRC

PDF = json.loads((HERE / "extracted.json").read_text())
FAIL = []


def ok(cond, msg):
    print(("  ok   " if cond else "  FAIL ") + msg)
    if not cond:
        FAIL.append(msg)


spot_re = re.compile(r"\\draw\[line width=1pt,fill=white\] \(([\d.]+),([\d.]+)\) circle \(([\d.]+)\)")
for band in ["k-1", "grades-2-3", "grades-4-5"]:
    tex = (SRC / "editable" / "src" / f"{band}.tex").read_text()
    pages = tex.split("\\newpage")
    pdf_pages = PDF[f"week-34-{band}.pdf"]
    ok(len(pages) == len(pdf_pages), f"{band}: {len(pages)} source pages, {len(pdf_pages)} PDF pages")
    for i, (src_page, pdf_page) in enumerate(zip(pages, pdf_pages), start=1):
        src = [(10 * (float(x) + 1.5), 10 * (float(y) + 1.5), 20 * float(r)) for x, y, r in spot_re.findall(src_page)]
        pdf = [(x, y, r["spot_diam_mm"][0]) for r in pdf_page["rings"] for x, y in r["spot_centres_mm"]]
        unmatched = [s for s in src if not any(math.dist(s[:2], p[:2]) < 0.05 and abs(s[2] - p[2]) < 0.05 for p in pdf)]
        ok(len(src) == len(pdf) and not unmatched,
           f"{band} p{i}: {len(src)} source spots = {len(pdf)} printed spots, same centres and diameters (0.05 mm)")

tex = (BONUS_SRC / "student-src" / "bonus.tex").read_text()
body = tex.split("\\begin{document}")[1]
calls = re.findall(r"\\ring\{(\d+)\}\{([\d.]+)\}\{([\d.]+)\}\{([^}]*)\}", body)
src_rings = [(int(n), float(R) * 10, float(r) * 20, f) for n, R, r, f in calls]
pdf_rings = [(r["n"], r["ring_radius_mm"], r["spot_diam_mm"][0], r["contents_cw_from_top"])
             for pg in PDF["week-34-bonus.pdf"] for r in pg["rings"]
             if r["outline"] == "grey" and not (r["n"] == 4)]
ok(len(src_rings) == len(pdf_rings), f"bonus: {len(src_rings)} \\ring calls, {len(pdf_rings)} printed grey-outline rings (layer figure excluded)")
# compare as multisets (the extractor orders rings by position, the source by call order)
src_keys = sorted((n, round(R, 1), round(r, 1), "".join(f.split(","))) for n, R, r, f in src_rings)
pdf_keys = sorted((n, round(R, 1), round(r, 1), "".join(c)) for n, R, r, c in pdf_rings)
for s, p in zip(src_keys, pdf_keys):
    ok(s == p, f"bonus ring n={s[0]} R={s[1]}mm spot={s[2]}mm contents {s[3]} matches print {p}")
print("\nSUMMARY:", "all checks passed" if not FAIL else f"{len(FAIL)} FAIL: {FAIL}")
