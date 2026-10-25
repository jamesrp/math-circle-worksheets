#!/usr/bin/env python3
"""Check the compiled guide against the final student PDFs and the materials file.

- every "Problem N, page M" heading in each band section names the student page
  on which that packet prints "Problem N:";
- every "guide page N" reference points to the page holding the four-stack table;
- the materials file has the page and object names the guide cites.
Run after compiling: python3 check_pdf.py ../facilitator.pdf
"""
import re
import subprocess
import sys

import os
PAGES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
MATERIALS = os.path.join(PAGES, "materials.pdf")
guide = sys.argv[1] if len(sys.argv) > 1 else "../facilitator.pdf"


def pages_text(pdf):
    out = subprocess.run(["pdftotext", "-layout", pdf, "-"], capture_output=True, text=True, check=True).stdout
    return out.split("\f")[:-1] if out.endswith("\f") else out.split("\f")


ok = True
G = pages_text(guide)
print("guide pages:", len(G))

# where each packet prints each problem
where = {}
for band, fn in [("K-1", "k-1.pdf"), ("2-3", "grades-2-3.pdf"), ("4-5", "grades-4-5.pdf")]:
    where[band] = {}
    for i, t in enumerate(pages_text(f"{PAGES}/{fn}"), 1):
        for m in re.finditer(r"Problem (\d+):", t):
            where[band][int(m.group(1))] = i

# split the guide text into band sections by their headings
full = "\n".join(G)
heads = [("K-1", "K–1: sorting with tokens"), ("2-3", "Grades 2–3: fewest flips"),
         ("4-5", "Grades 4–5: bounds, breaks"), (None, "Sources and evidence")]
pos = [full.index(h) for _, h in heads]
for (band, _), a, b in zip(heads, pos, pos[1:]):
    sec = full[a:b]
    cited = {int(n): int(p) for n, p in re.findall(r"Problem (\d+), page (\d+)", sec)}
    if cited != where[band]:
        ok = False
        print("MISMATCH", band, cited, where[band])
    else:
        print(f"{band}: problems {sorted(cited)} on the pages cited: ok")

# "guide page N" must be the page with the table
table_page = [i for i, t in enumerate(G, 1) if "All 24 stacks of four" in t]
refs = {int(n) for n in re.findall(r"guide\s+page\s+(\d+)", full)}
print("table on guide page", table_page, "; references", sorted(refs))
if len(table_page) != 1 or refs != {table_page[0]}:
    ok = False
    print("MISMATCH in guide page references")

# the materials file: one page, the title and objects the guide cites
M = pages_text(MATERIALS)
mt = M[0]
need = ["Pancakes and spatula", "spatula", "100 mm"] + [str(k) for k in range(1, 7)]
if len(M) != 1 or not all(x in mt for x in need):
    ok = False
    print("MISMATCH with materials file")
else:
    print("materials: 1 page, 'Pancakes and spatula', pancakes 1-6, spatula, 100 mm bar: ok")
for cite in ["materials page 1", "Pancakes and spatula"]:
    if cite not in full.replace("\n", " "):
        ok = False
        print("guide does not cite", cite)

print("PDF CHECKS PASSED" if ok else "PDF CHECKS FAILED")
sys.exit(0 if ok else 1)
