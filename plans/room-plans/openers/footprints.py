# Builds ../2026-11-18-footprints.pdf: four "whose footprints?" puzzles on the Week 10 house town.
# One Letter page, print at 100%; readable in black and white (islands carry colour words and letters).
# Every puzzle is checked for exactly one answer by footprints_check.py.
# Run: python3 footprints.py   (needs reportlab and the DejaVu fonts)
from pathlib import Path

from reportlab.lib.colors import HexColor, black, white
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

FONTS = Path("/usr/share/fonts/truetype/dejavu")
pdfmetrics.registerFont(TTFont("Sans", str(FONTS / "DejaVuSans.ttf")))
pdfmetrics.registerFont(TTFont("Sans-Bold", str(FONTS / "DejaVuSans-Bold.ttf")))

OUT = Path(__file__).resolve().parent.parent / "2026-11-18-footprints.pdf"
W, H = letter
M = 36  # page margin

# The house town: green A top, purple B and yellow C in the middle, blue D and red E at the bottom.
POS = {"A": (0.5, 1.24), "B": (0.0, 0.72), "C": (1.0, 0.72), "D": (0.0, 0.0), "E": (1.0, 0.0)}
WORD = {"A": "green", "B": "purple", "C": "yellow", "D": "blue", "E": "red"}
FILL = {"A": "#BFE5C9", "B": "#D9C6EC", "C": "#FBE8A6", "D": "#C3D6F5", "E": "#F5C2C2"}
BRIDGES = ["DE", "DB", "EC", "BC", "BA", "CA"]

# (text, held notes, Pat's known island, "started" or "now", answer sentence)
PUZZLES = [
    ("Pat started on blue and is holding these 2 notes. Where is Pat now?",
     ["DE", "EC"], "D", "started", "Pat is on _______________ now."),
    ("Pat is on green now and is holding these 3 notes. Where did Pat start?",
     ["DB", "BC", "CA"], "A", "now", "Pat started on _______________."),
    ("Pat is on purple now and is holding these 3 notes. Where did Pat start?",
     ["BC", "CA", "BA"], "B", "now", "Pat started on _______________."),
    ("Pat started on green and is holding these 5 notes. Where is Pat now?",
     ["BA", "DB", "DE", "EC", "BC"], "A", "started", "Pat is on _______________ now."),
]


def wrap(c, text, font, size, width):
    lines, line = [], ""
    for word in text.split():
        trial = (line + " " + word).strip()
        if c.stringWidth(trial, font, size) <= width:
            line = trial
        else:
            lines.append(line)
            line = word
    return lines + [line]


def note_icon(c, x, y):
    """A small paper note with a folded corner, centred on (x, y)."""
    w, h, f = 17, 13, 5
    c.setFillColor(white)
    c.setStrokeColor(black)
    c.setLineWidth(1.2)
    p = c.beginPath()
    p.moveTo(x - w / 2, y - h / 2)
    p.lineTo(x + w / 2, y - h / 2)
    p.lineTo(x + w / 2, y + h / 2 - f)
    p.lineTo(x + w / 2 - f, y + h / 2)
    p.lineTo(x - w / 2, y + h / 2)
    p.close()
    c.drawPath(p, fill=1, stroke=1)
    c.setLineWidth(0.7)
    for dy in (-2.5, 1.0):
        c.line(x - w / 2 + 3, y + dy, x + w / 2 - 4, y + dy)


def pat(c, x, y, label):
    """A little stick figure standing at (x, y), with a two-line label under it."""
    c.setStrokeColor(black)
    c.setFillColor(black)
    c.setLineWidth(1.6)
    c.circle(x, y + 22, 4.5, fill=1, stroke=0)
    c.line(x, y + 17, x, y + 6)
    c.line(x, y + 6, x - 4.5, y - 3)
    c.line(x, y + 6, x + 4.5, y - 3)
    c.line(x - 6, y + 13, x + 6, y + 13)
    c.setFont("Sans-Bold", 8.5)
    for i, part in enumerate(label):
        c.drawCentredString(x, y - 13 - 10 * i, part)


def town(c, ox, oy, held, pat_at, pat_word):
    sx, sy = 130, 135  # points per unit
    xy = {k: (ox + sx * px, oy + sy * py) for k, (px, py) in POS.items()}
    held = {frozenset(h) for h in held}
    # bridges: plain thin grey for the rest, thick black with a note for the ones Pat holds
    for b in BRIDGES:
        (x1, y1), (x2, y2) = xy[b[0]], xy[b[1]]
        if frozenset(b) in held:
            c.setStrokeColor(black)
            c.setLineWidth(4.5)
            c.setDash()
        else:
            c.setStrokeColor(HexColor("#9A9A9A"))
            c.setLineWidth(1.3)
            c.setDash(4, 3)
        c.line(x1, y1, x2, y2)
    c.setDash()
    for b in BRIDGES:
        if frozenset(b) in held:
            (x1, y1), (x2, y2) = xy[b[0]], xy[b[1]]
            note_icon(c, (x1 + x2) / 2, (y1 + y2) / 2)
    # islands
    iw, ih = 62, 30
    for k, (x, y) in xy.items():
        c.setFillColor(HexColor(FILL[k]))
        c.setStrokeColor(black)
        c.setLineWidth(1.3)
        c.roundRect(x - iw / 2, y - ih / 2, iw, ih, 8, fill=1, stroke=1)
        c.setFillColor(black)
        c.setFont("Sans-Bold", 11)
        c.drawCentredString(x, y - 4, f"{WORD[k]} {k}")
    # Pat, just outside the town next to the known island
    x, y = xy[pat_at]
    label = ["Pat started", "here"] if pat_word == "started" else ["Pat is", "here now"]
    if pat_at == "A":
        pat(c, x + 68, y - 4, label)
    else:
        pat(c, x - 58, y - 8, label)


def main():
    c = canvas.Canvas(str(OUT), pagesize=letter)
    c.setTitle("Week 10 Bridges footprints")
    # header and footer
    c.setFont("Sans", 10)
    c.setFillColor(black)
    c.drawString(M, H - M, "Week 10 / Bridges footprints / Grades K–5")
    c.drawString(M, M - 14, "Bellingham Math Circle / Week 10 / footprints")
    # shared rules
    rules = ("Pat walked around the house town. Every time Pat crossed a bridge, Pat picked up "
             "the note on it, and a bridge with no note is closed. Pat is holding the notes on "
             "the thick bridges, so Pat crossed each of those bridges once and crossed no other bridge.")
    y = H - M - 26
    c.setFont("Sans", 12)
    for line in wrap(c, rules, "Sans", 12, W - 2 * M):
        c.drawString(M, y, line)
        y -= 16
    # four panels, two by two
    gutter = 14
    pw = (W - 2 * M - gutter) / 2
    top = y - 6
    ph = (top - M - gutter) / 2
    for i, (text, held, at, word, answer) in enumerate(PUZZLES):
        col, row = i % 2, i // 2
        px = M + col * (pw + gutter)
        py = top - (row + 1) * ph - row * gutter
        c.setStrokeColor(HexColor("#B5B5B5"))
        c.setLineWidth(0.8)
        c.roundRect(px, py, pw, ph, 10, fill=0, stroke=1)
        ty = py + ph - 22
        c.setFillColor(black)
        lines = wrap(c, f"Problem {i + 1}: " + text, "Sans", 12.5, pw - 24)
        for j, line in enumerate(lines):
            if j == 0:
                head = f"Problem {i + 1}:"
                c.setFont("Sans-Bold", 12.5)
                c.drawString(px + 12, ty, head)
                c.setFont("Sans", 12.5)
                c.drawString(px + 12 + c.stringWidth(head + " ", "Sans-Bold", 12.5), ty,
                             line[len(head):].strip())
            else:
                c.setFont("Sans", 12.5)
                c.drawString(px + 12, ty, line)
            ty -= 16
        town(c, px + 96, py + 76, held, at, word)
        c.setFont("Sans", 13)
        c.drawString(px + 16, py + 16, answer)
    c.showPage()
    c.save()
    print("wrote", OUT)


if __name__ == "__main__":
    main()
