#!/usr/bin/env python3
"""Build the separate six-investigation upper catalog (ReportLab, US Letter).

Mathematical data and facilitator notes live in plans/week-02-catalog-upper*.
Run plans/verify-week-02-catalog-upper.py for independent exhaustive checks.
"""
import json
import math
from pathlib import Path

from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph

ROOT = Path(__file__).resolve().parents[3]
DATA = json.loads((ROOT / "plans/week-02-catalog-upper-data.json").read_text())
OUT = ROOT / "lowell-math-circle-year-2/week-02/week-02-shared-catalog-upper.pdf"
W, H, M = 612, 792, 44


def fonts():
    for directory, regular, bold in [
        ("/System/Library/Fonts/Supplemental", "Arial.ttf", "Arial Bold.ttf"),
        ("/usr/share/fonts/truetype/dejavu", "DejaVuSans.ttf", "DejaVuSans-Bold.ttf"),
    ]:
        base = Path(directory)
        if (base / regular).exists():
            pdfmetrics.registerFont(TTFont("Catalog", str(base / regular)))
            pdfmetrics.registerFont(TTFont("CatalogB", str(base / bold)))
            pdfmetrics.registerFontFamily("Catalog", normal="Catalog", bold="CatalogB")
            return
    raise RuntimeError("Arial or DejaVu Sans required")


def graph_data(name):
    graph = DATA["graphs"][name]
    if "cycle" in graph:
        n = graph["cycle"]
        return (
            [(math.sin(2 * math.pi * i / n), math.cos(2 * math.pi * i / n))
             for i in range(n)],
            [(i + 1, (i + 1) % n + 1) for i in range(n)],
        )
    return graph["xy"], graph["edges"]


class Catalog:
    def __init__(self):
        self.c = canvas.Canvas(str(OUT), pagesize=(W, H), invariant=1)
        self.c.setTitle("Week 2 / Lamp lab / Upper puzzle catalog")
        self.c.setAuthor("Bellingham Math Circle")
        self.page = 0
        self.pairs = 0

    def start(self, problem):
        if self.page:
            self.c.showPage()
        self.page += 1
        c = self.c
        c.setFillGray(.1)
        c.setFont("CatalogB", 10.3)
        c.drawString(M, H - 39, "Week 2 / Lamp lab / Shared collection")
        c.setLineWidth(.6)
        c.setStrokeGray(.55)
        c.line(M, 44, W - M, 44)
        c.setFont("Catalog", 8.5)
        c.setFillGray(.2)
        c.drawString(M, 29, "Bellingham Math Circle / Week 2 / F02-S-CAT-UP-v1")
        c.drawRightString(W - M, 29, str(self.page))
        key = f"problem-{problem['number']}"
        c.bookmarkPage(key)
        c.addOutlineEntry(f"Problem {problem['number']}", key)
        style = ParagraphStyle("task", fontName="Catalog", fontSize=13.5,
                               leading=18, textColor="#171717")
        p = Paragraph(f"<b>Problem {problem['number']}:</b> {problem['prompt']}", style)
        _, height = p.wrap(W - 2 * M, H)
        p.drawOn(c, M, H - 65 - height)
        return 65 + height

    def graph(self, name, cx, top, width, height, on=(), radius=8):
        xy, edges = graph_data(name)
        xs, ys = zip(*xy)
        dx, dy = max(xs) - min(xs), max(ys) - min(ys)
        scale = min((width - 2 * (radius + 2)) / dx if dx else float("inf"),
                    (height - 2 * (radius + 2)) / dy if dy else float("inf"))
        points = [(cx + (x - (min(xs) + max(xs)) / 2) * scale,
                   H - top - height / 2 + (y - (min(ys) + max(ys)) / 2) * scale)
                  for x, y in xy]
        # Reject graphs whose distinct lamps would touch or overlap.
        assert all(math.dist(a, b) >= 2 * radius + 3
                   for i, a in enumerate(points) for b in points[i + 1:]), name
        c = self.c
        c.setStrokeGray(.18)
        c.setLineWidth(1.25)
        for a, b in edges:
            c.line(*points[a - 1], *points[b - 1])
        for i, (x, y) in enumerate(points, 1):
            c.setFillGray(1)
            c.circle(x, y, radius, fill=1, stroke=1)
            if i in on:
                c.setFillGray(.1)
                c.circle(x, y, 3.3, fill=1, stroke=0)

    def arrow(self, cx, top):
        c = self.c
        y = H - top
        c.setLineWidth(1.2)
        c.setStrokeGray(.22)
        c.line(cx - 10, y, cx + 10, y)
        c.line(cx + 5, y + 3, cx + 10, y)
        c.line(cx + 5, y - 3, cx + 10, y)

    def pair(self, case, left, top, width, height, label):
        c = self.c
        c.setFont("Catalog", 10)
        c.setFillGray(.2)
        c.drawString(left, H - top - 10, label)
        gap = 34
        inset = 10
        picture_width = (width - 2 * inset - gap) / 2
        cy = top + 13
        cx = left + width / 2
        offset = (picture_width + gap) / 2
        for x, state in [(cx - offset, case["start"]), (cx + offset, case["target"])]:
            self.graph(case["graph"], x, cy, picture_width, height, state)
        self.arrow(cx, cy + height / 2)
        assert cy + height < 731
        self.pairs += 1

    def build_page(self, problem):
        prompt_bottom = self.start(problem)
        layout = problem["layout"]
        if layout in ("six", "four"):
            rows = 3 if layout == "six" else 2
            top = max(prompt_bottom + 20, 150 if rows == 3 else 145)
            step = (708 - top) / rows
            slot = (W - 2 * M - 20) / 2
            for i, case in enumerate(problem["cases"]):
                row, col = divmod(i, 2)
                self.pair(case, M + col * (slot + 20), top + row * step,
                          slot, 115 if rows == 3 else 140, chr(65 + i))
        elif layout in ("networks", "trees"):
            top = max(prompt_bottom + 14, 124)
            rows = len(problem["cases"])
            step = (729 - top) / rows
            for i, case in enumerate(problem["cases"]):
                self.pair(case, M, top + i * step, W - 2 * M,
                          step - 24, chr(65 + i))
        elif layout == "invent":
            for i, n in enumerate(problem["rings"]):
                row, col = divmod(i, 2)
                self.graph(f"ring{n}", 171 + col * 270, 164 + row * 270,
                           180, 180, radius=9)
        else:
            raise ValueError(layout)


def main():
    fonts()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    book = Catalog()
    for problem in DATA["problems"]:
        book.build_page(problem)
    assert book.page == 6 and book.pairs == 26
    book.c.save()
    print(f"Built {OUT}: {book.page} pages, {book.pairs} start-to-target pairs")


if __name__ == "__main__":
    main()
