#!/usr/bin/env python3
"""Draw the Hackenbush starting-positions page for plans/home-plans/2026-11-21-hackenbush.md.

    python3 plans/home-plans/src/hackenbush_positions.py

Writes plans/home-plans/2026-11-21-hackenbush-positions.pdf (needs reportlab). The
geometry below is the single source for the page and for the checker
(src/hackenbush_check.py imports POSITIONS), so the boards checked are the boards
printed. Each board is a list of segments (x1, y1, x2, y2, colour) in millimetres
inside its panel; a point on y = GROUND touches the ground. "B" is blue, "R" red.
"""
import pathlib

GROUND = 12  # mm above the panel's bottom edge

# (number, kid name, segments)
POSITIONS = [
    (1, "Two towers", [
        (30, 12, 30, 30, "B"), (30, 30, 30, 48, "B"), (30, 48, 30, 66, "B"),
        (64, 12, 64, 30, "R"), (64, 30, 64, 48, "R"),
    ]),
    (2, "The tree", [
        (47, 12, 47, 36, "B"),
        (47, 36, 27, 56, "R"), (47, 36, 47, 64, "R"), (47, 36, 67, 56, "R"),
    ]),
    (3, "The house", [
        (30, 12, 30, 38, "B"), (64, 12, 64, 38, "B"),
        (30, 38, 64, 38, "R"), (30, 38, 47, 60, "R"), (64, 38, 47, 60, "R"),
    ]),
    (4, "Sticks", [
        (34, 12, 34, 30, "B"), (34, 30, 34, 48, "R"),
        (60, 12, 60, 30, "R"),
    ]),
    (5, "More sticks", [
        (24, 12, 24, 30, "B"), (24, 30, 24, 48, "R"),
        (47, 12, 47, 30, "B"), (47, 30, 47, 48, "R"),
        (70, 12, 70, 30, "R"),
    ]),
    (6, "Your board", []),
]


def draw(out):
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.units import mm
    from reportlab.pdfgen import canvas

    BLUE = (0.10, 0.33, 0.85)
    RED = (0.86, 0.13, 0.13)
    W, H = letter
    c = canvas.Canvas(str(out), pagesize=letter, invariant=1)
    c.setTitle("Hackenbush starting positions")
    c.setFont("Helvetica-Bold", 15)
    c.drawString(14 * mm, H - 16 * mm, "Hackenbush: starting positions")
    c.setFont("Helvetica", 9)
    c.setFillColorRGB(0.4, 0.4, 0.4)
    c.drawRightString(W - 14 * mm, H - 16 * mm,
                      "Print in colour. Blue chops blue, Red chops red. Cross out whatever falls.")
    pw, ph, gap = 92, 78, 6
    x0 = (W / mm - 2 * pw - gap) / 2
    y_top = H / mm - 24
    for k, (num, name, segs) in enumerate(POSITIONS):
        col, row = k % 2, k // 2
        px = x0 + col * (pw + gap)
        py = y_top - (row + 1) * ph - row * gap
        c.setStrokeColorRGB(0.75, 0.75, 0.75)
        c.setLineWidth(0.6)
        c.roundRect(px * mm, py * mm, pw * mm, ph * mm, 3 * mm)
        c.setFillColorRGB(0, 0, 0)
        c.setFont("Helvetica-Bold", 12)
        c.drawString((px + 4) * mm, (py + ph - 7) * mm, f"{num}  {name}")
        # ground: a thick line with hatching below
        gy = py + GROUND
        c.setStrokeColorRGB(0.2, 0.2, 0.2)
        c.setLineWidth(2.2)
        c.line((px + 8) * mm, gy * mm, (px + pw - 8) * mm, gy * mm)
        c.setLineWidth(0.6)
        x = px + 9
        while x < px + pw - 9:
            c.line(x * mm, gy * mm, (x - 2.5) * mm, (gy - 3) * mm)
            x += 4
        c.setLineCap(1)
        for (x1, y1, x2, y2, colour) in segs:
            c.setStrokeColorRGB(*(BLUE if colour == "B" else RED))
            c.setLineWidth(6.5)
            c.line((px + x1) * mm, (py + y1) * mm, (px + x2) * mm, (py + y2) * mm)
        # joints, so every segment is visibly separate
        joints = {(x, y) for (x1, y1, x2, y2, _) in segs for (x, y) in ((x1, y1), (x2, y2))}
        c.setFillColorRGB(0, 0, 0)
        for (x, y) in joints:
            c.circle((px + x) * mm, (py + y) * mm, (1.4 if y == GROUND else 1.6) * mm, stroke=0, fill=1)
        if not segs:
            c.setFont("Helvetica", 9)
            c.setFillColorRGB(0.45, 0.45, 0.45)
            c.drawCentredString((px + pw / 2) * mm, (py + 40) * mm,
                                "Draw a board here, or on any scrap of paper.")
    c.showPage()
    c.save()


if __name__ == "__main__":
    out = pathlib.Path(__file__).resolve().parent.parent / "2026-11-21-hackenbush-positions.pdf"
    draw(out)
    print("wrote", out)
