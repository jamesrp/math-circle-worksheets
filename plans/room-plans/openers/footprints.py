# Builds ../2026-11-18-footprints.pdf: three route-logic puzzles ("whose footprints?") for the Week 10
# Bridges circle. One Letter page, print in colour at 100%. Puzzles live in footprints_puzzles.py and
# are checked for exactly one route, with every clue needed, by footprints_check.py.
# Run: python3 footprints.py   (needs reportlab and the DejaVu fonts)
from pathlib import Path

from reportlab.lib.colors import HexColor, black
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

from footprints_puzzles import PUZZLES

FONTS = Path("/usr/share/fonts/truetype/dejavu")
pdfmetrics.registerFont(TTFont("Sans", str(FONTS / "DejaVuSans.ttf")))
pdfmetrics.registerFont(TTFont("Sans-Bold", str(FONTS / "DejaVuSans-Bold.ttf")))

OUT = Path(__file__).resolve().parent.parent / "2026-11-18-footprints.pdf"
W, H = letter
M = 36
FILL = {"G": "#BFE5C9", "R": "#F5C2C2", "B": "#C3D6F5", "Y": "#FBE8A6", "W": "#FFFFFF"}
WORD = {"G": "green", "R": "red", "B": "blue", "Y": "yellow", "W": ""}
BRIDGE = {"R": "#D83A3A", "B": "#3B73D6", None: "#555555"}

RULES = ("Pat walks from island to island over the bridges. Pat never crosses the same bridge twice, "
         "but Pat may stand on an island more than once. Use the clues to find Pat's whole route. "
         "Write it as the islands' letters in order.")


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


def town(c, ox, oy, p, sx, sy):
    xy = {k: (ox + sx * a, oy + sy * b) for k, (a, b) in p["pos"].items()}
    for e in p["edges"]:
        col = e[2] if len(e) > 2 else None
        c.setStrokeColor(HexColor(BRIDGE[col]))
        c.setLineWidth(4.5 if col else 2.5)
        if col == "B":
            c.setDash(7, 4)  # blue bridges also dashed, so they stay distinct if colour fades
        c.line(*xy[e[0]], *xy[e[1]])
        c.setDash()
    for k, (x, y) in xy.items():
        c.setFillColor(HexColor(FILL[p["islands"][k]]))
        c.setStrokeColor(black)
        c.setLineWidth(1.3)
        c.roundRect(x - 33, y - 15, 66, 30, 8, fill=1, stroke=1)
        c.setFillColor(black)
        c.setFont("Sans-Bold", 11.5)
        c.drawCentredString(x, y - 4, (WORD[p["islands"][k]] + " " + k).strip())


def main():
    c = canvas.Canvas(str(OUT), pagesize=letter)
    c.setTitle("Week 10 Bridges footprints")
    c.setFillColor(black)
    c.setFont("Sans", 10)
    c.drawString(M, H - M, "Week 10 / Bridges footprints / Grades 2–5")
    c.drawString(M, M - 14, "Bellingham Math Circle / Week 10 / footprints")
    y = H - M - 26
    c.setFont("Sans", 12.5)
    for line in wrap(c, RULES, "Sans", 12.5, W - 2 * M):
        c.drawString(M, y, line)
        y -= 17
    gap = 12
    top = y - 4
    ph = (top - M - 2 * gap) / 3
    pw = W - 2 * M
    for i, p in enumerate(PUZZLES):
        py = top - (i + 1) * ph - i * gap
        c.setStrokeColor(HexColor("#B5B5B5"))
        c.setLineWidth(0.8)
        c.roundRect(M, py, pw, ph, 10, fill=0, stroke=1)
        # town on the left
        six = len(p["pos"]) == 6
        sx, sy = (105, 130) if six else (150, 105)
        span_y = sy * max(b for _, b in p["pos"].values())
        town(c, M + 48, py + (ph - span_y) / 2, p, sx, sy)
        # problem and clues on the right
        tx = M + 300
        ty = py + ph - 28
        c.setFillColor(black)
        c.setFont("Sans-Bold", 13)
        c.drawString(tx, ty, f"Problem {p['n']}:")
        c.setFont("Sans", 13)
        c.drawString(tx + c.stringWidth(f"Problem {p['n']}: ", "Sans-Bold", 13), ty, "Find Pat's route.")
        ty -= 26
        for clue in p["clues"]:
            lines = wrap(c, clue, "Sans", 13, pw - (tx - M) - 34)
            c.drawString(tx, ty, "•")
            for line in lines:
                c.drawString(tx + 14, ty, line)
                ty -= 18
            ty -= 6
        c.setFont("Sans", 13)
        c.drawString(tx, py + 22, "Pat's route:")
        c.setLineWidth(0.8)
        c.setStrokeColor(black)
        c.line(tx + 84, py + 20, M + pw - 16, py + 20)
    c.showPage()
    c.save()
    print("wrote", OUT)


if __name__ == "__main__":
    main()
