#!/usr/bin/env python3
"""Build the compact Week 2 start-to-target catalog, preserving target scale.

Reuses the shared collection's graph data and vector drawing routine. Catalog
problems 1-10 correspond to original problems 2, 5-10, and 11-13; diagram lookup
keys retain the original numbers. The opening rule is unnumbered guidance.
"""
from pathlib import Path
import importlib.util

from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph

SOURCE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("shared_explore", SOURCE / "build-shared-explore.py")
shared = importlib.util.module_from_spec(spec)
spec.loader.exec_module(shared)

ROOT = shared.ROOT
OUT = ROOT / "lowell-math-circle-year-2/week-02/week-02-shared-catalog.pdf"
W, H, M = shared.W, shared.H, shared.M
WIDTH = W - 2 * M
INSTANCES = {item["problem"]: item for item in shared.DATA["checks"]}

# Exact bounding boxes passed to the original target drawing routine. Reusing
# them preserves node size, line weight, spacing, orientation, and physical scale.
TARGET_BOXES = {
    2: (WIDTH / 3 - 16, 116),
    5: (WIDTH / 2 - 16, 99),
    6: (WIDTH / 2 - 16, 99),
    7: (WIDTH / 3 - 16, 94),
    8: (226, 80),
    9: (WIDTH / 4 - 16, 118),
    10: (WIDTH / 4 - 16, 120),
    11: (300, 124),
}


def picture_size(name, box):
    """Ink extent of shared.Book.graph, excluding its surrounding whitespace."""
    width, height = box
    radius = 20 if width > 250 else 8
    points = shared.DATA["graphs"][name]["xy"]
    dx = max(p[0] for p in points) - min(p[0] for p in points)
    dy = max(p[1] for p in points) - min(p[1] for p in points)
    scale = min((width - 2 * (radius + 4)) / dx,
                (height - 2 * (radius + 4)) / dy)
    return dx * scale + 2 * radius, dy * scale + 2 * radius


class Catalog(shared.Book):
    def __init__(self):
        OUT.parent.mkdir(parents=True, exist_ok=True)
        self.c = canvas.Canvas(str(OUT), pagesize=(W, H))
        self.c.setTitle("Week 2 / Lamp lab / Puzzle catalog")
        self.c.setAuthor("Bellingham Math Circle")
        self.page = 0
        self.pair_count = 0
        self.bottoms = []

    def start(self):
        if self.page:
            self.c.showPage()
        self.page += 1
        c = self.c
        c.setFillGray(.1)
        c.setFont("AuxB", 10.3)
        c.drawString(M, H - 39, "Week 2 / Lamp lab / Shared collection")
        c.setLineWidth(.6)
        c.setStrokeGray(.55)
        c.line(M, 44, W - M, 44)
        c.setFont("Aux", 8.5)
        c.setFillGray(.2)
        c.drawString(M, 29, "Bellingham Math Circle / Week 2 / F02-S-CAT-v2")
        c.drawRightString(W - M, 29, str(self.page))
        return 65

    def problem(self, num, text, top):
        return self.paragraph(f"<b>Problem {num}:</b> {text}", top)

    def paragraph(self, text, top):
        style = ParagraphStyle("task", fontName="Aux", fontSize=13.5,
                               leading=18, textColor="#171717")
        paragraph = Paragraph(text, style)
        _, height = paragraph.wrap(WIDTH, H)
        assert top + height <= 728, (self.page, text, top + height)
        paragraph.drawOn(self.c, M, H - top - height)
        return top + height

    def picture(self, name, center_x, center_top, box, on):
        width, height = box
        self.graph(name, (center_x - width / 2, center_top - height / 2,
                          width, height), on, labels=False)

    def arrow(self, x1, t1, x2, t2):
        c = self.c
        c.setStrokeGray(.22)
        c.setLineWidth(1.2)
        c.line(x1, H - t1, x2, H - t2)
        if t1 == t2:
            c.line(x2 - 5, H - t2 + 3, x2, H - t2)
            c.line(x2 - 5, H - t2 - 3, x2, H - t2)
        else:
            c.line(x2 - 3, H - t2 + 5, x2, H - t2)
            c.line(x2 + 3, H - t2 + 5, x2, H - t2)

    def pairs(self, num, top, columns=2, vertical=False):
        item = INSTANCES[num] if num != 6 else {
            "graph": "ring6", "start": [1], "targets": [[1]]}
        name = item["graph"]
        box = TARGET_BOXES[num]
        pw, ph = picture_size(name, box)
        gap = 34
        gutter = 24
        slot = (WIDTH - gutter * (columns - 1)) / columns
        row_height = 2 * ph + gap if vertical else ph
        assert vertical or 2 * pw + gap <= slot
        for index, target in enumerate(item["targets"]):
            row, col = divmod(index, columns)
            cy = top + row * (row_height + 14) + ph / 2
            cx = M + col * (slot + gutter) + slot / 2
            if vertical:
                self.picture(name, cx, cy, box, item["start"])
                self.picture(name, cx, cy + ph + gap, box, target)
                self.arrow(cx, cy + ph / 2 + 7,
                           cx, cy + ph / 2 + gap - 7)
            else:
                offset = (pw + gap) / 2
                self.picture(name, cx - offset, cy, box, item["start"])
                self.picture(name, cx + offset, cy, box, target)
                self.arrow(cx - gap / 2 + 6, cy, cx + gap / 2 - 6, cy)
            self.pair_count += 1
        rows = (len(item["targets"]) + columns - 1) // columns
        bottom = top + rows * row_height + (rows - 1) * 14
        assert bottom <= 728, (self.page, num, bottom)
        return bottom

    def save(self):
        assert self.page == 4
        assert self.pair_count == 19
        self.c.save()


def main():
    shared.fonts()
    book = Catalog()
    top = book.start()
    top = book.paragraph("Empty is OFF. A dot is ON. Choose a line. Change BOTH "
                         "lamps at its ends: add a dot or erase a dot. Each arrow "
                         "points from the start to the target.", top)
    top = book.problem(1, "Make each target picture.", top + 16)
    top = book.pairs(2, top + 12)
    top = book.problem(2, "Make each target picture.", top + 22)
    top = book.pairs(5, top + 12)
    top = book.problem(3, "Visit every lamp and bring the light home.", top + 22)
    top = book.pairs(6, top + 12)
    book.bottoms.append(round(top, 2))

    top = book.start()
    top = book.problem(4, "Make each target picture.", top)
    top = book.pairs(7, top + 12, columns=1)
    top = book.problem(5, "Make each target picture.", top + 22)
    top = book.pairs(8, top + 12, columns=1)
    book.bottoms.append(round(top, 2))

    top = book.start()
    top = book.problem(6, "Make each target picture.", top)
    top = book.pairs(9, top + 12)
    top = book.problem(7, "Make each target picture.", top + 24)
    top = book.pairs(10, top + 12)
    book.bottoms.append(round(top, 2))

    top = book.start()
    top = book.problem(8, "Can you make the target picture?", top)
    top = book.pairs(11, top + 12, columns=1, vertical=True)
    top = book.problem(9, "Draw ONE new line between lamps on different islands. "
                        "Try the trip with your bridge.", top + 18)
    top = book.problem(10, "Make some puzzles for your partner.", top + 24)
    book.bottoms.append(round(top, 2))
    book.save()
    print(f"Built {OUT}: {book.page} pages, {book.pair_count} start-to-target pairs")
    print(f"Content bottoms (points from top): {book.bottoms}")


if __name__ == "__main__":
    main()
