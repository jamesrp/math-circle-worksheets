#!/usr/bin/env python3
"""Week 38 strips: print-and-cut bands A and B, and the one-third B for Problem 7.

Writes materials.pdf in the package root (US Letter landscape, print at 100%).
check_materials.py reads the finished PDF and verifies it independently.

Each strip is 260 x 45 mm. Its short ends carry corner marks, a dot and a
square, and an arrow from square to dot. Joining a strip's ends dot to dot and
square to square with matching marks on the same long edge (A) gives a band
with no half-turn, an annulus; on B the right end's marks are swapped, so the
same join needs one half-turn and gives a Moebius band. Sheet 1 has the dashed
middle line and U and L on the two halves (Problems 1-6). Sheet 2 has B's
marks and a dotted line one third of the way across, and the same line two
thirds of the way across: after the half-turn they are one closed cut
(K-1 and grades 2-3 Problem 7).
"""
from pathlib import Path

from reportlab import rl_config
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

rl_config.invariant = 1
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
OUT = ROOT / 'materials.pdf'
FONTS = ROOT / 'fonts'
pdfmetrics.registerFont(TTFont('Kit', str(FONTS / 'DejaVuSans.ttf')))
pdfmetrics.registerFont(TTFont('KitBold', str(FONTS / 'DejaVuSans-Bold.ttf')))

MM = 72 / 25.4
W, H = 792, 612                 # US Letter landscape
ID = 'W38-M-v1'
SL, SH = 260 * MM, 45 * MM      # strip length and height
X0 = (W - SL) / 2               # 9.7 mm side margins
TOP = H - 19.5 * MM             # top of the first strip
MARK = 6 * MM                   # corner-mark centre, from the end and from the long edge
ARROW = 14 * MM                 # alignment arrow, from the end
# Group of eleven at three tables (worksheet-workflow/context.md): K-1 4, grades 2-3 4, grades 4-5 3.
SHEET1 = 14                     # one per child, three for the adults (pretest, launch, spares)
SHEET2 = 3                      # twelve new B: eight K-3 children, pretest, launch, two spares


def mark(c, x, y, dot):
    c.setStrokeGray(0)
    c.setLineWidth(.8)
    if dot:
        c.setFillGray(0)
        c.circle(x, y, 2.2 * MM, stroke=0, fill=1)
    else:
        c.setFillGray(1)
        c.rect(x - 2 * MM, y - 2 * MM, 4 * MM, 4 * MM, stroke=1, fill=1)
    c.setFillGray(0)


def arrow(c, x, y_from, y_to):
    c.setStrokeGray(0)
    c.setFillGray(0)
    c.setLineWidth(.9)
    s = 1 if y_to > y_from else -1
    c.line(x, y_from, x, y_to - s * 2.2 * MM)
    p = c.beginPath()
    p.moveTo(x, y_to)
    p.lineTo(x - 1.3 * MM, y_to - s * 2.6 * MM)
    p.lineTo(x + 1.3 * MM, y_to - s * 2.6 * MM)
    p.close()
    c.drawPath(p, stroke=0, fill=1)


def strip(c, top, name, swapped, lines):
    """One strip with its top edge at y=top. swapped: the right end's marks are B's."""
    bottom = top - SH
    c.setStrokeGray(0)
    c.setLineWidth(1)
    c.rect(X0, bottom, SL, SH, stroke=1, fill=0)
    hi, lo = top - MARK, bottom + MARK
    for x, right in ((X0 + MARK, False), (X0 + SL - MARK, True)):
        dot_top = not (right and swapped)
        mark(c, x, hi, dot_top)
        mark(c, x, lo, not dot_top)
        ax = X0 + ARROW if not right else X0 + SL - ARROW
        if dot_top:
            arrow(c, ax, lo + 2 * MM, hi - 2 * MM)
        else:
            arrow(c, ax, hi - 2 * MM, lo + 2 * MM)
    if lines == 'middle':
        c.setStrokeGray(.35)
        c.setLineWidth(.7)
        c.setDash(4, 3)
        c.line(X0, top - SH / 2, X0 + SL, top - SH / 2)
        c.setDash()
        c.setFillGray(.25)
        c.setFont('Kit', 13)
        for xm in (70, 130, 190):
            c.drawCentredString(X0 + xm * MM, top - SH / 4 - 4.5, 'U')
            c.drawCentredString(X0 + xm * MM, bottom + SH / 4 - 4.5, 'L')
    else:
        c.setStrokeGray(0)
        c.setLineWidth(.9)
        c.setDash(1, 2.5)
        for f in (1 / 3, 2 / 3):
            c.line(X0, top - f * SH, X0 + SL, top - f * SH)
        c.setDash()
    c.setFillGray(0)
    c.setFont('KitBold', 15)
    c.drawString(X0 + 22 * MM, top - SH / 4 - 5.5 if lines == 'middle' else top - SH / 2 - 5.5, name)


def page(c, n, title, lines):
    c.setFillGray(.1)
    c.setFont('KitBold', 9.5)
    c.drawString(X0, H - 7.5 * MM, title)
    c.setFont('Kit', 8)
    c.drawRightString(X0 + SL, H - 7.5 * MM, 'physically unrehearsed')
    c.setStrokeGray(.55)
    c.setLineWidth(.6)
    c.line(X0, H - 9.5 * MM, X0 + SL, H - 9.5 * MM)
    c.setFont('Kit', 8)
    c.setFillGray(0)
    for k, text in enumerate(lines):
        c.drawString(X0, H - (13.4 + 3.5 * k) * MM, text)
    c.setFillGray(.2)
    c.drawString(X0, 9.9 * MM, f'Bellingham Math Circle / Week 38 / {ID} / page {n}')
    # 10 cm check, right-aligned with the strips
    x1 = X0 + SL
    x0 = x1 - 100 * MM
    c.setStrokeGray(0)
    c.setLineWidth(1)
    c.line(x0, 11 * MM, x1, 11 * MM)
    c.line(x0, 11 * MM - 4, x0, 11 * MM + 4)
    c.line(x1, 11 * MM - 4, x1, 11 * MM + 4)
    c.setFillGray(0)
    c.drawRightString(x0 - 6, 11 * MM - 3, '10 cm check: this line must measure 10 cm')


def build():
    c = canvas.Canvas(str(OUT), pagesize=(W, H), pageCompression=1)
    c.setTitle('Week 38 seams: print-and-cut strips')
    c.setAuthor('Bellingham Math Circle')
    page(c, 1, 'Week 38 / Seams / Materials: strips A and B',
         [f'Print {SHEET1} copies at 100% on copy paper: one per child (grades 4–5 use the spare A and B in '
          'Problem 6), three for the adults. Cut on the solid lines.',
          'Write U and L on the back, behind the printed U and L. Tape the short ends on both faces, dot to dot '
          'and square to square: A with no twist, B with one half-turn.'])
    for k, (name, swapped) in enumerate((('A', False), ('B', True), ('A', False), ('B', True))):
        strip(c, TOP - k * SH, name, swapped, 'middle')
    c.showPage()
    page(c, 2, 'Week 38 / Seams / Materials: new B for K–1 and grades 2–3 Problem 7',
         [f'Print {SHEET2} copies at 100% on copy paper: twelve strips for eight children, the pretest, '
          'the launch and two spares. Cut on the solid lines.',
          'Join each as B, with one half-turn. The dotted lines meet at the seam as one closed line; in '
          'Problem 7 an adult cuts along it until the cut closes, twice round.'])
    for k in range(4):
        strip(c, TOP - k * SH, 'new B', True, 'thirds')
    c.showPage()
    c.save()
    print(f'Built {OUT} (2 pages)')


if __name__ == '__main__':
    build()
