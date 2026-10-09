"""Read the coloured cube rows printed in the adult guide (small coloured squares) directly from the PDF.

Prints, per page, each run of small coloured squares as a colour word list, with the nearest text to its left.
Repository root is found four folders up from this file (plans/review/checks/week-03/).
"""
import sys
from pathlib import Path

import pymupdf

HERE = Path(__file__).resolve().parent
REPO = next(up for up in HERE.parents if (up / "lowell-math-circle-year-2").is_dir())
PDF = REPO / "lowell-math-circle-year-2/week-03/week-03-facilitator.pdf"

COL = {
    "green": (0x3F, 0xAE, 0x4A), "blue": (0x2F, 0x6F, 0xD6), "red": (0xD8, 0x34, 0x3C), "yellow": (0xF5, 0xC5, 0x18),
    "purple": (0x7D, 0x46, 0xA8), "pink": (0xF0, 0x7A, 0xB4), "teal": (0x1E, 0xA5, 0x9B), "gray": (0x8C, 0x90, 0x99),
}


def colour_name(fill):
    if fill is None:
        return None
    rgb = tuple(round(255 * c) for c in fill)
    best = min(COL, key=lambda k: sum((a - b) ** 2 for a, b in zip(COL[k], rgb)))
    if sum((a - b) ** 2 for a, b in zip(COL[best], rgb)) < 300:
        return best
    return None


def rows_by_page():
    """{page: [(y, x, label, [colours])]} for every run of two or more small coloured squares."""
    out = {}
    doc = pymupdf.open(PDF)
    for pno, page in enumerate(doc, 1):
        sq = []
        for d in page.get_drawings():
            name = colour_name(d.get("fill"))
            r = d["rect"]
            if name and r.width < 14 and r.height < 14:
                sq.append((round(r.y0, 0), r.x0, r.x1, name))
        words = page.get_text("words")
        rows = {}
        for y, x0, x1, n in sorted(sq):
            rows.setdefault(y, []).append((x0, x1, n))
        for y, items in sorted(rows.items()):
            items.sort()
            groups, cur = [], [items[0]]
            for a, b in zip(items, items[1:]):
                if b[0] - a[1] > 4:
                    groups.append(cur)
                    cur = []
                cur.append(b)
            groups.append(cur)
            for g in groups:
                if len(g) < 2:
                    continue
                left = [w for w in words if abs((w[1] + w[3]) / 2 - (y + 5)) < 8 and w[2] <= g[0][0] + 1]
                lab = max(left, key=lambda w: w[2])[4] if left else "?"
                out.setdefault(pno, []).append((y, g[0][0], lab, [n for _, _, n in g]))
    return out


def main():
    doc = pymupdf.open(PDF)
    for pno, page in enumerate(doc, 1):
        sq = []
        for d in page.get_drawings():
            name = colour_name(d.get("fill"))
            r = d["rect"]
            if name and r.width < 14 and r.height < 14:
                sq.append((round(r.y0, 0), r.x0, r.x1, name))
        if not sq:
            continue
        words = page.get_text("words")
        sq.sort()
        rows = {}
        for y, x0, x1, n in sq:
            rows.setdefault(y, []).append((x0, x1, n))
        print(f"--- page {pno}")
        for y, items in sorted(rows.items()):
            items.sort()
            groups, cur = [], [items[0]]
            for a, b in zip(items, items[1:]):
                if b[0] - a[1] > 4:
                    groups.append(cur)
                    cur = []
                cur.append(b)
            groups.append(cur)
            for g in groups:
                left = [w for w in words if abs((w[1] + w[3]) / 2 - (y + 5)) < 8 and w[2] <= g[0][0] + 1]
                lab = max(left, key=lambda w: w[2])[4] if left else "?"
                print(f"  y={y:.0f} x={g[0][0]:.0f} [{lab}] " + " ".join(n for _, _, n in g))


if __name__ == "__main__":
    main()
