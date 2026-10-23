#!/usr/bin/env python3
"""Build the blank working boards and counters for the compact Week 2 catalog.

One board per graph of week-02-shared-catalog.pdf (square, six-ring, tree,
3 x 3 grid, islands), drawn in the catalog's orientation with 22 mm lamps, and
a card-stock sheet of 18 mm counters with a dot on the printed side (dot up is
ON). The catalog's small pictures then serve as start and target cards. Board
layout and counts are in plans/week-02-catalog-kit-data.json; the graphs come
from plans/week-02-shared-data.json. plans/verify-week-02-catalog-kit.py
checks the finished PDF. US Letter, print at 100%.
"""
from pathlib import Path
import importlib.util
import json
import sys

from reportlab import rl_config
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph

rl_config.invariant = 1
SOURCE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("shared_explore", SOURCE / "build-shared-explore.py")
shared = importlib.util.module_from_spec(spec)
spec.loader.exec_module(shared)

ROOT = shared.ROOT
GRAPHS = shared.DATA["graphs"]
KIT = json.loads((ROOT / "plans/week-02-catalog-kit-data.json").read_text())["boards"]
OUT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else ROOT / "lowell-math-circle-year-2/week-02/week-02-shared-catalog-boards.pdf"
W, H = 612, 792
LEFT = 40
MM = 72 / 25.4
ID = "F02-S-CAT-BRD-v1"
LAMP_R = KIT["lamp_diameter_mm"] / 2 * MM
SETS = KIT["sets"]
TABLES = [("K–1", SETS["K-1"]), ("Grades 2–3", SETS["Grades 2-3"]),
          ("Grades 4–5", SETS["Grades 4-5"]), ("adults", SETS["adults"])]


class Sheets:
    def __init__(self):
        OUT.parent.mkdir(parents=True, exist_ok=True)
        self.c = canvas.Canvas(str(OUT), pagesize=(W, H), pageCompression=1)
        self.c.setTitle("Week 2 / Lamp lab / Boards and counters")
        self.c.setAuthor("Bellingham Math Circle")
        self.page = 0
        self.body = ParagraphStyle("body", fontName="Aux", fontSize=9.8, leading=12.8, textColor="#1a1a1a")

    def start(self, title, print_line, how):
        if self.page:
            self.c.showPage()
        self.page += 1
        c = self.c
        c.setFillGray(.1)
        c.setFont("AuxB", 10.3)
        c.drawString(LEFT, H - 34, "Week 2 / Lamp lab / Boards and counters")
        c.setStrokeGray(.55)
        c.setLineWidth(.6)
        c.line(LEFT, H - 41, W - LEFT, H - 41)
        c.line(LEFT, 40, W - LEFT, 40)
        c.setFont("Aux", 8.5)
        c.setFillGray(.2)
        c.drawString(LEFT, 27, f"Bellingham Math Circle / Week 2 / {ID} / physically unrehearsed")
        c.drawRightString(W - LEFT, 27, str(self.page))
        c.setFillGray(0)
        c.setFont("AuxB", 13)
        c.drawString(LEFT, H - 61, title)
        top = self.para(print_line, H - 68)
        top = self.para(how, top - 2)
        self.scale()
        return top

    def para(self, text, top):
        p = Paragraph(text, self.body)
        _, h = p.wrap(W - 2 * LEFT, H)
        p.drawOn(self.c, LEFT, top - h)
        return top - h

    def scale(self):
        c = self.c
        x, y = LEFT, 62
        c.setStrokeGray(0)
        c.setLineWidth(1)
        c.line(x, y, x + 100 * MM, y)
        c.line(x, y - 4, x, y + 4)
        c.line(x + 100 * MM, y - 4, x + 100 * MM, y + 4)
        c.setFont("Aux", 8)
        c.drawString(x + 100 * MM + 8, y - 3, "10 cm check: this line must measure 10 cm")

    def board(self, name, unit_mm, label, top):
        """Draw one board below `top` (PDF y); return the y of its bottom edge."""
        c = self.c
        g = GRAPHS[name]
        xs = [p[0] for p in g["xy"]]
        ys = [p[1] for p in g["xy"]]
        u = unit_mm * MM
        height = (max(ys) - min(ys)) * u + 2 * LAMP_R
        c.setFont("AuxB", 10.5)
        c.setFillGray(.15)
        c.drawString(LEFT, top - 12, label)
        cy_top = top - 24 - LAMP_R                # centre height of the top row of lamps
        cx = W / 2 - (min(xs) + max(xs)) / 2 * u
        pts = [(cx + a * u, cy_top - (max(ys) - b) * u) for a, b in g["xy"]]
        c.setStrokeGray(.15)
        c.setLineWidth(2.2)
        for a, b in g["edges"]:
            c.line(*pts[a - 1], *pts[b - 1])
        c.setLineWidth(1.5)
        for x, y in pts:
            c.setFillGray(1)
            c.circle(x, y, LAMP_R, fill=1, stroke=1)
        return top - 24 - height

    def save(self):
        self.c.save()


def counts():
    return " · ".join(f"{t} {n}" for t, n in TABLES)


def build():
    shared.fonts()
    s = Sheets()
    sets = sum(n for _, n in TABLES)
    for k, boards in enumerate(KIT["pages"], 1):
        names = ", ".join(b["label"].split(": ")[1].split(" (")[0] for b in boards)
        top = s.start(f"Board sheet {k} of 3: {names}",
                      f"<b>Print on copy paper, at 100%:</b> {counts()}. One sheet per pair and one for the launch; "
                      "pages 1–3 make one set of boards.",
                      "A counter on every lamp: dot up is ON, blank up is OFF. Set the counters to a start picture. "
                      "One child points to a line; the partner flips the counters at both of its ends.")
        free = top - 74                       # room down to the scale line
        heights = []
        for b in boards:
            g = GRAPHS[b["graph"]]
            ys = [p[1] for p in g["xy"]]
            heights.append(24 + (max(ys) - min(ys)) * b["spacing_mm"] * MM + 2 * LAMP_R)
        gap = (free - sum(heights)) / (len(boards) + 1)
        assert gap > 5, (k, gap)
        y = top - gap
        for b in boards:
            y = s.board(b["graph"], b["spacing_mm"], b["label"], y) - gap

    # counters
    side = KIT["counter_side_mm"] * MM
    dot = KIT["counter_dot_mm"] * MM / 2
    cols, rows = 10, KIT["counters_per_sheet"] // 10
    per = KIT["counters_per_set"]
    top = s.start("Counters: dot up is ON",
                  f"<b>Print on card stock, at 100%:</b> one sheet in all. Cut it into {sets} sets of {per} counters, "
                  f"one set for each board set: {counts()}; {cols * rows - sets * per} are spare.",
                  "Cut along every line with a paper trimmer: first the long lines, then across. The back of each "
                  "counter stays blank: blank up is OFF. Existing two-colour counters work too; choose one colour "
                  "for ON.")
    x0 = (W - cols * side) / 2
    y0 = top - 24
    c = s.c
    c.setStrokeGray(.35)
    c.setLineWidth(.6)
    for i in range(rows + 1):
        c.line(x0, y0 - i * side, x0 + cols * side, y0 - i * side)
    for j in range(cols + 1):
        c.line(x0 + j * side, y0, x0 + j * side, y0 - rows * side)
    c.setFillGray(.08)
    for i in range(rows):
        for j in range(cols):
            c.circle(x0 + (j + .5) * side, y0 - (i + .5) * side, dot, fill=1, stroke=0)
    assert y0 - rows * side > 90
    s.save()
    print(f"Built {OUT} ({s.page} pages)")


if __name__ == "__main__":
    build()
