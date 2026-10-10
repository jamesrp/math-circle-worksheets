"""Cross-check: the edge numbers and card numbers in the LaTeX sources (source/week-05/src/*.tex)
are the ones the final PDFs print (pdf_data.json from extract_pdf.py).

Run after extract_pdf.py:  python3 -I source_vs_pdf.py > source_vs_pdf.out
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import REPO  # noqa: E402

SRC = REPO / "lowell-math-circle-year-2" / "source" / "week-05" / "src"
DATA = json.loads((Path(__file__).resolve().parent / "pdf_data.json").read_text())

scope_re = re.compile(r"\\begin\{scope\}(.*?)\\end\{scope\}", re.S)
frame_re = re.compile(r"\\draw\[line width=1\.6pt\] \(0,0\) rectangle \(([\d.]+),([\d.]+)\);")
inner_re = re.compile(r"\\draw\[line width=0\.7pt\] \(([\d.]+),0\) -- ")
node_re = re.compile(r"\\node at \((-?[\d.]+),(-?[\d.]+)\) \{\\Large (\d)\};")


def tex_items(path):
    """Edge-number dicts for every printed puzzle grid and number pairs for every card, in source order."""
    text = path.read_text()
    bodies = scope_re.findall(text)
    # puzzles drawn without a scope (single grid in a tikzpicture)
    for pic in re.findall(r"\\begin\{tikzpicture\}(.*?)\\end\{tikzpicture\}", text, re.S):
        if "\\begin{scope}" not in pic:
            bodies.append(pic)
    grids, cards = [], []
    for body in bodies:
        f = frame_re.search(body)
        nodes = [(float(x), float(y), int(d)) for x, y, d in node_re.findall(body)]
        if f:
            S = float(f.group(1))
            n = len(set(inner_re.findall(body))) + 1
            cell = S / n
            cl = {}
            for x, y, d in nodes:
                if y > S:
                    cl[f"T{int(x // cell) + 1}"] = d
                elif y < 0:
                    cl[f"B{int(x // cell) + 1}"] = d
                elif x < 0:
                    cl[f"L{n - int(y // cell)}"] = d
                elif x > S:
                    cl[f"R{n - int(y // cell)}"] = d
            if cl:
                grids.append(cl)
        elif len(nodes) == 2:
            cards.append((sorted(nodes)[0][2], sorted(nodes)[1][2]))
    return grids, cards


def pdf_items(band, pages):
    grids, cards = [], []
    for p in pages:
        info = DATA["student"][band][str(p)]
        grids += [g["clues"] for g in info["grids"] if g["clues"]]
    return grids


bad = 0
for band, tex, pages in (("M", "grades-2-3.tex", (3, 4, 5)), ("U", "grades-4-5.tex", (3, 4, 5))):
    tg, tc = tex_items(SRC / tex)
    pg = pdf_items(band, pages)
    same = sorted(map(lambda d: sorted(d.items()), tg)) == sorted(map(lambda d: sorted(d.items()), pg))
    print(f"{tex}: {len(tg)} puzzle grids with printed numbers in source, {len(pg)} in PDF; same edge numbers: {same}")
    bad += not same
    if band == "U":
        pc = [tuple(c) for c in DATA["student"]["U"]["1"]["cards"][1:]]
        print(f"  cards source {tc}\n  cards PDF    {pc}; same: {tc == pc}")
        bad += tc != pc
tg, tc = tex_items(SRC / "k-1.tex")
pc = [tuple(c) for p in (3, 6, 7) for c in DATA["student"]["K"][str(p)]["cards"]]  # p.6: the eight 2-2 frames
print(f"k-1.tex cards source {tc}\n        cards PDF    {pc}; same: {tc == pc}")
bad += tc != pc
print("\nDIFFERENCES:", bad)
