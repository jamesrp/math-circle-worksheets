#!/usr/bin/env python3
"""Check that the editable .tex sources draw exactly the glyphs found in the delivered PDFs.

Parses every tile/icon \\draw in source/week-36/editable/src/{k-1,grades-2-3,grades-4-5}.tex
(TikZ: x = 1 cm, y = -1 cm, origin page north-west shifted by (1.5, 1.5) cm), converts to PDF
points and matches each one to a glyph from extracted.json by shape, fill and centre (0.1 pt).
Also lists the problem statements in the sources next to the PDF text.
Run: python3 compare_source.py > out_compare_source.txt
"""
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import HERE, SRC, PRINT, ok, finish  # noqa: E402

CM = 72 / 2.54
D = json.loads((HERE / "extracted.json").read_text())
NUM = r"(-?[0-9.]+)"
PAIRS = {"k-1.tex": "week-36-k-1.pdf", "grades-2-3.tex": "week-36-grades-2-3.pdf", "grades-4-5.tex": "week-36-grades-4-5.pdf"}


def fill_of(opts):
    if "pattern=" in opts:
        return "striped"
    if "fill=black" in opts:
        return "solid"
    if "fill=white" in opts:
        return "open"
    return None


def pt(x, y):
    return ((x + 1.5) * CM, (y + 1.5) * CM)


def parse(tex):
    pages, cur = [], []
    for line in tex.splitlines():
        if line.startswith("\\newpage"):
            pages.append(cur)
            cur = []
        m = re.match(r"\\draw\[([^\]]*)\]\s*(.*);?$", line.strip())
        if not m or "gray" in m.group(1):
            continue
        opts, body = m.group(1), m.group(2)
        f = fill_of(opts)
        if f is None:
            continue
        c = re.match(r"\(%s,%s\) circle \(%s\)" % (NUM, NUM, NUM), body)
        r = re.match(r"\(%s,%s\) rectangle \(%s,%s\)" % (NUM, NUM, NUM, NUM), body)
        t = re.match(r"\(%s,%s\) -- \(%s,%s\) -- \(%s,%s\) -- cycle" % ((NUM,) * 6), body)
        if c:
            x, y, _ = map(float, c.groups())
            cur.append(("circle", f, pt(x, y)))
        elif r:
            x0, y0, x1, y1 = map(float, r.groups())
            cur.append(("square", f, pt((x0 + x1) / 2, (y0 + y1) / 2)))
        elif t:
            v = list(map(float, t.groups()))
            xs, ys = v[0::2], v[1::2]
            cur.append(("triangle", f, pt((min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2)))
    pages.append(cur)
    return pages


def pdf_glyphs(pdf):
    out = []
    for pg in D[pdf]:
        g = []
        for b in pg["boards"]:
            for row in b["cells"]:
                g += row
        for grp in pg["groups"]:
            g += grp
        out.append(g)
    return out


for texname, pdf in PAIRS.items():
    tex = (SRC / texname).read_text()
    src_pages = parse(tex)
    got = pdf_glyphs(pdf)
    ok(len(src_pages) == len(got), "%s: %d pages in source, %d in PDF" % (texname, len(src_pages), len(got)))
    for pno, (sp, gp) in enumerate(zip(src_pages, got), 1):
        unmatched = list(gp)
        missing = []
        for shape, fill, (x, y) in sp:
            hit = [t for t in unmatched if t["shape"] == shape and t["fill"] == fill
                   and abs(t["cx"] - x) < 0.1 and abs(t["cy"] - y) < 0.1]
            if hit:
                unmatched.remove(hit[0])
            else:
                missing.append((shape, fill, round(x, 1), round(y, 1)))
        ok(not missing and not unmatched, "%s p%d: %d source glyphs = %d PDF glyphs (same shape, fill, centre)" % (
            texname, pno, len(sp), len(gp)) + ("" if not missing else " missing %s" % missing)
           + ("" if not unmatched else " extra %s" % [(t["shape"], t["fill"], t["cx"], t["cy"]) for t in unmatched]))
    # problem statements
    stmts = re.findall(r"\\textbf\{Problem (\d+):\} ([^}]*)\}", tex)
    text = subprocess.run(["pdftotext", str(PRINT / pdf), "-"], capture_output=True, text=True).stdout
    flat = " ".join(text.split())
    for n, s in stmts:
        s2 = " ".join(s.replace("--", "–").split())
        ok(s2 in flat, "%s Problem %s statement in source appears verbatim in the PDF" % (texname, n))
finish()
