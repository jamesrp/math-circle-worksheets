"""Week 87 figures, canvas page template and materials pages, carried over from the old
builder (archive-before-problem-files-2026-10-23/build.py). The October 23, 2026 card fixes
changed two drawings: number-line stems (numberline) and the knockout mat's Out and Winner boxes.

Coordinates are millimetres from the top-left corner of the paper, y down: each page is
one TikZ overlay that draws its own header, rules, footer and page number. Problem files
call the functions below by name in their `figure` sections; the rules and prompt wording
live in the problem files. The materials pages are not problem files:
editable/student/build.py writes them with materials_tex().
"""

PRE = r'''\documentclass[letterpaper]{article}
\usepackage[margin=0pt]{geometry}
\usepackage[T1]{fontenc}
\usepackage{lmodern,tikz}
\pagestyle{empty}
\setlength{\parindent}{0pt}
\pdfinfoomitdate=1
\pdftrailerid{}
\pdfsuppressptexinfo=15
\begin{document}
'''
OPEN = r'\null\begin{tikzpicture}[remember picture,overlay,x=1mm,y=-1mm]\begin{scope}[shift={(current page.north west)}]'
CLOSE = r'\end{scope}\end{tikzpicture}'


# ---------------------------------------------------------------- drawing primitives

def t(x, y, s, w=178, size=12):
    return rf'\node[anchor=north west,inner sep=0pt,text width={w}mm,font=\fontsize{{{size}}}{{{size*1.25}}}\selectfont] at ({x},{y}) {{{s}}};'


def line(x, y, x2, y2):
    return rf'\draw ({x},{y})--({x2},{y2});'


def box(x, y, w, h, label='', size=12):
    return rf'\draw ({x},{y}) rectangle ++({w},{h});'+(t(x+2, y+2, label, w-4, size) if label else '')


def circle(x, y, r, label, size=10):
    return rf'\draw ({x},{y}) circle ({r});\node[font=\fontsize{{{size}}}{{{size+1}}}\selectfont] at ({x},{y}) {{{label}}};'


def card(x, y, seq, vid, w=36, h=51):
    out = box(x, y, w, h)+t(x+2, y+2, vid, w-4, 9)
    for i, c in enumerate(seq):
        yy = y+10+i*(h-10)/3
        out += line(x, yy, x+w, yy)+t(x+2, yy+2, ['1st', '2nd', '3rd'][i], 8, 8)+t(x+11, yy+1, c, max(w-13, 5), 15)
    return out


def cards(x, y, profile, w=36, h=51, gap=9):
    return ''.join(card(x+i*(w+gap), y, s, 'V'+str(i+1), w, h) for i, s in enumerate(profile))


def space(y, h=35):
    return box(18, y, 180, h)


def numberline(x, y, span=160, favs=None, proposals=None, small=False):
    out = line(x, y, x+span, y)
    for i in range(11):
        xx = x+span*i/10
        out += line(xx, y-1.5, xx, y+1.5)+t(xx-2, y+3, str(i), 6, 7 if small else 9)
    if favs:
        # Every favorite has the same 4 mm stem and its label 6 mm above it; voters who share a
        # favorite stack their labels 7 mm apart over that one stem. (Until October 23, 2026 the
        # stem height followed the voter number, so V3, the middle favorite, always stood tallest.)
        stacked = {}
        for i, f in enumerate(favs):
            k = stacked[f] = stacked.get(f, -1)+1
            xx = x+span*f/10
            out += (line(xx, y-6, xx, y-2) if k == 0 else '')+t(xx-4, y-12-7*k, 'V'+str(i+1), 10, 7 if small else 9)
    if proposals:
        for lab, f in proposals:
            xx = x+span*f/10
            out += box(xx-3, y+13, 6, 6)+t(xx-2, y+14, lab, 5, 7)
    return out


def tally(x, y, labels, groups, scale=1):
    out = ''
    for j, (lab, vs) in enumerate(zip(labels, groups)):
        xx = x+j*19*scale
        out += box(xx, y, 18*scale, 26*scale)+t(xx+1, y+1, lab, 16*scale, 7*scale)
        for k, v in enumerate(vs):
            out += circle(xx+(5+(k % 2)*8)*scale, y+(12+(k//2)*8)*scale, 3.1*scale, v, 5*scale)
    return out


# ---------------------------------------------------------------- page template

def page_preamble(week, topic, header, footer):
    return PRE


def page_open(page):
    return OPEN+t(18, 13, f'Week {page.week} / {page.topic} / {page.header}', size=10)+line(18, 21, 198, 21)


def page_close(page):
    return line(18, 262, 198, 262)+t(18, 266, f'Bellingham Math Circle / Week {page.week} / {page.footer}', size=9)+t(190, 266, str(page.number), 8, 9)+CLOSE+'\n'


def page_prompt(n, body, x, y, size):
    return t(18, y, rf'\textbf{{Problem {n}:}} '+body, 178, size or 12)


def page_text(x, y, body, w, size):
    return t(x, y, body, w or 178, size or 12)


# ---------------------------------------------------------------- the line launch (problems/05-line-rules.md)

def line_example():
    """One unchanged five-voter input (favorites 0, 1, 5, 8, 10; X = 2, Y = 8), every
    voter's distances and choice, then the complete tally."""
    s = t(18, 63, 'Fixed favorites; proposals X=2, Y=8', 99, 8)
    for i, f in enumerate([0, 1, 5, 8, 10]):
        yy = 79+i*8
        s += t(18, yy-3, 'V'+str(i+1), 10, 7)+line(30, yy, 110, yy)
        for j in range(11):
            s += line(30+8*j, yy-1, 30+8*j, yy+1)
        s += circle(30+8*f, yy, 3, 'V'+str(i+1), 5)
    s += numberline(30, 123, 80, small=True)
    s += box(43, 137, 6, 6)+t(44, 138, 'X', 5, 7)
    s += r'\draw (94,136)--(98,140)--(94,144)--(90,140)--cycle;'+t(92, 138, 'Y', 5, 7)
    s += t(119, 63, 'Distances to X / Y; choice', 79, 8)
    for i, (dx, dy, vote) in enumerate([(2, 8, 'X'), (1, 7, 'X'), (3, 3, 'Tie'), (6, 0, 'Y'), (8, 2, 'Y')]):
        s += t(121, 77+i*9, rf'V{i+1}: {dx} / {dy} $\to$ {vote}', 76, 9)
    s += tally(122, 127, ['X', 'Y', 'Tie'], [['V1', 'V2'], ['V4', 'V5'], ['V3']], 1.15)
    s += t(119, 162, 'Tied vote: 2 to 2; V3 in Tie.', 79, 9)
    return s


# ---------------------------------------------------------------- materials pages (not problem files)

def materials_tex(week=87, topic='Voting and agendas', level='Materials', ident='W87-M-v1'):
    """The five materials pages: fixed cards, tiles and tokens; two blank-card pages with
    letter slips; the tally and knockout mats; the five-lane favorite board."""
    P = []

    def page(content):
        n = len(P)+1
        P.append(t(18, 13, f'Week {week} / {topic} / '+level, size=10)+line(18, 21, 198, 21)+content+line(18, 262, 198, 262)
                 + t(18, 266, f'Bellingham Math Circle / Week {week} / {ident}', size=9)+t(190, 266, str(n), 8, 9))

    s = t(18, 29, r'Cut on outlines. Print at actual size (100\%).', size=11)+cards(25, 43, ['ABC', 'BCA', 'CAB'], 45, 80, 11)
    for i, a in enumerate('AABBCC'):
        s += box(21+i*29, 139, 28, 28, a, 23)
    for i in range(5):
        s += circle(34+i*35, 189, 9, 'V'+str(i+1), 13)
    s += line(23, 229, 123, 229)+line(23, 226, 23, 232)+line(123, 226, 123, 232)+t(23, 236, '100 mm scale check', 140, 10)
    page(s)
    for group in range(2):
        s = t(18, 29, 'Cut on outlines. One set of three blank ranking cards.', size=11)+cards(25, 48, ['   ']*3, 45, 80, 11)
        # supplemental letter strips for ordinary reusable slips; no count substitution for real cards
        for row in range(3):
            for col, a in enumerate('ABCABC'):
                s += box(25+col*27, 155+row*27, 21, 21, a, 19)
        page(s)
    s = t(18, 29, 'Keep these mats whole. Label the first two wells with the current option tiles, or with the separate X/Y tally labels for line votes.', size=11)
    s += box(23, 43, 170, 90)
    for j, lab in enumerate(['Option', 'Option', 'Tie']):
        xx = 25+j*55
        s += box(xx, 77, 54, 54)
        if j < 2:
            s += box(xx+12, 45, 30, 30, 'Option', 9)
        else:
            s += t(xx+2, 61, lab, 50, 9)
        for dx, dy in [(11, 11), (43, 11), (27, 27), (11, 43), (43, 43)]:
            s += circle(xx+dx, 77+dy, 9, '', 8)
    s += box(20, 147, 175, 100)
    # Every box holds the 28 mm tiles it needs with at least 2.5 mm to spare on each side; Out
    # holds the two losers side by side (it was a 29 mm column until October 23, 2026).
    s += box(25, 154, 61, 39, 'First pair', 9)+box(92, 154, 33, 39, 'Waiting', 9)+box(130, 154, 61, 39, 'Out', 9)
    s += box(25, 200, 33, 39, 'First winner', 9)+box(63, 200, 61, 39, 'Final pair', 9)+box(129, 200, 34, 39, 'Winner', 9)
    page(s)
    s = t(18, 29, 'Keep the board whole. Favorite markers stay on their own lanes; proposal markers go below the line.', size=11)
    # Board: five lanes precisely aligned to the 16mm tick spacing.
    for i in range(5):
        yy = 60+i*19
        s += t(18, yy-6, 'V'+str(i+1), 12, 8)+line(33, yy, 193, yy)
        for j in range(11):
            s += line(33+16*j, yy-2, 33+16*j, yy+2)
    s += numberline(33, 153, 160)+t(18, 173, 'Proposals X and Y', 180, 9)
    s += t(18, 184, 'Cut the pieces below. Keep proposals on the board while voting.', 180, 9)
    for i in range(5):
        s += circle(35+i*34, 203, 6.5, 'V'+str(i+1), 9)
    s += t(30, 217, 'Proposal markers', 85, 9)+t(126, 217, 'Tally labels', 68, 9)
    s += box(126, 227, 23, 23, 'X', 18)+box(162, 227, 23, 23, 'Y', 18)
    s += box(42, 229, 13, 13)+t(45, 230, 'X', 10, 12)
    s += r'\draw (90,226)--(99,235)--(90,244)--(81,235)--cycle;'+t(87, 230, 'Y', 10, 12)
    page(s)
    body = '\n\\newpage\n'.join(OPEN+p+CLOSE for p in P)
    return PRE+body+'\n\\end{document}\n'
