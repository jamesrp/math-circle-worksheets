#!/usr/bin/env python3
"""Week 28 print-and-cut kit: folding disks, wedge sets, K-1 tabs and route cards.

Writes build/materials.pdf (US Letter, print at 100%). Every dimension is in
millimetres and converted once. Angles are degrees clockwise from the top, the
convention of the student pages: ray 1 points up and rays are numbered
clockwise. check_materials.py reads the finished PDF and verifies it
independently of this file.
"""
from pathlib import Path
import math

from reportlab import rl_config
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Table, TableStyle

rl_config.invariant = 1
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
OUT = ROOT / 'build' / 'materials.pdf'
FONTS = ROOT / 'fonts'
pdfmetrics.registerFont(TTFont('Kit', str(FONTS / 'DejaVuSans.ttf')))
pdfmetrics.registerFont(TTFont('KitBold', str(FONTS / 'DejaVuSans-Bold.ttf')))
pdfmetrics.registerFontFamily('Kit', normal='Kit', bold='KitBold', italic='Kit', boldItalic='KitBold')

MM = 72 / 25.4
W, H = 612, 792
LEFT = 40
ID = 'W28-M-v3'   # v2 for the October 23 student-page fixes; v3 for a fourth K-1 tab stock (Critic K, October 23)
DISK_R = 90 * MM            # 18 cm folding disks
DISK_CY = 372               # disk centre height on its page (points)

# The group in worksheet-workflow/context.md (October 3, 2026): K-1 table 4,
# grades 2-3 table 4, grades 4-5 table 3, one adult at each table.
TABLES = ('K–1', 'Grades 2–3', 'Grades 4–5', 'adults')

BODY = ParagraphStyle('body', fontName='Kit', fontSize=9.6, leading=12.6, textColor='#1a1a1a')
SMALL = ParagraphStyle('small', fontName='Kit', fontSize=8.6, leading=11, textColor='#1a1a1a')
CELL = ParagraphStyle('cell', fontName='Kit', fontSize=8.6, leading=10.6)
CELLB = ParagraphStyle('cellb', fontName='KitBold', fontSize=8.6, leading=10.6)


def pt(a, r, cx, cy):
    """Point at angle a (clockwise from up) and radius r around (cx, cy)."""
    z = math.radians(a)
    return cx + r * math.sin(z), cy + r * math.cos(z)


class Kit:
    def __init__(self):
        OUT.parent.mkdir(parents=True, exist_ok=True)
        self.c = canvas.Canvas(str(OUT), pagesize=(W, H), pageCompression=1)
        self.c.setTitle('Week 28 flat folding: print-and-cut materials')
        self.c.setAuthor('Bellingham Math Circle')
        self.page = 0

    # ----- page furniture -------------------------------------------------
    def start(self, title, counts, paper, uses, how):
        """Header, sheet heading with per-table print counts, and instructions."""
        if self.page:
            self.c.showPage()
        self.page += 1
        c = self.c
        c.setFillGray(.1)
        c.setFont('KitBold', 10)
        c.drawString(LEFT, H - 34, 'Week 28 / Flat folds / Materials')
        c.setStrokeGray(.55)
        c.setLineWidth(.6)
        c.line(LEFT, H - 41, W - LEFT, H - 41)
        c.line(LEFT, 40, W - LEFT, 40)
        c.setFont('Kit', 8)
        c.setFillGray(.2)
        c.drawString(LEFT, 27, f'Bellingham Math Circle / Week 28 / {ID} / physically unrehearsed')
        c.drawRightString(W - LEFT, 27, str(self.page))
        c.setFillGray(0)
        c.setFont('KitBold', 13)
        c.drawString(LEFT, H - 61, title)
        top = H - 68
        if counts is not None:
            per = ' · '.join(f'{t} {n}' for t, n in zip(TABLES, counts) if n)
            text = f'<b>Print on {paper}, at 100%:</b> {per}. {uses}'
        else:
            text = uses
        top = self.para(text, top)
        if how:
            top = self.para(how, top - 2)
        return top

    def para(self, text, top, style=BODY, width=W - 2 * LEFT, x=LEFT):
        p = Paragraph(text, style)
        _, h = p.wrap(width, H)
        p.drawOn(self.c, x, top - h)
        return top - h

    def scale(self, x, y):
        """The 10 cm check line: measure it before cutting."""
        c = self.c
        c.setStrokeGray(0)
        c.setLineWidth(1)
        c.line(x, y, x + 100 * MM, y)
        c.line(x, y - 4, x, y + 4)
        c.line(x + 100 * MM, y - 4, x + 100 * MM, y + 4)
        c.setFont('Kit', 8)
        c.setFillGray(0)
        c.drawString(x + 100 * MM + 8, y - 3, '10 cm check: this line must measure 10 cm')

    # ----- folding disks --------------------------------------------------
    def disk(self, rays, letter=None, note=None, numbered=True, ticks=None, long_ticks=()):
        c = self.c
        cx, cy, R = W / 2, DISK_CY, DISK_R
        # Corner marks for the optional 18 cm square trim; they sit outside the square.
        c.setStrokeGray(.35)
        c.setLineWidth(.5)
        for sx in (-1, 1):
            for sy in (-1, 1):
                x, y = cx + sx * R, cy + sy * R
                c.line(x + sx * 3, y, x + sx * 12, y)
                c.line(x, y + sy * 3, x, y + sy * 12)
        c.setFillGray(.93)
        c.circle(cx, cy, R, stroke=0, fill=1)
        c.setStrokeGray(0)
        if ticks:
            c.setLineWidth(.7)
            for k in range(int(round(360 / ticks))):
                a = k * ticks
                length = 6.5 * MM if a in long_ticks else 4 * MM
                c.line(*pt(a, R - length, cx, cy), *pt(a, R, cx, cy))
        c.setLineWidth(.6)
        for a in rays:
            c.line(cx, cy, *pt(a, R, cx, cy))
        if numbered:
            for k, a in enumerate(rays, 1):
                x, y = pt(a, R - 9 * MM, cx, cy)
                c.setFillGray(1)
                c.circle(x, y, 3.4 * MM, stroke=0, fill=1)
                c.setFillGray(0)
                c.setFont('KitBold', 11)
                c.drawCentredString(x, y - 3.9, str(k))
        c.setFillGray(0)
        c.circle(cx, cy, 1.4, stroke=0, fill=1)
        c.setLineWidth(1.1)
        c.circle(cx, cy, R, stroke=1, fill=0)
        # Letter and front mark inside the largest sector of the right half
        # (the added ray of grades 2-3 Problem 4 always lands in the left half).
        ordered = sorted(rays)
        sectors = [(ordered[i], (ordered[(i + 1) % len(ordered)] - ordered[i]) % 360 or 360)
                   for i in range(len(ordered))]
        right = [s for s in sectors if s[0] + s[1] <= 180] or sectors or [(0, 90)]
        start, span = max(right, key=lambda s: s[1])
        x, y = pt(start + span / 2, .45 * R, cx, cy)
        if letter:
            c.setFont('KitBold', 22)
            c.drawCentredString(x, y + 4, letter)
            y -= 14
        c.setFont('Kit', 10)
        c.drawCentredString(x, y - 6, 'front')
        if note:
            c.setFont('Kit', 8)
            c.drawCentredString(x, y - 19, note)

    # ----- wedges ---------------------------------------------------------
    def sector(self, cx, cy, r, a1, a2, label, gray, font=7.5):
        """One wedge from a1 to a2 (clockwise), outline is its cut line."""
        c = self.c
        c.setFillGray(gray)
        c.setStrokeGray(0)
        c.setLineWidth(.8)
        if a2 - a1 >= 360:
            c.circle(cx, cy, r, stroke=1, fill=1)
        else:
            c.wedge(cx - r, cy - r, cx + r, cy + r, 90 - a2, a2 - a1, stroke=1, fill=1)
        if label:
            span = a2 - a1
            rr = .64 * r if span < 100 else .55 * r
            x, y = pt((a1 + a2) / 2, rr, cx, cy)
            c.setFillGray(0)
            c.setFont('KitBold', font)
            c.drawCentredString(x, y - font * .36, label)

    def half_board(self, cx, cy, r):
        """Half-turn board: a semicircle on a straight edge, centre marked. Not cut."""
        c = self.c
        c.setStrokeGray(0)
        c.setLineWidth(.8)
        c.wedge(cx - r, cy - r, cx + r, cy + r, 0, 180, stroke=1, fill=0)
        c.setLineWidth(.5)
        c.line(cx - r - 4 * MM, cy, cx + r + 4 * MM, cy)
        c.circle(cx, cy, 1.1, stroke=0, fill=1)

    def fill_board(self, cx, cy, r):
        c = self.c
        c.setStrokeGray(0)
        c.setLineWidth(.8)
        c.circle(cx, cy, r, stroke=1, fill=0)
        c.setLineWidth(1)
        c.line(cx, cy, cx, cy + r)
        c.setFont('Kit', 7)
        c.drawCentredString(cx, cy + r + 3, 'start')

    def keep_whole_band(self, y_top, y_bottom, label, parts=1):
        c = self.c
        c.setStrokeGray(0)
        c.setLineWidth(.8)
        c.rect(LEFT, y_bottom, W - 2 * LEFT, y_top - y_bottom)
        for k in range(1, parts):
            x = LEFT + k * (W - 2 * LEFT) / parts
            c.line(x, y_bottom, x, y_top)
        c.setFont('Kit', 7.5)
        c.setFillGray(.25)
        c.drawString(LEFT + 4, y_top - 10, label)
        c.setFillGray(0)

    def save(self):
        self.c.save()


def disk_page(kit, title, counts, uses, rays, how, **kw):
    kit.start(title, counts, 'copy paper', uses, how)
    kit.disk(rays, **kw)
    kit.scale(LEFT, 70)


CUT = ('Cut on the circle, or trim to an 18 cm square on the four corner marks: a fold about one centre '
       'point behaves the same on both. The tinted side is the front. ')
CREASE = ('Crease each printed ray both ways, pressing only along that ray from the centre out; '
          'make no other crease. ')


def build():
    kit = Kit()
    # ---- page 1: print plan ------------------------------------------------
    top = kit.start('Print plan for the whole kit', None, None,
                    'For eleven children at three tables (K–1 four, grades 2–3 four, grades 4–5 three) and '
                    'three adults. Print every sheet at 100% (Actual size), single-sided, on US Letter. '
                    'Folding disks go on ordinary copy paper, which folds flat; card stock is too stiff to fold. '
                    'Wedges, tabs and cards go on card stock. Check the 10 cm line on every sheet after printing.',
                    None)
    rows = [['Page', 'Sheet', 'Paper', 'K–1', '2–3', '4–5', 'Adults', 'Total', 'Used in'],
            ['2', 'Disk, four right angles', 'copy', '6', '4', '4', '2', '16',
             'K–1 P1, P2, P3, P5; 2–3 P2 (A), P5; 4–5 P1 (A), P4, P5; launch'],
            ['3', 'Disk B', 'copy', '', '2', '2', '', '4', '2–3 P2; 4–5 P1'],
            ['4', 'Disk C', 'copy', '', '2', '2', '1', '5', '2–3 P2; 4–5 P1; adult pretest'],
            ['5', 'Disk D', 'copy', '', '2', '2', '1', '5', '2–3 P2; 4–5 P1; adult pretest'],
            ['6–9', 'Add-a-ray disks A, B, C, D', 'copy', '', '2 each', '', '', '8', '2–3 P4'],
            ['10', 'Blank disk, 15° rim ticks', 'copy', '1', '1', '1', '1', '4', 'extra workspace'],
            ['11', 'Seven lettered wedges', 'card', '', '1', '', '', '1', '2–3 P1'],
            ['12', 'Sixteen matching wedges', 'card', '', '2', '', '', '2', '2–3 P3; 4–5 P3 (A)'],
            ['13', 'Six wedges', 'card', '', '1', '1', '', '2', '2–3 P6; 4–5 P6, P3 (B)'],
            ['14', 'K–1 M and V tabs', 'card', '1', '', '', '', '1', 'K–1 P4; recording'],
            ['15', 'K–1 route cards A–H', 'card', '1', '', '', '', '1', 'K–1 P6']]
    cells = [[Paragraph(x, CELLB if i == 0 else CELL) for x in row] for i, row in enumerate(rows)]
    t = Table(cells, colWidths=[34, 120, 38, 30, 40, 30, 42, 36, 162])
    t.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), .4, colors.HexColor('#9aa3aa')),
                           ('LEFTPADDING', (0, 0), (-1, -1), 4), ('RIGHTPADDING', (0, 0), (-1, -1), 4),
                           ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#e8edf1')),
                           ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                           ('TOPPADDING', (0, 0), (-1, -1), 3), ('BOTTOMPADDING', (0, 0), (-1, -1), 3)]))
    _, h = t.wrapOn(kit.c, W - 2 * LEFT, H)
    t.drawOn(kit.c, LEFT, top - 10 - h)
    top -= 10 + h + 8
    for text in [
        '<b>Totals.</b> 42 sheets of copy paper and 7 of card stock. Nothing on these sheets reveals an answer, '
        'but cut the pieces before children arrive.',
        '<b>Disks.</b> Cut on the circle, or trim each disk sheet to the 18 cm square on its corner marks with '
        'four straight cuts. Whether a disk folds flat is decided at its centre, so the square folds in exactly '
        'the same ways: any flat fold of the disk enlarges to the square, and any flat fold of the square trims '
        'down to the disk. Crease each printed ray both ways before class, pressing only along that ray from '
        'the centre out; a ray with no ray opposite it must not be continued through the centre, because that '
        'would add a ray. Precrease every disk this way before class. On pages 6–9 crease only the three printed '
        'rays: children choose, draw and crease the fourth. Replace a disk that gets an extra crease.',
        '<b>Wedges.</b> Pieces in one set touch along shared cut lines, so each straight cut separates two pieces. '
        'Their radii match the student pages (2.25 cm, 2.5 cm, 2.4 cm), so a wedge can be laid on its printed '
        'picture. The half-turn boards and start disks stay whole. Keep each set in its own labelled envelope '
        'and never mix sets: the seven-piece and six-piece sets both use the letters A, B and C.',
        '<b>K–1.</b> Cut the tabs apart (36 M and 36 V, four children\'s stocks for Problem 4) and the 16 route '
        'cards (two sets of A–H).',
        '<b>Time.</b> About two and a quarter hours for one adult with scissors: 40 minutes of disk cutting (20 '
        'with squares and a paper trimmer), 45 of precreasing, 30 of wedges, 20 of tabs and cards.',
        '<b>Status.</b> Digitally checked: every printed dimension and angle, and every crease pattern against '
        'the flat-folding conditions the problems need. Physically unrehearsed: no disk from this kit has been '
        'folded and no piece has been cut. The adult pretest in the guide (pp. 2–3) still comes first.']:
        top = kit.para(text, top, style=SMALL) - 5
    kit.scale(LEFT, 70)

    # ---- folding disks -----------------------------------------------------
    disk_page(kit, 'Folding disk: four right angles', (6, 4, 4, 2),
              'K–1 Problems 1, 2, 3 and 5; grades 2–3 Problem 2 (disk A) and 5; grades 4–5 Problem 1 '
              '(disk A), 4 and 5; the launch. A spare uncut sheet makes a large recording disk.',
              [0, 90, 180, 270], CUT + CREASE)
    disk_page(kit, 'Folding disk B: 45°, 90°, 90°, 135°', (0, 2, 2, 0),
              'Grades 2–3 Problem 2 and grades 4–5 Problem 1, disk B.',
              [0, 45, 135, 225], CUT + CREASE, letter='B')
    disk_page(kit, 'Folding disk C: 60°, 120°, 120°, 60°', (0, 2, 2, 1),
              'Grades 2–3 Problem 2 and grades 4–5 Problem 1, disk C. Adults: one for the pretest.',
              [0, 60, 180, 300], CUT + CREASE, letter='C')
    disk_page(kit, 'Folding disk D: 30°, 60°, 150°, 120°', (0, 2, 2, 1),
              'Grades 2–3 Problem 2 and grades 4–5 Problem 1, disk D. Adults: pretest its tuck '
              '(guide p. 3) and keep one successful fold as a spare.',
              [0, 30, 90, 240], CUT + CREASE, letter='D')
    for letter, a in zip('ABCD', (90, 60, 30, 120)):
        disk_page(kit, f'Add-a-ray disk {letter}: rays at 0°, {a}° and 180°', (0, 2, 0, 0),
                  f'Grades 2–3 Problem 4, pattern {letter}. Short ticks mark every 30° on the rim.',
                  [0, a, 180],
                  CUT + 'Crease only the three printed rays, both ways, pressing only along each ray from the '
                  'centre out: a crease carried through the centre would add a ray. A child adds the fourth ray '
                  'with a ruler, from the centre dot to a rim tick, then creases it.',
                  letter=letter, note='add one ray', numbered=False, ticks=30)
    disk_page(kit, 'Blank disk with 15° rim ticks', (1, 1, 1, 1),
              'Extra workspace: a pattern of a child\'s own, or a grades 4–5 pattern from Problems 2 and 3. '
              'Long ticks mark every 45°.',
              [], CUT + 'Draw rays with a ruler from the centre dot to the ticks before creasing.',
              numbered=False, ticks=15, long_ticks=tuple(range(0, 360, 45)))

    # ---- wedge sets ----------------------------------------------------------
    # Seven lettered wedges, radius 2.25 cm: a disk G F E and a half-disk A C D B
    # per set; three sets. The Problem 1 page prints its own half-turn template.
    top = kit.start('Seven lettered wedges, grades 2–3 Problem 1', (0, 1, 0, 0), 'card stock',
                    'Three sets: one for each pair and a spare. A=30°, B=30°, C=60°, D=60°, E=90°, F=120°, '
                    'G=150°, radius 2.25 cm, the size of the pictures and of the half-turn template on the '
                    'Problem 1 page.',
                    'Cut each disk and half-disk on its outline, then along every line between letters. Put each '
                    'set of seven in its own envelope.')
    r = 22.5 * MM
    for k in range(3):
        y = top - 30 - r - k * (2 * r + 36)
        cx = LEFT + 90
        for a1, a2, lab in [(0, 150, 'G'), (150, 270, 'F'), (270, 360, 'E')]:
            kit.sector(cx, y, r, a1, a2, lab, .96)
        cx2 = cx + 2 * r + 60
        y2 = y - r * .45
        for a1, a2, lab in [(270, 300, 'A'), (300, 360, 'C'), (0, 60, 'D'), (60, 90, 'B')]:
            kit.sector(cx2, y2, r, a1, a2, lab, .96)
        kit.c.setFont('Kit', 8)
        kit.c.drawString(cx2 + r + 40, y - 3, f'set {k + 1}')
    kit.scale(LEFT, 70)

    # Sixteen matching wedges, radius 2.5 cm: the four grades 2-3 Problem 3 disks (one set)
    # and two half-turn boards per sheet.
    top = kit.start('Sixteen matching wedges, grades 2–3 Problem 3', (0, 2, 0, 0), 'card stock',
                    'One set and two half-turn boards per sheet, so one sheet for each pair. Each disk is cut '
                    'into the four sectors of the matching Problem 3 disk, radius 2.5 cm; sectors 1 and 3 are '
                    'shaded as on the page. Disk B\'s pieces also give grades 4–5 Problem 3, pattern A.',
                    'Cut each disk on its circle, then along its four rays to the centre. Keep the sixteen '
                    'pieces in one envelope. Cut out the board strip whole, then into its two boards: one for '
                    'the shaded pair and one for the white pair.')
    r = 25 * MM
    disks = {'A': [90, 90, 90, 90], 'B': [45, 90, 90, 135], 'C': [60, 120, 120, 60], 'D': [30, 60, 150, 120]}
    pitch = 2 * r + 30
    x0 = (W - 3 * 2 * r - 2 * 30) / 2 + r
    for j, (name, sec) in enumerate(disks.items()):
        cx = x0 + (j % 3) * pitch
        y = top - 30 - r - (j // 3) * (2 * r + 34)
        a = 0
        for i, s in enumerate(sec, 1):
            kit.sector(cx, y, r, a, a + s, f'{name}{i}', .82 if i % 2 else 1, font=7.5)
            a += s
    band_left = x0 + r + 24
    band_top = top - 30 - (2 * r + 34) + 12
    band_w = W - LEFT - band_left
    c0 = kit.c
    c0.setStrokeGray(0)
    c0.setLineWidth(.8)
    c0.rect(band_left, band_top - 2 * r - 36, band_w, 2 * r + 36)
    c0.line(band_left + band_w / 2, band_top - 2 * r - 36, band_left + band_w / 2, band_top)
    c0.setFont('Kit', 7.5)
    c0.setFillGray(.25)
    c0.drawString(band_left + 4, band_top - 10, 'Half-turn boards: keep each one whole')
    c0.setFillGray(0)
    for k in range(2):
        kit.half_board(band_left + band_w / 4 + k * band_w / 2, band_top - r - 26, r)
    kit.scale(LEFT, 70)

    # Six wedges, radius 2.4 cm: printed in an order that is not an answer.
    top = kit.start('Six wedges, grades 2–3 and 4–5 Problem 6', (0, 1, 1, 0), 'card stock',
                    'Three sets: one for each pair and a spare. A, A = 30°, B, B = 60°, C, C = 90°, radius 2.4 cm '
                    'as on the grades 2–3 page; equal letters are identical. The same set gives grades 4–5 '
                    'Problem 3, pattern B.',
                    'Cut each disk on its circle, then along its six rays to the centre. Keep each set of six in '
                    'its own envelope. The start disks stay whole: a board for filling a disk and reading '
                    'clockwise from the top ray.')
    r = 24 * MM
    order = [('A', 30), ('B', 60), ('A', 30), ('C', 90), ('B', 60), ('C', 90)]
    for k in range(3):
        cx = LEFT + (k + .5) * (W - 2 * LEFT) / 3
        y = top - 28 - r
        a = 0
        for lab, s in order:
            kit.sector(cx, y, r, a, a + s, lab, .96, font=8)
            a += s
    band_top = top - 28 - 2 * r - 26
    kit.keep_whole_band(band_top, band_top - 2 * r - 44, 'Start disks: keep each one whole', parts=3)
    for k in range(3):
        kit.fill_board(LEFT + (k + .5) * (W - 2 * LEFT) / 3, band_top - 26 - r, r)
    kit.scale(LEFT, 70)

    # ---- K-1 tabs: 10 mm squares, 36 M then 36 V ------------------------------
    top = kit.start('K–1 M and V tabs, Problem 4', (1, 0, 0, 0), 'card stock',
                    'Four children\'s stocks of nine M and nine V tabs (each Problem 4 row takes the six its '
                    'page shows), or spares for recording folds on Problems 1, 3 and 5. A printed stock box '
                    'on the page is 9 mm; these tabs are 10 mm and cover it.',
                    'Cut along every line. Keep the tabs in an envelope.')
    s = 10 * MM
    x0 = (W - 9 * s) / 2
    y0 = top - 30
    c = kit.c
    for row in range(8):
        for col in range(9):
            x, y = x0 + col * s, y0 - (row + 1) * s
            c.setStrokeGray(0)
            c.setLineWidth(.6)
            c.rect(x, y, s, s, stroke=1, fill=0)
            c.setFont('KitBold', 15)
            c.drawCentredString(x + s / 2, y + s / 2 - 5.3, 'M' if row < 4 else 'V')
    kit.scale(LEFT, 70)

    # ---- K-1 route cards: two sets of the eight folds -------------------------
    top = kit.start('K–1 route cards A–H, Problem 6', (1, 0, 0, 0), 'card stock',
                    'Two sets, one for each pair. Each card is one of the eight folds printed on the Problem 6 '
                    'page, with the same letter, so children can move cards into a route before writing it.',
                    'Cut along every line between cards.')
    words = ['MMMV', 'MMVM', 'MVMM', 'VMMM', 'MVVV', 'VMVV', 'VVMV', 'VVVM']
    s = 46 * MM
    x0 = (W - 4 * s) / 2
    y0 = top - 16
    for k in range(16):
        row, col = divmod(k, 4)
        x, y = x0 + col * s, y0 - (row + 1) * s
        letter, word = 'ABCDEFGH'[k % 8], words[k % 8]
        c.setStrokeGray(0)
        c.setLineWidth(.6)
        c.rect(x, y, s, s, stroke=1, fill=0)
        c.setFont('KitBold', 14)
        c.drawString(x + 3 * MM, y + s - 7 * MM, letter)
        cx, cy, rr = x + s / 2, y + s / 2 - 2 * MM, 14 * MM
        c.setLineWidth(.8)
        c.circle(cx, cy, rr, stroke=1, fill=0)
        for i, a in enumerate((0, 90, 180, 270)):
            c.line(cx, cy, *pt(a, rr, cx, cy))
            nx, ny = pt(a, rr + 3.2 * MM, cx, cy)
            c.setFont('Kit', 6.5)
            c.drawCentredString(nx, ny - 2.3, str(i + 1))
            lx, ly = pt(a, .58 * rr, cx, cy)
            c.setFillGray(1)
            c.rect(lx - 3.6, ly - 4.2, 7.2, 8.6, stroke=0, fill=1)
            c.setFillGray(0)
            c.setFont('KitBold', 9)
            c.drawCentredString(lx, ly - 3.2, word[i])
        c.circle(cx, cy, 1, stroke=0, fill=1)
    kit.scale(LEFT, 70)
    kit.save()
    print(f'Built {OUT} ({kit.page} pages)')


if __name__ == '__main__':
    build()
