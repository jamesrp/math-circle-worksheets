#!/usr/bin/env python3
"""Week 37 kit: a card-stock tetrahedron net, removable letter caps, a pose mat.

Writes materials.pdf in the package root (US Letter, print at 100%).
check_materials.py reads the finished PDF and verifies it independently.

Geometry. The net is an equilateral triangle of side 180 mm cut into four
faces of edge 90 mm; folding the three corner faces up closes a regular
tetrahedron. Folding brings the six outer half-sides together in three pairs;
one half of each pair carries a tab, and the seam is taped. A letter cap is three equilateral
triangles of side 26 mm around one point (half of a regular hexagon): folded on
its two inner lines it has the same three 60-degree face angles as a corner of
the model, so it sits over that corner and shows its letter on all three faces.
"""
from pathlib import Path
import math

from reportlab import rl_config
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph

rl_config.invariant = 1
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
OUT = ROOT / 'materials.pdf'
FONTS = ROOT / 'fonts'
pdfmetrics.registerFont(TTFont('Kit', str(FONTS / 'DejaVuSans.ttf')))
pdfmetrics.registerFont(TTFont('KitBold', str(FONTS / 'DejaVuSans-Bold.ttf')))
pdfmetrics.registerFontFamily('Kit', normal='Kit', bold='KitBold', italic='Kit', boldItalic='KitBold')

MM = 72 / 25.4
W, H = 612, 792
LEFT = 40
ID = 'W37-M-v1'
EDGE = 90 * MM          # model edge
CAP = 26 * MM           # letter-cap triangle side
TAB = 9 * MM            # glue-tab depth
SQ3 = math.sqrt(3)
TABLES = ('K–1', 'Grades 2–3', 'Grades 4–5', 'adults')
# Sheets per table. Group of eleven (worksheet-workflow/context.md): K–1 4, grades 2–3 4, grades 4–5 3.
NETS = (4, 4, 3, 2)      # one model per child, two for the adults
CAPS = (1, 1, 1, 1)      # each sheet caps four models
MATS = (2, 2, 2, 1)      # one per pair or trio of models, one for the launch
BODY = ParagraphStyle('body', fontName='Kit', fontSize=9.6, leading=12.6, textColor='#1a1a1a')


class Kit:
    def __init__(self):
        self.c = canvas.Canvas(str(OUT), pagesize=(W, H), pageCompression=1)
        self.c.setTitle('Week 37 mirror twins: print-and-cut materials')
        self.c.setAuthor('Bellingham Math Circle')
        self.page = 0

    def start(self, title, counts, paper, uses, how):
        if self.page:
            self.c.showPage()
        self.page += 1
        c = self.c
        c.setFillGray(.1)
        c.setFont('KitBold', 10)
        c.drawString(LEFT, H - 34, 'Week 37 / Mirror twins / Materials')
        c.setStrokeGray(.55)
        c.setLineWidth(.6)
        c.line(LEFT, H - 41, W - LEFT, H - 41)
        c.line(LEFT, 40, W - LEFT, 40)
        c.setFont('Kit', 8)
        c.setFillGray(.2)
        c.drawString(LEFT, 27, f'Bellingham Math Circle / Week 37 / {ID} / physically unrehearsed')
        c.drawRightString(W - LEFT, 27, str(self.page))
        c.setFillGray(0)
        c.setFont('KitBold', 13)
        c.drawString(LEFT, H - 61, title)
        per = ' · '.join(f'{t} {n}' for t, n in zip(TABLES, counts) if n)
        top = self.para(f'<b>Print on {paper}, at 100%:</b> {per}. {uses}', H - 68)
        return self.para(how, top - 2)

    def para(self, text, top):
        p = Paragraph(text, BODY)
        _, h = p.wrap(W - 2 * LEFT, H)
        p.drawOn(self.c, LEFT, top - h)
        return top - h

    def scale(self, x, y):
        c = self.c
        c.setStrokeGray(0)
        c.setLineWidth(1)
        c.line(x, y, x + 100 * MM, y)
        c.line(x, y - 4, x, y + 4)
        c.line(x + 100 * MM, y - 4, x + 100 * MM, y + 4)
        c.setFont('Kit', 8)
        c.drawString(x + 100 * MM + 8, y - 3, '10 cm check: this line must measure 10 cm')

    def poly(self, pts, stroke=1, fill=0, dash=None, width=.9, gray=0):
        c = self.c
        p = c.beginPath()
        p.moveTo(*pts[0])
        for q in pts[1:]:
            p.lineTo(*q)
        p.close()
        c.setLineWidth(width)
        c.setStrokeGray(0)
        c.setFillGray(gray)
        if dash:
            c.setDash(*dash)
        c.drawPath(p, stroke=stroke, fill=fill)
        c.setDash()

    def line(self, a, b, dash=None, width=.9):
        c = self.c
        c.setLineWidth(width)
        c.setStrokeGray(0)
        if dash:
            c.setDash(*dash)
        c.line(*a, *b)
        c.setDash()

    def save(self):
        self.c.save()


def tab(a, b, inward_from):
    """Trapezoid glue tab on segment a-b, on the side away from point inward_from."""
    ax, ay = a
    bx, by = b
    ux, uy = (bx - ax) / EDGE, (by - ay) / EDGE
    nx, ny = -uy, ux
    mx, my = (ax + bx) / 2, (ay + by) / 2
    if (inward_from[0] - mx) * nx + (inward_from[1] - my) * ny > 0:
        nx, ny = -nx, -ny
    inset = TAB / math.tan(math.radians(50))
    return [a, (ax + ux * inset + nx * TAB, ay + uy * inset + ny * TAB),
            (bx - ux * inset + nx * TAB, by - uy * inset + ny * TAB), b]


def cap(kit, x, y, up, letter):
    """Letter cap with its long side at height y, centred on x; up=True points up."""
    s = CAP
    h = s * SQ3 / 2
    sgn = 1 if up else -1
    o = (x, y)                                   # centre of the long side: the corner point
    pts = [(x - s, y), (x + s, y), (x + s / 2, y + sgn * h), (x - s / 2, y + sgn * h)]
    kit.poly(pts, width=.8)
    for q in (pts[2], pts[3]):
        kit.line(o, q, dash=(3, 2), width=.6)
    kit.c.setFont('KitBold', 14)
    for k in range(3):
        a = math.radians(30 + 60 * k)
        cx, cy = x + math.cos(a) * h * .62, y + sgn * math.sin(a) * h * .62
        kit.c.drawCentredString(cx, cy - 5, letter)


def build():
    kit = Kit()
    # ---- page 1: tetrahedron net ------------------------------------------
    top = kit.start('Tetrahedron model: net with 90 mm edges', NETS, 'card stock',
                    'One model per sheet: one for each child, and two for the adults, who use them for the '
                    'pretest and the launch and keep them as spares.',
                    'Cut on the solid outline. Score the dashed lines with a ballpoint pen against a ruler, then fold '
                    'each so the printed side ends up inside. Close the model with the three tabs inside and tape '
                    'each of the three open edges along its full length. A closed card '
                    'tetrahedron cannot flex: it is the rigid model the pages call for. Leave the faces blank; '
                    'letters go on the caps. Allow about 6 minutes per model.')
    big = 2 * EDGE
    cx = W / 2
    base_y = 128
    P = (cx, base_y + big * SQ3 / 2)
    Q = (cx - EDGE, base_y)
    R = (cx + EDGE, base_y)
    mPQ = ((P[0] + Q[0]) / 2, (P[1] + Q[1]) / 2)
    mQR = ((Q[0] + R[0]) / 2, (Q[1] + R[1]) / 2)
    mRP = ((R[0] + P[0]) / 2, (R[1] + P[1]) / 2)
    centre = ((P[0] + Q[0] + R[0]) / 3, (P[1] + Q[1] + R[1]) / 3)
    t1 = tab(mPQ, P, centre)     # upper half of the left side
    t2 = tab(P, mRP, centre)     # upper half of the right side
    t3 = tab(Q, mQR, centre)     # left half of the base
    # walk the outline counterclockwise: Q -> base tab -> mQR -> R -> mRP -> right tab -> P -> left tab -> mPQ
    outline = [Q, t3[1], t3[2], mQR, R, mRP, t2[2], t2[1], P, t1[2], t1[1], mPQ]
    kit.poly(outline, width=1)
    for a, b in [(mPQ, mQR), (mQR, mRP), (mRP, mPQ), (mPQ, P), (P, mRP), (Q, mQR)]:
        kit.line(a, b, dash=(4, 3), width=.7)
    kit.c.setFont('Kit', 7)
    kit.c.setFillGray(.35)
    for t in (t1, t2, t3):
        mx = sum(p[0] for p in t) / 4
        my = sum(p[1] for p in t) / 4
        kit.c.drawCentredString(mx, my - 2.5, 'tab')
    kit.c.setFillGray(0)
    kit.scale(LEFT, 70)

    # ---- page 2: letter caps ----------------------------------------------
    top = kit.start('Letter caps: A, A, B, B, C, C, D for each model', CAPS, 'card stock',
                    'Each sheet gives four models their seven caps: 8 A, 8 B, 8 C and 4 D. The spares let a pair '
                    'make any two letters equal while keeping one of the two names (grades 2–3 and 4–5 Problem 4), '
                    'and build A, A, B, C (K–1 Problem 4, grades 2–3 Problems 5 and 6).',
                    'Cut each row out along its two long edges, then cut along the slanted lines. Fold both dashed '
                    'lines of each cap so the letters are outside. A cap wraps one corner of a model, its three '
                    'triangles on the three faces there; a pea-sized ball of sticky tack inside holds it. To change '
                    'a letter, swap the cap.')
    rows = ['AAAA', 'AAAA', 'BBBB', 'BBBB', 'CCCC', 'CCCC', 'DDDD']
    h = CAP * SQ3 / 2
    pitch = 1.5 * CAP
    width = 3 * pitch + 2 * CAP
    x0 = (W - width) / 2 + CAP
    y = top - 14
    for r, letters in enumerate(rows):
        y_row_top = y - r * (h + 3 * MM)
        for k, letter in enumerate(letters):
            up = k % 2 == 0
            x = x0 + k * pitch
            cap(kit, x, y_row_top - h if up else y_row_top, up, letter)
    kit.scale(LEFT, 70)

    # ---- page 3: pose mat ---------------------------------------------------
    top = kit.start('Pose mat: two footprints', MATS, 'copy paper',
                    'One sheet for each pair or trio, and one for the launch. Each footprint is the size of a '
                    'model face.',
                    'Stand each model on a footprint, corners on the corners. Then “same pose” means the same '
                    'letter at the top, at the back, at front left and at front right. Cut across the middle line '
                    'to give each child a footprint, or keep the pair together.')
    hh = EDGE * SQ3 / 2
    mid = (top + 70) / 2 + 6
    kit.line((LEFT, mid), (W - LEFT, mid), width=.6)
    for k, (label, ytop) in enumerate([('first model', top - 30), ('second model', mid - 34)]):
        apex = (W / 2, ytop)
        bl = (W / 2 - EDGE / 2, ytop - hh)
        br = (W / 2 + EDGE / 2, ytop - hh)
        kit.poly([apex, bl, br], width=1.2, fill=1, gray=.94)
        kit.c.setFillGray(0)
        kit.c.setFont('Kit', 9)
        kit.c.drawCentredString(apex[0], apex[1] + 6, 'back')
        kit.c.drawRightString(bl[0] - 6, bl[1] - 3, 'front left')
        kit.c.drawString(br[0] + 6, br[1] - 3, 'front right')
        kit.c.setFont('KitBold', 10)
        kit.c.drawCentredString(W / 2, bl[1] + hh / 3 - 4, label)
        kit.c.setFont('Kit', 8)
        kit.c.drawCentredString(W / 2, bl[1] - 16, 'this edge faces you')
    kit.scale(LEFT, 70)
    kit.save()
    print(f'Built {OUT} ({kit.page} pages)')


if __name__ == '__main__':
    build()
