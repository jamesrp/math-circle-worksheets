#!/usr/bin/env python3
"""Draw the Hackenbush puzzle sheet and its answer key.

    python3 plans/home-plans/src/hackenbush_puzzles.py

Writes plans/home-plans/2026-11-21-hackenbush-puzzles.pdf (the child's pages) and
plans/home-plans/2026-11-21-hackenbush-puzzles-key.pdf (answers for the adult).
Needs reportlab. The boards below are the single source for the pages and for the
checker (src/hackenbush_puzzles_check.py imports BOARDS), so the boards checked
are the boards printed.

A board is a list of pieces in millimetres, relative to the panel's ground line
(y = 0 is the ground):
  ("seg", x1, y1, x2, y2, colour)   a segment; endpoints that coincide are joined
  ("loop", x, y, r, colour)         a circle hanging from the point (x, y); in play
                                    it is the same as one segment on that point
  ("inf", x, pattern)               a stalk that never ends; pattern(i) is the
                                    colour of segment i, counting from the ground
"B" is blue, "R" red.
"""
import pathlib

SEG = 12  # mm, length of one stalk segment


def stalk(x, s, seg=SEG):
    """Stalk s (bottom to top) standing at x."""
    return [("seg", x, k * seg, x, (k + 1) * seg, c) for k, c in enumerate(s)]


def alternating(i):            # B R B R B R ...
    return "BR"[i % 2]


def third(i):                  # B R R B R B R ...
    return "BRR"[i] if i < 3 else "BR"[(i - 3) % 2]


def red_forever(i):            # B R R R R ...
    return "B" if i == 0 else "R"


# Problem 1: what is each stalk worth?
P1 = {"a": "BRB", "b": "BRRB", "c": "BRBB", "d": "RBR"}
# Problem 3: two blue and two red, every order (printed in this order, labelled A to F)
P3 = {"A": "BRRB", "B": "RRBB", "C": "BRBR", "D": "RBBR", "E": "BBRR", "F": "RBRB"}
# Problem 4: the board to balance
P4 = stalk(22, "BRB") + stalk(44, "BRRR")
# Problem 5: pictures
P5 = {
    "The Y": [("seg", 0, 0, 0, 16, "B"), ("seg", 0, 16, -11, 30, "B"), ("seg", 0, 16, 11, 30, "R")],
    "The bush": [("seg", 0, 0, 0, 14, "B"), ("seg", 0, 14, 0, 28, "R"),
                 ("seg", 0, 28, -10, 40, "B"), ("seg", 0, 28, 10, 40, "B")],
    "The flower": [("seg", 0, 0, 0, 13, "B"), ("seg", 0, 13, 0, 26, "B"),
                   ("seg", 0, 26, -12, 31, "R"), ("seg", 0, 26, -6, 38, "R"),
                   ("seg", 0, 26, 6, 38, "R"), ("seg", 0, 26, 12, 31, "R")],
    "The person": [("seg", -7, 0, 0, 15, "B"), ("seg", 7, 0, 0, 15, "B"),
                   ("seg", 0, 15, 0, 30, "R"),
                   ("seg", 0, 30, -11, 22, "B"), ("seg", 0, 30, 11, 22, "B"),
                   ("loop", 0, 30, 5, "R")],
}
P7 = [("inf", 0, alternating)]
P10 = [("inf", 0, red_forever)]

# everything the checker needs, by name
BOARDS = {"P1": {k: stalk(0, s) for k, s in P1.items()},
          "P3": {k: stalk(0, s) for k, s in P3.items()},
          "P4": P4, "P5": P5, "P7": P7, "P10": P10,
          "third": [("inf", 0, third)]}

INF_SHOWN = 8         # segments drawn before the dots
INF_FIRST = 13.0      # mm, the bottom segment
INF_SHRINK = 0.88


def inf_heights():
    ys, y, h = [0.0], 0.0, INF_FIRST
    for _ in range(INF_SHOWN):
        y += h
        ys.append(y)
        h *= INF_SHRINK
    return ys


# ---------------------------------------------------------------- drawing
BLUE = (0.10, 0.33, 0.85)
RED = (0.86, 0.13, 0.13)
GREY = (0.35, 0.35, 0.35)


class Page:
    def __init__(self, c, num, total):
        from reportlab.lib.pagesizes import letter
        from reportlab.lib.units import mm
        self.c, self.mm = c, mm
        self.W, self.H = letter[0] / mm, letter[1] / mm
        self.num, self.total = num, total
        c.setFont("Helvetica", 9)
        c.setFillColorRGB(*GREY)
        c.drawString(14 * mm, (self.H - 11) * mm, "Hackenbush puzzles")
        c.drawRightString((self.W - 14) * mm, 9 * mm, f"Hackenbush puzzles / page {num} of {total}")
        c.setFillColorRGB(0, 0, 0)
        self.y = self.H - 20  # cursor, mm from the bottom

    def text(self, s, size=11, bold=False, indent=0, gap=1.5, width=None):
        from reportlab.lib.utils import simpleSplit
        font = "Helvetica-Bold" if bold else "Helvetica"
        width = width or (self.W - 28 - indent)
        lines = simpleSplit(s, font, size, width * self.mm)
        self.c.setFont(font, size)
        for ln in lines:
            self.y -= size * 0.42
            self.c.drawString((14 + indent) * self.mm, self.y * self.mm, ln)
            self.y -= size * 0.12
        self.y -= gap

    def problem(self, n, s):
        """'Problem n:' in bold, then the task in plain text on the same line."""
        from reportlab.lib.utils import simpleSplit
        mm, c = self.mm, self.c
        lead = f"Problem {n}: "
        lw = c.stringWidth(lead, "Helvetica-Bold", 11) / mm
        first = simpleSplit(s, "Helvetica", 11, (self.W - 28 - lw) * mm)
        self.y -= 11 * 0.42
        c.setFont("Helvetica-Bold", 11)
        c.drawString(14 * mm, self.y * mm, lead)
        c.setFont("Helvetica", 11)
        c.drawString((14 + lw) * mm, self.y * mm, first[0])
        self.y -= 11 * 0.12
        rest = s[len(first[0]):].strip()
        if rest:
            self.text(rest, gap=0)
        self.y -= 2

    def ground(self, x1, x2, gy):
        c, mm = self.c, self.mm
        c.setStrokeColorRGB(0.2, 0.2, 0.2)
        c.setLineWidth(2.2)
        c.line(x1 * mm, gy * mm, x2 * mm, gy * mm)
        c.setLineWidth(0.6)
        x = x1 + 1
        while x < x2 - 1:
            c.line(x * mm, gy * mm, (x - 2.5) * mm, (gy - 3) * mm)
            x += 4

    def board(self, ox, gy, pieces):
        """Draw pieces with their ground point at (ox, gy)."""
        c, mm = self.c, self.mm
        c.setLineCap(1)
        joints = set()
        for p in pieces:
            if p[0] == "seg":
                _, x1, y1, x2, y2, col = p
                c.setStrokeColorRGB(*(BLUE if col == "B" else RED))
                c.setLineWidth(6)
                c.line((ox + x1) * mm, (gy + y1) * mm, (ox + x2) * mm, (gy + y2) * mm)
                joints |= {(x1, y1), (x2, y2)}
            elif p[0] == "loop":
                _, x, y, r, col = p
                c.setStrokeColorRGB(*(BLUE if col == "B" else RED))
                c.setLineWidth(5)
                c.circle((ox + x) * mm, (gy + y + r) * mm, r * mm, stroke=1, fill=0)
                joints.add((x, y))
            elif p[0] == "inf":
                _, x, pat = p
                ys = inf_heights()
                for i in range(INF_SHOWN):
                    c.setStrokeColorRGB(*(BLUE if pat(i) == "B" else RED))
                    c.setLineWidth(max(3.0, 6 * INF_SHRINK ** i))
                    c.line((ox + x) * mm, (gy + ys[i]) * mm, (ox + x) * mm, (gy + ys[i + 1]) * mm)
                c.setFillColorRGB(0, 0, 0)
                for i, yy in enumerate(ys):
                    c.circle((ox + x) * mm, (gy + yy) * mm, max(0.9, 1.5 * INF_SHRINK ** i) * mm,
                             stroke=0, fill=1)
                top = ys[-1]
                for k in range(3):
                    c.circle((ox + x) * mm, (gy + top + 4 + 3.2 * k) * mm, 0.6 * mm, stroke=0, fill=1)
                c.setFont("Helvetica-Oblique", 9)
                c.drawString((ox + x + 4) * mm, (gy + top + 6) * mm, "and so on, forever")
        c.setFillColorRGB(0, 0, 0)
        for (x, y) in joints:
            c.circle((ox + x) * mm, (gy + y) * mm, (1.3 if y == 0 else 1.5) * mm, stroke=0, fill=1)

    def label(self, x, y, s, size=11, bold=False, centre=True):
        c, mm = self.c, self.mm
        c.setFont("Helvetica-Bold" if bold else "Helvetica", size)
        c.setFillColorRGB(0, 0, 0)
        (c.drawCentredString if centre else c.drawString)(x * mm, y * mm, s)

    def lines(self, n, gap=9):
        c, mm = self.c, self.mm
        c.setStrokeColorRGB(0.7, 0.7, 0.7)
        c.setLineWidth(0.5)
        for _ in range(n):
            self.y -= gap
            c.line(14 * mm, self.y * mm, (self.W - 14) * mm, self.y * mm)
        self.y -= 3


def draw_sheet(out):
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas
    c = canvas.Canvas(str(out), pagesize=letter, invariant=1)
    c.setTitle("Hackenbush puzzles")
    TOTAL = 5

    # ---------------- page 1
    p = Page(c, 1, TOTAL)
    p.text("Hackenbush puzzles", size=16, bold=True, gap=3)
    p.text("Blue chops one blue segment, Red chops one red segment, taking turns. Anything no longer "
           "joined to the ground falls. If you have nothing to chop, you lose.")
    p.text("A board's worth counts spare moves: one blue segment is worth 1, one red segment is worth "
           "minus 1, and BR (blue on the ground, red on top) is worth 1/2. Boards side by side add up. "
           "To test a guess, play the board next to boards worth the opposite amount: if whoever moves "
           "first loses, they cancel out.", gap=5)

    p.problem(1, "What is each stalk worth?")
    gy = p.y - 52
    for k, (name, s) in enumerate(P1.items()):
        x = 14 + 23 + k * 47
        p.ground(x - 18, x + 18, gy)
        p.board(x, gy, stalk(0, s))
        p.label(x, gy - 9, f"({name})", bold=True)
        p.label(x, gy - 18, "worth: ________")
    p.y = gy - 26

    p.problem(2, "Draw a stalk worth exactly 9/16, a stalk worth exactly 11/16, and a stalk worth "
                 "exactly 2 and 3/4.")
    gy = p.y - 70
    for k, target in enumerate(["9/16", "11/16", "2 and 3/4"]):
        x = 14 + 31 + k * 63
        p.ground(x - 26, x + 26, gy)
        p.label(x, gy - 9, target, bold=True)
    c.showPage()

    # ---------------- page 2
    p = Page(c, 2, TOTAL)
    p.problem(3, "Each of these stalks has two blue segments and two red ones. Put them in order, from "
                 "the best for Blue to the best for Red.")
    gy = p.y - 54
    for k, (name, s) in enumerate(P3.items()):
        x = 14 + 16 + k * 31
        p.ground(x - 12, x + 12, gy)
        p.board(x, gy, stalk(0, s))
        p.label(x, gy - 9, name, bold=True)
    p.y = gy - 20
    p.label(14, p.y, "Best for Blue   ______   ______   ______   ______   ______   ______   Best for Red",
            centre=False)
    p.y -= 16

    p.problem(4, "Draw one more stalk on this ground so that whoever moves first loses.")
    gy = p.y - 66
    p.ground(14, p.W - 14, gy)
    p.board(14, gy, P4)
    c.showPage()

    # ---------------- page 3
    p = Page(c, 3, TOTAL)
    p.problem(5, "What is each picture worth?")
    gy = p.y - 56
    for k, (name, pieces) in enumerate(P5.items()):
        x = 14 + 23 + k * 47
        p.ground(x - 18, x + 18, gy)
        p.board(x, gy, pieces)
        p.label(x, gy - 9, name, bold=True)
        p.label(x, gy - 18, "worth: ________")
    p.y = gy - 28

    p.problem(6, "Draw a board where Red has 10 segments and Blue has only 1, and Blue still wins "
                 "whoever moves first.")
    gy = p.y - 100
    p.ground(14, p.W - 14, gy)
    c.showPage()

    # ---------------- page 4
    p = Page(c, 4, TOTAL)
    p.text("These stalks never end. A game on one still ends: after the first chop, the stalk has a top.",
           gap=4)
    p.problem(7, "This stalk goes blue, red, blue, red, and so on forever. What is it worth?")
    gy = p.y - 100
    p.ground(30, 90, gy)
    p.board(55, gy, P7)
    p.label(140, gy + 40, "worth: ____________")
    p.y = gy - 10

    p.problem(8, "Draw a stalk that never ends and is worth exactly 1/3.")
    gy = p.y - 100
    p.ground(30, 120, gy)
    c.showPage()

    # ---------------- page 5
    p = Page(c, 5, TOTAL)
    p.problem(9, "No stalk that ends is worth exactly 1/3. Why not?")
    p.lines(6)
    p.y -= 6
    p.problem(10, "Here a blue trunk holds up red segments forever. Who wins if Blue moves first? "
                  "If Red moves first? Is there any fraction bigger than 0 that this stalk is worth "
                  "more than?")
    gy = p.y - 100
    p.ground(30, 90, gy)
    p.board(55, gy, P10)
    c.showPage()
    c.save()


KEY = [
    ("h", "Hackenbush puzzles: answers"),
    ("p", "For the adult. Every answer here is checked on the printed boards by "
          "src/hackenbush_puzzles_check.py. Stalks are written bottom to top: BRRB is blue on the ground, "
          "then red, red, blue."),
    ("h2", "The mathematics"),
    ("p", "<b>Reading a stalk (Berlekamp's rule).</b> The first run of one colour counts 1 per segment. After the "
          "first change of colour, each segment counts half the one below it, plus for blue and minus for red. "
          "So every stalk that ends is worth a fraction whose bottom is a power of 2, and every such fraction "
          "is the worth of exactly one stalk."),
    ("p", "<b>Pictures.</b> Any red-blue board is worth the simplest number strictly between Blue's best chop "
          "and Red's best chop, and boards side by side add (Conway, <i>On Numbers and Games</i>; Berlekamp, "
          "Conway and Guy, <i>Winning Ways</i>; cited, not rechecked). Worth 0 means whoever moves first "
          "loses; a board beside its colour swap is always worth 0."),
    ("p", "<b>Stalks that never end.</b> Every chop leaves a stalk that ends, so a game still ends. The worth is "
          "the number squeezed between what Blue's chops leave (all below it) and what Red's chops leave (all "
          "above it). When the colours keep switching forever, that is just the rule's never-ending sum: BRBR... "
          "is 2/3, and B R R followed by BR forever is 1/3. No board that ends is worth 1/3, so thirds need "
          "infinity. When the colours stop switching, the sum lies: B with red forever on top adds to 0, but "
          "Blue wins it whoever starts. It is worth more than 0 and less than every positive fraction, which no "
          "ordinary number is; Conway's surreal numbers call it “one over omega”."),
    ("p", "<b>Route.</b> Problems 1 to 4 are about stalks, 5 and 6 about pictures, 7 to 10 about forever. "
          "Problems 9 and 10 are talking problems: let him explain out loud and help write it down."),
    ("h2", "Answers"),
    ("q", "1", "(a) BRB = 3/4. (b) BRRB = 3/8 (1 - 1/2 - 1/4 + 1/8). (c) BRBB = 7/8. (d) RBR = -3/4, the colour "
               "swap of (a). To test (a) at the table: BRB beside RB and RBB, whoever moves first loses. Hint "
               "if stuck: “BR is 1/2. What does one more blue on top add?”"),
    ("q", "2", "9/16 = BRBRR, 11/16 = BRBRB, 2 and 3/4 = BBBRB. Each is the only stalk that works. Hint for "
               "2 and 3/4: start with whole moves (how many blues at the bottom?), then go above and below "
               "with halves and quarters."),
    ("q", "3", "E BBRR (5/4), C BRBR (5/8), A BRRB (3/8), D RBBR (-3/8), F RBRB (-5/8), B RRBB (-5/4). The bottom "
               "matters most; the list reads the same from either end with colours swapped."),
    ("q", "4", "The board is 3/4 + 1/8 = 7/8. Add RBRR (-1 + 1/2 - 1/4 - 1/8 = -7/8), the only stalk that works. "
               "Test it by playing both starts."),
    ("q", "5", "The Y = 1: Blue's chops leave 0 or 1/2, Red's leaves 2, and the simplest number between 1/2 "
               "and 2 is 1, so it plays like a single blue segment. The bush = 7/8, like the stalk BRBB in "
               "problem 1(c): two blue leaves on one point act like two blue in a row. The flower = 1 and 1/16, "
               "like BBRRRR: the stem is 2 and the petals take away 1/2, 1/4, 1/8, 1/16. The person = 3/2, like "
               "BBR. Each is checked by putting it beside its colour swap. Hint: “What can Blue chop, and "
               "what is left? What can Red chop?”"),
    ("q", "6", "B with 10 red stacked on top, or one blue trunk with 10 red leaves (as on the tree board): both "
               "are worth 1/1024. Every red segment hangs from Blue's one, so Blue chops it and Red has nothing "
               "left. There is no limit: any number of red works."),
    ("q", "7", "2/3. Chopping a blue leaves 0, 1/2, 5/8, 21/32, ... (just under 2/3); chopping a red leaves 1, "
               "3/4, 11/16, ... (just over). The only number squeezed between is 2/3. Also 1 - 1/2 + 1/4 - 1/8 "
               "+ ... = 2/3. Hint: “Work out B, BR, BRB, BRBR, BRBRB. Where are they heading?”"),
    ("q", "8", "B R R, then B R B R ... forever. It is the only one. 1 - 1/2 - 1/4 = 1/4, and the tail from "
               "problem 7, shrunk to 1/8 size, adds 1/8 of 2/3, which is 1/12: 1/4 + 1/12 = 1/3. Hint: “Start "
               "from the problem 7 stalk. Can you get to 1/3 by fixing the bottom?” Three of these beside "
               "one red segment would balance."),
    ("q", "9", "A stalk that ends is a whole number plus halves, quarters, eighths and so on, down to some "
               "smallest piece, so its worth is a number of those smallest pieces: some count over 2, 4, 8, 16 "
               "and so on. If that were 1/3, then 3 times the count would be a power of 2, but multiplying 2s "
               "never makes a 3. In his words it might be: “hallving never makes thirds.” Every "
               "red-blue board that ends, not only stalks, is worth such a fraction (cited)."),
    ("q", "10", "Blue wins whoever starts. Blue first: chop the trunk and everything falls. Red first: whatever "
                "Red chops leaves B with some red on top, worth more than 0, and Blue wins that. So it is worth "
                "more than 0. But it is worth less than every BR...R: beside RBB...B (worth -1/2, -1/4, "
                "-1/8, ...) Red wins whoever starts, by chopping the forever stalk so that it keeps one "
                "more red than there are blues. So no: there is no fraction bigger than 0 that it beats. It is bigger than 0 "
                "and smaller than every fraction bigger than 0. Adding with the rule gives 1 - 1/2 - 1/4 - ... "
                "= 0, which is wrong, because the colours stop switching."),
]


def draw_key(out):
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.units import mm
    from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
    body = ParagraphStyle("body", fontName="Helvetica", fontSize=10, leading=13.2, spaceAfter=5)
    h1 = ParagraphStyle("h1", parent=body, fontName="Helvetica-Bold", fontSize=15, leading=18, spaceAfter=6)
    h2 = ParagraphStyle("h2", parent=body, fontName="Helvetica-Bold", fontSize=12, leading=15, spaceBefore=6)
    q = ParagraphStyle("q", parent=body, leftIndent=8 * mm, firstLineIndent=-8 * mm)
    flow = []
    for item in KEY:
        if item[0] == "h":
            flow.append(Paragraph(item[1], h1))
        elif item[0] == "h2":
            flow.append(Paragraph(item[1], h2))
        elif item[0] == "p":
            flow.append(Paragraph(item[1], body))
        else:
            flow.append(Paragraph(f"<b>{item[1]}.</b>&nbsp;&nbsp;{item[2]}", q))
    flow.append(Spacer(1, 2))

    def footer(c, doc):
        c.setFont("Helvetica", 9)
        c.setFillColorRGB(*GREY)
        c.drawRightString(letter[0] - 14 * mm, 9 * mm, f"Hackenbush puzzles: answers / page {doc.page}")

    doc = SimpleDocTemplate(str(out), pagesize=letter, leftMargin=16 * mm, rightMargin=16 * mm,
                            topMargin=14 * mm, bottomMargin=16 * mm, title="Hackenbush puzzles: answers",
                            invariant=1)
    doc.build(flow, onFirstPage=footer, onLaterPages=footer)


if __name__ == "__main__":
    here = pathlib.Path(__file__).resolve().parent.parent
    draw_sheet(here / "2026-11-21-hackenbush-puzzles.pdf")
    draw_key(here / "2026-11-21-hackenbush-puzzles-key.pdf")
    print("wrote the puzzles and the key in", here)
